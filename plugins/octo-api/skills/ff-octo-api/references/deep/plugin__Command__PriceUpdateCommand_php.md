# PriceUpdateCommand (`src/Command/PriceUpdateCommand.php`)

## Zweck
Konsolen-Command `ff:price:update`, der die Preise **aller** OCTO-Produkte (Parent-Produkte mit `ffOctoProduct`-Extension) in der Datenbank neu berechnet/aktualisiert. Manuelles Pendant zum geplanten `OctoApiPriceUpdaterTask` (alle 3h).

## Typ & Vererbung
- Namespace: `FfOctoApi\Command`
- `class PriceUpdateCommand extends Symfony\Component\Console\Command\Command`
- Attribut: `#[AsCommand(name: 'ff:price:update', description: 'Updates the price of all products in the database.')]`
- Hinweis: PHPDoc nennt fälschlich `UpdateCustomFieldsCommand` / `FfLondonBase\Command` (Copy-Paste-Reste).

## Konstruktor / DI
| Parameter | Typ | Zweck |
|-----------|-----|-------|
| `$productRepository` | `EntityRepository` | Lädt Produkte (DAL). |
| `$priceService` | `PriceService` | Führt die eigentliche Preisberechnung aus. |
| `$logger` | `OctoLoggerInterface` | Fehler-Logging (Channel `octo`). |

## Methoden
### `private getProducts(): ProductCollection|EntityCollection`
- Baut `Criteria` mit `addAssociation('ffOctoProduct')` und Filter `EqualsFilter('parentId', null)` (nur Parent-Produkte).
- Sucht mit `Context::createDefaultContext()`, filtert das Ergebnis zusätzlich auf `hasExtension('ffOctoProduct')`.
- **Rückgabe:** Collection der OCTO-Parent-Produkte.

### `protected execute(InputInterface $input, OutputInterface $output): int`
- Erzeugt `SymfonyStyle`, lädt Produkte, zählt Varianten via `array_sum(map(getChildCount))`.
- Gibt Info aus, startet `ProgressBar`.
- Schleife über alle Produkte: holt `ffOctoProduct`-Extension (`OctoProductEntity`), ruft
  `priceService->updatePrices($product->getId(), $octoProduct->getIdentifier(), $octoProduct->getProduct())`, advanced die ProgressBar.
- **Rückgabe:** `Command::SUCCESS` bei Erfolg; bei `Exception` wird geloggt und `Command::FAILURE` zurückgegeben.
- **Seiteneffekte:** schreibt Preise in die DB (über `PriceService`), Konsolen-Output, Logging.
- **Fallstrick:** Im `catch` wird `$progressBar->advance()` statt `finish()` aufgerufen; ein Fehler bei einem Produkt bricht die gesamte Schleife ab (kein per-Produkt-Resume).

## Bezüge
`PriceService`, `OctoProductEntity`, `OctoLoggerInterface`, `Service/ScheduledTask/OctoApiPriceUpdaterHandler.php`, `commands.xml`.
