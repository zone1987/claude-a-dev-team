# ReUI primitives and hooks — free, no licence

Generated from `https://reui.io/r/registry.json` (sha256 `a598d3b8b544a0fa`) by `scripts/gen_registry_refs.py`. 81 entries. Do not edit by hand.

Every entry installs with `shadcn add @reui/<name>` and needs no `REUI_LICENSE_KEY`.

| Item | Type | npm dependencies | @reui registry dependencies |
|---|---|---|---|
| `alert` | ui | `class-variance-authority` | — |
| `autocomplete` | ui | `@base-ui/react`, `class-variance-authority` | — |
| `badge` | ui | `@base-ui/react`, `class-variance-authority` | — |
| `cascader` | ui | `@base-ui/react`, `@tanstack/react-virtual` | `@reui/cascader-async`, `@reui/cascader-columns`, `@reui/cascader-context`, `@reui/cascader-i18n`, `@reui/cascader-item`, `@reui/cascader-lib`, `@reui/cascader-types` |
| `cascader-async` | ui | — | `@reui/cascader-context`, `@reui/cascader-lib`, `@reui/cascader-types` |
| `cascader-columns` | ui | `@base-ui/react` | `@reui/cascader-context`, `@reui/cascader-item`, `@reui/cascader-lib` |
| `cascader-context` | ui | — | `@reui/cascader-types` |
| `cascader-footer` | ui | `@base-ui/react` | `@reui/cascader-context`, `@reui/cascader-item`, `@reui/cascader-lib`, `@reui/cascader-types` |
| `cascader-i18n` | ui | — | `@reui/cascader-types` |
| `cascader-item` | ui | `@base-ui/react` | `@reui/cascader-context`, `@reui/cascader-lib`, `@reui/cascader-types` |
| `cascader-lib` | ui | — | `@reui/cascader-types` |
| `cascader-nav` | ui | `@base-ui/react` | `@reui/cascader-context`, `@reui/cascader-i18n`, `@reui/cascader-lib`, `@reui/cascader-types` |
| `cascader-types` | ui | — | — |
| `cascader-virtual` | ui | `@tanstack/react-virtual` | `@reui/cascader-columns`, `@reui/cascader-context`, `@reui/cascader-item` |
| `code-block` | ui | `shiki` | `@reui/code-block-highlight` |
| `code-block-highlight` | ui | `shiki` | — |
| `data-grid` | ui | `@base-ui/react`, `@dnd-kit/core`, `@dnd-kit/modifiers`, `@dnd-kit/sortable`, `@dnd-kit/utilities`, `@tanstack/react-table`, `@tanstack/react-virtual` | `@reui/badge`, `@reui/data-grid-i18n`, `@reui/data-grid-table` |
| `data-grid-cell-selection` | ui | `@tanstack/react-table` | `@reui/data-grid` |
| `data-grid-column-filter` | ui | `@tanstack/react-table` | `@reui/badge`, `@reui/data-grid` |
| `data-grid-column-header` | ui | `@tanstack/react-table` | `@reui/data-grid` |
| `data-grid-column-visibility` | ui | `@tanstack/react-table` | `@reui/data-grid` |
| `data-grid-i18n` | ui | — | — |
| `data-grid-pagination` | ui | — | `@reui/data-grid` |
| `data-grid-scroll-area` | ui | `@base-ui/react` | `@reui/data-grid` |
| `data-grid-table` | ui | `@tanstack/react-table` | `@reui/data-grid` |
| `data-grid-table-dnd` | ui | `@dnd-kit/core`, `@dnd-kit/sortable`, `@dnd-kit/utilities`, `@tanstack/react-table` | `@reui/data-grid`, `@reui/data-grid-table` |
| `data-grid-table-dnd-rows` | ui | `@dnd-kit/core`, `@dnd-kit/modifiers`, `@dnd-kit/sortable`, `@dnd-kit/utilities`, `@tanstack/react-table` | `@reui/data-grid`, `@reui/data-grid-table` |
| `data-grid-table-virtual` | ui | `@tanstack/react-table`, `@tanstack/react-virtual` | `@reui/data-grid`, `@reui/data-grid-table` |
| `date-selector` | ui | `date-fns`, `react-day-picker` | — |
| `event-calendar` | ui | `@base-ui/react`, `@date-fns/tz`, `date-fns` | `@reui/event-calendar-agenda-view`, `@reui/event-calendar-dnd`, `@reui/event-calendar-event`, `@reui/event-calendar-i18n`, `@reui/event-calendar-lib`, `@reui/event-calendar-month-view`, `@reui/event-calendar-recurrence`, `@reui/event-calendar-resource-view`, `@reui/event-calendar-time-grid`, `@reui/event-calendar-types`, `@reui/icon-stack` |
| `event-calendar-agenda-view` | ui | `@base-ui/react`, `date-fns` | `@reui/event-calendar`, `@reui/event-calendar-event`, `@reui/event-calendar-lib`, `@reui/event-calendar-types`, `@reui/icon-stack` |
| `event-calendar-content` | ui | `@base-ui/react` | `@reui/event-calendar`, `@reui/event-calendar-agenda-view`, `@reui/event-calendar-month-view`, `@reui/event-calendar-resource-view`, `@reui/event-calendar-time-grid`, `@reui/event-calendar-types` |
| `event-calendar-dnd` | ui | `date-fns` | `@reui/event-calendar`, `@reui/event-calendar-lib`, `@reui/event-calendar-types` |
| `event-calendar-event` | ui | `@base-ui/react`, `date-fns` | `@reui/event-calendar`, `@reui/event-calendar-dnd`, `@reui/event-calendar-lib`, `@reui/event-calendar-types` |
| `event-calendar-i18n` | ui | `date-fns` | `@reui/event-calendar-types` |
| `event-calendar-lib` | ui | `@date-fns/tz`, `date-fns` | `@reui/event-calendar-recurrence`, `@reui/event-calendar-types` |
| `event-calendar-month-view` | ui | `@base-ui/react`, `date-fns` | `@reui/event-calendar`, `@reui/event-calendar-dnd`, `@reui/event-calendar-event`, `@reui/event-calendar-lib`, `@reui/event-calendar-types` |
| `event-calendar-nav` | ui | `@base-ui/react`, `date-fns` | `@reui/event-calendar`, `@reui/event-calendar-lib`, `@reui/event-calendar-types` |
| `event-calendar-recurrence` | ui | `@date-fns/tz`, `date-fns` | `@reui/event-calendar-types` |
| `event-calendar-resource-view` | ui | `@base-ui/react`, `date-fns` | `@reui/event-calendar`, `@reui/event-calendar-dnd`, `@reui/event-calendar-event`, `@reui/event-calendar-lib`, `@reui/event-calendar-time-grid`, `@reui/event-calendar-types` |
| `event-calendar-time-grid` | ui | `@base-ui/react`, `date-fns` | `@reui/event-calendar`, `@reui/event-calendar-dnd`, `@reui/event-calendar-event`, `@reui/event-calendar-lib`, `@reui/event-calendar-types` |
| `event-calendar-types` | ui | — | — |
| `filters` | ui | `class-variance-authority`, `date-fns` | `@reui/cascader`, `@reui/cascader-context`, `@reui/cascader-footer`, `@reui/cascader-item`, `@reui/cascader-lib`, `@reui/cascader-nav`, `@reui/cascader-types`, `@reui/cascader-virtual`, `@reui/filters-advanced`, `@reui/filters-builder`, `@reui/filters-chip`, `@reui/filters-context`, `@reui/filters-dnd`, `@reui/filters-draft`, `@reui/filters-editors`, `@reui/filters-i18n`, `@reui/filters-lib`, `@reui/filters-operators`, `@reui/filters-query`, `@reui/filters-types` |
| `filters-advanced` | ui | — | `@reui/filters-builder`, `@reui/filters-chip`, `@reui/filters-context`, `@reui/filters-dnd`, `@reui/filters-i18n`, `@reui/filters-lib`, `@reui/filters-operators`, `@reui/filters-query`, `@reui/filters-types` |
| `filters-builder` | ui | — | `@reui/cascader`, `@reui/cascader-footer`, `@reui/cascader-nav`, `@reui/cascader-types`, `@reui/cascader-virtual`, `@reui/filters-context`, `@reui/filters-lib`, `@reui/filters-operators`, `@reui/filters-types` |
| `filters-chip` | ui | — | `@reui/filters-context`, `@reui/filters-editors`, `@reui/filters-lib`, `@reui/filters-operators`, `@reui/filters-query`, `@reui/filters-types` |
| `filters-context` | ui | — | `@reui/filters-draft`, `@reui/filters-lib`, `@reui/filters-types` |
| `filters-date` | ui | `date-fns` | — |
| `filters-dnd` | ui | — | — |
| `filters-draft` | ui | — | `@reui/filters-types` |
| `filters-editors` | ui | — | `@reui/cascader`, `@reui/cascader-context`, `@reui/cascader-footer`, `@reui/cascader-item`, `@reui/cascader-nav`, `@reui/cascader-types`, `@reui/filters-context`, `@reui/filters-lib`, `@reui/filters-types` |
| `filters-i18n` | ui | — | `@reui/filters-types` |
| `filters-lib` | ui | — | `@reui/cascader`, `@reui/cascader-lib`, `@reui/cascader-types`, `@reui/filters-types` |
| `filters-operators` | ui | — | `@reui/filters-types` |
| `filters-query` | ui | — | `@reui/filters-types` |
| `filters-types` | ui | — | — |
| `frame` | ui | `class-variance-authority` | — |
| `gantt` | ui | `@base-ui/react`, `@date-fns/tz`, `date-fns` | `@reui/gantt-bar`, `@reui/gantt-dnd`, `@reui/gantt-i18n`, `@reui/gantt-lib`, `@reui/gantt-recurrence`, `@reui/gantt-types` |
| `gantt-bar` | ui | `@base-ui/react` | `@reui/gantt`, `@reui/gantt-dnd`, `@reui/gantt-lib`, `@reui/gantt-types` |
| `gantt-dnd` | ui | `date-fns` | `@reui/gantt`, `@reui/gantt-lib`, `@reui/gantt-types` |
| `gantt-i18n` | ui | `date-fns` | `@reui/gantt-types` |
| `gantt-lib` | ui | `@date-fns/tz`, `date-fns` | `@reui/gantt-recurrence`, `@reui/gantt-types` |
| `gantt-nav` | ui | `@base-ui/react`, `date-fns` | `@reui/gantt`, `@reui/gantt-lib`, `@reui/gantt-types` |
| `gantt-recurrence` | ui | `@date-fns/tz`, `date-fns` | `@reui/gantt-types` |
| `gantt-types` | ui | — | — |
| `gantt-view` | ui | `@base-ui/react`, `date-fns` | `@reui/gantt`, `@reui/gantt-bar`, `@reui/gantt-dnd`, `@reui/gantt-lib`, `@reui/gantt-types` |
| `icon-stack` | ui | — | — |
| `icon-tile` | ui | `@base-ui/react`, `class-variance-authority` | — |
| `kanban` | ui | `@base-ui/react`, `@dnd-kit/core`, `@dnd-kit/sortable`, `@dnd-kit/utilities` | — |
| `number-field` | ui | `@base-ui/react`, `class-variance-authority` | — |
| `phone-input` | ui | `react-phone-number-input` | — |
| `rating` | ui | `class-variance-authority` | — |
| `scrollspy` | ui | — | — |
| `sortable` | ui | `@base-ui/react`, `@dnd-kit/core`, `@dnd-kit/sortable`, `@dnd-kit/utilities` | — |
| `stepper` | ui | `@base-ui/react` | — |
| `timeline` | ui | `@base-ui/react` | — |
| `tree` | ui | `@base-ui/react`, `@headless-tree/core` | — |
| `use-copy-to-clipboard` | hook | — | — |
| `use-file-upload` | hook | — | — |
| `use-scroll-position` | hook | — | — |
| `use-slider-input` | hook | — | — |

