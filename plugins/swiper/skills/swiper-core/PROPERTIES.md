# Swiper — Instance properties

All properties are read-only (unless noted otherwise) and available directly on the instance.

```js
const swiper = new Swiper('.swiper', { ... });

console.log(swiper.activeIndex);    // current index
console.log(swiper.realIndex);      // real index (loop-normalized)
console.log(swiper.isBeginning);    // true when the first slide is active
console.log(swiper.isEnd);          // true when the last slide is active
console.log(swiper.progress);       // 0..1 progress of the wrapper
console.log(swiper.slides);         // array of all slide HTMLElements
console.log(swiper.params);         // active configuration
```

## Further reading
- [PROPERTIES-DETAIL.md](PROPERTIES-DETAIL.md) — complete table of all properties (core, Navigation, Pagination, Scrollbar, Autoplay, Thumbs, Zoom, Keyboard, Mousewheel) with type and description
