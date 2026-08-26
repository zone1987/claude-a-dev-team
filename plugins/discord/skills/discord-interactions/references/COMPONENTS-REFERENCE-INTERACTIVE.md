# Component Reference — Interactive Components

The interactive half of `https://docs.discord.com/developers/components/reference`, retrieved
2026-08-26: Button (2), String Select (3), Text Input (4), User Select (5), Role Select (6), Mentionable
Select (7), Channel Select (8), File Upload (19), Radio Group (21), Checkbox Group (22), Checkbox (23).

Layout and content components (Action Row 1, Section 9, Text Display 10, Thumbnail 11, Media Gallery
12, File 13, Separator 14, Container 17, Label 18), the complete component type table, the shared
component anatomy, the Unfurled Media Item and Legacy behavior are in
`COMPONENTS-REFERENCE-LAYOUT-AND-CONTENT.md`.

Every interactive component carries `type` and optional `id` (see Anatomy of a Component in the layout
file) plus a `custom_id`.

## Contents

- [Button (type 2)](#button-type-2)
- [String Select (type 3)](#string-select-type-3)
- [Text Input (type 4)](#text-input-type-4)
- [User Select (type 5)](#user-select-type-5)
- [Role Select (type 6)](#role-select-type-6)
- [Mentionable Select (type 7)](#mentionable-select-type-7)
- [Channel Select (type 8)](#channel-select-type-8)
- [File Upload (type 19)](#file-upload-type-19)
- [Radio Group (type 21)](#radio-group-type-21)
- [Checkbox Group (type 22)](#checkbox-group-type-22)
- [Checkbox (type 23)](#checkbox-type-23)

---

## Button (type 2)

A Button is an interactive component that can only be used in messages. It creates clickable elements
that users can interact with, sending an interaction to your app when clicked.

Buttons must be placed inside an Action Row or a Section's `accessory` field.

### Button Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `2` for a button |
| id? | integer | Optional identifier for component |
| style | integer | A button style |
| label? | string | Text that appears on the button; max 80 characters |
| emoji? | partial emoji | `name`, `id`, and `animated` |
| custom\_id? | string | Developer-defined identifier for the button; 1-100 characters |
| sku\_id? | snowflake | Identifier for a purchasable SKU, only available when using premium-style buttons |
| url? | string | URL for link-style buttons; max 512 characters |
| disabled? | boolean | Whether the button is disabled (defaults to `false`) |

Buttons come in various styles to convey different types of actions. These styles also define what
fields are valid for a button.

- Non-link and non-premium buttons **must** have a `custom_id`, and cannot have a `url` or a `sku_id`.
- Link buttons **must** have a `url`, and cannot have a `custom_id`
- Link buttons do not send an interaction to your app when clicked
- Premium buttons **must** contain a `sku_id`, and cannot have a `custom_id`, `label`, `url`, or
  `emoji`.
- Premium buttons do not send an interaction to your app when clicked

### Button Styles

| Name | Value | Action | Required Field |
| --- | --- | --- | --- |
| Primary | 1 | The most important or recommended action in a group of options | `custom_id` |
| Secondary | 2 | Alternative or supporting actions | `custom_id` |
| Success | 3 | Positive confirmation or completion actions | `custom_id` |
| Danger | 4 | An action with irreversible consequences | `custom_id` |
| Link | 5 | Navigates to a URL | `url` |
| Premium | 6 | Purchase | `sku_id` |

### Examples

**Message Example** — Message create payload with a Button component:

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 1,  // ComponentType.ACTION_ROW
      "components": [
          {
            "type": 2,  // ComponentType.BUTTON,
            "custom_id": "click_me",
            "label": "Click me!",
            "style": 1
          }
      ]
    }
  ]
}
```

**Message Interaction Response Example** — when a user interacts with a Button in a message, this is
the basic form of the interaction data payload you will receive. The full payload is available in the
interaction reference (`RECEIVING-AND-RESPONDING.md`).

```jsonc
{
  "type": 3, // InteractionType.MESSAGE_COMPONENT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "component_type": 2, // ComponentType.BUTTON
    "id": 2,
    "custom_id": "click_me",
  },
}
```

The upstream defines no separate "Button Interaction Response Structure" table.

### Button Design Guidelines

#### General Button Content

- 34 characters max with icon or emoji.
- 38 characters max without icon or emoji.
- Keep text concise and to the point.
- Use clear and easily understandable language. Avoid jargon or overly technical terms.
- Use verbs that indicate the outcome of the action.
- Maintain consistency in language and tone across buttons.
- Anticipate the need for translation and test for expansion or contraction in different languages.

#### Multiple Buttons

Use different button styles to create a hierarchy. Use only one `Primary` button per group.

*(Image: Example showing one primary button per button group.)*

If there are multiple buttons of equal significance, use the `Secondary` button style for all buttons.

*(Image: Example showing multiple buttons in a group with equal significance.)*

#### Premium Buttons

Premium buttons will automatically have the following:

- Shop Icon
- SKU name
- SKU price

*(Image: A premium button.)*

---

## String Select (type 3)

A String Select is an interactive component that allows users to select one or more provided `options`.

String Selects can be configured for both single-select and multi-select behavior. When a user finishes
making their choice(s) your app receives an interaction.

String Selects are available in messages and modals. They must be placed inside an Action Row in
messages and a Label in modals.

### String Select Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `3` for string select |
| id? | integer | Optional identifier for component |
| custom\_id | string | ID for the select menu; 1-100 characters |
| options | array of select options | Specified choices in a select menu; max 25 |
| placeholder? | string | Placeholder text if nothing is selected or default; max 150 characters |
| min\_values? \* | integer | Minimum number of items that must be chosen (defaults to 1); min 0 (see note), max 25 |
| max\_values? | integer | Maximum number of items that can be chosen (defaults to 1); max 25 |
| required? \*\* | boolean | Whether the string select is required to answer in a modal (defaults to `true`) |
| disabled? \*\*\* | boolean | Whether select menu is disabled in a message (defaults to `false`) |

\* `min_values` must be either omitted or at least `1` if `required` is omitted or `true`.

\*\* The `required` field is only available for String Selects in modals. It is ignored in messages.

\*\*\* Using `disabled` in a modal will result in an error. Modals can not currently have disabled
components in them.

### Select Option Structure

| Field | Type | Description |
| --- | --- | --- |
| label | string | User-facing name of the option; max 100 characters |
| value | string | Dev-defined value of the option; max 100 characters |
| description? | string | Additional description of the option; max 100 characters |
| emoji? | partial emoji object | `id`, `name`, and `animated` |
| default? | boolean | Will show this option as selected by default |

### String Select Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type \* | integer | `3` for a String Select |
| component\_type \* | integer | `3` for a String Select |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| values | array of strings | The text of the selected options |

\* In message interaction responses `component_type` will be returned and in modal interaction
responses `type` will be returned.

### Examples

**Message Example** — Message create payload with a String Select component:

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 1, // ComponentType.ACTION_ROW,
      "id": 1,
      "components": [
        {
          "type": 3, // ComponentType.STRING_SELECT
          "id": 2,
          "custom_id": "favorite_bug",
          "placeholder": "Favorite bug?",
          "options": [
            {
              "label": "Ant",
              "value": "ant",
              "description": "(best option)",
              "emoji": {"name": "🐜"}
            },
            {
              "label": "Butterfly",
              "value": "butterfly",
              "emoji": {"name": "🦋"}
            },
            {
              "label": "Caterpillar",
              "value": "caterpillar",
              "emoji": {"name": "🐛"}
            }
          ]
        }
      ]
    }
  ]
}
```

**Message Interaction Data Example:**

```jsonc
{
  "type": 3, // InteractionType.MESSAGE_COMPONENT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "component_type": 3, // ComponentType.STRING_SELECT
    "custom_id": "favorite_bug",
    "values": [
      "butterfly",
    ]
  },
}
```

**Modal Example** — Modal create payload with a String Select component:

```jsonc
{
  "type": 9, // InteractionCallbackType.MODAL
  "data": {
    "custom_id": "bug_modal",
    "title": "Bug Survey",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "id": 1,
        "label": "Favorite bug?",
        "component": {
          "type": 3, // ComponentType.STRING_SELECT
          "id": 2,
          "custom_id": "favorite_bug",
          "placeholder": "Ants are the best",
          "options": [
            {
              "label": "Ant",
              "value": "ant",
              "description": "(best option)",
              "emoji": {"name": "🐜"}
            },
            {
              "label": "Butterfly",
              "value": "butterfly",
              "emoji": {"name": "🦋"}
            },
            {
              "label": "Caterpillar",
              "value": "caterpillar",
              "emoji": {"name": "🐛"}
            }
          ]
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "bug_modal",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "id": 1,
        "component": {
          "type": 3, // ComponentType.STRING_SELECT
          "id": 2,
          "custom_id": "favorite_bug",
          "values": [
            "butterfly",
          ]
        }
      }
    ]
  },
}
```

---

## Text Input (type 4)

Text Input is an interactive component that allows users to enter free-form text responses in modals. It
supports both short, single-line inputs and longer, multi-line paragraph inputs.

Text Inputs can only be used within modals and must be placed inside a Label.

**Info:** Discord no longer recommends using Text Input within an Action Row in modals. Going forward
all Text Inputs should be placed inside a Label component.

### Text Input Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `4` for a text input |
| id? | integer | Optional identifier for component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| style | integer | The Text Input Style |
| min\_length? | integer | Minimum input length for a text input; min 0, max 4000 |
| max\_length? | integer | Maximum input length for a text input; min 1, max 4000 |
| required? | boolean | Whether this component is required to be filled (defaults to `true`) |
| value? | string | Pre-filled value for this component; max 4000 characters |
| placeholder? | string | Custom placeholder text if the input is empty; max 100 characters |

**Info:** The `label` field on a Text Input is deprecated in favor of `label` and `description` on the
Label component.

### Text Input Styles

| Name | Value | Description |
| --- | --- | --- |
| Short | 1 | Single-line input |
| Paragraph | 2 | Multi-line input |

### Text Input Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `4` for a Text Input |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| value | string | The user's input text |

### Examples

**Modal Example** — Modal create payload with a Text Input component:

```jsonc
{
  "type": 9, // InteractionCallbackType.MODAL
  "data": {
    "custom_id": "game_feedback_modal",
    "title": "Game Feedback",
    "components": [
      {
        "type": 18,  // ComponentType.LABEL
        "label": "What did you find interesting about the game?",
        "description": "Please give us as much detail as possible so we can improve the game!",
        "component": {
          "type": 4,  // ComponentType.TEXT_INPUT
          "custom_id": "game_feedback",
          "style": 2,
          "min_length": 100,
          "max_length": 4000,
          "placeholder": "Write your feedback here...",
          "required": true
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "game_feedback_modal",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "id": 1,
        "component": {
          "type": 4, // ComponentType.TEXT_INPUT
          "id": 2,
          "custom_id": "game_feedback",
          "value": "The recent changes to acceleration feel much better, but shadows still need help"
        }
      }
    ]
  },
}
```

---

## User Select (type 5)

A User Select is an interactive component that allows users to select one or more users in a message or
modal. Options are automatically populated based on the server's available users.

User Selects can be configured for both single-select and multi-select behavior. When a user finishes
making their choice(s) your app receives an interaction.

User Selects are available in messages and modals. They must be placed inside an Action Row in messages
and a Label in modals.

### User Select Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `5` for user select |
| id? | integer | Optional identifier for component |
| custom\_id | string | ID for the select menu; 1-100 characters |
| placeholder? | string | Placeholder text if nothing is selected; max 150 characters |
| default\_values? | array of default value objects | List of default values for auto-populated select menu components; number of default values must be in the range defined by `min_values` and `max_values` |
| min\_values? \* | integer | Minimum number of items that must be chosen (defaults to 1); min 0 (see note), max 25 |
| max\_values? | integer | Maximum number of items that can be chosen (defaults to 1); max 25 |
| required? \*\* | boolean | Whether the user select is required to answer in a modal (defaults to `true`) |
| disabled? \*\*\* | boolean | Whether select menu is disabled in a message (defaults to `false`) |

\* `min_values` must be either omitted or at least `1` if `required` is omitted or `true`.

\*\* The `required` field is only available for User Selects in modals. It is ignored in messages.

\*\*\* Using `disabled` in a modal will result in an error. Modals can not currently have disabled
components in them.

### Select Default Value Structure

Shared by User Select, Role Select, Mentionable Select and Channel Select.

| Field | Type | Description |
| --- | --- | --- |
| id | snowflake | ID of a user, role, or channel |
| type | string | Type of value that `id` represents. Either `"user"`, `"role"`, or `"channel"` |

### User Select Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type \* | integer | `5` for a User Select |
| component\_type \* | integer | `5` for a User Select |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| resolved | resolved data | Resolved entities from selected options |
| values | array of snowflakes | IDs of the selected users |

\* In message interaction responses `component_type` will be returned and in modal interaction
responses `type` will be returned.

### Examples

**Message Example:**

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 1,  // ComponentType.ACTION_ROW
      "components": [
        {
          "type": 5,  // ComponentType.USER_SELECT
          "custom_id": "user_select",
          "placeholder": "Select a user"
        }
      ]
    }
  ]
}
```

**Message Interaction Data Example.** Info: `members` and `users` may both be present in the `resolved`
object when a user is selected.

```jsonc
{
  "type": 3, // InteractionType.MESSAGE_COMPONENT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "component_type": 5, // ComponentType.USER_SELECT
    "id": 2,
    "custom_id": "user_select",
    "values": [
      "1111111111111111111",
    ],
    "resolved": {
      "members": {
        "1111111111111111111": {
          "avatar": null,
          "banner": null,
          "collectibles": null,
          "communication_disabled_until": null,
          "flags": 0,
          "joined_at": "2025-05-16T22:51:16.692000+00:00",
          "nick": null,
          "pending": false,
          "permissions": "2248473465835073",
          "premium_since": null,
          "roles": [
            "2222222222222222222"
          ],
          "unusual_dm_activity_until": null
        }
      },
      "users": {
        "1111111111111111111": {
          "avatar": "d54e87d20539fe9aad2f2cebe56809a2",
          "avatar_decoration_data": null,
          "bot": true,
          "clan": null,
          "collectibles": null,
          "discriminator": "9062",
          "display_name_styles": null,
          "global_name": null,
          "id": "1111111111111111111",
          "primary_guild": null,
          "public_flags": 524289,
          "username": "ExampleBot"
        }
      }
    }
  },
}
```

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "user_modal",
    "title": "User Chooser",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "label": "Choose your users",
        "component": {
          "type": 5, // ComponentType.USER_SELECT
          "custom_id": "user_selected",
          "max_values": 5,
          "required": true
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "user_modal",
    "components": [
      {
        "component": {
          "custom_id": "user_selected",
          "id": 2,
          "type": 5,
          "values": [
            "11111111111111111"
          ]
        },
        "id": 1,
        "type": 18
      }
    ],
    "resolved": {
      "members": {
        "11111111111111111": {
          "avatar": null,
          "banner": null,
          "collectibles": null,
          "communication_disabled_until": null,
          "flags": 0,
          "joined_at": "2025-04-02T23:07:21.476000+00:00",
          "nick": "Ant",
          "pending": false,
          "permissions": "4503599627370495",
          "premium_since": null,
          "roles": [
            "1357409927680889032"
          ],
          "unusual_dm_activity_until": null
        }
      },
      "users": {
        "11111111111111111": {
          "avatar": "a_b15bd8ee42e3c3d9a7de129fee60bc84",
          "avatar_decoration_data": null,
          "clan": null,
          "collectibles": {
            "nameplate": {
              "asset": "nameplates/spell/white_mana/",
              "expires_at": null,
              "label": "COLLECTIBLES_SPELL_WHITE_MANA_NP_A11Y",
              "palette": "bubble_gum",
              "sku_id": "1379220459203072050"
            }
          },
          "discriminator": "0",
          "display_name_styles": {
            "colors": [
              16777215
            ],
            "effect_id": 4,
            "font_id": 3
          },
          "global_name": "Anthony",
          "id": "11111111111111111",
          "primary_guild": null,
          "public_flags": 65,
          "username": "actuallyanthony"
        }
      }
    }
  }
}
```

---

## Role Select (type 6)

A Role Select is an interactive component that allows users to select one or more roles in a message or
modal. Options are automatically populated based on the server's available roles.

Role Selects can be configured for both single-select and multi-select behavior. When a user finishes
making their choice(s) your app receives an interaction.

Role Selects are available in messages and modals. They must be placed inside an Action Row in messages
and a Label in modals.

### Role Select Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `6` for role select |
| id? | integer | Optional identifier for component |
| custom\_id | string | ID for the select menu; 1-100 characters |
| placeholder? | string | Placeholder text if nothing is selected; max 150 characters |
| default\_values? | array of default value objects | List of default values for auto-populated select menu components; number of default values must be in the range defined by `min_values` and `max_values` |
| min\_values? \* | integer | Minimum number of items that must be chosen (defaults to 1); min 0 (see note), max 25 |
| max\_values? | integer | Maximum number of items that can be chosen (defaults to 1); max 25 |
| required? \*\* | boolean | Whether the role select is required to answer in a modal (defaults to `true`) |
| disabled? \*\*\* | boolean | Whether select menu is disabled in a message (defaults to `false`) |

\* `min_values` must be either omitted or at least `1` if `required` is omitted or `true`.

\*\* The `required` field is only available for Role Selects in modals. It is ignored in messages.

\*\*\* Using `disabled` in a modal will result in an error. Modals can not currently have disabled
components in them.

### Role Select Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type \* | integer | `6` for a Role Select |
| component\_type \* | integer | `6` for a Role Select |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| resolved | resolved data | Resolved entities from selected options |
| values | array of snowflakes | IDs of the selected roles |

\* In message interaction responses `component_type` will be returned and in modal interaction
responses `type` will be returned.

### Examples

**Message Example.** The upstream image caption reads "Example of a Role Select allowing up to 3 choices" — that `3` is this example's own `max_values`, not a documented Role Select limit; the documented ceiling is `max_values` max 25.

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 1,  // ComponentType.ACTION_ROW
      "components": [
        {
          "type": 6,  // ComponentType.ROLE_SELECT
          "custom_id": "role_ids",
          "placeholder": "Which roles?",
          "min_values": 1,
          "max_values": 3
        }
      ]
    }
  ]
}
```

**Message Interaction Data Example:**

```jsonc
{
  "type": 3, // InteractionType.MESSAGE_COMPONENT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "component_type": 6, // ComponentType.ROLE_SELECT
    "id": 2,
    "custom_id": "role_ids",
    "values": [
      "222222222222222222",
    ],
    "resolved": {
      "roles": {
        "222222222222222222": {
          "color": 12745742,
          "colors": {
            "primary_color": 12745742,
            "secondary_color": null,
            "tertiary_color": null
          },
          "description": null,
          "flags": 0,
          "hoist": false,
          "icon": null,
          "id": "222222222222222222",
          "managed": false,
          "mentionable": true,
          "name": "Developer",
          "permissions": "0",
          "position": 2,
          "unicode_emoji": "🔧"
        }
      }
    }
  },
}
```

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "role_modal",
    "title": "Role Select",
    "components": [
      {
        "type": 18,
        "label": "Select which roles to assign",
        "component": {
          "type": 6,
          "custom_id": "roles_selected",
          "max_values": 10,
          "required": true
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "role_modal",
    "components": [
      {
        "component": {
          "custom_id": "roles_selected",
          "id": 2,
          "type": 6,
          "values": [
            "1362213912946147499",
            "1357409927680889032"
          ]
        },
        "id": 1,
        "type": 18
      }
    ],
    "resolved": {
      "roles": {
        "1357409927680889032": {
          "color": 7419530,
          "colors": {
            "primary_color": 7419530,
            "secondary_color": null,
            "tertiary_color": null
          },
          "description": null,
          "flags": 0,
          "hoist": true,
          "icon": null,
          "id": "1357409927680889032",
          "managed": false,
          "mentionable": true,
          "name": "Player",
          "permissions": "2249596494938111",
          "position": 3,
          "unicode_emoji": "🎮"
        },
        "1362213912946147499": {
          "color": 11342935,
          "colors": {
            "primary_color": 11342935,
            "secondary_color": null,
            "tertiary_color": null
          },
          "description": null,
          "flags": 0,
          "hoist": false,
          "icon": null,
          "id": "1362213912946147499",
          "managed": false,
          "mentionable": false,
          "name": "Mod",
          "permissions": "0",
          "position": 1,
          "unicode_emoji": "🔨"
        }
      }
    }
  }
}
```

