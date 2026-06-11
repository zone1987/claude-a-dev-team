# routes.xml (`src/Resources/config/routes.xml`)

## Zweck
Lädt alle Controller-Routen über PHP-Attribute (`#[Route]`).

## Inhalt
- `<import resource="../../Controller/*Controller.php" type="attribute" />`

## Besonderheiten
- Routen werden NICHT hier definiert, sondern als Attribute in den Controllern. Neue Controller-Routen wirken automatisch, sofern die Datei auf `*Controller.php` endet.

## Bezüge
`Controller/*`.
