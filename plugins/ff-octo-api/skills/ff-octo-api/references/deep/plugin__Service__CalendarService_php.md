# CalendarService (`src/Service/CalendarService.php`)

## Zweck
Erzeugt für **Offline-Produkte** (RheinKurier) lokal einen Verfügbarkeitskalender aus den persistierten `ff_octo_product.product`-Daten (Wochentage, Startzeiten, Saisons), da kein OCTO-`availability/calendar`-Endpunkt zur Verfügung steht. `declare(strict_types=1)`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `class CalendarService`

## Konstanten
`DEFAULT_WEEKDAYS` (alle 7 → false), `STATUS_AVAILABLE`/`STATUS_CLOSED` (`AVAILABLE`/`CLOSED`), `MESSAGE_AVAILABLE`/`MESSAGE_CLOSED`, `DEFAULT_TIMEZONE` (`Europe/Berlin`).

## Konstruktor / DI
`OctoLoggerInterface $logger`, `OctoApiClientRegistry $clientRegistry`, `EntityRepository $octoProductRepository`.

## Methoden
- `private getOctoProduct(octoProductId, ?context): ?OctoProductEntity` — sucht `ff_octo_product` per `uuid`.
- `getCalendar(octoProductId, octoOptionId, localDateStart, localDateEnd, ?context): array` (public):
  - lädt OctoProduct; **nur wenn Offline-Client** (sonst `[]`).
  - findet Option (`findOption`), liest `availabilityWeekdays`, `availabilityLocalStartTimes`, `availabilitySeasons`, Timezone (Default Europe/Berlin).
  - iteriert Tag für Tag: aktive Saison (`findActiveSeason`), Schedule (`resolveSchedule`), Tageseintrag (`buildDayEntry`). Bei Exception error + `[]`.
- `private findOption(product, optionId): ?array` — Option per `id`.
- `private findActiveSeason(date, seasons, productUuid, optionId): ?array` — Saison mit `start <= date <= end`; **loggt Warnung bei überlappenden Saisons**, nimmt erste.
- `private resolveSchedule(?season, globalWeekdays, globalStartTimes): array` — Saison-`day`/`startTimes` überschreiben global.
- `private buildDayEntry(date, schedule): array` — `localDate`, `availabilityLocalStartTimes` (wenn offen), `available`, `status`/`statusCode`/`statusMessage`.
- `private isOfflineClient(octoProduct): bool` — über Registry.

## Besonderheiten
- Reiner Offline-Pfad; wird vom `AvailbilityController::availabilityCalendar` für Offline-Clients genutzt.

## Bezüge
`OctoApiClientRegistry`, `OctoProductEntity`, `Controller/AvailbilityController.php`, `../appserver-integration.md`.
