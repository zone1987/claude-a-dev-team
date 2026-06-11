---
name: sw-admin-repository-js
description: >
  Das Admin-Repository (JS) in Shopware 6 im Detail: create/get/search/save/delete/clone/syncDeleted, Entity &
  EntityCollection erzeugen, Versionskontext, association lazy load. Trigger: "repository.create admin", "repository.get",
  "createEntity admin", "EntityCollection js", "repository.clone", "syncDeleted", "neue Entity admin anlegen". Shopware 6.7.
---

# Shopware 6 — Admin-Repository (JS)

```js
const repo = this.repositoryFactory.create('ff_example');

// neuer Datensatz
const entity = repo.create(Shopware.Context.api);
entity.name = 'Neu';
await repo.save(entity, Shopware.Context.api);

// einzelner Datensatz mit Associations
const item = await repo.get(id, Shopware.Context.api, criteria);

// löschen / klonen
await repo.delete(id, Shopware.Context.api);
await repo.clone(id, Shopware.Context.api, behavior);
```

`create()` erzeugt eine Entity mit generierter ID (clientseitig, UUID). `save()` macht create/update. Für Listen
liefert `search()` eine `EntityCollection` (add/remove/getIds). Versionierung über `repositoryFactory` + Version-Context
analog DAL. Lade-Performance: Associations gezielt per Criteria.
