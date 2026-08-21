# Swiper A11y (accessibility) module — Complete reference

## Contents

- [Concept](#concept)
- [Import and activation](#import-and-activation)
- [Parameters](#parameters)
- [Automatically set ARIA attributes](#automatically-set-aria-attributes)
- [Localization example (German)](#localization-example-german)
- [Focus management](#focus-management)
- [Interaction with the Navigation module](#interaction-with-the-navigation-module)

## Concept

The A11y module adds ARIA attributes and screen reader messages to the Swiper to improve accessibility. It sets roles, labels and live region announcements.

## Import and activation

```js
import Swiper from 'swiper';
import { A11y, Navigation, Pagination } from 'swiper/modules';

const swiper = new Swiper('.swiper', {
  modules: [A11y, Navigation, Pagination],
  a11y: {
    prevSlideMessage: 'Previous slide',
    nextSlideMessage: 'Next slide',
    firstSlideMessage: 'This is the first slide',
    lastSlideMessage: 'This is the last slide',
    paginationBulletMessage: 'Go to slide {{index}}',
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
```

## Parameters

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `enabled` | `boolean` | `true` | Enable the A11y module |
| `prevSlideMessage` | `string` | `'Previous slide'` | Screen reader text for the prev button |
| `nextSlideMessage` | `string` | `'Next slide'` | Screen reader text for the next button |
| `firstSlideMessage` | `string` | `'This is the first slide'` | Announcement when the first slide is active (no loop) |
| `lastSlideMessage` | `string` | `'This is the last slide'` | Announcement when the last slide is active (no loop) |
| `paginationBulletMessage` | `string` | `'Go to slide {{index}}'` | Text for pagination bullets; `{{index}}` = 1-based index |
| `notificationClass` | `string` | `'swiper-notification'` | CSS class for the screen reader live region |
| `id` | `string \| number` | `null` | Custom ID for the Swiper wrapper |
| `containerMessage` | `string` | `null` | `aria-label` for the Swiper container |
| `containerRoleDescriptionMessage` | `string` | `null` | `aria-roledescription` for the container |
| `itemRoleDescriptionMessage` | `string` | `null` | `aria-roledescription` for individual slides |
| `slideLabelMessage` | `string` | `'{{index}} / {{slidesLength}}'` | `aria-label` template for each slide |
| `slideRole` | `string` | `'group'` | ARIA role for slides (`'group'` or `'listitem'`) |
| `slidesRole` | `string` | `'group'` | ARIA role for the Swiper wrapper |

## Automatically set ARIA attributes

The module sets the following attributes automatically:

```html
<!-- Swiper container -->
<div class="swiper" role="group" aria-label="Image gallery">
  <!-- Wrapper -->
  <div class="swiper-wrapper" role="group" aria-label="Slides">
    <!-- Slides -->
    <div class="swiper-slide" role="group" aria-label="1 / 5">...</div>
    <div class="swiper-slide" role="group" aria-label="2 / 5" aria-hidden="true">...</div>
  </div>
  
  <!-- Navigation buttons -->
  <div class="swiper-button-prev" aria-label="Previous slide" role="button" tabindex="0"></div>
  <div class="swiper-button-next" aria-label="Next slide" role="button" tabindex="0"></div>
</div>

<!-- Live region for announcements -->
<span class="swiper-notification" aria-live="assertive" aria-atomic="true"></span>
```

## Localization example (German)

```js
const swiper = new Swiper('.swiper', {
  modules: [A11y, Navigation, Pagination],
  a11y: {
    enabled: true,
    prevSlideMessage: 'Vorheriger Slide',
    nextSlideMessage: 'Nächster Slide',
    firstSlideMessage: 'Dies ist der erste Slide',
    lastSlideMessage: 'Dies ist der letzte Slide',
    paginationBulletMessage: 'Zu Slide {{index}} wechseln',
    containerMessage: 'Produkt-Galerie',
    containerRoleDescriptionMessage: 'Bildkarussell',
    itemRoleDescriptionMessage: 'Produktbild',
    slideLabelMessage: 'Slide {{index}} von {{slidesLength}}',
  },
});
```

## Focus management

The module makes sure that:
- Navigation buttons are reachable by keyboard (`tabindex="0"`)
- The active slide is focusable
- Slides that are not visible receive `aria-hidden="true"`

## Interaction with the Navigation module

When Navigation is active, the buttons automatically receive the correct ARIA attributes:

```js
const swiper = new Swiper('.swiper', {
  modules: [A11y, Navigation],
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  a11y: {
    nextSlideMessage: 'Next',
    prevSlideMessage: 'Back',
    // Buttons automatically receive:
    // role="button", tabindex="0", aria-label="..."
  },
});
```

---
Source: https://swiperjs.com/swiper-api#accessibility-a11y
