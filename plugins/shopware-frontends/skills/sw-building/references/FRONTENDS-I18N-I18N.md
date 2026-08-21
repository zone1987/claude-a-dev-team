# Shopware Frontends – Internationalisation (i18n)

Source: `apps/docs/src/getting-started/languages.md`

---

## Contents

- [Two sources of translations](#two-sources-of-translations)
- [Configuration with `@nuxtjs/i18n`](#configuration-with-nuxtjsi18n)
- [Building URLs with a language prefix](#building-urls-with-a-language-prefix)
- [Switching the language](#switching-the-language)
- [localeId – diverging language codes](#localeid--diverging-language-codes)
- [Reverse proxy environments](#reverse-proxy-environments)
- [Multi-domain example](#multi-domain-example)

## Two sources of translations

| Source | Contains |
|--------|---------|
| **Backend (Shopware)** | CMS translations, products, categories, routing paths |
| **Frontend (vue-i18n)** | All static UI texts |

> **Important:** backend language codes and frontend language codes must match!

---

## Configuration with `@nuxtjs/i18n`

### Same-domain strategy (recommended)

```
www.example.com          // GB (default)
www.example.com/de-DE    // DE
```

```ts
// nuxt.config.ts
{
  i18n: {
    vueI18n: {
      fallbackLocale: "en-GB",
    },
    strategy: "prefix_except_default",
    defaultLocale: "en-GB",
    langDir: "i18n/src/",
    locales: [
      { code: "en-GB", iso: "en-GB", file: "en-GB.ts" },
      { code: "de-DE", iso: "de-DE", file: "de-DE.ts" },
    ],
  },
}
```

### Multi-domain strategy

```
www.example1.com   // GB
www.example2.com   // DE
```

```ts
{
  i18n: {
    langDir: "i18n/src/",
    locales: [
      { domain: "example1.com", code: "en-GB", iso: "en-GB", file: "en-GB.ts" },
      { domain: "example2.com", code: "de-DE", iso: "de-DE", file: "de-DE.ts" },
    ],
  },
}
```

---

## Building URLs with a language prefix

With the `prefix` strategy: use `formatLink()` from `useInternationalization` so that the language prefix is set correctly.

```vue
<script setup lang="ts">
const localePath = useLocalePath();
const { formatLink } = useInternationalization(localePath);
</script>
<template>
  <NuxtLink :to="formatLink('/account')">Account</NuxtLink>
</template>
```

---

## Switching the language

```ts
const onChangeHandler = async (option: Event) => {
  const data = await changeLanguage((option.target as HTMLSelectElement).value);

  if (data.redirectUrl) {
    window.location.replace(replaceToDevStorefront(data.redirectUrl));
  } else {
    window.location.reload();
  }
};
```

### Local dev environment: solving the redirect problem

After a language switch the backend URL redirects to the configured storefront domain – not to localhost.

**Option A: dev resolver in the app**

```ts
const dev = process.dev;

const onChangeHandler = async (option: Event) => {
  const data = await changeLanguage((option.target as HTMLSelectElement).value);

  if (dev) {
    locale.value = getLanguageCodeFromId((option.target as HTMLSelectElement).value);
    window.location.replace(`${window.location.origin}/${locale.value}`);
    return;
  }

  if (data.redirectUrl) {
    window.location.replace(replaceToDevStorefront(data.redirectUrl));
  } else {
    window.location.reload();
  }
};
```

**Option B: override the hosts file**

```
# Windows: C:\Windows\System32\drivers\etc
# macOS/Linux: /etc/hosts
127.0.0.1    yourDomainFromBackend.com
::1          yourDomainFromBackend.com
```

### Local testing with an environment variable

```bash
NUXT_PUBLIC_SHOPWARE_DEV_STOREFRONT_URL=http://127.0.0.1:3000
```

---

## localeId – diverging language codes

When the frontend prefix and the backend language code diverge (e.g. `testde` vs. `de-DE`):

```ts
locales: [
  { code: "en-GB", iso: "en-GB", file: "en-GB.ts" },
  {
    code: "testde",       // frontend prefix
    iso: "de-DE",
    file: "de-DE.ts",
    localeId: "c19b753b5f2c4bea8ad15e00027802d4",  // backend language ID from the Shopware admin
  },
],
```

The `localeId` corresponds to the language ID in the Shopware Administration → **Einstellungen** (Settings) → **Sprachen** (Languages).

---

## Reverse proxy environments

With Cloudflare, Fastly, Vercel and other proxies:

### Understanding language detection

- `@nuxtjs/i18n` detects the language via the URL prefix or the `Accept-Language` header
- `detectBrowserLanguage: false` → URL-based detection only
- Two URL strategies: `prefix_except_default` or `prefix_and_default`

### The `x-forwarded-host` header

The i18n module reads `x-forwarded-host` for domain detection – relevant in a reverse proxy setup.

### Avoiding caching problems

- The cache should differentiate based on the URL structure or `Accept-Language`
- Purge the proxy cache after deploying new language configurations

---

## Multi-domain example

GitHub example: https://github.com/shopware/frontends/tree/main/examples/i18n-multi-domain

*Must be run locally because of the multi-domain requirements*