---

## Mentionable Select (type 7)

A Mentionable Select is an interactive component that allows users to select one or more mentionables in
a message or modal. Options are automatically populated based on available mentionables in the server.

Mentionable Selects can be configured for both single-select and multi-select behavior. When a user
finishes making their choice(s), your app receives an interaction.

Mentionable Selects are available in messages and modals. They must be placed inside an Action Row in
messages and a Label in modals.

### Mentionable Select Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `7` for mentionable select |
| id? | integer | Optional identifier for component |
| custom\_id | string | ID for the select menu; 1-100 characters |
| placeholder? | string | Placeholder text if nothing is selected; max 150 characters |
| default\_values? | array of default value objects | List of default values for auto-populated select menu components; number of default values must be in the range defined by `min_values` and `max_values` |
| min\_values? \* | integer | Minimum number of items that must be chosen (defaults to 1); min 0 (see note), max 25 |
| max\_values? | integer | Maximum number of items that can be chosen (defaults to 1); max 25 |
| required? \*\* | boolean | Whether the mentionable select is required to answer in a modal (defaults to `true`) |
| disabled? \*\*\* | boolean | Whether select menu is disabled in a message (defaults to `false`) |

\* `min_values` must be either omitted or at least `1` if `required` is omitted or `true`.

\*\* The `required` field is only available for Mentionable Selects in modals. It is ignored in messages.

