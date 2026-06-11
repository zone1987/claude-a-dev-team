# sw-landing-page-view

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | yes |  |

## Computed Properties

| Name | Description |
|------|-------------|
| `landingPage` | |
| `cmsPage` | |

## Examples

### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
            <sw-landing-page-view
                v-if="landingPage"
                ref="landingPageView"
                :is-loading="isLoading"
            />
            {% endblock %}

            {% block sw_category_content_discard_changes_modal %}
            <sw-discard-changes-modal
                v-if="isDisplayingLeavePageWarning"
                @keep-editing="onLeaveModalClose(nextRoute)"
                @discard-changes="onLeaveModalConfirm(nextRoute)"
            />
            {% endblock %}

```
