# Swiper Angular — Vollständige Referenz (via Swiper Element)

**Wichtig:** Die separaten Angular-Komponenten (`swiper/angular`) wurden in Swiper v9 entfernt.
Der offizielle Weg ist seither die Integration via **Swiper Element** (Web Component).

---

## Migration von alten Angular-Komponenten (< v9)

Alte Imports entfernen:
```typescript
// ALT (v8, nicht mehr verfügbar):
import { SwiperModule } from 'swiper/angular';
// imports: [SwiperModule]
// <swiper [slidesPerView]="3">...</swiper>
```

Archiv für v8: https://v8.swiperjs.com/angular

---

## Installation

```bash
npm install swiper
```

---

## Schritt 1: CUSTOM_ELEMENTS_SCHEMA registrieren

### In einem NgModule (Angular < 19 ohne Standalone)

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

### In einer Standalone-Komponente (Angular 17+)

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

## Schritt 2: Swiper Element registrieren

```typescript
// main.ts (oder app.component.ts)
import { register } from 'swiper/element/bundle';
register();
```

Alternativ in `app.config.ts` (Angular 17+ Application Builder):
```typescript
import { ApplicationConfig } from '@angular/core';
import { register } from 'swiper/element/bundle';

register();

export const appConfig: ApplicationConfig = {
  providers: [...],
};
```

---

## Schritt 3: CSS importieren

```typescript
// angular.json — styles Array:
// "styles": ["node_modules/swiper/swiper-bundle.min.css"]

// Oder in styles.scss / styles.css:
@import 'swiper/css';
@import 'swiper/css/navigation';
@import 'swiper/css/pagination';
```

---

## Template — Attribute-Binding (einfache Werte)

```html
<!-- In der Component-Template -->
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

## Template — Property-Binding (Angular `[property]="value"`)

Für komplexe Parameter (Objekte, Arrays, Expressions):

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

## Swiper-Instanz via ViewChild

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

    // Komplexe Parameter vor initialize() setzen
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

## Events (DOM Custom Events)

Ab Swiper v11 haben alle Events standardmäßig den Präfix `swiper`:

```html
<!-- v11+ Events (Präfix "swiper") -->
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

Präfix anpassen (leerer String = kein Präfix, wie vor v11):
```html
<swiper-container events-prefix="">
  <!-- Events ohne Präfix: "slidechange", "progress", etc. -->
</swiper-container>
```

---

## NgFor mit Slides

```html
<swiper-container [slidesPerView]="3">
  <swiper-slide *ngFor="let item of items; let i = index">
    <img [src]="item.image" [alt]="item.title" />
    <h3>{{ item.title }}</h3>
  </swiper-slide>
</swiper-container>
```

---

## Thumbs-Integration

```typescript
@Component({
  template: `
    <!-- Haupt-Swiper -->
    <swiper-container
      #mainSwiper
      init="false"
      thumbs-swiper=".thumbs-swiper"
    >
      <swiper-slide *ngFor="let img of images">
        <img [src]="img" />
      </swiper-slide>
    </swiper-container>

    <!-- Thumbs-Swiper -->
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

## Signals-basierter Ansatz (Angular 17+)

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

## TypeScript-Typen

Für TypeScript-Unterstützung können Typ-Deklarationen für Custom Elements genutzt werden:

```typescript
// Eigene Type-Declaration wenn nötig
declare global {
  interface HTMLElementTagNameMap {
    'swiper-container': HTMLElement & {
      swiper: any;
      initialize: () => void;
      slidesPerView: number | 'auto';
      spaceBetween: number;
      loop: boolean;
      // weitere Parameter...
    };
    'swiper-slide': HTMLElement;
  }
}
```

---

## Häufige Probleme & Lösungen

| Problem | Lösung |
|---|---|
| `'swiper-container' is not a known element` | `CUSTOM_ELEMENTS_SCHEMA` im Modul/Component hinzufügen |
| Styles werden nicht angewendet | `@import 'swiper/css'` in `styles.scss` oder `angular.json` |
| Komplexe Parameter funktionieren nicht als Attribut | Via `Object.assign` + `initialize()` oder `[property]`-Binding |
| Events werden nicht gefeuert | Event-Namen prüfen: v11+ Prefix `swiper` (z.B. `swiperslidechange`) |
| Swiper initialisiert sich vor Property-Binding | `init="false"` Attribut setzen, dann `swiperEl.initialize()` manuell aufrufen |

---

*Quelle: https://swiperjs.com/angular + https://swiperjs.com/element — Swiper v12.2.0*