\*\*\* Using `disabled` in a modal will result in an error. Modals can not currently have disabled
components in them.

### Mentionable Select Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type \* | integer | `7` for a Mentionable Select |
| component\_type \* | integer | `7` for a Mentionable Select |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| resolved | resolved data | Resolved entities from selected options |
| values | array of snowflakes | IDs of the selected mentionables |

\* In message interaction responses `component_type` will be returned and in modal interaction
responses `type` will be returned.

### Examples

**Message Example:**

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 1,  // ComponentType.ACTION_ROW
      "components": [
        {
          "type": 7, // ComponentType.MENTIONABLE_SELECT
          "custom_id": "who_to_ping",
          "placeholder": "Who?",
        }
      ]
    }
  ]
}
```

**Message Interaction Data Example.** Info: `members` and `users` may both be present in the `resolved`
object when a user is selected.

```jsonc
{
  "type": 3, // InteractionType.MESSAGE_COMPONENT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "component_type": 7, // ComponentType.MENTIONABLE_SELECT
    "id": 2,
    "custom_id": "who_to_ping",
    "values": [
      "111111111111111111",
      "222222222222222222",
    ],
    "resolved": {
      "members": {
        "1111111111111111111": {
          "avatar": null,
          "banner": null,
          "collectibles": null,
          "communication_disabled_until": null,
          "flags": 0,
          "joined_at": "2025-05-16T22:51:16.692000+00:00",
          "nick": null,
          "pending": false,
          "permissions": "2248473465835073",
          "premium_since": null,
          "roles": [
            "2222222222222222222"
          ],
          "unusual_dm_activity_until": null
        }
      },
      "users": {
        "1111111111111111111": {
          "avatar": "d54e87d20539fe9aad2f2cebe56809a2",
          "avatar_decoration_data": null,
          "bot": true,
          "clan": null,
          "collectibles": null,
          "discriminator": "9062",
          "display_name_styles": null,
          "global_name": null,
          "id": "1111111111111111111",
          "primary_guild": null,
          "public_flags": 524289,
          "username": "ExampleBot"
        }
      },
      "roles": {
        "222222222222222222": {
          "color": 12745742,
          "colors": {
            "primary_color": 12745742,
            "secondary_color": null,
            "tertiary_color": null
          },
          "description": null,
          "flags": 0,
          "hoist": false,
          "icon": null,
          "id": "222222222222222222",
          "managed": false,
          "mentionable": true,
          "name": "Developer",
          "permissions": "0",
          "position": 2,
          "unicode_emoji": "🔧"
        }
      }
    }
  },
}
```

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "mentionable_modal",
    "title": "Unmentionables",
    "components": [
      {
        "type": 18,
        "label": "Who gets mentioned?",
        "component": {
          "type": 7,
          "custom_id": "mentionables_selected",
          "required": true
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "mentionable_modal",
    "components": [
      {
        "component": {
          "custom_id": "mentionables_selected",
          "id": 2,
          "type": 7,
          "values": [
            "1361539726405926952"
          ]
        },
        "id": 1,
        "type": 18
      }
    ],
    "resolved": {
      "roles": {
        "1361539726405926952": {
          "color": 12745742,
          "colors": {
            "primary_color": 12745742,
            "secondary_color": null,
            "tertiary_color": null
          },
          "description": null,
          "flags": 0,
          "hoist": false,
          "icon": null,
          "id": "1361539726405926952",
          "managed": false,
          "mentionable": true,
          "name": "Developer",
          "permissions": "0",
          "position": 2,
          "unicode_emoji": "🔧"
        }
      }
    }
  }
}
```

