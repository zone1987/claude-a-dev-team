# Component Migration Examples

Real-world migration scenarios showing complete before/after code for common Shopware admin patterns.

---

## 1. Full Detail Page Migration

A typical plugin detail page with cards, form fields, tabs, and action buttons.

### BEFORE (6.6)

```html
{% block my_plugin_detail %}
<sw-page class="my-plugin-detail">
    <template #smart-bar-actions>
        <sw-button variant="ghost" @click="onCancel">
            {{ $tc('global.default.cancel') }}
        </sw-button>
        <sw-button
            variant="primary"
            :isLoading="isLoading"
            :disabled="!hasChanges"
            @click="onSave"
        >
            {{ $tc('global.default.save') }}
        </sw-button>
    </template>

    <template #content>
        <sw-card-view>
            <sw-card :title="$tc('my-plugin.detail.generalCard')" :isLoading="isLoading">
                <sw-text-field
                    :value="item.name"
                    :label="$tc('my-plugin.detail.labelName')"
                    :error="nameError"
                    :required="true"
                    @input="onNameChange"
                />

                <sw-textarea-field
                    :value="item.description"
                    :label="$tc('my-plugin.detail.labelDescription')"
                    :maxLength="500"
                    @input="item.description = $event"
                />

                <sw-switch-field
                    :value="item.active"
                    :label="$tc('my-plugin.detail.labelActive')"
                    @input="item.active = $event"
                />

                <sw-select-field
                    :value="item.type"
                    :label="$tc('my-plugin.detail.labelType')"
                    :options="typeOptions"
                    @input="item.type = $event"
                />

                <sw-number-field
                    :value="item.priority"
                    :label="$tc('my-plugin.detail.labelPriority')"
                    numberType="int"
                    :min="0"
                    :max="100"
                    @input="item.priority = $event"
                />

                <sw-colorpicker
                    :value="item.color"
                    :label="$tc('my-plugin.detail.labelColor')"
                    @input="item.color = $event"
                />

                <sw-datepicker
                    :value="item.validFrom"
                    :label="$tc('my-plugin.detail.labelValidFrom')"
                    dateType="datetime"
                    @input="item.validFrom = $event"
                />
            </sw-card>

            <sw-card :title="$tc('my-plugin.detail.settingsCard')">
                <sw-email-field
                    :value="item.contactEmail"
                    :label="$tc('my-plugin.detail.labelEmail')"
                    @input="item.contactEmail = $event"
                />

                <sw-url-field
                    :value="item.website"
                    :label="$tc('my-plugin.detail.labelWebsite')"
                    @input="item.website = $event"
                />

                <sw-password-field
                    :value="item.apiKey"
                    :label="$tc('my-plugin.detail.labelApiKey')"
                    :passwordToggleAble="true"
                    @input="item.apiKey = $event"
                />

                <sw-checkbox-field
                    :value="item.sendNotifications"
                    :label="$tc('my-plugin.detail.labelNotifications')"
                    @input="item.sendNotifications = $event"
                />
            </sw-card>
        </sw-card-view>
    </template>
</sw-page>
{% endblock %}
```

### AFTER (6.7)

```html
{% block my_plugin_detail %}
<sw-page class="my-plugin-detail">
    <template #smart-bar-actions>
        <mt-button variant="secondary" :ghost="true" @click="onCancel">
            {{ $tc('global.default.cancel') }}
        </mt-button>
        <mt-button
            variant="primary"
            :isLoading="isLoading"
            :disabled="!hasChanges"
            @click="onSave"
        >
            {{ $tc('global.default.save') }}
        </mt-button>
    </template>

    <template #content>
        <sw-card-view>
            <mt-card :title="$tc('my-plugin.detail.generalCard')" :isLoading="isLoading">
                <mt-text-field
                    v-model="item.name"
                    :label="$tc('my-plugin.detail.labelName')"
                    :error="nameError"
                    :required="true"
                />

                <mt-textarea
                    v-model="item.description"
                    :label="$tc('my-plugin.detail.labelDescription')"
                    :maxLength="500"
                />

                <mt-switch
                    v-model="item.active"
                    :label="$tc('my-plugin.detail.labelActive')"
                />

                <mt-select
                    v-model="item.type"
                    :label="$tc('my-plugin.detail.labelType')"
                    :options="typeOptions"
                />

                <mt-number-field
                    v-model="item.priority"
                    :label="$tc('my-plugin.detail.labelPriority')"
                    numberType="int"
                    :min="0"
                    :max="100"
                />

                <mt-colorpicker
                    v-model="item.color"
                    :label="$tc('my-plugin.detail.labelColor')"
                />

                <mt-datepicker
                    v-model="item.validFrom"
                    :label="$tc('my-plugin.detail.labelValidFrom')"
                    dateType="datetime"
                />
            </mt-card>

            <mt-card :title="$tc('my-plugin.detail.settingsCard')">
                <mt-email-field
                    v-model="item.contactEmail"
                    :label="$tc('my-plugin.detail.labelEmail')"
                />

                <mt-url-field
                    v-model="item.website"
                    :label="$tc('my-plugin.detail.labelWebsite')"
                />

                <mt-password-field
                    v-model="item.apiKey"
                    :label="$tc('my-plugin.detail.labelApiKey')"
                    :toggable="true"
                />

                <mt-checkbox
                    v-model="item.sendNotifications"
                    :label="$tc('my-plugin.detail.labelNotifications')"
                />
            </mt-card>
        </sw-card-view>
    </template>
</sw-page>
{% endblock %}
```

