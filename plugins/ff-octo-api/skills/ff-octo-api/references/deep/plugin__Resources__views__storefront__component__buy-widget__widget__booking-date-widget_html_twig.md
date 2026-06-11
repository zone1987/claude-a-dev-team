# booking-date-widget.html.twig (`.../buy-widget/widget/booking-date-widget.html.twig`)

## Zweck
Rendert das Datums-Eingabefeld der Buy-Box (`data-ff-date-select` für flatpickr) inkl. Optionen (Locale, Default-Datum aus Session, Warning-Icon, „keine Slots"-Snippet, Session-Routen).

## Block
- `octo_configurator__booking_date`

## Inhalt
- Liest `octo-product-session-{product.id}` (Default-Datum).
- `dateSelectOptions` (locale, productId, defaultDate, `snippets.noAvailableSlotsHint` = `OctoApi.flatpickr.noAvailableSlots`, warningIcon, session-Routen).
- `<input data-ff-date-select data-ff-date-select-options="…">` + Label `OctoApi.configuratorDetails.bookingDateLabel`.

## Bezüge
`plugin/date-select.plugin.js`, `configurator.html.twig`.