---

## Channel Select (type 8)

A Channel Select is an interactive component that allows users to select one or more channels in a
message or modal. Options are automatically populated based on available channels in the server and can
be filtered by channel types.

Channel Selects can be configured for both single-select and multi-select behavior. When a user finishes
making their choice(s) your app receives an interaction.

Channel Selects are available in messages and modals. They must be placed inside an Action Row in
messages and a Label in modals.

### Channel Select Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `8` for channel select |
| id? | integer | Optional identifier for component |
| custom\_id | string | ID for the select menu; 1-100 characters |
| channel\_types? | array of channel types | List of channel types to include in the channel select component |
| placeholder? | string | Placeholder text if nothing is selected; max 150 characters |
| default\_values? | array of default value objects | List of default values for auto-populated select menu components; number of default values must be in the range defined by `min_values` and `max_values` |
| min\_values? \* | integer | Minimum number of items that must be chosen (defaults to 1); min 0 (see note), max 25 |
| max\_values? | integer | Maximum number of items that can be chosen (defaults to 1); max 25 |
| required? \*\* | boolean | Whether the channel select is required to answer in a modal (defaults to `true`) |
| disabled? \*\*\* | boolean | Whether select menu is disabled in a message (defaults to `false`) |

\* `min_values` must be either omitted or at least `1` if `required` is omitted or `true`.

