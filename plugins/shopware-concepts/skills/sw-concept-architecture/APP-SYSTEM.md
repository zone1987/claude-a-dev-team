# Shopware App-System — Konzept

Vollständige Konzept-Doku: `APP-SYSTEM-DETAIL.md`

## Kurzüberblick

Das App-System koppelt Erweiterungen vom Shopware-Core ab — freie Technologiewahl, Cloud-kompatibel.

### Kernkonzepte

- **Manifest** (`manifest.xml`) — zentrales Bindeglied; definiert Features, Endpoints, Permissions
- **Registration Handshake** — bei Installation; Shopware verifiziert App-Server, App erhält API-Credentials
- **Webhooks** — Shopware sendet HTTP-POST an App für definierte Events
- **Admin API** — App liest/schreibt Shopware-Daten über Admin API

### Capabilities

| Feature | Beschreibung |
|---|---|
| Storefront-Assets | Twig-Templates, SCSS, JS, Snippets mitliefern |
| App Scripts | Business-Logik im Shopware-Prozess ausführen (Twig-basiert) |
| Payment | Sync/Async Payments implementieren |
| Rule Conditions | Eigene Rule-Builder-Bedingungen |
| CMS-Blöcke | Eigene CMS-Elemente bereitstellen |

### In-App Purchases (ab 6.6.9.0)

- Features hinter Paywall innerhalb derselben Extension
- JWT pro Extension — signiert, manipulationssicher
- Shopware übernimmt Checkout-Prozess (Payment, Subscription)
- JWKS-Verifikation: `https://api.shopware.com/inappfeatures/jwks`
- IAP-JWT wird bei jedem App-Server-Request mitgesendet

Technische Umsetzung: `shopware-apps` (Dev-Plugin)
