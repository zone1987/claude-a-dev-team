# sw-extension-domains-modal

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionLabel | `any` | — | yes |  |
| domains | `any` | — | yes |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

## Methods

| Method | Description |
|--------|-------------|
| `close` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
    <sw-extension-domains-modal
        v-if="showDomainsModal"
        :extension-label="extensionLabel"
        :domains="domainsList"
        @modal-close="toggleDomainsModal(false)"
    />
    {% endblock %}
</sw-modal>
{% endblock %}

```
