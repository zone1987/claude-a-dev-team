# @shopware/cms-base-layer — Vollständige CMS-Referenz

Version: **3.0.0**

Nuxt-Layer mit Vue-3-Komponenten für das Rendering aller Shopware-CMS-Typen (Sections, Blocks, Elemente).

---

## Integration als Nuxt-Layer

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  extends: ['@shopware/cms-base-layer'],
  // Voraussetzung: @shopware/nuxt-module ist als Modul registriert
})
```

Der Layer:
- Registriert alle CMS-Komponenten **global** (auto-import aus `app/components/public/`)
- Aktiviert Auto-Import der Nuxt-Composables in cms-base-Dateien (Fix für Nitro-Import-Transformationen)
- Nutzt `@nuxt/image` für optimierte Bilder, `@tresjs/nuxt` für 3D-Inhalte

---

## Kern-Rendering-Komponenten

### `<CmsPage :content="cmsPage" />`

Eintrittspunkt für das Rendering einer vollständigen CMS-Page. Rendert alle Sections dynamisch.

```vue
<script setup>
import type { Schemas } from '#shopware'
const { page } = useListing()
// oder: via useProductSearch / useCategorySearch / useLandingSearch mit withCmsAssociations: true
</script>
<template>
  <CmsPage v-if="page?.cmsPage" :content="page.cmsPage" />
</template>
```

**Props:**
```ts
defineProps<{ content: Schemas["CmsPage"] }>()
```

**Intern:** Iteriert `content.sections[]`, löst pro Section den Komponenten-Namen auf (`CmsSection${pascalCase(section.type)}`), rendert via `h()`. Wendet `getCmsLayoutConfiguration` für Styles und CSS-Klassen an. Ruft `createCategoryListingContext` auf wenn `routeName === 'frontend.navigation.page'`.

---

### `<CmsGenericBlock :content="block" />`

Rendert einen CMS-Block dynamisch anhand von `block.type`.

```vue
<template>
  <CmsGenericBlock :content="block" />
</template>
```

**Props:**
```ts
defineProps<{ content: Schemas["CmsBlock"] }>()
```

**Intern:**
1. `resolveCmsComponent(block)` → löst `CmsBlock${pascalCase(block.type)}` auf
2. Wendet Hintergrundstyles und CSS-Klassen an (`getCmsLayoutConfiguration`)
3. Stellt `slotCount` und `imageSizes` via `provide` bereit
4. In `import.meta.dev`: Konsolenwarnung mit Docs-Link wenn Komponente fehlt

---

### `<CmsGenericElement :content="slot" />`

Rendert ein CMS-Element (Slot) dynamisch anhand von `slot.type`.

**Props:**
```ts
defineProps<{ content: Schemas["CmsSlot"] }>()
```

**Intern:**
1. `resolveCmsComponent(slot)` → löst `CmsElement${pascalCase(slot.type)}` auf
2. Wendet CSS-Klassen/Styles an
3. In `import.meta.dev`: Konsolenwarnung wenn Element fehlt

---

### `<CmsNoComponent :content="..." />`

Fallback-Komponente die in Dev-Mode angezeigt wird wenn ein Block/Element-Typ nicht implementiert ist. Zeigt den fehlenden Komponenten-Namen an.

---

## Komponenten-Resolver: `resolveCmsComponent`

```ts
import { resolveCmsComponent } from '@shopware/composables'

const { resolvedComponent, componentName, isResolved, componentNameToResolve } =
  resolveCmsComponent(content)
