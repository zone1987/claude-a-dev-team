# shadcn-direction

The `DirectionProvider` sets text direction (`ltr` or `rtl`) for shadcn/ui components. Wraps the Radix UI `Direction.DirectionProvider` (new-york-v4) or re-exports from `@base-ui/react/direction-provider` (Base UI). Essential for RTL languages (Arabic, Hebrew, Persian).

## Exports

- `DirectionProvider` — context provider, accepts `direction` or `dir` prop
- `useDirection` — hook to read the current direction in child components

## Quick start

```bash
npx shadcn@latest add direction
```

## References

- `DIRECTION-INSTALLATION.md` — CLI + manual install
- `DIRECTION-SOURCE.md` — complete source code for both variants
- `DIRECTION-API.md` — props and hook usage
