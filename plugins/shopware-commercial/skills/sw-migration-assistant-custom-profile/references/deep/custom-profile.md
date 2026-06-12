# Migration Assistant — Custom Profile & Extensions

## Szenario-Auswahl

| Ziel                                                  | Guide                              |
|-------------------------------------------------------|------------------------------------|
| Plugin-Daten aus SW5 migrieren (lokales Gateway)      | Shopware-Profil erweitern          |
| Plugin-Daten aus SW5 via API migrieren                | Migration Connector erweitern      |
| Konverter eines bestehenden Profils anpassen          | Converter dekorieren + Premapping  |
| Drittanbieter-System migrieren (nicht Shopware)       | Neues Profil von Grund auf         |

## A) Bestehendes Shopware-Profil erweitern (BundleExample)

### 1. DataSet anlegen

```php
class BundleDataSet extends DataSet
{
    public static function getEntity(): string
    {
        return 'swag_bundle'; // Entitaets-Bezeichner (muss mit Writer-supports() uebereinstimmen)
    }

    public function supports(MigrationContextInterface $migrationContext): bool
    {
        // Alle Shopware-Profile-Versionen unterstuetzen
        return $migrationContext->getProfile() instanceof ShopwareProfileInterface;
    }

    public function getSnippet(): string
    {
        return 'swag-migration.index.selectDataCard.entities.' . static::getEntity();
    }
}
```

**DIC-Tag:** `shopware.migration.data_set`

### 2. DataSelection dekorieren (Entitaet zu bestehender Auswahl hinzufuegen)

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
            DataSelectionStruct::PLUGIN_DATA_TYPE  // Typ: PLUGIN_DATA_TYPE statt BASIC_DATA_TYPE
        );
    }

    public function getDataSets(): array
    {
        $entities = $this->originalDataSelection->getDataSets();
        $entities[] = new BundleDataSet(); // Neue Entitaet NACH Abhaengigkeiten einfuegen
        return $entities;
    }

    public function getDataSetsRequiredForCount(): array
    {
        return $this->originalDataSelection->getDataSetsRequiredForCount();
    }
}
```

**DIC-Registrierung (dekorieren):**
```php
$services->set(ProductDataSelection::class)
    ->decorate(OriginalProductDataSelection::class)
    ->args([service('.inner')]);

$services->set(BundleDataSet::class)->tag('shopware.migration.data_set');
```

### 3. Administration-Snippet fuer Entitaetszaehler

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

### 4. Lokalen Reader erstellen

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

        // IDs paginiert holen
        $ids = $this->fetchIdentifiers('s_bundles', $migrationContext->getOffset(), $migrationContext->getLimit());

        // Hauptdaten mit Tabellen-Prefix
        $bundles = $this->mapData($this->fetchBundles($ids), [], ['bundles']);

        // Assoziierte Daten nachladen und einbetten
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
        $this->addTableSelection($query, 's_bundles', 'bundles'); // Fuegt Prefix-Aliase hinzu
        $query->where('bundles.id IN (:ids)');
        $query->setParameter('ids', $ids, Connection::PARAM_STR_ARRAY);
        $query->addOrderBy('bundles.id');
        return $query->execute()->fetchAll();
    }
}
```

**DIC-Registrierung:**
```php
$services->set(LocalBundleReader::class)
    ->parent(AbstractReader::class)
    ->tag('shopware.migration.reader');
```

### 5. Converter erstellen

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

        // Relationen auflösen (Mapping bereits migrierter Entitaeten)
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

**DIC-Tag:** `shopware.migration.converter`

### 6. Writer erstellen

```php
class BundleWriter extends AbstractWriter
{
    public function supports(): string { return BundleDataSet::getEntity(); }
}
```

**DIC-Registrierung:**
```php
$services->set(BundleWriter::class)
    ->parent(AbstractWriter::class)
    ->args([
        service(EntityWriter::class),
        service(BundleDefinition::class), // EntityDefinition des Ziel-Entities
    ])
    ->tag('shopware.migration.writer');
```

