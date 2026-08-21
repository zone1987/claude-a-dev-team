# Shopware 6 — App manifest.xml reference

> Source: `resources/references/app-reference/manifest-reference.md`

---

## Contents

- [Meta (required)](#meta-required)
- [Setup (Optional)](#setup-optional)
- [Requirements (since 6.7.10.0, optional)](#requirements-since-67100-optional)
- [Storefront (Optional)](#storefront-optional)
- [Permissions (Optional)](#permissions-optional)
- [Allowed Hosts (since 6.4.12.0, optional)](#allowed-hosts-since-64120-optional)
- [Webhooks (Optional)](#webhooks-optional)
- [Admin Extension (Optional)](#admin-extension-optional)
- [Custom Fields (Optional)](#custom-fields-optional)
- [Cookies (Optional)](#cookies-optional)
- [Payments (Optional)](#payments-optional)
- [Shipping Methods (Optional)](#shipping-methods-optional)
- [Rule Conditions (Optional)](#rule-conditions-optional)
- [Tax (Optional)](#tax-optional)

## Meta (required)

Metadata about the app. Specify inside the `<meta>` element.

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

Required when communication between Shopware and the app is needed.

```xml
<setup>
    <registrationUrl>https://app.example.com/registration</registrationUrl>
    <secret>your-app-secret</secret>
</setup>
```

---

## Requirements (since 6.7.10.0, optional)

Requirements that must be met for the app to work.

```xml
<requirements>
    <requirement>public-access</requirement>
</requirements>
```

### Available requirements

| Requirement | Description | Since |
|:------------|:-------------|:-----|
| `public-access` | Shopware instance must be publicly reachable (HTTPS, no localhost, DNS resolution, health check returns HTTP 200) | 6.7.10.0 |

---

## Storefront (Optional)

Can be omitted unless the app template priority should be higher than other plugins/apps.

```xml
<storefront>
    <template-load-priority>100</template-load-priority>
</storefront>
```

---

## Permissions (Optional)

Permissions for entity access.

**Granular permissions:**
```xml
<permissions>
    <read>product</read>
    <create>product</create>
    <update>product</update>
    <delete>product</delete>
</permissions>
```

**CRUD shortcut (since 6.7.3.0):**
```xml
<permissions>
    <crud>product</crud>
    <!-- equivalent to read+create+update+delete for product -->
</permissions>
```

---

## Allowed Hosts (since 6.4.12.0, optional)

All external endpoints the app communicates with.

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

All available events: see `references/deep/webhook-events-reference.md` (sw-events-reference).

---

## Admin Extension (Optional)

Only needed when the Administration should be extended.

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

**Single cookie:**
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

**Cookie group:**
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

The identifier must be unique and immutable.

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
