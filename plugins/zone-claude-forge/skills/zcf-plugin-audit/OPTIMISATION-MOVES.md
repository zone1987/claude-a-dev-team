# Repair moves

Ordered cheapest first. Apply the first that holds and stop; each later move costs more and changes
more.

## 1. Sharpen the description

The cheapest fix and the most common need. A description is too long, or its anchors are generic, or
the key use case is not first.

- Cut the statement, not the trigger list: the statement describes scope, the anchors do the work.
- Bind a generic noun to a brand word, a filename, a path shape or an exact identifier.
- Move the key use case to the front, because the entry truncates from the end.

Costs nothing but the edit. Changes no structure.

## 2. Disclose a reference

The body is over 120 lines, or it holds material only some runs need.

The test is **branching**: inline what every branch needs, push behind a pointer what only some
branches reach. Move the section into a flat `SCREAMING-CASE.md` sibling, link it from `SKILL.md`
with a note on what it holds, and add a table of contents if it passes 100 lines.

Costs one file. Changes nothing about how the skill is reached.

## 3. Switch invocation

The description is well written and still expensive, and Claude rarely chooses the skill anyway.

`disable-model-invocation: true` removes the description from context and leaves only the name. The
price is real: **nothing but the human can reach the skill**, so no other skill may call it, and a
step depending on it becomes an instruction to the human. Add a router entry, or the skill becomes
something only its author remembers.

Costs reachability. Saves the whole entry.

## 4. Merge by domain

Two skills that always fire together spend two descriptions and two overheads for one concept.

Merge them, keep both sets of reference files as siblings, and write one description covering the
domain. Verify afterwards that no content was lost: a merge that drops a section is a regression the
gate cannot see.

Costs a rewrite. Saves one entry outright.

## 5. Split by sequence

The opposite case: one skill carries two jobs, and the second tempts the agent to rush the first.

Split where a run of steps has post-completion steps in view. Note that this only helps across a real
context boundary; an inline call leaves the later steps in context and clears nothing.

Costs an entry. Buys reliability.

## What is never a move

**Deleting facts to shorten a file.** A field without its type, an enum value without its meaning, a
parameter without its optionality: each is a gap, and the gate rejects the change. `COV-04`

If a reference file is too long, it splits. It does not shrink by omission.

**Restating a rule in a skill.** A skill names a rule ID; `rules.json` owns the wording. Copying the
text creates a second source of truth that drifts.

## Order matters

Applying move 3 before move 1 hides a fixable description behind an invocation change, and the
description stays bad for whoever un-hides it later. Work the list in order, and re-run the gate after
each step rather than at the end, so it is clear which move fixed what.

## Source

Levers distilled from [mattpocock/skills](https://github.com/mattpocock/skills) `writing-for-agents`,
retrieved 2026-08-21, and the budget mechanics in
[skills](https://code.claude.com/docs/en/skills), retrieved 2026-08-21.
