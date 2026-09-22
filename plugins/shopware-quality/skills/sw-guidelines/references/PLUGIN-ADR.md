# Shopware 6 plugin — the plugin's own ADRs

**ADR** = Architecture Decision Record. One file per decision, recording **why** something is the way it is.

**This is about the ADRs a plugin writes for itself** — its own `adr/` directory, its own decisions, maintained by
whoever works on the plugin. That is a different thing from the ADRs of the Shopware core team, which document binding
decisions of the platform and are only read, never written, by a plugin; those are in
[ADR-KNOWLEDGE.md](ADR-KNOWLEDGE.md) with the full index in
[ADR-KNOWLEDGE-ADR-INDEX.md](ADR-KNOWLEDGE-ADR-INDEX.md).

**An ADR is the place the prose comments go that ground rule 2 banishes from the code**
([PLUGIN-GROUND-RULES.md](PLUGIN-GROUND-RULES.md)).

## Contents

- [File name and location](#file-name-and-location)
- [The layout](#the-layout)
- [The three sections](#the-three-sections)
- [An accepted ADR is never edited](#an-accepted-adr-is-never-edited)
- [Which ADRs every plugin needs](#which-adrs-every-plugin-needs)
- [The table in CLAUDE.md](#the-table-in-claudemd)
- [When an ADR is written](#when-an-adr-is-written)

---

## File name and location

```
adr/YYYY-MM-DD-<title-in-kebab-case>.md
adr/_superseded/YYYY-MM-DD-<title>.md     # superseded ones
```

Examples:

```
adr/2026-09-21-everything-is-written-in-english.md
adr/2026-09-21-nothing-internal-to-shopware-is-used.md
adr/2026-09-22-one-task-at-a-time-without-a-todo-file.md
```

**The date comes first**, so that alphabetical order is also chronological order.

**The title is a sentence, not a heading.** Not `logging.md` but
`the-listing-survives-whatever-this-plugin-gets-wrong.md`. Whoever lists the directory then reads the decisions, not
merely their topics.

---

## The layout

```markdown
---
title: One task at a time, and mutation testing last, without a file to track it in
date: 2026-09-22
area: process
tags: [process, workflow, mutation, testing]
status: accepted
supersedes: 2026-09-22-one-task-at-a-time-and-mutation-testing-last.md
---

## Context

What the decision hangs on. What prompted it. What was measured.

## Decision

What holds. In the present tense, phrased as a rule.

## Consequences

What it costs. What it makes harder. What it does not excuse.
```

**The frontmatter field by field:**

| Field | Values | Purpose |
|---|---|---|
| `title` | a whole sentence | appears in the table in `CLAUDE.md` |
| `date` | `YYYY-MM-DD` | when it was decided |
| `area` | `core`, `storefront`, `administration`, `devops`, `process`, `documentation` | grouping |
| `tags` | list | findability |
| `status` | `accepted`, `superseded` | see below |
| `supersedes` | file name | only when this ADR replaces another |

---

## The three sections

**`## Context` — what it hangs on.**

This is where the measurements go. From a real ADR:

> Measured on a plugin list page before this was settled: the "Add" button stood at 32px against the language
> switch's 40px, and sat four pixels lower than the control it was aligned with.

**A number from an observation** is what separates an ADR from an opinion.

**`## Decision` — what holds.**

In the present tense, as a rule: "One task is finished before the next is started." Not "we should" or "it would be
good".

**`## Consequences` — what it costs.**

The most important section and the most often neglected. Here stands what the decision makes **worse**:

> A request that arrives mid-task and is not written into one of the four places above is lost when the session ends.
> That is the cost of having no catch-all file, and it is deliberate.

**An ADR without drawbacks in `Consequences` is incomplete.** Any decision that cost nothing was not a decision.

---

## An accepted ADR is never edited

**This is the most important rule of this file.**

A decision that no longer holds:

1. stays unchanged in content
2. moves to `adr/_superseded/`
3. gets its `status` set to `superseded`
4. gets a **new** ADR written, with `supersedes:` in the frontmatter and a link back in its `Context`

```markdown
## Context

set two rules that were right and stay right: …
```

**Why not simply change it:** an ADR documents **what was decided at a point in time, and why**. Rewrite it and the
reasoning is gone, and the code written under the old rule looks wrong without anyone being able to reconstruct why it
is as it is.

An ADR is a record, not a wiki article.

---

## Which ADRs every plugin needs

These are **generally applicable** and belong in every plugin, by content:

| ADR | What it records |
|---|---|
| **Everything is written in English, except the README** | ground rule 1 |
| **Annotation style** | complete DocBlock tags; the basis for the skip rules in Rector and php-cs-fixer |
| **Nothing internal to Shopware is used** | no `@internal`; the basis for the plugin's own package attribute |
| **Live shops decide what may change** | existing behaviour is untouchable as long as it is correct |
| **@throws is declared where it is known** | part of the annotation style, its own ADR because of the scope |
| **Test strategy: five levels, 100 percent, and the gate** | the whole testing and tooling setup in one decision |
| **An end-to-end test does what a person does** | the guiding principle for E2E |
| **End-to-end tests run against browserless** | the E2E runtime |
| **One task at a time** | the workflow, see [PLUGIN-WORKFLOW.md](PLUGIN-WORKFLOW.md) |
| **Every image is licence-free, documented, and marked when a machine made it** | image handling |

**Plugin-specific** on top of that: every decision about the plugin's own behaviour, about its relationship to other
plugins, and about presentation rules (such as *"Nothing in this plugin is small"*).

---

## The table in `CLAUDE.md`

Every ADR appears in a table in `CLAUDE.md`:

```markdown
| Decision | Area |
|---|---|
| Everything is written in English, except the README | core |
| Test strategy: five levels, 100 percent, and the gate | devops |
```

**Why the list and not just the directory:** whoever reads `CLAUDE.md` sees at a glance which decisions exist, without
opening a directory. And when an ADR moves to `_superseded/` it disappears from the table — the table only ever shows
what holds.

---

## When an ADR is written

**Immediately**, when a decision is taken that:

- is not obvious
- does not follow from the code
- would later make someone ask "why, actually?"
- is a deviation from what Shopware or the ecosystem usually does

**No ADR** for: self-evident things, things that are already in the code, one-off decisions without consequences.
