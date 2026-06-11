# config/routes/shopware_app.yaml (`ResubmissionAppServer/config/routes/shopware_app.yaml`)

## Zweck
Bindet die vom `shopware/app-bundle` bereitgestellten Lifecycle- und Webhook-Routen ein (Prefix `/app`).

## Inhalt
- `shopware_app_lifecycle` → `@ShopwareAppBundle/.../lifecycle.xml`, prefix `/app`.
- `shopware_app_webhook` → `@ShopwareAppBundle/.../webhook.xml`, prefix `/app`.

## Besonderheiten
- `/app/lifecycle/register` ist die `registrationUrl` aus dem Manifest (App-Installation/Handshake).

## Bezüge
`manifest.xml` (`registrationUrl`), `../appserver-integration.md`.
