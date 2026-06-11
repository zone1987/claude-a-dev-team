---
name: sw-entity-versioning
description: >
  Entity-Versioning in Shopware 6 DAL: createVersion, merge, Versionskontext, ReferenceVersionField,
  VersionField. Trigger: "Versioning", "createVersion", "merge version", "Entity-Version", "ReferenceVersionField",
  "versionierte Entity", "draft version". Shopware 6.7.
---

# Shopware 6 — Entity-Versioning

DAL kann Entities versionieren (z.B. Order-Drafts). Eine Version ist ein isolierter Stand, der gemerged wird.

```php
$versionId = $this->repo->createVersion($id, $context);          // neue Version
$versionContext = $context->createWithVersionId($versionId);     // darin arbeiten
$this->repo->update([...], $versionContext);
$this->repo->merge($versionId, $context);                        // in LIVE übernehmen
```

Versionierbare Entities brauchen ein `VersionField` (PK-Teil) bzw. Beziehungen ein `ReferenceVersionField`.
Standard ist die Live-Version (`Defaults::LIVE_VERSION`). Typisch für Bestellungen und komplexe Bearbeitungs-Flows.

→ Mechanik, merge/clone Details: [references/versioning.md](references/versioning.md)
