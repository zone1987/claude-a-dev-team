# Shopware Migration Assistant — Entwickler-Referenz

GitHub: https://github.com/shopware/SwagMigrationAssistant

## Architektur-Ueberblick

```
Profile
  └─ Gateway (local | api)
       └─ Reader (liest Quelldaten, paginiert)
Converter (transformiert in SW6-Struktur)
  └─ MappingService (old_id → new_uuid, Checksum)
DataSelection
  └─ DataSet (je Entitaet eine Klasse)
Writer (schreibt in SW6-DAL)
MediaFileProcessor (HTTP-Download | Lokales Kopieren)
PremappingReader (UI fuer manuelle Zuordnungen)
```

## Migrationsprozess (States)

```
Fetching → ErrorResolution → Writing → MediaProcessing → Cleanup → Indexing → WaitingForApprove → Finished
```

Jeder Schritt laeuft asynchron via Message Queue (`MigrationProcessMessage`).

### Fetching

Pro `DataSet` in den ausgewaehlten `DataSelections`:
1. Reader liest Quelldaten (paginiert via `offset` + `limit`)
2. Converter wandelt Daten um und speichert in `swag_migration_data`
3. MappingService speichert `(old_id → new_uuid, checksum)` in `swag_migration_mapping`

### ErrorResolution

Benutzer sieht Validierungsfehler (aus `MigrationEntityValidationService`), kann Korrekturen
in `swag_migration_fix` speichern.

### Writing

Writer schreibt konvertierte Daten aus `swag_migration_data` via DAL in Shopware 6.

### MediaProcessing

Prozessor liest Queue aus `swag_migration_media_file` (flag `written=true`) und
laed/kopiert Dateien in Shopware-Medienspeicher.

## Profile

```php
class OwnProfile implements ProfileInterface
{
    final public const PROFILE_NAME = 'ownProfile';
    final public const SOURCE_SYSTEM_NAME = 'MySourceSystem';
    final public const SOURCE_SYSTEM_VERSION = '1.0';

    public function getName(): string { return self::PROFILE_NAME; }
    public function getSourceSystemName(): string { return self::SOURCE_SYSTEM_NAME; }
    public function getVersion(): string { return self::SOURCE_SYSTEM_VERSION; }
    public function getAuthorName(): string { return 'My Company'; }
    public function getIconPath(): string { return '/path/to/icon.svg'; }
}
```

**DIC-Registrierung:**
```php
$services->set(OwnProfile::class)->tag('shopware.migration.profile');
```

## Connection

Entity `swag_migration_connection`: Verbindet Profile, Gateway, Credentials und Premapping.
Pro Verbindung werden alle Mappings gespeichert — ermoeglicht mehrere Migrationen ohne Datenverlust.

## Gateway

Kommunikationsschicht zum Quellsystem:

| Gateway | Beschreibung                                 |
|---------|----------------------------------------------|
| `local` | Direkter DB-Zugriff (beide Systeme gleicher Server) |
| `api`   | HTTP-Kommunikation via SwagMigrationConnector |

```php
class OwnLocalGateway implements GatewayInterface
{
    public function getName(): string { return 'local'; }

    public function supports(ProfileInterface $profile): bool
    {
        return $profile instanceof OwnProfile;
    }

    public function read(MigrationContextInterface $migrationContext): array
    {
        $reader = $this->readerRegistry->getReader($migrationContext);
        return $reader->read($migrationContext);
    }
}
```

**DIC-Tag:** `shopware.migration.gateway`

## Reader

Liest paginiert Quelldaten und zaehlt Gesamtmenge:

```php
class ProductReader extends AbstractReader
{
    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof OwnProfile
            && $migrationContext->getDataSet()::getEntity() === 'product';
    }

    public function supportsTotal(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof OwnProfile
            && $migrationContext->getGateway()->getName() === ShopwareLocalGateway::GATEWAY_NAME;
    }

    public function readTotal(MigrationContextInterface $migrationContext): ?TotalStruct
    {
        $this->setConnection($migrationContext);
        $total = (int) $this->connection->createQueryBuilder()->select('COUNT(*)')->from('product')->execute()->fetchColumn();
        return new TotalStruct('product', $total);
    }

    public function read(MigrationContextInterface $migrationContext, array $params = []): array
    {
        $this->setConnection($migrationContext);
        return $this->connection->createQueryBuilder()
            ->from('product')->addSelect('*')
            ->setFirstResult($migrationContext->getOffset())
            ->setMaxResults($migrationContext->getLimit())
            ->execute()->fetchAll(\PDO::FETCH_ASSOC);
    }
}
```

