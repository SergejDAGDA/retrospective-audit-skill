# Retrospective Skill Audit

[Русская версия](README.ru.md)

A Codex skill for auditing another Codex skill against real Codex Desktop task
history.

It helps detect drift between a written `SKILL.md` workflow and how work is
actually performed: skipped steps, repeated repair loops, manual corrections,
stale rules, missing stop-lines, and useful deviations that should be promoted
into the skill.

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
└── skills/
    └── retrospective-skill-audit/
        ├── SKILL.md
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
  .\skills\retrospective-skill-audit `
  $env:USERPROFILE\.codex\skills\retrospective-skill-audit
```

After installation, start a new Codex task so the skill list refreshes.

## Basic prompt

```text
Use $retrospective-skill-audit.

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
If I choose a skill for audit, use $retrospective-skill-audit.
If I approve edits after the audit, use $skill-creator to update the skill.
```

## Validation status

This skill can be checked structurally without access to task history. A full
behavioral validation requires real Codex Desktop tasks and a user-approved
sample. That limitation is intentional: the audit should be evidence-driven, not
simulated from expectations.

## Related skills

- `maintain-project-memory`: maintains durable project memory.
- `retrospective-skill-audit`: maintains the quality of skills themselves.

Together they form a small organizational toolkit for project and process
continuity.

## License

MIT.
