# ADRs and CONTEXT.md — where reasoning lives

This standard forbids prose comments in code and then repeatedly says "the reasoning goes
into an ADR or `CONTEXT.md`". This file says what those are, so that instruction is
actionable.

**Both are mandatory.** Every plugin has an `adr/` directory and a `CONTEXT.md` in its
root.

## Why not comments

A paragraph explaining *why* sits next to code that changes. The code moves, the paragraph
stays, and within a few releases the file carries a confident explanation of something no
longer true — with the authority of being right there in the source.

An ADR is dated and reviewed as a decision. `CONTEXT.md` is read at the start of every
session. A test name **fails** when the rule it states stops holding. All three are places
that something checks; a comment is not.

## ADRs

One markdown file per decision, in `adr/`, named `YYYY-MM-DD-descriptive-title.md`:

```
adr/
├── 2026-09-09-annotation-style.md
├── 2026-09-11-highest-reached-tier-wins.md
├── 2026-09-11-test-strategy.md
└── _superseded/
    └── 2026-09-11-discount-tiers-belong-to-this-plugin.md
```

### The shape

Metadata as bold lines, then exactly three sections:

```markdown
# The highest reached tier wins, once

**title:** The highest reached tier wins, once  
**date:** 2026-09-11  
**area:** checkout  
**tags:** [discounts, cart, rounding]  

## Context

With tiers at 250 €, 500 € and 1000 €, a cart of 600 € has passed two of them. What does it
get?

Three readings are defensible: the highest reached tier alone (10 %), every reached tier
summed (15 %), or each tier applied to the amount within its band. The customer's wording
reads naturally as the first, but naturally is not a specification.

## Decision

**The highest tier whose threshold the cart has reached, applied once.** A cart of 600 €
gets 10 %, not 15 %.

**The comparison is `>=`.** "From 500 €" means from 500 € inclusive.

**Rounding is towards zero.** A 5 % discount on 24.99 € is 1.2495 €, granted as 1.24 €.

## Consequences

Summing tiers is the reading a merchant might expect, and they will not get it. The
configuration screen has to say so.

Rounding towards zero means a shopper is always a fraction of a cent worse off. Over a
single cart this is invisible; it is stated here so nobody "fixes" it into banker's
rounding later and quietly changes every discount in every shop.
```

Note the two trailing spaces after each metadata line — without them the lines collapse
into one paragraph.

### The three sections earn their place

**Context** states the question and the defensible alternatives. An ADR that opens with the
answer is a note, not a record — the value is in showing that the decision was a choice.

**Decision** is the ruling, in the imperative, with the specifics. Numbers, operators,
directions of rounding.

**Consequences** is what this costs, stated openly — including what someone will
reasonably expect and not get. This section is what stops the decision from being quietly
reversed by the next person who finds it inconvenient.

### An accepted ADR is never edited

A decision that no longer holds **moves to `adr/_superseded/`** and is replaced by a new
one that links back to it:

```markdown
# Discount tiers come from Shopware promotions

**date:** 2026-09-11  
**area:** checkout  
**supersedes:** `_superseded/2026-09-11-discount-tiers-belong-to-this-plugin.md`  

## Context

The earlier decision had this plugin compute and apply the discounts itself. That was taken
before it was established that a merchant can express the same thing as a normal Shopware
promotion with a cart rule …
```

Editing an accepted ADR destroys the thing it is for: knowing what was decided *when*, and
on what basis. A superseded ADR stays readable, because the question "why did we ever do it
that way" has an answer that matters.

### What deserves an ADR

Anything a later reader would otherwise undo by accident:

- a rule with defensible alternatives (which tier wins, where a threshold is measured)
- a deviation from what Shopware or a reference plugin does, **with the numbers**
- a tool chosen over an obvious competitor, and why
- a limitation accepted on purpose
- a rejection, so it is not re-proposed every six months

**Rejections are records too.** "Pest was evaluated and not adopted", with the reasoning,
saves the same argument being had annually.

### What does not

How a class works — the code says that. What a method returns — the signature says that.
An ADR that restates the implementation rots exactly like the comment it replaced.

### ADRs are binding

An ADR is not a historical note. **Code that contradicts an accepted ADR is wrong, even
when it works.** Read the ADR before touching the area it governs; when an ADR and a
`CLAUDE.md` disagree, the ADR wins and `CLAUDE.md` gets corrected.

List them in `CLAUDE.md` as a table of decision and area, so the set is visible without
opening the directory.

## CONTEXT.md

One file in the plugin root. **Read before starting or resuming anything, written after
finishing anything.** Its purpose: a session that was compacted or restarted resumes from
it without loss.

### What it carries

| Section | Content |
|---|---|
| Where the plugin stands | version, what it does, what is live |
| What was built this session | file paths, exactly |
| What was verified | and **how** — "Playwright green" versus "two runs, counts identical" |
| Decisions taken, and why | the short form; the long form is an ADR |
| Defects found | including ones caused and fixed in the same session |
| Mistakes made | what was assumed, what it cost, what settled it |
| Open questions | with the next concrete step |

### Three rules

**Never shortened to save space.** Completed items are marked done, not deleted. Length is
not a defect; loss is. A file of several thousand lines is working as intended.

**Verification is claimed only when it has been run.** "Tests green" means a run was
observed. A figure quoted is a figure that was measured. A summary claiming 100 % coverage
without a run behind it is worse than no summary, because it stops anyone from checking.

**Write down the mistakes.** This is the part people skip, and the part with the highest
value per line:

> **`Price` takes net before gross.** I asserted it the other way round, "corrected" a
> passing test into a failing one, and only reading the constructor settled it.

That paragraph saves the next person an hour. A record listing only what worked will not
stop anyone repeating what did not.

### Rewrite it in full before compression

At 90 %, 95 % and 98 % context usage, restate the complete current state. Everything not
written down is lost when the session compacts, and the restatement is cheap compared with
rediscovering it.

## How the three fit together

| Where | What | Checked by |
|---|---|---|
| Test name | the rule | it fails when the rule stops holding |
| ADR | why this rule and not the alternative | review, and the next person reading it |
| `CONTEXT.md` | what is done, verified, open | read at the start of every session |
| Code comment | a non-obvious constraint, one line | — |

If reasoning does not land in one of the first three, it has not been recorded.
