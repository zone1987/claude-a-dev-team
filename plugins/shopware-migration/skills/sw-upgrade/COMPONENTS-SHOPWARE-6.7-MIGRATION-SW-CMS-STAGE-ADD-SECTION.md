# sw-cms-stage-add-section

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| forceChoose | `any` | — | no |  |
| disabled | `any` | — | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| stage-section-add | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onAddSection` | |
| `toggleSelection` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `componentClasses` | |

## Examples

### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
        <sw-cms-stage-add-section
            :key="0"
            :disabled="!acl.can('cms.editor') || undefined"
            :force-choose="true"
            @stage-section-add="onAddSection($event, 0, true)"
        />
    </div>
    {% endblock %}
</div>
{% endblock %}

{% block sw_cms_detail_stage %}
<div
    v-else
    :id="`page-${page.id}`"
```

### Example 2
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
        <sw-cms-stage-add-section
            :key="page.sections.length + 1"
            :disabled="!acl.can('cms.editor') || undefined"
            @stage-section-add="onAddSection($event, page.sections.length, true)"
        />
        {% endblock %}
    </div>
    {% endblock %}
</div>
{% endblock %}

{% block sw_cms_detail_sidebar %}
<sw-cms-sidebar
    ref="cmsSidebar"
    :page="page"
```
