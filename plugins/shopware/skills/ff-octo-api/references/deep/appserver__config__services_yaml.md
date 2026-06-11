# config/services.yaml (`ResubmissionAppServer/config/services.yaml`)

## Zweck
Symfony-DI-Konfiguration des AppServers. Standard-Autowiring/Autoconfigure; registriert alle Klassen aus `src/` als Services.

## Inhalt
- `_defaults`: `autowire: true`, `autoconfigure: true`.
- `App\:` resource `../src/` (Service pro Klasse).
- Keine expliziten Service-Definitionen nötig (alles per Autowiring: Controller, `AdminApiService`, `ModuleActionService`).

## Bezüge
`src/*`, `Service/AdminApiService.php`, `Service/ModuleActionService.php`.
