# Setting a User's Rich Presence from an Activity

How `setActivity()` drives what appears on a user's profile while they are in your Activity: the
`rpc.activities.write` scope, the activity partial fields, asset uploads and external asset URLs.

Source: `https://docs.discord.com/developers/rich-presence/using-with-the-embedded-app-sdk`,
retrieved 2026-08-26.

## Contents

- [Scope of this guide](#scope-of-this-guide)
- [Default Rich Presence Data](#default-rich-presence-data)
- [Custom Rich Presence Data](#custom-rich-presence-data)
- [Updating Presence](#updating-presence)
- [rpc.activities.write Scope](#rpcactivitieswrite-scope)
- [setActivity Fields](#setactivity-fields)
- [setActivity Example](#setactivity-example)
- [Uploading Custom Assets](#uploading-custom-assets)
- [Using External Custom Assets](#using-external-custom-assets)

## Scope of this guide

When developing an Activity, the Embedded App SDK makes it easy to integrate Rich Presence to display
details about what a user is up to inside your game or social experience.

Rich Presence data can be thought of as an extension of your Activity — and leveling it up just a
*little* makes it more interesting and relevant to the user playing your Activity (and their friends
that might want to jump in and play).

The guide assumes you've already developed an app that can launch an Activity. If you aren't at that
point yet, follow `BUILDING-AN-ACTIVITY.md` first. Upstream also points at its "Choosing an SDK"
section (`https://docs.discord.com/developers/rich-presence/overview#choosing-an-sdk`) for deciding
whether the Embedded App SDK is the right SDK at all.

## Default Rich Presence Data

By default, when a user is connected to your Activity, the app's icon will appear on their profile. If
the user viewing the profile has the ability to join, an "Ask to Join" button will be displayed as
well.

(Screenshot: "Example of default Rich Presence data for an Activity".)

Upstream's own assessment: "While this is okay, it's pretty limited and doesn't provide much context
about what a user is actually *doing* inside of the Activity."

## Custom Rich Presence Data

(Screenshot: "Image of where Rich Presence data appears in Discord profiles for Activities" — an
annotated profile showing which field lands where.)

Three things to note about that image:

1. `large_image` and `small_image` are both in the `assets` object (see the activity partial table
   below). They're labeled with the object's keys to make it more clear how they appear in a Discord
   profile.
2. You can't set App Name when setting presence — it's always the name configured in your app's
   settings (`https://discord.com/developers/applications`).
3. The state `(1 of max_party)` badge will only render when a party field is provided. Otherwise, state
   will be shown in a line of text below details.

## Updating Presence

When updating Rich Presence data using the Embedded App SDK, the only real command you need to use is
**`setActivity()`**. Under the hood, `setActivity()` calls the RPC `SET_ACTIVITY` command with the
features and fields available when you're building an Activity.

**Why the word "activity" is everywhere.** The "activities" referenced in the RPC docs aren't related
to the Activities you're building with the Embedded App SDK. When Rich Presence was introduced, the
underlying object that contains presence data was called an "activity" (long before the Embedded App
SDK), which is what the RPC `SET_ACTIVITY` command is referencing. And that's *also* why the Embedded
App SDK's wrapper around the RPC command is called `setActivity()` yet isn't really related to setting
the state for the kind of Activity that *you're* building. Upstream's words: "the naming was logical at
the time because it was really about the user's activity in a 3rd party game or service, but now it
sorta feels like activity-ception."

## rpc.activities.write Scope

To display custom Rich Presence data for a user, your app will need to be authorized with the
`rpc.activities.write` scope for that user. To request the scope, your `authorize()` call might look
something like this:

```js
// Authorize with Discord Client
const { code } = await discordSdk.commands.authorize({
  client_id: import.meta.env.VITE_DISCORD_CLIENT_ID,
  response_type: "code",
  state: "",
  prompt: "none",
  scope: [
    "identify",
    "rpc.activities.write"
  ],
});
```

## setActivity Fields

When calling `setActivity()`, you are expected to pass a partial activity object (the Gateway activity
structure). Below is the table upstream provides of "many of the available fields for the activity
partial. Some were left out since they don't have an effect for Activities." The complete `Activity`
interface as the SDK types it — including `name`, `url`, `created_at`, `application_id`, `details_url`,
`state_url`, `emoji`, `secrets`, `instance` and `flags` — is in `EMBEDDED-APP-SDK-EVENTS.md`.

### Activity partial object

All of the fields on the partial object are optional and nullable.

| field | type | description |
| --- | --- | --- |
| type | integer | Activity type, which determines the header text for the Rich Presence data |
| state | string | User's current party status |
| details | string | What the player is currently doing in your Activity |
| timestamps | timestamps object | Unix timestamps to display start and/or end times |
| assets | assets object | Images used for the Rich Presence data (and their hover texts) |
| party | party object | Information for the current party of the player |

The `timestamps`, `assets` and `party` sub-objects are the Gateway activity ones; their SDK-typed
equivalents are `Timestamp`, `Assets` and `Party` in `EMBEDDED-APP-SDK-EVENTS.md`. For the Gateway
activity types and asset-image rules, call the Skill tool with "discord-gateway".

## setActivity Example

(Screenshot: "Example of a fake game's Rich Presence data".) To create this sort of Rich Presence,
here is what the `setActivity()` code would look like:

```js
await discordSdk.commands.setActivity({
  activity: {
    type: 0,
    details: 'Traveling with a group',
    state: 'In Mainframe',
    assets: {
      large_image: 'main-game-image',
      large_text: 'in a group',
      small_image: 'map-mainframe',
      small_text: 'in mainframe'
    },
    timestamps: {
      start: 1723137832
    },
    party: {
      size: [2,4]
    }
  }
});
```

## Uploading Custom Assets

To upload custom art assets for Rich Presence, navigate to your app's settings
(`https://discord.com/developers/applications`) and click **Rich Presence** on the left-hand sidebar.
On the **Art Assets** page (`https://discord.com/developers/applications/select/rich-presence/assets`),
you can upload up to **300** custom assets for your app. It's recommended to make all Rich Presence
assets **1024 x 1024**.

When uploading assets, the asset keys will automatically be changed to lowercase. Keep this in mind when
referencing asset keys in the `assets` object when calling `setActivity()` — for example, an asset
uploaded as `Main-Game-Image` would be referenced as `main-game-image`.

For tips on choosing assets, upstream points at its Rich Presence best practices guide
(`https://docs.discord.com/developers/rich-presence/best-practices#have-interesting-expressive-art`),
which is outside this skill's page set.

## Using External Custom Assets

Typically when building an Activity, you need to be aware of the proxy and how to use external
resources (see `DEVELOPMENT-GUIDES.md` under Networking). However, image URLs in fields for features
like Rich Presence don't need to jump through any extra hoops.

If you have more than 300 custom assets or want to use images stored somewhere else, you can specify an
external URL for `large_image` or `small_image` within the `assets` object.

```js
await discordSdk.commands.setActivity({
  activity: {
    type: 2,
    state: 'Broken Hearts and Code (club edit)',
    details: 'DJ Wump',
    assets: {
      large_image: 'https://example.com/album-covers/dj-wump/broken-code-and-hearts-club-edit.jpg',
      large_text: 'Listening to a track',
    }
  }
});
```

**Format support.** Uploaded assets (added via the developer portal) support PNG, JPEG, and WebP only —
animated images are not supported for uploaded assets. Unlike uploaded assets, external URLs also
support GIF, animated WebP, and AVIF. The Gateway "Activity Asset Image" section carries the details;
call the Skill tool with "discord-gateway".

## Source

Discord Developer Documentation,
`https://docs.discord.com/developers/rich-presence/using-with-the-embedded-app-sdk`, retrieved
2026-08-26.
