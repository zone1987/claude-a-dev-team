# sw-extension-permissions-details-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| permissions | `any` | — | yes |  |
| modalTitle | `any` | — | yes |  |
| selectedEntity | `any` | `''` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `scrollSelectedEntityIntoView` | |
| `close` | |
| `categoryLabel` | |
| `entityLabel` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `operations` | |
| `ankerId` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
    <sw-extension-permissions-details-modal
        v-if="showDetailsModal"
        :modal-title="modalTitle"
        :permissions="permissionsWithGroupedOperations"
        :selected-entity="selectedEntity"
        @modal-close="closeDetailsModal"
    />
    {% endblock %}

    {% block sw_extension_permissions_modal_domains %}
    <sw-extension-domains-modal
        v-if="showDomainsModal"
        :extension-label="extensionLabel"
        :domains="domainsList"
        @modal-close="toggleDomainsModal(false)"
```
