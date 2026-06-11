# checkout.xml (`src/Resources/config/checkout.xml`)

## Zweck
Registriert den `OctoCartCollector` als Cart-Processor **und** Cart-Collector mit **Priority 6000**.

## Definierte Services
- `FfOctoApi\Core\Checkout\Cart\OctoCartCollector`
  - Argumente: `RequestStack`, `PriceDefinitionFactory`, `LoggerService`.
  - Tags: `shopware.cart.processor` (priority **6000**), `shopware.cart.collector` (priority **6000**).

## Besonderheiten / Fallstricke
- **Priority 6000** ist hier definiert (nicht in der Klasse). Hohe Priorität → läuft früh, kann OCTO-Preise vor anderen Prozessoren setzen.

## Bezüge
`Core/Checkout/Cart/OctoCartCollector.php`, `../price-calculation.md`.
