# Shopware 6 – SEO settings & sitemap – complete reference

Sources:
- https://docs.shopware.com/de/shopware-6-de/einstellungen/seo
- https://docs.shopware.com/de/shopware-6-de/einstellungen/sitemap

---

## Contents

- [SEO URL templates](#seo-url-templates)
- [Redirect (HTTP 301)](#redirect-http-301)
- [Rebuilding the SEO index](#rebuilding-the-seo-index)
- [Canonical URLs](#canonical-urls)
- [Sitemap](#sitemap)

## SEO URL templates

**Path:** Einstellungen (Settings) > Shop > SEO-Einstellungen (SEO settings)

### Sales channel selection
Configurations can be made globally for all channels or per channel.

---

### Product detail page
Twig syntax for URL templates: `{{ product.name }}`

**Available variables:**
| Variable | Meaning |
|---|---|
| `{{ product.productNumber }}` | Product number |
| `{{ product.name }}` | Product name |
| `{{ product.ean }}` | EAN code |
| `{{ product.manufacturer.name }}` | Manufacturer name |
| `{% for part in product.categories.sortByPosition().first.breadcrumb %}` | Category breadcrumb |

**Particularities:**
- Multi-level variables require manual completion
- Length restriction: `{{ product.translated.name[:50] }}`
- Conditional logic: IF queries are possible
- Validation indicator: green check mark = correct, red X = error

**Twig filters (pipe operator):**
```twig
{{ product.translated.name|lower }}
```

---

### Landing page
| Variable | Meaning |
|---|---|
| `{{landingPage.name}}` | Name of the landing page |
| `{{landingPage.metaTitle}}` | Meta title |
| `{{landingPage.url}}` | URL |
| `{{landingPage.active}}` | Active status |

> Prerequisite: at least one landing page must exist.

---

### Category page
| Variable | Meaning |
|---|---|
| `{{ category.seoBreadcrumb }}` | Breadcrumb path |
| `{{ category.translated.name }}` | Translated category name |
| `{{ category.translated.metaTitle }}` | Translated meta title |
| `{{ category.parentId }}` | Parent category |

**Example with a filter:**
```twig
{% for part in category.seoBreadcrumb %}{{ part|lower }}{% endfor %}
```

---

## Redirect (HTTP 301)

Option: activate automatic redirects when URLs change (instead of only canonical links).

---

## Rebuilding the SEO index

After template changes a rebuild is required:
```bash
php bin/console dal:refresh:index
```

---

## Canonical URLs

- Identify the preferred page to search engines in the case of duplicated content
- Can use different domains
- Minor variations (sorting, filters) are ignored

---

## Sitemap

**Path:** Einstellungen > Shop > Sitemap  
**Available from:** 6.1.0

### Basic principle
Shopware creates a machine-readable `sitemap.xml` for search engines.  
Available at: `https://mydomain.com/sitemap.xml`

For large shops the file is split automatically (index + partial sitemaps).

### Configurable options
- Refresh time for the sitemap
- Refresh strategy

### Three refresh strategies

| Strategy | Description |
|---|---|
| **Geplant** (Scheduled) | Automatic generation via a scheduled task |
| **Live** | New sitemap when the cache is missing or expired |
| **Manuell** (Manual) | Automatic generation disabled; manual generation via CLI |

**Manual command:**
```bash
php bin/console sitemap:generate
```
> Must be run again after every URL change.

### Notes
- Shopware cannot guarantee that every URL is indexed
- For custom URLs: consult the developer documentation
