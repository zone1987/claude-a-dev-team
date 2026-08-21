# Swiper — Instance methods

Call all methods on the Swiper instance.

```js
const swiper = new Swiper('.swiper', { ... });

swiper.slideNext();           // Next slide
swiper.slidePrev();           // Previous slide
swiper.slideTo(3, 500);       // To index 3 in 500 ms
swiper.update();              // Recalculate after DOM changes
swiper.destroy();             // Destroy the instance

swiper.on('slideChange', (s) => console.log(s.activeIndex));
```

## Further reading
- [METHODS-DETAIL.md](METHODS-DETAIL.md) — complete table of all methods (core, Navigation, Pagination, Scrollbar, Autoplay, Manipulation, Thumbs, Zoom, Keyboard, Mousewheel) with signatures and descriptions