\*\* The `required` field is only available for Channel Selects in modals. It is ignored in messages.

\*\*\* Using `disabled` in a modal will result in an error. Modals can not currently have disabled
components in them.

Channel type integers are defined on the channel object — call the Skill tool with "discord-rest".

### Channel Select Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type \* | integer | `8` for a Channel Select |
| component\_type \* | integer | `8` for a Channel Select |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| resolved | resolved data | Resolved entities from selected options |
| values | array of snowflakes | IDs of the selected channels |

\* In message interaction responses `component_type` will be returned and in modal interaction
responses `type` will be returned.

### Examples

**Message Example:**

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 1,  // ComponentType.ACTION_ROW
      "components": [
        {
          "type": 8,  // ComponentType.CHANNEL_SELECT
          "custom_id": "notification_channel",
          "channel_types": [0],  // ChannelType.TEXT
          "placeholder": "Which text channel?"
        }
      ]
    }
  ]
}
```

**Message Interaction Data Example:**

```jsonc
{
  "type": 3, // InteractionType.MESSAGE_COMPONENT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "component_type": 8, // ComponentType.CHANNEL_SELECT
    "id": 2,
    "custom_id": "notification_channel",
    "values": [
      "333333333333333333",
    ],
    "resolved": {
      "channels": {
        "333333333333333333": {
          "flags": 0,
          "guild_id": "44444444444444444",
          "id": "333333333333333333",
          "last_message_id": null,
          "name": "playtesting",
          "nsfw": false,
          "parent_id": "5555555555555555",
          "permissions": "4503599627370495",
          "position": 1,
          "rate_limit_per_user": 0,
          "topic": null,
          "type": 0  // ChannelType.TEXT
        }
      }
    }
  },
}
```

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "channel_modal",
    "title": "Lockdown",
    "components": [
      {
        "type": 18,
        "label": "Which channel should be locked?",
        "component": {
          "type": 8,
          "custom_id": "channel_selected",
          "required": true
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "channel_modal",
    "components": [
      {
        "component": {
          "custom_id": "channel_selected",
          "id": 2,
          "type": 8,
          "values": [
            "1357483683627663450"
          ]
        },
        "id": 1,
        "type": 18
      }
    ],
    "resolved": {
      "channels": {
        "1357483683627663450": {
          "flags": 0,
          "guild_id": "1111111111111111",
          "id": "1357483683627663450",
          "last_message_id": null,
          "name": "playtesting",
          "nsfw": false,
          "parent_id": "1357129309164404938",
          "permissions": "4503599627370495",
          "position": 1,
          "rate_limit_per_user": 0,
          "topic": null,
          "type": 0
        }
      }
    }
  }
}
```

