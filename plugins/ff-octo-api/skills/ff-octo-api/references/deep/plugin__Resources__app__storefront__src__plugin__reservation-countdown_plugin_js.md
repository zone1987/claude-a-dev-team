# FfReservationCountdownPlugin (`src/Resources/app/storefront/src/plugin/reservation-countdown.plugin.js`)

## Zweck
Zeigt im Warenkorb/Offcanvas einen Countdown bis zum Ablauf der OCTO-Reservierung an und **entfernt das LineItem automatisch**, wenn die Reservierung abläuft (+ Benachrichtigung).

## Typ & Vererbung
- `export default class FfReservationCountdownPlugin extends Plugin`
- Registriert auf `[data-ff-reservation-countdown]` (in `main.js` UND als Child im Buy-Box-Registry).

## Optionen (`static options`)
`reservationExpiresAt` (null), `snippet` (''), `lineItemLabel` (null), `routes.notify` (null).

## Methoden
- `async init()` — `update()`, dann Interval (1s).
- `async update()` — bei Ablauf: Interval stoppen + `removeLineItem()`. Sonst Countdown via `lib/countdown` rendern (`%time%`-Snippet); ab < 2 min Rest: Alert von `alert-info` → `alert-warning`.
- `async removeLineItem()` — sucht das LineItem-Remove-Form, postet es (`X-Requested-With`), danach `notify()`.
- `async notify()` — POST auf `routes.notify` mit Snippet `OctoApi.offcanvas.lineItem.deleted` (+ `%productName%`).

## Besonderheiten / Fallstricke
- Auto-Remove bei Ablauf — kann Warenkorbpositionen ohne Nutzeraktion entfernen.
- `reservationExpiresAt` kommt aus dem LineItem-Payload (`reservation.utcExpiresAt`).

## Bezüge
`lib/countdown.js`, `main.js`, `buy-box.plugin.js`, `Controller/NotificationController.php`, Twig Line-Item.
