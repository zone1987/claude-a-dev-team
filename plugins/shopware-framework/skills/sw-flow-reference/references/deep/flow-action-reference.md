# Shopware 6 — App Flow-Action XML-Referenz

> Quelle: `resources/references/app-reference/flow-action-reference.md`

---

## XML-Struktur: flow-action.xml

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

## `<meta>`-Elemente

| Element | Pflicht | Beschreibung |
|:--------|:--------|:-------------|
| `<name>` | ja | Eindeutiger technischer Name der Action |
| `<label>` | ja | Bezeichnung (wiederholbar mit `lang="de-DE"`) |
| `<headline>` | nein | Überschrift (übersetzbar) |
| `<description>` | nein | Beschreibung (übersetzbar) |
| `<url>` | ja | Ziel-URL, wird per POST aufgerufen |
| `<sw-icon>` | nein | Shopware-Icon-Name |
| `<icon>` | nein | Eigene Icon-Datei (im Resources-Verzeichnis) |
| `<requirements>` | nein | Aware-Interface-Anforderungen (z.B. `orderAware`, `customerAware`) — wiederholbar |

---

## `<config>`-Eingabefelder

### input-field type Werte

| Type | Beschreibung |
|:-----|:-------------|
| `text` | Einzeiliger Text |
| `textarea` | Mehrzeiliger Text |
| `int` | Ganzzahl |
| `float` | Dezimalzahl |
| `bool` | Checkbox |
| `date` | Datum |
| `datetime` | Datum + Zeit |
| `colorpicker` | Farbauswahl |
| `password` | Passwort-Feld |
| `single-select` | Einzelauswahl |
| `multi-select` | Mehrfachauswahl |

### Sub-Elemente je input-field

| Element | Pflicht | Beschreibung |
|:--------|:--------|:-------------|
| `<name>` | ja | Feldname (technisch) |
| `<label>` | ja | Bezeichnung (übersetzbar) |
| `<place-holder>` | nein | Platzhalter (übersetzbar) |
| `<required>` | nein | `true`/`false` |
| `<defaultValue>` | nein | Standardwert |
| `<helpText>` | nein | Hilfetext (übersetzbar) |

---

## Verfügbare Variablen je Trigger-Event

| Event(s) | Verfügbare Variablen |
|:---------|:---------------------|
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

## `<requirements>` — Aware-Interfaces

| Requirement | Beschreibung |
|:------------|:-------------|
| `orderAware` | Gibt Zugriff auf `order`-Objekt |
| `customerAware` | Gibt Zugriff auf `customer`-Objekt |
| `mailAware` | Gibt Zugriff auf Mail-Daten |
| `salesChannelAware` | Gibt Zugriff auf Sales-Channel-Kontext |
| `userAware` | Gibt Zugriff auf Admin-User |

---

## Beispiel: Telegram-Flow-Action

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
