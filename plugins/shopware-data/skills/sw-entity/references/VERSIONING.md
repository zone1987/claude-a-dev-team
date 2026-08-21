# Shopware 6 — Entity versioning

The DAL can version entities (order drafts, for example). A version is an isolated state that gets merged back.

```php
$versionId = $this->repo->createVersion($id, $context);          // new version
$versionContext = $context->createWithVersionId($versionId);     // work inside it
$this->repo->update([...], $versionContext);
$this->repo->merge($versionId, $context);                        // apply to LIVE
```

Versionable entities need a `VersionField` (part of the PK); relations to them need a `ReferenceVersionField`.
The default is the live version (`Defaults::LIVE_VERSION`). Typical for orders and complex editing flows.

→ Mechanics, merge/clone details: [VERSIONING-DETAIL.md](VERSIONING-DETAIL.md)