**DIC-Registrierung:**
```php
$services->set(ProductReader::class)
    ->parent(AbstractReader::class)
    ->tag('shopware.migration.reader');
```

## DataSelection und DataSet

`DataSet` = eine Entitaet (entspricht einer Tabelle).
`DataSelection` = geordnete Gruppe von DataSets.

```php
class ProductDataSet extends DataSet
{
    public static function getEntity(): string { return DefaultEntities::PRODUCT; }

    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface;
    }
}

class ProductDataSelection implements DataSelectionInterface
{
    public const IDENTIFIER = 'products';

    public function getData(): DataSelectionStruct
    {
        return new DataSelectionStruct(
            self::IDENTIFIER,
            $this->getDataSets(),
            $this->getDataSetsRequiredForCount(),
            'swag-migration.index.selectDataCard.dataSelection.products',
            100,       // Position (kleiner = frueherer Start)
            true,      // processMediaFiles
            DataSelectionStruct::BASIC_DATA_TYPE,
            false      // required (Pflichtauswahl)
        );
    }

    public function getDataSets(): array
    {
        // REIHENFOLGE WICHTIG — Abhaengigkeiten beachten
        return [new MediaFolderDataSet(), new ProductDataSet()];
    }
}
```

**DIC-Tags:**
```php
$services->set(ProductDataSelection::class)->tag('shopware.migration.data_selection');
$services->set(ProductDataSet::class)->tag('shopware.migration.data_set');
```

## Converter

Transformiert Quelldaten in Shopware-6-Format:

```php
class ProductConverter extends ShopwareConverter
{
    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof OwnProfile
            && $migrationContext->getDataSet()::getEntity() === ProductDataSet::getEntity();
    }

    public function getSourceIdentifier(array $data): string
    {
        return $data['id']; // Eindeutiger Key im Quellsystem (fuer Delta-Erkennung)
    }

    public function convert(array $data, Context $context, MigrationContextInterface $migrationContext): ConvertStruct
    {
        // 1. Checksum fuer Delta-Erkennung
        $this->generateChecksum($data);

        // 2. Mapping holen oder erstellen (old_id → new_uuid)
        $this->mainMapping = $this->mappingService->getOrCreateMapping(
            $migrationContext->getConnection()->getId(),
            ProductDataSet::getEntity(),
            $data['id'],
            $context,
            $this->checksum  // Checksum zum Speichern
        );

        // 3. Daten konvertieren
        $converted = ['id' => $this->mainMapping['entityUuid']];
        $this->convertValue($converted, 'productNumber', $data, 'product_number');
        $this->convertValue($converted, 'name', $data, 'product_name');
        $this->convertValue($converted, 'stock', $data, 'stock', self::TYPE_INTEGER);

        // 4. Unmapped-Data (unbearbeitete Felder) fuer Debugging entfernen
        unset($data['id'], $data['product_number'], $data['product_name'], $data['stock']);
        if (empty($data)) {
            $data = null;
        }

        // 5. Mapping speichern und ConvertStruct zurueckgeben
        $this->updateMainMapping($migrationContext, $context);
        return new ConvertStruct($converted, $data, $this->mainMapping['id']);
    }

    public function writeMapping(Context $context): void
    {
        $this->mappingService->writeMapping($context);
    }
}
```

**DIC-Tag:** `shopware.migration.converter`

## MappingService

Kern-Service fuer ID-Mapping zwischen Quell- und Zielsystem.

