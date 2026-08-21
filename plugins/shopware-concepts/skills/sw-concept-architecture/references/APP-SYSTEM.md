# Shopware app system — concept

Complete concept documentation: `APP-SYSTEM-DETAIL.md`

## Brief overview

The app system decouples extensions from the Shopware core — free choice of technology, cloud-compatible.

### Core concepts

- **Manifest** (`manifest.xml`) — the central link; defines features, endpoints, permissions
- **Registration handshake** — on installation; Shopware verifies the app server, the app receives API credentials
- **Webhooks** — Shopware sends an HTTP POST to the app for defined events
- **Admin API** — the app reads/writes Shopware data via the Admin API

### Capabilities

| Feature | Description |
|---|---|
| Storefront assets | Ship Twig templates, SCSS, JS, snippets |
| App scripts | Execute business logic inside the Shopware process (Twig-based) |
| Payment | Implement sync/async payments |
| Rule conditions | Custom rule builder conditions |
| CMS blocks | Provide custom CMS elements |

### In-app purchases (from 6.6.9.0)

- Features behind a paywall within the same extension
- One JWT per extension — signed, tamper-proof
- Shopware handles the checkout process (payment, subscription)
- JWKS verification: `https://api.shopware.com/inappfeatures/jwks`
- The IAP JWT is sent along with every app server request

Technical implementation: `shopware-apps` (dev plugin)