**Key changes:**
- All `sw-*` form components replaced with `mt-*` equivalents
- `:value` + `@input` replaced with `v-model` (much cleaner)
- `sw-button variant="ghost"` becomes `mt-button variant="secondary" :ghost="true"`
- `sw-textarea-field` becomes `mt-textarea`
- `sw-switch-field` becomes `mt-switch`
- `sw-checkbox-field` becomes `mt-checkbox`
- `:passwordToggleAble` becomes `:toggable`

---

## 2. List Page with Data Grid

### BEFORE (6.6)

```html
{% block my_plugin_list %}
<sw-page class="my-plugin-list">
    <template #smart-bar-actions>
        <sw-button variant="primary" :router-link="{ name: 'my.plugin.create' }">
            {{ $tc('my-plugin.list.buttonCreate') }}
        </sw-button>
    </template>

    <template #content>
        <sw-card :isLoading="isLoading">
            <template #grid>
                <sw-data-grid
                    :data-source="items"
                    :columns="columns"
                    :show-selection="true"
                    :show-actions="true"
                    @selection-change="onSelectionChange"
                    @column-sort="onSortColumn"
                >
                    <template #column-active="{ item }">
                        <sw-icon
                            :name="item.active ? 'regular-checkmark-xs' : 'regular-times-s'"
                            :small="true"
                        />
                    </template>

                    <template #actions="{ item }">
                        <sw-context-menu-item
                            :router-link="{ name: 'my.plugin.detail', params: { id: item.id } }"
                        >
                            {{ $tc('my-plugin.list.contextMenuEdit') }}
                        </sw-context-menu-item>
                        <sw-context-menu-item
                            variant="danger"
                            @click="onDelete(item.id)"
                        >
                            {{ $tc('my-plugin.list.contextMenuDelete') }}
                        </sw-context-menu-item>
                    </template>
                </sw-data-grid>
            </template>
        </sw-card>
    </template>
</sw-page>
{% endblock %}
```

### AFTER (6.7)

```html
{% block my_plugin_list %}
<sw-page class="my-plugin-list">
    <template #smart-bar-actions>
        <router-link :to="{ name: 'my.plugin.create' }">
            <mt-button variant="primary">
                {{ $tc('my-plugin.list.buttonCreate') }}
            </mt-button>
        </router-link>
    </template>

    <template #content>
        <mt-card :isLoading="isLoading">
            <template #grid>
                <!-- TODO: sw-data-grid to mt-data-table requires manual migration -->
                <!-- The data-grid API differs significantly; review mt-data-table docs -->
                <sw-data-grid
                    :data-source="items"
                    :columns="columns"
                    :show-selection="true"
                    :show-actions="true"
                    @selection-change="onSelectionChange"
                    @column-sort="onSortColumn"
                >
                    <template #column-active="{ item }">
                        <mt-icon
                            :name="item.active ? 'regular-checkmark-xs' : 'regular-times-s'"
                            size="16px"
                        />
                    </template>

                    <template #actions="{ item }">
                        <sw-context-menu-item
                            :router-link="{ name: 'my.plugin.detail', params: { id: item.id } }"
                        >
                            {{ $tc('my-plugin.list.contextMenuEdit') }}
                        </sw-context-menu-item>
                        <sw-context-menu-item
                            variant="danger"
                            @click="onDelete(item.id)"
                        >
                            {{ $tc('my-plugin.list.contextMenuDelete') }}
                        </sw-context-menu-item>
                    </template>
                </sw-data-grid>
            </template>
        </mt-card>
    </template>
</sw-page>
{% endblock %}
```

