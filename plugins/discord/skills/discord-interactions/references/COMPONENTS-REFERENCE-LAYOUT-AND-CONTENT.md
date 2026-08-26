# Component Reference — Types, Layout and Content Components

The shared and layout/content half of `https://docs.discord.com/developers/components/reference`,
retrieved 2026-08-26: the complete component type table, component anatomy, `custom_id`, the
`IS_COMPONENTS_V2` flag semantics, Action Row (1), Section (9), Text Display (10), Thumbnail (11), Media
Gallery (12), File (13), Separator (14), Container (17), Label (18), the Unfurled Media Item, file
uploading and Legacy Message Component Behavior.

Interactive components — Button (2), String Select (3), Text Input (4), User/Role/Mentionable/Channel
Select (5-8), File Upload (19), Radio Group (21), Checkbox Group (22), Checkbox (23) — are in
`COMPONENTS-REFERENCE-INTERACTIVE.md`.

## Contents

- [Overview and the IS_COMPONENTS_V2 flag](#overview-and-the-is_components_v2-flag)
- [Component Types (all 20)](#component-types-all-20)
- [Anatomy of a Component](#anatomy-of-a-component)
- [Action Row (type 1)](#action-row-type-1)
- [Section (type 9)](#section-type-9)
- [Text Display (type 10)](#text-display-type-10)
- [Thumbnail (type 11)](#thumbnail-type-11)
- [Media Gallery (type 12)](#media-gallery-type-12)
- [File (type 13)](#file-type-13)
- [Separator (type 14)](#separator-type-14)
- [Container (type 17)](#container-type-17)
- [Label (type 18)](#label-type-18)
- [Unfurled Media Item](#unfurled-media-item)
- [Uploading a file](#uploading-a-file)
- [Legacy Message Component Behavior](#legacy-message-component-behavior)
- [Nesting rules at a glance](#nesting-rules-at-a-glance)
- [All limits in one place](#all-limits-in-one-place)

---

## Overview and the IS_COMPONENTS_V2 flag

The reference covers three main categories:

- **Layout Components** — for organizing and structuring content (Action Rows, Sections, Containers)
- **Content Components** — for displaying static text, images, and files (Text Display, Media Gallery,
  Thumbnails)
- **Interactive Components** — for user interactions (Buttons, Select Menus, Text Input)

To use these components, you need to send the message flag `1 << 15` (`IS_COMPONENTS_V2`, decimal
`32768`) which can be sent on a per-message basis. Once a message has been sent with this flag, it can't
be removed from that message. This enables the new components system with the following changes:

- The `content` and `embeds` fields will no longer work but you'll be able to use Text Display and
  Container as replacements
- Attachments won't show by default — they must be exposed through components
- The `poll` and `stickers` fields are disabled
- Messages allow up to 40 total components

**Info:** Legacy component behavior will continue to work but provides less flexibility and control over
the message layout.

Components allow you to style and structure your messages, modals, and interactions. They are
interactive elements that can create rich user experiences in your Discord applications. Components are
a field on the message object and on the modal interaction callback data. You can use them when creating
messages or responding to an interaction, like an application command.

The components overview page adds: components are accessible, customizable, and easy to use; and using
the `IS_COMPONENTS_V2` flag disables traditional content and embeds, so all content must be sent as
components instead. Legacy message component behavior will **not** be deprecated and will continue to be
available to your apps on a message-by-message basis; Discord recommends the new components for new
projects and features.

---

## Component Types (all 20)

The complete table of available components. Values `15`, `16` and `20` are not defined by the upstream.

| Type | Name | Description | Style | Usage |
| --- | --- | --- | --- | --- |
| 1 | Action Row | Container to display a row of interactive components | Layout | Message |
| 2 | Button | Button object | Interactive | Message |
| 3 | String Select | Select menu for picking from defined text options | Interactive | Message, Modal |
| 4 | Text Input | Text input object | Interactive | Modal |
| 5 | User Select | Select menu for users | Interactive | Message, Modal |
| 6 | Role Select | Select menu for roles | Interactive | Message, Modal |
| 7 | Mentionable Select | Select menu for mentionables (users *and* roles) | Interactive | Message, Modal |
| 8 | Channel Select | Select menu for channels | Interactive | Message, Modal |
| 9 | Section | Container to display text alongside an accessory component | Layout | Message |
| 10 | Text Display | Markdown text | Content | Message, Modal |
| 11 | Thumbnail | Small image that can be used as an accessory | Content | Message |
| 12 | Media Gallery | Display images and other media | Content | Message |
| 13 | File | Displays an attached file | Content | Message |
| 14 | Separator | Component to add vertical padding between other components | Layout | Message |
| 17 | Container | Container that visually groups a set of components | Layout | Message |
| 18 | Label | Container associating a label and description with a component | Layout | Modal |
| 19 | File Upload | Component for uploading files | Interactive | Modal |
| 21 | Radio Group | Single-choice set of options | Interactive | Modal |
| 22 | Checkbox Group | Multi-selectable group of checkboxes | Interactive | Modal |
| 23 | Checkbox | Single checkbox for yes/no choice | Interactive | Modal |

---

## Anatomy of a Component

All components have the following fields:

| Field | Type | Description |
| --- | --- | --- |
| type | integer | The type of the component |
| id? | integer | 32 bit integer used as an optional identifier for component |

The `id` field is optional and is used to identify components in the response from an interaction. The
`id` must be unique within the message and is generated sequentially if left empty. Generation of `id`s
won't use another `id` that exists in the message if you have one defined for another component. Sending
components with an `id` of `0` is allowed but will be treated as empty and replaced by the API.

### Custom ID

Additionally, interactive components like buttons and selects must have a `custom_id` field. The
developer defines this field when sending the component payload, and it is returned in the interaction
payload sent when a user interacts with the component. For example, if you set `custom_id: click_me` on
a button, you'll receive an interaction containing `custom_id: click_me` when a user clicks that button.

`custom_id` is only available on interactive components and must be unique per component. Multiple
components on the same message must not share the same `custom_id`. This field is a string of 1 to 100
characters and can be used flexibly to maintain state or pass through other important data.

| Field | Type | Description |
| --- | --- | --- |
| custom\_id | string | Developer-defined identifier, 1-100 characters |

---

## Action Row (type 1)

An Action Row is a top-level layout component.

Action Rows can contain one of the following:

- Up to 5 contextually grouped buttons
- A single select component (string select, user select, role select, mentionable select, or channel
  select)

**Info:** Label is recommended for use over an Action Row in modals. Action Row with Text Inputs in
modals are now deprecated.

### Action Row Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `1` for action row component |
| id? | integer | Optional identifier for component |
| components | array of action row child components | Up to 5 interactive button components or a single select component |

### Action Row Child Components

| Available Components | Description |
| --- | --- |
| Button | An Action Row can contain up to 5 Buttons |
| String Select | A single String Select |
| User Select | A single User Select |
| Role Select | A single Role Select |
| Mentionable Select | A single Mentionable Select |
| Channel Select | A single Channel Select |

### Examples

**Message Example** — Message create payload with an Action Row component.
*(Image: Example of an Action Row with three buttons.)*

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 1,  // ComponentType.ACTION_ROW
      "components": [
        {
          "type": 2,  // ComponentType.BUTTON
          "custom_id": "click_yes",
          "label": "Accept",
          "style": 1
        },
        {
          "type": 2,  // ComponentType.BUTTON
          "label": "Learn More",
          "style": 5,
          "url": "http://watchanimeattheoffice.com/"
        },
        {
          "type": 2,  // ComponentType.BUTTON
          "custom_id": "click_no",
          "label": "Decline",
          "style": 4
        }
      ]
    }
  ]
}
```

---

## Section (type 9)

A Section is a top-level layout component that allows you to contextually associate content with an
accessory component. The typical use case is to contextually associate text content with an accessory.

Sections are currently only available in messages.

**Info:** To use this component in messages you must send the message flag `1 << 15`
(`IS_COMPONENTS_V2`) which can be activated on a per-message basis.

### Section Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `9` for section component |
| id? | integer | Optional identifier for component |
| components | array of section child components | One to three child components representing the content of the section that is contextually associated to the accessory |
| accessory | section accessory component | A component that is contextually associated to the content of the section |

**Info:** Don't hardcode `components` to contain only text components. Discord may add other components
in the future. Similarly, `accessory` may be expanded to include other components in the future.

### Section Child Components

| Available Components |
| --- |
| Text Display |

### Section Accessory Components

| Available Components |
| --- |
| Button |
| Thumbnail |

### Examples

**Message Example** — Message create payload with a Section (and Thumbnail) component.
*(Image: Example of a Section showing a fake game changelog and a thumbnail.)*

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 9,  // ComponentType.SECTION
      "components": [
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "# Real Game v7.3"
        },
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "Hope you're excited, the update is finally here! Here are some of the changes:\n- Fixed a bug where certain treasure chests wouldn't open properly\n- Improved server stability during peak hours\n- Added a new type of gravity that will randomly apply when the moon is visible in-game\n- Every third thursday the furniture will scream your darkest secrets to nearby npcs"
        },
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "-# That last one wasn't real, but don't use voice chat near furniture just in case..."
        }
      ],
      "accessory": {
        "type": 11,  // ComponentType.THUMBNAIL
        "media": {
          "url": "https://websitewithopensourceimages/gamepreview.webp"
        }
      }
    }
  ]
}
```

---

## Text Display (type 10)

A Text Display is a top-level content component that allows you to add markdown formatted text,
including mentions (users, roles, etc) and emojis. The behavior of this component is extremely similar
to the `content` field of a message, but allows you to add multiple text components, controlling the
layout of your message.

When sent in a message, pingable mentions (@user, @role, etc) present in this component will ping and
send notifications based on the value of the allowed mention object set in `message.allowed_mentions`.

**Info:** To use this component in messages you must send the message flag `1 << 15`
(`IS_COMPONENTS_V2`) which can be activated on a per-message basis.

### Text Display Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `10` for text display |
| id? | integer | Optional identifier for component |
| content | string | Text that will be displayed similar to a message |

### Text Display Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `10` for a Text Display |
| id | integer | Unique identifier for the component |

### Examples

**Message Example.** *(Image: Example of a Text Display with markdown.)*

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 10,  // ComponentType.TEXT_DISPLAY
      "content": "# This is a Text Display\nAll the regular markdown rules apply\n- You can make lists\n- You can use `code blocks`\n- You can use [links](http://watchanimeattheoffice.com/)\n- Even :blush: :star_struck: :exploding_head:\n- Spoiler alert: ||these too!||"
    }
  ]
}
```

**Modal Example.** *(Image: Example of a Text Display from the code below.)*

```jsonc
{
  "type": 9,
  "data": {
    "custom_id": "jail_modal",
    "title": "Jail",
    "components": [
      {
        "type": 10,
        "content": "This action will move the selected user to the selected voice channel and take away all their permissions **for 1 hour**."
      },
      {
        "type": 18,
        "label": "Choose a user",
        "component": {
          "type": 5,
          "custom_id": "user_selected",
          "required": true
        }
      },
      {
        "type": 18,
        "label": "Where should they be sent?",
        "component": {
          "type": 8,
          "custom_id": "channel_selected",
          "channel_types": [
            2
          ],
          "required": true
        }
      }
    ]
  }
}
```

---

## Thumbnail (type 11)

A Thumbnail is a content component that displays visual media in a small form-factor. It is intended as
an accessory to other content, and is primarily usable with sections. The media displayed is defined by
the unfurled media item structure, which supports both uploaded media and externally hosted media.

Thumbnails are currently only available in messages as an accessory in a section.

Thumbnails currently only support images, including animated formats like GIF and WEBP. Videos are not
supported at this time.

**Info:** To use this component, you need to send the message flag `1 << 15` (`IS_COMPONENTS_V2`), which
can be activated on a per-message basis.

### Thumbnail Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `11` for thumbnail component |
| id? | integer | Optional identifier for component |
| media | unfurled media item | A url or attachment provided as an unfurled media item |
| description? | ?string | Alt text for the media, max 1024 characters |
| spoiler? | boolean | Whether the thumbnail should be a spoiler (or blurred out). Defaults to `false` |

### Examples

**Message Example** — Message create payload with a Thumbnail component (via Section). The upstream
reuses the Section payload here verbatim.
*(Image: Example of a Thumbnail in a Section from the code below.)*

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 9,  // ComponentType.SECTION
      "components": [
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "# Real Game v7.3"
        },
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "Hope you're excited, the update is finally here! Here are some of the changes:\n- Fixed a bug where certain treasure chests wouldn't open properly\n- Improved server stability during peak hours\n- Added a new type of gravity that will randomly apply when the moon is visible in-game\n- Every third thursday the furniture will scream your darkest secrets to nearby npcs"
        },
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "-# That last one wasn't real, but don't use voice chat near furniture just in case..."
        }
      ],
      "accessory": {
        "type": 11,  // ComponentType.THUMBNAIL
        "media": {
          "url": "https://websitewithopensourceimages/gamepreview.webp"
        }
      }
    }
  ]
}
```

---

## Media Gallery (type 12)

A Media Gallery is a top-level content component that allows you to display 1-10 media attachments in an
organized gallery format. Each item can have optional descriptions and can be marked as spoilers.

Media Galleries are currently only available in messages.

**Info:** To use this component in messages you must send the message flag `1 << 15`
(`IS_COMPONENTS_V2`) which can be activated on a per-message basis.

### Media Gallery Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `12` for media gallery component |
| id? | integer | Optional identifier for component |
| items | array of media gallery items | 1 to 10 media gallery items |

### Media Gallery Item Structure

| Field | Type | Description |
| --- | --- | --- |
| media | unfurled media item | A url or attachment provided as an unfurled media item |
| description? | ?string | Alt text for the media, max 1024 characters |
| spoiler? | boolean | Whether the media should be a spoiler (or blurred out). Defaults to `false` |

### Examples

**Message Example.** *(Image: Example of a Media Gallery showing screenshots from live webcam feeds.)*

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 10,  // ComponentType.TEXT_DISPLAY
      "content": "Live webcam shots as of 18-04-2025 at 12:00 UTC"
    },
    {
      "type": 12,  // ComponentType.MEDIA_GALLERY
      "items": [
        {
          "media": {"url": "https://livevideofeedconvertedtoimage/webcam1.webp"},
          "description": "An aerial view looking down on older industrial complex buildings. The main building is white with many windows and pipes running up the walls."
        },
        {
          "media": {"url": "https://livevideofeedconvertedtoimage/webcam2.webp"},
          "description": "An aerial view of old broken buildings. Nature has begun to take root in the rooftops. A portion of the middle building's roof has collapsed inward. In the distant haze you can make out a far away city."
        },
        {
          "media": {"url": "https://livevideofeedconvertedtoimage/webcam3.webp"},
          "description": "A street view of a downtown city. Prominently in photo are skyscrapers and a domed building"
        }
      ]
    }
  ]
}
```

---

## File (type 13)

A File is a top-level content component that allows you to display an uploaded file as an attachment to
the message and reference it in the component. Each file component can only display 1 attached file, but
you can upload multiple files and add them to different file components within your payload.

Files are currently only available in messages.

**Info:** The File component only supports using the `attachment://` protocol in the unfurled media
item.

**Info:** To use this component in messages you must send the message flag `1 << 15`
(`IS_COMPONENTS_V2`) which can be activated on a per-message basis.

### File Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `13` for a file component |
| id? | integer | Optional identifier for component |
| file | unfurled media item | This unfurled media item is unique in that it **only** supports attachment references using the `attachment://<filename>` syntax |
| spoiler? | boolean | Whether the media should be a spoiler (or blurred out). Defaults to `false` |
| name? | string | The name of the file. This field is ignored and provided by the API as part of the response |
| size? | integer | The size of the file in bytes. This field is ignored and provided by the API as part of the response |

### Examples

**Message Example.** *(Image: Example of a File showing a download for a game and manual.)* This example
makes use of the `attachment://` protocol functionality in the unfurled media item.

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 10,  // ComponentType.TEXT_DISPLAY
      "content": "# New game version released for testing!\nGrab the game here:"
    },
    {
      "type": 13,  // ComponentType.FILE
      "file": {
        "url": "attachment://game.zip"
      }
    },
    {
      "type": 10,  // ComponentType.TEXT_DISPLAY
      "content": "Latest manual artwork here:"
    },
    {
      "type": 13,  // ComponentType.FILE
      "file": {
        "url": "attachment://manual.pdf"
      }
    }
  ]
}
```

---

## Separator (type 14)

A Separator is a top-level layout component that adds vertical padding and visual division between other
components.

Separators are currently only available in messages.

**Info:** To use this component in messages you must send the message flag `1 << 15`
(`IS_COMPONENTS_V2`) which can be activated on a per-message basis.

### Separator Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `14` for separator component |
| id? | integer | Optional identifier for component |
| divider? | boolean | Whether a visual divider should be displayed in the component. Defaults to `true` |
| spacing? | integer | Size of separator padding — `1` for small padding, `2` for large padding. Defaults to `1` |

### Examples

**Message Example.** *(Image: Example of a separator with large spacing dividing content.)*

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 10,  // ComponentType.TEXT_DISPLAY
      "content": "It's dangerous to go alone!"
    },
    {
      "type": 14,  // ComponentType.SEPARATOR
      "divider": true,
      "spacing": 1
    },
    {
      "type": 10,  // ComponentType.TEXT_DISPLAY
      "content": "Take this."
    }
  ]
}
```

---

## Container (type 17)

A Container is a top-level layout component. Containers offer the ability to visually encapsulate a
collection of components and have an optional customizable accent color bar.

Containers are currently only available in messages.

**Info:** To use this component in messages you must send the message flag `1 << 15`
(`IS_COMPONENTS_V2`) which can be activated on a per-message basis.

### Container Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `17` for container component |
| id? | integer | Optional identifier for component |
| components | array of container child components | Child components that are encapsulated within the Container |
| accent\_color? | ?integer | Color for the accent on the container as RGB from `0x000000` to `0xFFFFFF` |
| spoiler? | boolean | Whether the container should be a spoiler (or blurred out). Defaults to `false`. |

### Container Child Components

| Available Components |
| --- |
| Action Row |
| Text Display |
| Section |
| Media Gallery |
| Separator |
| File |

### Examples

**Message Example.** *(Image: Example of a container showing text, image, and buttons for a wild enemy
encounter.)*

```jsonc
{
  "flags": 32768,
  "components": [
    {
      "type": 17,  // ComponentType.CONTAINER
      "accent_color": 703487,
      "components": [
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "# You have encountered a wild coyote!"
        },
        {
          "type": 12,  // ComponentType.MEDIA_GALLERY
          "items": [
            {
              "media": {"url": "https://websitewithopensourceimages/coyote.webp"},
            }
          ]
        },
        {
          "type": 10,  // ComponentType.TEXT_DISPLAY
          "content": "What would you like to do?"
        },
        {
          "type": 1,  // ComponentType.ACTION_ROW
          "components": [
            {
              "type": 2,  // ComponentType.BUTTON
              "custom_id": "pet_coyote",
              "label": "Pet it!",
              "style": 1
            },
            {
              "type": 2,  // ComponentType.BUTTON
              "custom_id": "feed_coyote",
              "label": "Attempt to feed it",
              "style": 2
            },
            {
              "type": 2,  // ComponentType.BUTTON
              "custom_id": "run_away",
              "label": "Run away!",
              "style": 4
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Label (type 18)

A Label is a top-level layout component. Labels wrap modal components with text as a label and optional
description.

**Info:** The `description` may display above or below the `component` depending on the platform.

### Label Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `18` for a label |
| id? | integer | Optional identifier for component |
| label | string | The label text; max 45 characters |
| description? | string | An optional description text for the label; max 100 characters |
| component | label child component | The component within the label |

### Label Child Components

| Available Components |
| --- |
| Text Input |
| String Select |
| User Select |
| Role Select |
| Mentionable Select |
| Channel Select |
| File Upload |
| Radio Group |
| Checkbox Group |
| Checkbox |

### Label Interaction Response Structure

| Field | Type | Description |
| --- | --- | --- |
| type | integer | `18` for a Label |
| id | integer | Unique identifier for the component |
| component | label interaction response child component | The component within the label |

### Label Interaction Response Child Components

Each entry points at that component's "Interaction Response Structure" table in
`COMPONENTS-REFERENCE-INTERACTIVE.md`.

| Available Components |
| --- |
| Text Input |
| String Select |
| User Select |
| Role Select |
| Mentionable Select |
| Channel Select |
| File Upload |
| Radio Group |
| Checkbox Group |
| Checkbox |

### Examples

**Modal Example** — Modal create payload with a Label component (wrapping a Text Input).
*(Image: A modal with Text Input in a Label.)*

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

---

## Unfurled Media Item

An Unfurled Media Item is a piece of media, represented by a URL, that is used within a component. It can
be constructed via either uploading media to Discord, or by referencing external media via **a direct
link** to the asset.

**Info:** While the structure below is the full representation of an Unfurled Media Item, **only the
`url` field is settable by developers** when making requests that utilize this structure. All other
fields will be automatically populated by Discord.

### Unfurled Media Item Structure

| Field | Type | Description |
| --- | --- | --- |
| url | string | Supports arbitrary urls and `attachment://<filename>` references |
| proxy\_url? \* | string | The proxied url of the media item |
| height? \* | ?integer | The height of the media item (if image or video) |
| width? \* | ?integer | The width of the media item (if image or video) |
| placeholder? \* | string | Thumbhash placeholder (if image or video) |
| placeholder\_version? \* | integer | Version of the placeholder (if image or video) |
| content\_type? \* | string | The media type of the content |
| flags? \* | integer | Unfurled media item flags combined as a bitfield |
| attachment\_id? \* \*\* | snowflake | The id of the uploaded attachment |

\* This field is ignored and provided by the API as part of the response.

\*\* Only present if the media item was uploaded as an attachment.

### Unfurled Media Item Flags

| Flag | Value | Description |
| --- | --- | --- |
| IS\_ANIMATED | `1 << 0` | This image is animated |

---

## Uploading a file

To upload a file with your message, you'll need to send your payload as `multipart/form-data` (rather
than `application/json`) and include your file with a valid filename in your payload. Details and
examples for uploading files can be found in the API Reference
(`https://docs.discord.com/developers/reference#uploading-files`).

---

## Legacy Message Component Behavior

Before the introduction of the `IS_COMPONENTS_V2` flag, message components were sent in conjunction with
message content. This means that you could send a message using a subset of the available components
without setting the `IS_COMPONENTS_V2` flag, and the components would be included in the message content
along with `content` and `embeds`.

Additionally, components of messages preceding components V2 will contain an `id` of `0`.

Apps using this Legacy Message Component behavior will continue to work as expected, but it is
recommended to use the new `IS_COMPONENTS_V2` flag for new apps or features as they offer more options
for layout and customization.

**Info:** Legacy messages allow up to 5 action rows as top-level components.

Legacy Message Component Example:

```jsonc
{
  "content": "This is a message with legacy components",
  "components": [
    {
      "type": 1,
      "components": [
        {
          "type": 2,
          "style": 1,
          "label": "Click Me",
          "custom_id": "click_me_1"
        }
      ]
    }
  ]
}
```

---

## Nesting rules at a glance

Derived only from the per-component statements above; the upstream states no additional nesting rules.

| Parent | Allowed children |
| --- | --- |
| Message top level (V2) | Action Row, Text Display, Section, Media Gallery, Separator, Container, File |
| Message top level (legacy) | up to 5 Action Rows |
| Action Row | up to 5 Buttons, **or** exactly one of String/User/Role/Mentionable/Channel Select |
| Section | 1-3 Text Display children, plus one `accessory`: Button or Thumbnail |
| Container | Action Row, Text Display, Section, Media Gallery, Separator, File |
| Modal top level | Label, Text Display (per the Text Display modal example); Action Row with Text Input is deprecated |
| Label | exactly one of Text Input, String/User/Role/Mentionable/Channel Select, File Upload, Radio Group, Checkbox Group, Checkbox |
| Thumbnail | usable only as a Section `accessory` |

---

## All limits in one place

| Limit | Value |
| --- | --- |
| Message flag to enable components V2 | `1 << 15` (`IS_COMPONENTS_V2`, decimal 32768); irreversible per message |
| Total components per V2 message | up to 40 |
| Action rows per legacy message | up to 5 |
| Buttons per Action Row | up to 5 |
| Selects per Action Row | exactly 1 |
| `custom_id` | 1-100 characters, unique per component within the message |
| Component `id` | 32 bit integer, unique within the message; `0` is treated as empty |
| Button `label` | max 80 characters |
| Button `url` | max 512 characters |
| Button content guideline | 34 characters max with icon or emoji, 38 without |
| Select `placeholder` | max 150 characters |
| Select `options` | max 25 |
| Select option `label` / `value` / `description` | max 100 characters each |
| Select `min_values` | min 0, max 25 (must be ≥ 1 when `required` is omitted or `true`) |
| Select `max_values` | max 25 |
| Text Input `min_length` | min 0, max 4000 |
| Text Input `max_length` | min 1, max 4000 |
| Text Input `value` | max 4000 characters |
| Text Input `placeholder` | max 100 characters |
| Section children | 1 to 3 — upstream wording: "One to three child components representing the content of the section that is contextually associated to the accessory" |
| Thumbnail / Media Gallery item `description` (alt text) | max 1024 characters |
| Media Gallery `items` | 1 to 10 |
| File component attachments | 1 file per component; `attachment://` only |
| Separator `spacing` | `1` small (default), `2` large |
| Container `accent_color` | RGB `0x000000` to `0xFFFFFF` |
| Label `label` | max 45 characters |
| Label `description` | max 100 characters |
| File Upload `min_values` / `max_values` | 0-10 / max 10 |
| File Upload `file_types` | max 10 entries |
| Radio Group `options` | min 2, max 10 |
| Checkbox Group `options` | min 1, max 10 |
| Checkbox Group `min_values` / `max_values` | min 0 max 10 / min 1 max 10 (default = number of options) |
| Modal `components` | between 1 and 5 (from the interaction response object) |

---

## Source

Discord Developer Documentation, retrieved 2026-08-26:

- `https://docs.discord.com/developers/components/reference`
- `https://docs.discord.com/developers/components/overview`
