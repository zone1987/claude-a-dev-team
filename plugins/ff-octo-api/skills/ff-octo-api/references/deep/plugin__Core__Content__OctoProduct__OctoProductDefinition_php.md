# OctoProductDefinition (`src/Core/Content/OctoProduct/OctoProductDefinition.php`)

## Zweck
DAL-Entity-Definition der Tabelle `ff_octo_product`, die die OCTO-/Supplier-Produktdaten zu einem Shopware-Produkt speichert (API-Produkt-UUID, Supplier-Identifier, vollständige Produkt-JSON).

## Typ & Vererbung
- Namespace: `FfOctoApi\Core\Content\OctoProduct`
- `class OctoProductDefinition extends EntityDefinition`
- Registriert in `definitions.xml` (Tag `shopware.entity.definition`).

## Konstanten
| Konstante | Wert | Bedeutung |
|-----------|------|-----------|
| `ENTITY_NAME` | `ff_octo_product` | Tabellen-/Entity-Name. |

## Methoden
- `getEntityName(): string` → `ff_octo_product`.
- `getCollectionClass(): string` → `OctoProductCollection`.
- `getEntityClass(): string` → `OctoProductEntity`.
- `since(): ?string` → `6.0.0.0`.
- `getDefaults(): array` → `['product' => []]`.
- `defineFields(): FieldCollection`:
  - `id` (IdField, ApiAware + PrimaryKey + Required)
  - `uuid` (StringField, ApiAware + Required) — API-Produkt-UUID.
  - `identifier` (StringField, ApiAware + Required) — Supplier (`goldentours`, `gocity`, `rheinkurier`, `demo`).
  - `product` (JsonField, ApiAware) — vollständige API-Produktdaten (options/units/content …).

## Besonderheiten
- `product`-JSON ist der Vertrag mit dem AppServer (`AdminApiClient` schreibt diese Struktur für RheinKurier).
- Index auf `identifier` via Migration `Migration1768988700`.

## Bezüge
`OctoProductEntity`, `OctoProductCollection`, `Extension/Content/Product/ProductExtension.php`, `Migration/*`, `../database-entities.md`, `../appserver-integration.md`.
