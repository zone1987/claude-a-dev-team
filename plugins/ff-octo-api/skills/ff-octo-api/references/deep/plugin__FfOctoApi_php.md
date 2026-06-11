# FfOctoApi (`src/FfOctoApi.php`)

## Zweck
Plugin-Hauptklasse. Registriert beim Container-Build die Logger-Config und einen Pfad-Parameter; räumt beim Uninstall (ohne „keepUserData") die Entity-Tabelle und die Product-Inheritance auf.

## Typ & Vererbung
- Namespace: `FfOctoApi`
- `class FfOctoApi extends Shopware\Core\Framework\Plugin`
- Nutzt `DatabaseTrait`, `PluginLoggerTrait`.

## Konstanten
| Konstante | Wert | Bedeutung |
|-----------|------|-----------|
| `ENTITIES` | `[OctoProductDefinition::class => 'ff_octo_product']` | Beim Uninstall zu entfernende Tabellen. |

## Methoden
### `build(ContainerBuilder $container): void`
`parent::build`, dann `registerPluginLogger($container, getPath())` (lädt Monolog-Config), setzt Parameter `ff-octo-api.plugin-dir`.

### `uninstall(UninstallContext $uninstallContext): void`
Wenn `keepUserData()` → Abbruch (Daten bleiben). Sonst: `removeTables` für `ff_octo_product`, `removeTableInheritances('product', ['ffOctoProduct','ff_octo_product_id'])`.

## Besonderheiten / Fallstricke
- **Kein `getDepends()`** → keine erzwungene Lade-/Override-Reihenfolge gegenüber FfLondonBase/FfLondonTheme (Template-Override-Konflikte, siehe Frontend-Doku).
- Uninstall ist destruktiv (DROP TABLE) ohne keepUserData.

## Bezüge
`Core/Framework/Config/PluginLoggerTrait.php`, `Core/Framework/Migration/DatabaseTrait.php`, `Core/Content/OctoProduct/OctoProductDefinition.php`, `Extension/Content/Product/ProductExtension.php`.
