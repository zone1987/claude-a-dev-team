---
title: PHP SDK Setup
impact: HIGH
impactDescription: The PHP SDK provides registration, signing, and API client for PHP app servers
tags: sdk, php, setup, composer, app-server
---

## PHP SDK Setup

The `shopware/app-php-sdk` package handles registration, HMAC verification, response signing, and OAuth2 API client.

### Installation

```bash
composer require shopware/app-php-sdk
```

For Symfony projects, use the bundle instead:

```bash
composer require shopware/app-bundle
```

### Basic Setup (Plain PHP)

```php
use Shopware\App\SDK\AppConfiguration;
use Shopware\App\SDK\Registration\RegistrationService;
use Shopware\App\SDK\Shop\ShopResolver;

$config = new AppConfiguration(
    'MyApp',
    'my-secret',
    'https://my-app.com/app/register/confirm'
);

$shopRepository = new FileShopRepository('/path/to/shops');
$registrationService = new RegistrationService($config, $shopRepository);
```

### Registration Flow

```php
// 1. Handle GET /app/register
$response = $registrationService->register($psrRequest);

// 2. Handle POST /app/register/confirm
$registrationService->registerConfirm($psrRequest);
```

### Context Resolution

```php
use Shopware\App\SDK\Context\ContextResolver;

$resolver = new ContextResolver();

// Webhook context
$webhookAction = $resolver->assembleWebhook($psrRequest, $shop);

// Action button context
$actionButton = $resolver->assembleActionButton($psrRequest, $shop);

// Module context (admin iframe)
$module = $resolver->assembleModule($psrRequest, $shop);

// Payment context
$payment = $resolver->assemblePayment($psrRequest, $shop);

// Tax provider context
$taxProvider = $resolver->assembleTaxProvider($psrRequest, $shop);
```

### Shop Resolution

```php
$shopResolver = new ShopResolver($shopRepository);
$shop = $shopResolver->resolveShop($psrRequest);
```
