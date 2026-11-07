/* Standalone acceptance example. Both ledgers are disposable SQLite files.
   No network, account, AWE state, signing key or E0 database is used. */
import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import {mkdtempDisposableSync} from 'node:fs';
import {tmpdir} from 'node:os';
import path from 'node:path';
import {DatabaseSync} from 'node:sqlite';
import {fileURLToPath} from 'node:url';

const entry = fileURLToPath(import.meta.url);
const [mode, directory, fault] = process.argv.slice(2);
const opening = 'employer.example/req-42';
const owner = 'fixture-owner';
const subject = 'initial_application';

function openLedger(folder, name) {
  const db = new DatabaseSync(path.join(folder, name));
  db.exec('PRAGMA busy_timeout = 5000');
  return db;
}

function setup(folder) {
  const jobs = openLedger(folder, 'outbox.sqlite');
  jobs.exec(`CREATE TABLE outbox (
    owner TEXT, opening TEXT, action TEXT CHECK(action = 'initial_application'),
    status TEXT NOT NULL, evidence TEXT,
    PRIMARY KEY(owner, opening, action)
  )`);
  jobs.close();
  const mailbox = openLedger(folder, 'fake-provider.sqlite');
  // Deliberately no UNIQUE constraint on business/session key at the provider.
  mailbox.exec('CREATE TABLE sent (receipt INTEGER PRIMARY KEY, opening TEXT, recipient TEXT)');
  mailbox.close();
}

function attempt(folder, injection) {
  const jobs = openLedger(folder, 'outbox.sqlite');
  // Committed before the effect. A losing or recovering worker cannot send.
  const claim = jobs.prepare(`INSERT INTO outbox VALUES (?, ?, ?, 'SENDING', NULL)
    ON CONFLICT(owner, opening, action) DO NOTHING`).run(owner, opening, subject);
  if (!claim.changes) { jobs.close(); return; }
  if (injection === 'before-effect') process.exit(77);
  const mailbox = openLedger(folder, 'fake-provider.sqlite');
  const receipt = mailbox.prepare('INSERT INTO sent(opening, recipient) VALUES (?, ?)')
    .run(opening, 'jobs@employer.example').lastInsertRowid;
  mailbox.close();
  if (injection === 'after-effect') process.exit(77);
  jobs.prepare(`UPDATE outbox SET status = 'ACK', evidence = ? WHERE owner = ? AND opening = ? AND action = ?`)
    .run(String(receipt), owner, opening, subject);
  jobs.close();
}

function reconcile(folder) {
  const mailbox = openLedger(folder, 'fake-provider.sqlite');
  const rows = mailbox.prepare('SELECT receipt FROM sent WHERE opening = ? AND recipient = ?')
    .all(opening, 'jobs@employer.example');
  mailbox.close();
  const jobs = openLedger(folder, 'outbox.sqlite');
  const status = rows.length === 1 ? 'PROVIDER_CONFIRMED' : 'OUTCOME_UNKNOWN';
  jobs.prepare('UPDATE outbox SET status = ?, evidence = ? WHERE owner = ? AND opening = ? AND action = ?')
    .run(status, rows.length === 1 ? String(rows[0].receipt) : null, owner, opening, subject);
  const row = jobs.prepare('SELECT status, evidence FROM outbox').get();
  jobs.close();
  return {status: row.status, evidence: row.evidence, effects: rows.length};
}

function worker(folder, injection = 'none') {
  return new Promise((resolve, reject) => {
    const child = spawn(process.execPath, [entry, 'worker', folder, injection], {
      windowsHide: true, stdio: ['ignore', 'ignore', 'inherit']
    });
    child.once('error', reject);
    child.once('exit', (code, signal) => signal ? reject(Error(signal)) : resolve(code));
  });
}

async function scenario(injection, expectedEffects, expectedStatus) {
  const temp = mkdtempDisposableSync(path.join(tmpdir(), 'awe-audit-fixture-'));
  try {
    setup(temp.path);
    if (injection !== 'race') assert.equal(await worker(temp.path, injection), 77);
    const exits = await Promise.all([worker(temp.path), worker(temp.path)]);
    assert.deepEqual(exits, [0, 0]);
    const observed = reconcile(temp.path);
    assert.equal(observed.effects, expectedEffects);
    assert.equal(observed.status, expectedStatus);
    assert.equal(observed.evidence, expectedEffects ? '1' : null);
    console.log(JSON.stringify({scenario: injection, ...observed}));
  } finally {
    temp.remove();
  }
}

if (mode === 'worker') {
  attempt(directory, fault);
} else {
  assert.equal(mode, undefined);
  await scenario('race', 1, 'PROVIDER_CONFIRMED');
  await scenario('after-effect', 1, 'PROVIDER_CONFIRMED');
  await scenario('before-effect', 0, 'OUTCOME_UNKNOWN');
}
