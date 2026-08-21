# sw-generic-seo-general-card

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| seoMetaTitle | `any` | `''` | no |  |
| seoMetaDescription | `any` | `''` | no |  |
| seoUrl | `any` | `''` | no |  |

## Methods

| Method | Description |
|--------|-------------|
| `emitSeoMetaTitle` | |
| `emitSeoMetaDescription` | |
| `emitSeoUrl` | |

## Examples

### Example 1
Source: `sw-custom-entity/page/sw-generic-custom-entity-detail/sw-generic-custom-entity-detail.html.twig`
```twig
                        <sw-generic-seo-general-card
                            :seo-meta-title="customEntityData?.swSeoMetaTitle"
                            :seo-meta-description="customEntityData?.swSeoMetaDescription"
                            :seo-url="customEntityData?.swSeoUrl"
                            @update:seo-meta-title="updateSeoMetaTitle"
                            @update:seo-meta-description="updateSeoMetaDescription"
                            @update:seo-url="updateSeoUrl"
                        />

                        <sw-generic-social-media-card
                            :og-title="customEntityData?.swOgTitle"
                            :og-description="customEntityData?.swOgDescription"
                            :og-image-id="customEntityData?.swOgImageId"
                            @update:og-title="updateOgTitle"
                            @update:og-description="updateOgDescription"
```
