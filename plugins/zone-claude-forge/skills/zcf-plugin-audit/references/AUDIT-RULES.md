# Reading a finding

What the gate reports, and what to do with each kind. The rules themselves live in
[`RULES.md`](../../RULES.md); this file is about the mechanics.

## The line format

```
plugins/foo/skills/foo-bar/SKILL.md:14: [DESC-01] description is 214 characters, limit 200
```

Path, line where one applies, rule ID, then the measured value against the limit. The measurement is
the useful part: it says how far off, not merely that something is wrong.

## Exit codes

| Code | Meaning |
|---|---|
| `0` | clean |
| `1` | errors, or warnings under `--strict` |
| `2` | warnings only |
| `3` | bad arguments, or no such plugin |

`--strict` promotes warnings to errors. Use it in CI and before shipping; leave it off while
iterating, so a headroom warning does not hide a real error.

## Blocking versus judgement-bound

Every rule carries an enforcement class, and the distinction is honest rather than cosmetic:

- **`blocking`** is machine-decidable: character counts, line counts, field whitelists, `## Source`
  presence, reference depth, manifest parity, language. The script decides, and there is nothing to
  discuss.
- **`review`** is judgement-bound: whether an anchor is genuinely unambiguous, whether a sentence is a
  no-op, whether a reference earned its disclosure. **No script decides these.** Each carries a
  **tell** in `RULES.md`, and `claude-component-reviewer` applies it.

A gate that claimed to enforce the second class would be making a promise it cannot keep. Where the
script emits a judgement-bound finding it does so as a **warning**, meaning "look at this", not "this
is wrong".

## Ground classes change how negotiable a finding is

| Ground | What a finding means |
|---|---|
| `documented` | the platform says so. Not negotiable; fix the file |
| `technique` | a claimed effect with a measurement. Negotiable by arguing against the measurement |
| `convention` | a choice with a purpose and no platform backing. Negotiable by changing the rule |

So a `REF-01` finding and a `DEPTH-01` finding look identical in the output and are not the same kind
of problem: one is a naming habit, the other is content that Claude will never read past line 100.
Check the class before deciding how hard to fight.

## Single-file mode

```bash
python3 scripts/validate_plugin.py --file <path>
```

Checks one file against the rules that apply to its kind, and exits fast when the path is outside
`plugins/`. This is what the `PreToolUse` gate calls, because a whole-plugin scan is too slow to run
before every write, and a slow gate does not block at all.

## What the script cannot see

Three things, all of which need a human or a subagent:

- **Whether the intended prompts reach the skill.** Trigger testing is empirical; run the prompts.
- **Whether a neighbouring domain's prompts leave it alone.** The more important half, and the one
  people skip.
- **Whether the content is true.** `verify_sources.py` checks that a quotation appears on its page;
  nothing checks that a distilled fact is correct.

## Source

Implemented in `plugins/zone-claude-forge/scripts/validate_plugin.py`, read 2026-08-21. Rule classes
are defined in [`rules.json`](../../rules.json) under `classes`.
