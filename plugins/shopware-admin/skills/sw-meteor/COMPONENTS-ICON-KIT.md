# Meteor Icon Kit — Referenz

Paket: `@shopware-ag/meteor-icon-kit`

## Icon-Namens-Schema

### Format

Icons folgen dem Schema: `{mode}-{basename}[-{size}]`

| Teil | Werte | Beschreibung |
|---|---|---|
| `mode` | `regular`, `solid` | Linienstil oder gefüllt |
| `basename` | z.B. `home`, `save`, `shopping-cart` | Icon-Name (Kebab-Case) |
| `size` | `s`, `xs` (optional) | Kleinere Variante |

**Beispiele:**
- `regular-home` — Home-Icon, Linienstil
- `solid-save` — Speichern-Icon, gefüllt
- `solid-filter-s` — Filter-Icon gefüllt, kleine Variante
- `regular-search-xs` — Such-Icon, extra-klein

### Bestand

- **regular**: 471 Icons
- **solid**: 435 Icons

### Verwendung in `mt-icon`

```html
<mt-icon name="solid-save" size="24px" />
<mt-icon name="regular-shopping-cart" size="16" />
```

Das Präfix `solid-` oder `regular-` im Namen überschreibt den `mode`-Prop.

### Verwendung als CSS-Klasse / Font

Das Icon-Kit liefert eine CSS-Datei:

```css
/* Einbinden */
@import '@shopware-ag/meteor-icon-kit/icons/meteor-icon-kit.scss';
/* oder */
@import '@shopware-ag/meteor-icon-kit/icons/meteor-icon-kit-aa7f6c2f67a2943b68c63f61fb088f50.css';
```

### Häufig genutzte Icons (Auswahl)

| Name | Beschreibung |
|---|---|
| `solid-home` / `regular-home` | Startseite |
| `solid-save` / `regular-save` | Speichern |
| `solid-search` / `regular-search` | Suche |
| `solid-filter-s` | Filter |
| `solid-plus-s` | Hinzufügen |
| `solid-trash` | Löschen |
| `solid-pencil-s` | Bearbeiten |
| `solid-times` | Schließen |
| `solid-check` | Bestätigen |
| `solid-info-circle` | Info |
| `solid-exclamation-triangle` | Warnung |
| `solid-exclamation-circle` | Fehler |
| `solid-chevron-right-xs` | Pfeil rechts |
| `solid-chevron-down-xs` | Pfeil unten |
| `solid-ellipsis-h-s` | Mehr-Menü (3 Punkte) |
| `solid-eye` | Sichtbar |
| `solid-eye-slash` | Ausgeblendet |
| `solid-download` | Download |
| `solid-upload` | Upload |
| `solid-shopping-cart` | Warenkorb |
| `solid-tag` | Tag/Label |
| `solid-user` | Benutzer |
| `solid-users` | Benutzergruppe |
| `solid-cog` | Einstellungen |
| `regular-analytics` | Statistiken |
| `solid-bell` | Benachrichtigung |
| `regular-calendar` | Kalender |
| `solid-image` | Bild |
| `solid-list` | Liste |
| `regular-table` | Tabelle |

### Meta-Datei

Die vollständige Icon-Metadaten-Datei liegt unter:
`icons/meta.json` — enthält für jedes Icon: `name`, `basename`, `mode`, `size`, `tags`, `sizes`, `modes`, `related`.
