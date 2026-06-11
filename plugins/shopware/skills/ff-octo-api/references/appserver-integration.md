# ResubmissionAppServer — Integration mit FfOctoApi

Der **ResubmissionAppServer** ist eine eigenständige Symfony-7-App (separates Repo, NICHT Teil des
Shopware-Plugins) und liegt typischerweise unter `/Users/andreasgerhardt/Projekte/AppServers/ResubmissionAppServer`.
Er ist eine **Shopware App** (`shopware/app-bundle ^4.2`) und erfüllt zwei Aufgaben, die beide
mit FfOctoApi verzahnt sind:

1. **RheinKurier-Produktanlage** (Non-API-Produkte) — schreibt direkt in die `ff_octo_product`-Entity.
2. **Wiedervorlagen-Verwaltung** (Resubmission) von Bestellungen — korrespondiert mit dem
   `resubmission_active`-Flow in `CheckoutService`.

Beide UIs erscheinen als **Iframe-Module in der Shopware-Administration** (über die Shopware-App-
Mechanik). Der AppServer hat selbst **keine Produkt-/Bestelldaten** in der eigenen DB — er hält nur
eine `shop`-Tabelle mit den OAuth-Credentials des registrierten Shops und arbeitet sonst
**live über die Shopware Admin API**.

> **Zwei zusammengehörige Artefakte:** Es gibt (a) den AppServer (Symfony-Repo, liefert die UI/Logik)
> und (b) die **Shopware-App `FfResubmission`** im Shop selbst unter
> `shopware/custom/apps/FfResubmission/`. Die App besteht praktisch nur aus `manifest.xml` (+ Icon) und
> ist das Bindeglied: sie registriert die Iframe-Module, definiert die Order-Custom-Fields, vergibt die
> Admin-API-Permissions und stellt den OAuth-Handshake her. Ohne dieses Manifest „existiert" der
> AppServer für die Admin nicht.

> **WICHTIG — Korrektur eines verbreiteten Missverständnisses:** RheinKurier-Produkte werden NICHT
> rein „manuell als Shopware-Produkt" angelegt. Sie entstehen über den ResubmissionAppServer, der per
> Admin-API ein `product` mit `ffOctoProduct`-Association erzeugt. Der Offline-Charakter
> (`RheinKurierClient::OFFLINE = true`) bezieht sich nur darauf, dass zur Laufzeit **keine OCTO-API**
> aufgerufen wird — die Daten kommen aus dem AppServer in die `ff_octo_product`-Entity.

## Tech-Stack (AppServer)

- PHP >= 8.2, Symfony 7.4
- `shopware/app-bundle` ^4.2 (Lifecycle, Webhooks, ModuleAction-Context, Shop-Registrierung)
- Frontend: Vue 3 + Meteor Component Library, Webpack Encore, Stimulus (CSRF)
- DB (eigene): nur `shop`-Tabelle (`migrations/Version20251211103914.php`)
- App-Name: `FfResubmission` (env `SHOPWARE_APP_NAME`), Config `config/packages/shopware_app.yaml`
- Tooling: PHPStan Level 6, Rector, GitLab CI (build → deploy via Deployer). **Keine Tests vorhanden.**

## Controller & Routen (AppServer)

| Controller | Route | Methode | Zweck |
|-----------|-------|---------|-------|
| `MainController` | `/` | GET | Landing Page |
| `ResubmissionController` | `/resubmission` | GET | Wiedervorlagen-Liste |
| | `/resubmission/add` | GET | Add-Formular |
| | `/resubmission/{id}/edit` | GET/POST | Wiedervorlage bearbeiten/speichern |
| | `/resubmission/orders` | POST | Bestellungen suchen (State/User/Sort) via Admin API |
| | `/resubmission/order/{id}/{resubmissionState}/toggle` | POST | Wiedervorlage-Status togglen |
| | `/resubmission/users` | POST | Benutzer für Filter |
| `CustomProductController` | `/customProductTemplate` | GET/POST | RheinKurier-Produkte listen/paginieren |
| | `/customProductTemplate/add` | GET/POST | Produkt + Varianten anlegen |
| | `/customProductTemplate/{id}/edit` + `/customProductTemplate/edit` | GET/POST | Produkt bearbeiten |
| | `/customProductTemplate/currency` | POST | Verfügbare Währungen |

