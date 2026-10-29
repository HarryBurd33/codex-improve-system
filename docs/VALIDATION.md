# Validation — 0.1.0

Observed on 2026-10-28 (America/Denver). This is a bounded synthetic validation, not a claim of broad or long-term improvement efficacy.

| Evidence | Observed result | Limit |
|---|---|---|
| Local package tests | 8 passed: 6 structure/package checks and 2 executed Git inverse-merge checks | Structure and merge primitive behavior do not prove agent compliance. |
| Build-time metadata/link validation | Passed for all 5 installable files | Build helper is not a runtime requirement; this is not full YAML or native selection validation. |
| Actual model responses | 19 constrained-response cases meet the frozen observable checks; separate evaluator found no critical failure | One shared worker context, not 19 isolated contexts. Sparse descriptions appropriately request sources rather than fabricate findings. |
| Actual file exercises | Partial approval, stale application, clean rollback, conflict preservation, and edited-created-file rollback passed | Six initial target files independently match expected bytes; arbitrary concurrency and permission failures not exercised. |
| Repeat run | Rejected proposal retained its ID/rejection; no duplicate proposal or target edit | Synthetic private decision record, not unrestricted memory. |
| Evidence-to-proposal audit | Read three actual synthetic files, identified an existing rule/procedure conflict, and proposed an exact two-line project skill reorder without editing targets | Export runtime behavior and later benefit were explicitly unexecuted/unknown. |
| Multi-target stale proposal | Matching first target remained unchanged when second target was stale; revised content stayed proposed | Two actual fixture files checked, not an atomic transaction guarantee. |
| Independent resources review | Skill, history/change references and both templates consistent with the supplied contract | Static review only; one minor example wording correction applied. |

The 19 responses and initial file exercises used the first draft. A later native natural-language smoke test selected the skill but timed out after 150 seconds while inspecting setup before asking for scope. The final draft tightens that step to ask A/B/C immediately and return. An isolated native run with the same natural-language prompt returned the menu in 22.73 seconds; the initial explicit projectless run took 20.04 seconds. These timings are observations, not a speed guarantee or controlled comparison: the corrected draft used a project-scoped fixture while the initial draft used the user installation. Global configuration and permission policies stayed unchanged. Final affected-scope regressions and installed checks are recorded below.

Six direct-prompt baseline responses were produced before the execution worker read the target skill. The narrow observed difference was that the skill response listed all three A/B/C scope choices. The other paired baseline cases already respected their tested boundaries. Both phases shared the worker context; host instructions and fixture inputs were already known. This is nonblind evidence and cannot establish a causal or general performance gain. Effective worker model/effort were not exposed and remain unknown.

The [frozen cases](../tests/cases.json), [structured results](../validation/results.json), [literal skill responses](../validation/model-responses.json), [direct-prompt responses](../validation/direct-prompt-responses.json), [evidence-rich review](../validation/evidence-audit-response.txt), and [two-target stale response](../validation/multi-stale-response.txt) preserve the evidence. Public copies sanitize local paths and file identity; original and sanitized hashes are distinguished. Populated private bookkeeping records are excluded.

Native installation/discovery/invocation and publication checks are completed in the delivery note below before final delivery. Personal histories, full session logs, credential stores, paid APIs, background services and permission-policy changes were not part of testing.

## Delivery checks

Final source and global installation match on all five files. Native `skills/list(forceReload=true)` found exactly one enabled user-scope installation from both an unrelated Git project and a projectless directory. On Codex CLI 0.164.0, the final explicit `$improve-system` projectless invocation returned the A/B/C menu in 18.24 seconds; the exact natural-language example from a clean unrelated project returned it in 16.77 seconds before auditing setup/history. Both completed successfully using ChatGPT authentication, a read-only sandbox, and no model override. The three affected S01/S02/H03 regression responses also meet their unchanged expectations. See [native evidence](../validation/native-checks.json) and [final scope responses](../validation/candidate2-scope-responses.json).

Remote publication, visibility and saved topics are verified after the initial source push and recorded here before final delivery.

## Remaining limits

No actual history connector retrieval, complete-history coverage, slash alias, background hook/monitor, cloud/device propagation, arbitrary-host guarantee, or real-user outcome study is claimed. Automatic natural-language selection and instruction enforcement depend on the host/model. Examples are illustrations; the case table is declarative and is not itself a test runner.
