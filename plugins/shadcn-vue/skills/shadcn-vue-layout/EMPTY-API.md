# Empty — API

## Sub-Komponenten

| Komponente | Beschreibung |
|---|---|
| `Empty` | Root-Container (zentriert, flex-col, border-dashed optional) |
| `EmptyHeader` | Bereich fuer Media, Titel, Beschreibung |
| `EmptyMedia` | Medien-Bereich (Icon, Avatar, Bild) |
| `EmptyTitle` | Titel des leeren Zustands |
| `EmptyDescription` | Beschreibung / Help-Text |
| `EmptyContent` | Bereich fuer Aktionen (Buttons, Input etc.) |

## Empty

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `class` | `string` | - | Z.B. `border` fuer Outline, `bg-muted` fuer Hintergrund |

Standard-Klassen: `flex min-w-0 flex-1 flex-col items-center justify-center gap-6 text-balance rounded-lg border-dashed p-6 text-center md:p-12`

## EmptyMedia

| Prop | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | `"default" \| "icon"` | `"default"` | Anzeige-Variante |
| `class` | `string` | - | - |

### Varianten

| Variante | Klassen |
|---|---|
| `default` | `bg-transparent` — fuer Bilder/Avatare |
| `icon` | `bg-muted text-foreground size-10 rounded-lg` — fuer Icons |

## Alle anderen Komponenten

Alle akzeptieren nur `class: string`. Keine weiteren Props.

| Komponente | Basis-Styling |
|---|---|
| `EmptyHeader` | `flex max-w-sm flex-col items-center gap-2 text-center` |
| `EmptyTitle` | `text-lg font-medium tracking-tight` |
| `EmptyDescription` | `text-muted-foreground text-sm/relaxed` + Link-Styling |
| `EmptyContent` | `flex w-full min-w-0 max-w-sm flex-col items-center gap-4` |
