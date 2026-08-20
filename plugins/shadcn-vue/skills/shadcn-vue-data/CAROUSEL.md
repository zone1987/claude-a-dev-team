# shadcn-vue-carousel

A skill for the shadcn-vue `Carousel` component — built on Embla Carousel and composed of five sub-components (`Carousel`, `CarouselContent`, `CarouselItem`, `CarouselNext`, `CarouselPrevious`) plus a `useCarousel` composable.

## Triggers

**DE:** "Carousel Komponente shadcn", "Slider Vue", "Karussell shadcn-vue", "CarouselItem"
**EN:** "carousel shadcn-vue", "embla carousel vue", "Carousel CarouselItem", "slider carousel"

## References

- [installation.md](`CAROUSEL-INSTALLATION.md`) — CLI and manual installation
- [source.md](`CAROUSEL-SOURCE.md`) — Complete source files
- [api.md](`CAROUSEL-API.md`) — Props, emits, slot props, composable API
- [examples.md](`CAROUSEL-EXAMPLES.md`) — Usage demos and patterns

## Quick Start

```bash
npx shadcn-vue@latest add carousel
```

```vue
<Carousel>
  <CarouselContent>
    <CarouselItem v-for="i in 5" :key="i">Slide {{ i }}</CarouselItem>
  </CarouselContent>
  <CarouselPrevious />
  <CarouselNext />
</Carousel>
```

## Key facts

- Wraps **Embla Carousel** (`embla-carousel-vue`)
- Provides injection-state context via `@vueuse/core` `createInjectionState`
- Supports `horizontal` and `vertical` orientation
- Navigation buttons are absolutely positioned — parent needs `px-12` (or similar) room
- All Embla options passable via `:opts`, plugins via `:plugins`
- Exposes Embla API via `@init-api` emit or template ref
