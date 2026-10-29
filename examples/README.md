# Synthetic examples

These are illustrations, not executed test results. All names, histories and preferences here are invented for demonstration.

**Current chat:** `$improve-system Review this chat for repeated verification failures.` The review lists inspected turns, checks whether the relevant procedure already exists, and proposes a scoped workflow fix only if evidence supports it.

**Cross-project:** `Review accessible chats across projects from the past two weeks.` The review discloses actual access, selects a bounded window, and distinguishes a project-specific export format from a repeated general preference for concise final answers.

**Approval:** Review proposes P001 (global brevity preference) and P002 (project export checklist). `Reject P001; apply P002.` Only P002 may change its reviewed target. A later unchanged run should retain the rejection rather than recreate P001 under another identifier.

**Weak evidence:** One ambiguous mistake can yield a qualified observation and no persistent change.

**Rollback:** After an approved checklist edit, another user adds an unrelated heading. Roll back only the checklist edit, preserving the new heading. A conflicting edit to the same lines requires reconciliation; no destructive overwrite.

The frozen synthetic case contract is in [tests/cases.json](../tests/cases.json); actual model outputs, when available, are reported separately from these authored examples.
