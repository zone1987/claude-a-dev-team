# Shopware 6 — App flow action XML reference

> Source: `resources/references/app-reference/flow-action-reference.md`

---

## Contents

- [XML structure: flow-action.xml](#xml-structure-flow-actionxml)
- [`<meta>` elements](#meta-elements)
- [`<config>` input fields](#config-input-fields)
- [Available variables per trigger event](#available-variables-per-trigger-event)
- [`<requirements>` — aware interfaces](#requirements--aware-interfaces)
- [Example: Telegram flow action](#example-telegram-flow-action)

## XML structure: flow-action.xml

```xml
// Resources/flow-action.xml
<flow-actions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Flow/Schema/flow-1.0.xsd">
    <flow-action>
        <meta>
            <name>slack</name>
            <label>Send slack message</label>
            <label lang="de-DE">Slack-Nachricht senden</label>
            <headline>Headline for send slack message</headline>
            <headline lang="de-DE">Überschrift für das Senden einer Slack-Nachricht</headline>
            <description>Slack send message description</description>
            <description lang="de-DE">Beschreibung der Slack-Sendenachricht</description>
            <url>https://hooks.slack.com/services/{id}</url>
            <sw-icon>default-communication-speech-bubbles</sw-icon>
            <icon>slack.png</icon>
            <requirements>orderAware</requirements>
            <requirements>customerAware</requirements>
        </meta>
        <headers>
            <parameter type="string" name="content-type" value="application/json"/>
        </headers>
        <parameters>
            <parameter type="string" name="text" value="{{ subject }} \n {{ message }} \n Order Number: {{ order.orderNumber }}"/>
        </parameters>
        <config>
            <input-field type="text">
                <name>subject</name>
                <label>Subject</label>
                <label lang="de-DE">Gegenstand</label>
                <place-holder>Placeholder</place-holder>
                <place-holder lang="de-DE">Platzhalter</place-holder>
                <required>true</required>
                <helpText>Help Text</helpText>
                <helpText lang="de-DE">Hilfstext</helpText>
            </input-field>
            <input-field type="textarea">
                <name>message</name>
                <label>Message</label>
                <label lang="de-DE">Nachricht</label>
                <place-holder>Placeholder</place-holder>
                <required>true</required>
                <helpText>Help Text</helpText>
            </input-field>
        </config>
    </flow-action>
</flow-actions>
```

---

## `<meta>` elements

| Element | Required | Description |
|:--------|:---------|:------------|
| `<name>` | yes | Unique technical name of the action |
| `<label>` | yes | Label (repeatable with `lang="de-DE"`) |
| `<headline>` | no | Headline (translatable) |
| `<description>` | no | Description (translatable) |
| `<url>` | yes | Target URL, called via POST |
| `<sw-icon>` | no | Shopware icon name |
| `<icon>` | no | Custom icon file (in the Resources directory) |
| `<requirements>` | no | Aware interface requirements (e.g. `orderAware`, `customerAware`) — repeatable |

---

## `<config>` input fields

### input-field type values

| Type | Description |
|:-----|:-------------|
| `text` | Single-line text |
| `textarea` | Multi-line text |
| `int` | Integer |
| `float` | Decimal number |
| `bool` | Checkbox |
| `date` | Date |
| `datetime` | Date + time |
| `colorpicker` | Color picker |
| `password` | Password field |
| `single-select` | Single selection |
| `multi-select` | Multiple selection |

### Sub-elements per input-field

| Element | Required | Description |
|:--------|:---------|:------------|
| `<name>` | yes | Field name (technical) |
| `<label>` | yes | Label (translatable) |
| `<place-holder>` | no | Placeholder (translatable) |
| `<required>` | no | `true`/`false` |
| `<defaultValue>` | no | Default value |
| `<helpText>` | no | Help text (translatable) |

---

## Available variables per trigger event

| Event(s) | Available variables |
|:---------|:--------------------|
| `checkout.order.placed` `state_enter.order.state.*` `state_enter.order_transaction.state.*` `state_enter.order_delivery.state.*` | `order` |
| `customer.group.registration.declined` `customer.group.registration.accepted` | `customer`, `customerGroup` |
| `user.recovery.request` | `userRecovery` |
| `checkout.customer.double_opt_in_registration` `checkout.customer.double_opt_in_guest_order` | `customer`, `confirmUrl` |
| `customer.recovery.request` | `customerRecovery`, `customer`, `resetUrl`, `shopName` |
| `contact_form.send` | `contactFormData` |
| `checkout.customer.register` | `customer` |
| `newsletter.register` | `newsletterRecipient`, `url` |
| `newsletter.confirm` | `newsletterRecipient` |

---

## `<requirements>` — aware interfaces

| Requirement | Description |
|:------------|:-------------|
| `orderAware` | Grants access to the `order` object |
| `customerAware` | Grants access to the `customer` object |
| `mailAware` | Grants access to mail data |
| `salesChannelAware` | Grants access to the sales channel context |
| `userAware` | Grants access to the admin user |

---

## Example: Telegram flow action

```xml
<flow-action>
    <meta>
        <name>telegram</name>
        <label>Send telegram message</label>
        <label lang="de-DE">Telegrammnachricht senden</label>
        <url>https://api.telegram.org/{id}</url>
        <sw-icon>default-communication-speech-bubbles</sw-icon>
        <requirements>orderAware</requirements>
        <requirements>customerAware</requirements>
    </meta>
    <headers>
        <parameter type="string" name="content-type" value="application/json"/>
    </headers>
    <parameters>
        <parameter type="string" name="chat_id" value="{{ chatId }}"/>
        <parameter type="string" name="text" value="{{ content }}"/>
    </parameters>
    <config>
        <input-field type="text">
            <name>chatId</name>
            <label>Chat Room</label>
            <required>true</required>
            <defaultValue>Hello</defaultValue>
            <helpText>Chat Room ID via Telegram API</helpText>
        </input-field>
        <input-field type="textarea">
            <name>content</name>
            <label>Content</label>
        </input-field>
    </config>
</flow-action>
```
