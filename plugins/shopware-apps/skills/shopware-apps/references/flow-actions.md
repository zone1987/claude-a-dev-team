---
title: Flow Actions
impact: LOW-MEDIUM
impactDescription: Custom flow actions extend the Flow Builder with webhook-based actions
tags: flow, actions, flow-builder, webhook, flow-xml
---

## Flow Actions

Custom flow actions extend the Flow Builder with webhook-based actions. Available since Shopware 6.4.10.0. Defined in `Resources/flow.xml`.

### flow.xml Example

```xml
<flow-extensions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/shopware/shopware/trunk/src/Core/Framework/App/Flow/Schema/flow-1.0.xsd">
    <flow-actions>
        <flow-action>
            <meta>
                <name>slack.send.message</name>
                <label>Send Slack message</label>
                <label lang="de-DE">Slack-Nachricht senden</label>
                <description>Sends a notification to Slack</description>
                <url>https://hooks.slack.com/services/{id}</url>
                <sw-icon>default-communication-speech-bubbles</sw-icon>
                <icon>Resources/slack.png</icon>
                <requirements>orderAware</requirements>
                <delayable>true</delayable>
            </meta>
            <headers>
                <parameter type="string" name="content-type" value="application/json"/>
            </headers>
            <parameters>
                <parameter type="string" name="text" value="{{ subject }}: {{ message }}"/>
            </parameters>
            <config>
                <input-field type="text">
                    <name>subject</name>
                    <label>Subject</label>
                    <required>true</required>
                </input-field>
                <input-field type="textarea">
                    <name>message</name>
                    <label>Message</label>
                    <place-holder>Enter your message...</place-holder>
                </input-field>
            </config>
        </flow-action>
    </flow-actions>
</flow-extensions>
```

### Meta Elements

| Element | Required | Description |
|---------|----------|-------------|
| `name` | Yes | Unique identifier (pattern: `[a-z][a-z.]*[a-z]`) |
| `label` | Yes | Display name (translatable) |
| `url` | Yes | Webhook endpoint |
| `requirements` | Yes | Awareness types (determines when action is available) |
| `sw-icon` | No | Shopware icon name |
| `icon` | No | Custom icon path |
| `headline` | No | Heading in config dialog |
| `description` | No | Description text |
| `delayable` | No | Whether the action can be delayed |

### Requirements (Awareness)

`orderAware`, `customerAware`, `mailAware`, `salesChannelAware`, `userAware`, `customerGroupAware`, `delayAware`

### Template Variables in Parameters

Parameters support Twig-like variable interpolation:
- Config values: `{{ subject }}`, `{{ message }}`
- Event data: `{{ order.orderNumber }}`, `{{ customer.email }}`

### Config Field Types

`text`, `textarea`, `text-editor`, `url`, `password`, `int`, `float`, `bool`, `checkbox`, `datetime`, `date`, `time`, `colorpicker`, `single-select`, `multi-select`
