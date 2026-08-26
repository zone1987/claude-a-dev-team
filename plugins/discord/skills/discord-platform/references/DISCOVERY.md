# Discord App Discovery

Complete extraction of the three `discovery/*` pages, retrieved 2026-08-26:

- `https://docs.discord.com/developers/discovery/overview`
- `https://docs.discord.com/developers/discovery/enabling-discovery`
- `https://docs.discord.com/developers/discovery/best-practices`

The `platform/discovery` platform page is a shorter introduction to the same subject; it is recorded
in `PLATFORM-FEATURES.md`.

## Contents

- [Scope](#scope)
- [Discovery Overview](#discovery-overview)
  - [App Directory](#app-directory)
  - [App Launcher](#app-launcher)
  - [App Launcher collections](#app-launcher-collections)
  - [Search ranking and marker tags](#search-ranking-and-marker-tags)
  - [Editorial recommendations](#editorial-recommendations)
  - [Social discovery](#social-discovery)
- [Enabling Discovery](#enabling-discovery)
  - [Step 1: Verify your app](#step-1-verify-your-app)
  - [Step 2: Opt into Discovery](#step-2-opt-into-discovery)
  - [The 24 hour delay](#the-24-hour-delay)
  - [Search for your app in Discord](#search-for-your-app-in-discord)
- [Discovery Best Practices](#discovery-best-practices)
  - [The three description fields and their character limits](#the-three-description-fields-and-their-character-limits)
  - [Show your story: visuals](#show-your-story-visuals)
  - [Find your users: tags](#find-your-users-tags)
  - [Support your users: the support server](#support-your-users-the-support-server)
  - [General housekeeping: the final compliance checklist](#general-housekeeping-the-final-compliance-checklist)
- [Every requirement and limit in one table](#every-requirement-and-limit-in-one-table)
- [Every Developer Portal path this subject uses](#every-developer-portal-path-this-subject-uses)

## Scope

**App discovery applies to Bots and Activities.** (Upstream carries this as an `Info` callout on the
overview page.)

## Discovery Overview

The overview page covers the discovery surfaces available to your app and how they work in detail.

### App Directory

Once you have enabled discovery for your app, users can find it in the **App Directory** — a
**searchable hub where they can browse by name, category, or collection**.

- **Search**: Users can search for your app by name and install it.
- **App Directory Product Page**: Share information about your app, including **descriptions, images,
  videos, and links**.

Image caption: "Your Discord App Profile".

The App Directory lives at `https://discord.com/discovery/applications` (the `platform/discovery` page
gives this URL) and is searchable at `https://discord.com/application-directory` (the
`enabling-discovery` page gives this URL).

### App Launcher

The App Launcher lets users discover apps **through collections and search** from the **app shapes
icon** throughout Discord.

Image caption: "App Launcher in Discord".

### App Launcher collections

**Five collection kinds**, exactly as upstream lists them:

| Collection | What it contains |
| --- | --- |
| **Recent Apps** | Apps you've recently used or installed — these appear **at the top** of the App Launcher. |
| **Installed Apps** | Apps already added to your account or server (if applicable). |
| **Curated Collections** | A mix of **user favorites, staff picks, and recommended apps**. |
| **Partner Apps** | Some apps may be developed **in collaboration with Discord**, marked with a **"Partner"** tag. |
| **Promoted Apps** | Apps given more visibility in the App Launcher or App Directory, identified by a **"Promoted"** tag. |

### Search ranking and marker tags

- **Search results are ranked based on relevance to the query and popularity based on usage.**
- Apps that **use ads** are marked with an **"Ad-supported"** tag on their details page.
- Apps that **offer in-app purchases** are marked with an **"In-App Purchases"** tag on their details
  page.

Four tags in total appear in discovery surfaces: `Partner`, `Promoted`, `Ad-supported`,
`In-App Purchases`.

### Editorial recommendations

Apps can be featured in the App Directory or App Launcher as part of a **curated collection or
promotion**. **Discord's editorial team will reach out to you** if they are interested in featuring
your app — there is no application path stated.

### Social discovery

Once your app is discoverable, users may find it through **social interactions** in Discord. When your
app is used in a server, **it may be visible to other users**, allowing them to learn more about it and
**install it themselves from your app's profile**.

#### Sharing links

Create **shareable links to your app's profile page, store page, or specific items**. Share these links
**in Discord, emails, or on your website**.

Image caption: "A shared embed link in Discord for the Sandscape app".

#### Rich Presence

Use **Rich Presence** to show what users are doing in your app, **driving more users to discover it**.
See `PLATFORM-FEATURES.md` for the Rich Presence platform page.

Image caption: "Examples of Rich Presence data on Discord user profiles".

### Next steps from the overview page

The overview page ends with two cards: **Enabling Discovery** ("Enable discovery for your app to make
it available in the App Directory and App Launcher") and **Discovery Best Practices** ("Learn how to
make your app stand out and drive more users to discover it").

## Enabling Discovery

Enabling **Discovery** for your app makes it available in the **App Directory** and **App Launcher**
for users to search for and install.

### Step 1: Verify your app

**To enable Discovery for your app, Discord requires your team owner to complete identity and
application verification.**

**App Verification also allows you to add monetization features to your app**, such as in-app purchases
and subscriptions.

To see the list of requirements for App Verification, the four upstream steps:

1. Visit the **Developer Portal** (`https://discord.com/developers/applications`) and select your app.
2. Select **App Verification** from the left-hand menu to see the requirements for verification
   (`https://discord.com/developers/applications/select/verification-onboarding`).
3. **Complete the listed App Verification qualification criteria** for your app.
4. Once you've completed the requirements, **you can submit your app for verification**.

Upstream does **not** enumerate the individual verification criteria on this page — it states that the
list is shown in the Developer Portal under App Verification, and points at the help centre article
"How Do I Get My App Verified" (`https://support-dev.discord.com/hc/en-us/articles/23926564536471`).
**Recorded as silent: the specific verification criteria are not stated in the documentation.**

### Step 2: Opt into Discovery

**After** you've verified your app, you can opt into Discovery in the Developer Portal, which will make
your app available in the App Directory and App Launcher.

The five upstream steps:

1. Visit the **Developer Portal** (`https://discord.com/developers/applications`) and select your app.
2. Select **Discovery -> Discovery Status** from the left-hand menu to see the requirements for
   enabling discovery (`https://discord.com/developers/applications/select/discovery/status`).
3. **Complete the listed Discovery qualification criteria** for your app.
4. **Add your app metadata and images** under the **Discovery -> Discovery Settings** menu
   (`https://discord.com/developers/applications/select/discovery/settings`) to customize your app's
   appearance in discovery surfaces.
5. Once you've completed the requirements, **you can enable Discovery for your app**.

Again the specific qualification criteria are **shown in the Developer Portal, not listed in the
documentation**. Upstream points at the help centre article "How Can Users Discover and Play My
Activity" (`https://support-dev.discord.com/hc/en-us/articles/21204493235991`).

### The 24 hour delay

**Once you enable Discovery, it may take up to 24 hours for your app to appear in the App Directory
and App Launcher.** (Upstream carries this as an `Info` callout.)

### Search for your app in Discord

To check if your app is discoverable, search for it in the App Directory or App Launcher:

1. Head to the **App Directory** (`https://discord.com/application-directory`) and search for your app
   **by name**.
2. **If you see it, you're good to go.**
3. **If not**, make sure you've completed all the steps above and **wait up to 24 hours** for your app
   to appear.

## Discovery Best Practices

Upstream frames this page as tips from Discord Staff to help boost performance of your **App Directory
Product Page**, whether you are about to opt in or already listed and not seeing the traction you want.
Every setting referenced is in your app's settings at `https://discord.com/developers/applications`; if
you don't have an app yet, upstream points at the Getting Started guide.

### The Elevator Pitch

**Quickly tell your users what your app does.** App descriptions should **convey the value of your app
and what it does**. Make descriptions **punchy and to the point** — letting folks know what your app
does in **simple terms** while also **exciting the potential user** to add the app and start using it.

**Spell check and review your grammar before posting your descriptions.** Upstream's reason: your app
has the potential to be seen by millions of people.

### The three description fields and their character limits

| Field | Portal location | Max length | Where it appears |
| --- | --- | --- | --- |
| **Description** (App General Information Description) | **General Information** tab (`/applications/select/information`) | **400 characters** | Within your **bot user's profile**. When a new user clicks on your app within Discord, they see this description. |
| **Summary** (App Summary) | **App Directory** tab (`/applications/select/discovery`) | **200 characters** | What users see when you appear **within search results** on the App Directory. |
| **Expanded Description** | **App Directory** tab, **near the bottom** of the page | Upstream states **no limit** for this field | Appears when someone **clicks on your app and enters its profile** within the App Directory. **Supports formatting via markdown.** |

Image captions on this page: "App description on the General Information tab"; "Poorly-written app
Summary on the App Directory tab"; "Well-written app Summary on the App Directory tab".

#### How to write the Summary

Think about **how to grab the user's attention and quickly convey the value of your app**. Upstream
contrasts a bad and a good example (both images): the bad one "could be true" but "doesn't really tell
folks how the app makes servers better or more fun". **The best descriptions start with an
attention-grabbing sentence that describes a problem a user might want to solve.**

#### How to write the Expanded Description

This is your opportunity to **showcase why a user should install your app, and the best functionality
your app has to offer**. The stated order: **first convey the value of the app to users; after the
value is clear, continue on with how to get started with your app after it's installed.**

### Show your story: visuals

**Include as many relevant visuals as possible.**

#### Show your app's functionality

Add **images and gifs** to your Product Page to give users a better idea of the functionality of your
app. Upstream's suggested starting point: **show off some of the commands you mentioned in your
description and how they work in Discord.** The questions to answer — **What are some of your app's
most popular commands? How do existing users generally interact with your app?**

Additionally, **new users need to know what to expect when they install the app**, so great images
should **showcase your app in action within a Discord server**. **The more your images display what
your app does and how it appears in Discord, the better.**

#### Include your app's lore

Other images you may want to include are ones related to **your app's lore** (if any). Upstream's own
example: for a hypothetical "Hypesquad App", include the Hypesquad badges and what each of them means.

#### Add a video

After adding some images, **make a quick screen recording to demonstrate your app's functionality**.
**Videos are awesome but it's definitely helpful to include images as well**, especially for folks who
may not watch the entire video.

### Find your users: tags

**Utilize search to your advantage.** Think of **up to five words that describe your app and add them
as tags**. Consider **what categories your app would fit under** or **what keywords users would type
into the search bar** when looking for apps to add to their servers.

Image caption: "App tags which help categorize apps and make them more searchable".

### Support your users: the support server

**Engage with your users directly.** Your app's **support server is a paramount part of your App
Product Page**. It is important to ensure your app has a **dedicated server and channel for
communication between your app's users and its developers and maintainers**.

**If your support server isn't discoverable, be sure to include an invite link in the "links" section
of your App Directory Product Page.** (Upstream carries this as an `Info` callout and links Discord's
"Enabling Server Discovery" help centre article.)

Three ways upstream names to use your support server successfully:

- **Encourage users to share feedback** or their experience with your app.
- **Offer technical support** for users of your app.
- **Share app updates in your support server, and update your App's Product Page description if it
  changes the functionality of your app.**

For general best practices on how to run a server, upstream points at `https://discord.com/community`.

### General housekeeping: the final compliance checklist

**Final checks to make sure you're ready to go.** Before you can click the final **"Enable Discovery"**
button, ensure that your App Directory Product Page complies with **all four** of the following:

1. **The rest of Discord's Directory eligibility criteria.**
2. **App content requirements** — the App Directory App Content Requirements Policy
   (`https://support-dev.discord.com/hc/en-us/articles/9489299950487`).
3. **Developer Terms of Service** (`https://support-dev.discord.com/hc/en-us/articles/8562894815383`).
4. **Developer Policy** (`https://support-dev.discord.com/hc/en-us/articles/8563934450327`).

For more details about what this information entails, upstream points at the help centre article on
App Directory app profile pages
(`https://support-dev.discord.com/hc/en-us/articles/6378525413143`).

Upstream closes by inviting you to join the official Discord Developers server
(`https://discord.gg/discord-developers`) to receive more information on how to update your apps.

## Every requirement and limit in one table

| Requirement or limit | Value | Source page |
| --- | --- | --- |
| Team owner completes **identity verification** | Mandatory before Discovery | enabling-discovery |
| Team owner completes **application verification** | Mandatory before Discovery | enabling-discovery |
| App Verification qualification criteria | Listed in the Developer Portal, **not** in the docs | enabling-discovery |
| App submitted for verification | Required, after criteria are met | enabling-discovery |
| Discovery qualification criteria | Listed in the Developer Portal, **not** in the docs | enabling-discovery |
| App metadata and images added | Under Discovery -> Discovery Settings | enabling-discovery |
| Discovery enabled in the portal | The final action | enabling-discovery |
| Time to appear in App Directory / App Launcher | **Up to 24 hours** | enabling-discovery |
| General **Description** max length | **400 characters** | best-practices |
| **Summary** max length | **200 characters** | best-practices |
| **Expanded Description** | Markdown supported, no stated length limit | best-practices |
| Tags | **Up to five words** | best-practices |
| Support server | Dedicated server and channel; invite link in "links" if not discoverable | best-practices |
| Directory eligibility criteria compliance | Required before "Enable Discovery" | best-practices |
| App content requirements policy compliance | Required | best-practices |
| Developer Terms of Service compliance | Required | best-practices |
| Developer Policy compliance | Required | best-practices |
| App types eligible | **Bots and Activities** | overview |
| Monetization side effect of verification | App Verification also unlocks in-app purchases and subscriptions | enabling-discovery |

## Every Developer Portal path this subject uses

| Path | Purpose |
| --- | --- |
| `https://discord.com/developers/applications` | Select your app. |
| `/applications/select/verification-onboarding` | App Verification requirements. |
| `/applications/select/discovery/status` | Discovery Status — the requirements for enabling discovery. |
| `/applications/select/discovery/settings` | Discovery Settings — app metadata and images. |
| `/applications/select/information` | General Information tab — the 400-character Description. |
| `/applications/select/discovery` | App Directory tab — Summary, Expanded Description, tags. |
| `https://discord.com/application-directory` | The user-facing App Directory search. |
| `https://discord.com/discovery/applications` | The App Directory (URL given on the `platform/discovery` page). |

## Source

Discord Developer Documentation, retrieved 2026-08-26:
`https://docs.discord.com/developers/discovery/overview`,
`https://docs.discord.com/developers/discovery/enabling-discovery`,
`https://docs.discord.com/developers/discovery/best-practices`.
