# Direction — API Reference

## DirectionProvider

Sets text direction for all shadcn/ui components in the subtree.

| Prop        | Type              | Default | Description                                      |
| ----------- | ----------------- | ------- | ------------------------------------------------ |
| `direction` | `"ltr" \| "rtl"` | –       | Preferred prop (shadcn wrapper alias for `dir`)  |
| `dir`       | `"ltr" \| "rtl"` | –       | Radix UI native prop (both work, `direction` wins)|
| `children`  | `ReactNode`       | –       | Child components                                 |

### Usage — RTL layout

```tsx
import { DirectionProvider } from "@/components/ui/direction"

<html dir="rtl">
  <body>
    <DirectionProvider direction="rtl">
      {/* Your app content */}
    </DirectionProvider>
  </body>
</html>
```

### Usage — LTR layout (default)

```tsx
<DirectionProvider direction="ltr">
  {/* Your app content */}
</DirectionProvider>
```

## useDirection

Hook to read the current direction in child components.

```tsx
import { useDirection } from "@/components/ui/direction"

function MyComponent() {
  const direction = useDirection()
  return <div>Current direction: {direction}</div>
}
```

Returns `"ltr"` or `"rtl"`.

## Notes

- Wrap your root layout (or specific subtree) with `DirectionProvider`.
- Set the matching `dir` attribute on the `<html>` element for full browser RTL support.
- All shadcn/ui components that support RTL will automatically adapt when wrapped in `DirectionProvider`.

---

_Source: `apps/v4/content/docs/components/base/direction.mdx`, `apps/v4/content/docs/components/radix/direction.mdx`_
