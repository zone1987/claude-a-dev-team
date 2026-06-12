# Twig-Templates

## Template-Übersicht

| Template | Pfad | Zweck |
|----------|------|-------|
| buy-widget.html.twig | views/storefront/component/buy-widget/ | Shopware Buy-Widget Override |
| configurator.html.twig | views/storefront/component/buy-widget/ | OCTO-Konfigurator-Wrapper |
| octo-configurator.html.twig | views/storefront/component/buy-widget/ | Dynamischer Konfigurator-Inhalt |
| accompanied-by.html.twig | views/storefront/macros/ | Begleitperson-Macro |
| product.html.twig | views/storefront/component/line-item/type/ | Line-Item im Warenkorb |
| order-item.html.twig | views/storefront/page/account/order-history/ | Bestellhistorie |

---

## buy-widget.html.twig

**Extends:** `@Storefront/storefront/component/buy-widget/buy-widget.html.twig`

### Überschriebene Blöcke

```twig
{% block buy_widget_configurator_include %}
    {# Wenn Parent-Produkt mit Optionen und nicht Default-Variante #}
    {% if product.parentId and product.options|length > 0 and not isDefaultVariant %}
        {{ parent() }}
    {% endif %}
{% endblock %}

{% block buy_widget_price %}
    {% if not isOctoProduct %}{{ parent() }}{% endif %}
{% endblock %}

{% block buy_widget_tax %}
    {% if not isOctoProduct %}{{ parent() }}{% endif %}
{% endblock %}

{% block buy_widget_buy_form %}
    {% if not isOctoProduct %}{{ parent() }}{% endif %}
{% endblock %}
```

### Erkennung

```twig
{% set octoProduct = product.getExtension('ffOctoProduct') %}
{% set isOctoProduct = product.extensions.foreignKeys.ffOctoProductId != null %}

{# Default-Variante: Erste Option mit default: true #}
{% set isDefaultVariant = false %}
{% if octoProduct and octoProduct.product.options|first.default %}
    {% set isDefaultVariant = true %}
{% endif %}
```

Bei `isDefaultVariant`: CSS-Klasse `is-default-variant` → `visually-hidden`

---

## configurator.html.twig

**Extends:** `@Storefront/storefront/component/buy-widget/configurator.html.twig`

### Block: buy_widget_configurator

```twig
{% block buy_widget_configurator %}
    {% if isOctoProduct %}
        <div class="product-detail-configurator-container">
            {# Standard Shopware Varianten-Selector #}
            {% block buy_widget_configurator_group %}
                {{ parent() }}
            {% endblock %}

            {# OCTO Konfigurator #}
            <div data-ff-buy-box='{{ {
                apiProduct: {
                    identifier: octoProduct.identifier,
                    uuid: octoProduct.uuid,
                    product: octoProduct.product
                },
                product: { id: product.id, ... },
                selector: { wrapper: ".product-detail-configurator-details-wrapper" },
                routes: {
                    checkAvailability: path("frontend.octo-api.availability.check"),
                    getItem: path("frontend.octo-api.session.get-item"),
                    setItem: path("frontend.octo-api.session.set"),
                    removeItem: path("frontend.octo-api.session.remove-item")
                }
            }|json_encode }}'>
                <div class="product-detail-configurator-details-wrapper">
                    {% sw_include '@FfOctoApi/storefront/component/buy-widget/octo-configurator.html.twig' %}
                </div>
            </div>
        </div>
    {% else %}
        {{ parent() }}
    {% endif %}
{% endblock %}
```

---

## octo-configurator.html.twig

Wird initial und nach **jedem** AJAX-Availability-Check gerendert.

### Session-Daten

```twig
{% set sessionItem = app.request.session.get('octo-product-session-' ~ product.id)|json_decode %}
```

### Übergebene Variablen (vom Controller)

- `units` — Array von Unit-Objekten mit id, type, title, subtitle, quantity, price, restrictions
- `localStartTimes` — Array von Uhrzeiten (wenn verfügbar)
- `price` — Gesamtpreis-Objekt mit retail
- `product` — Shopware-Produkt
- `localDateStart` — Gewähltes Startdatum
- `localStartTime` — Gewählte Uhrzeit
- `status` — Verfügbarkeitsstatus (AVAILABLE, LIMITED, SOLD_OUT, FREESALE, CLOSED)
- `available` — Boolean
- `capacity` — Verfügbare Plätze

### Blöcke

