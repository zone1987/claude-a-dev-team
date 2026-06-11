# BuyBoxPage (`tests/E2E/Support/BuyBoxPage.php`)

## Zweck
Page-Object für die Buy-Box (~614 Zeilen, ~40 Methoden): kapselt alle UI-Interaktionen der E2E-BuyBox-Tests (öffnen, flatpickr bedienen, Tage auswählen, Units inkrementieren, Preise/Status lesen).

## Typ
- `final class BuyBoxPage` (ctor `Client $client`).

## Methoden (Auswahl)
`open(url)`, `statusCode()`, `waitForReady()`, `isBuyBoxRendered()`, `dateInputExists()`, `openDatePicker()`, `waitForFlatpickrCalendar()`, `availableDayLabels()`, `disabledDayLabels()`, `pickFirstAvailableDay()`, `ensureOptionSelected()`, `pickDate(isoDate)`, `changeMonth(delta)`, `waitForUnitsLoaded()`, `hasUnits()`, `currentCalendarMonth()`, `incrementFirstUnitBy(n)`, `selectedUnitTotal()`, … (Preis-/Status-/Hint-Getter).

## Besonderheiten
- Zentrale Abstraktion über die Buy-Box-Selektoren/Klassen — bei DOM-/Klassenänderungen in `configurator.html.twig`/SCSS hier nachziehen.

## Bezüge
`E2E/Storefront/BuyBox/*`, `configurator.html.twig`, `buy-box.plugin.js`.
