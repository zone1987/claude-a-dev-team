# Gotenberg — Clients & SDKs Referenz

## Grundprinzip

Gotenberg ist eine Standard-HTTP-API. Jede HTTP-Bibliothek in jeder Sprache funktioniert.
Das Protokoll ist `multipart/form-data` (POST) mit binaerer Datei-Antwort.

Dedizierte Clients bieten:
- Fluent Interface / Builder-Pattern
- Typsicherheit fuer Form-Felder
- Vereinfachtes File-Handling
- Eingebautes Error-Handling

## Offizieller Client: PHP

**Package**: `gotenberg/gotenberg-php`
**Repository**: https://github.com/gotenberg/gotenberg-php

```bash
composer require gotenberg/gotenberg-php
```

Beispiel: URL zu PDF

```php
use Gotenberg\Gotenberg;
use Gotenberg\Stream;

$request = Gotenberg::chromium($apiUrl)
    ->pdf()
    ->url('https://my.url');

$response = $client->sendRequest($request);
```

Beispiel: HTML zu PDF

```php
use Gotenberg\Gotenberg;
use Gotenberg\Stream;

$request = Gotenberg::chromium($apiUrl)
    ->pdf()
    ->html(Stream::path('/path/to/index.html'));

$response = $client->sendRequest($request);
```

Beispiel: Office-Dokument zu PDF

```php
use Gotenberg\Gotenberg;
use Gotenberg\Stream;

$request = Gotenberg::libreOffice($apiUrl)
    ->pdf()
    ->convert(Stream::path('/path/to/document.docx'));

$response = $client->sendRequest($request);
```

## Community Clients

Vollstaendige Liste: https://github.com/gotenberg/awesome-gotenberg#clients

Verfuegbare Community-Clients (Stand 2026):
- **Go**: github.com/gotenberg/gotenberg-go-client
- **JavaScript / Node.js**: npm `chromiumly` oder andere auf Awesome-Liste
- **Python**: auf Awesome-Liste
- **Ruby**, **Java**, **C#** / .NET: auf Awesome-Liste

## Eigene Integration (kein SDK)

Da `multipart/form-data` Standard ist, genuegt jede HTTP-Bibliothek:

### cURL (Bash)

```bash
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://my.url \
  -o output.pdf
```

### PHP (ohne SDK)

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

## Response-Handling

Erfolg (200): Binaere Datei direkt im Body.
- `Content-Disposition: attachment; filename=<name.ext>`
- `Content-Type: application/pdf` (oder image/png etc.)
- `Gotenberg-Trace: <trace-id>`

Fehler (400/409/503): Plaintext-Fehlermeldung im Body.

---
Quelle: https://gotenberg.dev/docs/getting-started/clients
