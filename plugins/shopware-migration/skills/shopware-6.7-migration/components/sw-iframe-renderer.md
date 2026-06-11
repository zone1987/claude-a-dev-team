# sw-iframe-renderer

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| src | `any` | — | yes |  |
| locationId | `any` | — | yes |  |
| fullScreen | `any` | `false` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `signIframeSrc` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `locationIdHashQueryKey` | |
| `locationIdPathnameQueryKey` | |
| `locationIdSearchParamsQueryKey` | |
| `componentName` | |
| `extension` | |
| `extensionIsApp` | |
| `iFrameSrc` | |
| `iFrameHeight` | |
| `classes` | |

## Examples

### Example 1
Source: `sw-extension-sdk/page/sw-extension-sdk-module/sw-extension-sdk-module.html.twig`
```twig
    <sw-iframe-renderer
        v-if="!isLoading"
        ref="iframeRenderer"
        :src="module.baseUrl"
        :location-id="module.locationId"
        full-screen
    />
    {% endblock %}

    {% block sw_extension_sdk_module_content_loader %}
    <sw-loader v-else-if="!timedOut" />
    {% endblock %}

    {% block sw_extension_sdk_module_content_error_state %}
    <sw-my-apps-error-page v-if="timedOut" />
```

### Example 2
Source: `sw-cms/elements/location-renderer/config/sw-cms-el-config-location-renderer.html.twig`
```twig
    <sw-iframe-renderer
        :src="src"
        :location-id="configLocation"
    />
</div>
{% endblock %}

```

### Example 3
Source: `sw-cms/elements/location-renderer/component/sw-cms-el-location-renderer.html.twig`
```twig
    <sw-iframe-renderer
        :src="src"
        :location-id="elementLocation"
    />
</div>
{% endblock %}

```

### Example 4
Source: `sw-cms/elements/location-renderer/preview/sw-cms-el-preview-location-renderer.html.twig`
```twig
    <sw-iframe-renderer
        :src="src"
        :location-id="previewLocation"
    />
</div>
{% endblock %}

```
