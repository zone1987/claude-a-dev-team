# sw-flow-leave-page-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-leave-confirm | — | |
| page-leave-cancel | — | |

## Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `onCancel` | |

## Examples

### Example 1
Source: `sw-flow/page/sw-flow-detail/sw-flow-detail.html.twig`
```twig
<sw-flow-leave-page-modal
    v-if="showLeavePageWarningModal"
    @page-leave-cancel="onLeaveModalClose"
    @page-leave-confirm="onLeaveModalConfirm"
/>
{% endblock %}

<sw-card-view :class="{'sw-flow-detail__template': isTemplate }">
    {% block sw_flow_tabs_header %}
    <sw-tabs position-identifier="sw-flow-detail">
        {% block sw_flow_tabs_header_general %}
        <sw-tabs-item
            class="sw-flow-detail__tab-general"
            :route="routeDetailTab('general')"
        >
```
