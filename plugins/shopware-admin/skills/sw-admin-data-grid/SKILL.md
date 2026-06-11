---
name: sw-admin-data-grid
description: >
  Listen/Tabellen im Shopware-6-Admin: sw-data-grid/sw-entity-listing, Columns, Sortierung/Paginierung via
  listing-Mixin, Bulk-Edit, Inline-Edit. Trigger: "Admin Data Grid", "sw-data-grid", "sw-entity-listing", "Tabelle admin",
  "listing mixin", "columns grid admin", "inline edit grid". Shopware 6.7.
---

# Shopware 6 — Admin-Data-Grid

Listen mit `sw-entity-listing` (an Repository gekoppelt) bzw. `sw-data-grid` (eigene Daten).

```twig
{% block ff_example_list %}
<sw-entity-listing
    :items="items"
    :repository="repository"
    :columns="columns"
    :is-loading="isLoading"
    @column-sort="onSortColumn"
    @page-change="onPageChange" />
{% endblock %}
```
```js
mixins: [Shopware.Mixin.getByName('listing')],
computed: {
    columns() { return [{ property: 'name', label: this.$tc('ff-example.name'), routerLink: 'ff.example.detail' }]; },
},
```

Das `listing`-Mixin liefert `page`/`limit`/`sortBy`/`getList()`. Spalten mit `routerLink` für Detail-Navigation,
`inlineEdit` für direktes Bearbeiten, Selektion für Bulk-Aktionen. Daten via Repository (`sw-admin-data-handling`).
