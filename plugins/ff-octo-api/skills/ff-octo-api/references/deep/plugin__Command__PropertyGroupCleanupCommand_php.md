# PropertyGroupCleanupCommand (`src/Command/PropertyGroupCleanupCommand.php`)

## Zweck
Console-Command zum Aufräumen verwaister Eigenschaftsgruppen (Property Groups). Löscht alle Gruppen, die entweder keine Optionen besitzen oder deren Optionen keinem Produkt (über `productConfiguratorSettings`) zugeordnet sind. Reines Entwickler-/Wartungswerkzeug.

## Typ & Vererbung
- Namespace: `FfOctoApi\Command`
- `class PropertyGroupCleanupCommand extends Symfony\Component\Console\Command\Command`
- Attribut `#[AsCommand(name: 'ff:property-group:cleanup', description: 'Deletes all property groups that are empty or to which no option is assigned to a product.')]`
- Hinweis: Der PHPDoc-Klassenkopf nennt fälschlich `UpdateCustomFieldsCommand` / Package `FfLondonBase\Command` (veralteter Copy-Paste-Block, nicht maßgeblich).

## Konstruktor / DI
| Abhängigkeit | Typ | Wofür |
|---|---|---|
| `$propertyGroupRepository` | `EntityRepository` (readonly, promoted) | DAL-Repository der Entität `property_group`; Suche und Löschung. |

Ruft `parent::__construct()`.

## Konstanten/Properties
Keine eigenen Konstanten oder Properties (außer DI-Property). Verwendet `Command::SUCCESS` / `Command::FAILURE`.

## Methoden
- `private getPropertyGroups(): EntityCollection|PropertyGroupCollection`
  Lädt alle Property Groups mit Association `options` und verschachtelt `options.productConfiguratorSettings`. Nutzt `Context::createDefaultContext()`. DB-Lesezugriff. Wird in `execute()` zweimal aufgerufen (kein Caching).
- `private isDdevProject(): bool`
  Liest Env `IS_DDEV_PROJECT` (Default `'false'`) und prüft auf `'true'`. Schutzschranke.
- `private isDevEnv(): bool`
  Liest Env `APP_ENV` (Default `'prod'`) und prüft auf `'dev'`. Schutzschranke.
- `protected execute(InputInterface $input, OutputInterface $output): int`
  Hauptablauf:
  1. Wirft `Exception`, wenn nicht DDEV bzw. nicht `dev`-Env.
  2. `$emptyPropertyGroups`: Gruppen mit `options->count() === 0`.
  3. `$unassignedPropertyGroups`: Gruppen, bei denen keine Option ein `productConfiguratorSettings` mit `count() > 0` hat.
  4. Merge beider ID-Listen (`[['id' => ...]]`), bei nicht-leer `delete(...)` über das Repo (DB-Schreibzugriff), sonst Info-Meldung.
  Rückgabe `Command::SUCCESS`; bei gefangener `Exception` Fehlermeldung via `SymfonyStyle` und `Command::FAILURE`.

## Besonderheiten / Fallstricke
- **DDEV- und dev-Env-gebunden:** Läuft nur, wenn `IS_DDEV_PROJECT === 'true'` UND `APP_ENV === 'dev'`. In Produktion/CI sofortiger Abbruch.
- **Destruktive Operation:** Löscht Property Groups dauerhaft via DAL `delete()` — keine Soft-Delete, keine Bestätigungsabfrage, keine `--dry-run`-Option.
- **Doppelte Abfrage:** `getPropertyGroups()` wird zweimal ausgeführt; Merge kann theoretisch IDs doppelt enthalten (leere Gruppe ist immer auch „unassigned"), DAL-`delete` toleriert dies aber.
- Alle Aufrufe nutzen `Context::createDefaultContext()` (kein Sales-Channel-/User-Kontext).

## Bezüge
- Registrierung als Console-Command vermutlich in `Resources/config/services.xml` / `commands.xml`.
- Import `FfLondonBase\Service\CustomFieldServiceRegistry` ist ungenutzt (Altlast).
- DAL-Entitäten: `PropertyGroupEntity`, `PropertyGroupOptionEntity`, `PropertyGroupCollection` (Shopware Core).
