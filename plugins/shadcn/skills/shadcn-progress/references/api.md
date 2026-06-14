# Progress — API Reference

## Radix variant (new-york-v4 default)

### Composition

```text
Progress
└── ProgressIndicator  (internal, not exported)
```

### Progress

| Prop        | Type     | Default | Description                                  |
| ----------- | -------- | ------- | -------------------------------------------- |
| `value`     | `number` | `0`     | Current progress value (0–100)               |
| `max`       | `number` | `100`   | Maximum value                                |
| `className` | `string` |         | Override/extend default `h-2 rounded-full`   |

Inherits all `@radix-ui/react-progress` Root props. The indicator is animated with `transition-all` and moves via `translateX`.

## Base UI variant (extended API)

The Base UI variant exports additional sub-components for labeled progress bars.

### Composition

```text
Progress
├── ProgressLabel
├── ProgressValue
└── ProgressTrack
    └── ProgressIndicator
```

### ProgressLabel

Displays a text label above the track.

```tsx
import { Progress, ProgressLabel, ProgressValue } from "@/components/ui/progress"

<Progress value={56} className="w-full max-w-sm">
  <ProgressLabel>Upload progress</ProgressLabel>
  <ProgressValue />
</Progress>
```

### ProgressValue

Displays the current percentage value as text (rendered automatically from Base UI).

### ProgressTrack

The container track element. Base UI separates it from the root.

### ProgressIndicator

The moving fill element inside `ProgressTrack`.

---
Source: `content/docs/components/base/progress.mdx`
