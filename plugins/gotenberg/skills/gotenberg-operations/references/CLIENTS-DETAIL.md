# Gotenberg — Clients & SDKs Reference

## Contents

- [Basic principle](#basic-principle)
- [Official client: PHP](#official-client-php)
- [Community clients](#community-clients)
- [Custom integration (no SDK)](#custom-integration-no-sdk)
- [Response handling](#response-handling)

## Basic principle

Gotenberg is a standard HTTP API. Any HTTP library in any language works.
The protocol is `multipart/form-data` (POST) with a binary file response.

Dedicated clients provide:
- Fluent interface / builder pattern
- Type safety for form fields
- Simplified file handling
- Built-in error handling

## Official client: PHP

**Package**: `gotenberg/gotenberg-php`
**Repository**: https://github.com/gotenberg/gotenberg-php

```bash
composer require gotenberg/gotenberg-php
```

Example: URL to PDF

```php
use Gotenberg\Gotenberg;
use Gotenberg\Stream;

$request = Gotenberg::chromium($apiUrl)
    ->pdf()
    ->url('https://my.url');

$response = $client->sendRequest($request);
```

Example: HTML to PDF

```php
use Gotenberg\Gotenberg;
use Gotenberg\Stream;

$request = Gotenberg::chromium($apiUrl)
    ->pdf()
    ->html(Stream::path('/path/to/index.html'));

$response = $client->sendRequest($request);
```

Example: Office document to PDF

```php
use Gotenberg\Gotenberg;
use Gotenberg\Stream;

$request = Gotenberg::libreOffice($apiUrl)
    ->pdf()
    ->convert(Stream::path('/path/to/document.docx'));

$response = $client->sendRequest($request);
```

## Community clients

Complete list: https://github.com/gotenberg/awesome-gotenberg#clients

Available community clients (as of 2026):
- **Go**: github.com/gotenberg/gotenberg-go-client
- **JavaScript / Node.js**: npm `chromiumly` or others on the Awesome list
- **Python**: on the Awesome list
- **Ruby**, **Java**, **C#** / .NET: on the Awesome list

## Custom integration (no SDK)

Since `multipart/form-data` is a standard, any HTTP library is sufficient:

### cURL (Bash)

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://my.url \
  -o output.pdf
```

### PHP (without SDK)

```php
$client = new \GuzzleHttp\Client();
$response = $client->post('http://localhost:3000/forms/chromium/convert/url', [
    'multipart' => [
        ['name' => 'url', 'contents' => 'https://my.url'],
    ],
]);
file_put_contents('output.pdf', $response->getBody());
```

### JavaScript (fetch)

```js
const form = new FormData();
form.append('url', 'https://my.url');

const response = await fetch('http://localhost:3000/forms/chromium/convert/url', {
    method: 'POST',
    body: form,
});
const buffer = await response.arrayBuffer();
fs.writeFileSync('output.pdf', Buffer.from(buffer));
```

### Python (requests)

```python
import requests

response = requests.post(
    'http://localhost:3000/forms/chromium/convert/url',
    data={'url': 'https://my.url'},
)
with open('output.pdf', 'wb') as f:
    f.write(response.content)
```

## Response handling

Success (200): binary file directly in the body.
- `Content-Disposition: attachment; filename=<name.ext>`
- `Content-Type: application/pdf` (or image/png etc.)
- `Gotenberg-Trace: <trace-id>`

Error (400/409/503): plaintext error message in the body.

---
Source: https://gotenberg.dev/docs/getting-started/clients
