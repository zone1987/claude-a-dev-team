# sw-plugin-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| plugin | `any` | — | yes |  |
| showDescription | `any` | `true` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onInstall` | |
| `setupPlugin` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `pluginIsNotActive` | |
| `truncateFilter` | |

## Examples

### Example 1
Source: `sw-first-run-wizard/view/sw-first-run-wizard-plugins/sw-first-run-wizard-plugins.html.twig`
```twig
    <sw-plugin-card
        v-for="plugin in categoryLead"
        :key="plugin.name"
        :plugin="plugin"
        @on-plugin-installed="reloadRecommendations"
        @extension-activated="$emit('extension-activated', $event)"
    />
</div>

<hr
    v-if="showSpacer"
    class="spacer"
>

<h3
```

### Example 2
Source: `sw-first-run-wizard/view/sw-first-run-wizard-plugins/sw-first-run-wizard-plugins.html.twig`
```twig
            <sw-plugin-card
                v-for="plugin in notCategoryLead"
                :key="plugin.name"
                :plugin="plugin"
                :show-description="false"
                @on-plugin-installed="reloadRecommendations"
                @extension-activated="$emit('extension-activated', $event)"
            />
        </sw-container>
    </div>

</div>
{% endblock %}

```
