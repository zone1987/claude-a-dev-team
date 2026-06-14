# Select — Installation

## CLI (recommended)

```bash
npx shadcn@latest add select
```

## Manual (Radix variant)

### 1. Install dependency

```bash
npm install radix-ui
```

### 2. Copy component

Create `components/ui/select.tsx` with the source from [source.md](source.md).

### 3. Update import paths

Replace `@/lib/utils` with your project's `cn` utility path.

## Manual (Base UI variant)

### 1. Install dependency

```bash
npm install @base-ui/react
```

### 2. Use base variant source from [source.md](source.md).

## Usage (Radix)

```tsx
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

```tsx
<Select>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      <SelectItem value="light">Light</SelectItem>
      <SelectItem value="dark">Dark</SelectItem>
      <SelectItem value="system">System</SelectItem>
    </SelectGroup>
  </SelectContent>
</Select>
```

## Usage (Base UI — items prop pattern)

```tsx
const items = [
  { label: "Light", value: "light" },
  { label: "Dark", value: "dark" },
  { label: "System", value: "system" },
]

<Select items={items}>
  <SelectTrigger className="w-[180px]">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      {items.map((item) => (
        <SelectItem key={item.value} value={item.value}>
          {item.label}
        </SelectItem>
      ))}
    </SelectGroup>
  </SelectContent>
</Select>
```

## Composition

```text
Select
├── SelectTrigger
│   └── SelectValue
└── SelectContent
    ├── SelectGroup
    │   ├── SelectLabel
    │   ├── SelectItem
    │   └── SelectItem
    ├── SelectSeparator
    └── SelectGroup
        ├── SelectLabel
        ├── SelectItem
        └── SelectItem
```

## Invalid state

```tsx
<Field data-invalid>
  <FieldLabel>Fruit</FieldLabel>
  <SelectTrigger aria-invalid>
    <SelectValue />
  </SelectTrigger>
</Field>
```

## API Reference

- Radix: https://www.radix-ui.com/docs/primitives/components/select#api-reference
- Base UI: https://base-ui.com/react/components/select#api-reference

## Source files

- `content/docs/components/base/select.mdx`
- `content/docs/components/radix/select.mdx`
