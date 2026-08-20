# Migration Assistant — Custom Profile & Extensions

## Contents

- [Scenario selection](#scenario-selection)
- [A) Extend an existing Shopware profile (BundleExample)](#a-extend-an-existing-shopware-profile-bundleexample)
- [B) Decorate a converter + premapping reader (converter extension)](#b-decorate-a-converter--premapping-reader-converter-extension)
- [C) A new profile from scratch (third-party system)](#c-a-new-profile-from-scratch-third-party-system)
- [D) Extend the Migration Connector (SW5 API)](#d-extend-the-migration-connector-sw5-api)

## Scenario selection

| Goal                                                  | Guide                              |
|-------------------------------------------------------|------------------------------------|
| Migrate plugin data from SW5 (local gateway)          | Extend the Shopware profile        |
| Migrate plugin data from SW5 via API                  | Extend the Migration Connector     |
| Adjust the converter of an existing profile           | Decorate converter + premapping    |
| Migrate a third-party system (not Shopware)           | New profile from scratch           |

## A) Extend an existing Shopware profile (BundleExample)

### 1. Create the DataSet

```php
class BundleDataSet extends DataSet
{
    public static function getEntity(): string
    {
        return 'swag_bundle'; // Entity identifier (must match the writer's supports())
    }

    public function supports(MigrationContextInterface $migrationContext): bool
    {
        // Support all Shopware profile versions
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface;
    }

    public function getSnippet(): string
    {
        return 'swag-migration.index.selectDataCard.entities.' . static::getEntity();
    }
}
```

**DIC tag:** `shopware.migration.data_set`

### 2. Decorate the DataSelection (add an entity to an existing selection)

```php
class ProductDataSelection implements DataSelectionInterface
{
    public function __construct(private readonly DataSelectionInterface $originalDataSelection) {}

    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $this->originalDataSelection->supports($migrationContext);
    }

    public function getData(): DataSelectionStruct
    {
        $dataSelection = $this->originalDataSelection->getData();
        return new DataSelectionStruct(
            $dataSelection->getId(),
            $this->getDataSets(),
            $this->getDataSetsRequiredForCount(),
            $dataSelection->getSnippet(),
            $dataSelection->getPosition(),
            $dataSelection->getProcessMediaFiles(),
            DataSelectionStruct::PLUGIN_DATA_TYPE  // Type: PLUGIN_DATA_TYPE instead of BASIC_DATA_TYPE
        );
    }

    public function getDataSets(): array
    {
        $entities = $this->originalDataSelection->getDataSets();
        $entities[] = new BundleDataSet(); // Insert the new entity AFTER its dependencies
        return $entities;
    }

    public function getDataSetsRequiredForCount(): array
    {
        return $this->originalDataSelection->getDataSetsRequiredForCount();
    }
}
```

**DIC registration (decorate):**
```php
$services->set(ProductDataSelection::class)
    ->decorate(OriginalProductDataSelection::class)
    ->args([service('.inner')]);

$services->set(BundleDataSet::class)->tag('shopware.migration.data_set');
```

### 3. Administration snippet for the entity counter

```json
{
    "swag-migration": {
        "index": {
            "selectDataCard": {
                "entities": {
                    "swag_bundle": "Bundles:"
                }
            }
        }
    }
}
```

### 4. Create the local reader

```php
class LocalBundleReader extends AbstractReader
{
    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface
            && $migrationContext->getGateway()->getName() === ShopwareLocalGateway::GATEWAY_NAME
            && $migrationContext->getDataSet()::getEntity() === BundleDataSet::getEntity();
    }

    public function supportsTotal(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface
            && $migrationContext->getGateway()->getName() === ShopwareLocalGateway::GATEWAY_NAME;
    }

    public function readTotal(MigrationContextInterface $migrationContext): ?TotalStruct
    {
        $this->setConnection($migrationContext);
        $total = (int) $this->connection->createQueryBuilder()->select('COUNT(*)')->from('s_bundles')->execute()->fetchColumn();
        return new TotalStruct(BundleDataSet::getEntity(), $total);
    }

    public function read(MigrationContextInterface $migrationContext, array $params = []): array
    {
        $this->setConnection($migrationContext);

        // Fetch IDs page by page
        $ids = $this->fetchIdentifiers('s_bundles', $migrationContext->getOffset(), $migrationContext->getLimit());

        // Main data with table prefix
        $bundles = $this->mapData($this->fetchBundles($ids), [], ['bundles']);

        // Load associated data afterwards and embed it
        $bundleProducts = $this->fetchBundleProducts($ids);
        foreach ($bundles as &$bundle) {
            if (isset($bundleProducts[$bundle['id']])) {
                $bundle['products'] = $bundleProducts[$bundle['id']];
            }
        }
        return $bundles;
    }

    private function fetchBundles(array $ids): array
    {
        $query = $this->connection->createQueryBuilder();
        $query->from('s_bundles', 'bundles');
        $this->addTableSelection($query, 's_bundles', 'bundles'); // Adds the prefixed aliases
        $query->where('bundles.id IN (:ids)');
        $query->setParameter('ids', $ids, Connection::PARAM_STR_ARRAY);
        $query->addOrderBy('bundles.id');
        return $query->execute()->fetchAll();
    }
}
```

**DIC registration:**
```php
$services->set(LocalBundleReader::class)
    ->parent(AbstractReader::class)
    ->tag('shopware.migration.reader');
```

### 5. Create the converter

```php
class BundleConverter extends ShopwareConverter
{
    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface
            && $migrationContext->getDataSet()::getEntity() === BundleDataSet::getEntity();
    }

    public function getSourceIdentifier(array $data): string { return $data['id']; }

    public function convert(array $data, Context $context, MigrationContextInterface $migrationContext): ConvertStruct
    {
        $this->generateChecksum($data);

        $this->mainMapping = $this->mappingService->getOrCreateMapping(
            $migrationContext->getConnection()->getId(),
            BundleDataSet::getEntity(),
            $data['id'],
            $context,
            $this->checksum
        );
        $converted = ['id' => $this->mainMapping['entityUuid']];
        $this->convertValue($converted, 'name', $data, 'name');
        $converted['discountType'] = 'absolute';
        $converted['discount'] = 0;

        // Resolve relations (mapping of already migrated entities)
        if (isset($data['products'])) {
            $products = [];
            foreach ($data['products'] as $productId) {
                $mapping = $this->mappingService->getMapping(
                    $migrationContext->getConnection()->getId(),
                    DefaultEntities::PRODUCT . '_mainProduct',
                    $productId,
                    $context
                );
                if ($mapping !== null) {
                    $this->mappingIds[] = $mapping['id']; // Performance
                    $products[] = ['id' => $mapping['entityUuid']];
                }
            }
            if (!empty($products)) {
                $converted['products'] = $products;
            }
        }

        unset($data['id'], $data['name'], $data['products']);
        $this->updateMainMapping($migrationContext, $context);
        return new ConvertStruct($converted, empty($data) ? null : $data, $this->mainMapping['id']);
    }

    public function writeMapping(Context $context): void
    {
        $this->mappingService->writeMapping($context);
    }
}
```

**DIC tag:** `shopware.migration.converter`

### 6. Create the writer

```php
class BundleWriter extends AbstractWriter
{
    public function supports(): string { return BundleDataSet::getEntity(); }
}
```

**DIC registration:**
```php
$services->set(BundleWriter::class)
    ->parent(AbstractWriter::class)
    ->args([
        service(EntityWriter::class),
        service(BundleDefinition::class), // EntityDefinition of the target entity
    ])
    ->tag('shopware.migration.writer');
```

## B) Decorate a converter + premapping reader (converter extension)

### Create the premapping reader

Lets users manually assign SW5 manufacturers to SW6 manufacturers:

```php
class ManufacturerReader extends AbstractPremappingReader
{
    private const MAPPING_NAME = 'swag_manufacturer';

    public static function getMappingName(): string { return self::MAPPING_NAME; }

    public function supports(MigrationContextInterface $migrationContext, array $entityGroupNames): bool
    {
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface
            && in_array(ProductDataSelection::IDENTIFIER, $entityGroupNames, true);
    }

    public function getPremapping(Context $context, MigrationContextInterface $migrationContext): PremappingStruct
    {
        $this->fillConnectionPremappingDictionary($migrationContext); // Load existing assignments
        $mapping = $this->getMapping($migrationContext); // Read source data
        $choices = $this->getChoices($context);          // Read target options
        $this->setPreselection($mapping);                // Prefill automatically

        return new PremappingStruct(self::getMappingName(), $mapping, $choices);
    }

    private function getMapping(MigrationContextInterface $migrationContext): array
    {
        $gateway = $this->gatewayRegistry->getGateway($migrationContext);
        $preMappingData = $gateway->readTable($migrationContext, 's_articles_supplier');

        $entityData = [];
        foreach ($preMappingData as $data) {
            $uuid = $this->connectionPremappingDictionary[$data['id']]['destinationUuid'] ?? '';
            $entityData[] = new PremappingEntityStruct($data['id'], $data['name'], $uuid);
        }
        return $entityData;
    }
}
```

**DIC tag:** `shopware.migration.pre_mapping_reader`

Administration snippet for the premapping card title:
```json
{
    "swag-migration": {
        "index": {
            "premappingCard": {
                "group": {
                    "swag_manufacturer": "Manufacturer"
                }
            }
        }
    }
}
```

### Decorate the converter

```php
class Shopware55DecoratedProductConverter extends ProductConverter
{
    public function __construct(
        private readonly ConverterInterface $originalProductConverter,
        MappingServiceInterface $mappingService,
        LoggingServiceInterface $loggingService,
        MediaFileServiceInterface $mediaFileService
    ) {
        parent::__construct($mappingService, $loggingService, $mediaFileService);
    }

    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $this->originalProductConverter->supports($migrationContext);
    }

    public function convert(array $data, Context $context, MigrationContextInterface $migrationContext): ConvertStruct
    {
        if (!isset($data['manufacturer']['id'])) {
            return $this->originalProductConverter->convert($data, $context, $migrationContext);
        }

        $manufacturerId = $data['manufacturer']['id'];
        unset($data['manufacturer']);

        // Read the premapping assignment
        $mapping = $this->mappingService->getMapping(
            $migrationContext->getConnection()->getId(),
            ManufacturerReader::getMappingName(),
            $manufacturerId,
            $context
        );

        // Run the original converter
        $convertedStruct = $this->originalProductConverter->convert($data, $context, $migrationContext);

        if ($mapping === null) {
            return $convertedStruct;
        }

        // Merge the premapping result into the converted data
        $converted = $convertedStruct->getConverted();
        $converted['manufacturerId'] = $mapping['entityUuid'];
        return new ConvertStruct($converted, $convertedStruct->getUnmapped(), $convertedStruct->getMappingUuid());
    }
}
```

**DIC registration:**
```php
$services->set(Shopware55DecoratedProductConverter::class)
    ->decorate(Shopware55ProductConverter::class)  // Original converter to be decorated
    ->args([
        service('.inner'),
        service(MappingService::class),
        service(LoggingService::class),
        service(MediaFileService::class),
    ]);
```

## C) A new profile from scratch (third-party system)

### Minimum implementation

1. **Profile** implements `ProfileInterface` — `getName()`, `getSourceSystemName()`, `getVersion()`
2. **Gateway** implements `GatewayInterface` — `read()`, `readEnvironmentInformation()`, `readTotals()`
3. **Credentials page** in the Administration: Vue component `swag-migration-profile-{profileName}-{gatewayName}-credential-form`
4. **DataSet + DataSelection** for every entity to be migrated
5. **Reader** reads the source data page by page
6. **Converter** transforms it into the SW6 structure
7. **Writer** (often `AbstractWriter` with the correct `EntityDefinition` is enough)

### Component naming convention for the Administration

```
swag-migration-profile-{profileName}-{gatewayName}-credential-form
```

Example: `swag-migration-profile-ownProfile-local-credential-form`

### Optional plugin conditionality (when the Migration Assistant is optional)

Load conditionally in the plugin base class:
```php
if (class_exists(MigrationAssistantPluginClass::class)) {
    // Load the migration services
}
```

Separate DIC configuration file: `migration_assistant_extension.php`

## D) Extend the Migration Connector (SW5 API)

### Repository (SW5 side)

```php
class BundleRepository extends AbstractRepository
{
    public function fetch($offset = 0, $limit = 250): array
    {
        $ids = $this->fetchIdentifiers('s_bundles', $offset, $limit);
        // ... read data via Doctrine DBAL
    }
}
```

**DIC:** `->parent(AbstractRepository::class)`

### Service (SW5 side)

```php
class BundleService extends AbstractApiService
{
    public function getBundles($offset = 0, $limit = 250): array
    {
        $bundles = $this->bundleRepository->fetch($offset, $limit);
        return $this->cleanupResultSet($this->mapData($bundles, [], ['bundles']));
    }
}
```

### API controller (SW5 side, Shopware 5 MVC)

```php
class Shopware_Controllers_Api_SwagMigrationBundles extends Shopware_Controllers_Api_Rest
{
    public function indexAction(): void
    {
        $offset = (int) $this->Request()->getParam('offset', 0);
        $limit = (int) $this->Request()->getParam('limit', 250);
        $bundles = $this->container->get('bundle.service')->getBundles($offset, $limit);
        $response = new ControllerReturnStruct($bundles, empty($bundles));
        $this->view->assign($response->jsonSerialize());
    }
}
```

### API reader (SW6 side, inherits from ApiReader)

```php
class BundleReader extends ApiReader
{
    public function supports(MigrationContextInterface $migrationContext): bool
    {
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface
            && $migrationContext->getGateway()->getName() === ShopwareApiGateway::GATEWAY_NAME
            && $migrationContext->getDataSet()::getEntity() === BundleDataSet::getEntity();
    }

    protected function getApiRoute(): string
    {
        return 'SwagMigrationBundles'; // Matches the SW5 API controller name
    }
}
```

**DIC tag:** `shopware.migration.reader`
