# sw-loader

> **Migration wrapper** — Delegates to `mt-loader` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-loader](mt-loader.md) for the new component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `any` | `null` | no |  |
| value | `any` | `null` | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

## Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `useMeteorComponent` | |

## Examples

### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
<sw-loader v-if="isLoading" />
```

### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
        <sw-loader
            v-if="isLoading"
            class="sw-settings-country-new-snippet-modal__loader"
            size="16px"
        />

        <mt-icon
            class="sw-settings-country-new-snippet-modal__search-icon"
            name="regular-search-s"
            size="16px"
        />
    </template>
</sw-contextual-field>

<sw-tree
```

### Example 3
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-loader v-if="searchInProgress" />
```

### Example 4
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-process/sw-bulk-edit-save-modal-process.html.twig`
```twig
    <sw-loader
        class="sw-bulk-edit-save-modal__loading-icon"
        size="30px"
    />
</sw-label>
{% endblock %}

{% block sw_bulk_edit_save_modal_process_generate_document %}
<ul
    v-if="selectedDocumentTypes.length > 0"
    class="sw-bulk-edit-save-modal-process__generate-document-container"
>
    <li
        v-for="selectedDocumentType in selectedDocumentTypes"
        :key="selectedDocumentType.id"
```

### Example 5
Source: `sw-extension/page/sw-extension-app-module-page/sw-extension-app-module-page.html.twig`
```twig
<sw-loader />
```