```

| Rückgabe | Typ | Beschreibung |
|---|---|---|
| `resolvedComponent` | `Component \| string` | Aufgelöste Vue-Komponente, oder String wenn nicht gefunden |
| `componentName` | `string` | z.B. `"CmsElementText"` |
| `isResolved` | `boolean` | `true` wenn als echte Komponente aufgelöst |
| `componentNameToResolve` | `string` | Erwarteter Komponentenname |

**Namenskonvention:** Shopware CMS-Typ-String → `CmsElement` / `CmsBlock` / `CmsSection` + PascalCase des Typs.

Beispiele:
- Slot `type: "text"` → `CmsElementText`
- Block `type: "image-text"` → `CmsBlockImageText`
- Section `type: "default"` → `CmsSectionDefault`
- Section `type: "sidebar"` → `CmsSectionSidebar`

---

## Eigene CMS-Komponenten registrieren

### Eigenes CMS-Element

Für einen CMS-Slot-Typ der noch nicht in `cms-base-layer` existiert oder überschrieben werden soll:

```vue
<!-- components/CmsElementMyCustomType.vue -->
<script setup lang="ts">
import { useCmsElementConfig } from '@shopware/composables'
import type { CmsSlot } from '#shopware'

const props = defineProps<{ content: CmsSlot }>()
const { getConfigValue } = useCmsElementConfig(props.content)

const myOption = getConfigValue('myCustomOption')
</script>
<template>
  <div>{{ content.data?.text }}</div>
</template>
```

Nuxt auto-importiert Komponenten aus `components/` — da `CmsGenericElement` via `resolveComponent()` sucht, wird die eigene Komponente automatisch gefunden.

---

### Eigenen CMS-Block registrieren

```vue
<!-- components/CmsBlockMyCustomBlock.vue -->
<script setup lang="ts">
import { useCmsBlock } from '@shopware/composables'
import type { CmsBlock } from '#shopware'

const props = defineProps<{ content: CmsBlock }>()
const { getSlotContent } = useCmsBlock(props.content)
const mainSlot = getSlotContent('main')
</script>
<template>
  <div class="my-custom-block">
    <CmsGenericElement v-if="mainSlot" :content="mainSlot" />
  </div>
