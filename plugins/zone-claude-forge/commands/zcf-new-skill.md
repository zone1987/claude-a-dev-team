---
name: zcf-new-skill
description: Scaffolds a compliant SKILL.md with a measured description, a reference map and a source section.
argument-hint: <plugin> <skill-name> [--user-invoked]
allowed-tools: Read, Glob, Grep, Write, Bash
model: haiku
---

# /zcf-new-skill

Scaffold the skill named in $ARGUMENTS. Ask one question at a time, and skip whatever the arguments
already answer.

## Steps (one question at a time)

1. **The domain**, in one sentence: what a reader would come to this skill for.
2. **The anchors.** A brand word, an exact filename, a path shape or an exact identifier. Reject a
   bare generic noun and offer the bound form instead. Check each candidate against
   `ANCHOR-INVENTORY.md` before accepting it.
3. **Invocation.** Model-invoked only when Claude or another skill must reach it unprompted;
   otherwise `disable-model-invocation: true`, which costs only the name. `--user-invoked` settles
   this without asking.
4. **The description**, assembled as `<Statement>. Use when <anchor>, <anchor>.` Measure it before
   writing anything: `python3 -c "print(len('…'))"`. Over 200, or under 10 characters of headroom,
   go back to step 3 rather than shipping it.
5. **The reference files** the skill will need, named `SCREAMING-CASE.md`.

## Then write

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/scaffold_component.py" skill \
  --plugin <plugin> --name <skill-name> [--user-invoked] \
  --description "<measured description>" [--reference NAME]…
```

Add the skill to `skills[]` in both manifests with `scripts/register-plugin.py`, because a directory
under `skills/` loads whether or not it is listed, and an unlisted one costs budget silently.

Finish by running `/zcf-validate <plugin> --strict`.

## Output

The paths written, the measured description length, and the gate's verdict.

Write only the frontmatter and the section skeleton; the body is the author's. Invent no content.
