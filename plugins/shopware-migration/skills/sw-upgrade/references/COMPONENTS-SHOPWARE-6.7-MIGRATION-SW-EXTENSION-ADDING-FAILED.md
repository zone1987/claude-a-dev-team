# sw-extension-adding-failed

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| title | `any` | `null` | no |  |
| detail | `any` | `null` | no |  |
| documentationLink | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `myExtensions` | |
| `extension` | |
| `isRent` | |
| `headline` | |
| `text` | |

## Examples

### Example 1
Source: `sw-extension/component/sw-extension-card-bought/sw-extension-card-bought.html.twig`
```twig
    <sw-extension-adding-failed
        :extension-name="extension.name"
        :title="installationFailedError && installationFailedError.title"
        :detail="installationFailedError && installationFailedError.message"
        :documentation-link="installationFailedError && installationFailedError.parameters && installationFailedError.parameters.documentationLink"
        @close="closeInstallationFailedNotification"
    />
</sw-modal>
{% endblock %}

```