## Shopware-App `FfResubmission` (`shopware/custom/apps/FfResubmission/manifest.xml`)

Das Manifest (Schema `manifest-3.0.xsd`, App-Name `FfResubmission`, Version 1.0.0, Autor Nico Schnaß /
Forty-Four) ist die vollständige Registrierung. Inhalt im Detail:

**Admin-Module (Iframes):**
| Modul | `source` | `parent` | `position` |
|-------|----------|----------|-----------|
| `resubmission` | `https://resubmissionappserve.dev.44go.shop/resubmission` | `sw-order` | 50 |
| `customProductTemplate` | `https://resubmissionappserve.dev.44go.shop/customProductTemplate` | `sw-catalogue` | 50 |

→ Die `source`-URLs zeigen exakt auf die AppServer-Routen `ResubmissionController` bzw.
`CustomProductController`. Die Iframes erscheinen in der Admin unter Bestellungen bzw. Katalog.

**Custom-Fields (definiert HIER, nicht im FfOctoApi-Plugin), Set `resubmission` auf Entity `order`:**
- `resubmission_active` (bool), `resubmission_date` (datetime), `resubmission_note` (text-area),
  `resubmission_user` (single-entity-select → `user`).
→ Genau diese Felder setzt/liest der `ResubmissionController` des AppServers und korrespondieren mit der
  Resubmission-Logik in `CheckoutService`.

**Setup / Registrierung:**
- `registrationUrl`: `https://resubmissionappserve.dev.44go.shop/app/lifecycle/register`
  (vom `shopware/app-bundle` bereitgestellte Lifecycle-Route, prefix `/app`).
- `secret`: im Manifest hinterlegt (entspricht `SHOPWARE_APP_SECRET` des AppServers) → signierter
  Handshake, woraufhin der Shop dem AppServer client_id/secret übergibt (gespeichert in der `shop`-Tabelle).

**Permissions (zeigen die Kopplung exakt):**
- Order/Read-Bündel + `order:update` (Wiedervorlagen-Toggle, Custom-Fields).
- `product:read/create/update/delete`, `tax:read`, `product_manufacturer:create/update`.
- `ff_octo_product:read/create/update` ← schreibt die OCTO-Produktdaten.
- `product_configurator_setting:create/update`, `product_option:create/update`,
  `property_group(_option):create/update/delete` ← Varianten-/Property-Erzeugung (via FfOctoApi
  `VariantController` / `PropertyController`).
- `user:read`, `currency:read`, `payment_method:read`, `shipping_method:read`, `state_machine_state:read`,
  `country:read`, `document:read`, `sales_channel:read`, `order_customer/address/transaction/delivery:read`.

> Ändert sich eine AppServer-Route, eine `source`-URL, ein Custom-Field-Name oder ein benötigtes
> Admin-API-Recht, muss das **Manifest** mitgezogen werden (App neu installieren/aktualisieren). Manifest,
> AppServer und FfOctoApi-Plugin bilden zusammen den Vertrag.

## Datenfluss: AppServer → `ff_octo_product` (kritisch)

Kernklasse: `src/Service/AdminApiClient.php` (~822 LOC). Ablauf bei Produktanlage
(`CustomProductController::add` POST → `AdminApiClient::addProduct`):

1. **OAuth2** gegen den Shop: `POST {shopUrl}/api/oauth/token` (grant_type `client_credentials`,
   client_id/secret aus der `shop`-Entity).
2. Produktnummer reservieren (`/api/_action/number-range/reserve/product`), Steuersatz + Währung holen.
3. **`ffOctoProduct`-Struktur bauen** (hardcodiert):
   - `identifier = 'rheinkurier'`
   - `reference = 'GTP2'` (Produkt-Reference)
   - `id` = deterministischer Hash aus UUID + `GTP2` + `rheinkurier`
   - `product` = JSON mit `internalName`, `title`, `timeZone` (`Europe/Berlin`), `brand` (`Rhein-Kurier`),
     `options[]` (Optionen/Units mit Preisen — aus dem Vue-Formular `custom-product-form.vue`).
