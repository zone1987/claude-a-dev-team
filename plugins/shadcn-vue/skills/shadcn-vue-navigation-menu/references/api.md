# NavigationMenu — API-Referenz

## NavigationMenu (Root)

Basiert auf reka-ui `NavigationMenuRoot`. Enthalt automatisch `NavigationMenuViewport`.

### Props

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `viewport` | `boolean` | `true` | Viewport-Komponente einschliessen |
| `class` | `HTMLAttributes["class"]` | — | Zusatzliche CSS-Klassen |
| Alle `NavigationMenuRootProps` | — | Weitergeleitet |

### Emits

| Event | Typ | Beschreibung |
|---|---|---|
| Alle `NavigationMenuRootEmits` | — | Weitergeleitet |

---

## NavigationMenuList

Horizontale Liste der Menu-Eintrager.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `NavigationMenuListProps` | — | Weitergeleitet |

---

## NavigationMenuItem

Einzelner Navigationseintrag. Kann `Trigger + Content` oder direkten `Link` enthalten.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `value` | `string` | Eindeutiger Wert (fur controlled mode) |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## NavigationMenuTrigger

Button mit ChevronDown-Icon, das sich bei `data-[state=open]` dreht.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `NavigationMenuTriggerProps` | — | Weitergeleitet |

---

## NavigationMenuContent

Dropdown-Panel-Inhalt. Animationen basieren auf `data-motion`.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |
| Alle `NavigationMenuContentProps` | — | Weitergeleitet |

---

## NavigationMenuLink

Aktiver-Zustand-bewusster Link. Erkennt `data-active` automatisch.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `active` | `boolean` | Aktiver Zustand |
| `asChild` | `boolean` | Rendert als Kind (fur `<a>`-Tags) |
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## NavigationMenuViewport

Animiertes schwebendes Fenster. Normalerweise automatisch durch `NavigationMenu` eingebunden.

### Props

| Prop | Typ | Beschreibung |
|---|---|---|
| `class` | `HTMLAttributes["class"]` | Zusatzliche CSS-Klassen |

---

## NavigationMenuIndicator

Animierter Pfeil-Indikator unter dem aktiven Trigger.

---

## Exportierte Utility

```ts
export const navigationMenuTriggerStyle = cva("...")
// Gibt CVA-Klassennamen zuruck, verwendbar auf eigenstandigen Links
```

### Verwendung

```vue
<NavigationMenuLink
  :class="navigationMenuTriggerStyle()"
  href="/docs"
>
  Documentation
</NavigationMenuLink>
```

## reka-ui Referenz
- https://reka-ui.com/docs/components/navigation-menu
