# Shopware Migration Assistant — Developer reference

GitHub: https://github.com/shopware/SwagMigrationAssistant

## Contents

- [Architecture overview](#architecture-overview)
- [Migration process (states)](#migration-process-states)
- [Profile](#profile)
- [Connection](#connection)
- [Gateway](#gateway)
- [Reader](#reader)
- [DataSelection and DataSet](#dataselection-and-dataset)
- [Converter](#converter)
- [MappingService](#mappingservice)
- [Deltas (incremental migration)](#deltas-incremental-migration)
- [Writer](#writer)
- [Premapping](#premapping)
- [Media Processing](#media-processing)

## Architecture overview

```
Profile
  └─ Gateway (local | api)
       └─ Reader (reads source data, paginated)
Converter (transforms into SW6 structure)
  └─ MappingService (old_id → new_uuid, checksum)
DataSelection
  └─ DataSet (one class per entity)
Writer (writes into the SW6 DAL)
MediaFileProcessor (HTTP download | local copy)
PremappingReader (UI for manual assignments)
```

## Migration process (states)

```
Fetching → ErrorResolution → Writing → MediaProcessing → Cleanup → Indexing → WaitingForApprove → Finished
```

Every step runs asynchronously via the message queue (`MigrationProcessMessage`).

### Fetching

Per `DataSet` in the selected `DataSelections`:
1. Reader reads the source data (paginated via `offset` + `limit`)
2. Converter transforms the data and stores it in `swag_migration_data`
3. MappingService stores `(old_id → new_uuid, checksum)` in `swag_migration_mapping`

### ErrorResolution

The user sees validation errors (from `MigrationEntityValidationService`) and can store
corrections in `swag_migration_fix`.

### Writing

Writer writes the converted data from `swag_migration_data` into Shopware 6 via the DAL.

### MediaProcessing

The processor reads the queue from `swag_migration_media_file` (flag `written=true`) and
downloads/copies the files into the Shopware media storage.

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

**DIC registration:**
```php
$services->set(OwnProfile::class)->tag('shopware.migration.profile');
```

## Connection

Entity `swag_migration_connection`: connects profile, gateway, credentials and premapping.
All mappings are stored per connection — this enables multiple migrations without data loss.

## Gateway

Communication layer to the source system:

| Gateway | Description                                  |
|---------|----------------------------------------------|
| `local` | Direct DB access (both systems on the same server) |
| `api`   | HTTP communication via SwagMigrationConnector |

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

**DIC tag:** `shopware.migration.gateway`

## Reader

Reads source data page by page and counts the total amount:

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

**DIC registration:**
```php
$services->set(ProductReader::class)
    ->parent(AbstractReader::class)
    ->tag('shopware.migration.reader');
```

## DataSelection and DataSet

`DataSet` = one entity (corresponds to one table).
`DataSelection` = an ordered group of DataSets.

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
            100,       // Position (lower = starts earlier)
            true,      // processMediaFiles
            DataSelectionStruct::BASIC_DATA_TYPE,
            false      // required (mandatory selection)
        );
    }

    public function getDataSets(): array
    {
        // ORDER MATTERS — mind the dependencies
        return [new MediaFolderDataSet(), new ProductDataSet()];
    }
}
```

**DIC tags:**
```php
$services->set(ProductDataSelection::class)->tag('shopware.migration.data_selection');
$services->set(ProductDataSet::class)->tag('shopware.migration.data_set');
```

## Converter

Transforms source data into the Shopware 6 format:

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
        return $data['id']; // Unique key in the source system (for delta detection)
    }

    public function convert(array $data, Context $context, MigrationContextInterface $migrationContext): ConvertStruct
    {
        // 1. Checksum for delta detection
        $this->generateChecksum($data);

        // 2. Get or create mapping (old_id → new_uuid)
        $this->mainMapping = $this->mappingService->getOrCreateMapping(
            $migrationContext->getConnection()->getId(),
            ProductDataSet::getEntity(),
            $data['id'],
            $context,
            $this->checksum  // Checksum to store
        );

        // 3. Convert the data
        $converted = ['id' => $this->mainMapping['entityUuid']];
        $this->convertValue($converted, 'productNumber', $data, 'product_number');
        $this->convertValue($converted, 'name', $data, 'product_name');
        $this->convertValue($converted, 'stock', $data, 'stock', self::TYPE_INTEGER);

        // 4. Remove unmapped data (unprocessed fields) for debugging
        unset($data['id'], $data['product_number'], $data['product_name'], $data['stock']);
        if (empty($data)) {
            $data = null;
        }

        // 5. Store the mapping and return the ConvertStruct
        $this->updateMainMapping($migrationContext, $context);
        return new ConvertStruct($converted, $data, $this->mainMapping['id']);
    }

    public function writeMapping(Context $context): void
    {
        $this->mappingService->writeMapping($context);
    }
}
```

**DIC tag:** `shopware.migration.converter`

## MappingService

Core service for ID mapping between source and target system.

```php
// Get or newly create a mapping (with checksum)
$mapping = $this->mappingService->getOrCreateMapping(
    $connectionId,
    DefaultEntities::PRODUCT,
    $oldProductId,
    $context,
    $this->checksum
);
$newUuid = $mapping['entityUuid'];

// Only fetch an existing mapping (no creation)
$mapping = $this->mappingService->getMapping(
    $connectionId,
    SalutationReader::getMappingName(),
    $salutation,
    $context
);
if ($mapping === null) {
    // Logging: no mapping found
    return null;
}

// Currency and tax helper methods
$currencyUuid = $this->mappingService->getCurrencyUuid($connectionId, 'EUR', $context);
$taxUuid = $this->mappingService->getTaxUuid($connectionId, 19.0, $context);
```

**Important:** persist all collected `$this->mappingIds[]` at the end via `updateMainMapping()`,
so that the next migration loads all mapping IDs in one go (performance).

## Deltas (incremental migration)

The checksum is generated from the raw source data:
```php
$this->generateChecksum($data); // Internally: hash(serialize($data))
```

If the checksum is identical on the next migration run → skip the record.
Only changed records are migrated again.

## Writer

Writes converted data into the SW6 DAL:

```php
class ProductWriter extends AbstractWriter
{
    public function supports(): string { return DefaultEntities::PRODUCT; }
}
```

**DIC registration:**
```php
$services->set(ProductWriter::class)
    ->parent(AbstractWriter::class)
    ->args([
        service(EntityWriter::class),
        service(ProductDefinition::class),
    ])
    ->tag('shopware.migration.writer');
```

On a `WriteException` it tries to exclude the faulty entries and write the rest.
On other exceptions: individual processing to minimize data loss.

## Premapping

Enables manual assignment before the migration (e.g. salutations, payment methods):

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
        $mapping = $this->getMapping();         // Source data (selection options in the UI)
        $choices = $this->getChoices($context); // Target data (SW6 equivalents)
        $this->setPreselection($mapping);       // Automatic preselection
        return new PremappingStruct(self::getMappingName(), $mapping, $choices);
    }
}
```

**DIC tag:** `shopware.migration.pre_mapping_reader`

The premapping is used in the converter:
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

### Phase 1 — Converter queues media

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

| Processor                  | Gateway | Method                            |
|----------------------------|---------|-----------------------------------|
| `HttpMediaDownloadService` | api     | HTTP download via `HttpSimpleClient` |
| `LocalMediaProcessor`      | local   | File system copy                  |

Status flags in `swag_migration_media_file`:
- `written` — entity write completed
- `processed` — media import succeeded
- `process_failure` — import failed
