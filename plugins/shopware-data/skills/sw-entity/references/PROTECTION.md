# Shopware 6 — Entity/field protection

Controls which fields and entities are readable or writable through which API source (Admin/Store).

- `ApiAware` (no flag = not exposed via API): marks API visibility, optionally per source
  `new ApiAware(SalesChannelApiSource::class)`.
- `WriteProtected` / `ReadProtected`: write/read protection per scope (only the system may write, for example).
- Deliberately leave sensitive internal fields (tokens, flags) **without** `ApiAware`.

```php
(new StringField('secret', 'secret'))->addFlags(new WriteProtected(Context::SYSTEM_SCOPE)),
```

This keeps internal data out of the Admin and Store API without a separate entity. Complement it with ACL for admin permissions (`shopware-framework` → `sw-api-acl`).

→ Protection details: [PROTECTION-DETAIL.md](PROTECTION-DETAIL.md)
