# PropertyService (`src/Service/PropertyService.php`)

## Zweck
Erzeugt aus den Optionen eines OCTO-API-Produkts eine Shopware-Property-Group inkl. -Options (für Varianten) mit deterministischen IDs; räumt verwaiste Optionen auf. Liefert auch die ID-Berechnung, die `PriceService` fürs Option-Mapping nutzt. `readonly`.

## Typ & Vererbung
- Namespace: `FfOctoApi\Service`
- `readonly class PropertyService`

## Konstruktor / DI
`OctoLoggerInterface $logger`, `EntityRepository $propertyGroupRepository`, `EntityRepository $propertyGroupOptionRepository`.

## Methoden
### `createPropertyGroup(apiProduct, ?context): array`
Baut Group (`getPropertyGroup`) + Options (`getPropertyGroupOptions`), löscht nicht mehr vorhandene Optionen der Group, upsert Group inkl. `options`. Gibt die Group zurück.

### `private getPropertyGroupOptions(apiProduct, propertyGroupId, context): array`
Pro API-Option: deterministische `getPropertyGroupOptionId(apiProduct['id'], option['id'])`; matcht aber zuerst eine bestehende Option per `groupId`+`name` (nutzt deren ID). Name = `title`/`internalName`, Position fortlaufend.

### `private getPropertyGroup(apiProduct, context): array`
Sucht bestehende Group per `name`; sonst deterministische `getPropertyGroupId(apiProduct['id'])`. Setzt `filterable=false`, `visibleOnProductDetailPage=true`.

### `getPropertyGroupId(apiProductId): ?string` (public)
`Uuid::fromStringToHex("{apiProductId}-property-group")`.

### `getPropertyGroupOptionId(apiProductId, apiProductOptionId): ?string` (public)
`Uuid::fromStringToHex("{apiProductId}-{apiProductOptionId}-property-group-option")`.

## Besonderheiten / Fallstricke
- **Deterministische IDs** sind der Schlüssel fürs Preis-Mapping (`PriceService::getApiProductOptions`) und müssen mit dem AppServer konsistent sein.
- `apiProduct['id']` ist hier die deterministische Produkt-ID (`{octoId}-{reference}-{identifier}`), nicht die rohe OCTO-UUID — auf korrekten Aufruf achten.
- Option-Matching per Name kann bei umbenannten Optionen zu „neuen" Optionen führen.

## Bezüge
`Controller/PropertyController.php`, `Service/PriceService.php`, `Controller/VariantController.php`, `Command/PropertyGroupCleanupCommand.php`.
