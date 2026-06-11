# CalendarServiceTest (`tests/Unit/Service/CalendarServiceTest.php`)

## Zweck
Unit-Tests für `CalendarService` (Offline-Kalendergenerierung). Testsuite **unit**.

## Getestete Klasse
`FfOctoApi\Service\CalendarService`.

## Testfälle
- `testReturnsEmptyArrayWhenProductMissing`
- `testReturnsEmptyArrayForOnlineClient` — nur Offline-Clients.
- `testReturnsEmptyArrayWhenOptionNotFound`
- `testGeneratesCalendarUsingSeasonStartTimes` — Saison-Startzeiten.
- `testFallsBackToAvailabilityWeekdaysOutsideAllSeasons` — globale Wochentage außerhalb Saison.
- `testEachCalendarEntryHasRequiredStructure` — Tageseintrag-Struktur.

## Bezüge
`Service/CalendarService.php`.
