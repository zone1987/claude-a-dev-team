# Shopware 6 — Admin data grid

Lists with `sw-entity-listing` (coupled to a repository) or `sw-data-grid` (your own data).

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

The `listing` mixin provides `page`/`limit`/`sortBy`/`getList()`. Columns with `routerLink` for detail navigation,
`inlineEdit` for editing in place, selection for bulk actions. Data via repository (`sw-admin-data-handling`).