## B) Converter dekorieren + Premapping-Reader (Converter-Extension)

### Premapping-Reader erstellen

Erlaubt Benutzern, SW5-Hersteller manuell SW6-Herstellern zuzuordnen:

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
        $this->fillConnectionPremappingDictionary($migrationContext); // Bestehende Zuordnungen laden
        $mapping = $this->getMapping($migrationContext); // Quelldaten lesen
        $choices = $this->getChoices($context);          // Ziel-Optionen lesen
        $this->setPreselection($mapping);                // Automatisch vorausfuellen

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

**DIC-Tag:** `shopware.migration.pre_mapping_reader`

Administration-Snippet fuer Premapping-Karten-Titel:
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

### Converter dekorieren

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

        // Premapping-Zuordnung lesen
        $mapping = $this->mappingService->getMapping(
            $migrationContext->getConnection()->getId(),
            ManufacturerReader::getMappingName(),
            $manufacturerId,
            $context
        );

        // Original-Converter ausfuehren
        $convertedStruct = $this->originalProductConverter->convert($data, $context, $migrationContext);

        if ($mapping === null) {
            return $convertedStruct;
        }

        // Premapping-Ergebnis in konvertierte Daten einbauen
        $converted = $convertedStruct->getConverted();
        $converted['manufacturerId'] = $mapping['entityUuid'];
        return new ConvertStruct($converted, $convertedStruct->getUnmapped(), $convertedStruct->getMappingUuid());
    }
}
```

**DIC-Registrierung:**
```php
$services->set(Shopware55DecoratedProductConverter::class)
    ->decorate(Shopware55ProductConverter::class)  // Zu dekorierender Original-Converter
    ->args([
        service('.inner'),
        service(MappingService::class),
        service(LoggingService::class),
        service(MediaFileService::class),
    ]);
```

## C) Neues Profil von Grund auf (Drittanbieter-System)

### Mindest-Implementierung

1. **Profile** implementiert `ProfileInterface` — `getName()`, `getSourceSystemName()`, `getVersion()`
2. **Gateway** implementiert `GatewayInterface` — `read()`, `readEnvironmentInformation()`, `readTotals()`
3. **Credentials-Seite** in Administration: Vue-Komponente `swag-migration-profile-{profileName}-{gatewayName}-credential-form`
4. **DataSet + DataSelection** fuer jede zu migrierende Entitaet
5. **Reader** liest Quelldaten paginiert
6. **Converter** transformiert in SW6-Struktur
7. **Writer** (oft `AbstractWriter` mit korrekter `EntityDefinition` ausreichend)

### Komponentennamen-Konvention fuer Administration

```
swag-migration-profile-{profileName}-{gatewayName}-credential-form
```

Beispiel: `swag-migration-profile-ownProfile-local-credential-form`

### Optionale Plugin-Konditionalitaet (wenn Migration Assistant optional ist)

In der Plugin-Basisklasse bedingt laden:
```php
if (class_exists(MigrationAssistantPluginClass::class)) {
    // Migration-Services laden
}
```

Getrennte DIC-Konfigurationsdatei: `migration_assistant_extension.php`

## D) Migration Connector (SW5 API) erweitern

### Repository (SW5-Seite)

```php
class BundleRepository extends AbstractRepository
{
    public function fetch($offset = 0, $limit = 250): array
    {
        $ids = $this->fetchIdentifiers('s_bundles', $offset, $limit);
        // ... Daten via Doctrine DBAL lesen
    }
}
```

**DIC:** `->parent(AbstractRepository::class)`

### Service (SW5-Seite)

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

### API-Controller (SW5-Seite, Shopware 5 MVC)

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

### API-Reader (SW6-Seite, erbt von ApiReader)

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
        return 'SwagMigrationBundles'; // Entspricht SW5 API Controller-Name
    }
}
```

**DIC-Tag:** `shopware.migration.reader`