4. **`POST {shopUrl}/api/product`** mit `ffOctoProduct` als Association-Payload.
5. **`generateVariants()`** ruft **`POST {shopUrl}/api/product-variants/create`** auf — das ist die
   **Naht zum Plugin**: dieser Endpunkt ist der `VariantController` von FfOctoApi
   (`src/Controller/VariantController.php`). D.h. der AppServer nutzt direkt einen FfOctoApi-Plugin-
   Endpunkt, um Shopware-Varianten aus der OCTO-Options-Struktur zu erzeugen.

Bearbeiten (`AdminApiClient` ~Z. 682): `PATCH {shopUrl}/api/product/{id}` mit neuem `ffOctoProduct`,
danach erneut `generateVariants()`.

Listen/Filtern (`AdminApiClient` ~Z. 336): `/api/search/product` mit Filter
`ffOctoProduct.identifier == 'rheinkurier'` (hardcodiert), liest `ff_octo_product` aus `included`.

```
Shopware Admin (Iframe-Modul "FfResubmission")
   │  ModuleAction-Context (shopId, shopUrl, secret)
   ▼
ResubmissionAppServer (CustomProductController / ResubmissionController)
   │  Vue/Meteor-Formular  →  AdminApiClient
   ▼
OAuth2 Bearer  →  Shopware Admin API
   ├─ POST /api/product            (product + ffOctoProduct-Association)
   ├─ POST /api/product-variants/create   ←── FfOctoApi VariantController!
   └─ GET  /api/search/product     (Filter ffOctoProduct.identifier=rheinkurier)
   ▼
Shopware DB: product + ff_octo_product   (identifier='rheinkurier', product=JSON)
```

## Resubmission-Kopplung zu FfOctoApi

Der AppServer setzt/togglet auf der Order die Custom-Fields `resubmission_active`,
`resubmission_date`, `resubmission_note`, `resubmission_user` (über die Admin API). Diese Felder werden
durch das `FfResubmission`-Manifest auf der `order`-Entity angelegt (siehe Abschnitt oben).
Im Plugin korrespondiert das mit der Resubmission-Mechanik in
`src/Service/CheckoutService.php`: schlägt eine OCTO-Buchungsbestätigung fehl, wird die Order zur
Wiedervorlage markiert (Audit-Trail im Order-Kommentar). Der AppServer ist das UI, über das diese
Wiedervorlagen gesichtet und abgearbeitet werden.

## Berührungspunkte / typische Fehlerquellen über die Repo-Grenze

| Berührungspunkt | Plugin-Seite | AppServer-Seite | Risiko |
|-----------------|--------------|-----------------|--------|
| Varianten-Erzeugung | `VariantController` (`/api/product-variants/create`) | `AdminApiClient::generateVariants()` | Vertragsbruch: ändert sich Payload/Route im Plugin, brechen RheinKurier-Varianten |
| `ff_octo_product`-Schema | `OctoProductDefinition` (uuid/identifier/product-JSON) | `AdminApiClient::addProduct()` baut JSON | Strukturabweichung der `options`/`units` → Preis-/Anzeigefehler im Storefront |
| Hardcodierte Werte | RheinKurier-Pfade, `isOffline()` | `identifier='rheinkurier'`, `reference='GTP2'` | Beide Seiten müssen synchron bleiben |
| Resubmission | `CheckoutService` setzt Flag | `ResubmissionController` listet/toggelt | Custom-Field-Namen müssen übereinstimmen |
| Preis/Provision | `PriceService` (`rk_product_provision_value`) | Preise im Vue-Formular gepflegt | Offline-Fallback in `PriceService` muss zur AppServer-`options`-Struktur passen |

## Bei Änderungen beachten

- Wird im Plugin der `VariantController` oder die `ff_octo_product`-Struktur (`options`/`units`) geändert,
  **muss** `AdminApiClient` im AppServer mitgezogen werden (und umgekehrt). Das ist der zentrale
  Cross-Repo-Vertrag.
- Der AppServer hat keine Tests — Änderungen dort manuell über das Iframe-Modul verifizieren.
