# sw-discard-changes-modal

> Shopware Administration component.

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| keep-editing | — | |
| discard-changes | — | |

## Methods

| Method | Description |
|--------|-------------|
| `keepEditing` | |
| `discardChanges` | |

## Examples

### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
            <sw-discard-changes-modal
                v-if="isDisplayingLeavePageWarning"
                @keep-editing="onLeaveModalClose(nextRoute)"
                @discard-changes="onLeaveModalConfirm(nextRoute)"
            />
            {% endblock %}

            {% block sw_category_content_empty %}
            <mt-empty-state
                v-if="showEmptyState"
                :centered="true"
                :icon="$route.meta.$module.icon"
                :headline="$t('sw-category.general.emptyStateHeadline')"
                :description="$t($route.meta.$module.description)"
            />
```

### Example 2
Source: `sw-category/component/sw-category-entry-point-modal/sw-category-entry-point-modal.html.twig`
```twig
    <sw-discard-changes-modal
        v-if="isDisplayingLeavePageWarning"
        @keep-editing="onLeaveModalClose()"
        @discard-changes="onLeaveModalConfirm(nextRoute)"
    />
    {% endblock %}

</sw-modal>
{% endblock %}

```

### Example 3
Source: `sw-settings-rule/page/sw-settings-rule-detail/sw-settings-rule-detail.html.twig`
```twig
<sw-discard-changes-modal
    v-if="isDisplayingSaveChangesWarning"
    @keep-editing="onLeaveModalClose(nextRoute)"
    @discard-changes="onLeaveModalConfirm(nextRoute)"
/>
{% endblock %}
<sw-card-view>
    {% block sw_settings_rule_detail_tabs %}
    <sw-tabs
        v-if="rule && !rule.isNew()"
        class="sw-settings-rule-detail__tabs"
        position-identifier="sw-settings-rule-detail"
    >
        {% block sw_settings_rule_detail_tab_items %}
        <sw-tabs-item
```
