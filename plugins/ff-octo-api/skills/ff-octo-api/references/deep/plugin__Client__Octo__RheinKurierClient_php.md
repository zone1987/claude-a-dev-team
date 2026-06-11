# RheinKurierClient (`src/Client/Octo/RheinKurierClient.php`)

## Zweck
OCTO-Client für den Supplier **RheinKurier** — der einzige **OFFLINE**-Client. Macht zur Laufzeit **keine** OCTO-API-Calls; die Produktdaten werden extern über den ResubmissionAppServer in die `ff_octo_product`-Entity geschrieben (siehe `../appserver-integration.md`). Dient nur als Träger der Konstanten und des Offline-Flags.

## Typ & Vererbung
- Namespace: `FfOctoApi\Client\Octo`
- `class RheinKurierClient extends CachedOctoApiClient`
- Registriert in `clients.xml` mit Tag `octo.api.client`.

## Konstanten
| Konstante | Sichtbarkeit | Wert | Bedeutung |
|-----------|--------------|------|-----------|
| `IDENTIFIER` | public string | `rheinkurier` | Supplier-Identifier (Filter `ff_octo_product.identifier`). |
| `OFFLINE` | public bool | `true` | **Zentral:** markiert den Client als offline → `isOffline()` liefert true; alle API-Pfade müssen das behandeln. |
| `COLOR` | public string | `#6699CC` | Anzeigefarbe. |

Hat **keine** Base-URL-/API-Key-Konstanten (kein API-Zugriff nötig).

## Methoden
Keine eigenen. `isOffline()` (geerbt) wertet die `OFFLINE`-Konstante aus.

## Besonderheiten / Fallstricke
- **Offline-Konzept:** In `AbstractOctoApiClient::request()`, `AvailbilityController`, `CartController`, `BookingService`, `CheckoutService`, `OrderSubscriber`, `OctoApiWarmCacheHandler`, `OctoApiPriceUpdaterHandler` muss `isOffline()` geprüft werden (kein Call → leeres Ergebnis bzw. Preis aus `pricingFrom`).
- **Datenquelle:** Produkte/Varianten kommen aus dem ResubmissionAppServer (`AdminApiClient`, hardcodiert `identifier='rheinkurier'`, `reference='GTP2'`), nicht aus manueller Pflege.
- **Preis-Fallback:** Offline-Produkte liefern keine top-level `id`/`reference` → `PriceService` nutzt Flach-Sammeln + Lowest-Price (verhindert 0,00-€-Bug).

## Bezüge
`CachedOctoApiClient`, `../appserver-integration.md`, `PriceService`, `../supplier-comparison.md`.