---

## File Upload (type 19)

File Upload is an interactive component that allows users to upload files in modals. File Uploads can be
configured to have a minimum and maximum number of files between 0 and 10, along with `required` for if
the upload is required to submit the modal. The max file size a user can upload is based on the user's
upload limit in that channel.

File Uploads are available on modals. They must be placed inside a Label.

### File Upload Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `19` for file upload |
| id? | integer | Optional identifier for component |
| custom\_id | string | ID for the file upload; 1-100 characters |
| min\_values? \* | integer | Minimum number of items that must be uploaded (defaults to 1); min 0 (see note), max 10 |
| max\_values? | integer | Maximum number of items that can be uploaded (defaults to 1); max 10 |
| required? | boolean | Whether the file upload requires files to be uploaded before submitting the modal (defaults to `true`) |
| file\_types? \*\* | array of strings | File types to filter for; can be `image`, `video`, `audio`, or any dot-prefixed extension such as `.pdf`; max 10 |

\* `min_values` must be either omitted or at least `1` if `required` is omitted or `true`.

\*\* `file_types` only matches against the file extension. See File Type Filtering
(`https://docs.discord.com/developers/reference#file-type-filtering`) for details.

### File Upload Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `19` for a File Upload |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| values | array of snowflakes | IDs of the uploaded files found in the resolved data |

