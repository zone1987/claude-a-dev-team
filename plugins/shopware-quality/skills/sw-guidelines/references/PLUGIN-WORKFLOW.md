# Shopware 6 plugin — workflow and the definition of "done"

How a task runs from start to commit, and the fifteen conditions that decide whether it is finished. Builds on
[PLUGIN-GROUND-RULES.md](PLUGIN-GROUND-RULES.md); what is documented where is in
[PLUGIN-CLAUDE-MD.md](PLUGIN-CLAUDE-MD.md).

## Contents

- [One task at a time](#one-task-at-a-time)
- [A request arriving mid-task](#a-request-arriving-mid-task)
- [The order inside a task](#the-order-inside-a-task)
- [Two browser tabs](#two-browser-tabs)
- [Commits](#commits)
- [What is measured and what is asserted](#what-is-measured-and-what-is-asserted)
- [Definition of "done"](#definition-of-done)

---

## One task at a time

**A task is finished before the next one starts.** Finished means: the code is written, the tests are green, the gate
is green, the documentation is updated, and it is committed. **Not "the code works".**

---

## A request arriving mid-task

It is **noted, not followed**. The running task runs to its commit. Afterwards the request is written to its place
([PLUGIN-CLAUDE-MD.md](PLUGIN-CLAUDE-MD.md), the `TODO.md` rule).

**The sole exception:** a change to `CLAUDE.md` itself. It is carried out at once, because it changes the rules the
work is currently following.

---

## The order inside a task

```
1.  Read CONTEXT.md (if present)
2.  Read CLAUDE.md
3.  Read the ADRs of the affected area
4.  Write the failing test
5.  Make the change
6.  composer gate
7.  composer test:integration
8.  composer coverage:all — read the number, do not assume it
9.  composer test:admin
10. shopware-cli build, if administration or storefront is affected
11. E2E, if behaviour is affected
12. Look at it in the browser
13. Write CHANGELOG.md, README.md, ADRs
14. Continue CONTEXT.md
15. Commit
```

**Step 4 before step 5.** For a bug, the test that proves it is written first. A test written after the fix checks
that the code does what it does — not that the bug is gone.

**Step 12 is not optional.** A green test proves the code does what the test expects. Whether the result looks right
in the shop is something only a person sees.

---

## Two browser tabs

For browser testing, **two separate tabs** are always kept open:

| Tab | Content |
|---|---|
| Tab 0 | **Administration** (`/admin`) |
| Tab 1 | **Storefront** |

**Why:** a configuration change is saved in the administration and must then be checked in the storefront — often
dozens of times in a row. Navigating one tab back and forth loses the state every time: unsaved forms, the scroll
position, the open dialog, the admin session.

Further tabs as needed, such as Mailpit for mail tests.

---

## Commits

**Conventional Commits, in English:**

```
fix(listing): compute the offset cumulatively across pages
feat(admin): add a category tree to the badge form
test(e2e): prove every configuration combination in the storefront
docs(adr): record why nothing in this plugin is small
chore(deps): pin stryker to 9.6.1
```

**One commit per finished task**, not per file and not per working day.

**Never `git push`** (ground rule 4).

---

## What is measured and what is asserted

**Every number in a report comes from an observed run.**

| Wrong | Right |
|---|---|
| "Coverage is at 100 %" | run `composer coverage:all`, read the number |
| "The tests are green" | run the suite, show the output |
| "The shop is unchanged" | count before and after, compare the numbers |
| "That should work" | look at it in the browser |

> **A lesson from an own mistake:** after reactivating a plugin it was reported that a certain notice did not appear
> in the HTML — on the strength of `grep -c`. **`grep -c` counts lines, and a rendered page is one line.** There were
> in fact 48 occurrences. The correct form is `grep -o … | wc -l`.
>
> A tool whose counting method you do not know gives you a number, not an answer.

---

## Definition of "done"

A task is done when **all** of the following hold:

| # | Condition | How it is checked |
|---|---|---|
| 1 | `composer gate` green | run it |
| 2 | Two gate runs leave the same tree | `shasum` comparison |
| 3 | PHP coverage 100 %, **measured** | `composer coverage:all`, read the number |
| 4 | Jest 100 % enforced by threshold | `composer test:admin` |
| 5 | All integration tests green | `composer test:integration` |
| 6 | All E2E tests green | Playwright run |
| 7 | Two E2E runs leave the shop unchanged | count before/after |
| 8 | Every surviving mutant justified | baseline in `docs/mutation/<datum>/` |
| 9 | Looked at in the browser | by hand |
| 10 | `CHANGELOG.md` written | — |
| 11 | `README.md` current | — |
| 12 | ADRs for every decision taken | — |
| 13 | `CLAUDE.md` current, every new trap recorded | — |
| 14 | Committed — **in the feature branch**, and only if agreed at the start of the project | `git log`, `git branch --show-current` |
| 15 | **Nothing pushed** | — |

**Points 2, 3, 7 and 9 are the ones most likely to be skipped — and the ones that find the most expensive mistakes.**
