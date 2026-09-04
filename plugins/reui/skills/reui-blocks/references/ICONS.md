# Icons (ReUI delta over shadcn)

Follow the shadcn icon rules (use the project's configured `iconLibrary`, `data-icon` on icons inside `Button`, no sizing classes on icons inside components, pass icons as component objects not string keys). ReUI adds the following.

## Portable icons (library-agnostic)

ReUI components, examples, and blocks are authored to be icon-library-agnostic. When `iconLibrary` is set in `components.json`, the shadcn CLI installs each item's icons in **your** library automatically - you swap nothing. If an installed item's icons don't match your project (for example `iconLibrary` isn't set, so they came in from the item's demo library), change the **import source and component name** to your library, keeping the same icon-name semantics:

- `lucide` -> `lucide-react`
- `tabler` -> `@tabler/icons-react`
- `phosphor` -> `@phosphor-icons/react`
- `remix` -> `@remixicon/react`
- `hugeicons` -> `@hugeicons/react`

Don't assume `lucide-react`; read `iconLibrary` from `components.json`.

## Keep icons purposeful

Icons support the hierarchy, they don't replace it: keep them small, matched to the surrounding density, and decorative ones `aria-hidden="true"` (an icon-only control still needs an accessible label on the control). Don't add ornamental icons that do no job.

## Motion Icons (the `@reui/icons/...` set)

ReUI ships its own icon set in 4 styles (outline, solid, duotone, filled), each icon in two variants:

```bash
npx shadcn@latest add @reui/icons/default/<style>/<name> --yes    # static
npx shadcn@latest add @reui/icons/animated/<style>/<name> --yes   # hover-animated (motion/react)
```

Finding them via the MCP is free; installing requires an Ultimate license (`REUI_LICENSE_KEY`, see [reui-setup/LICENSE-SETUP.md](../../reui-setup/references/LICENSE-SETUP.md)). Reach for a Motion Icon on a primary action when a subtle hover cue helps; keep motion restrained.

Finding icons:

- Several icons (the common case): **`search_icons(concepts[])`** - up to 24 concepts in one call, the best icons per concept with install commands. Pass `animated: true` to get only icons with a hover-animated Motion variant.
- One icon: `search` with `type: "icon"`.
- Icon results and `get_icon` carry `animated: true` and `installAnimated` when an animated variant exists - use those install strings, do not construct paths by hand.
- Every icon result carries a `previewUrl` (its live icon-category page) - **share it with the user** so they can SEE the icon before installing.

The `icon-stack` component composes multiple icons into a stacked display.

## One vendor claim the platform documentation contradicts

ReUI's own skill states that "an MCP client config never expands variables, so a ReUI MCP server
config must carry the raw token instead." That is not true of Claude Code, and reui.io's own Claude
page says the opposite: Claude Code substitutes `${VAR}` and `${VAR:-default}` in a server's `url`
and `headers` in `.mcp.json`, which is why the ReUI installer writes
`Authorization: Bearer ${REUI_LICENSE_KEY}` there rather than the key itself. Keep the value in the
environment. The vendor's warning does hold for clients that do not interpolate — there a `${...}`
placeholder is sent as literal text and comes back as a 401.

## Source

Distilled from ReUI's own agent skill (`rules/icons.md`, skill version `3bdbad788a`),
retrieved 2026-09-04 — the vendor's working rules, which no `reui.io/docs` page covers.
The contradiction noted above is resolved against
[https://reui.io/docs/claude](https://reui.io/docs/claude) (mirrored 2026-09-04) and the
Claude Code documentation.
