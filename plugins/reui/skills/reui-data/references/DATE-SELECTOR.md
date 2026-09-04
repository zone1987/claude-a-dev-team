# Date Selector

Custom Shadcn Date Selector for React and Tailwind CSS. A universal date selector component with
multiple period types, filter modes, and flexible display options.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Examples](#examples)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/date-selector
```

(npm/yarn/bun equivalents: `npx shadcn@latest add @reui/date-selector`, `yarn dlx shadcn@latest add
@reui/date-selector`, `bunx shadcn@latest add @reui/date-selector`.)

## Usage

```tsx
import {
  DateSelector,
  type DateSelectorValue,
} from "@/components/reui/date-selector"
```

Basic shape:

```tsx
const [value, setValue] = useState<DateSelectorValue | undefined>()

return <DateSelector value={value} onChange={setValue} label="Due date" />
```

## API Reference

### DateSelector

The main component for selecting dates and time periods.

| Prop | Type | Default | Description |
|---|---|---|---|
| `value` | `DateSelectorValue` | — | The current value of the selector. |
| `onChange` | `(value: DateSelectorValue) => void` | — | Callback fired when the value changes. |
| `allowRange` | `boolean` | `true` | Whether to allow selecting date ranges (using "between" operator). |
| `periodTypes` | `DateSelectorPeriodType[]` | — | List of available period types (day, month, etc.). |
| `defaultPeriodType` | `DateSelectorPeriodType` | `"day"` | The initial period type. |
| `defaultFilterType` | `DateSelectorFilterType` | `"is"` | The initial filter operator. |
| `presetMode` | `DateSelectorFilterType` | — | If set, locks the selector to this specific filter mode. |
| `showInput` | `boolean` | `true` | Whether to show the text input field above the selector. |
| `showTwoMonths` | `boolean` | `true` | Whether to show two months in the calendar view (desktop only). |
| `label` | `string` | — | Optional label to display above the filter toggle. |
| `yearRange` | `number` | `10` | The number of years to show in the year/month/quarter list. |
| `baseYear` | `number` | `new Date().getFullYear()` | The reference year for the year selection list. |
| `minYear` | `number` | `2015` | The minimum selectable year. |
| `maxYear` | `number` | `2026` | The maximum selectable year. |
| `i18n` | `Partial` | — | Custom labels and operators for internationalization. |
| `inputHint` | `string` | — | Optional hint text to display in the input field when empty and focused. |
| `dayDateFormat` | `string` | `"MM/dd/yyyy"` | The format used to display single days. |
| `className` | `string` | — | Additional CSS classes for the container. |

The upstream `i18n` prop type is printed as literally `Partial` (no type argument shown) on the page.

Note: the "With i18n Support" example also passes a `weekStartsOn` prop to `<DateSelector>`
(`weekStartsOn={currentMeta.weekStartsOn}`, values `0` or `1`). This prop is used in the example code
but the page's API Reference table does not list it — the upstream page is silent on its type,
default, and full accepted range.

### Interfaces

#### DateSelectorValue

The structure of the value returned by the `onChange` callback.

| Property | Type | Description |
|---|---|---|
| `period` | `DateSelectorPeriodType` | The selected period type (`day`, `month`, `quarter`, `half-year`, `year`). |
| `operator` | `DateSelectorFilterType` | The selected operator (`is`, `before`, `after`, `between`). |
| `startDate` | `Date` | The selected start date (for `day` period). |
| `endDate` | `Date` | The selected end date (for `day` period range). |
| `year` | `number` | The selected year. |
| `month` | `number` | The selected month (0-11). |
| `quarter` | `number` | The selected quarter (0-3). |
| `halfYear` | `number` | The selected half-year (0-1). |
| `rangeStart` | `{ year: number; value: number }` | The start of a period range. |
| `rangeEnd` | `{ year: number; value: number }` | The end of a period range. |

The page does not print a table for `DateSelectorPeriodType` or `DateSelectorFilterType` as standalone
types — their member values are only stated inline: period types `day`, `month`, `quarter`,
`half-year`, `year`; filter types `is`, `before`, `after`, `between` (seen also as translation keys
`is`/`before`/`after`/`between` in the i18n example).

Other exports used in examples but not tabulated on the page: `formatDateValue(value, i18n?,
dateFormat?)` (formats a `DateSelectorValue` to a display string) and `DEFAULT_DATE_SELECTOR_I18N`
(the default i18n config object, spread as the base for custom translations) and the
`DateSelectorI18nConfig` type.

## Examples

### With Popover

Wraps `DateSelector` in a `Popover` with a button trigger showing the formatted value (via
`formatDateValue`), and Apply/Cancel actions that stage changes in local state before committing:

```tsx
"use client"

import { useEffect, useState } from "react"
import {
  DateSelector,
  formatDateValue,
  type DateSelectorValue,
} from "@/components/reui/date-selector"
import { Button } from "@/components/ui/button"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
import { Separator } from "@/components/ui/separator"
import { CalendarIcon } from 'lucide-react'

export function Pattern() {
  const [value, setValue] = useState<DateSelectorValue | undefined>()
  const [open, setOpen] = useState(false)
  const [internalValue, setInternalValue] = useState<
    DateSelectorValue | undefined
  >(value)
  const formattedValue = value ? formatDateValue(value) : ""
  const displayText = formattedValue || "Select a date"

  useEffect(() => {
    if (open) {
      setInternalValue(value)
    }
  }, [open, value])

  const handleApply = () => {
    setValue(internalValue)
    setOpen(false)
  }

  const handleCancel = () => {
    setInternalValue(value)
    setOpen(false)
  }

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger
        render={
          <Button variant="outline" className="w-56 justify-start">
            <CalendarIcon />
            {displayText}
          </Button>
        }
      />
      <PopoverContent className="w-auto gap-3 p-0" align="start" sideOffset={4}>
        <div className="p-3">
          <DateSelector
            value={internalValue}
            onChange={setInternalValue}
            allowRange={true}
            label="Due date"
            inputHint="Try: 2025, Q4, 05/10/2025"
          />
        </div>
        <Separator className="p-0" />
        <div className="flex justify-end gap-2 p-3 pt-0">
          <Button variant="outline" onClick={handleCancel}>
            Cancel
          </Button>
          <Button onClick={handleApply}>Apply</Button>
        </div>
      </PopoverContent>
    </Popover>
  )
}
```

### With Dialog

Same staged-state pattern as the Popover example, but hosted in a `Dialog` with `showInput={true}` on
`DateSelector` and no range allowance override:

```tsx
"use client"

