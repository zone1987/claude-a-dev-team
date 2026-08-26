# Using Message and Modal Components

Complete distillation of three pages, retrieved 2026-08-26:

- `https://docs.discord.com/developers/components/overview`
- `https://docs.discord.com/developers/components/using-message-components`
- `https://docs.discord.com/developers/components/using-modal-components`

## Contents

- [Components Overview](#components-overview)
- [Using Message Components](#using-message-components)
  - [Sending a Message with a Component](#sending-a-message-with-a-component)
  - [Sending a Message with Multiple Components](#sending-a-message-with-multiple-components)
  - [Nesting Components with Layout Components](#nesting-components-with-layout-components)
  - [Using Message Components with Interactions](#using-message-components-with-interactions)
- [Using Modal Components](#using-modal-components)
  - [Displaying a Modal](#displaying-a-modal)

---

## Components Overview

Components allow you to add interactive elements to modals and the messages your app sends. They're
accessible, customizable, and easy to use. For an introduction to component types and modals, see the
Components & Modals platform page (`https://docs.discord.com/developers/platform/components`) — call
the Skill tool with "discord-platform".

*(Image: Examples of components UI.)*

To use components, messages must be sent with the `IS_COMPONENTS_V2` flag (`1<<15`). Note that using
this flag disables traditional content and embeds — all content must be sent as components instead.

**Info:** Legacy message component behavior will **not** be deprecated and will continue to be
available to your apps on a message-by-message basis. However, Discord recommends using the new
components for new projects and features. See Legacy Message Component Behavior in
`COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md`.

The overview page links three destinations: Using Message Components (a guide on sending Message
Components with examples), Using Modal Components (a guide on sending Modal Components with examples),
and the Component Reference.

### Get Help & Join the Community

The overview page closes by inviting developers to join the DDevs Discord Server
(`https://discord.gg/discord-developers`) to get help from the community, share best practices, and
discover new ways to enhance apps.

---

## Using Message Components

Message components are a powerful way to add interactivity to your messages. They allow you to create
rich, interactive experiences for your users, making it easier for them to engage with your content.

**Info:** If you are sending components as part of a webhook you'll need to use the
`?with_components=true` query param otherwise they'll be ignored.

### Prerequisites

- You must have a Discord account and be a member of the Discord Developer Portal.
- You must have a Discord application created in the Discord Developer Portal.
- You must have the necessary permissions to send messages in the channel where you want to use
  components.

### Sending a Message with a Component

To send a message with a component, you need to set the `IS_COMPONENTS_V2` flag (`1<<15`) in your
message's `flags` field. This can be done when using Message Create, Execute Webhook, or responding to
an interaction (Create Followup Message).

**Warning:** Setting the `IS_COMPONENTS_V2` message flag cannot be reverted: once the message has been
sent, the flag cannot be removed from the message when editing the message.

This flag indicates that the message contains components and disables traditional content and embeds.

All content must be sent as components instead of using the standard message format.

```json
{
  "flags": 32768,
  "components": [
    {
      "type": 10,
      "content": "This is a message using the Text Display component"
    }
  ]
}
```

### Sending a Message with Multiple Components

To send a message with multiple components, you can include multiple component objects in your message's
`components` field. This field allows you to specify an array of components that will be included in the
message.

```json
{
  "flags": 32768,
  "components": [
    {
      "type": 10,
      "content": "This is a Text Display component."
    },
    {
      "type": 10,
      "content": "This is another Text Display component!"
    }
  ]
}
```

### Nesting Components with Layout Components

You can also nest components within layout components. This gives you more flexibility in displaying
information, images, and interactive components to your users. See the component type table in
`COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md` for a complete list of available layout components.

For example, you can create a message with an Action Row component that contains multiple Button
components.

```json
{
  "flags": 32768,
  "components": [
    {
      "type": 10,
      "content": "This is a message with v2 components"
    },
    {
      "type": 1,
      "components": [
        {
          "type": 2,
          "style": 1,
          "label": "Click Me",
          "custom_id": "click_me_1"
        },
        {
          "type": 2,
          "style": 2,
          "label": "Click Me Too",
          "custom_id": "click_me_2"
        }
      ]
    }
  ]
}
```

### Using Message Components with Interactions

When a user interacts with an interactive message component, your app will receive an interaction event.
This event contains information about the interaction, including the type of interaction and the
component that was interacted with.

See the list of supported component types in `COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md` for a list of
interactive message components and their interaction event payloads (the payloads themselves are in
`COMPONENTS-REFERENCE-INTERACTIVE.md`).

You can use this information to respond to the interaction, update the message, or perform other
actions, such as displaying a modal based on the user's input.

See `RECEIVING-AND-RESPONDING.md` for handling interactions and responding to user input from
interactive components.

---

## Using Modal Components

Modal components are a great way to collect freeform information from your users.

### Prerequisites

- You must have a Discord account and be a member of the Discord Developer Portal.
- You must have a Discord application created in the Discord Developer Portal.

### Displaying a Modal

Displaying a modal can be done in response to an interaction. When displaying a modal you'll use an
interaction response with the `MODAL` interaction callback type (`9`) and modal fields (`custom_id`,
`title`, `components` — see Interaction Callback Data: Modal in `RECEIVING-AND-RESPONDING.md`).

An example of a modal with a String Select and Text Input both wrapped in Labels:

```json
{
  "type": 9,
  "data": {
    "custom_id": "bug_modal",
    "title": "Bug Report",
    "components": [
      {
        "type": 18,
        "label": "What's your favorite bug?",
        "component": {
          "type": 3,
          "custom_id": "bug_string_select",
          "placeholder": "Choose...",
          "options": [
            {
              "label": "Ant",
              "value": "ant",
              "description": "(best option)",
              "emoji": {
                "name": "🐜"
              }
            },
            {
              "label": "Butterfly",
              "value": "butterfly",
              "emoji": {
                "name": "🦋"
              }
            },
            {
              "label": "Caterpillar",
              "value": "caterpillar",
              "emoji": {
                "name": "🐛"
              }
            }
          ]
        }
      },
      {
        "type": 18,
        "label": "Why is it your favorite?",
        "description": "Please provide as much detail as possible!",
        "component": {
          "type": 4,
          "custom_id": "bug_explanation",
          "style": 2,
          "min_length": 1000,
          "max_length": 4000,
          "placeholder": "Write your explanation here...",
          "required": true
        }
      }
    ]
  }
}
```

*(Image: Example of the rendered modal.)*

The modal page states nothing beyond this: no submit-handling walkthrough, no limits of its own. The
modal `custom_id`, `title` and `components` limits are on the interaction response object
(`RECEIVING-AND-RESPONDING.md`); the per-component limits are in the two component reference files.

---

## Source

Discord Developer Documentation, retrieved 2026-08-26:

- `https://docs.discord.com/developers/components/overview`
- `https://docs.discord.com/developers/components/using-message-components`
- `https://docs.discord.com/developers/components/using-modal-components`
