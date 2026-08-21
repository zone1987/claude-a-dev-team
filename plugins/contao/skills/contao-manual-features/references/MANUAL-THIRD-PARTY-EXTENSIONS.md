# Contao 5.x – Third-party extensions

Complete reference from the Contao 5.x manual (German).

---

## Contents

- [1. Animated Timeline (`pdir/animated-timeline-bundle`)](#1-animated-timeline-pdiranimated-timeline-bundle)
- [2. EasyThemes (`terminal42/contao-easy_themes`)](#2-easythemes-terminal42contao-easy_themes)
- [3. Isotope eCommerce (`isotope/isotope-core`)](#3-isotope-ecommerce-isotopeisotope-core)
- [4. Maklermodul for estate agents (`pdir/maklermodul-bundle`)](#4-maklermodul-for-estate-agents-pdirmaklermodul-bundle)
- [5. Merger² (`contao-community-alliance/merger2`)](#5-merger²-contao-community-alliancemerger2)
- [6. MetaModels](#6-metamodels)
- [7. News Facebook Sync (`inspiredminds/contao-news-facebook`)](#7-news-facebook-sync-inspiredmindscontao-news-facebook)
- [8. Further extensions mentioned](#8-further-extensions-mentioned)

## 1. Animated Timeline (`pdir/animated-timeline-bundle`)

**Vendor:** pdir GmbH

**Description:** jQuery extension for Contao 4 for presenting content in a dynamic timeline with fade-in animations.

**Main features:**
- Horizontal and vertical timeline orientations
- Responsive design: horizontal on the desktop, vertical on mobile devices
- Fade-in animations

**Documentation:** https://docs.pdir.de/#/animated-timeline/index

---

## 2. EasyThemes (`terminal42/contao-easy_themes`)

**Vendor:** terminal42 gmbh

**Description:** direct access to stylesheets, modules, page layouts and image sizes with fewer clicks – especially useful with several themes.

**Installation and activation:**
1. Backend → Benutzerverwaltung (User Management) → edit a Benutzer (user)
2. In the last section: tick "EasyTheme aktivieren" (Activate EasyTheme)

**Configuration — active modules:**
- Edit theme
- Stylesheets
- Frontend modules
- Seitenlayouts (Page layouts)
- Image sizes

**Note:** the internal CSS editor is deprecated and will be removed in a future Contao version.

**Display modes:**
| Mode | Description |
|-------|-------------|
| Context menu | Appears on right-clicking themes |
| Mouseover | Appears when hovering over the themes |
| DOM inject | Displayed directly below the themes |
| Backend module | Creates an additional backend module (optional reference group) |

---

## 3. Isotope eCommerce (`isotope/isotope-core`)

**Vendor:** terminal42 gmbh

**Description:** free eCommerce solution for the Contao CMS.

**Its own user manual:** https://docs.isotopeecommerce.org/manual/de/

---

## 4. Maklermodul for estate agents (`pdir/maklermodul-bundle`)

**Vendor:** pdir GmbH (paid)

**Description:** specialised module for estate agents for managing property listings and customer interactions in Contao.

**Project website:** https://maklermodul.de
**Documentation:** https://docs.pdir.de/#/maklermodul/index

---

## 5. Merger² (`contao-community-alliance/merger2`)

**Vendor:** Contao Community Alliance (CCA)

**Description:** frontend module for condition-based content display and merging. Supports articles, pages and other frontend modules.

**Main use cases:**
- **Content consolidation:** display language-specific modules conditionally (e.g. by browser language) — reduces layout variants
- **Conditional display:** show modules/articles only under certain criteria (page depth, mobile view, browser language)
- **Article inheritance:** automatic passing of articles from parent pages to child pages in the page tree

**Detailed configuration:** https://github.com/contao-community-alliance/merger2/wiki

---

## 6. MetaModels

**Vendor:** MetaModels team

**Description:** extension for structured data entry and output in various formats. No programming knowledge required.

**Fields of application:**
- Product catalogues
- Events
- Menus and meal plans
- Address and staff directories
- Property listings
- Image galleries
- Multilingual content management

**Features:**
- List and detail view
- Filtering, sorting, pagination
- Multilingual support

**Package:** https://packagist.org/packages/metamodels/
**Manual:** https://metamodels.readthedocs.io/de/latest/

---

## 7. News Facebook Sync (`inspiredminds/contao-news-facebook`)

**Vendor:** INSPIRED MINDS (paid, from v9.0)

**Description:** automatic synchronisation between Facebook pages/groups and Contao news archives. Import of Facebook posts as news items and publication of Contao news on Facebook.

### Installation

Adjust `composer.json`:
```json
{
  "repositories": [
    {
      "type": "composer",
      "url": "https://<USERNAME>:<TOKEN>@packeton.inspiredminds.at"
    }
  ],
  "require": {
    "inspiredminds/contao-news-facebook": "^9.0"
  }
}
```

### Creating a Facebook app (optional)

1. developers.facebook.com → create an app
2. Use case: "Other", type: "Business"
3. Add "Facebook Login for Business"
4. Redirect URI: `https://example.org/_facebook/callback`

### Configuring the app credentials (optional, if there is no integrated app)

`config/config.yaml`:
```yaml
contao_news_facebook:
    app_id: '%env(FACEBOOK_APP_ID)%'
    app_secret: '%env(FACEBOOK_APP_SECRET)%'
```

`.env.local`:
```
FACEBOOK_APP_ID=123456789123456
FACEBOOK_APP_SECRET=abc123...
```

### Configuring the news archive

1. Open the news archive
2. Enable "Facebook-Sync"
3. Enter the numeric Facebook page ID
4. Enable "Seitenbeiträge abrufen" (Retrieve page posts) (optional: date limits)
5. "Facebook verbinden" (Connect Facebook) for token authorisation
6. Configure the image download folder (default: `files/facebook_images`)

### Additional system settings
- **Disable OpenGraph metatags**: prevents automatic `og:image` tags on shared articles
- **Post as photos**: re-enable if articles with a teaser image should be posted as a photo

**Configuring the headline length:**
```yaml
contao_news_facebook:
    headline_length: 64
```

### Usage

- **Retrieving Facebook posts**: hourly via the Contao cronjob
- **Publishing to Facebook**: when "Auf Facebook-Seite posten" (Post to Facebook page) is enabled in the article; checked every minute
- **Synchronising manually**: button in the global operations of the news archives

### Hooks

**`processFacebookPost`:** adjusts the conversion of Facebook posts into Contao items.

**`changeFacebookMessage`:** changes the message text before the Facebook post.

```php
#[AsHook('changeFacebookMessage')]
class ChangeFacebookMessageListener
{
    public function __invoke(string $message, $news, $archive): string
    {
        if ($news->addImage && $news->fbPostAsPhoto) {
            $message .= "\n\n".$this->generator->generate($news, [], 1);
        }
        return $message;
    }
}
```

### Template data

Templates receive additional variables:
- `fbData` – original data of the Facebook post
- `fbPostId` – associated Facebook post ID
- `fromFb` – boolean: Facebook origin

---

## 8. Further extensions mentioned

**News Sync** (`inspiredminds/contao-news-sync`): paid extension for synchronising news articles between Contao installations.

**Social Feed**: displays feeds from Facebook and Instagram.

---

Sources:
- https://docs.contao.org/5.x/manual/en/extensions/
- https://docs.contao.org/5.x/manual/en/extensions/animated-timeline/
- https://docs.contao.org/5.x/manual/en/extensions/contao-easy_themes/
- https://docs.contao.org/5.x/manual/en/extensions/isotope-core/
- https://docs.contao.org/5.x/manual/en/extensions/maklermodul/
- https://docs.contao.org/5.x/manual/en/extensions/cca-merger2/
- https://docs.contao.org/5.x/manual/en/extensions/metamodels/
- https://docs.contao.org/5.x/manual/en/extensions/news-facebook-sync/

## Social Feed

**Package:** `pdir/social-feed-bundle`, by pdir GmbH.

Shows a user feed from Facebook and Instagram. The posts are written **directly into the database**,
created as news items, and then displayed with the **news list** module type.

The manual page carries nothing further: no backend module, no configuration field, no front-end
module of its own, no setup steps, no caveat or version note. It points at `docs.pdir.de` for
detailed instructions. Recorded as absent rather than guessed.

Source: https://docs.contao.org/5.x/manual/en/extensions/social-feed/

---
