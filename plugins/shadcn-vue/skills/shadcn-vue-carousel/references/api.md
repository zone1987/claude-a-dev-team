# Carousel — API Reference

## Sub-components

| Component | Description |
|-----------|-------------|
| `Carousel` | Root container. Provides context, handles keyboard navigation, exposes Embla API. |
| `CarouselContent` | Scroll viewport. Attaches Embla's root ref. |
| `CarouselItem` | Individual slide. Uses `basis-full` by default. |
| `CarouselNext` | Absolute-positioned "next" button (ArrowRight icon). |
| `CarouselPrevious` | Absolute-positioned "previous" button (ArrowLeft icon). |

---

## Carousel

### Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `opts` | `CarouselOptions` | — | Embla Carousel options (align, loop, dragFree, etc.) |
| `plugins` | `CarouselPlugin` | — | Array of Embla plugins (e.g. Autoplay) |
| `orientation` | `"horizontal" \| "vertical"` | `"horizontal"` | Scroll axis |
| `class` | `HTMLAttributes["class"]` | — | Additional CSS classes on the wrapper div |

### Emits

| Event | Payload | Description |
|-------|---------|-------------|
| `init-api` | `CarouselApi` (unwrapped Embla instance) | Fired once on `onMounted` after Embla initialises |

### Slot props (default slot via `v-slot`)

```vue
<Carousel v-slot="{ canScrollNext, canScrollPrev, carouselApi, carouselRef, orientation, scrollNext, scrollPrev }">
```

| Name | Type | Description |
|------|------|-------------|
| `canScrollNext` | `Ref<boolean>` | Whether the carousel can scroll forward |
| `canScrollPrev` | `Ref<boolean>` | Whether the carousel can scroll backward |
| `carouselApi` | `Ref<EmblaCarouselApi \| undefined>` | Raw Embla API instance |
| `carouselRef` | `Ref<HTMLElement \| undefined>` | The Embla root node ref |
| `orientation` | `"horizontal" \| "vertical"` | Current orientation |
| `scrollNext` | `() => void` | Scroll to next slide |
| `scrollPrev` | `() => void` | Scroll to previous slide |

### Exposed (template ref)

Same set as slot props — accessible via `const carouselRef = ref()` on the `<Carousel>` element.

### Keyboard navigation (built-in)

| Orientation | Prev key | Next key |
|-------------|----------|----------|
| horizontal | `ArrowLeft` | `ArrowRight` |
| vertical | `ArrowUp` | `ArrowDown` |

---

## CarouselContent

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Appended to the inner flex container |

Notes:
- `inheritAttrs: false` — extra attrs (`v-bind="$attrs"`) are forwarded to the inner flex div, not the overflow wrapper.
- Default negative margin: `-ml-4` (horizontal) / `-mt-4` (vertical) to compensate CarouselItem padding.

---

## CarouselItem

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `class` | `string` | — | Override/extend item sizing (e.g. `basis-1/2`) |

Default classes: `min-w-0 shrink-0 grow-0 basis-full pl-4` (horizontal) / `pt-4` (vertical).

---

## CarouselNext / CarouselPrevious

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `ButtonVariants["variant"]` | `"outline"` | shadcn Button variant |
| `size` | `ButtonVariants["size"]` | `"icon"` | shadcn Button size |
| `class` | `string` | — | Override positioning or appearance |

Default positioning (cannot scroll → button is `disabled`):

| Component | horizontal | vertical |
|-----------|-----------|---------|
| `CarouselPrevious` | `top-1/2 -left-12 -translate-y-1/2` | `-top-12 left-1/2 -translate-x-1/2 rotate-90` |
| `CarouselNext` | `top-1/2 -right-12 -translate-y-1/2` | `-bottom-12 left-1/2 -translate-x-1/2 rotate-90` |

Both buttons use the default slot — replace content to swap icons:

```vue
<CarouselNext>
  <ChevronRight class="size-4" />
</CarouselNext>
```

---

## useCarousel composable

```ts
import { useCarousel } from "@/components/ui/carousel"

const { canScrollNext, canScrollPrev, carouselApi, carouselRef, orientation, scrollNext, scrollPrev } = useCarousel()
```

**Must** be called inside a component that is a descendant of `<Carousel>`. Throws if no context is found:

```
useCarousel must be used within a <Carousel />
```

---

## TypeScript types

```ts
import type { CarouselApi } from "@/components/ui/carousel"
// CarouselApi = UnwrapRef<EmblaCarouselVueType[1]>
```

See also: [Embla Carousel API docs](https://www.embla-carousel.com/api/)
