# Shopware app system — complete concept documentation

Sources: `concepts/extensions/apps-concept.md`, `concepts/framework/in-app-purchases.md`

---

## App system (apps-concept.md)

The app system makes it possible to extend and adapt Shopware functionality and appearance.
It uses well-defined extension points.

### Architectural principle

**Decoupling** from Shopware:
- Only the HTTP interface has to be understood (no knowledge of Shopware internals needed)
- Free choice of technology for the app backend server
- Deployment of Shopware and the app is independent
- Admin API + webhooks as the communication medium (instead of language constructs)

**Consequence**: an app is automatically multi-tenant cloud-compatible (Shopware SaaS).

### Manifest (`manifest.xml`)

The central link between Shopware and the app:
- Defines the available features
- Describes the endpoints for Shopware requests
- Declares permissions
- Registers webhooks, actions, CMS blocks, etc.

More details: the App Base Guide in the Shopware documentation.

### Communication Shopware ↔ app

**Shopware → app** (events/webhooks):
- HTTP POST to the endpoints defined in manifest.xml
- The app subscribes to the events it cares about

**App → Shopware** (data):
- Admin REST API for reading and writing Shopware data

**Security**: registration handshake on installation:
- Shopware verifies the app backend server
- The app receives credentials for API authentication

**Optional**: if app and Shopware do not need to communicate (e.g. a pure theme app),
registration is optional.

### App capabilities

#### 1. Adapt the storefront appearance

Ship assets (Twig templates, JS sources, SCSS, snippets) with `manifest.xml`.
Shopware rebuilds the storefront automatically on app installation.
No need to serve the assets from an external server.

#### 2. Integrate payment providers (from 6.4.1.0)

**Synchronous payments**: no user interaction; approval via a background request.
**Asynchronous payments**: user redirect; the app supplies the redirect URL;
after the return: Shopware verifies the payment status with the app.

#### 3. App scripts (from 6.4.8.0)

Business logic **inside the Shopware execution stack** (not on an external server):
- Use case 1: load additional data to be rendered in the storefront
- Use case 2: manipulate the cart
- Implementation: Twig-based (safer than direct PHP)
- Runs inside Shopware, not on the app server → no webhook needed

#### 4. Custom rule builder conditions (from 6.4.12.0)

Add custom conditions for the rule builder.
Declared in `manifest.xml`.

---

## In-app purchases / IAP (in-app-purchases.md)

Available from Shopware 6.6.9.0.

### Concept

Features behind a paywall **within the same extension** — a free tier with limited features,
a paid version with more features.

### Creating an IAP

Created in the Shopware Account.
Documentation: the extension partner area in the Shopware Account.

### Token mechanism (JWT)

- Every in-app purchase is represented by a **signed JWT** (issued per extension)
- The JWT guarantees that purchase data cannot be manipulated or forged
- **All purchased IAPs** are part of the JWT claims

**Verification**:
- JWKS: `https://api.shopware.com/inappfeatures/jwks`
- Shopware verifies the signature automatically for core and admin

**Token refresh**:
- Automatically on new purchases and on periodic updates
- Manually: `bin/console scheduled-task:run-single in-app-purchase.update`
- Or: `POST /api/_action/in-app-purchases/refresh`

### IAP for apps (recommended)

Optimised for the app server use case:
- The IAP JWT is sent along with **every** request from Shopware to the app server
- The app server validates active purchases and unlocks the corresponding features
- Apps are inherently safer for IAP (no direct code access)

### IAP for plugins (less recommended)

Plugins are less secure due to their open nature (more susceptible to spoofing/tampering).

### Checkout process

Shopware handles the **entire checkout process** (payment + subscription management).
The extension only needs to supply the IAP identifier → a modal window for the purchase opens automatically.
