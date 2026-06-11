# Storefront main.js (`src/Resources/app/storefront/src/main.js`)

## Zweck
Einstiegspunkt des Storefront-JS. Startet den BuyBox-Loader und registriert das Reservierungs-Countdown-Plugin. Setzt das globale Debug-Flag.

## Inhalt
- `window.octoDebug = false` — globales Debug-Flag (steuert `OctoBasePlugin`-Logs).
- `BuyBoxLoader.load()` — initialisiert die sichtbare BuyBox (siehe `buy-box.loader.js`).
- `PluginManager.register('FfReservationCountdown', FfReservationCountdownPlugin, '[data-ff-reservation-countdown]')`.

## Besonderheiten
- Es werden **zwei** Storefront-Plugins genutzt: `FfBuyBox` (über Loader) und `FfReservationCountdown`.

## Bezüge
`loader/buy-box.loader.js`, `plugin/reservation-countdown.plugin.js`, `plugin/buy-box.plugin.js`.
