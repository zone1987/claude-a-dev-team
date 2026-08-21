# Progressive disclosure

`SKILL.md` is a map, not the territory. Where each piece sits decides what the agent pays for and
what it can still find. Rules: `DEPTH-01`, `REF-01`, `LINK-01`, `TOC-01`, `SIZE-01`.

## The hierarchy

Three rungs, ranked by how immediately the agent needs the material:

1. **In-file step**: what the agent does, in order. The primary tier.
2. **In-file reference**: consulted on demand. Often a flat peer-set, which is a fine arrangement
   rather than a smell: every rule of a review on one rung.
3. **Disclosed reference**: a sibling file reached by a pointer, loaded only when the pointer fires.

Push too little down and the top bloats; push too much and you hide what the agent needs. That
tension is the whole decision.

## The branching test

**Inline what every branch needs; disclose what only some branches reach.** A branch is a distinct
case the document handles, so different runs take different paths. That test is cleaner than any
length heuristic, and it explains why disclosure is not primarily a token optimisation: it protects
the hierarchy. In-file reference that should be disclosed buries the steps around it and turns
attending to them into a coin-flip.

## One level deep, and why it is a mechanism

> Claude may partially read files when they're referenced from other referenced files. When
> encountering nested references, Claude might use commands like `head -100` to preview content
> rather than reading entire files, resulting in incomplete information.
>
> **Keep references one level deep from SKILL.md.**

So a `references/deep/x.md` layout silently loses most of its own content: **everything past line 100
of a nested file is effectively invisible.** This is not a preference to trade off against tidiness.
`DEPTH-01`

Consequences for layout:

- Reference files are **flat siblings** of `SKILL.md`, named `SCREAMING-CASE.md`. `REF-01`
- **No `references/` subdirectory**, at any depth.
- Subdirectories carry non-markdown only: `scripts/`, `examples/`, `assets/`.
- **Every sibling is linked from `SKILL.md`** with a note on what it holds, so the agent can decide
  whether to open it, and so nothing becomes unreachable. `LINK-01`
- **A file over 100 lines carries a table of contents**, unless it has fewer than three sections.
  The 100 is the same preview boundary: a TOC is what lets a partial read still see the full scope.
  `TOC-01`

## Sprawl

The failure mode here is a document simply too long, even when every line is live and unique.
Attention thins across the excess, and every extra line is one more to keep relevant. The cure is the
ladder: disclose reference behind pointers, and split by branch or sequence so each path carries only
what it needs. `SIZE-01`

## Co-location

Where the ladder decides how far down a piece sits, co-location decides what sits beside it once
there. Keep a concept's definition, rules and caveats under one heading rather than scattered, so
reading one part brings its neighbours with it. Scattering fragments one meaning across many places;
that is distinct from duplication, which repeats one meaning in two.

## Source

[Progressive disclosure patterns](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#progressive-disclosure-patterns),
[avoid deeply nested references](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#avoid-deeply-nested-references)
and [structure longer reference files](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#structure-longer-reference-files-with-table-of-contents),
retrieved 2026-08-21. The hierarchy and branching test are distilled from
[mattpocock/skills](https://github.com/mattpocock/skills) `writing-for-agents`, retrieved 2026-08-21.