</template>
```

---

### Standard-Komponente überschreiben

Eine eigene `CmsElementText.vue` in `components/` überschreibt die aus dem Layer. Nuxt gibt Projekt-Komponenten Vorrang gegenüber Layer-Komponenten.

---

## Vollständige Komponenten-Liste

### Sections (2)

| Komponentenname | Shopware-Typ | Beschreibung |
|---|---|---|
| `CmsSectionDefault` | `default` | Standard-Section (nur `main`-Position) |
| `CmsSectionSidebar` | `sidebar` | Zwei-Spalten-Layout: `main` + `sidebar` |

---

### Blocks (44)

| Komponentenname | Shopware-Typ | Layout/Inhalt |
|---|---|---|
| `CmsBlockCategoryNavigation` | `category-navigation` | Kategorie-Navigation |
| `CmsBlockCenterText` | `center-text` | Zentrierter Text |
| `CmsBlockCrossSelling` | `cross-selling` | Cross-Selling-Produkte |
| `CmsBlockCustomForm` | `custom-form` | Eigenes Formular |
| `CmsBlockDefault` | (fallback) | Fallback-Block |
| `CmsBlockForm` | `form` | Standardformular |
| `CmsBlockGalleryBuybox` | `gallery-buybox` | Galerie + Kaufbox |
| `CmsBlockHtml` | `html` | Roher HTML-Inhalt |
| `CmsBlockImage` | `image` | Einzelbild |
| `CmsBlockImageBubbleRow` | `image-bubble-row` | Bilder in Bubble-Form |
| `CmsBlockImageCover` | `image-cover` | Vollbild-Bild |
| `CmsBlockImageFourColumn` | `image-four-column` | 4-Spalten-Bilder |
| `CmsBlockImageGallery` | `image-gallery` | Bildergalerie |
| `CmsBlockImageGalleryBig` | `image-gallery-big` | Große Bildergalerie |
| `CmsBlockImageHighlightRow` | `image-highlight-row` | Highlight-Bilder-Zeile |
| `CmsBlockImageSimpleGrid` | `image-simple-grid` | Simples Bild-Grid |
| `CmsBlockImageSlider` | `image-slider` | Bild-Slider |
| `CmsBlockImageText` | `image-text` | Bild + Text |
| `CmsBlockImageTextBubble` | `image-text-bubble` | Bild + Text (Bubble-Stil) |
| `CmsBlockImageTextCover` | `image-text-cover` | Bild-Cover + Text |
| `CmsBlockImageTextGallery` | `image-text-gallery` | Galerie + Text |
| `CmsBlockImageTextRow` | `image-text-row` | Bilder-Text-Zeile |
| `CmsBlockImageThreeColumn` | `image-three-column` | 3-Spalten-Bilder |
| `CmsBlockImageThreeCover` | `image-three-cover` | 3 Cover-Bilder |
| `CmsBlockImageTwoColumn` | `image-two-column` | 2-Spalten-Bilder |
| `CmsBlockProductDescriptionReviews` | `product-description-reviews` | Beschreibung + Bewertungen |
| `CmsBlockProductHeading` | `product-heading` | Produkt-Überschrift |
| `CmsBlockProductListing` | `product-listing` | Produkt-Listing |
| `CmsBlockProductSlider` | `product-slider` | Produkt-Slider |
| `CmsBlockProductThreeColumn` | `product-three-column` | 3-Spalten-Produkte |
| `CmsBlockSidebarFilter` | `sidebar-filter` | Sidebar-Filter |
| `CmsBlockText` | `text` | Text-Block |
| `CmsBlockTextHero` | `text-hero` | Text-Hero |
| `CmsBlockTextOnImage` | `text-on-image` | Text auf Bild |
| `CmsBlockTextTeaser` | `text-teaser` | Text-Teaser |
| `CmsBlockTextTeaserSection` | `text-teaser-section` | Text-Teaser-Sektion |
| `CmsBlockTextThreeColumn` | `text-three-column` | 3-Spalten-Text |
| `CmsBlockTextTwoColumn` | `text-two-column` | 2-Spalten-Text |
| `CmsBlockVimeoVideo` | `vimeo-video` | Vimeo-Video |
| `CmsBlockYoutubeVideo` | `youtube-video` | YouTube-Video |

---

### Elemente (21)

| Komponentenname | Shopware-Typ | Beschreibung |
|---|---|---|
| `CmsElementBuyBox` | `buy-box` | Kaufbox (Produkt + In-den-Warenkorb) |
| `CmsElementCategoryNavigation` | `category-navigation` | Kategorie-Navleiste |
| `CmsElementCrossSelling` | `cross-selling` | Cross-Selling-Produkte |
| `CmsElementCustomForm` | `custom-form` | Eigenes Formular |
| `CmsElementForm` | `form` | Standardformular |
| `CmsElementHtml` | `html` | XSS-sanitierter HTML-Inhalt |
| `CmsElementImage` | `image` | Bild mit Link, Display-Mode, Thumbnails |
| `CmsElementImageGallery` | `image-gallery` | Bildergalerie mit Zoom |
| `CmsElementImageGallery3dPlaceholder` | (intern) | 3D-Platzhalter in Galerie |
| `CmsElementImageSlider` | `image-slider` | Bild-Slider |
| `CmsElementManufacturerLogo` | `manufacturer-logo` | Hersteller-Logo |
| `CmsElementProductBox` | `product-box` | Produkt-Karte |
| `CmsElementProductDescriptionReviews` | `product-description-reviews` | Tabs: Beschreibung/Bewertungen |
| `CmsElementProductListing` | `product-listing` | Vollständiges Produkt-Listing |
| `CmsElementProductName` | `product-name` | Produktname als Überschrift |
| `CmsElementProductSlider` | `product-slider` | Horizontal scrollbarer Produkt-Slider |
| `CmsElementSidebarFilter` | `sidebar-filter` | Filter-Sidebar |
| `CmsElementText` | `text` | Rich-Text (HTML via html-to-vue-Renderer) |
| `CmsElementVimeoVideo` | `vimeo-video` | Eingebettetes Vimeo-Video |
| `CmsElementYoutubeVideo` | `youtube-video` | Eingebettetes YouTube-Video |
| `SwProductListingPagination` | (intern) | Pagination für Produkt-Listings |

---

## Listing-Filter-Komponenten

| Komponentenname | Beschreibung |
|---|---|
| `SwFilterPrice` | Preis-Schieberegler mit Dual-Input |
| `SwFilterProperties` | Checkbox-Liste für Property-Gruppen/Hersteller |
| `SwFilterRating` | 5-Sterne-Bewertungsfilter |
| `SwFilterShippingFree` | Gratis-Versand-Toggle |

---

## Sw*-Komponenten (Wiederverwendbare UI)

Zusätzlich zu den CMS-Komponenten exportiert der Layer allgemeine Storefront-Komponenten:

| Komponente | Beschreibung |
|---|---|
| `SwCategoryNavigation` | Kategorie-Navigationsleiste |
| `SwCategoryNavigationLink` | Einzelner Navigationslink |
| `SwContactForm` | Kontaktformular |
| `SwFilterChips` | Aktive Filter als Chips |
| `SwFilterDropdown` | Filter-Dropdown-Container |
| `SwListingProductPrice` | Preis im Listing |
| `SwMedia3D` | 3D-Medien (via @tresjs) |
| `SwNewsletterForm` | Newsletter-Anmeldeformular |
| `SwPagination` | Allgemeine Pagination |
| `SwProductAddToCart` | In-den-Warenkorb-Button |
| `SwProductCard` | Produktkarte (Bild + Name + Preis) |
| `SwProductCardDetails` | Produktkarten-Details |
| `SwProductCardImage` | Produktkarten-Bild |
| `SwProductCardSkeleton` | Skeleton-Loader für Produktkarte |
| `SwProductGallery` | Produktbild-Galerie |
| `SwProductListingFilter` | Einzelner Listing-Filter |
| `SwProductListingFilters` | Listing-Filter-Panel (vertikal) |
| `SwProductListingFiltersHorizontal` | Listing-Filter-Panel (horizontal) |
| `SwProductPrice` | Produkt-Preisanzeige |
| `SwProductRating` | Sternebewertungs-Anzeige |
| `SwProductReviews` | Bewertungsliste |
| `SwProductReviewsForm` | Bewertung-Eingabeformular |
| `SwProductUnits` | Produkteinheiten |
| `SwQuantitySelect` | Mengenauswahl |
| `SwSharedPrice` | Preis-Formatierung |
| `SwSlider` | Allgemeiner Slider |
| `SwSortDropdown` | Sortierungs-Dropdown |
| `SwStockInfo` | Lagerbestand-Anzeige |
| `SwVariantConfigurator` | Varianten-Auswahl |

---

## UI-Basiskomponenten

| Komponente | Beschreibung |
|---|---|
| `BaseButton` | Basisschaltfläche (verschiedene Varianten) |
| `BaseIcon` | Icon-Wrapper |
| `Checkbox` | Checkbox mit Custom-Styling |
| `CheckmarkIcon` | Häkchen-Icon |
| `ChevronIcon` | Pfeil-Icon (chevron) |
| `ExclamationIcon` | Ausrufezeichen-Icon |
| `IconButton` | Icon-Schaltfläche |
| `RadioButton` | Radio-Button (`defineModel<string\|null>`) |
| `StarIcon` | Stern-Icon (`filled` Prop) |
| `SwitchButton` | Toggle-Switch (`defineModel<boolean\|null>`) |
| `UserIcon` | Nutzer-Icon |
| `WishlistIcon` | Wunschliste-Icon (gefüllt/leer) |

---

## CMS-Composables in Komponenten

### `useCmsBlock` — in Block-Komponenten

```vue
<!-- CmsBlockImageText.vue -->
<script setup lang="ts">
import { useCmsBlock } from '@shopware/composables'
import type { CmsBlock } from '#shopware'

