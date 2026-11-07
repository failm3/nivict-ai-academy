import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {existsSync, readFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const audit = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
if (!process.argv[2]) throw Error('Pass the path to the original Sol worktree');
const original = path.resolve(process.argv[2]);
const finalDir = 'MASTER-INTEGRATION-01/MASTER02/FINALIZATION';
const packageDir = finalDir + '/COMPLETE-01';
const source = 'c53d1fb3606218a4f3961f37f57ebc41ac6681ef';
const seal = '3579aeeda379caf78dafe5351704956f1ecc0ea5';
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const read = (root, name) => readFileSync(path.join(root, name));
const json = name => JSON.parse(read(original, name));
const git = (...args) => execFileSync('git', ['-C', audit, ...args], {encoding: 'utf8', maxBuffer: 16 * 1024 * 1024});
const tree = new Map(git('ls-tree', '-rz', source).split('\0').filter(Boolean).map(line => {
  const [descriptor, name] = line.split('\t');
  return [name, descriptor.split(' ')[2]];
}));
const review = json(finalDir + '/CONTROLLER-REVIEW-05.json');
assert.equal(review.application_source_commit, source);
let missingInAudit = 0;
let exactSourceBlobs = 0;
for (const pin of review.sources) {
  const bytes = read(original, pin.path);
  assert.equal(hash(bytes), pin.sha256, pin.path);
  if (existsSync(path.join(audit, pin.path))) assert.equal(hash(read(audit, pin.path)), pin.sha256, pin.path);
  else missingInAudit++;
  const blob = createHash('sha1').update('blob ' + bytes.length + '\0').update(bytes).digest('hex');
  if (tree.get(pin.path) === blob) exactSourceBlobs++;
}
const integrity = json(finalDir + '/FINAL-COMPLETE-INTEGRITY-01.json');
const anchor = git('show', seal + ':' + finalDir + '/FINAL-COMPLETE-INTEGRITY-01.json');
assert.deepEqual(integrity, JSON.parse(anchor));
for (const root of [audit, original]) {
  for (const pin of [integrity.complete_checkpoint, integrity.report, integrity.package_manifest, integrity.package_result, integrity.native_proof_verification]) {
    assert.equal(hash(read(root, pin.path)), pin.sha256, pin.path);
  }
  const rows = read(root, packageDir + '/MANIFEST.sha256').toString().trimEnd().split(/\r?\n/);
  assert.equal(rows.length, 534);
  const listed = new Set();
  for (const row of rows) {
    const [, expected, name] = /^([0-9a-f]{64})  (.+)$/.exec(row);
    assert(name.startsWith(packageDir + '/') && !name.split('/').includes('..'));
    assert(!listed.has(name)); listed.add(name);
    assert.equal(hash(read(root, name)), expected, name);
  }
}
const result = json(packageDir + '/RESULT.json');
let linuxMetadata = 0;
for (const {original: from, preserved: to} of result.copies) {
  assert.equal(from.sha256, to.sha256);
  assert.equal(hash(read(original, to.path)), to.sha256, to.path);
  if (from.path.startsWith('/home/')) linuxMetadata++;
  else assert.equal(hash(read(original, from.path)), from.sha256, from.path);
}
const artifact = read(original, packageDir + '/result.txt');
assert.equal(artifact.length, 36);
assert.equal(hash(artifact), '98c0de0acc3d2ce1c21f174f5b34e5e9e52727136f362159e6cd78605772f5b1');
assert.deepEqual(artifact, read(original, 'MASTER-INTEGRATION-01/MASTER02/NATIVE-01/result.txt'));
console.log(JSON.stringify({source, seal, reviewPins: review.sources.length, exactSourceBlobs,
  missingInAudit, manifestEntriesPerTree: 534, portableCopies: result.copies.length,
  originalRelativeFiles: result.copies.length - linuxMetadata, linuxMetadataExportOnly: linuxMetadata,
  artifactBytes: artifact.length, artifactSha256: hash(artifact)}, null, 2));
