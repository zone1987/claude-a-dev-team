# Workflow: the order things are built in, and when they are done

## Test first, and the test fails first

```
specification / ADR  →  failing test  →  implementation  →  green gate  →  handover
```

**A test that passes the moment it is written has not been shown to test anything.** Run
it before the implementation exists and watch it fail for the reason you expect — "class
not found" is the right failure; "assertion failed on line 3" when you expected line 12 is
a test that is measuring something else.

This applies without exception to calculating classes. For wiring and configuration it
applies where practical.

## Test names state the rule, not the method

```php
public function testACartAtExactlyTheThresholdEarnsTheTier(): void   // yes
public function testCalculate(): void                                 // no
```

The name is the documentation that survives a refactoring. A suite of rule-shaped names
reads as the specification of the class; a suite of method names reads as nothing.

The same in JavaScript:

```javascript
it('asks for the offers of the product it was given', …)   // yes
it('renders', …)                                            // no
```

## The order a suite is built in

This order is not preference. Each step makes the next one safe.

### 1. Playwright first, on existing behaviour

Before any refactoring, before the gate, **pin what the plugin renders today**. It is the
only thing that can prove a rewrite changed nothing a shopper or a theme can see.

Writing it first also means writing it against behaviour you have not yet changed, so it
documents what is rather than what you intended.

### 2. The gate

There has to be something that can be green before anything else is worth doing. PHPStan,
style, Rector, the phpunit configs, coverage, Infection, the architecture rules.

Its acceptance check: two consecutive runs leave the tree byte-identical.

### 3. The arithmetic, out of wherever it is hiding

In a display plugin that is usually Twig. A template cannot be unit tested; whatever it
computes is untestable by construction. Move it to PHP, one class per question, and the
template renders what it is handed.

**Expect to find defects here.** Rules that were never written down have never been
checked. The three found in one such rewrite: a currency picked at random by `|first`, a
weight-based matrix compared against a cart value, and a free shipping band with an upper
bound announced as free shipping.

### 4. The feature

Test first, now that there is a gate to be green and a suite to prove nothing broke.

### 5. Jest, for whatever JavaScript exists

Administration and storefront, both to 100 %.

### 6. The acceptance suite grows

Every new flow, every new configuration switch.

## Done means all of this

- `composer gate` green
- coverage 100 % on the plugin's own PHP
- Jest 100 % on administration and storefront, enforced by threshold
- a mutation baseline recorded, every survivor documented
- the Playwright suite green
- **the shop unchanged after the run** → [STANDARD-CLEANUP.md](STANDARD-CLEANUP.md)
- `CONTEXT.md` and `CHANGELOG.md` written
- `README.md`, the ADRs and `CLAUDE.md` up to date
- **seen in a browser** — a green test proves the code does what the test expects; whether
  the result is right on screen is something only a person sees
- committed on the feature branch, **nothing pushed**

**Committing is part of done — under three conditions.** Ask at the start of a project
whether committing is wanted (a "no" holds for the whole project), commit only on a
feature branch, and **never push**.
→ Git is the plugin owner's: [STANDARD-DECISIONS.md](STANDARD-DECISIONS.md)

## Verification is claimed only when it has been run

"Tests green" means a test run was observed. A figure quoted in a report is a figure that
was measured. This is not pedantry — a summary that says "coverage 100 %" without a run
behind it is worse than no summary, because it stops anyone from checking.

## CONTEXT.md carries the state

Read before starting or resuming anything, written after finishing. What was decided and
why, what is verified, what is open, what the next concrete step is — with exact paths.

**Never shortened to save space.** Completed items are marked done, not deleted. The file
exists so that a session that lost its context can resume without losing knowledge, and
that only works if it is complete.

Write down the mistakes too. "The context's shipping method has no price matrix; the
delivery's does" is a paragraph that saves the next person an hour — and it only gets
written if getting it wrong is treated as information rather than as embarrassment.

## Scope discipline when a test fails

A failing test has exactly one of three causes, and naming which one before touching
anything saves a great deal:

1. **The code is wrong.** Fix the code.
2. **The test's expectation is wrong.** Fix the test — but prove the expectation is wrong
   first, by reading the source of the thing under test rather than by flipping the
   assertion until it passes.
3. **The test's setup is wrong.** Fix the setup.

Case 2 is where damage happens. A passing test "corrected" into a failing one because the
constructor argument order was assumed rather than read costs more than the original bug.