const props = defineProps<{ content: CmsBlock }>()
const { block, getSlotContent } = useCmsBlock(props.content)

const imageSlot = getSlotContent('left')    // Slot nach Position/Name
const textSlot = getSlotContent('right')
</script>
<template>
  <div class="flex">
    <CmsGenericElement v-if="imageSlot" :content="imageSlot" />
    <CmsGenericElement v-if="textSlot" :content="textSlot" />
  </div>
</template>
```

---

### `useCmsSection` — in Section-Komponenten

```vue
<!-- CmsSectionSidebar.vue -->
<script setup lang="ts">
import { useCmsSection } from '@shopware/composables'
import type { CmsSection } from '#shopware'

const props = defineProps<{ content: CmsSection }>()
const { section, getPositionContent } = useCmsSection(props.content)

const mainBlocks = getPositionContent('main')
const sidebarBlocks = getPositionContent('sidebar')
</script>
<template>
  <div class="flex">
    <aside class="w-1/4">
      <CmsGenericBlock v-for="block in sidebarBlocks" :key="block.id" :content="block" />
    </aside>
    <main class="w-3/4">
      <CmsGenericBlock v-for="block in mainBlocks" :key="block.id" :content="block" />
    </main>
  </div>
</template>
```

---

### `useCmsElementConfig` — Element-Konfiguration lesen

```vue
<!-- CmsElementImage.vue -->
<script setup lang="ts">
import { useCmsElementConfig, useCmsElementImage } from '@shopware/composables'