**Key changes:**
- `sw-button :router-link` becomes `<router-link>` wrapping `<mt-button>`
- `sw-card` becomes `mt-card`
- `sw-icon :small` becomes `mt-icon size="16px"`
- `sw-data-grid` stays as-is (requires manual migration to `mt-data-table`)
- `sw-context-menu-item` is not part of the Meteor migration (stays as-is)

---

## 3. Modal with Form Fields

### BEFORE (6.6)

```html
<sw-modal
    v-if="showModal"
    :title="$tc('my-plugin.modal.createTitle')"
    variant="large"
    @modal-close="onCloseModal"
>
    <template #modal-body>
        <sw-alert variant="warning" :closable="false">
            {{ $tc('my-plugin.modal.warningMessage') }}
        </sw-alert>

        <sw-text-field
            :value="newItem.name"
            :label="$tc('my-plugin.modal.labelName')"
            :required="true"
            :error="nameError"
            @input="newItem.name = $event"
        />

        <sw-select-field
            :value="newItem.category"
            :label="$tc('my-plugin.modal.labelCategory')"
            :options="categoryOptions"
            @input="newItem.category = $event"
        />

        <sw-switch-field
            :value="newItem.active"
            :label="$tc('my-plugin.modal.labelActive')"
            @input="newItem.active = $event"
        />
    </template>

    <template #modal-footer>
        <sw-button @click="onCloseModal">
            {{ $tc('global.default.cancel') }}
        </sw-button>
        <sw-button
            variant="primary"
            :disabled="!isFormValid"
            :isLoading="isSaving"
            @click="onSave"
        >
            {{ $tc('global.default.save') }}
        </sw-button>
    </template>
</sw-modal>
```

### AFTER (6.7)

```html
<mt-modal
    v-if="showModal"
    :title="$tc('my-plugin.modal.createTitle')"
    width="l"
    @close="onCloseModal"
>
    <mt-banner variant="attention" :closable="false">
        {{ $tc('my-plugin.modal.warningMessage') }}
    </mt-banner>

    <mt-text-field
        v-model="newItem.name"
        :label="$tc('my-plugin.modal.labelName')"
        :required="true"
        :error="nameError"
    />

    <mt-select
        v-model="newItem.category"
        :label="$tc('my-plugin.modal.labelCategory')"
        :options="categoryOptions"
    />

    <mt-switch
        v-model="newItem.active"
        :label="$tc('my-plugin.modal.labelActive')"
    />

    <template #footer>
        <mt-button @click="onCloseModal">
            {{ $tc('global.default.cancel') }}
        </mt-button>
        <mt-button
            variant="primary"
            :disabled="!isFormValid"
            :isLoading="isSaving"
            @click="onSave"
        >
            {{ $tc('global.default.save') }}
        </mt-button>
    </template>
</mt-modal>
```

**Key changes:**
- `sw-modal variant="large"` becomes `mt-modal width="l"`
- `@modal-close` becomes `@close`
- `#modal-body` slot is removed (use default slot directly)
- `#modal-footer` becomes `#footer`
- `sw-alert variant="warning"` becomes `mt-banner variant="attention"`
- All form fields use `v-model` instead of `:value` + `@input`

---

## 4. Tabs with Content Panels

### BEFORE (6.6)

```html
<sw-tabs @new-item-active="onTabChange">
    <template #default="{ active }">
        <sw-tabs-item :active-tab="active" name="general">
            {{ $tc('my-plugin.tabs.general') }}
        </sw-tabs-item>
        <sw-tabs-item :active-tab="active" name="advanced">
            {{ $tc('my-plugin.tabs.advanced') }}
        </sw-tabs-item>
        <sw-tabs-item :active-tab="active" name="permissions">
            {{ $tc('my-plugin.tabs.permissions') }}
        </sw-tabs-item>
    </template>

    <template #content="{ active }">
        <sw-card v-if="active === 'general'">
            <sw-text-field :value="item.name" @input="item.name = $event" />
        </sw-card>
        <sw-card v-if="active === 'advanced'">
            <sw-number-field :value="item.priority" @input="item.priority = $event" />
        </sw-card>
        <sw-card v-if="active === 'permissions'">
            <sw-checkbox-field :value="item.public" @input="item.public = $event" />
        </sw-card>
    </template>
</sw-tabs>
```

### AFTER (6.7)

