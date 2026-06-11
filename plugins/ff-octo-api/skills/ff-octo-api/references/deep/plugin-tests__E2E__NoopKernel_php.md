# NoopKernel (`tests/E2E/NoopKernel.php`)

## Zweck
Minimaler Symfony-Kernel für die Panther-Tests (Panther erwartet einen Kernel, die E2E-Tests laufen aber gegen die echte, separat laufende Storefront). Registriert keine Bundles, leere Container-Config, eigene Cache-/Log-Dirs.

## Typ
- `final class NoopKernel extends Kernel`.
- Methoden: `registerBundles()` (leer), `registerContainerConfiguration()` (leer), `getCacheDir()`, `getLogDir()`.

## Bezüge
`Support/PantherTestCase.php`, `bootstrap.php`.
