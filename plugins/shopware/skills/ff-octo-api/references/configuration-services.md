# Konfiguration & Service-Definitionen

## Plugin-Konfiguration (config.xml)

**Datei:** `src/Resources/config/config.xml`

### Card 1: Allgemeine Einstellungen

**expirationTime** (Single-Select)
- Typ: `<component name="sw-single-select">`
- Default: 10800
- Optionen: 0 (Kein Cache), 3600 (1h), 7200 (2h), 10800 (3h)
- Verwendung: Cache-TTL für API-Responses

**bookingReservationTime** (Single-Select)
- Default: 30
- Optionen: 5, 10, 15, 20, 25, 30, 45, 60 (Minuten)
- Verwendung: Wie lange eine Buchungsreservierung gültig bleibt

### Card 2: API-Schlüssel

**goldentoursApiKey** (Password)
- Config-Key: `FfOctoApi.config.goldentoursApiKey`
- Env-Variable: `OCTO_API_KEY_GOLDEN_TOURS` (hat Vorrang!)

**gocityApiKey** (Password)
- Config-Key: `FfOctoApi.config.gocityApiKey`
- Env-Variable: `OCTO_API_KEY_GO_CITY`

**demoApiKey** (Password)
- Config-Key: `FfOctoApi.config.demoApiKey`
- Env-Variable: `OCTO_API_KEY_DEMO`

### Card 3: Provision

**provisionValue** (Float)
- Default: 10 (= 10%)
- Verwendung: Wird vom Netto-Preis abgezogen
- Override: Custom Field `rk_product_provision_value` pro Produkt

### Card 4: Testing

**testingEnvironment** (Bool)
- Default: true
- Verwendung: Setzt HTTP-Header `Octo-Env: test` (statt `live`)

---

## Service-Definitionen (XML)

### services.xml (Hauptdatei)

```xml
<!-- Imports -->
<import resource="definitions.xml"/>
<import resource="extensions.xml"/>
<import resource="controllers.xml"/>
<import resource="clients.xml"/>
<import resource="subscribers.xml"/>
<import resource="scheduledTasks.xml"/>
<import resource="twig.xml"/>
<import resource="checkout.xml"/>
<import resource="validations.xml"/>
<import resource="commands.xml"/>

<!-- Services -->
<service id="FfOctoApi\Service\PriceService">
    <argument type="service" id="monolog.logger.octo"/>
    <argument type="service" id="product.repository"/>
    <argument type="service" id="currency.repository"/>
    <argument type="service" id="FfOctoApi\Core\Api\Octo\OctoApiClientRegistry"/>
    <argument type="service" id="FfOctoApi\Service\PropertyService"/>
    <argument type="service" id="Shopware\Core\System\SystemConfig\SystemConfigService"/>
</service>

<service id="FfOctoApi\Service\PropertyService">
    <argument type="service" id="monolog.logger.octo"/>
    <argument type="service" id="property_group.repository"/>
    <argument type="service" id="property_group_option.repository"/>
</service>

<service id="FfOctoApi\Service\MediaService">
    <argument type="service" id="product.repository"/>
    <argument type="service" id="media.repository"/>
    <argument type="service" id="media_folder.repository"/>
    <argument type="service" id="Shopware\Core\Content\Media\MediaUploadService"/>
</service>

<service id="FfOctoApi\Service\SessionService"/>

<service id="FfOctoApi\Service\BookingService">
    <argument type="service" id="monolog.logger.octo"/>
    <argument type="service" id="FfOctoApi\Core\Api\Octo\OctoApiClientRegistry"/>
    <argument type="service" id="FfOctoApi\Service\ValidationService"/>
</service>

<service id="FfOctoApi\Service\ValidationService">
    <argument type="service" id="validator"/>
    <argument type="service" id="FfOctoApi\Constraint\ConstraintCollectionRegistry"/>
</service>

<service id="FfOctoApi\Service\StateService">
    <argument type="service" id="order.repository"/>
    <argument type="service" id="state_machine_transition.repository"/>
    <argument type="service" id="monolog.logger.octo"/>
</service>

<service id="FfOctoApi\Service\CheckoutService">
    <argument type="service" id="order.repository"/>
    <argument type="service" id="product.repository"/>
    <argument type="service" id="customer.repository"/>
    <argument type="service" id="monolog.logger.octo"/>
    <argument type="service" id="FfOctoApi\Core\Api\Octo\OctoApiClientRegistry"/>
</service>
```