```html
<mt-tabs
    :items="[
        { label: $tc('my-plugin.tabs.general'), name: 'general' },
        { label: $tc('my-plugin.tabs.advanced'), name: 'advanced' },
        { label: $tc('my-plugin.tabs.permissions'), name: 'permissions' },
    ]"
    @new-item-active="activeTab = $event"
/>

<mt-card v-if="activeTab === 'general'">
    <mt-text-field v-model="item.name" />
</mt-card>
<mt-card v-if="activeTab === 'advanced'">
    <mt-number-field v-model="item.priority" />
</mt-card>
<mt-card v-if="activeTab === 'permissions'">
    <mt-checkbox v-model="item.public" />
</mt-card>
```

**Key changes:**
- `sw-tabs` with child `sw-tabs-item` components becomes a single `mt-tabs` with `:items` array
- Tab content is no longer inside the tabs component (separate rendering)
- Active tab state must be managed in component data (`activeTab`)

---

## 5. Inheritance Fields (Sales Channel)

### BEFORE (6.6)

```html
<sw-text-field
    :value="product.name"
    :label="$tc('sw-product.detail.labelName')"
    :inherit-value="parentProduct ? parentProduct.name : null"
    :is-inheritance-field="true"
    :is-inherited="isInherited(product, 'name')"
    @input="product.name = $event"
    @inheritance-restore="restoreInheritance(product, 'name')"
    @inheritance-remove="removeInheritance(product, 'name')"
/>
```

### AFTER (6.7)

```html
<mt-text-field
    v-model="product.name"
    :label="$tc('sw-product.detail.labelName')"
    :is-inheritance-field="true"
    :is-inherited="isInherited(product, 'name')"
    @inheritance-restore="restoreInheritance(product, 'name')"
    @inheritance-remove="removeInheritance(product, 'name')"
/>
```

---

## 6. Error Handling Pattern

### BEFORE (6.6)

```javascript
computed: {
    nameError() {
        if (this.$store) {
            return Shopware.State.getters'error/getApiError';
        }
        return null;
    },
},
```

### AFTER (6.7)

```javascript
// Error handling API is the same - mt-* components accept the same error format
// { code: number, detail: string }
computed: {
    nameError() {
        // Use Shopware.Store (Pinia) instead of Shopware.State (Vuex) if migrated
        const errorStore = Shopware.Store.get('error');
        return errorStore.getApiError(this.product, 'name');
    },
},
```

---

## 7. ACL-Protected Actions

### BEFORE (6.6)

```html
<sw-button
    variant="primary"
    :disabled="!acl.can('my_plugin.editor')"
    @click="onSave"
>
    {{ $tc('global.default.save') }}
</sw-button>

<sw-button
    variant="danger"
    :disabled="!acl.can('my_plugin.deleter')"
    @click="onDelete"
>
    {{ $tc('global.default.delete') }}
</sw-button>
```

### AFTER (6.7)

```html
<mt-button
    variant="primary"
    :disabled="!acl.can('my_plugin.editor')"
    @click="onSave"
>
    {{ $tc('global.default.save') }}
</mt-button>

<mt-button
    variant="critical"
    :disabled="!acl.can('my_plugin.deleter')"
    @click="onDelete"
>
    {{ $tc('global.default.delete') }}
</mt-button>
```

**Note:** ACL integration is unchanged. Only the component names and variant names change (`danger` becomes `critical`).

---

## 8. Loading States

### BEFORE (6.6)

```html
<sw-card :title="title" :isLoading="isLoading">
    <template v-if="isLoading">
        <sw-skeleton-bar />
        <sw-skeleton-bar />
        <sw-skeleton-bar />
    </template>
    <template v-else>
        <!-- actual content -->
    </template>
</sw-card>
```

### AFTER (6.7)

```html
<mt-card :title="title" :isLoading="isLoading">
    <template v-if="isLoading">
        <mt-skeleton-bar />
        <mt-skeleton-bar />
        <mt-skeleton-bar />
    </template>
    <template v-else>
        <!-- actual content -->
    </template>
</mt-card>
```

---

## 9. Progress Indicator

### BEFORE (6.6)

```html
<sw-progress-bar :value="importProgress" :maxValue="totalItems" />
```

### AFTER (6.7)

```html
<mt-progress-bar
    v-model="importProgress"
    :label="$tc('my-plugin.import.progress')"
    :maxValue="totalItems"
/>
```

**Note:** `mt-progress-bar` requires a `label` prop (required in Meteor component).