#### octo_configurator__availability_state
```twig
{% if status and status != 'AVAILABLE' and status != 'FREESALE' %}
    <div class="alert alert-{{ status == 'SOLD_OUT' or status == 'CLOSED' ? 'danger' : 'warning' }}">
        {{ ('OctoApi.availability.state.' ~ status)|trans }}
    </div>
{% endif %}
```

#### octo_configurator__units
```twig
{% for unit in units %}
    <div class="detail-unit" data-browser-translation="{{ unit.type }}">
        {# Unit-Titel #}
        <span class="detail-unit-label-title">
            {{ ('OctoApi.units.' ~ unit.type)|trans }}
        </span>

        {# Alterseinschränkung #}
        {% if unit.restrictions.minAge or unit.restrictions.maxAge %}
            <span class="detail-unit-label-subtitle">
                {{ 'OctoApi.unit.subtitle'|trans({
                    '%minAge%': unit.restrictions.minAge|default('0'),
                    '%maxAge%': unit.restrictions.maxAge|default('99')
                }) }}
            </span>
        {% endif %}

        {# Begleitperson-Info #}
        {% from '@FfOctoApi/storefront/macros/accompanied-by.html.twig' import accompanied_by %}
        {{ accompanied_by(units, unit) }}

        {# Preis #}
        <span class="detail-unit-label-price">
            {{ unit.price.retail|currency }}
        </span>

        {# Mengen-Steuerung #}
        <div data-quantity-select='{{ {
            unit: unit,
            units: units
        }|json_encode }}'>
            <button class="detail-unit-quantity-subtract">-</button>
            <span class="detail-unit-quantity-count">{{ unit.quantity|default(0) }}</span>
            <button class="detail-unit-quantity-add">+</button>
        </div>
    </div>
{% endfor %}
```

#### octo_configurator__start_times
```twig
{% if localStartTimes|length > 0 %}
    <div data-time-select='{{ {
        route: path("frontend.octo-api.session.set")
    }|json_encode }}'>
        <select>
            {% for time in localStartTimes %}
                <option value="{{ time }}" {{ time == localStartTime ? 'selected' }}>
                    {{ time }}
                </option>
            {% endfor %}
        </select>
    </div>
{% endif %}
```

#### octo_configurator__date
```twig
<div data-date-select='{{ {
    apiProduct: { identifier: ..., uuid: ..., product: ... },
    selectedOptionUuid: selectedOptionUuid,
    locale: app.request.locale,
    defaultDate: localDateStart
}|json_encode }}'>
    <input type="text" class="form-control" />
</div>
```

#### octo_configurator__price
```twig
{% if price and price.retail > 0 %}
    <div class="product-detail-configurator-details-total">
        <span class="h4">{{ price.retail|currency }}</span>
        <small>{{ 'OctoApi.configuratorDetails.taxInfo'|trans }}</small>
    </div>
{% endif %}
```

#### octo_configurator__buy_btn
Standard Shopware Buy-Form mit hidden fields.

---

## accompanied-by.html.twig (Macro)

```twig
{% macro accompanied_by(units, unit) %}
    {% if unit.restrictions.accompaniedBy|length > 0 %}
        {% for accompaniedUnit in units %}
            {% if accompaniedUnit.id in unit.restrictions.accompaniedBy
                and accompaniedUnit.type != 'OTHER' %}
                <small>
                    {{ 'OctoApi.accompaniedByMessage'|trans({
                        '%count%': unit.restrictions.accompaniedByRatioDenominator|default(1),
                        '%type%': ('OctoApi.accompaniedByType.' ~ accompaniedUnit.type)|trans
                    }) }}
                </small>
            {% endif %}
        {% endfor %}
    {% endif %}
{% endmacro %}
```

Beispiel-Ausgabe: "1 Erwachsener muss 2 Kinder begleiten"

---

## product.html.twig (Line-Item)

**Extends:** `@Storefront/storefront/component/line-item/type/product.html.twig`

### Block: component_line_item_type_product_number

```twig
{% if lineItem.payload.visitingDate %}
    <div class="line-item-product-date">
        {{ lineItem.payload.visitingDate|date('d.m.Y') }}
    </div>

    {# Units anzeigen #}
    {% for unit in lineItem.payload.units %}
        {% if unit.quantity > 0 %}
            {{ ('OctoApi.units.' ~ unit.type)|trans }}: {{ unit.quantity }}
        {% endif %}
    {% endfor %}

    {# Reservierungs-Countdown #}
    {% if lineItem.payload.reservation.utcExpiresAt %}
        <div data-ff-reservation-countdown='{{ {
            expiresAt: lineItem.payload.reservation.utcExpiresAt,
            route: path("frontend.notification.send")
        }|json_encode }}'>
            {# Countdown wird via JS aktualisiert #}
        </div>
    {% endif %}
{% endif %}
```

