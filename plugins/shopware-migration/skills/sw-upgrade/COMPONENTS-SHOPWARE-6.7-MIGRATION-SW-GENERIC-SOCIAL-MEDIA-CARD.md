# sw-generic-social-media-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ogTitle | `any` | `''` | no |  |
| ogDescription | `any` | `''` | no |  |
| ogImageId | `any` | `null` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `onCreated` | |
| `loadOgImage` | |
| `removeOgImage` | |
| `onOpenMediaModal` | |
| `onCloseMediaModal` | |
| `onImageUpload` | |
| `onSelectionChanges` | |
| `emitMediaId` | |
| `emitOgTitle` | |
| `emitOgDescription` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `uploadTag` | |

## Examples

### Example 1
Source: `sw-custom-entity/page/sw-generic-custom-entity-detail/sw-generic-custom-entity-detail.html.twig`
```twig
                        <sw-generic-social-media-card
                            :og-title="customEntityData?.swOgTitle"
                            :og-description="customEntityData?.swOgDescription"
                            :og-image-id="customEntityData?.swOgImageId"
                            @update:og-title="updateOgTitle"
                            @update:og-description="updateOgDescription"
                            @update:og-image-id="updateOgImageId"
                        />
                    </template>
                </template>
            </sw-tabs>
        </sw-card-view>
    </template>
</sw-page>
{% endblock %}
```
