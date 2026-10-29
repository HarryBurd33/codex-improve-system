# History reader update — 0.1.1

Oversized chat responses now have a bounded fewer-turn fallback, selective visible-message handling, explicit truncation and targeted expansion before findings. Existing scope, approval and rollback boundaries remain unchanged. No connector, crawler, runtime script, background monitor or expanded access is added.

Validation:

- Eight local package/rollback checks passed.
- The actual reader procedure encountered an oversized five-turn response and succeeded with one turn. Structured filtering kept the visible-message body to 8,019 characters, below the approximately 12,000-character batch guideline. It disclosed unread older pages and did not claim complete coverage.
- An image-only question source explicitly reported its missing attachment. No question contents or answer-accuracy findings were invented. Raw histories and source identifiers remain private.
- Only visible user/assistant messages were passed onward; unrelated reasoning blocks and incidental account fields were excluded. The procedure was executed in the current context, not an isolated blind model experiment. It does not establish universal behavior or long-term benefit.
- Source and user installation hashes are compared, and native user-scope discovery is checked after installation. Published contents are compared with a fresh immutable GitHub download.

The [original validation](VALIDATION.md) retains the original synthetic execution evidence, scope correction and limitations. This update does not change the three scope choices, individual approval, stale-target checks, private records or rollback process.

[Structured update results](../validation/v0.1.1.json) contain the source hashes and scoped check summary.
