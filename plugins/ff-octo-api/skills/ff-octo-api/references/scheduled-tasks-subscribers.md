# Scheduled Tasks & Event Subscribers

## Scheduled Tasks

### 1. Cache Warm-Up

**Task:** `OctoApiWarmCacheTask`
- **Name:** `ff.octoapi.warm_cache`
- **Interval:** 10800 Sekunden (3 Stunden)
- **Datei:** `src/Service/ScheduledTask/OctoApiWarmCacheTask.php`

**Handler:** `OctoApiWarmCacheHandler`
- **Datei:** `src/Service/ScheduledTask/OctoApiWarmCacheHandler.php`

```php
public function run(): void
{
    foreach ($this->clientRegistry->getClientIdentifiers() as $identifier) {
        $client = $this->clientRegistry->getClientByIdentifier($identifier);

        if ($client->isOffline()) continue;  // RheinKurier überspringen

        $client->setCapabilities(['octo/content']);

        // Alten Cache löschen
        $this->cache->deleteItem('ff.octo-api.products.' . $client->getSupplierId());

        // Neuen Cache aufbauen
        $products = $client->getCachedProducts();

        $this->logger->info("Cached {count} products for {identifier}", [...]);
    }
}
```

### 2. Preis-Update

**Task:** `OctoApiPriceUpdaterTask`
- **Name:** `ff.octoapi.price-updater`
- **Interval:** 10800 Sekunden (3 Stunden)
- **Datei:** `src/Service/ScheduledTask/OctoApiPriceUpdaterTask.php`

**Handler:** `OctoApiPriceUpdaterHandler`
- **Datei:** `src/Service/ScheduledTask/OctoApiPriceUpdaterHandler.php`

```php
public function run(): void
{
    // Alle Produkte mit ffOctoProduct finden
    $criteria = new Criteria();
    $criteria->addFilter(new NotFilter(
        MultiFilter::CONNECTION_AND,
        [new EqualsFilter('ffOctoProductId', null)]
    ));
    $criteria->addAssociation('ffOctoProduct');

    $products = $this->productRepository->search($criteria, Context::createDefaultContext());

    foreach ($products as $product) {
        $identifier = $product->getExtension('ffOctoProduct')->getIdentifier();

        // RheinKurier überspringen
        if ($identifier === RheinKurierClient::IDENTIFIER) continue;

        $this->priceService->updatePrices($product->getId(), $identifier);
    }
}
```

### Message Queue Voraussetzung

Scheduled Tasks laufen über Symfony Messenger:
```bash
bin/console messenger:consume async scheduled_task
```

---

## Event Subscribers

### 1. ProductDetailSubscriber

**Datei:** `src/Subscriber/ProductDetailSubscriber.php`
**Event:** `ProductPageCriteriaEvent`

```php
public static function getSubscribedEvents(): array
{
    return [ProductPageCriteriaEvent::class => 'onProductPageCriteria'];
}

public function onProductPageCriteria(ProductPageCriteriaEvent $event): void
{
    $event->getCriteria()
        ->addAssociation('ffOctoProduct')
        ->addAssociation('options.group.options');
}
```

**Zweck:** Stellt sicher, dass OCTO-Produktdaten und Optionsgruppen auf der Produktdetailseite geladen werden.

---

### 2. ProductSaveSubscriber

**Datei:** `src/Subscriber/ProductSaveSubscriber.php`
**Event:** `ProductEvents::PRODUCT_WRITTEN_EVENT`

```php
public function onProductSave(EntityWrittenEvent $event): void
{
    // Rekursionsschutz
    if ($event->getContext()->hasExtension('octo_price_update')) {
        return;
    }

    foreach ($event->getIds() as $productId) {
        $product = $this->productRepository->search(
            (new Criteria([$productId]))->addAssociation('ffOctoProduct'),
            $event->getContext()
        )->first();

        if (!$product) continue;

        // Für Varianten: Parent laden (Preise auf Hauptprodukt-Ebene)
        if ($product->getParentId()) {
            $product = $this->productRepository->search(
                (new Criteria([$product->getParentId()]))->addAssociation('ffOctoProduct'),
                $event->getContext()
            )->first();
        }

        $octoProduct = $product?->getExtension('ffOctoProduct');
        if (!$octoProduct) continue;

        // Rekursionsschutz setzen
        $event->getContext()->addExtension('octo_price_update', new ArrayStruct());

        $this->priceService->updatePrices(
            $product->getId(),
            $octoProduct->getIdentifier(),
            null,
            $event->getContext()
        );
    }
}
```

**Zweck:** Aktualisiert OCTO-Preise automatisch wenn ein verknüpftes Produkt gespeichert wird.
**WICHTIG:** Rekursionsschutz via Context-Extension `octo_price_update`!

---

### 3. ProductDeleteSubscriber

**Datei:** `src/Subscriber/ProductDeleteSubscriber.php`
**Event:** `EntityDeleteEvent`

```php
public function onEntityDelete(EntityDeleteEvent $event): void
{
    // Nur Product-Entities
    $ids = $event->getIds('product');
    if (empty($ids)) return;

    // OctoProduct-IDs sammeln (BEVOR FK gelöscht wird!)
    $octoProductIds = $this->getOctoProductIds($ids);
    if (empty($octoProductIds)) return;

    // Nach erfolgreichem Delete: OctoProducts aufräumen
    $event->addSuccess(function () use ($octoProductIds) {
        $this->octoProductRepository->delete(
            array_map(fn($id) => ['id' => $id], $octoProductIds),
            Context::createDefaultContext()
        );
    });
}
```

