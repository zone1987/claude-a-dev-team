# Filters

Custom Shadcn Filters for React and Tailwind CSS. A stepped filter builder with nested attributes,
popover value editors and a boolean query tree.

Free component — no licence key required.

Filters turns a schema of attributes into a filter bar. A user picks an attribute, picks a
condition, gives it a value, and the result is one boolean query object you compile into a
predicate, a query string or a request body.

The state it edits is a TREE, not a list of chips. `FilterQuery` is a group of rules combined by
`and` or `or`, and a group may hold another group, so `(A and B) or C` is expressible from day one.
The chip row renders the flat case of that tree and the advanced builder renders the whole of it,
read and written through the same actions, which is why `variant` picks a chrome rather than a
second state model.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Prompt for the query tree migration](#prompt-for-the-query-tree-migration)
- [Examples](#examples)
- [API Reference](#api-reference) — in full in [FILTERS-API.md](FILTERS-API.md)
- Worked example sources — [FILTERS-EXAMPLES.md](FILTERS-EXAMPLES.md)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/filters
```

(npm/yarn/bun equivalents: `npx shadcn@latest add @reui/filters`, `yarn dlx shadcn@latest add
@reui/filters`, `bunx shadcn@latest add @reui/filters`.)

The install target moved. The old primitive was a single `components/reui/filters.tsx`. The rewrite
ships fourteen files under `components/reui/filters/`, so an existing consumer must delete the old
single file after installing, or end up with two different `Filters` exports one directory apart.

The registry item pulls six shadcn parts — `button`, `button-group`, `dropdown-menu`, `input`,
`popover` and `tooltip` — plus one ReUI item, `cascader`. `@reui/cascader` is the heavy one and
brings `@base-ui/react` and `@tanstack/react-virtual` with it, since every list in this primitive is
the cascader, configured: the attribute picker drills through nested fields, the operator menu and
each option editor are the same control run flat, and the keyboard, `aria-activedescendant`,
typeahead, RTL keys, windowing and the live region all come from there rather than from a listbox
this primitive re-implements. Two npm packages come in directly: `class-variance-authority`, for the
bar's size variants, and `date-fns`, used only by `filters-date.tsx`. Nothing in the core imports the
date helpers, so that file and its dependency can both be deleted if you do not want a date editor.

Nine of the fourteen files import no UI library at all. `filters-types`, `filters-query`,
`filters-lib`, `filters-operators`, `filters-draft`, `filters-i18n`, `filters-context`,
`filters-date` and `filters-dnd` pull nothing from Base UI, from `radix-ui` or from the shadcn parts.
Eight of those nine touch no DOM either, which is what lets the query, the operator catalog and the
step machine be tested in a node environment with no browser at all. `filters-dnd` is the exception:
it is a pointer engine, so it is library free but not DOM free.

## Usage

```tsx
import { Filters } from "@/components/reui/filters/filters"
import { createFilterQuery } from "@/components/reui/filters/filters-query"
import type {
  FilterField,
  FilterQuery,
} from "@/components/reui/filters/filters-types"
```

```tsx
const fields: FilterField[] = [
  { id: "title", label: "Title", type: "text" },
  {
    id: "status",
    label: "Status",
    type: "select",
    options: [
      { value: "active", label: "Active" },
      { value: "archived", label: "Archived" },
    ],
  },
]

export function Toolbar() {
  const [query, setQuery] = useState<FilterQuery>(() => createFilterQuery())

  return <Filters fields={fields} query={query} onQueryChange={setQuery} />
}
```

`fields` is the only required prop. Leave `query` off and the bar keeps its own state, seeded from
`defaultQuery`.

Choosing an attribute commits the rule straight away, so the chip appears reading "Select
condition", and picking a condition advances the same popover to the value editor. Escape keeps an
unfinished rule rather than dropping it, drawn with a dashed outline, and `flattenFilterConditions`
skips it so a half-built rule can never silently filter nothing.

### The query is a tree

A query is always a group, never a bare array. The root holds rules and other groups in order, and
its `combinator` says how they join.

```tsx
const query: FilterQuery = {
  id: "root",
  type: "group",
  combinator: "and",
  rules: [
    {
      id: "r1",
      type: "rule",
      path: ["status"],
      operator: "is",
      value: "active",
    },
  ],
}
```

### Basic and advanced

`variant` picks the chrome. Both read and write the same `query`, so a saved view built in one opens
in the other with nothing converted on the way.

```tsx
// A flat pill row, for a toolbar over a table.
<Filters fields={fields} />

// The condition builder, hung off a trigger that carries the rule count.
<Filters fields={fields} variant="advanced" />

// The same builder rendered in place, for a sidebar or a settings page.
<Filters fields={fields} variant="advanced" advancedMode="inline" />
```

### Nested attributes

A field carrying `fields` renders as a branch the picker drills into. A rule stores the whole path,
root first.

```tsx
const fields: FilterField[] = [
  {
    id: "name",
    label: "Name",
    fields: [
      { id: "full", label: "Full name", type: "text" },
      { id: "first", label: "First name", type: "text" },
    ],
  },
]

// A rule on "First name" stores path: ["name", "first"]
```

### The None option

An option marked `exclusive` is the row that means NONE OF THE ABOVE. Picking it clears every other
pick, and picking anything else clears it.

```tsx
options: [
  { value: "ada", label: "Ada" },
  { value: "unassigned", label: "Unassigned", exclusive: true },
]
```

### Taking the query somewhere

The primitive stops at the tree and compiles nothing. There is no SQL here, and that is deliberate:
the tree is the integration surface, and SQL is one target beside Prisma, Drizzle, a REST query
string and Elasticsearch, none of which a browser serves well.

The query is plain JSON, so it goes on the wire as it stands — no class instances, no functions, and
no `Date` objects, since a date rule stores a relative token. `flattenFilterConditions` gives you
`{ path, field, operator, values, negated }` per rule when a flat conjunction is all you need; walk
the tree yourself when the parentheses carry meaning.

Operator arity, custom value editors, date tokens, validation helpers and the full export list are
in the API Reference below.

## Prompt for the query tree migration

If you already have Filters installed, paste the prompt below into your coding agent. It covers both
cases: a session with the ReUI MCP connected, and a plain project where the primitive is reinstalled
from the registry.

```
Migrate ReUI Filters from the flat filter array to the query tree.

STEP 1 - Replace the Filters primitive from the registry.

  Case A, the ReUI MCP is available in this session:
    - Call search("filters"), then get_component("filters") to read the current API.
    - Call get_examples("filters") to see real composition.
    - Run the command returned by get_install_command("filters") and overwrite when prompted.

  Case B, no ReUI MCP:
    - Run: npx shadcn@latest add @reui/filters
    - Answer yes when asked to overwrite the existing files.

  Every filters file must come from the registry. Do not hand-patch them, do not merge
  them by hand, and do not keep a local fork of any of them.

STEP 2 - Delete the old single file.

  - The install target moved from components/reui/filters.tsx to the components/reui/filters/
    directory. The installer does not remove the file it replaces.
  - Delete components/reui/filters.tsx once the install has finished.
  - Do not continue until it is gone. If both survive, the project has two different
    Filters exports one directory apart, and which one an import resolves to depends on
    module resolution order, so the app can typecheck and build and still render the old
    primitive against the new props.

STEP 3 - Convert the state from a flat array to a query tree.

  - The old state was Filter[], each { id, field, operator, values }, joined by an
    implicit AND that was never written down anywhere.
  - The new state is a single FilterQuery, which is ALWAYS a group:
      { id, type: "group", combinator: "and" | "or", rules: FilterNode[] }
    A FilterNode is either a rule or another group, so nesting is the same shape again.
  - Each old filter becomes a rule:
      { id, type: "rule", path: string[], operator: string, value, negated?: boolean }
  - Two of those are shape changes, not renames, and both need conversion code:
      1. field: string becomes path: string[], root first. A flat field is a one-element
         path, so field: "status" becomes path: ["status"]. Nested attributes are the
         reason it is an array.
      2. values: T[] becomes a single value. A multiselect keeps its array AS that one
         value; a single-value operator takes the scalar itself, not a one-element array.
  - Wrap the converted rules in a root group with combinator "and". That reproduces the
    old implicit-AND behaviour exactly, so existing saved views keep their meaning.
  - Anything that persisted filters (localStorage, a saved-view table, a URL param) holds
    the OLD shape. Convert on read, and decide explicitly whether to write the new shape
    back or to keep converting, because a half-migrated store is the failure mode here.

STEP 4 - Update the component props.

  - filters and onChange become query (or defaultQuery for uncontrolled) and onQueryChange.
    onQueryChange receives (query, details), where details carries the reason it fired:
    add, update, remove, duplicate, negate, reorder, combinator or clear.
  - fields changed shape. FilterFieldsConfig, which accepted either a field array or a
    group array, becomes a plain FilterField[]. Per field, key becomes id, and id and
    label are both REQUIRED now rather than optional.
  - A field's type survives the name but not the values. The old union was
    "select" | "multiselect" | "text" | "custom" | "separator". The new FilterValueType is
    "text" | "number" | "range" | "select" | "multiselect" | "boolean". There is no
    "custom" - register an editor and name it with the field's editor prop - and no
    "separator", which was a rendering hint rather than a value type.
  - Field groups are gone as a separate concept. A field carrying its own fields IS a
    branch that the picker drills into, and the rule stores the whole path.
  - variant survives the name but changed meaning entirely: "solid" | "default" became
    "basic" | "advanced". "basic" is the chip row, "advanced" is the nested condition
    builder. If variant="solid" was passed for appearance, delete it rather than mapping it.
  - i18n becomes labels, with the operator wording split out into operatorLabels.
  - Removed with no replacement: radius, showSearchInput, allowMultiple, menuPopupClassName,
    collapseAddButton, enableShortcut, shortcutKey and shortcutLabel.
  - Unchanged: size, trigger and className.

STEP 5 - Prove the migration is complete.

  Search the whole project. Every one of these must return zero results:
    components/reui/filters.tsx
    variant="solid"
    showSearchInput
    allowMultiple
    collapseAddButton
    enableShortcut
    shortcutKey

  Then check every <Filters> element: none may still pass filters= or onChange=.
  Any hit is a call site that was missed.

STEP 6 - Verify it actually runs.

  Typecheck must pass with no errors. Then open each filter bar and confirm: adding a
  condition, editing its value in place, removing it, and that a previously saved or
  seeded query still loads with the same meaning it had before. If variant="advanced" is
  used anywhere, also confirm nested groups render, that switching a group between AND and
  OR works, and - if you passed `reorderable` - that drag reordering works.
```

## Examples

The docs page names 5 examples with "Copy"/"View Code" affordances (heading only, no printed
description or inline code in the mirrored markdown): Nested Attributes, Table Filtering, Choice
Editors, Advanced In A Popover, Nested Groups Inline.

"The other six ship exactly as these do and stay browsable on the Filters components page: status
and priority color badges, avatar options paged over the wire, a date and a date range editor,
sliders as the value editor, typed values in shadcn inputs, and a controlled bar across three sizes
and three locales." (upstream page's own wording; no code printed for any of the eleven).

The page's own worked appendix example (fixtures using `Dot`, a star-icon Priority swatch, and
`Avatar`/`AvatarGroup` for assignees) is present in full on the mirrored page after the Accessibility
section but is not reproduced in this reference — see [FILTERS-API.md](./FILTERS-API.md) for what
that appendix demo's imports establish about custom `renderValue`/icon composition, restated as API
facts rather than as example code.

## API Reference

The complete `Filters` root prop table, the query model, every sub-component
(`FiltersRow`/`FiltersBuilder`/`FiltersAdvanced`/`FiltersAdvancedPanel`/`FilterAdvancedRow`/
`FilterChip`/`FilterFieldPicker`/`FilterOperatorPopover`/`FilterValuePopover`/
`FilterRuleMenuItems`/`FilterMenu`), every type (`FilterField`, `FilterOperator`, `FilterOption`,
value editors, `FilterEditorProps`, `FilterOptionsState`, `FilterLoadContext`/`FilterLoadResult`,
`FilterValueDisplayContext`), the full `FilterLabels` i18n key table, every hook, Right to left,
Development warnings, Keyboard, and Accessibility are in
**[FILTERS-API.md](./FILTERS-API.md)** — split out because together with this file it would exceed
what one reference file should carry.

## Base UI vs Radix UI

Detect your build from `components.json` -> `style`: `base-nova` -> Base UI (this file's default),
`radix-nova` -> Radix UI.

Filters' own public API carries **no** `render`/`asChild` props anywhere (confirmed by diffing the
two mirrored pages: zero occurrences of either in the diff) — every `Filters*`/`Filter*` component's
prop table is byte-identical text between the two builds. Filters is built on `@reui/cascader`
internally (see [CASCADER.md](./CASCADER.md) for that component's own, larger Base UI/Radix UI diff),
but Filters does not expose the cascader's `render`/`asChild` surface through its own props.

Real differences found in the diff:

- **Wording only**, no functional difference: "The rewrite ships fourteen files under
  `components/reui/filters/`" — identical on both pages except the Base UI mirror's markdown
  extraction dropped the inline code span around the path and the component name in two spots (a
  markdown-extraction artifact of the mirror, not an upstream content difference).
- Marketing copy differs ("Base UI primitives from @base-ui/react" vs "the Radix UI implementation
  with accessible primitives from the Radix stack").
- The appendix worked example (fixtures for a custom `renderValue`) imports differ slightly between
  builds in ways consistent with the same Base UI vs Radix UI import-path pattern seen in every other
  component (not confirmed in exhaustive detail for this file, since the appendix example itself is
  out of scope for this reference — see [FILTERS-API.md](./FILTERS-API.md)'s note).

Everything else — the `Filters` root prop table, the query model, every sub-component's prop table,
every type, `FilterLabels`, every hook, Right to left, Development warnings, Keyboard, and
Accessibility — is identical text between the two builds.

## Source

- https://reui.io/docs/components/base/filters (Base UI)
- https://reui.io/docs/components/radix/filters (Radix UI)
- Mirrored 2026-09-04.
