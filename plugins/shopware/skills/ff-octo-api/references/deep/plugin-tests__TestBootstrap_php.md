# TestBootstrap.php (`tests/TestBootstrap.php`)

## Zweck
Bootstrap für die PHPUnit-Tests (Unit/Integration). Nutzt Shopware `TestBootstrapper`, aktiviert das Plugin `FfOctoApi` (Force-Install) und registriert den Test-PSR-4-Namespace `FfOctoApi\Tests\`.

## Inhalt
- `TestBootstrapper()->addCallingPlugin()->addActivePlugins('FfOctoApi')->setForceInstallPlugins(true)->bootstrap()`.
- `$loader->addPsr4('FfOctoApi\\Tests\\', __DIR__)`.

## Bezüge
`phpunit.xml`, alle Unit/Integration-Tests.
