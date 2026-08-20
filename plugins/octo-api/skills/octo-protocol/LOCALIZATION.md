# Localization

Suppliers store content in several languages. Which one you get is negotiated per request.

## Contents

- [Requesting a language](#requesting-a-language)
- [Caching translated content](#caching-translated-content)
- [What gets translated](#what-gets-translated)
- [Time zones are separate](#time-zones-are-separate)

## Requesting a language

Send `Accept-Language` with standard HTTP syntax — ideally passing through the preference list the
user's browser sent, quality values included:

```http
Accept-Language: fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5
```

The API matches your preference list against the languages the supplier has actually translated, and
answers with `Content-Language` naming the language it resolved to:

```http
Content-Language: fr
```

A request for an untranslated language **falls back rather than failing** — typically to English. So
compare `Content-Language` against what you asked for instead of assuming you got it.

Localized product content is requested through the ordinary product endpoint:
`GET /products/{productId}` with the header set. **`Accept-Language` is required on that endpoint**,
optional elsewhere.

## Caching translated content

`Octo-Available-Languages` in every response lists the languages the supplier has translated. That
header is the intended basis for a cache:

> If you cache content locally, use the `Octo-Available-Languages` header, which lists languages
> translated by the supplier. You can repeat the request with each available language to retrieve
> localized content.

So the documented pattern for a multilingual catalogue is: read the available languages once, then
fetch the product once per language. There is no endpoint that returns every translation at once.

## What gets translated

- **Supplier content** — product and option titles, descriptions and the other `octo/content`
  fields.
- **`errorMessage`** — the human-readable half of a `400` body. The `error` code never changes,
  which is why matching on `error` and never on `errorMessage` is the only safe approach.

`Product.locale` reports the product's own locale, independent of the language you requested.

## Time zones are separate

Language negotiation says nothing about time. `Product.timeZone` is an IANA zone such as
`Europe/London`, and availability identifiers are local times with an offset
(`2020-01-01T10:30+08:00`). Never normalise an `availabilityId` to UTC before sending it back — pass
through the exact string you received.

## Source

[docs.ventrata.com/getting-started/localization](https://docs.ventrata.com/getting-started/localization)
and `getting-started/headers`, retrieved 2026-08-20. Header syntax follows the HTTP standard; see
[MDN on Accept-Language](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Language).
