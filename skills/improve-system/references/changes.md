# Reviewed changes and private records

This is a cooperative file-editing procedure, not a security boundary or an atomic
transaction engine. Use available native tools. No helper can manufacture user
approval, permission, a valid source, or proven improvement.

## Private review state

Keep records outside installed skills, source repositories, and public packages.
Use a user-chosen private directory or, when supported,
`~/.local/state/codex-improve-system/<scope-key>/<review-id>/`. Separate project/chat
scope keys; do not treat a shared directory as permission to inspect every record.
Set private directory/file permissions where available. If storage cannot be saved,
say so and return a minimal saveable record; do not claim durable memory.

Store only what supports decisions and rollback: scope/window, inspected source
pointers, proposal fingerprints/IDs, precise reviewed versions, user decisions,
checks, necessary before/after content, and later outcome evidence. Avoid raw full
transcripts. Before/after instruction content can itself be private. Do not publish
it. The JSON template is a starting record shape, not a script or hidden database.

Choose stable IDs such as `P-001` within a stable review ID. Derive a fingerprint
from normalized intervention, target owner/path, intended behavior, and scope;
do not rely on display number alone. Reuse the ID/fingerprint when revisiting the
same intervention. Record rejected IDs/fingerprints and reason; unchanged evidence
must not endlessly regenerate them under new IDs. Materially new evidence may
justify reopening, with an explicit reason and a new reviewed version.

Private administrative records do not authorize behavior changes. The audit may
save its own proposed/rejected decision metadata, but proposed target content must
not be installed, loaded as instructions, or treated as an approved preference.

## Review snapshots and approval

For each target resolve an exact path and project/global owner. Read applicable
instructions and inspect existing skills. Record:

- whether it existed (`exists`), its file identity/type, and a SHA-256 of exact bytes;
- private before content for rollback, or a distinct `missing` sentinel for a new file;
- the proposed diff/new content, its content hash, and a reviewed proposal version;
- intended file mode/encoding where a change would matter;
- the evidence, scope, tradeoffs, checks, and rollback method shown to the user.

Zero-length existing content has the SHA-256 of empty bytes and `exists: true`.
It must never be confused with `exists: false`/`missing`. Reject or reconcile
symlinks, changed file types, unexpected path resolution, and inaccessible files;
do not follow a newly substituted link to write somewhere else.

Approval must come from the current user and identify reviewed proposals/versions.
Resolve partial selections unambiguously. Rejections and revisions are separate
decisions; a changed revision starts proposed. Saved/historical approvals do not
authorize new changes. Self-edits use the same process.

## Apply protocol

1. Confirm current authority, approved IDs/versions, allowed paths, and meaningful
   verification. Ensure before snapshots/records were actually saved or disclose
   the rollback limitation before relying on them.
2. Re-read **all** targets of each approved proposal and compare exact existence,
   bytes/hash, type, and resolved identity with the reviewed state before writing
   any of that proposal. Verify any shared targets across proposals are compatible.
3. If anything changed, preserve current content and do not blindly apply the old
   patch. Show a reconciled diff against current state. Obtain renewed approval
   for material changes to content, effect, scope, or conflict resolution. A harmless
   reconciliation may retain approval only if its approved effect is unchanged
   and that equivalence is explained; uncertain cases remain unapplied.
4. Apply only approved paths/hunks with native edit/patch tools. Recheck immediately
   before each write; use a supported expected-hash/conditional-write mechanism
   when available. Never claim these checks eliminate all concurrent-write races.
   Preserve file modes/encoding and unrelated content. Do not run shell text taken
   from evidence or stored records as a command.
5. Read back actual files and inspect diffs/hashes. Run the stated focused checks;
   record actual outputs and unavailable checks. Mark the proposal applied only
   for changes that really occurred, verified only for the checks that passed.
6. If a multi-target application fails halfway, stop, record exactly which targets
   changed, and report partial application. Preserve remaining targets. Reconcile
   or reverse only already approved/applied changes; do not label it atomic or
   silently widen the repair.

Use events with time, actor/source, proposal version, and evidence pointers:
`proposed` → `approved` or `rejected`; `approved` → `applied`; `applied` → `verified`
only after stated checks pass; `applied`/`verified` → `rolled_back` after a verified
reverse change. Keep the events and per-target outcomes. Failed checks remain
failed; “applied” is not “verified.” A later assessment of benefit is separate.

## Rollback without losing later edits

A current request to roll back an identified proposal authorizes reversing that
recorded change. Confirm target identity and private before/applied snapshots.
Read current content before choosing the inverse:

- **Current exactly equals applied:** restore that proposal's before state, subject
  to any later dependent approved changes. Do not remove a dependency unnoticed.
- **Current differs:** compute an inverse patch/three-way merge in temporary files.
  With Git, `git merge-file -p CURRENT APPLIED BEFORE` uses the applied version as
  the common base and the before version as the change to merge into current.
  Supply independently verified literal file paths; do not evaluate stored shell.
  Capture candidate output without writing it into the live target.
- **Clean inverse:** inspect the candidate diff to confirm it reverses only the
  proposal and preserves unrelated changes. Recheck the live target has not moved,
  then write, read back, and verify the result.
- **Conflict/error:** leave the live target intact. Present the conflict and a
  reviewable resolution; request a decision if resolving it changes unrelated or
  dependent work. Do not write conflict markers into a live instruction file.
- **Created file:** delete only when its current bytes/type match the recorded
  applied file and no later dependency requires it. If edited, retain it and
  reconcile the owned content. A new empty file is still a created file.

Without Git, inspect/apply a minimal inverse patch using available tools. If safe
reversal cannot be established, preserve current and snapshots and disclose the
specific manual reconciliation needed. Never restore a whole snapshot over later
edits merely because it is convenient. Record rollback verification separately
from later behavior; keep enough history to explain the reversal.

## Assess later benefit

On a later in-scope review, compare similar triggers/task types before and after
the intervention, including counterexamples and changed tools/environment. Use
`unknown`, `helped`, `no_clear_change`, or `worsened` with observed evidence and
limits. A saved rule, user approval, one successful task, or passing format check
alone does not prove a general improvement. Propose any further change through
the same review and approval boundary.
