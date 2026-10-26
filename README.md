# Retrospective Audit

[Русская версия](README.ru.md)

A portable Agent Skill for evaluating other Agent Skills against actual Codex Desktop task histories.

It helps detect drift between a written `SKILL.md` workflow and how work is
actually performed: skipped steps, repeated repair loops, manual corrections,
stale rules, missing stop-lines, and useful deviations that should be promoted
into the skill.

**Repository:** `SergejDAGDA/retrospective-audit-skill`.

**Installed Skill ID:** `retrospective-audit` (directory `skills/retrospective-audit/`, invocation `$retrospective-audit`). The GitHub-only `-skill` suffix is not part of the installed ID. The previous ID `retrospective-skill-audit` belongs to pre-migration releases; it is **not** a runtime alias.

**Package version:** `0.2.0`. Published GitHub Release and local installation must be verified independently. The supported retrospective evidence source is Codex Desktop task history; compatibility with other agents is not claimed as tested.

## What it does

- Reads the target `SKILL.md`.
- Finds relevant past Codex Desktop tasks.
- Shows candidate tasks before deep inspection.
- Waits for the user to approve the sample.
- Reads selected task histories.
- Decomposes the skill into a testable contract.
- Compares the contract with observed task behavior.
- Separates durable patterns from one-off exceptions.
- Produces recommendations and a patch plan.

The audit is read-only by default. It must not edit skills, files, Git state,
Codex tasks, or external systems until the user explicitly approves changes.

## When to use it

Use this skill after:

- 5-10 real uses of a skill;
- repeated manual corrections;
- repeated failed repair cycles;
- a noticeable process change;
- preparing a skill for a new release;
- deciding whether a skill is stable enough to keep as-is.

Avoid using it after only one atypical task. The skill treats fewer than three
independent examples as weak evidence, not a durable pattern.

## Repository layout

```text
.
├── LICENSE
├── README.md
├── README.ru.md
├── skills/
    └── retrospective-audit/
        ├── SKILL.md
        ├── VERSION
        ├── agents/
        │   └── openai.yaml
        └── references/
            └── report-template.md
```

## Installation

Install with Codex skill installation flow from this repository, or copy the
skill folder manually:

```powershell
Copy-Item -Recurse `
  .\skills\retrospective-audit `
  $env:USERPROFILE\.codex\skills\retrospective-audit
```

After installation, start a new Codex task so the skill list refreshes.

## Basic prompt

```text
Use $retrospective-audit.

Audit this skill in read-only mode:
<PATH_TO_SKILL.md>

First find relevant past Codex Desktop tasks, show candidate tasks, and wait for
my approval of the sample. Do not change files, Git, skills, Codex tasks, or
external systems.
```

## Skill Lab prompt

For a permanent chat dedicated to skill maintenance:

```text
This is my Codex Skill Lab.

Show my installed user skills from:
%USERPROFILE%\.codex\skills

If CODEX_HOME is set, use:
%CODEX_HOME%\skills

Separate user skills from system or third-party skills. For each skill, show:
name, purpose, path to SKILL.md, and whether it has agents/openai.yaml,
references, or scripts.

Do not change anything without separate approval.
If I choose a skill for audit, use $retrospective-audit.
If I approve edits after the audit, use $skill-creator to update the skill.
```

**Identity migration (from v0.1.1):** Previous versions used `$retrospective-skill-audit` and `skills/retrospective-skill-audit/`. Do not run both old and new IDs as simultaneous live skills. In the controlled installation stage, preserve the old payload as rollback evidence, install the new ID, verify discovery in a fresh Codex Desktop chat, and only then retire the old active directory. No automatic uninstall or file deletion is performed by this repository.

## Validation status

This skill can be checked structurally without access to task history. A full
behavioral validation requires real Codex Desktop tasks and a user-approved
sample. That limitation is intentional: the audit should be evidence-driven, not
simulated from expectations.

## Related skills

- `maintain-project-memory`: maintains durable project memory.
- `retrospective-audit`: maintains the quality of skills themselves.

Together they form a small organizational toolkit for project and process
continuity.

## License

MIT.
