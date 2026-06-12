# PluginLoggerTrait (`src/Core/Framework/Config/PluginLoggerTrait.php`)

## Zweck
Trait für die Plugin-Hauptklasse, das beim Container-Build die plugin-eigene Logger-/Monolog-Konfiguration aus `Resources/config/packages/*.yaml` lädt (eigener Log-Channel `octo`).

## Typ
- Namespace: `FfOctoApi\Core\Framework\Config`
- `trait PluginLoggerTrait`

## Methoden
### `protected registerPluginLogger(ContainerBuilder $container, string $path): void`
Baut einen `DelegatingLoader` (Yaml/Glob/Directory), lädt `{path}/Resources/config/{packages}/*.yaml` als Glob. Wirft `Exception` bei Ladefehlern.

## Besonderheiten
- Wird in `FfOctoApi::build()` genutzt, damit die Monolog-Channel-Config (Datei `var/log/octo-{env}.log`) registriert wird.

## Bezüge
`FfOctoApi.php`, `Service/LoggerService.php`, `Resources/config/packages/*.yaml`.
