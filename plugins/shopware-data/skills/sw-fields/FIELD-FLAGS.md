# Shopware 6 — Field flags

Flags control a field's behaviour and visibility: `->addFlags(new Required(), new ApiAware())`.

| Flag | Effect |
|---|---|
| `PrimaryKey` | part of the primary key |
| `Required` | mandatory on write |
| `ApiAware` | readable/writable via API (otherwise internal) |
| `Inherited` | inheritance parent→child (→ `sw-field-inheritance`) |
| `Runtime` | not persisted, filled at runtime (subscriber/resolver) |
| `Computed` | computed, not writable |
| `CascadeDelete` / `RestrictDelete` / `SetNullOnDelete` | delete behaviour of associations |
| `SearchRanking` | weight in full-text search |
| `ReadProtected` / `WriteProtected` | access protection per scope (→ `sw-entity-protection`) |
| `AllowHtml` | HTML allowed in the value |

Rule of thumb: mark API fields `ApiAware` explicitly; leave internal fields without it. Choose association delete flags deliberately.

→ All flags in detail: [FIELD-FLAGS-FLAGS.md](FIELD-FLAGS-FLAGS.md)
