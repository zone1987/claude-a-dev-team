# Free vs premium — what installs without a licence

Generated from `https://reui.io/r/registry.json` (sha256 `a598d3b8b544a0fa`) by `scripts/gen_registry_refs.py`. 1719 entries. Do not edit by hand.

The registry document is the authority for this split: an item carrying
`meta.group` is a premium block, everything else in it installs free.

| Tier | What | Count | Licence at install |
|---|---|---|---|
| Free | primitives (`registry:ui`) | 77 | none |
| Free | hooks (`registry:hook`) | 4 | none |
| Free | component examples (`c-*`) | 1105 | none |
| **Pro** | premium blocks | 533 | `REUI_LICENSE_KEY` |
| **Ultimate** | icons | 638 (2,552 variants) | `REUI_LICENSE_KEY` |
| **Ultimate** | full-page templates | 14 | `REUI_LICENSE_KEY` |

Icons and templates are not served in `registry.json`; `/r/icons.json` answers `401` without a licence, so their counts come from `llms.txt`: 638 icons in 4 styles = 2,552 installable variants. (The pricing table counts the 2,552 variants; the Introduction page's "562 icons" is stale.)

The 77 `registry:ui` files make up **22 documented primitives** plus the documented `file-upload` pattern — 23 documentation pages per build. A primitive ships as a family of files (`data-grid` pulls in `data-grid-pagination`, `data-grid-table`, ...), which is why the file count exceeds the component count.

## Premium block groups

| Group | Blocks |
|---|---|
| Application | 292 |
| eCommerce | 87 |
| Solutions | 65 |
| Marketing | 40 |
| Data Grid | 37 |
| AI & Agents | 12 |

## Telling them apart from a name

- `c-<component>-<n>` — free example.
- `<component>` with no prefix — free primitive.
- anything else (`app-shell-3`, `hero-11`, `solution-crm-2`, `data-grid-base-1`) — premium block.
- `@reui/icons/<default|animated>/<style>/<name>` — Ultimate icon.

## Source

Generated from [`https://reui.io/r/registry.json`](https://reui.io/r/registry.json), sha256 `a598d3b8b544a0fa1fc834d7a590b2b04642c080890c46790c7a5df5e1ea239f`, mirrored 2026-09-04, by `scripts/gen_registry_refs.py`. Counts cross-checked against [`https://reui.io/llms.txt`](https://reui.io/llms.txt) (sha256 `a58bc32429b11535`). Regenerate with `/reui-sync`.