### Examples

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "bug_submit_modal",
    "title": "Bug Submission",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "label": "File Upload",
        "description": "Please upload a screenshot or other image that shows the bug you encountered.",
        "component": {
          "type": 19, // ComponentType.FILE_UPLOAD
          "custom_id": "file_upload",
          "min_values": 1,
          "max_values": 10,
          "required": true
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "components": [
      {
          "component": {
              "custom_id": "file_upload",
              "id": 2,
              "type": 19,
              "values": [
                  "111111111111111111111"
              ]
          },
          "id": 1,
          "type": 18
      }
    ],
    "custom_id": "bug_submit_modal",
    "resolved": {
      "attachments": {
        "111111111111111111111": {
            "content_type": "image/png",
            "ephemeral": true,
            "filename": "bug.png",
            "height": 604,
            "id": "111111111111111111111",
            "placeholder": "/PcBAoBQydvKesabEIoMsdg=",
            "placeholder_version": 1,
            "proxy_url": "https://media.discordapp.net/ephemeral-attachments/2222222222222222222/111111111111111111111/bug.png?ex=68dc7ce1&is=68db2b61&hm=5954f90117ccf8716ffa6c7f97a778a0d039810c9584045f400d8a9fff590768&",
            "size": 241394,
            "url": "https://cdn.discordapp.com/ephemeral-attachments/2222222222222222222/111111111111111111111/bug.png?ex=68dc7ce1&is=68db2b61&hm=5954f90117ccf8716ffa6c7f97a778a0d039810c9584045f400d8a9fff590768&",
            "width": 2482
        }
      }
    }
  }
}
```

---

## Radio Group (type 21)

A Radio Group is an interactive component for selecting exactly one option from a defined list. Radio
Groups are available in modals and must be placed inside a Label.

### Radio Group Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `21` for radio group |
| id? | integer | Optional identifier for component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| options | array of radio group options | List of options to show; min 2, max 10 |
| required? | boolean | Whether a selection is required to submit the modal (defaults to `true`) |

### Radio Group Option Structure

| Field | Type | Description |
| --- | --- | --- |
| value | string | Dev-defined value of the option; max 100 characters |
| label | string | User-facing label of the option; max 100 characters |
| description? | string | Optional description for the option; max 100 characters |
| default? | boolean | Shows the option as selected by default |

### Radio Group Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `21` for a Radio Group |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| value | ?string | The value of the selected option, or `null` if no option is selected |

### Examples

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "class_selection_modal",
    "title": "Class Selection",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "label": "Choose your class",
        "description": "Your class detertmines the style of play for your character.",
        "component": {
          "type": 21, // ComponentType.RADIO_GROUP
          "custom_id": "class_radio",
          "options": [
            {"value": "warrior", "label": "Warrior", "description": "Strong and brave"},
            {"value": "rogue", "label": "Rogue", "description": "Weak and squishy"},
            {"value": "wizard", "label": "Wizard", "description": "Nerd"},
            {"value": "bard", "label": "Bard", "description": "Annoys everyone"},
            {"value": "witch_doctor", "label": "Witch Doctor", "description": "Actually a pretty cool option"}
          ]
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "class_selection_modal",
    "components": [
      {
        "id": 1,
        "type": 18, // ComponentType.LABEL
        "component": {
          "custom_id": "class_radio",
          "id": 2,
          "type": 21, // ComponentType.RADIO_GROUP
          "value": "warrior"
        }
      }
    ]
  }
}
```

