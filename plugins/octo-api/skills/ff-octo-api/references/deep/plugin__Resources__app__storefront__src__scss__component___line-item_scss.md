# SCSS component/_line-item.scss (`.../scss/component/_line-item.scss`)

## Zweck
Stylt die OCTO-spezifische Line-Item-Darstellung im Offcanvas/Warenkorb (Units-Liste, Reservierungs-Hinweis) und blendet bei OCTO-Produkten die Standard-Mengensteuerung aus (`.line-item-quantity.is-octo-product { display: none }`).

## Typ
- SCSS (≈62 Zeilen).

## Besonderheiten
- `is-octo-product`-Klasse versteckt die Standard-Quantity-Box (OCTO-Mengen kommen aus Units).

## Bezüge
`views/storefront/component/line-item/type/product.html.twig`, `variables/_custom.scss`.
