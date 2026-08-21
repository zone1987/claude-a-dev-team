# Shopware 6 – API access (access key)

An API access key is generated per Verkaufskanal (Sales channel).

## Where

**Verkaufskanal > "API-Zugang" (API access) section**

## Function

- Unique API key for the Sales Channel (Store) API
- Allows third-party systems (apps, PWA, mobile) to access shop data
- Every channel has its own key → requests are channel-specific

## Important

- The key is visible only once → secure it immediately
- If compromised: generate a new key (the old one becomes invalid)
- Headless channel: API access is used internally by extensions

## Source

https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