---

## Checkbox Group (type 22)

A Checkbox Group is an interactive component for selecting one or many options via checkboxes. Checkbox
Groups are available in modals and must be placed inside a Label.

### Checkbox Group Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `22` for checkbox group |
| id? | integer | Optional identifier for component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| options | array of checkbox group options | List of options to show; min 1, max 10 |
| min\_values? \* | integer | Minimum number of items that must be chosen; min 0, max 10 (defaults to 1); |
| max\_values? | integer | Maximum number of items that can be chosen; min 1, max 10 (defaults to the number of options) |
| required? | boolean | Whether selecting within the group is required (defaults to `true`) |

\* `min_values` must be either omitted or at least `1` if `required` is omitted or `true`.

### Checkbox Group Option Structure

| Field | Type | Description |
| --- | --- | --- |
| value | string | Dev-defined value of the option; max 100 characters |
| label | string | User-facing label of the option; max 100 characters |
| description? | string | Optional description for the option; max 100 characters |
| default? | boolean | Shows the option as selected by default |

### Checkbox Group Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `22` for a Checkbox Group |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| values | array of strings | The values of the selected options, or an empty array `[]` if no options are selected |

### Examples

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "day_selection_modal",
    "title": "Study Days",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "label": "Which days are you free?",
        "description": "Choose all of the days you're able to meet up.",
        "component": {
          "type": 22, // ComponentType.CHECKBOX_GROUP
          "custom_id": "event_checkbox",
          "options": [
            {"value": "march-4", "label": "March 4th"},
            {"value": "march-5", "label": "March 5th"},
            {"value": "march-7", "label": "March 7th", "description": "I know this is a Saturday and is tough"},
            {"value": "march-9", "label": "March 9th"},
            {"value": "march-10", "label": "March 10th"}
          ]
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "day_selection_modal",
    "components": [
      {
        "id": 1,
        "type": 18, // ComponentType.LABEL
        "component": {
          "custom_id": "event_checkbox",
          "id": 2,
          "type": 22, // ComponentType.CHECKBOX_GROUP
          "values": [
            "march-5",
            "march-10",
            "march-4"
          ]
        }
      }
    ]
  }
}
```

---

## Checkbox (type 23)

A Checkbox is a single interactive component for simple yes/no style questions. Checkboxes are available
in modals and must be placed inside a Label.

### Checkbox Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `23` for checkbox |
| id? | integer | Optional identifier for component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| default? | boolean | Whether the checkbox is selected by default |

**Tip:** While you can't set a checkbox as required, you can use a Checkbox Group with a single option
and `required` to achieve similar functionality.

### Checkbox Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `23` for a Checkbox |
| id | integer | Unique identifier for the component |
| custom\_id | string | Developer-defined identifier for the input; 1-100 characters |
| value | boolean | The state of the checkbox (`true` if checked, `false` if unchecked) |

### Examples

**Modal Example:**

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "secret_note_modal",
    "title": "Secret Note",
    "components": [
      {
        "type": 18, // ComponentType.LABEL
        "label": "Do you like me?",
        "description": "😳😳😳",
        "component": {
          "type": 23, // ComponentType.CHECKBOX
          "custom_id": "like_checkbox"
        }
      }
    ]
  }
}
```

**Modal Submit Interaction Data Example:**

```jsonc
{
  "type": 5, // InteractionType.MODAL_SUBMIT
  ...additionalInteractionFields, // See the Interaction documentation for all fields

  "data": {
    "custom_id": "secret_note_modal",
    "components": [
      {
        "id": 1,
        "type": 18, // ComponentType.LABEL
        "component": {
          "custom_id": "like_checkbox",
          "id": 2,
          "type": 23, // ComponentType.CHECKBOX
          "value": true
        }
      }
    ]
  }
}
```

---

## Source

Discord Developer Documentation, page `https://docs.discord.com/developers/components/reference`,
retrieved 2026-08-26.
