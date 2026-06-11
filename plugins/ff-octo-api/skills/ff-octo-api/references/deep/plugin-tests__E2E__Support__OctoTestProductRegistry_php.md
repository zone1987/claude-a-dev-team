# OctoTestProductRegistry (`tests/E2E/Support/OctoTestProductRegistry.php`)

## Zweck
Registry der E2E-Test-Produkte je Provider (URLs/Identifier aus Env). Liefert Test-Produkt-Einträge und überspringt Tests, wenn die nötigen Env-Variablen fehlen.

## Typ
- `final class OctoTestProductRegistry`.
- Konstanten: `PROVIDER_GOLDENTOURS/GOCITY/RHEINKURIER`, `ENV_KEYS`.
- Methoden: `entriesFor(provider)`, `urlsFor(provider)`, `allOnlineProviders()`, `allProviders()`, `skipIfMissing(envName, test)`.

## Besonderheiten
- Steuert, gegen welche realen Produkte die E2E-Tests laufen; `skipIfMissing` verhindert Fehlschläge bei fehlender Konfiguration (kein verdecktes Skippen von Preis-Checks).

## Bezüge
`ProviderDataProvider.php`, `E2E/Storefront/**`.
