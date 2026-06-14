# Item — API-Referenz

## Item (Root)

Basiert auf reka-ui `Primitive` — polymorphes Element.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `as` | `string \| Component` | `"div"` | HTML-Tag oder Komponente |
| `asChild` | `boolean` | `false` | Rendert als Kind-Element (Slot-basiert) |
| `variant` | `"default" \| "outline" \| "muted"` | `"default"` | Visueller Stil |
| `size` | `"default" \| "sm"` | `"default"` | Grosse/Abstande |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

### Slots

| Slot | Beschreibung |
|---|---|
| default | Beliebige Item-Sub-Komponenten |

---

## ItemGroup

```html
<div role="list" data-slot="item-group">
```

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## ItemContent

Flex-Spalte, wachst auf `flex-1`. Zweite `ItemContent` wird automatisch auf `flex-none` gesetzt.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## ItemTitle

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## ItemDescription

Rendert als `<p>`. Links werden automatisch unterstrichen.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## ItemMedia

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | `"default" \| "icon" \| "image"` | `"default"` | Layout-Typ |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

### itemMediaVariants Details

| Variant | Grosse | Beschreibung |
|---|---|---|
| `default` | — | Kein eigenes Layout |
| `icon` | `size-8` | Quadrat mit Border + muted bg, SVG 4x4 |
| `image` | `size-10` | Quadrat, overflow hidden, `img` fullt aus |

---

## ItemActions

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## ItemHeader

Volle Breite (`basis-full`), `justify-between`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## ItemFooter

Volle Breite (`basis-full`), `justify-between`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## ItemSeparator

Basiert auf `Separator` (reka-ui), immer `orientation="horizontal"`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `SeparatorProps` | — | Werden weitergeleitet |

---

## Exportierte Typen

```ts
import type { ItemVariants, ItemMediaVariants } from "@/components/ui/item"
```

## reka-ui Referenz
- https://reka-ui.com/docs/utilities/primitive
