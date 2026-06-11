# commands.xml (`src/Resources/config/commands.xml`)

## Zweck
Registriert die beiden Konsolen-Commands.

## Definierte Services
- `PropertyGroupCleanupCommand` — `property_group.repository`; Tag `console.command` (`ff:property-group:cleanup`).
- `PriceUpdateCommand` — `product.repository`, `PriceService`, `LoggerService`; Tag `console.command` (`ff:price:update`).

## Bezüge
`Command/PropertyGroupCleanupCommand.php`, `Command/PriceUpdateCommand.php`.