### Block: component_line_item_type_product_col_quantity

Versteckt das Standard-Quantity-Feld für OCTO-Produkte (Menge wird über Units gesteuert).

---

## order-item.html.twig (Bestellhistorie)

**Extends:** Account Order History Item Template

### Block: page_account_order_item_context_menu_cancel_order

```twig
{# Prüft ob mindestens ein Line-Item stornierbar ist #}
{% set hasCancellableItems = false %}
{% for lineItem in order.lineItems %}
    {% if lineItem.getPayloadValue('cancellable') %}
        {% set hasCancellableItems = true %}
    {% endif %}
{% endfor %}

{# Cancel-Button nur wenn stornierbare Items vorhanden #}
{% if not hasCancellableItems %}
    {# Button disabled oder versteckt #}
{% endif %}
```

---

## Twig-Filter

### json_decode

**Datei:** `src/Twig/TwigFilters.php`

```php
class TwigFilters extends AbstractExtension
{
    public function getFilters(): array
    {
        return [
            new TwigFilter('json_decode', [$this, 'jsonDecode']),
        ];
    }

    public function jsonDecode(string $string): mixed
    {
        return json_decode($string, true);
    }
}
```

Verwendung: `{{ jsonString|json_decode }}`

## Twig-Funktionen

### ff_octo_listing_price(apiProduct)

**Datei:** `src/Twig/TwigFilters.php`

Berechnet den niedrigsten „Ab"-Preis (float, Major-Währungseinheit, z. B. `66.00`) aus dem rohen OCTO-Produkt-Array (`options[].units[].pricingFrom`). Intern: `PriceService::getLowestPriceFrom()` mit CHILD/INFANT-Filter und GBP→EUR-Konvertierung. Liefert `null`, wenn kein From-Preis ableitbar ist.

Verwendung im initialen Server-Rendering der OCTO-PDP (Datei `configurator.html.twig`, Block `buy_widget_configurator_detail__price_inner`), damit beim PDP-Load **kein `0,00 €`** angezeigt wird, bevor der JS-Roundtrip zu `availability/check` läuft.

```twig
{% set octoFromPrice = apiProduct ? ff_octo_listing_price(apiProduct.product) : null %}
{% set listingPriceFrom = octoFromPrice is not null %}
{% set price = { retail: octoFromPrice|default(product.calculatedPrice.unitPrice|default(0)) } %}
```

**Zwei Render-Kontexte:** Der Block `buy_widget_configurator_detail__price_inner` wird auch von `AvailbilityController::renderBlockView` aufgerufen — dort übergibt der Controller `listingPriceFrom` und `price` direkt. Der Template-Code prüft daher mit `{% if listingPriceFrom is not defined and price is not defined %}`, ob der Controller-Mode aktiv ist, und überschreibt die Werte nicht.

---

## Translation-Keys

### Storefront (OctoApi.*)

```
OctoApi.configuratorDetails.header
OctoApi.configuratorDetails.dateLabel
OctoApi.configuratorDetails.from
OctoApi.configuratorDetails.taxInfo
OctoApi.units.ADULT / YOUTH / CHILD / INFANT / FAMILY / SENIOR / STUDENT / OTHER
OctoApi.unit.subtitle          (%minAge% - %maxAge% Jahre)
OctoApi.unit.shortSubtitle     (ab %minAge% Jahre)
OctoApi.accompaniedByType.ADULT / YOUTH / CHILD / ...
OctoApi.accompaniedByMessage   (%count% %type% muss begleiten)
OctoApi.loadingHint
OctoApi.booking.reservation.expiresIn
OctoApi.booking.cancellation.offlineProduct
OctoApi.availability.state.AVAILABLE / LIMITED / SOLD_OUT / FREESALE / CLOSED
OctoApi.availability.empty
OctoApi.offcanvas.lineItem.deleted
```

### Admin (sw-product.*)

```
sw-product.apiProductForm.title
sw-product.apiProductForm.supplierLabel
sw-product.apiProductForm.productSelectLabel
sw-product.apiProductForm.applyButton
sw-product.apiProductForm.success
sw-product.apiProductForm.error
sw-product.apiProductForm.supplier.gocity / goldentours / demo
```
