# Slider — Base vs Radix

## Dependency

| Variant  | Package          |
| -------- | ---------------- |
| Radix    | `radix-ui`       |
| Base UI  | `@base-ui/react` |

## Key differences

| Aspect                    | new-york-v4 (Radix)                               | base variant (Base UI)                               |
| ------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| Root structure            | `Root > Track > Range + Thumb(s)`                 | `Root > Control > Track > Indicator + Thumb(s)`      |
| Range component           | `SliderPrimitive.Range`                           | `SliderPrimitive.Indicator`                          |
| Thumb alignment           | Default (centered on track)                       | `thumbAlignment="edge"` (thumb edge on track edge)   |
| `"use client"` directive  | Yes                                               | No (not needed)                                      |
| Disabled CSS selector     | `data-[disabled]:`                                | `data-disabled:`                                     |
| Orientation CSS selectors | `data-[orientation=horizontal]:`                  | `data-horizontal:` / `data-vertical:`                |
| Thumb styling             | Explicit: `rounded-full border border-primary bg-white shadow-sm ring-ring/50` | Via `cn-slider-thumb` CSS class token |

## API compatibility

Both exports accept the same props: `defaultValue`, `value`, `onValueChange`, `min`, `max`, `step`, `orientation`, `disabled`.

## Source files

- `registry/new-york-v4/ui/slider.tsx`
- `registry/bases/base/ui/slider.tsx`