import { useEffect, useState } from "react"
import {
  DateSelector,
  formatDateValue,
  type DateSelectorValue,
} from "@/components/reui/date-selector"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { CalendarIcon } from 'lucide-react'

export function Pattern() {
  const [value, setValue] = useState<DateSelectorValue | undefined>()
  const [open, setOpen] = useState(false)
  const [internalValue, setInternalValue] = useState<
    DateSelectorValue | undefined
  >(value)
  const formattedValue = value ? formatDateValue(value) : ""
  const displayText = formattedValue || "Select a date"

  useEffect(() => {
    if (open) {
      setInternalValue(value)
    }
  }, [open, value])

  const handleApply = () => {
    if (internalValue) {
      setValue(internalValue)
    }
    setOpen(false)
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger
        render={
          <Button variant="outline" className="w-56 justify-start">
            <CalendarIcon />
            {displayText}
          </Button>
        }
      />
      <DialogContent className="sm:max-w-lg" showCloseButton={false}>
        <DialogHeader>
          <DialogTitle>Select Due Date</DialogTitle>
        </DialogHeader>
        <DateSelector
          value={internalValue}
          onChange={setInternalValue}
          showInput={true}
        />
        <DialogFooter>
          <DialogClose render={<Button variant="outline">Cancel</Button>} />
          <Button onClick={handleApply}>Apply</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
```

### With i18n Support

A language switcher (`DropdownMenu`) driving `DateSelector`'s `i18n`, `dayDateFormat`, and
`weekStartsOn` props. Demonstrates building a full `DateSelectorI18nConfig` per locale by spreading
`DEFAULT_DATE_SELECTOR_I18N` with per-language overrides (`selectDate`, `apply`, `cancel`, `clear`,
`today`, `filterTypes.{is,before,after,between}`, `periodTypes.{day,month,quarter,halfYear,year}`,
`months`, `monthsShort`, `quarters`, `halfYears`, `weekdays`, `weekdaysShort`, `placeholder`,
`rangePlaceholder`). Languages shown: English (`en`), Spanish (`es`), French (`fr`), German (`de`).

```tsx
"use client"

import { useEffect, useMemo, useState } from "react"
import {
  DateSelector,
  DEFAULT_DATE_SELECTOR_I18N,
  formatDateValue,
  type DateSelectorI18nConfig,
  type DateSelectorValue,
} from "@/components/reui/date-selector"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { CalendarIcon, ChevronDownIcon } from 'lucide-react'

// Helper function to create i18n config from translations
function createI18nConfig(
  translations: Partial<DateSelectorI18nConfig>
): DateSelectorI18nConfig {
  return { ...DEFAULT_DATE_SELECTOR_I18N, ...translations }
}

// Language-specific translations
const translations: Record<string, Partial<DateSelectorI18nConfig>> = {
  es: {
    selectDate: "Seleccionar fecha",
    apply: "Aplicar",
    cancel: "Cancelar",
    clear: "Limpiar",
    today: "Hoy",
    filterTypes: { is: "es", before: "antes de", after: "después de", between: "entre" },
    periodTypes: { day: "Día", month: "Mes", quarter: "Trimestre", halfYear: "Semestre", year: "Año" },
    months: ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    monthsShort: ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"],
    quarters: ["T1", "T2", "T3", "T4"],
    halfYears: ["S1", "S2"],
    weekdays: ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"],
    weekdaysShort: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sá"],
    placeholder: "Seleccionar fecha...",
    rangePlaceholder: "Seleccionar rango de fechas...",
  },
  fr: {
    selectDate: "Sélectionner une date",
    apply: "Appliquer",
    cancel: "Annuler",
    clear: "Effacer",
    today: "Aujourd'hui",
    filterTypes: { is: "est", before: "avant", after: "après", between: "entre" },
    periodTypes: { day: "Jour", month: "Mois", quarter: "Trimestre", halfYear: "Semestre", year: "Année" },
    months: ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"],
    monthsShort: ["Jan","Fév","Mar","Avr","Mai","Juin","Juil","Aoû","Sep","Oct","Nov","Déc"],
    quarters: ["T1", "T2", "T3", "T4"],
    halfYears: ["S1", "S2"],
    weekdays: ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"],
    weekdaysShort: ["Di", "Lu", "Ma", "Me", "Je", "Ve", "Sa"],
    placeholder: "Sélectionner une date...",
    rangePlaceholder: "Sélectionner une plage de dates...",
  },
  de: {
    selectDate: "Datum auswählen",
    apply: "Anwenden",
    cancel: "Abbrechen",
    clear: "Löschen",
    today: "Heute",
    filterTypes: { is: "ist", before: "vor", after: "nach", between: "zwischen" },
    periodTypes: { day: "Tag", month: "Monat", quarter: "Quartal", halfYear: "Halbjahr", year: "Jahr" },
    months: ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"],
    monthsShort: ["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"],
    quarters: ["Q1", "Q2", "Q3", "Q4"],
    halfYears: ["H1", "H2"],
    weekdays: ["Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag"],
    weekdaysShort: ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"],
    placeholder: "Datum auswählen...",
    rangePlaceholder: "Datumsbereich auswählen...",
  },
}

// Internationalization configurations
const i18nConfigs: Record<string, DateSelectorI18nConfig> = {
  en: DEFAULT_DATE_SELECTOR_I18N,
  es: createI18nConfig(translations.es),
  fr: createI18nConfig(translations.fr),
  de: createI18nConfig(translations.de),
}

// Language metadata
const languageMetadata = {
  en: { label: "English", flag: "🇺🇸", dateFormat: "MM/dd/yyyy", weekStartsOn: 0 as const,
    ui: { label: "Due date", hint: "Try: 2025, Q4, 05/10/2025", placeholder: "Select a date" } },
  es: { label: "Español", flag: "🇪🇸", dateFormat: "dd/MM/yyyy", weekStartsOn: 1 as const,
    ui: { label: "Fecha de vencimiento", hint: "Prueba: 2025, T4, 05/10/2025", placeholder: "Seleccionar una fecha" } },
  fr: { label: "Français", flag: "🇫🇷", dateFormat: "dd/MM/yyyy", weekStartsOn: 1 as const,
    ui: { label: "Date d'échéance", hint: "Essayez: 2025, T4, 05/10/2025", placeholder: "Sélectionner une date" } },
  de: { label: "Deutsch", flag: "🇩🇪", dateFormat: "dd.MM.yyyy", weekStartsOn: 1 as const,
    ui: { label: "Fälligkeitsdatum", hint: "Versuchen Sie: 2025, Q4, 05.10.2025", placeholder: "Datum auswählen" } },
}

// Language options for the selector
const languageOptions = Object.entries(languageMetadata).map(
  ([value, meta]) => ({ value, label: meta.label, flag: meta.flag })
)

export function Pattern() {
  const [value, setValue] = useState<DateSelectorValue | undefined>()
  const [open, setOpen] = useState(false)
  const [internalValue, setInternalValue] = useState<
    DateSelectorValue | undefined
  >(value)
  const [currentLanguage, setCurrentLanguage] =
    useState<keyof typeof languageMetadata>("fr")

  const currentMeta = useMemo(
    () => languageMetadata[currentLanguage] || languageMetadata.en,
    [currentLanguage]
  )
  const currentI18n = useMemo(
    () => i18nConfigs[currentLanguage] || i18nConfigs.en,
    [currentLanguage]
  )

  useEffect(() => {
    if (open) {
      setInternalValue(value)
    }
  }, [open, value])

  const formattedValue = useMemo(
    () =>
      value ? formatDateValue(value, currentI18n, currentMeta.dateFormat) : "",
    [value, currentI18n, currentMeta.dateFormat]
  )
  const displayText = formattedValue || currentMeta.ui.placeholder

  const handleApply = () => {
    setValue(internalValue)
    setOpen(false)
  }

  const handleCancel = () => {
    setInternalValue(value)
    setOpen(false)
  }

  return (
    <div className="flex h-full w-full grow flex-col items-stretch gap-4">
      <div className="flex w-full justify-end">
        <DropdownMenu>
          <DropdownMenuTrigger
            render={
              <Button
                variant="outline"
                size="sm"
                className="flex items-center gap-2"
              >
                <span>{currentMeta.flag}</span>
                <span>{currentMeta.label}</span>
                <ChevronDownIcon />
              </Button>
            }
          />
          <DropdownMenuContent align="start">
            {languageOptions.map((lang) => (
              <DropdownMenuItem
                key={lang.value}
                onClick={() =>
                  setCurrentLanguage(
                    lang.value as keyof typeof languageMetadata
                  )
                }
                className="flex items-center gap-2"
              >
                <span>{lang.flag}</span>
                <span>{lang.label}</span>
              </DropdownMenuItem>
            ))}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      <div className="flex grow items-center justify-center">
        <Dialog open={open} onOpenChange={setOpen}>
          <DialogTrigger
            render={
              <Button variant="outline" className="w-56 justify-start">
                <CalendarIcon />
                {displayText}
              </Button>
            }
          />
          <DialogContent className="sm:max-w-lg" showCloseButton={false}>
            <DialogHeader>
              <DialogTitle>{currentMeta.ui.label}</DialogTitle>
            </DialogHeader>
            <DateSelector
              value={internalValue}
              onChange={setInternalValue}
              showInput={true}
              i18n={currentI18n}
              dayDateFormat={currentMeta.dateFormat}
              weekStartsOn={currentMeta.weekStartsOn}
            />
            <DialogFooter>
              <DialogClose
                render={
                  <Button variant="outline" onClick={handleCancel}>
                    {currentI18n.cancel}
                  </Button>
                }
              />
              <Button onClick={handleApply}>{currentI18n.apply}</Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>
      </div>
    </div>
  )
}
```

### API-reference default example

The API Reference section on the page also carries its own runnable demo, printing the live value as
formatted JSON (dates rendered via `date-fns` `format(val, "MM/dd/yyyy")`):

```tsx
"use client"

import { useState } from "react"
import {
  DateSelector,
  type DateSelectorValue,
} from "@/components/reui/date-selector"
import { format } from "date-fns"
import { Card, CardContent } from "@/components/ui/card"

export function Pattern() {
  const [value, setValue] = useState<DateSelectorValue | undefined>()

  return (
    <div className="flex w-full flex-col items-center gap-5">
      <Card className="p-0">
        <CardContent className="p-3">
          <DateSelector
            value={value}
            onChange={setValue}
            label="Due date"
            inputHint="Try: 2025, Q4, 05/10/2025"
          />
        </CardContent>
      </Card>
      {value ? (
        <pre className="bg-muted w-full overflow-auto rounded-md p-3 font-mono text-xs md:w-[500px]">
          {JSON.stringify(
            value,
            (key, val) => {
              if (val instanceof Date) {
                return format(val, "MM/dd/yyyy")
              }
              return val
            },
            2
          )}
        </pre>
      ) : (
        <div className="text-muted-foreground text-sm">
          No value selected. Select a date to see the debug information.
        </div>
      )}
    </div>
  )
}
```

## Base UI vs Radix UI

Detect your build from `components.json` -> `style`: `base-nova` -> Base UI (this file's default),
`radix-nova` -> Radix UI.

| | Base UI | Radix UI |
|---|---|---|
| Install | `pnpm dlx shadcn@latest add @reui/date-selector` | `pnpm dlx shadcn@latest add @reui/r-date-selector` |
| Import path | `@/components/reui/date-selector` | `@/components/reui/r-date-selector` |

Real behavioural/API difference — composition idiom on every trigger/close component used alongside
`DateSelector` in the examples (`PopoverTrigger`, `DialogTrigger`, `DialogClose`,
`DropdownMenuTrigger`):

- Base UI: `render={<Button ...>...</Button>}` prop.
- Radix UI: `asChild` prop with the `<Button>` as a direct child.

Example (Popover trigger), Base UI:

```tsx
<PopoverTrigger
  render={
    <Button variant="outline" className="w-56 justify-start">
      <CalendarIcon />
      {displayText}
    </Button>
  }
/>
```

Radix UI:

```tsx
<PopoverTrigger asChild>
  <Button variant="outline" className="w-56 justify-start">
    <CalendarIcon />
    {displayText}
  </Button>
</PopoverTrigger>
```

The `DateSelector` component's own API Reference table (props and `DateSelectorValue` interface) is
identical between the two builds — the upstream pages state no prop or default differences for
`DateSelector` itself.

## Source

- https://reui.io/docs/components/base/date-selector (Base UI)
- https://reui.io/docs/components/radix/date-selector (Radix UI)
- Mirrored 2026-09-04.