### clients.xml

```xml
<service id="FfOctoApi\Core\Api\Octo\OctoApiClientRegistry">
    <argument type="tagged_iterator" tag="octo.api.client"/>
</service>

<!-- Jeder Client bekommt: -->
<service id="FfOctoApi\Client\Octo\GoldenToursClient">
    <argument type="service" id="Shopware\Core\System\SystemConfig\SystemConfigService"/>
    <argument type="service" id="http_client"/>
    <argument type="service" id="monolog.logger.octo"/>
    <argument type="service" id="cache.app"/>
    <tag name="octo.api.client"/>
</service>
```

### checkout.xml

```xml
<service id="FfOctoApi\Core\Checkout\Cart\OctoCartCollector">
    <argument type="service" id="request_stack"/>
    <argument type="service" id="Shopware\Core\Checkout\Cart\Price\PriceDefinitionFactory"/>
    <argument type="service" id="monolog.logger.octo"/>
    <tag name="shopware.cart.processor" priority="6000"/>
    <tag name="shopware.cart.collector" priority="6000"/>
</service>
```

### validations.xml

```xml
<service id="FfOctoApi\Constraint\ConstraintCollectionRegistry">
    <argument type="tagged_iterator" tag="octo.validation.constraint-collection"/>
</service>

<service id="FfOctoApi\Constraint\Booking\ReservationConstraintCollection">
    <tag name="octo.validation.constraint-collection"/>
</service>
<service id="FfOctoApi\Constraint\Availability\AvailabilityCheckConstraintCollection">
    <tag name="octo.validation.constraint-collection"/>
</service>
<service id="FfOctoApi\Constraint\Availability\AvailabilityCalendarConstraintCollection">
    <tag name="octo.validation.constraint-collection"/>
</service>
```

### definitions.xml

```xml
<service id="FfOctoApi\Core\Content\OctoProduct\OctoProductDefinition">
    <tag name="shopware.entity.definition"/>
</service>
```

### extensions.xml

```xml
<service id="FfOctoApi\Extension\Content\Product\ProductExtension">
    <tag name="shopware.entity.extension"/>
</service>
```

### twig.xml

```xml
<service id="FfOctoApi\Twig\TwigFilters">
    <tag name="twig.extension"/>
</service>
```

---

## Composer Dependencies

```json
{
    "require": {
        "php": ">=8.3",
        "symfony/uid": "^7.3"
    },
    "require-dev": {
        "shopware/core": "6.7.*",
        "phpunit/phpunit": "^11.5.17",
        "vimeo/psalm": "^6.10",
        "symplify/easy-coding-standard": "*",
        "squizlabs/php_codesniffer": "^3.13",
        "frosh/shopware-rector": "^0.5",
        "rector/rector": "^2.0"
    },
    "conflict": {
        "shopware/core": "<6.7 || >=6.8"
    }
}
```

---

## Quality Scripts

```bash
composer rector        # Rector dry-run
composer rector-fix    # Rector apply
composer psalm         # Psalm Level 4
composer phpcs         # PHP CodeSniffer
composer phpcs-fix     # PHP-CS-Fixer
composer ecs           # Easy Coding Standard
composer ecs-fix       # ECS fix
composer phpdoc        # PHPDocumentor
composer quality-gate  # psalm + ecs + phpcs
composer all-checks    # psalm + ecs + phpcs + rector
```

---

## GitLab CI

```yaml
stages:
  - deploy

deploy:
  image: reg.dev44.de/docker/deploy-env
  tags: [docker]
  stage: deploy
  script:
    - 'curl --header "Job-Token: $CI_JOB_TOKEN" --data tag=$CI_COMMIT_TAG "${CI_API_V4_URL}/projects/$CI_PROJECT_ID/packages/composer"'
  only:
    - tags
```

Deployment nur bei Tags — publiziert als Composer-Paket auf GitLab.
