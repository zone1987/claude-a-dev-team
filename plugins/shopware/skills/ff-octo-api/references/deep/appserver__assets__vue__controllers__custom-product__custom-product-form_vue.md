# custom-product-form.vue (`ResubmissionAppServer/assets/vue/controllers/custom-product/custom-product-form.vue`)

## Zweck
Das zentrale RheinKurier-Produktformular (Add/Edit) in der Admin-Iframe. Erfasst Name und beliebig viele Optionen mit Verfügbarkeits-Konfiguration (Wochentage, Startzeiten, Dauer, Stornofristen, Saisons) und Units (Preise/Währung). Sendet die Optionen als JSON an `CustomProductController`.

## Typ
- Vue 3 SFC (Composition API, Meteor Components `MtCard`/`MtTextField`/…). ~mehrere hundert Zeilen.

## Props
- `urlParams` (String), `mode` (`add`/`edit`), `templateId`, `template`.

## Struktur/Verhalten (Auswahl)
- `form.name`, `form.options[]`; pro Option: `title`, `availabilityWeekdays` (DaySelector), `availabilityLocalStartTimes` (StartTimeSelector), `durationAmount/Unit` + `cancellationCutoffAmount/Unit` (DurationInput), `availabilitySeasons[]` (je Saison day/startTimes/duration), Units (UnitForm).
- Verschachtelte `CollapsibleSection`s; `expandedOptionIndex`, `expandedAvailability*`-State.
- Add/Edit, Option/Season hinzufügen/entfernen.
- Speichern: POST der Optionen (JSON) an `/customProductTemplate/add` bzw. `/edit`.

## Besonderheiten / Fallstricke
- Die hier erzeugte `options`-Struktur wird 1:1 zur `ffOctoProduct.product.options` (siehe `AdminApiClient::addProduct`) → muss zur Plugin-Erwartung (`OctoProductDefinition`, `PriceService`, `CalendarService`) passen.
- Saisons/Wochentage/Startzeiten steuern den offline berechneten Kalender (`CalendarService`).

## Bezüge
`components/{CollapsibleSection,DaySelector,DurationInput,StartTimeSelector,UnitForm}.vue`, `add.vue`/`edit.vue`, `Controller/CustomProductController.php`, FfOctoApi `CalendarService`/`PriceService`.
