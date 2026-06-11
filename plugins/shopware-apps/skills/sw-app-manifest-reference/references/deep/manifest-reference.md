# Shopware 6 — App manifest.xml Referenz

> Quelle: `resources/references/app-reference/manifest-reference.md`

---

## Meta (Pflicht)

Metadaten über die App. Im `<meta>`-Element angeben.

```xml
<meta>
    <name>MyApp</name>
    <label>My App</label>
    <label lang="de-DE">Meine App</label>
    <description>App description</description>
    <description lang="de-DE">App-Beschreibung</description>
    <author>Company GmbH</author>
    <copyright>(c) by Company GmbH</copyright>
    <version>1.0.0</version>
    <license>MIT</license>
    <icon>Resources/config/plugin.png</icon>
</meta>
```

---

## Setup (Optional)

Wird benötigt, wenn Kommunikation zwischen Shopware und der App nötig ist.

```xml
<setup>
    <registrationUrl>https://app.example.com/registration</registrationUrl>
    <secret>your-app-secret</secret>
</setup>
```

---

## Requirements (seit 6.7.10.0, optional)

Anforderungen, die erfüllt sein müssen, damit die App funktioniert.

```xml
<requirements>
    <requirement>public-access</requirement>
</requirements>
```

### Verfügbare Requirements

| Requirement | Beschreibung | Seit |
|:------------|:-------------|:-----|
| `public-access` | Shopware-Instanz muss öffentlich erreichbar sein (HTTPS, kein localhost, DNS-Auflösung, Health-Check gibt HTTP 200 zurück) | 6.7.10.0 |

---

## Storefront (Optional)

Kann weggelassen werden wenn die App-Template-Priorität höher als andere Plugins/Apps sein soll.

```xml
<storefront>
    <template-load-priority>100</template-load-priority>
</storefront>
```

---

## Permissions (Optional)

Berechtigungen für Entity-Zugriff.

**Granulare Permissions:**
```xml
<permissions>
    <read>product</read>
    <create>product</create>
    <update>product</update>
    <delete>product</delete>
</permissions>
```

**CRUD-Shortcut (seit 6.7.3.0):**
```xml
<permissions>
    <crud>product</crud>
    <!-- äquivalent zu read+create+update+delete für product -->
</permissions>
```

---

## Allowed Hosts (seit 6.4.12.0, optional)

Alle externen Endpunkte, mit denen die App kommuniziert.

```xml
<allowed-hosts>
    <host>api.example.com</host>
</allowed-hosts>
```

---

## Webhooks (Optional)

```xml
<webhooks>
    <webhook name="order-placed"
             url="https://app.example.com/hook/order"
             event="checkout.order.placed"/>
    <webhook name="product-updated"
             url="https://app.example.com/hook/product"
             event="product.written"/>
</webhooks>
```

Alle verfügbaren Events: siehe `references/deep/webhook-events-reference.md` (sw-events-reference).

---

## Admin Extension (Optional)

Nur nötig wenn die Administration erweitert werden soll.

```xml
<admin>
    <action-button action="doSomething"
                   entity="order"
                   view="detail"
                   url="https://app.example.com/action">
        <label>Do something</label>
    </action-button>
    <module name="myModule"
            source="https://app.example.com/admin-module"
            parent="sw-catalogue">
        <label>My Module</label>
        <label lang="de-DE">Mein Modul</label>
    </module>
</admin>
```

---

## Custom Fields (Optional)

```xml
<custom-fields>
    <custom-field-set>
        <name>custom_field_test</name>
        <label>Custom field test</label>
        <label lang="de-DE">Meine Zusatzfelder</label>
        <related-entities>
            <order/>
        </related-entities>
        <fields>
            <text name="myTextField">
                <label>My text field</label>
            </text>
        </fields>
    </custom-field-set>
</custom-fields>
```

---

## Cookies (Optional)

**Einzelnes Cookie:**
```xml
<cookies>
    <cookie>
        <cookie>my-cookie</cookie>
        <snippet-name>myApp.cookies.myCookie</snippet-name>
        <cookie-provider>My App</cookie-provider>
        <path>/</path>
        <value>1</value>
        <expiration>30</expiration>
    </cookie>
</cookies>
```

**Cookie-Gruppe:**
```xml
<cookies>
    <group>
        <snippet-name>myApp.cookies.cookieGroup</snippet-name>
        <entries>
            <cookie>
                <cookie>my-group-cookie</cookie>
                <snippet-name>myApp.cookies.groupCookie</snippet-name>
            </cookie>
        </entries>
    </group>
</cookies>
```

---

## Payments (Optional)

```xml
<payments>
    <payment-method>
        <identifier>myPaymentMethod</identifier>
        <name>My Payment Method</name>
        <name lang="de-DE">Meine Zahlungsmethode</name>
        <description>My payment method description</description>
        <pay-url>https://payment.app/pay</pay-url>
        <finalize-url>https://payment.app/finalize</finalize-url>
        <icon>Resources/config/payment.png</icon>
    </payment-method>
</payments>
```

---

## Shipping Methods (Optional)

```xml
<shipping-methods>
    <shipping-method>
        <identifier>myShippingMethod</identifier>
        <name>My Shipping Method</name>
        <name lang="de-DE">Meine Versandmethode</name>
        <description>My shipping method description</description>
        <delivery-time>
            <name>1-2 days</name>
            <min>1</min>
            <max>2</max>
            <unit>day</unit>
        </delivery-time>
        <icon>Resources/config/shipping.png</icon>
    </shipping-method>
</shipping-methods>
```

---

## Rule Conditions (Optional)

Der Identifier muss eindeutig und unveränderlich sein.

```xml
<rule-conditions>
    <rule-condition>
        <identifier>myCustomCondition</identifier>
        <name>My Custom Condition</name>
        <group>my-app</group>
        <script>Resources/scripts/rule-conditions/my-custom-condition.twig</script>
    </rule-condition>
</rule-conditions>
```

---

## Tax (Optional)

```xml
<tax>
    <tax-provider>
        <identifier>myTaxProvider</identifier>
        <name>My Tax Provider</name>
        <name lang="de-DE">Mein Steueranbieter</name>
        <priority>1</priority>
        <process-url>https://tax.app/process</process-url>
    </tax-provider>
</tax>
```
