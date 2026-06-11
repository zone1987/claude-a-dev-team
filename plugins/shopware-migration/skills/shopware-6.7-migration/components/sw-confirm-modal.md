# sw-confirm-modal

> Confirmation modal dialog with confirm and cancel actions.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | `''` | no |  |
| text | `any` | `''` | no |  |
| textConfirm | `any` | `''` | no |  |
| variant | `any` | `'small'` | no | Valid: `default`, `small`, `large`, `full` |
| type | `any` | `'confirm'` | no | Valid: `confirm`, `delete`, `yesno`, `discard` |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| cancel | — | |
| confirm | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `titleText` | |
| `descriptionText` | |
| `confirmText` | |
| `cancelText` | |
| `confirmButtonVariant` | |

## Examples

### Example 1
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
        <sw-confirm-modal
            v-if="isDisplayingLeavePageWarning"
            class="sw_settings_search_leave_modal"
            type="yesno"
            :text="$tc('sw-settings-search.textLeaveConfirm')"
            @confirm="onConfirmLeave"
            @close="onCloseLeaveModal"
            @cancel="onCancelLeaveModal"
        />
        {% endblock %}

    </template>
    {% endblock %}
</sw-page>
{% endblock %}
```

### Example 2
Source: `sw-category/component/sw-category-entry-point-overwrite-modal/sw-category-entry-point-overwrite-modal.html.twig`
```twig
<sw-confirm-modal
    class="sw-category-entry-point-overwrite-modal"
    @cancel="onCancel"
    @close="onCancel"
    @confirm="onConfirm"
>

    <p class="sw-confirm-modal__text">
        {{ $tc('sw-category.entry-point-overwrite-modal.textBefore', {}, salesChannels.length) }}
    </p>

    <ul>
        <li
            v-for="salesChannel in salesChannels"
            :key="salesChannel.translated.name"
```

### Example 3
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
<sw-confirm-modal
    v-if="showLayoutSetAsDefaultModal"
    class="sw-cms-list__confirm-set-as-default-modal"
    :title="$tc('sw-cms.components.setDefaultLayoutModal.title')"
    :text="$tc('sw-cms.components.setDefaultLayoutModal.infoText', {}, newDefaultLayout.type === 'product_detail')"
    @confirm="onConfirmLayoutSetAsDefault"
    @cancel="onCloseLayoutSetAsDefault"
    @close="onCloseLayoutSetAsDefault"
/>

{% block sw_cms_list_rename_modal %}
<sw-modal
    v-if="showRenameModal"
    :title="$tc('sw-cms.components.cmsListItem.modal.renameModalTitle')"
    variant="small"
```

### Example 4
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
                <sw-confirm-modal
                    v-if="showLayoutSetAsDefaultModal"
                    class="sw-cms-detail__confirm-set-as-default-modal"
                    :title="$tc('sw-cms.components.setDefaultLayoutModal.title')"
                    :text="$tc('sw-cms.components.setDefaultLayoutModal.infoText', {}, page.type === 'product_detail')"
                    @confirm="onConfirmLayoutSetAsDefault"
                    @cancel="onCloseLayoutSetAsDefault"
                    @close="onCloseLayoutSetAsDefault"
                />

                {% block sw_cms_detail_missing_element_modal %}
                <sw-cms-missing-element-modal
                    v-if="showMissingElementModal"
                    :missing-elements="missingElements"
                    @modal-close="onCloseMissingElementModal"
```

### Example 5
Source: `sw-cms/component/sw-cms-reset-inheritance/sw-cms-reset-inheritance.html.twig`
```twig
    <sw-confirm-modal
        v-if="showModal"
        type="delete"
        :text="$t('sw-cms.inherit.unlinkAllConfirmText')"
        :title="$t('sw-cms.inherit.unlinkAllTitle')"
        :text-confirm="$t('sw-cms.inherit.unlinkAllTitle')"
        @confirm="onConfirm"
        @cancel="showModal = false;"
        @close="showModal = false;"
    />
</div>

```
