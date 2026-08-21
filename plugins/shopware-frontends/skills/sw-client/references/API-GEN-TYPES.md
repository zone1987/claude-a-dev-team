# Shopware Frontends — @shopware/api-gen

Generates TypeScript types (`operations`, `Schemas`) from the shop's OpenAPI spec — the foundation of the type
safety of the `api-client`.

```bash
# Load the schema from the shop (Store API, APP_ENV=dev) and generate types
npx @shopware/api-gen loadSchema --apiType=store --url=https://shop.example.com
npx @shopware/api-gen generate --apiType=store
```

Produces e.g. `api-types/storeApiTypes.d.ts`, wired into the project as the `#shopware` alias. With installed plugins
that have their own Store API routes, reload the schema so that their endpoints are typed (reference: `shopware-api` →
`sw-api-catalog`/`sw-store-api-route`). `--apiType=admin` for admin types.

→ Complete reference: [API-GEN-TYPES-API-GEN-REFERENCE.md](API-GEN-TYPES-API-GEN-REFERENCE.md)