**Zweck:** Löscht verwaiste `ff_octo_product` Einträge wenn das verknüpfte Shopware-Produkt gelöscht wird.

**Wichtig:** Die OctoProduct-IDs müssen **vor** dem Delete gesammelt werden (solange der FK noch existiert). Die eigentliche Löschung erfolgt erst nach erfolgreichem Product-Delete via `$event->addSuccess()`.

---

### 4. OrderSubscriber

**Datei:** `src/Subscriber/OrderSubscriber.php`

#### Events

```php
public static function getSubscribedEvents(): array
{
    return [
        'state_machine.order.state_changed' => 'onStateMachineStateChanged',
        'state_machine.order_transaction.state_changed' => 'onStateMachineStateTransactionChanged',
        AccountOrderPageLoadedEvent::class => 'onAccountOrderPageLoadedEvent',
        CancelOrderRouteRequestEvent::class => 'onCancelOrderRouteRequestEvent',
    ];
}
```

#### onStateMachineStateTransactionChanged — Buchung bestätigen

```php
public function onStateMachineStateTransactionChanged(StateMachineStateChangeEvent $event): void
{
    if ($event->getTransitionSide() !== StateMachineStateChangeEvent::STATE_MACHINE_TRANSITION_SIDE_ENTER) return;
    if ($event->getStateName() !== OrderTransactionStates::STATE_PAID) return;

    $orderId = $event->getTransition()->getEntityId();
    $this->checkoutService->confirmOrder($orderId, $event->getContext());
}
```

**Trigger:** Transaction-Status wechselt zu `paid`
**Aktion:** Bestätigt alle Buchungen in der Order

#### onStateMachineStateChanged — Bestellung stornieren

```php
public function onStateMachineStateChanged(StateMachineStateChangeEvent $event): void
{
    if ($event->getTransitionSide() !== StateMachineStateChangeEvent::STATE_MACHINE_TRANSITION_SIDE_ENTER) return;
    if ($event->getStateName() !== OrderStates::STATE_CANCELLED) return;

    $orderId = $event->getTransition()->getEntityId();
    $this->checkoutService->cancelOrder($orderId, $event->getContext());
}
```

**Trigger:** Order-Status wechselt zu `cancelled`
**Aktion:** Storniert alle Buchungen in der Order

#### onAccountOrderPageLoadedEvent — Stornierbarkeit prüfen

```php
public function onAccountOrderPageLoadedEvent(AccountOrderPageLoadedEvent $event): void
{
    foreach ($event->getPage()->getOrders() as $order) {
        foreach ($order->getLineItems() as $lineItem) {
            $reservationUuid = $lineItem->getPayloadValue('reservationUuid');
            if (!$reservationUuid) continue;

            $identifier = $lineItem->getPayloadValue('identifier');
            $client = $this->clientRegistry->getClientByIdentifier($identifier);

            if ($client->isOffline()) continue;

            $booking = $client->getBooking($reservationUuid);
            $lineItem->setPayloadValue('cancellable', $booking['cancellable'] ?? false);
        }
    }
}
```

**Trigger:** Account-Bestellseite wird geladen
**Aktion:** Prüft via API ob jede Buchung stornierbar ist

#### onCancelOrderRouteRequestEvent — Kunde storniert

```php
public function onCancelOrderRouteRequestEvent(CancelOrderRouteRequestEvent $event): void
{
    $orderId = $event->getRequest()->get('orderId');
    $this->checkoutService->cancelOrder($orderId, $event->getContext());
}
```

**Trigger:** Kunde klickt "Stornieren" im Account
**Aktion:** Storniert alle Buchungen

---

## CLI-Commands

### ff:log:test

**Datei:** `src/Command/LogTestCommand.php`

Schreibt Test-Eintrag in den OCTO-Logger (`var/log/octo-{env}.log`).

### ff:property-group:cleanup

**Datei:** `src/Command/PropertyGroupCleanupCommand.php`

Löscht leere/unbenutzte Property Groups. **Nur in DDEV + dev Modus** verfügbar.

---

## Service-Registrierung

### scheduledTasks.xml

```xml
<service id="FfOctoApi\Service\ScheduledTask\OctoApiWarmCacheTask">
    <tag name="shopware.scheduled.task"/>
</service>
<service id="FfOctoApi\Service\ScheduledTask\OctoApiWarmCacheHandler">
    <argument type="service" id="scheduled_task.repository"/>
    <argument type="service" id="FfOctoApi\Core\Api\Octo\OctoApiClientRegistry"/>
    <argument type="service" id="cache.app"/>
    <argument type="service" id="monolog.logger.octo"/>
    <tag name="messenger.message_handler"/>
</service>
<!-- Analog für PriceUpdater -->
```

### subscribers.xml

```xml
<service id="FfOctoApi\Subscriber\ProductDeleteSubscriber">
    <tag name="kernel.event_subscriber"/>
</service>
<!-- Analog für ProductDetailSubscriber, ProductSaveSubscriber, OrderSubscriber -->
```

### commands.xml

```xml
<service id="FfOctoApi\Command\PropertyGroupCleanupCommand">
    <tag name="console.command"/>
</service>
<service id="FfOctoApi\Command\LogTestCommand">
    <tag name="console.command"/>
</service>
```

---

## Logging

### Konfiguration (monolog.yaml)

```yaml
monolog:
    channels: ['octo']
    handlers:
        octoLogHandler:
            type: rotating_file
            path: '%kernel.logs_dir%/octo-%kernel.environment%.log'
            level: error
            max_files: 30
            channels: ['octo']
```

**Log-Datei:** `var/log/octo-{dev|prod|test}.log`
**Max Dateien:** 30 (rotierend)
**Level:** error
