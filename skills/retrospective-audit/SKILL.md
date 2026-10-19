---
name: retrospective-audit
description: Audit an Agent Skill against real past Codex Desktop task history. Use when the user asks to backtest, retrospectively audit, evaluate, calibrate, improve, or compare a SKILL.md against how work was actually done across previous Codex tasks; when repeated manual corrections, repair loops, skipped steps, stale procedures, or process drift suggest the skill may no longer match real workflow. Work read-only until the user explicitly approves edits.
---

# Retrospective Audit

## Core rule

Run a read-only retrospective audit first. Do not edit the skill, project files,
Git state, Codex tasks, or external systems unless the user gives a separate
explicit approval after seeing the audit and patch plan.

This skill audits the skill process, not the project outcome. The goal is to find
where written instructions diverge from real Codex task behavior and whether the
divergence matters.

## Required workflow

1. Read the target `SKILL.md` completely.
2. Discover relevant past Codex Desktop tasks using available task/thread tools.
   Prefer full task history over titles, previews, summaries, or memory.
3. Present candidate tasks before deep reading:
   - title;
   - date, when available;
   - short relevance reason;
   - include/exclude recommendation.
4. Stop for user agreement on the sample unless the user already gave a specific
   task list.
5. After approval, read the selected tasks fully, including paginated or older
   turns when available.
6. Decompose the target skill into a testable contract.
7. Compare each selected task against that contract.
8. Separate durable patterns from one-off exceptions.
9. Produce recommendations and a patch plan only. Do not apply it.

If task-history access is unavailable or incomplete, say so directly. Do not
infer missing evidence from project memory, summaries, titles, previews, or user
expectations.

## Evidence rules

- Use memory only to find candidate tasks, not to prove conclusions.
- Base conclusions on the actual task history whenever possible.
- Treat manual actions outside Codex as invisible unless the history records
  them.
- Do not call a deviation a skill defect by default. First evaluate whether it:
  - improved the result;
  - caused an error, rework, or repair loop;
  - was an intentional exception;
  - came from a task-specific constraint;
  - protects against a rare but expensive risk.
- Call a pattern durable only when it appears in at least three independent
  relevant tasks.
- Mark weaker signals as hypotheses or exceptions.

## Skill contract decomposition

Extract these checkable elements from the target skill:

- trigger conditions: when the skill should activate;
- expected inputs: files, paths, approvals, task history, repo state, or user
  decisions it expects;
- ordered workflow: required steps and sequencing;
- checks and stop-lines: validations, approvals, read-only boundaries, and
  escalation points;
- completion criteria: what counts as done;
- outputs: expected files, reports, diffs, proposals, commits, or releases;
- optional branches: conditions under which references, scripts, tools, or
  external systems are used.

Keep this contract compact. Quote only short fragments when needed.

## Per-task comparison labels

For each selected task, mark contract items as:

- followed;
- skipped;
- reordered;
- repeated;
- added outside the skill;
- required manual correction;
- caused rework or repair cycle;
- impossible to determine from history.

Capture concise evidence for each non-trivial label: task title/date, relevant
turn summary, and observed consequence.

## Final report

Use the five-section report structure from
`references/report-template.md`.

For every recommendation include:

- concrete skill rule or fragment;
- tasks supporting the finding;
- observed evidence;
- expected effect;
- confidence: high, medium, or low;
- proposed wording for the change.

End with a compact patch plan. The plan may name files and sections to change,
but must not be applied during the audit turn.

## Stop-lines

Stop and ask the user before:

- reading a very large number of tasks when a smaller representative sample is
  available;
- using external systems beyond Codex task history and local files;
- changing any files;
- committing, pushing, publishing, installing, or uninstalling anything;
- treating fewer than three examples as a durable pattern.

If the user asks to proceed directly to edits, still summarize the evidence and
patch plan first, then apply only the approved changes.
