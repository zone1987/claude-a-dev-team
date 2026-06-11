# CalendarTest (`tests/E2E/Storefront/BuyBox/CalendarTest.php`)

## Zweck
E2E: deaktivierte Tage nicht wählbar; Units laden in leerem Monat nicht und erscheinen nach Wahl eines verfügbaren Datums. Suite **e2e-buybox**.

## Testfälle
- `testDisabledDaysAreNotSelectable`
- `testUnitsDoNotLoadInEmptyMonthAndReturnAfterPickingAvailableDate`

## Bezüge
`date-select.plugin.js`, `buy-box.plugin.js` (`_onCalendarChanged`/empty-month).
