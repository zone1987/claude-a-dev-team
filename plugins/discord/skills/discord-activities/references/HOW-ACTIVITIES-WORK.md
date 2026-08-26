# How Activities Work, and How to Design One

The technical model (iframe, `postMessage`, launch paths, lifecycle), the Activities overview and
sample projects, the platform-page framing, and the complete design-patterns guidance.

Sources: `activities/how-activities-work`, `activities/overview`, `platform/activities` and
`activities/design-patterns` on `https://docs.discord.com/developers/`, retrieved 2026-08-26.

## Contents

- [The model](#the-model)
- [Launching Activities](#launching-activities)
- [Designed for Single-Page Apps](#designed-for-single-page-apps-spas)
- [Activity Lifecycle](#activity-lifecycle)
- [Minimal setup example](#minimal-setup-example)
- [Activities Overview and sample projects](#activities-overview-and-sample-projects)
- [Platform page framing](#platform-page-framing)
- [Design Patterns: guiding principles](#design-patterns-guiding-principles)
- [Design Patterns: solo-plus experience](#design-patterns-solo-plus-experience)
- [Design Patterns: user presence and privacy](#design-patterns-user-presence-and-privacy)
- [Design Patterns: deliver a quality experience](#design-patterns-deliver-a-quality-experience)
- [Design Patterns: game design considerations](#design-patterns-game-design-considerations)
- [Design Patterns: co-watching and co-listening](#design-patterns-co-watching-and-co-listening)
- [Design Patterns: technical considerations](#design-patterns-technical-considerations)
- [Design Patterns: quality and testing](#design-patterns-quality-and-testing)

## The model

Activities are web applications that run in an iframe within Discord on desktop, mobile and web. In
order to achieve this, Discord uses the `postMessage` protocol to enable secure communication between
your application and Discord.

The Embedded App SDK simplifies this process by managing the `postMessage` protocol on your behalf.
Available commands and their usage are in `EMBEDDED-APP-SDK-COMMANDS.md` and
`EMBEDDED-APP-SDK-EVENTS.md`.

## Launching Activities

After you have Activities enabled in your Application's Activity settings
(`https://discord.com/developers/applications/select/embedded/settings`), your app can launch
Activities in two ways:

1. When a user invokes your app's Entry Point command in the App Launcher
2. By responding to an interaction with the `LAUNCH_ACTIVITY` callback type

### Entry Point Command

Activities are primarily opened when users invoke your app's Entry Point command in the App Launcher.

When you enable Activities for your app, a default Entry Point command called "Launch" is created for
you. By default, Discord automatically handles opening your Activity when your Entry Point command is
run by a user.

Setup details are in `DEVELOPMENT-GUIDES.md` under User Actions.

### Interaction Response

Activities can be launched in response to command, message component, and modal submission
interactions. To open an Activity, set the callback type to `LAUNCH_ACTIVITY` (type `12`) when
responding to the interaction. Call the Skill tool with "discord-interactions" for the response
mechanics.

## Designed for Single-Page Apps (SPAs)

This SDK is intended for use by a single-page application. Discord recognizes developers may be using
frameworks or approaches that are not an exact fit for single-page applications, and recommends nesting
those frameworks inside your Activity's top-level single-page application and passing messages as you
see fit. The Nested Messages App sample project is the reference for this approach.

## Activity Lifecycle

1. **Initialization:** When your iframe is loaded within Discord, it will include unique query
   parameters in its URL. These parameters are identifiable by your application using the Discord SDK.
2. **Handshake Process:** Constructing the SDK instance begins a handshake process with the Discord
   client. Once the connection is established, the iframe receives a `[FRAME, {evt: 'READY', ...}]`
   message. The `ready()` method of the SDK instance resolves once a successful connection has been
   established.
3. **Authorization and Authentication:** After receiving the `READY` payload, your application should
   perform authorization and authentication to acquire necessary permissions (scopes). This step is
   crucial for utilizing specific features or scopes, such as `rpc.activities.write`.
4. **Interacting with Discord Client:** Post-authentication, your application can subscribe to events
   and send commands to the Discord client. Note that attempting to use commands or subscribe to events
   outside your granted scope will result in errors. Adding new scopes may prompt an OAuth modal for
   user permission re-confirmation.
5. **Disconnection and Errors:** Receiving a `[CLOSE, {message: string, code: number}]` message
   indicates an error or a need to restart the connection process.
6. **Sending Errors or Close Requests:** To communicate an error or request a close from the Discord
   client, send `[CLOSE, {message?: string, code: number}]`. A code other than `CLOSE_NORMAL` will
   display the message to the user, while `CLOSE_NORMAL` results in a silent closure.

## Minimal setup example

Note the proxy-relative fetch path `/.proxy/api/token` in this version of the flow.

```javascript
import {DiscordSDK} from '@discord/embedded-app-sdk';
const discordSdk = new DiscordSDK(YOUR_OAUTH2_CLIENT_ID);

async function setup() {
  // Wait for READY payload from the discord client
  await discordSdk.ready();

  // Pop open the OAuth permission modal and request for access to scopes listed in scope array below
  const {code} = await discordSdk.commands.authorize({
    client_id: YOUR_OAUTH2_CLIENT_ID,
    response_type: 'code',
    state: '',
    prompt: 'none',
    scope: ['identify'],
  });

  // Retrieve an access_token from your application's server
  const response = await fetch('/.proxy/api/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      code,
    }),
  });
  const {access_token} = await response.json();

  // Authenticate with Discord client (using the access_token)
  auth = await discordSdk.commands.authenticate({
    access_token,
  });
}
```

(Diagram: "Diagram of how Activities communicate with Discord" — the communication flow between your
application and Discord for the code above.)

## Activities Overview and sample projects

Activities are web apps hosted in an iframe that use the Embedded App SDK to communicate with Discord
clients.

**Developing Activities.** Whether you're developing a multiplayer game, a new social experience, or
another creative idea, your Activity will be built as a web app that is run in an iframe in Discord on
desktop, mobile, and web.

- **Commands.** The SDK has a set of commands you can call to interact with a Discord client, given you
  have the appropriate scopes. This is helpful when you want to authorize and authenticate users, fetch
  information about your Activity, or update information for your Activity or an authenticated user.
- **Events.** The SDK also has events you can subscribe (or unsubscribe) to for things happening in a
  connected client that are relevant to your Activity, given you have the appropriate scopes. This is
  helpful when you want to do things like handle initial connection and thrown errors, listen to
  updates about a connected user, and listen to events related to your Activity instance.

Real-world Activities can be explored through Discord's developer case studies at
`https://discord.com/build#case-studies`.

**Sample projects.** A list of community-maintained samples, including more framework-specific
examples, is at
`https://github.com/discord/embedded-app-sdk-examples?tab=readme-ov-file#community-curated-examples`.

- **Discord Activity Starter** —
  `https://github.com/discord/embedded-app-sdk-examples/tree/main/discord-activity-starter`. This
  TypeScript starter template is perfect for getting your own Activity up and running quickly.
- **Embedded App SDK Playground** —
  `https://github.com/discord/embedded-app-sdk-examples/tree/main/sdk-playground`. This reference
  example implements the commands and events available to you within the Embedded App SDK.
- **Nested Framework App** —
  `https://github.com/discord/embedded-app-sdk-examples/tree/main/nested-messages`. This reference
  example demonstrates an Activity using a nested framework like a game engine.

## Platform page framing

The `platform/activities` page is a short marketing-level introduction and adds only these facts:

- Activities are multiplayer games and social experiences embedded directly in Discord. They can be
  launched in channels, DMs, or from the App Launcher with no external window or separate download
  required.
- Players can jump in together with friends already in a voice channel, making Activities a natural fit
  for party games, co-watching, collaborative tools, and more.
- Under the hood, Activities are an iframe that communicates with Discord using the Embedded App SDK.
  The SDK provides methods for interacting between your Activity and the Discord client.

Everything else on that page is navigation to the three pages distilled in this skill.

## Design Patterns: guiding principles

Page: `https://docs.discord.com/developers/activities/design-patterns`

**Interaction over Isolation**

- Activities are not for screen-sharing, Discord already has that built-in.
- Give users a way to interact with one another.
- User actions should impact the experiences of other participants.

**Expression over Monotony**

- Discord's users want to create memorable moments.
- Create experiences where users craft moments and react in ways they want to share with others.

**Accessibility over Exclusion**

- Inclusivity is key.
- Reduce the bar to entry for your Activity and reward people for engaging deeply with your experience.

## Design Patterns: solo-plus experience

Successful experiences will be built to accommodate small group sessions ("Plus"), but also playable
and enjoyable for the case of single-player ("Solo") sessions.

**Solo or single-player**

- While most people use Discord with small groups of friends, consider experiences that are compelling
  alone, but better together.
- If you don't support solo play, expect to see a lot of users peeking into the Activity on their own.
  Consider what you can do to preview the Activity and compel them to come back with their friends.

**Solo-Plus or small groups of users**

- Small group sessions (3-8 people) show more engagement and retention from users than single-player
  experiences.
- Letting players join with their friends keeps them coming back for more.

**Large groups of users**

- While you can set a "max participants" suggestion to users, the only real limit is the number of
  people who can join a Voice call.
- Be aware of how your Activity will behave when there are 25 or more people in the call.

## Design Patterns: user presence and privacy

When in an Activity with others, make the actions and presence of the others visible to each player.

**Make actions and presence of the others visible to each player**

- Users enjoy participating in a space that feels active.
- If a user has customized their server nickname or avatar, use their server nickname or avatar in
  game.
- Show when a user is speaking in the voice call, or whether they're active or inactive.

(Screenshot: "Speech bubbles in Bobble League".)

**Respect user privacy**

- For Activity sessions that match users from various servers, usernames and avatars should be
  anonymized by default.
- Discord personal identifiers should only be populated into the Activity with user confirmation.
- Only use these identifiers when the people who can see them already have access via the server or DM.

## Design Patterns: deliver a quality experience

Make your app fast, easy to join, and maximize fun to launch a crowd favorite.

**Surprise and delight users**

- Surprise and delight is about caring about the small details of how a person experiences your work.
- Put the right emotion in when they least expect it to deliver the magic.

(Screenshot: "Bobble League".)

**Keep load times as low as possible**

- This allows for easier drop-in drop-out behavior for the large portion of mobile users on Discord.
- See the Quality and Testing section below for key areas of minimum quality support and testing
  recommendations.
- See the Technical Considerations section below for recommendations on how to partition loading and
  work with various development tools to reduce load times.
- Consider different screen sizes and orientations across desktop and mobile devices and make sure UI
  elements scale appropriately.

**Support drop-in, drop-out behavior**

- Activities are frictionless to join and easy to discover, so you can expect that users will join
  mid-experience. Give those users something to do, even if it's just letting them spectate until they
  can join without being disruptive. In the same vein, users can leave without notice or become afk
  (away from keyboard). Handle these cases gracefully.
- Create a case for users who have joined a call but have not yet started playing or engaging. Allow
  these users to "spectate" other users who are playing. This can also be helpful for Activities that
  have an ideal number in mind for play.

(Screenshot: "Support drop-in, drop-out behavior in your Activity" — Eights.)

**Make your app as available as possible**

*Cross-Platform Support*

- Supporting desktop and mobile devices will expand your user-base to the widest number of users.
- Discord device usage is split between mobile and desktop platforms.

*Discord is a Global Audience*

- Consider supporting a multitude of languages and cultures to make your app more usable for all
  Discord users.

*Implement Invites*

- The Embedded App SDK allows for sending invites from within an Activity out to other friended users.
- Add invite buttons to a screen or flow with intentionality, not only on the start screen and at the
  beginning. Examples of intentional Invite prompting include:
  - Cases where players leave the activity session
  - Cases where the minimum number of participants has not been reached (e.g. any activity that needs
    2+ to start, or is more fun with more people, or when you need an opponent in a game like Chess.)

*Implement Sharing*

Discord is a social platform where users talk to each other. Sharing and invites lets your app live and
engage in those shared spaces, making it visible and accessible to everyone not currently playing.
Things like sharing and invites are important ways to reach into those private, shared spaces and
attract other players.

- The Embedded App SDK allows for sending an image or gif from within an Activity.
  - Share photos or GIFs that capture moments of fun and memorable, or something to brag about. Don't
    make things shareable just to feature the activity.
  - Sharing a high score alone may not be very engaging, but sharing a really good move made in a game,
    or a collaborative drawing that creates a memory is a conversation starter and may make others want
    to join in on the fun.

(Screenshot: "Shared Moment from Chess in the Park".)

*Activities in Text Channels*

- The Activity user interface, copy and user flows should not rely on people in voice to explain,
  organize, clarify, or instruct about how the activity works.
- All controls, CTAs, and instructions should be clear enough that folks (especially first time users)
  playing in a text channel are able to quickly start using the app without needing to talk on voice to
  learn about it.
- Lean on dynamic first-time user experience and "How To Play" instructions, toast messages, Call To
  Action buttons, etc. but be careful to not over-clutter with copy.

**Monetization Considerations**

Upstream notes: "Monetization in Activities will be available soon. Keep the following considerations in
mind as you design your Activity."

- Avoid prohibitive gates in front of participation (e.g. login wall / paywall), especially early in
  the user journey.
- Avoid monetized unlocks that give unfair advantage to other non-paying players or users (i.e. "pay to
  win").
- Take advantage of Discord as a social platform: look for opportunities to offer users customizable
  skins, aesthetic themes, new avatars, etc.

## Design Patterns: game design considerations

**Build games that are easy to learn, hard to master**

- Players can often feel pressure when joining a multiplayer game (voice/video) in the moment if they've
  never played before.
- Games that have a simple quick reference control scheme that are easily approachable help ease
  players into an experience without dropping them into the deep end.
- An easy to understand game loop combined with easy to digest controls tends to work best. If you have
  to go through a tutorial to understand the game then it will be intimidating to join a game in the
  moment.

**Discord users who engage with voice are among Discord's most engaged users**

- Activity engagement and retention increases when users are in a voice call with friends.

**Consider existing game expectations and tropes**

- If you're developing a game, you're more likely to attract users who are gamers.
- Take advantage of existing tropes and expectations for games of the genre you're developing.
- Appeal to the player interests that your game (or game genre) provides, and support those interests as
  a means to get them coming back.

**Activities close when the last participant in the Activity leaves it**

- The next time the Activity is launched, even if it's in the same DM or Voice Channel, it will be a
  different instance and could have different participants.

**If a game is launched, what % of the time do users reach different phases of the game?**

- This includes launch → start, as there can be a large dropoff between these two (especially if you
  don't support solo play or small group sizes).
- This also includes various check points in the game, including what % of sessions that start a game
  reach the end of that game.
- If your Activity has different settings you can start a game with, see if some are more popular or
  more successful — you may want to change your defaults.
  - For non-games, you may want to analyze a certain action instead (such as queueing a video / song
    for a co-watching / co-listening Activity).
- If drop-off is really high at a certain point, see if you can figure out why or change flows.

**How many games are played in a session?**

- More games per session isn't inherently better (you may have an Activity that is meant to be one long
  game), but is a good baseline to understand.
- If you expect to see a lot of repeat plays per session and don't, it can be worth digging in to
  understand more.

**How does the group size impact various key metrics?**

- For example, are larger sessions more or less likely to reach the end of a game? To replay? Etc.
- This can help you catch if your Activity has unexpected weak points in different group sizes — maybe
  the game drags on if there are too many people or isn't compelling enough if there's only two.
- Not every Activity needs to be built for robust group sizes, but if you have the option to play with
  X # of players, it's good practice to make sure that experience is enjoyable for all involved.

## Design Patterns: co-watching and co-listening

- Co-watching and co-listening should be more than just screen-sharing. Consider creative ways to make
  each user's experience impacted by other participants.
- Consider providing host-controls so that playback isn't overly chaotic. If host controls are provided,
  make sure everyone can participate in some way, even if it's just recommending content to the host.
- If content is not available for everyone in the activity (for example, geo-restricted content), make
  sure that information is known when the content is queued and when it's playing. The host is generally
  interested in creating a good experience for their friends. Playback of content should be in sync with
  others in a local channel or call.
- Familiar design patterns can help to get people to participate in your Activity right away. Most
  Discord users are extremely familiar with media browsing (Spotify, YouTube, Netflix, etc.) and will
  immediately understand your content if you follow these patterns.
- Mobile device volume can be controlled by a device's built-in controls (volume buttons on the side of
  the device) and work as expected across desktop, mobile, and browsers.

## Design Patterns: technical considerations

**Developing for the iframe**

- Remember that you need to contend with the Discord Client itself for resources (CPU, RAM and GPU) as
  that client is still fully running while executing your Activity.
- Prioritize time-to-first-interaction.
- Minimize the amount of Web Assembly (WASM) as much as possible in your Activity.
  - Older iOS devices are especially affected by WebKit's optimization compilation pass of WASM that
    occurs during the first few minutes of usage of an Activity. To varying degrees, this will cause
    noticeable stutters, device thermal issues, and possibly degraded Discord AV quality during those
    early minutes.
- All network traffic is routed through the Discord Proxy for various security reasons.
- Create multiple versions of your Activity in the Developer Portal for less and more stable development
  versioning (e.g. Development, Staging, Production). This allows you to show and test the last stable
  build while also having development and staging environments.

**Developing in Unity**

Developing for the iframe in Unity is possible, but will likely require extensive min/maxing of all
facets of your game to meet performance and quality standards. Other, web-first, game engines are
generally more performant out of the box.

## Design Patterns: quality and testing

**Verify User Interface and User Experience**

- Ensure all buttons and UI elements function correctly without any blocking issues for standard
  Activity use or gameplay.
- Test Discord usernames handling, ensuring they display appropriately based on the chosen format
  (Discord username or server identity).

**Test for Performance**

- Evaluate performance to ensure it is satisfactory for the majority of users across phones, tablets,
  and desktop machines and across multiple operating systems.
- Lag or slowness should not significantly impact the Activity or gameplay experience.

**Test for Audio**

- Check that sound effects and background music work as intended, with volume settings functioning
  correctly.
- Being able to hear when playing on a voice call is important.

**Validate Activity Controls**

- Confirm that all game controls, including clicks, drag, key controls, swiping, and hovers, work as
  expected and are suitable for the platform.
- Test in-app tutorials and instructions for accuracy and relevance to the current activity
  functionality and user platform (desktop or mobile).

**Mobile Device UI Considerations**

- Watch out for potential issues on devices with top notches or cameras in specific corners that may
  hide or cut off UI elements and buttons, rendering them untappable.
- Be mindful of Android curved screen edges that could obscure or make elements and buttons
  inaccessible.
- Take into account iOS/Android swipe gestures that may interfere with UI elements or buttons located at
  the bottom of the screen.
- Ensure that Android devices with a back button do not overlap with elements or buttons at the bottom
  of the screen, preventing users from tapping them.
- Respect the safe area defined by the platform to prevent any buttons or content from being cut off or
  non-functional.

**Desktop Accessibility Guidelines**

- Enable users to cycle through Discord buttons and fields on desktop by pressing TAB repeatedly,
  ensuring that the activity does not capture control.
- Implement the functionality for the ESC key to close any open in-activity modals, providing a
  consistent user experience.
- Opt for color-blind friendly colors with high contrast, especially for crucial game elements that need
  to be distinguishable based on color.
- Avoid using similar colors for objects that are essential for gameplay but differ only in color, as
  this may pose challenges for color-blind users.

## Source

Discord Developer Documentation, retrieved 2026-08-26:

- `https://docs.discord.com/developers/activities/how-activities-work`
- `https://docs.discord.com/developers/activities/overview`
- `https://docs.discord.com/developers/platform/activities`
- `https://docs.discord.com/developers/activities/design-patterns`
