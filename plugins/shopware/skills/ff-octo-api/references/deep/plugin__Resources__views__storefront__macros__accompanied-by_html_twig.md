# accompanied-by.html.twig (`.../storefront/macros/accompanied-by.html.twig`)

## Zweck
Twig-Macro, das für eine Unit (z.B. CHILD/INFANT) den Begleitpersonen-Hinweis rendert („muss von … begleitet werden"), inkl. Ratio-Denominator.

## Macro
- `accompanied_by(units, unit)`:
  - filtert `units` auf `unit.restrictions.accompaniedBy`-IDs.
  - baut Text aus `OctoApi.accompaniedByType.{type}` (mit Ratio), verbunden per `,`/`oder`.
  - rendert `OctoApi.accompaniedByMessage` nur wenn `unit.type != 'OTHER'` und Begleit-Units vorhanden.

## Besonderheiten
- Entspricht der Backend-Begleit-Logik (`AvailbilityController` setzt `accompaniedBy`) und der Buy-Btn-Standalone-Regel.

## Bezüge
`widget/unit-widget.html.twig`, `Controller/AvailbilityController.php`, `plugin/buy-btn.plugin.js`.
