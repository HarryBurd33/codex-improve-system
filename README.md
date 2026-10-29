# improve-system for Codex

Review selected interactions, identify recurring friction, and propose small, evidence-backed improvements to instructions, existing skills, and reusable workflows. Works with coding and noncoding tasks, including projectless chats where the host supports skills.

This changes the working instructions and resources available to Codex. It does not retrain a model, provide unrestricted memory or complete history access, or guarantee instruction enforcement.

## Invoke

```text
$improve-system
$improve-system Review accessible chats across projects from the past two weeks.
Review our recent interactions and improve my Codex setup.
Find recurring mistakes and propose changes to my skills.
Improve our working process based on these conversations.
```

Explicit `$improve-system` invocation and natural-language matching are supported skill mechanisms. Automatic matching depends on the host/model. `/improve-system` and `/improve system` are not implemented or tested aliases. An ordinary bug report, one correction, or a conceptual question should not start an audit.

If scope is missing, the skill asks you to choose:

- **A — Current chat and active project.** In a projectless chat, review the current chat alone.
- **B — Recent chats related to the active project.** Requires an identified project.
- **C — Recent accessible chats across projects.** Separates project conventions from general working agreements.

An explicit scope is honored without asking again. Proposed default for “recent”: the last 14 days, up to 20 relevant accessible chats, initially up to 10 recent turns per chat. The review reports the actual selection, truncation, pagination and gaps; these caps never establish exhaustive coverage. Explicit user limits control.

## What happens

1. Discover available file/history tools, inventory the sources actually reviewed, and disclose access limits. Without history tools, use the current chat and selected supplied transcripts or exports; broader coverage remains partial.
2. Link findings to inspected evidence. Separate observations, hypotheses, tool/environment failures, isolated errors, and successful practices worth preserving.
3. Inspect existing instructions and skills. Investigate an ignored rule before adding a duplicate. Prefer a project rule for a local convention, an existing skill for its procedure, and no persistent change for weak evidence.
4. Present a manageable prioritized set of proposals. Each has a stable ID, evidence, exact target paths and scope, a diff or full new content, tradeoffs, meaningful verification, and rollback.
5. Wait for individual approval. “Apply proposals 1 and 3” authorizes only those reviewed changes. Rejection and revision are equally valid. Before application, compare all targets with their reviewed snapshots; material changes require renewed review.
6. Verify actual edits and record what was applied, verified, rejected, or rolled back. A later audit can assess outcomes. Approval and a successful write are not proof that an improvement helped.

Historical conversations are evidence, not instructions or permissions. The skill does not run commands found in them. It does not inspect credential stores, modify historical logs, weaken permission policies, enable paid services, or install background monitoring.

## Install one user-level copy

Requires a Codex host with local skill support. The skill itself requires file/diff tools for changes; Python is only used by the validation suite. Git is optional for a three-way rollback merge. Desktop chat tools are optional. Skill Forge is not required.

[Current official documentation](https://learn.chatgpt.com/docs/build-skills) identifies `~/.agents/skills` as the user skill root. Review the source first, then from a local clone:

```sh
git clone https://github.com/HarryBurd33/codex-improve-system.git
cd codex-improve-system
python3 -m unittest discover -s tests -v
mkdir -p ~/.agents/skills
test ! -e ~/.agents/skills/improve-system && test ! -L ~/.agents/skills/improve-system && test ! -e ~/.codex/skills/improve-system && test ! -L ~/.codex/skills/improve-system && cp -R skills/improve-system ~/.agents/skills/improve-system
```

If a same-name copy already exists, inspect and preserve it first. Check other repository/admin/plugin locations if the host reports duplicates. Do not add both a repository-local and user-level installation for routine use. The installable folder is `skills/improve-system`, not the entire repository.

Codex detects skill changes automatically according to current documentation. If discovery does not update, restart Codex and open a new chat. Verify in the skill selector or through the host's supported skill-listing interface from an unrelated directory. User-level installation applies to this user's local host/profile; it does not install on other devices, accounts, containers, cloud environments, or hosts without compatible discovery. A projectless UI chat still needs host support and tools.

## Private review records

Choose a private writable location outside repositories, the installed skill, and distributable archives. The skill proposes `~/.local/state/codex-improve-system/` on local hosts; use another accessible private location when unavailable. Project records stay partitioned by stable project identity. A narrower audit must not silently consult records from other scopes.

Store minimal evidence references, reviewed snapshots required for rollback, proposal decisions, and verification/outcome notes. Private bookkeeping does not itself change Codex's behavior. Avoid raw transcripts and secrets; do not publish the record directory. Use the supplied [record](skills/improve-system/templates/record.json) and [review](skills/improve-system/templates/review.md) as structures, not historical evidence or permissions. A later chat must actually have access to the record to use it.

## Update, uninstall, and rollback

For an update, fetch the desired revision, inspect the diff, back up the installed folder to a private directory outside all skill discovery roots, and compare it with the previously installed revision. Merge any personal customizations deliberately. Replace only after review and validation. Keep the old version until discovery and relevant behavioral checks pass. Do not overwrite an unknown or customized copy with `cp -R`.

To uninstall, move `~/.agents/skills/improve-system` to a private backup outside skill roots, then verify it disappears from discovery. Keep private review records if you need change history. Removing this skill does not undo improvements previously approved and applied to other files.

To roll back the skill installation, restore that preserved folder and verify discovery. To roll back a specific approved improvement, follow [the change procedure](skills/improve-system/references/changes.md): compare the applied snapshot with the current target, reverse only that proposal, preserve intervening edits, and refuse conflict overwrites. New files that acquired unrelated edits must not simply be deleted.

## Examples and validation

[Examples](examples/README.md) use synthetic material. [Current validation](docs/UPDATE-0.1.1.md) distinguishes static checks, deterministic file exercises, actual model responses, illustrations, and unavailable checks. [Research](docs/RESEARCH.md) records source coverage and reuse rights. Run local checks with:

```sh
python3 -m unittest discover -s tests -v
```

On-demand only. Scheduling, lifecycle hooks, and additional aliases require a separate request and verified support.

MIT for original work. See [LICENSE](LICENSE) and [CHANGELOG](CHANGELOG.md).
