# sw-flow-trigger

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| overlay | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| eventName | `any` | — | yes |  |
| isUnknownTrigger | `any` | `false` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| option-select | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `handleClickEvent` | |
| `handleGeneralKeyEvents` | |
| `handleArrowKeyEvents` | |
| `getClosestSiblingAncestor` | |
| `getClosestSiblingDescendant` | |
| `getFirstChildById` | |
| `getSibling` | |
| `changeSearchSelection` | |
| `toggleSelectedTreeItem` | |
| `findTreeItemVNodeById` | |
| `openDropdown` | |
| `closeDropdown` | |
| `changeTrigger` | |
| `onConfirm` | |
| `onCloseConfirm` | |
| `getLastEventName` | |
| `getDataByEvent` | |
| `hasOnlyStopFlow` | |
| `getEventTree` | |
| `getBreadcrumb` | |
| `onClickSearchItem` | |
| `getEventName` | |
| `isSearchResultInFocus` | |
| `getEventNameTranslated` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `swFlowTriggerClasses` | |
| `formatEventName` | |
| `showTreeView` | |
| `eventTree` | |
| `isTemplate` | |
| `triggerNamePlaceholder` | |
| `flow` | |
| `triggerEvents` | |
| `isSequenceEmpty` | |
| `flowEventNameError` | |

## Examples

### Example 1
Source: `sw-flow/view/detail/sw-flow-detail-flow/sw-flow-detail-flow.html.twig`
```twig
        <sw-flow-trigger
            :disabled="!acl.can('flow.editor')"
            :event-name="flow.eventName"
            :is-unknown-trigger="isUnknownTrigger"
            @option-select="onEventChange"
        />
        {% endblock %}
    </div>
    {% endblock %}

    {% block sw_flow_detail_flow_trigger_explains %}
    <div
        v-if="!flow.eventName"
        class="sw-flow-detail-flow__trigger-explain"
    >
```
