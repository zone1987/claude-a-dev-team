# Pagination — API-Referenz

## Pagination (Root)

Basiert auf reka-ui `PaginationRoot`.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `page` | `number` | — | Aktuelle Seite (kontrolliert) |
| `defaultPage` | `number` | `1` | Startseite (unkontrolliert) |
| `total` | `number` | — | Gesamtzahl der Eintrager |
| `itemsPerPage` | `number` | `10` | Eintrager pro Seite |
| `siblingCount` | `number` | `1` | Anzahl sichtbarer Seiten neben aktueller |
| `showEdges` | `boolean` | `false` | Erste/letzte Seite immer anzeigen |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| `update:page` | `number` | Seitenänderung |

### Slot Props

```ts
// v-slot="{ page, pages }"
// pages: Array of { type: 'page' | 'ellipsis', value?: number }
```

---

## PaginationContent

Basiert auf reka-ui `PaginationList`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

### Slot Props

```ts
// v-slot="{ items }"
```

---

## PaginationItem

Basiert auf reka-ui `PaginationListItem`.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `value` | `number` | — | Seitennummer |
| `isActive` | `boolean` | `false` | Aktive Seite (outline variant) |
| `size` | `ButtonVariants["size"]` | `"icon"` | Buttongrosse |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

---

## PaginationEllipsis

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `index` | `number` | Eindeutige Position (required) |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## PaginationPrevious / PaginationNext / PaginationFirst / PaginationLast

Alle basieren auf den entsprechenden reka-ui-Primitiven.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `size` | `ButtonVariants["size"]` | `"default"` | Buttongrosse |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |

---

## reka-ui Referenz
- https://reka-ui.com/docs/components/pagination
