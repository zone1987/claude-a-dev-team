# Swiper — Controller module

Synchronize two or more Swiper instances with each other.

```js
import Swiper from 'swiper';
import { Controller } from 'swiper/modules';

const swiper1 = new Swiper('.swiper-1', { modules: [Controller] });
const swiper2 = new Swiper('.swiper-2', {
  modules: [Controller],
  controller: {
    control: swiper1,
    inverse: false,
    by: 'slide',
  },
});

// Bidirectional
swiper1.controller.control = swiper2;
swiper2.controller.control = swiper1;
```

## Further reading
- [CONTROLLER-DETAIL.md](CONTROLLER-DETAIL.md) — all parameters, properties, methods, bidirectional sync pattern