const props = defineProps<{ content: CmsSlot }>()
const { getConfigValue } = useCmsElementConfig(props.content)
const { imageAttrs, anchorAttrs, displayMode, isVideoElement } = useCmsElementImage(props.content)

const minHeight = getConfigValue('minHeight')  // z.B. "200px"
const displayMode = getConfigValue('displayMode')  // "cover", "contain", "standard"
</script>
```

---

## HTML-zu-Vue-Renderer (`CmsElementText`)

`CmsElementText` verwendet einen eigenen AST-basierten HTML-Renderer (aus `helpers/html-to-vue/`):

1. **`generateAST(html)`**: Parsed HTML-String in einen AST (via `html-to-ast`)
2. **`rectifyAST(ast)`**: Umbenennt Tags zu Vue-Komponenten-Namen
3. **`renderer(ast, config)`**: Konvertiert AST in VNodes via `h()`; nutzt `extraComponentsMap` für Custom-Tag-Handler
4. **`renderToHtml(html, config)`**: Einstiegspunkt; konfigurierbar mit:
   - `container.type` — Wrapper-Element
   - `extraComponentsMap` — Custom-Tag-Handler
   - `textTransformer` — Text-Transformation

**XSS-Schutz**: HTML wird via `xss`-Bibliothek sanitiert bevor es gerendert wird.

---

## 3D-Inhalte (`CmsBlockSpatialViewer`)

Rendert `.glb`-3D-Modelle via `@tresjs/cientos` (Three.js). Wird durch `isSpatial(media)` (prüft `.glb`-Extension) aktiviert.

---

## Layout-Konfiguration

`getCmsLayoutConfiguration(element)` extrahiert aus jedem CMS-Element:

```ts
{
  cssClasses: {
    // Sichtbarkeitsklassen (Tailwind):
    'max-md:hidden': boolean,      // nur Desktop
    'md:max-lg:hidden': boolean,   // nur Mobile + Desktop (kein Tablet)
    'lg:hidden': boolean,          // nur Mobile
  },
  layoutStyles: {
    backgroundColor?: string,      // CSS Hintergrundfarbe
    backgroundImage?: string,      // CSS url(...)
    backgroundSize?: string,       // "cover", "contain", "auto"
    sizingMode?: string,           // "boxed" | "full_width"
  }
}
```

`CmsPage` wandelt `sizingMode` in Tailwind-Klassen um:
- `"boxed"` → `"max-w-screen-2xl w-full mx-auto"`
- `"full_width"` → `"w-full"`