## Files per component family

Installing the family root pulls its parts in as registry dependencies.

- **alert** (1): `alert`
- **autocomplete** (1): `autocomplete`
- **badge** (1): `badge`
- **cascader** (1): `cascader`
- **cascader-async** (1): `cascader-async`
- **cascader-columns** (1): `cascader-columns`
- **cascader-context** (1): `cascader-context`
- **cascader-footer** (1): `cascader-footer`
- **cascader-i18n** (1): `cascader-i18n`
- **cascader-item** (1): `cascader-item`
- **cascader-lib** (1): `cascader-lib`
- **cascader-nav** (1): `cascader-nav`
- **cascader-types** (1): `cascader-types`
- **cascader-virtual** (1): `cascader-virtual`
- **code-block** (1): `code-block`
- **code-block-highlight** (1): `code-block-highlight`
- **data-grid** (1): `data-grid`
- **data-grid-cell-selection** (1): `data-grid-cell-selection`
- **data-grid-column-filter** (1): `data-grid-column-filter`
- **data-grid-column-header** (1): `data-grid-column-header`
- **data-grid-column-visibility** (1): `data-grid-column-visibility`
- **data-grid-i18n** (1): `data-grid-i18n`
- **data-grid-pagination** (1): `data-grid-pagination`
- **data-grid-scroll-area** (1): `data-grid-scroll-area`
- **data-grid-table** (1): `data-grid-table`
- **data-grid-table-dnd** (1): `data-grid-table-dnd`
- **data-grid-table-dnd-rows** (1): `data-grid-table-dnd-rows`
- **data-grid-table-virtual** (1): `data-grid-table-virtual`
- **date-selector** (1): `date-selector`
- **event-calendar** (1): `event-calendar`
- **event-calendar-agenda-view** (1): `event-calendar-agenda-view`
- **event-calendar-content** (1): `event-calendar-content`
- **event-calendar-dnd** (1): `event-calendar-dnd`
- **event-calendar-event** (1): `event-calendar-event`
- **event-calendar-i18n** (1): `event-calendar-i18n`
- **event-calendar-lib** (1): `event-calendar-lib`
- **event-calendar-month-view** (1): `event-calendar-month-view`
- **event-calendar-nav** (1): `event-calendar-nav`
- **event-calendar-recurrence** (1): `event-calendar-recurrence`
- **event-calendar-resource-view** (1): `event-calendar-resource-view`
- **event-calendar-time-grid** (1): `event-calendar-time-grid`
- **event-calendar-types** (1): `event-calendar-types`
- **filters** (1): `filters`
- **filters-advanced** (1): `filters-advanced`
- **filters-builder** (1): `filters-builder`
- **filters-chip** (1): `filters-chip`
- **filters-context** (1): `filters-context`
- **filters-date** (1): `filters-date`
- **filters-dnd** (1): `filters-dnd`
- **filters-draft** (1): `filters-draft`
- **filters-editors** (1): `filters-editors`
- **filters-i18n** (1): `filters-i18n`
- **filters-lib** (1): `filters-lib`
- **filters-operators** (1): `filters-operators`
- **filters-query** (1): `filters-query`
- **filters-types** (1): `filters-types`
- **frame** (1): `frame`
- **gantt** (1): `gantt`
- **gantt-bar** (1): `gantt-bar`
- **gantt-dnd** (1): `gantt-dnd`
- **gantt-i18n** (1): `gantt-i18n`
- **gantt-lib** (1): `gantt-lib`
- **gantt-nav** (1): `gantt-nav`
- **gantt-recurrence** (1): `gantt-recurrence`
- **gantt-types** (1): `gantt-types`
- **gantt-view** (1): `gantt-view`
- **icon-stack** (1): `icon-stack`
- **icon-tile** (1): `icon-tile`
- **kanban** (1): `kanban`
- **number-field** (1): `number-field`
- **phone-input** (1): `phone-input`
- **rating** (1): `rating`
- **scrollspy** (1): `scrollspy`
- **sortable** (1): `sortable`
- **stepper** (1): `stepper`
- **timeline** (1): `timeline`
- **tree** (1): `tree`
- **use-copy-to-clipboard** (1): `use-copy-to-clipboard`
- **use-file-upload** (1): `use-file-upload`
- **use-scroll-position** (1): `use-scroll-position`
- **use-slider-input** (1): `use-slider-input`

## Source

Generated from [`https://reui.io/r/registry.json`](https://reui.io/r/registry.json), sha256 `a598d3b8b544a0fa1fc834d7a590b2b04642c080890c46790c7a5df5e1ea239f`, mirrored 2026-09-04, by `scripts/gen_registry_refs.py`. Counts cross-checked against [`https://reui.io/llms.txt`](https://reui.io/llms.txt) (sha256 `a58bc32429b11535`). Regenerate with `/reui-sync`.
