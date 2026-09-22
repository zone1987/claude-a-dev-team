# Shopware 6 plugin — `CLAUDE.md`, `CONTEXT.md`, and the `TODO.md` rule

Three files that answer one question together: **what is documented where**. `CLAUDE.md` says what holds,
`CONTEXT.md` carries unfinished work across a break, and there is deliberately no general task file. Reasons go into
an ADR ([PLUGIN-ADR.md](PLUGIN-ADR.md)).

## Contents

- [CLAUDE.md](#claudemd)
  - [The layout](#the-layout)
  - [What belongs in each section](#what-belongs-in-each-section)
  - [Under 200 lines](#under-200-lines)
  - [It is maintained continuously](#it-is-maintained-continuously)
- [CONTEXT.md](#contextmd)
  - [Purpose](#purpose)
  - [What belongs in it](#what-belongs-in-it)
  - [The maintenance rules](#the-maintenance-rules)
  - [It is gitignored](#it-is-gitignored)
  - [When it goes away](#when-it-goes-away)
- [TODO.md](#todomd)

---

# `CLAUDE.md`

The plugin's rulebook. It sits in the root and is the file read at the start of every session.

## The layout

```markdown
# <PLUGIN-NAME>

One or two sentences: what the plugin does.

**It runs in several live shops.** Namespace, vendor, table prefix, log channel.

## Commands
## Architecture
## Code style
## Rules
## Decisions
## Traps already paid for
## Done means
```

## What belongs in each section

**Head:** what the plugin is, in two sentences. Plus the identifiers needed constantly:

```markdown
**It runs in several live shops.** Namespace `<PLUGIN-NAMESPACE>`, vendor
`<PACKAGE-NAME>`, table prefix `<TABLE-PREFIX>`, log channel `<LOG-CHANNEL>`.
```

**`## Commands`:** the commands actually used — half a sentence per line saying what they do. Not all of them, just
the ones needed daily.

**`## Architecture`:** three to five sentences about the structure, plus the one thing you must know in order to break
nothing.

**`## Code style`:** the style rules no tool enforces, or that have to be held in mind while writing.

**`## Decisions`:** the table of all ADRs ([PLUGIN-ADR.md](PLUGIN-ADR.md)).

**`## Rules`:** what to do and what to leave alone. One bullet per rule, starting in bold.

**`## Traps already paid for`:** the most valuable section. Every trap that has already cost time, as a paragraph:
**the symptom in bold**, then the cause and the fix.

**`## Done means`:** one sentence listing what must be satisfied.

## Under 200 lines

**The file is read at every session.** What is too long gets skimmed, and what gets skimmed has no effect.

**What does not belong in it:**

| What | Where instead |
|---|---|
| Reasons | ADR |
| Interim states | `CONTEXT.md` |
| Complete configurations | the configuration file itself |
| What the plugin does for the operator | `README.md` |
| Changes | `CHANGELOG.md` |
| Security policy | `SECURITY.md` |
| Upgrade notes | `UPGRADE-<SHOPWARE-NEXT>.md` |

**The rule behind it:** `CLAUDE.md` says **what holds**. The linked files say **why**.

## It is maintained continuously

**Every trap that has cost time goes into the `Traps` section** — immediately, not later. Every new rule goes into
`Rules`. Every new ADR goes into the table.

**A change to `CLAUDE.md` interrupts the running task** and is carried out at once. It is the sole exception to the
rule that a mid-task request is noted but not followed ([PLUGIN-WORKFLOW.md](PLUGIN-WORKFLOW.md)).

**A wrong note in `CLAUDE.md` is worse than no note.** That has actually happened: a sentence about stub repositories
that was not true cost five percentage points of mutation score. What stands there is believed.

---

# `CONTEXT.md`

The knowledge and status collection kept **during** development.

## Purpose

After a `/compact` or in a new session, work must be able to continue seamlessly from `CONTEXT.md` alone — without
loss of knowledge.

## What belongs in it

- the current task and its goal
- verified facts **with evidence** (command, output, file, line)
- decisions taken **with reasoning**
- changes made, with exact file paths
- the precise verification state: what is green, what is red
- the currently unresolved symptom and the next hypothesis
- the next concrete step

**Very precisely:** selectors, snippet keys, routes, file and line references, commands, root-cause hypotheses with
evidence.

## The maintenance rules

| When | What |
|---|---|
| **Before every task** | read it — even for apparently small changes |
| **After every task** | log entry: what, where, how, when, verification state, open points |
| **At 90 %, 95 % and 98 % context usage** | rewrite it completely, the whole current state |

**Never shorten it to save space.** Length is irrelevant — 50,000 lines is fine. Completeness and precision take
priority. Finished items are marked "done", not deleted.

## It is gitignored

```gitignore
/CONTEXT.md
```

**Why it is not committed:** it is working state, not a result. What should survive it moves to its proper place at
the end of the task:

| Content | Destination |
|---|---|
| a decision | ADR |
| a trap | `CLAUDE.md`, section `Traps` |
| a behavioural change | `CHANGELOG.md` |
| a rule | `CLAUDE.md`, section `Rules` |

## When it goes away

**When the plugin is finished.** A file whose purpose is to carry unfinished work across a break describes nothing
once there is no unfinished work.

A status document nobody maintains is worse than none: it asserts something that was once true — with the authority
of a checked-in file.

**At the next larger piece of work it is created again.**

---

# `TODO.md`

**There is no general task file, and none is created.**

That is a deliberate decision, recorded in `adr/YYYY-MM-DD-one-task-at-a-time-without-a-todo-file.md`.

## Where a request goes instead

A request arriving in the middle of a task is **noted but not followed**. The running task runs to its commit.
Afterwards:

| The request is | It goes |
|---|---|
| a decision about how things work | into a new ADR |
| a change to the working rules | into `CLAUDE.md` |
| a behavioural change visible to the operator | into `CHANGELOG.md` |
| work to be done next | into the reply — and then it is done |

## Why no catch-all file

**The price stands in the ADR itself:**

> A request that arrives mid-task and is not written into one of the four places above is lost when the session ends.
> That is the cost of having no catch-all file, and it is deliberate: it forces the question "where does this belong?"
> at the moment the request arrives, rather than letting a list absorb everything and decay.

A catch-all file absorbs everything, and everything it absorbs decays. Answering "where does this belong?" at the
moment the request arrives is less comfortable and puts the knowledge where someone will find it.

## When a TODO file is right after all

**As a work list inside a single, large task** — created at the start, removed at the end.

**The difference from the forbidden catch-all file:** this list has a defined end point. It describes a task, not a
state.

## `TODO` and `FIXME` in the code

Forbidden in **JavaScript**, enforced by ESLint:

```js
'no-warning-comments': ['error', { location: 'anywhere' }],
```

Allowed in **PHP**, but only with a concrete reference:

```php
// TODO: replace once P-12 lands
```

A `TODO` without a reference to something traceable is a note to nobody.
