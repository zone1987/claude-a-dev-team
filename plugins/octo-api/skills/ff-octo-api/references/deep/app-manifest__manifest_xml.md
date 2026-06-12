# manifest.xml (`shopware/custom/apps/FfResubmission/manifest.xml`)

## Zweck
Manifest der Shopware-App **FfResubmission** — registriert den ResubmissionAppServer in der Admin: zwei Iframe-Module, die Order-Custom-Fields, die Admin-API-Permissions und den OAuth-Registrierungs-Handshake. Bindeglied zwischen Shop, AppServer und FfOctoApi-Plugin.

## Inhalt (Zusammenfassung)
- **meta:** name `FfResubmission`, v1.0.0, Autor Nico Schnaß / A-Dev-Team, Icon.
- **custom-fields** (Set `resubmission` auf `order`): `resubmission_active` (bool), `resubmission_date` (datetime), `resubmission_note` (text-area), `resubmission_user` (single-entity-select → user).
- **admin module** `resubmission` (parent `sw-order`) → `https://resubmissionappserve.dev.44go.shop/resubmission`; `customProductTemplate` (parent `sw-catalogue`) → `…/customProductTemplate`.
- **setup:** `registrationUrl` `…/app/lifecycle/register`, `secret`.
- **permissions:** order:read/update + Order-Detail-Reads, `product:read/create/update/delete`, `ff_octo_product:read/create/update`, `property_group(_option):*`, `product_configurator_setting:*`, `product_option:*`, `product_manufacturer:create/update`, tax/currency/user/… reads.

→ **Vollständige Detailerklärung in `../appserver-integration.md`** (Abschnitt „Shopware-App FfResubmission").

## Besonderheiten / Fallstricke
- Name/Secret müssen mit `config/packages/shopware_app.yaml` des AppServers übereinstimmen.
- Änderungen an Route/URL/Custom-Field/Permission → Manifest mitziehen + App neu installieren.

## Bezüge
`../appserver-integration.md`, `ResubmissionAppServer/*`, FfOctoApi `CheckoutService` (resubmission), `VariantController`/`PropertyController`.