```php
// Mapping holen oder neu anlegen (mit Checksum)
$mapping = $this->mappingService->getOrCreateMapping(
    $connectionId,
    DefaultEntities::PRODUCT,
    $oldProductId,
    $context,
    $this->checksum
);
$newUuid = $mapping['entityUuid'];

// Nur vorhandenes Mapping holen (kein Anlegen)
$mapping = $this->mappingService->getMapping(
    $connectionId,
    SalutationReader::getMappingName(),
    $salutation,
    $context
);
if ($mapping === null) {
    // Logging: kein Mapping gefunden
    return null;
}

// Waehrung und Steuer-Hilfsmethoden
$currencyUuid = $this->mappingService->getCurrencyUuid($connectionId, 'EUR', $context);
$taxUuid = $this->mappingService->getTaxUuid($connectionId, 19.0, $context);
```

**Wichtig:** Alle gesammelten `$this->mappingIds[]` am Ende per `updateMainMapping()` persistieren,
damit bei der naechsten Migration alle Mapping-IDs auf einmal geladen werden (Performance).

## Deltas (inkrementelle Migration)

Checksum wird aus rohen Quelldaten generiert:
```php
$this->generateChecksum($data); // Intern: hash(serialize($data))
```

Wenn beim naechsten Migrationslauf die Checksum gleich ist → Datensatz ueberspringen.
Nur geaenderte Datensaetze werden neu migriert.

## Writer

Schreibt konvertierte Daten in SW6-DAL:

```php
class ProductWriter extends AbstractWriter
{
    public function supports(): string { return DefaultEntities::PRODUCT; }
}
```

**DIC-Registrierung:**
```php
$services->set(ProductWriter::class)
    ->parent(AbstractWriter::class)
    ->args([
        service(EntityWriter::class),
        service(ProductDefinition::class),
    ])
    ->tag('shopware.migration.writer');
```

Bei `WriteException` wird versucht, fehlerhafte Eintraege auszuschliessen und Rest zu schreiben.
Bei anderen Exceptions: Einzelverarbeitung zum Minimieren von Datenverlust.

## Premapping

Ermoeglicht manuelle Zuordnung vor der Migration (z.B. Anreden, Zahlungsmethoden):

```php
class SalutationReader extends AbstractPremappingReader
{
    public static function getMappingName(): string { return 'salutation'; }

    public function supports(MigrationContextInterface $migrationContext, array $entityGroupNames): bool
    {
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface
            && in_array(BasicSettingsDataSelection::IDENTIFIER, $entityGroupNames, true);
    }

    public function getPremapping(Context $context, MigrationContextInterface $migrationContext): PremappingStruct
    {
        $this->fillConnectionPremappingDictionary($migrationContext);
        $mapping = $this->getMapping();         // Quelldaten (Auswahl-Optionen im UI)
        $choices = $this->getChoices($context); // Zieldaten (SW6-Aequivalente)
        $this->setPreselection($mapping);       // Automatische Vorauswahl
        return new PremappingStruct(self::getMappingName(), $mapping, $choices);
    }
}
```

**DIC-Tag:** `shopware.migration.pre_mapping_reader`

Im Converter wird Premapping verwendet:
```php
$mapping = $this->mappingService->getMapping(
    $this->connectionId,
    SalutationReader::getMappingName(),
    $salutation,
    $this->context
);
$salutationUuid = $mapping['entityId'] ?? null;
```

## Media Processing

### Phase 1 — Converter queued Media

```php
$this->mediaFileService->saveMediaFile([
    'runId'    => $migrationContext->getRunUuid(),
    'entity'   => MediaDataSet::getEntity(),
    'uri'      => $data['uri'] ?? $data['path'],
    'fileName' => $data['name'],
    'fileSize' => (int) $data['file_size'],
    'mediaId'  => $converted['id'],
]);
```

### Phase 2 — MediaFileProcessor

| Processor                  | Gateway | Verfahren                         |
|----------------------------|---------|-----------------------------------|
| `HttpMediaDownloadService` | api     | HTTP-Download via `HttpSimpleClient` |
| `LocalMediaProcessor`      | local   | Dateisystem-Kopie                 |

Status-Flags in `swag_migration_media_file`:
- `written` — Entity-Write abgeschlossen
- `processed` — Medien-Import erfolgreich
- `process_failure` — Import fehlgeschlagen
