# Shopware 6 plugin: the plugin's own ADRs

**ADR** = Architecture Decision Record. One file per decision, recording **why** something is the way it is.

**Plugin ADRs are written in German** (every Markdown file of a plugin is German, see ground rule 1). The keys of the frontmatter and the values of `area` and `status` stay English because tools read them, and the section headings below are shown in English here as the English source of the German `Kontext`, `Entscheidung` and `Konsequenzen`.

**This is about the ADRs a plugin writes for itself**, its own `adr/` directory, its own decisions, maintained by
whoever works on the plugin. That is a different thing from the ADRs of the Shopware core team, which document binding
decisions of the platform and are only read, never written, by a plugin; those are in
[ADR-KNOWLEDGE.md](ADR-KNOWLEDGE.md) with the full index in
[ADR-KNOWLEDGE-ADR-INDEX.md](ADR-KNOWLEDGE-ADR-INDEX.md).

**An ADR is the place the prose comments go that ground rule 2 banishes from the code**
([PLUGIN-GROUND-RULES.md](PLUGIN-GROUND-RULES.md)).

## Contents

- [Both are mandatory](#both-are-mandatory)
- [Why not comments](#why-not-comments)
- [File name and location](#file-name-and-location)
- [The layout](#the-layout)
- [The three sections](#the-three-sections)
- [An accepted ADR is never edited](#an-accepted-adr-is-never-edited)
- [Which ADRs every plugin needs](#which-adrs-every-plugin-needs)
- [The table in CLAUDE.md](#the-table-in-claudemd)
- [ADRs are binding](#adrs-are-binding)
- [When an ADR is written](#when-an-adr-is-written)
- [A worked example](#a-worked-example)

---

## Both are mandatory

Every plugin has an `adr/` directory and a `CONTEXT.md` in its root. The standard forbids prose comments in code and then repeatedly says "the reasoning goes into an ADR or `CONTEXT.md`". This file says what an ADR is, so that instruction is actionable ([PLUGIN-CLAUDE-MD.md](PLUGIN-CLAUDE-MD.md) covers `CONTEXT.md`).

## Why not comments

A paragraph explaining why sits next to code that changes. The code moves, the paragraph stays, and within a few releases the file carries a confident explanation of something no longer true, with the authority of being right there in the source.

An ADR is dated and reviewed as a decision. `CONTEXT.md` is read at the start of every session. A test name **fails** when the rule it states stops holding. All three are places that something checks, a comment is not.

---

## File name and location

```
adr/YYYY-MM-DD-<title-in-kebab-case>.md
adr/_superseded/YYYY-MM-DD-<title>.md     # superseded ones
```

Examples:

```
adr/2026-09-21-code-is-english-markdown-is-german.md
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

**`## Context`, what it hangs on.**

This is where the measurements go. From a real ADR:

> Measured on a plugin list page before this was settled: the "Add" button stood at 32px against the language
> switch's 40px, and sat four pixels lower than the control it was aligned with.

**A number from an observation** is what separates an ADR from an opinion.

**`## Decision`, what holds.**

In the present tense, as a rule: "One task is finished before the next is started." Not "we should" or "it would be
good".

**`## Consequences`, what it costs.**

The most important section and the most often neglected. Here stands what the decision makes **worse**:

> A request that arrives mid-task and is not written into one of the four places above is lost when the session ends.
> That is the cost of having no catch-all file, and it is deliberate.

**An ADR without drawbacks in `Consequences` is incomplete.** Any decision that cost nothing was not a decision.

**Context states the question and the defensible alternatives.** An ADR that opens with the answer is a note, not a record: the value is in showing that the decision was a choice.

**Decision is the ruling,** in the imperative, with the specifics: numbers, operators, directions of rounding.

**Consequences is what this costs,** stated openly, including what someone will reasonably expect and not get. This section is what stops the decision from being quietly reversed by the next person who finds it inconvenient.

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

Editing an accepted ADR destroys the thing it is for: knowing what was decided when, and on what basis. A superseded ADR stays readable, because the question "why did we ever do it that way" has an answer that matters.

---

## Which ADRs every plugin needs

The cross-cutting ADRs of a plugin follow the rule book [PLUGIN-RULES.md](PLUGIN-RULES.md), the English source of the decisions that hold in every plugin (eight chapters, each decision once). A plugin writes them as German ADRs in its own `adr/` directory. The list below is the minimum, the rule book is the full set:

| ADR | What it records |
|---|---|
| **Code is English, every Markdown file is German** | ground rule 1 |
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
| Code is English, every Markdown file is German | core |
| Test strategy: five levels, 100 percent, and the gate | devops |
```

**Why the list and not just the directory:** whoever reads `CLAUDE.md` sees at a glance which decisions exist, without
opening a directory. And when an ADR moves to `_superseded/` it disappears from the table, the table only ever shows
what holds.

---

## ADRs are binding

An ADR is not a historical note. **Code that contradicts an accepted ADR is wrong, even when it works.** Read the ADR before touching the area it governs. When an ADR and a `CLAUDE.md` disagree, the ADR wins and `CLAUDE.md` gets corrected.

List the ADRs in `CLAUDE.md` as a table of decision and area, so the set is visible without opening the directory.

---

## When an ADR is written

**Immediately**, when a decision is taken that:

- is not obvious
- does not follow from the code
- would later make someone ask "why, actually?"
- is a deviation from what Shopware or the ecosystem usually does

**An ADR is written for anything a later reader would otherwise undo by accident:**

- a rule with defensible alternatives (which tier wins, where a threshold is measured)
- a deviation from what Shopware or a reference plugin does, **with the numbers**
- a tool chosen over an obvious competitor, and why
- a limitation accepted on purpose
- a rejection, so it is not re-proposed every six months

**Rejections are records too.** "Pest was evaluated and not adopted", with the reasoning, saves the same argument being had annually.

**No ADR** for: self-evident things, things that are already in the code, one-off decisions without consequences. How a class works is said by the code, and what a method returns is said by the signature. An ADR that restates the implementation rots exactly like the comment it replaced.

---

## A worked example

```markdown
---
title: The highest reached tier wins, once
date: 2026-09-11
area: checkout
tags: [discounts, cart, rounding]
status: accepted
---

## Context

With tiers at 250 EUR, 500 EUR and 1000 EUR, a cart of 600 EUR has passed two of them. What does it get?

Three readings are defensible: the highest reached tier alone (10 %), every reached tier summed (15 %), or each tier applied to the amount within its band. The customer's wording reads naturally as the first, but naturally is not a specification.

## Decision

**The highest tier whose threshold the cart has reached, applied once.** A cart of 600 EUR gets 10 %, not 15 %.

**The comparison is `>=`.** "From 500 EUR" means from 500 EUR inclusive.

**Rounding is towards zero.** A 5 % discount on 24.99 EUR is 1.2495 EUR, granted as 1.24 EUR.

## Consequences

Summing tiers is the reading a merchant might expect, and they will not get it. The configuration screen has to say so.

Rounding towards zero means a shopper is always a fraction of a cent worse off. Over a single cart this is invisible. It is stated here so nobody "fixes" it into banker's rounding later and quietly changes every discount in every shop.
```

The superseding ADR links back in its `Context`, for example: "The earlier decision had this plugin compute and apply the discounts itself. That was taken before it was established that a merchant can express the same thing as a normal Shopware promotion with a cart rule." Its frontmatter carries `supersedes: _superseded/2026-09-11-discount-tiers-belong-to-this-plugin.md`.
