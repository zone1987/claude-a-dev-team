# AdminApiService (`ResubmissionAppServer/src/Service/AdminApiService.php`)

## Zweck
Factory, die pro Shop-Kontext einen `AdminApiClient` mit den jeweiligen OAuth-Credentials erzeugt.

## Typ
- Namespace `App\Service`, `class AdminApiService`.

## Konstruktor / DI
`HttpClientInterface $httpClient`.

## Methoden
- `createClient(shopUrl, clientId, clientSecret): AdminApiClient` — neuer Client mit dem geteilten HttpClient + Shop-Credentials.

## Bezüge
`AdminApiClient`, `Controller/{Resubmission,CustomProduct}Controller.php`.
