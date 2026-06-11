# countdown.js (`src/Resources/app/storefront/src/lib/countdown.js`)

## Zweck
**Vendor-Bibliothek** countdown.js v2.6.1 (countdownjs.org, MIT, Stephen M. McKamey). Berechnet Zeitspannen zwischen zwei Daten in wählbaren Einheiten (DAYS/HOURS/MINUTES/SECONDS …).

## Typ
- Default-Export `countdown` (Funktion + Einheiten-Konstanten als Bitflags).

## Verwendung im Plugin
`FfReservationCountdownPlugin` nutzt `countdown(currentDate, expirationDate, DAYS|HOURS|MINUTES|SECONDS)` für den Reservierungs-Countdown.

## Besonderheiten
- **Fremdcode** — nicht modifizieren; bei Bedarf upstream aktualisieren.

## Bezüge
`plugin/reservation-countdown.plugin.js`.
