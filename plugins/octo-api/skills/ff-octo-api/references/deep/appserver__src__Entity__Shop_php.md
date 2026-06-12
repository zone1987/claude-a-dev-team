# Shop (`ResubmissionAppServer/src/Entity/Shop.php`)

## Zweck
Doctrine-Entity der einzigen AppServer-Tabelle `shop`: speichert die Registrierungs-/OAuth-Daten des verbundenen Shopware-Shops. Erbt alles von der SDK-Basisklasse.

## Typ & Vererbung
- Namespace `App\Entity`, `#[Entity]`, `class Shop extends Shopware\AppBundle\Entity\AbstractShop`, `declare(strict_types=1)`.

## Felder
Geerbt von `AbstractShop`: u.a. `shopId`, `shopUrl`, `shopSecret`, `shopClientId`, `shopClientSecret`, `shopActive` (Getter `getShopUrl()`, `getShopClientId()`, `getShopClientSecret()`, `getShopSecret()`, `getShopId()`).

## Besonderheiten
- Konfiguriert in `config/packages/shopware_app.yaml` (`doctrine.shop_class`). Migration `Version20251211103914` legt die Tabelle an.

## Bezüge
`config/packages/shopware_app.yaml`, `migrations/Version20251211103914.php`, `Service/AdminApiClient.php` (nutzt die Credentials).
