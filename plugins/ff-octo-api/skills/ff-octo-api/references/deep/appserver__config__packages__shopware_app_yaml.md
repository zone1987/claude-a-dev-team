# config/packages/shopware_app.yaml (`ResubmissionAppServer/config/packages/shopware_app.yaml`)

## Zweck
Konfiguration des `shopware/app-bundle`: App-Name/-Secret (aus Env), Shop-Speicher und Shop-Entity.

## Inhalt
- `name: %env(SHOPWARE_APP_NAME)%` (= `FfResubmission`, muss zum Manifest passen).
- `secret: %env(SHOPWARE_APP_SECRET)%` (= Manifest-`<secret>`, für Signatur/Handshake).
- `storage: auto`.
- `doctrine.shop_class: App\Entity\Shop`.

## Besonderheiten / Fallstricke
- **Name + Secret müssen mit `FfResubmission/manifest.xml` übereinstimmen** — sonst scheitert die App-Registrierung/Signaturprüfung.

## Bezüge
`src/Entity/Shop.php`, `manifest.xml`, `.env`, `../appserver-integration.md`.
