# Swiper Angular — Complete reference (via Swiper Element)

**Important:** The separate Angular components (`swiper/angular`) were removed in Swiper v9.
Since then, the official approach is integration via **Swiper Element** (Web Component).

---

## Contents

- [Migration from the old Angular components (< v9)](#migration-from-the-old-angular-components-v9)
- [Installation](#installation)
- [Step 1: Register CUSTOM_ELEMENTS_SCHEMA](#step-1-register-custom_elements_schema)
- [Step 2: Register Swiper Element](#step-2-register-swiper-element)
- [Step 3: Import the CSS](#step-3-import-the-css)
- [Template — attribute binding (simple values)](#template-attribute-binding-simple-values)
- [Template — property binding (Angular `[property]="value"`)](#template-property-binding-angular-propertyvalue)
- [Swiper instance via ViewChild](#swiper-instance-via-viewchild)
- [Events (DOM custom events)](#events-dom-custom-events)
- [NgFor with slides](#ngfor-with-slides)
- [Thumbs integration](#thumbs-integration)
- [Signals-based approach (Angular 17+)](#signals-based-approach-angular-17)
- [TypeScript types](#typescript-types)
- [Common problems and solutions](#common-problems-and-solutions)

## Migration from the old Angular components (< v9)

Remove the old imports:
```typescript
// OLD (v8, no longer available):
import { SwiperModule } from 'swiper/angular';
// imports: [SwiperModule]
// <swiper [slidesPerView]="3">...</swiper>
```

Archive for v8: https://v8.swiperjs.com/angular

---

## Installation

```bash
npm install swiper
```

---

## Step 1: Register CUSTOM_ELEMENTS_SCHEMA

### In an NgModule (Angular < 19 without standalone)

```typescript
// app.module.ts
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent],
})
export class AppModule {}
```

### In a standalone component (Angular 17+)

```typescript
// my.component.ts
import { Component, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@Component({
  selector: 'app-my',
  standalone: true,
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  template: `
    <swiper-container [slidesPerView]="3" [spaceBetween]="30">
      <swiper-slide>Slide 1</swiper-slide>
      <swiper-slide>Slide 2</swiper-slide>
    </swiper-container>
  `,
})
export class MyComponent {}
```

---

## Step 2: Register Swiper Element

```typescript
// main.ts (or app.component.ts)
import { register } from 'swiper/element/bundle';
register();
```

Alternatively in `app.config.ts` (Angular 17+ Application Builder):
```typescript
import { ApplicationConfig } from '@angular/core';
import { register } from 'swiper/element/bundle';

register();

export const appConfig: ApplicationConfig = {
  providers: [...],
};
```

---

## Step 3: Import the CSS

```typescript
// angular.json — styles array:
// "styles": ["node_modules/swiper/swiper-bundle.min.css"]

// Or in styles.scss / styles.css:
@import 'swiper/css';
@import 'swiper/css/navigation';
@import 'swiper/css/pagination';
```

---

## Template — attribute binding (simple values)

```html
<!-- In the component template -->
<swiper-container
  slides-per-view="3"
  space-between="30"
  loop="true"
  navigation="true"
  pagination="true"
  scrollbar="true"
  centered-slides="true"
  autoplay-delay="2500"
  autoplay-disable-on-interaction="false"
>
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
  <swiper-slide>Slide 3</swiper-slide>
</swiper-container>
```

---

## Template — property binding (Angular `[property]="value"`)

For complex parameters (objects, arrays, expressions):

```html
<swiper-container
  [slidesPerView]="slidesPerView"
  [spaceBetween]="spaceBetween"
  [loop]="true"
  [navigation]="true"
  [breakpoints]="breakpoints"
  [pagination]="{ clickable: true }"
  [autoplay]="{ delay: 3000, disableOnInteraction: false }"
  (swiperslidechange)="onSlideChange($event)"
  (swiperprogress)="onProgress($event)"
>
  <swiper-slide *ngFor="let slide of slides">{{ slide }}</swiper-slide>
</swiper-container>
```

```typescript
@Component({ ... })
export class MyComponent {
  slidesPerView = 3;
  spaceBetween = 30;
  breakpoints = {
    640: { slidesPerView: 2 },
    768: { slidesPerView: 3 },
    1024: { slidesPerView: 4 },
  };
  slides = ['Slide 1', 'Slide 2', 'Slide 3'];

  onSlideChange(event: CustomEvent) {
    const [swiper] = event.detail;
    console.log('Active index:', swiper.activeIndex);
  }

  onProgress(event: CustomEvent) {
    const [swiper, progress] = event.detail;
    console.log('Progress:', progress);
  }
}
```

---

## Swiper instance via ViewChild

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-swiper',
  standalone: true,
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  template: `
    <swiper-container #swiperRef init="false">
      <swiper-slide>Slide 1</swiper-slide>
      <swiper-slide>Slide 2</swiper-slide>
    </swiper-container>
    <button (click)="next()">Next</button>
    <button (click)="prev()">Prev</button>
  `,
})
export class SwiperComponent implements AfterViewInit {
  @ViewChild('swiperRef') swiperRef!: ElementRef;

  ngAfterViewInit() {
    const swiperEl = this.swiperRef.nativeElement;

    // Set complex parameters before initialize()
    Object.assign(swiperEl, {
      slidesPerView: 3,
      spaceBetween: 30,
      breakpoints: {
        640: { slidesPerView: 2 },
        1024: { slidesPerView: 4 },
      },
    });

    swiperEl.initialize();
  }

  next() {
    this.swiperRef.nativeElement.swiper.slideNext();
  }

  prev() {
    this.swiperRef.nativeElement.swiper.slidePrev();
  }

  slideTo(index: number) {
    this.swiperRef.nativeElement.swiper.slideTo(index);
  }
}
```

---

## Events (DOM custom events)

As of Swiper v11, all events carry the prefix `swiper` by default:

```html
<!-- v11+ events (prefix "swiper") -->
<swiper-container
  (swiperslidechange)="onSlideChange($event)"
  (swiperprogress)="onProgress($event)"
  (swiperreachend)="onReachEnd($event)"
  (swiperinit)="onInit($event)"
  (swipertransitionstart)="onTransitionStart($event)"
  (swipertransitionend)="onTransitionEnd($event)"
  (swiperclick)="onClick($event)"
  (swiperautoplaytimeLeft)="onAutoplayTimeLeft($event)"
>
```

```typescript
onSlideChange(event: CustomEvent) {
  const [swiper] = event.detail;
  console.log('Active index:', swiper.activeIndex);
}

onProgress(event: CustomEvent) {
  const [swiper, progress] = event.detail;
}

onAutoplayTimeLeft(event: CustomEvent) {
  const [swiper, time, progress] = event.detail;
}
```

Change the prefix (empty string = no prefix, as before v11):
```html
<swiper-container events-prefix="">
  <!-- Events without prefix: "slidechange", "progress", etc. -->
</swiper-container>
```

---

## NgFor with slides

```html
<swiper-container [slidesPerView]="3">
  <swiper-slide *ngFor="let item of items; let i = index">
    <img [src]="item.image" [alt]="item.title" />
    <h3>{{ item.title }}</h3>
  </swiper-slide>
</swiper-container>
```

---

## Thumbs integration

```typescript
@Component({
  template: `
    <!-- Main Swiper -->
    <swiper-container
      #mainSwiper
      init="false"
      thumbs-swiper=".thumbs-swiper"
    >
      <swiper-slide *ngFor="let img of images">
        <img [src]="img" />
      </swiper-slide>
    </swiper-container>

    <!-- Thumbs Swiper -->
    <swiper-container
      class="thumbs-swiper"
      slides-per-view="4"
      space-between="10"
      watch-slides-progress="true"
      free-mode="true"
    >
      <swiper-slide *ngFor="let img of images">
        <img [src]="img" />
      </swiper-slide>
    </swiper-container>
  `,
})
export class ThumbsComponent {}
```

---

## Signals-based approach (Angular 17+)

```typescript
import { Component, signal, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@Component({
  standalone: true,
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  template: `
    <swiper-container [slidesPerView]="slidesPerView()">
      @for (slide of slides(); track slide.id) {
        <swiper-slide>{{ slide.text }}</swiper-slide>
      }
    </swiper-container>
  `,
})
export class ReactiveComponent {
  slidesPerView = signal(3);
  slides = signal([
    { id: 1, text: 'Slide 1' },
    { id: 2, text: 'Slide 2' },
  ]);
}
```

---

## TypeScript types

For TypeScript support you can add type declarations for the custom elements:

```typescript
// Your own type declaration where needed
declare global {
  interface HTMLElementTagNameMap {
    'swiper-container': HTMLElement & {
      swiper: any;
      initialize: () => void;
      slidesPerView: number | 'auto';
      spaceBetween: number;
      loop: boolean;
      // further parameters...
    };
    'swiper-slide': HTMLElement;
  }
}
```

---

## Common problems and solutions

| Problem | Solution |
|---|---|
| `'swiper-container' is not a known element` | Add `CUSTOM_ELEMENTS_SCHEMA` to the module/component |
| Styles are not applied | `@import 'swiper/css'` in `styles.scss` or `angular.json` |
| Complex parameters do not work as an attribute | Use `Object.assign` + `initialize()` or `[property]` binding |
| Events are not fired | Check the event names: v11+ prefix `swiper` (e.g. `swiperslidechange`) |
| Swiper initializes before the property binding | Set the `init="false"` attribute, then call `swiperEl.initialize()` manually |

---

*Source: https://swiperjs.com/angular + https://swiperjs.com/element — Swiper v12.2.0*
