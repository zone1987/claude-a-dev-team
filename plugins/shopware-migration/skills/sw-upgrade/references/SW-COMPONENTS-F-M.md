# Administration (sw-*) components

176 components, each with its props, slots, events and examples exactly as the generator extracted them. One file per component cost 1044 unreachable references; grouped, every component stays one direct link from SKILL.md.

## Contents

- [`sw-field-copyable`](#sw-field-copyable)
- [`sw-field-error`](#sw-field-error)
- [`sw-file-input`](#sw-file-input)
- [`sw-filter-panel`](#sw-filter-panel)
- [`sw-first-run-wizard-data-import`](#sw-first-run-wizard-data-import)
- [`sw-first-run-wizard-defaults`](#sw-first-run-wizard-defaults)
- [`sw-first-run-wizard-finish`](#sw-first-run-wizard-finish)
- [`sw-first-run-wizard-mailer-base`](#sw-first-run-wizard-mailer-base)
- [`sw-first-run-wizard-mailer-local`](#sw-first-run-wizard-mailer-local)
- [`sw-first-run-wizard-mailer-selection`](#sw-first-run-wizard-mailer-selection)
- [`sw-first-run-wizard-mailer-smtp`](#sw-first-run-wizard-mailer-smtp)
- [`sw-first-run-wizard-modal`](#sw-first-run-wizard-modal)
- [`sw-first-run-wizard-paypal-base`](#sw-first-run-wizard-paypal-base)
- [`sw-first-run-wizard-paypal-credentials`](#sw-first-run-wizard-paypal-credentials)
- [`sw-first-run-wizard-paypal-info`](#sw-first-run-wizard-paypal-info)
- [`sw-first-run-wizard-plugins`](#sw-first-run-wizard-plugins)
- [`sw-first-run-wizard-shopware-account`](#sw-first-run-wizard-shopware-account)
- [`sw-first-run-wizard-shopware-base`](#sw-first-run-wizard-shopware-base)
- [`sw-first-run-wizard-shopware-domain`](#sw-first-run-wizard-shopware-domain)
- [`sw-first-run-wizard-store`](#sw-first-run-wizard-store)
- [`sw-first-run-wizard-welcome`](#sw-first-run-wizard-welcome)
- [`sw-first-run-wizard`](#sw-first-run-wizard)
- [`sw-flow-affiliate-and-campaign-code-modal`](#sw-flow-affiliate-and-campaign-code-modal)
- [`sw-flow-app-action-modal`](#sw-flow-app-action-modal)
- [`sw-flow-change-customer-group-modal`](#sw-flow-change-customer-group-modal)
- [`sw-flow-change-customer-status-modal`](#sw-flow-change-customer-status-modal)
- [`sw-flow-create-mail-template-modal`](#sw-flow-create-mail-template-modal)
- [`sw-flow-detail-flow`](#sw-flow-detail-flow)
- [`sw-flow-detail-general`](#sw-flow-detail-general)
- [`sw-flow-detail`](#sw-flow-detail)
- [`sw-flow-event-change-confirm-modal`](#sw-flow-event-change-confirm-modal)
- [`sw-flow-generate-document-modal`](#sw-flow-generate-document-modal)
- [`sw-flow-grant-download-access-modal`](#sw-flow-grant-download-access-modal)
- [`sw-flow-index`](#sw-flow-index)
- [`sw-flow-leave-page-modal`](#sw-flow-leave-page-modal)
- [`sw-flow-list-flow-templates`](#sw-flow-list-flow-templates)
- [`sw-flow-list`](#sw-flow-list)
- [`sw-flow-mail-send-modal`](#sw-flow-mail-send-modal)
- [`sw-flow-rule-modal`](#sw-flow-rule-modal)
- [`sw-flow-sequence-action-error`](#sw-flow-sequence-action-error)
- [`sw-flow-sequence-action`](#sw-flow-sequence-action)
- [`sw-flow-sequence-condition`](#sw-flow-sequence-condition)
- [`sw-flow-sequence-modal`](#sw-flow-sequence-modal)
- [`sw-flow-sequence-selector`](#sw-flow-sequence-selector)
- [`sw-flow-sequence`](#sw-flow-sequence)
- [`sw-flow-set-entity-custom-field-modal`](#sw-flow-set-entity-custom-field-modal)
- [`sw-flow-set-order-state-modal`](#sw-flow-set-order-state-modal)
- [`sw-flow-tag-modal`](#sw-flow-tag-modal)
- [`sw-flow-trigger`](#sw-flow-trigger)
- [`sw-form-field-renderer`](#sw-form-field-renderer)
- [`sw-generic-cms-page-assignment`](#sw-generic-cms-page-assignment)
- [`sw-generic-custom-entity-detail`](#sw-generic-custom-entity-detail)
- [`sw-generic-custom-entity-list`](#sw-generic-custom-entity-list)
- [`sw-generic-seo-general-card`](#sw-generic-seo-general-card)
- [`sw-generic-social-media-card`](#sw-generic-social-media-card)
- [`sw-grid-column`](#sw-grid-column)
- [`sw-grid-row`](#sw-grid-row)
- [`sw-grid`](#sw-grid)
- [`sw-grouped-single-select`](#sw-grouped-single-select)
- [`sw-gtc-checkbox`](#sw-gtc-checkbox)
- [`sw-help-center-v2`](#sw-help-center-v2)
- [`sw-help-sidebar`](#sw-help-sidebar)
- [`sw-help-text`](#sw-help-text)
- [`sw-hidden-iframes`](#sw-hidden-iframes)
- [`sw-highlight-text`](#sw-highlight-text)
- [`sw-icon-deprecated`](#sw-icon-deprecated)
- [`sw-icon`](#sw-icon)
- [`sw-iframe-renderer`](#sw-iframe-renderer)
- [`sw-ignore-class`](#sw-ignore-class)
- [`sw-image-preview-modal`](#sw-image-preview-modal)
- [`sw-image-slider`](#sw-image-slider)
- [`sw-import-export-activity-log-info-modal`](#sw-import-export-activity-log-info-modal)
- [`sw-import-export-activity-result-modal`](#sw-import-export-activity-result-modal)
- [`sw-import-export-activity`](#sw-import-export-activity)
- [`sw-import-export-edit-profile-field-indicators`](#sw-import-export-edit-profile-field-indicators)
- [`sw-import-export-edit-profile-general`](#sw-import-export-edit-profile-general)
- [`sw-import-export-edit-profile-import-settings`](#sw-import-export-edit-profile-import-settings)
- [`sw-import-export-edit-profile-modal-identifiers`](#sw-import-export-edit-profile-modal-identifiers)
- [`sw-import-export-edit-profile-modal-mapping`](#sw-import-export-edit-profile-modal-mapping)
- [`sw-import-export-edit-profile-modal`](#sw-import-export-edit-profile-modal)
- [`sw-import-export-entity-path-select`](#sw-import-export-entity-path-select)
- [`sw-import-export-exporter`](#sw-import-export-exporter)
- [`sw-import-export-importer`](#sw-import-export-importer)
- [`sw-import-export-new-profile-wizard-csv-page`](#sw-import-export-new-profile-wizard-csv-page)
- [`sw-import-export-new-profile-wizard-general-page`](#sw-import-export-new-profile-wizard-general-page)
- [`sw-import-export-new-profile-wizard-mapping-page`](#sw-import-export-new-profile-wizard-mapping-page)
- [`sw-import-export-new-profile-wizard`](#sw-import-export-new-profile-wizard)
- [`sw-import-export-progress`](#sw-import-export-progress)
- [`sw-import-export-view-export`](#sw-import-export-view-export)
- [`sw-import-export-view-import`](#sw-import-export-view-import)
- [`sw-import-export-view-profiles`](#sw-import-export-view-profiles)
- [`sw-import-export`](#sw-import-export)
- [`sw-in-app-purchase-checkout`](#sw-in-app-purchase-checkout)
- [`sw-inactivity-login`](#sw-inactivity-login)
- [`sw-inherit-wrapper`](#sw-inherit-wrapper)
- [`sw-inheritance-switch`](#sw-inheritance-switch)
- [`sw-inheritance-warning`](#sw-inheritance-warning)
- [`sw-integration-list`](#sw-integration-list)
- [`sw-internal-link`](#sw-internal-link)
- [`sw-label`](#sw-label)
- [`sw-landing-page-detail-base`](#sw-landing-page-detail-base)
- [`sw-landing-page-detail-cms`](#sw-landing-page-detail-cms)
- [`sw-landing-page-tree`](#sw-landing-page-tree)
- [`sw-landing-page-view`](#sw-landing-page-view)
- [`sw-language-info`](#sw-language-info)
- [`sw-language-switch`](#sw-language-switch)
- [`sw-license-violation`](#sw-license-violation)
- [`sw-list-price-field`](#sw-list-price-field)
- [`sw-loader-deprecated`](#sw-loader-deprecated)
- [`sw-loader`](#sw-loader)
- [`sw-login-login`](#sw-login-login)
- [`sw-login-recovery-info`](#sw-login-recovery-info)
- [`sw-login-recovery-recovery`](#sw-login-recovery-recovery)
- [`sw-login-recovery`](#sw-login-recovery)
- [`sw-login`](#sw-login)
- [`sw-mail-header-footer-create`](#sw-mail-header-footer-create)
- [`sw-mail-header-footer-detail`](#sw-mail-header-footer-detail)
- [`sw-mail-header-footer-list`](#sw-mail-header-footer-list)
- [`sw-mail-template-create`](#sw-mail-template-create)
- [`sw-mail-template-detail`](#sw-mail-template-detail)
- [`sw-mail-template-index`](#sw-mail-template-index)
- [`sw-mail-template-list`](#sw-mail-template-list)
- [`sw-mail-template-view-header-footer`](#sw-mail-template-view-header-footer)
- [`sw-mail-template-view-templates`](#sw-mail-template-view-templates)
- [`sw-maintain-currencies-modal`](#sw-maintain-currencies-modal)
- [`sw-manufacturer-detail`](#sw-manufacturer-detail)
- [`sw-manufacturer-list`](#sw-manufacturer-list)
- [`sw-many-to-many-assignment-card`](#sw-many-to-many-assignment-card)
- [`sw-media-add-thumbnail-form`](#sw-media-add-thumbnail-form)
- [`sw-media-base-item`](#sw-media-base-item)
- [`sw-media-breadcrumbs`](#sw-media-breadcrumbs)
- [`sw-media-collapse`](#sw-media-collapse)
- [`sw-media-compact-upload-v2`](#sw-media-compact-upload-v2)
- [`sw-media-display-options`](#sw-media-display-options)
- [`sw-media-entity-mapper`](#sw-media-entity-mapper)
- [`sw-media-field`](#sw-media-field)
- [`sw-media-folder-content`](#sw-media-folder-content)
- [`sw-media-folder-info`](#sw-media-folder-info)
- [`sw-media-folder-item`](#sw-media-folder-item)
- [`sw-media-grid`](#sw-media-grid)
- [`sw-media-index`](#sw-media-index)
- [`sw-media-library`](#sw-media-library)
- [`sw-media-list-selection-item-v2`](#sw-media-list-selection-item-v2)
- [`sw-media-list-selection-v2`](#sw-media-list-selection-v2)
- [`sw-media-media-item`](#sw-media-media-item)
- [`sw-media-modal-delete`](#sw-media-modal-delete)
- [`sw-media-modal-folder-dissolve`](#sw-media-modal-folder-dissolve)
- [`sw-media-modal-folder-settings`](#sw-media-modal-folder-settings)
- [`sw-media-modal-move`](#sw-media-modal-move)
- [`sw-media-modal-renderer`](#sw-media-modal-renderer)
- [`sw-media-modal-replace`](#sw-media-modal-replace)
- [`sw-media-modal-v2`](#sw-media-modal-v2)
- [`sw-media-preview-v2`](#sw-media-preview-v2)
- [`sw-media-quickinfo-metadata-item`](#sw-media-quickinfo-metadata-item)
- [`sw-media-quickinfo-multiple`](#sw-media-quickinfo-multiple)
- [`sw-media-quickinfo-usage`](#sw-media-quickinfo-usage)
- [`sw-media-quickinfo`](#sw-media-quickinfo)
- [`sw-media-replace`](#sw-media-replace)
- [`sw-media-save-modal`](#sw-media-save-modal)
- [`sw-media-sidebar`](#sw-media-sidebar)
- [`sw-media-tag`](#sw-media-tag)
- [`sw-media-upload-v2`](#sw-media-upload-v2)
- [`sw-media-url-form`](#sw-media-url-form)
- [`sw-meteor-card`](#sw-meteor-card)
- [`sw-meteor-navigation`](#sw-meteor-navigation)
- [`sw-meteor-page`](#sw-meteor-page)
- [`sw-meteor-single-select`](#sw-meteor-single-select)
- [`sw-modal`](#sw-modal)
- [`sw-modals-renderer`](#sw-modals-renderer)
- [`sw-model-editor`](#sw-model-editor)
- [`sw-model-viewer`](#sw-model-viewer)
- [`sw-multi-select-filter`](#sw-multi-select-filter)
- [`sw-multi-select`](#sw-multi-select)
- [`sw-multi-snippet-drag-and-drop`](#sw-multi-snippet-drag-and-drop)
- [`sw-multi-tag-ip-select`](#sw-multi-tag-ip-select)
- [`sw-multi-tag-select`](#sw-multi-tag-select)

## sw-field-copyable

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| copyableText | `any` | `null` | no |  |
| tooltip | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `copyToClipboard` | |
| `tooltipSuccess` | |
| `notificationSuccess` | |
| `resetTooltipText` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `tooltipText` | |

### Examples

#### Basic Usage
```twig
<sw-field-copyable>
    <!-- content -->
</sw-field-copyable>
```

## sw-field-error

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| error | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `formatParameters` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `errorMessage` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-download-form/sw-product-download-form.html.twig`
```twig
<sw-field-error :error="error" />
```

#### Example 2
Source: `sw-product-stream/component/sw-product-stream-filter/sw-product-stream-filter.html.twig`
```twig
<sw-field-error :error="currentError" />
```

## sw-file-input

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| maxFileSize | `any` | `null` | no |  |
| allowedMimeTypes | `any` | `null` | no |  |
| label | `any` | `null` | no |  |
| value | `any` | — | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| caption-label | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `beforeUnmountComponent` | |
| `onChooseButtonClick` | |
| `onRemoveIconClick` | |
| `onFileInputChange` | |
| `setSelectedFile` | |
| `checkFileSize` | |
| `checkFileType` | |
| `onDragEnter` | |
| `onDragLeave` | |
| `stopEventPropagation` | |
| `onDrop` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `id` | |
| `isDragActiveClass` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-csv-page/sw-import-export-new-profile-wizard-csv-page.html.twig`
```twig
<sw-file-input
    v-model:value="csvFile"
    :allowed-mime-types="['text/csv']"
    :label="$tc('sw-import-export.profile.csvUploadText')"
    class="sw-import-export-new-profile-wizard-csv-page__file-upload"
    @update:value="onFileChange"
>
    <template #caption-label>
        {{ $tc('sw-import-export.importer.labelUploadCaption') }}
    </template>
</sw-file-input>
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-importer/sw-import-export-importer.html.twig`
```twig
<sw-file-input
    :key="isLoading"
    v-model:value="importFile"
>
    <template #caption-label>
        {{ $tc('sw-import-export.importer.labelUploadCaption') }}
    </template>
</sw-file-input>
```

## sw-filter-panel

> Filter panel with multiple configurable filter types.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filters | `any` | — | yes |  |
| defaults | `any` | — | yes |  |
| storeKey | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| criteria-changed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateFilter` | |
| `resetFilter` | |
| `resetAll` | |
| `showFilter` | |
| `getBreadcrumb` | |
| `getLabelName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `criteria` | |
| `isFilterActive` | |
| `activeFiltersNumber` | |
| `listFilters` | |

### Examples

#### Basic Usage
```twig
<sw-filter-panel
    filters="..."
    defaults="..."
    storeKey="..."
>
    <!-- content -->
</sw-filter-panel>
```

## sw-first-run-wizard-data-import

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| buttons-update | — | |
| frw-set-title | — | |
| extension-activated | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateButtons` | |
| `setTitle` | |
| `notInstalled` | |
| `onInstall` | |
| `getInstalledPlugins` | |
| `findPluginKeyByName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pluginRepository` | |
| `buttonConfig` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-data-import>
    <!-- content -->
</sw-first-run-wizard-data-import>
```

## sw-first-run-wizard-defaults

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| frw-redirect | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `nextAction` | |
| `updateButtons` | |
| `updateSalesChannel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `buttonConfig` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-defaults>
    <!-- content -->
</sw-first-run-wizard-defaults>
```

## sw-first-run-wizard-finish

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| buttons-update | — | |
| frw-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `onFinish` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `edition` | |
| `successMessage` | |
| `buttonConfig` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-finish>
    <!-- content -->
</sw-first-run-wizard-finish>
```

## sw-first-run-wizard-mailer-base

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `filteredAttributes` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-mailer-base>
    <!-- content -->
</sw-first-run-wizard-mailer-base>
```

## sw-first-run-wizard-mailer-local

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| buttons-update | — | |
| frw-set-title | — | |
| frw-redirect | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateButtons` | |
| `setTitle` | |
| `loadMailerSettings` | |
| `saveMailerSettings` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `emailSendmailOptions` | |
| `nextAction` | |
| `buttonConfig` | |
| `requiredFieldsFilled` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-mailer-local>
    <!-- content -->
</sw-first-run-wizard-mailer-local>
```

## sw-first-run-wizard-mailer-selection

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| buttons-update | — | |
| frw-set-title | — | |
| frw-redirect | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateButtons` | |
| `setTitle` | |
| `handleSelection` | |
| `setMailAgent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `nextLabel` | |
| `buttonConfig` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-mailer-selection>
    <!-- content -->
</sw-first-run-wizard-mailer-selection>
```

## sw-first-run-wizard-mailer-smtp

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| buttons-update | — | |
| frw-set-title | — | |
| frw-redirect | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateButtons` | |
| `setTitle` | |
| `loadMailerSettings` | |
| `saveMailerSettings` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `nextAction` | |
| `buttonConfig` | |
| `requiredFieldsFilled` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-mailer-smtp>
    <!-- content -->
</sw-first-run-wizard-mailer-smtp>
```

## sw-first-run-wizard-modal

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `handleRouteUpdate` | |
| `createdComponent` | |
| `updateButtons` | |
| `onButtonClick` | |
| `redirect` | |
| `setTitle` | |
| `finishFRW` | |
| `onExtensionActivated` | |
| `closeModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `columns` | |
| `variant` | |
| `showSteps` | |
| `buttons` | |
| `stepIndex` | |
| `stepInitialItemVariants` | |
| `extensionManagementDisabled` | |
| `isClosable` | |
| `stepper` | |

### Examples

#### Example 1
Source: `sw-first-run-wizard/page/index/sw-first-run-wizard.html.twig`
```twig
<sw-first-run-wizard-modal />
```

## sw-first-run-wizard-paypal-base

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `filteredAttributes` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-paypal-base>
    <!-- content -->
</sw-first-run-wizard-paypal-base>
```

## sw-first-run-wizard-paypal-credentials

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `buttonConfig` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-paypal-credentials>
    <!-- content -->
</sw-first-run-wizard-paypal-credentials>
```

## sw-first-run-wizard-paypal-info

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `installPayPal` | |
| `activatePayPalAndRedirect` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-paypal-info>
    <!-- content -->
</sw-first-run-wizard-paypal-info>
```

## sw-first-run-wizard-plugins

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| extension-activated | — | |
| frw-set-title | — | |
| buttons-update | — | |
| loading-finished | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `regionVariant` | |
| `categoryVariant` | |
| `onSelectRegion` | |
| `onSelectCategory` | |
| `getRecommendations` | |
| `getRecommendationRegions` | |
| `reloadRecommendations` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `categoryLead` | |
| `notCategoryLead` | |
| `showSpacer` | |
| `showCategoryLead` | |
| `showNotCategoryLead` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-recommendation/sw-extension-store-recommendation.html.twig`
```twig
<sw-first-run-wizard-plugins @loading-finished="finishLoading" />
```

## sw-first-run-wizard-shopware-account

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| buttons-update | — | |
| frw-redirect | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `testCredentials` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-shopware-account>
    <!-- content -->
</sw-first-run-wizard-shopware-account>
```

## sw-first-run-wizard-shopware-base

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `filteredAttributes` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-shopware-base>
    <!-- content -->
</sw-first-run-wizard-shopware-base>
```

## sw-first-run-wizard-shopware-domain

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| buttons-update | — | |
| frw-redirect | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `verifyDomain` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `domainToVerify` | |
| `isDomainEmpty` | |
| `nextAction` | |
| `domainOptions` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-shopware-domain>
    <!-- content -->
</sw-first-run-wizard-shopware-domain>
```

## sw-first-run-wizard-store

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| frw-redirect | — | |
| extension-activated | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateExtensionStatus` | |
| `activateStore` | |
| `installExtensionStore` | |
| `updateButtons` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `edition` | |
| `buttonConfig` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-store>
    <!-- content -->
</sw-first-run-wizard-store>
```

## sw-first-run-wizard-welcome

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| frw-set-title | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-first-run-wizard-welcome>
    <!-- content -->
</sw-first-run-wizard-welcome>
```

## sw-first-run-wizard

> Shopware Administration component.

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-recommendation/sw-extension-store-recommendation.html.twig`
```twig
<sw-first-run-wizard-plugins @loading-finished="finishLoading" />
```

#### Example 2
Source: `sw-first-run-wizard/page/index/sw-first-run-wizard.html.twig`
```twig
<sw-first-run-wizard-modal />
```

## sw-flow-affiliate-and-campaign-code-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| action | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fieldError` | |
| `onSave` | |
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `entityOptions` | |
| `triggerEvent` | |
| `triggerActions` | |

### Examples

#### Basic Usage
```twig
<sw-flow-affiliate-and-campaign-code-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-affiliate-and-campaign-code-modal>
```

## sw-flow-app-action-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChange` | |
| `isValid` | |
| `handleValid` | |
| `onSave` | |
| `buildConfig` | |
| `onClose` | |
| `getFields` | |
| `convertDefaultValue` | |
| `getConfig` | |
| `helpText` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `actionLabel` | |
| `appBadge` | |
| `currentLocale` | |
| `headline` | |
| `paragraph` | |

### Examples

#### Basic Usage
```twig
<sw-flow-app-action-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-app-action-modal>
```

## sw-flow-change-customer-group-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `onAddAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerGroupRepository` | |
| `customerGroupCriteria` | |
| `customerGroups` | |

### Examples

#### Basic Usage
```twig
<sw-flow-change-customer-group-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-change-customer-group-modal>
```

## sw-flow-change-customer-status-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `onAddAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerStatus` | |
| `options` | |

### Examples

#### Basic Usage
```twig
<sw-flow-change-customer-status-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-change-customer-status-modal>
```

## sw-flow-create-mail-template-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `onAddMailTemplate` | |
| `getMailTemplateType` | |
| `onChangeType` | |
| `getMailTemplate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mailTemplateRepository` | |
| `mailTemplateTypeRepository` | |
| `mailTemplateCriteria` | |
| `outerCompleterFunction` | |
| `mailTemplateContentHtmlError` | |
| `mailTemplateContentPlainError` | |
| `mailTemplateMailTemplateTypeIdError` | |
| `mailTemplateSubjectError` | |

### Examples

#### Example 1
Source: `sw-flow/component/modals/sw-flow-mail-send-modal/sw-flow-mail-send-modal.html.twig`
```twig
<sw-flow-create-mail-template-modal
    v-if="showCreateMailTemplateModal"
    class="sw-flow-mail-send-modal__create-mail-template"
    @process-finish="onCreateMailTemplateSuccess"
    @modal-close="onCloseCreateMailTemplateModal"
/>
{% endblock %}

{% block sw_flow_mail_send_modal_custom %}
{% endblock %}

{% block sw_flow_mail_send_modal_footer %}
<template #modal-footer>
    {% block sw_flow_mail_send_modal_footer_cancel_button %}
    <mt-button
```

## sw-flow-detail-flow

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| isNewFlow | `any` | `false` | no |  |
| isTemplate | `any` | `false` | no |  |
| isUnknownTrigger | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getTriggerActions` | |
| `convertSequenceData` | |
| `convertToTreeData` | |
| `createSequence` | |
| `onEventChange` | |
| `onAddRootSequence` | |
| `getSequenceId` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sequenceRepository` | |
| `formatSequences` | |
| `rootSequences` | |
| `showActionWarning` | |
| `flow` | |
| `triggerActions` | |
| `sequences` | |
| `availableActions` | |
| `hasAvailableAction` | |

### Examples

#### Basic Usage
```twig
<sw-flow-detail-flow>
    <!-- content -->
</sw-flow-detail-flow>
```

## sw-flow-detail-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| isNewFlow | `any` | `false` | no |  |
| isTemplate | `any` | `false` | no |  |
| isUnknownTrigger | `any` | `false` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `logGridColumns` | |
| `isFlowTemplate` | |
| `flow` | |
| `flowNameError` | |

### Examples

#### Basic Usage
```twig
<sw-flow-detail-general>
    <!-- content -->
</sw-flow-detail-general>
```

## sw-flow-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| flowId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `routeDetailTab` | |
| `createNewFlow` | |
| `getDetailFlow` | |
| `getAppFlowAction` | |
| `getDetailFlowTemplate` | |
| `onSave` | |
| `updateSequences` | |
| `getDeletedSequenceIds` | |
| `handleFieldValiationError` | |
| `saveFinish` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `removeAllSelectors` | |
| `validateEmptySequence` | |
| `getDataForActionDescription` | |
| `createFromFlowTemplate` | |
| `createSequenceEntity` | |
| `buildSequencesFromConfig` | |
| `getRuleDataForFlowTemplate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `flowRepository` | |
| `flowTemplateRepository` | |
| `flowSequenceRepository` | |
| `appFlowActionRepository` | |
| `isNewFlow` | |
| `flowCriteria` | |
| `flowTemplateCriteria` | |
| `documentTypeRepository` | |
| `documentTypeCriteria` | |
| `mailTemplateRepository` | |
| `customFieldSetRepository` | |
| `customFieldRepository` | |
| `mailTemplateIdsCriteria` | |
| `customerGroupRepository` | |
| `customerGroupCriteria` | |
| `appFlowActionCriteria` | |
| `stateMachineStateRepository` | |
| `stateMachineStateCriteria` | |
| `customFieldSetCriteria` | |
| `customFieldCriteria` | |
| `ruleRepository` | |
| `isTemplate` | |
| `isUnknownTrigger` | |
| `flow` | |
| `triggerEvents` | |
| `sequences` | |
| `mailTemplateIds` | |
| `customFieldSetIds` | |
| `customFieldIds` | |
| `hasFlowChanged` | |
| `flowNameError` | |
| `flowEventNameError` | |

### Examples

#### Basic Usage
```twig
<sw-flow-detail>
    <!-- content -->
</sw-flow-detail>
```

## sw-flow-event-change-confirm-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-confirm | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sequences` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-trigger/sw-flow-trigger.html.twig`
```twig
    <sw-flow-event-change-confirm-modal
        v-if="showConfirmModal"
        @modal-confirm="onConfirm"
        @modal-close="onCloseConfirm"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-flow-generate-document-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `onAddAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `documentTypeRepository` | |
| `documentTypeCriteria` | |
| `documentTypes` | |

### Examples

#### Basic Usage
```twig
<sw-flow-generate-document-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-generate-document-modal>
```

## sw-flow-grant-download-access-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| action | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getConfig` | |
| `fieldError` | |
| `onSave` | |
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `valueOptions` | |
| `triggerEvent` | |
| `triggerActions` | |

### Examples

#### Basic Usage
```twig
<sw-flow-grant-download-access-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-grant-download-access-modal>
```

## sw-flow-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createComponent` | |
| `getTotal` | |
| `onUpdateTotalFlow` | |
| `onSearch` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `flowRepository` | |
| `flowCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-flow-index>
    <!-- content -->
</sw-flow-index>
```

## sw-flow-leave-page-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-leave-confirm | — | |
| page-leave-cancel | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `onCancel` | |

### Examples

#### Example 1
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

## sw-flow-list-flow-templates

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createComponent` | |
| `getList` | |
| `onEditFlow` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `flowTemplateRepository` | |
| `flowTemplateCriteria` | |
| `flowTemplateColumns` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-flow-list-flow-templates>
    <!-- content -->
</sw-flow-list-flow-templates>
```

## sw-flow-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `''` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-update-total | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createComponent` | |
| `getList` | |
| `isValidTrigger` | |
| `onDuplicateFlow` | |
| `onEditFlow` | |
| `onDeleteFlow` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `updateRecords` | |
| `getTranslatedEventName` | |
| `selectionChange` | |
| `deleteWarningMessage` | |
| `bulkDeleteWarningMessage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `flowRepository` | |
| `flowCriteria` | |
| `flowColumns` | |
| `detailPageLinkText` | |
| `assetFilter` | |
| `triggerEvents` | |

### Examples

#### Basic Usage
```twig
<sw-flow-list>
    <!-- content -->
</sw-flow-list>
```

## sw-flow-mail-send-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClose` | |
| `getRecipientData` | |
| `isRecipientGridError` | |
| `onAddAction` | |
| `onCreateMailTemplate` | |
| `onCloseCreateMailTemplateModal` | |
| `onCreateMailTemplateSuccess` | |
| `onChangeMailTemplate` | |
| `onChangeRecipient` | |
| `addRecipient` | |
| `saveRecipient` | |
| `cancelSaveRecipient` | |
| `onEditRecipient` | |
| `onDeleteRecipient` | |
| `mailTemplateError` | |
| `setNameError` | |
| `setMailError` | |
| `validateRecipient` | |
| `resetError` | |
| `allowDeleteRecipient` | |
| `changeShowReplyToField` | |
| `buildReplyToTooltip` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mailTemplateCriteria` | |
| `documentTypeRepository` | |
| `isNewMail` | |
| `recipientCustomer` | |
| `recipientAdmin` | |
| `recipientCustom` | |
| `recipientDefault` | |
| `recipientContactFormMail` | |
| `entityAware` | |
| `recipientOptions` | |
| `recipientColumns` | |
| `replyToOptions` | |
| `replyToSelection` | |
| `showReplyToField` | |
| `mailTemplates` | |
| `triggerEvent` | |
| `triggerActions` | |

### Examples

#### Basic Usage
```twig
<sw-flow-mail-send-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-mail-send-modal>
```

## sw-flow-rule-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadConditionData` | |
| `createRule` | |
| `loadRule` | |
| `loadConditions` | |
| `syncConditions` | |
| `onConditionsChanged` | |
| `getRuleDetail` | |
| `onSaveRule` | |
| `saveRule` | |
| `showErrorNotification` | |
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `ruleRepository` | |
| `conditionRepository` | |
| `appScriptConditionRepository` | |
| `availableModuleTypes` | |
| `moduleTypes` | |
| `scopesOfRuleAwarenessKey` | |
| `flow` | |
| `ruleNameError` | |
| `rulePriorityError` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence-condition/sw-flow-sequence-condition.html.twig`
```twig
    <sw-flow-rule-modal
        v-if="showCreateRuleModal"
        :rule-id="selectedRuleId"
        @process-finish="onSaveRuleSuccess"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-flow-sequence-action-error

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |

### Methods

| Method | Description |
|--------|-------------|
| `removeWarning` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sequences` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-flow-sequence-action-error
    v-if="!isValidAction(item.actionName)"
    :sequence="item"
>
    <template #content>
        <div class="sw-flow-sequence-action__error-action">
            <div class="sw-flow-sequence-action__error-action-title">
                <mt-icon
                    name="regular-question-circle-s"
                    size="14px"
                    class="mt-icon-action"
                />

                <span>{{ $tc('sw-flow.actions.unknownLabel') }}</span>
            </div>
```

## sw-flow-sequence-action

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| isUnknownTrigger | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `openDynamicModal` | |
| `onSaveActionSuccess` | |
| `onCloseModal` | |
| `addAction` | |
| `editAction` | |
| `removeAction` | |
| `actionsWithoutStopFlow` | |
| `showMoveOption` | |
| `moveAction` | |
| `onEditAction` | |
| `removeActionContainer` | |
| `getActionTitle` | |
| `sortByPosition` | |
| `stopFlowStyle` | |
| `getActionDescriptions` | |
| `setFieldError` | |
| `removeFieldError` | |
| `isNotStopFlow` | |
| `capitalize` | |
| `isAppDisabled` | |
| `getStopFlowIndex` | |
| `sortActionOptions` | |
| `isValidAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sequenceRepository` | |
| `customFieldSetRepository` | |
| `actionOptions` | |
| `groups` | |
| `sequenceData` | |
| `showAddAction` | |
| `stopFlowActionName` | |
| `actionClasses` | |
| `errorArrow` | |
| `modalName` | |
| `currentLocale` | |
| `invalidSequences` | |
| `stateMachineState` | |
| `documentTypes` | |
| `mailTemplates` | |
| `customerGroups` | |
| `customFieldSets` | |
| `customFields` | |
| `triggerEvent` | |
| `triggerActions` | |
| `availableActions` | |
| `actionGroups` | |
| `sequences` | |
| `appActions` | |
| `getSelectedAppAction` | |
| `hasAvailableAction` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-action
    v-show="isActionSequence"
    :sequence="sequenceData"
    :disabled="disabled"
    :is-unknown-trigger="isUnknownTrigger"
/>
{% endblock %}

{% block sw_flow_sequence_extension %}{% endblock %}

{% block sw_flow_sequence_true_block %}
<div
    v-if="sequenceData.trueBlock"
    class="sw-flow-sequence__true-block"
    :class="trueBlockClasses"
```

#### Example 2
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-flow-sequence-action-error
    v-if="!isValidAction(item.actionName)"
    :sequence="item"
>
    <template #content>
        <div class="sw-flow-sequence-action__error-action">
            <div class="sw-flow-sequence-action__error-action-title">
                <mt-icon
                    name="regular-question-circle-s"
                    size="14px"
                    class="mt-icon-action"
                />

                <span>{{ $tc('sw-flow.actions.unknownLabel') }}</span>
            </div>
```

## sw-flow-sequence-condition

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onCreateNewRule` | |
| `onCloseModal` | |
| `onSaveRuleSuccess` | |
| `onRuleChange` | |
| `deleteRule` | |
| `addIfCondition` | |
| `addThenAction` | |
| `showArrowIcon` | |
| `disabledAddSequence` | |
| `arrowClasses` | |
| `removeCondition` | |
| `createSequence` | |
| `setFieldError` | |
| `removeFieldError` | |
| `toggleAddButton` | |
| `onEditRule` | |
| `isRuleDisabled` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `restrictedRules` | |
| `flow` | |
| `invalidSequences` | |
| `sequences` | |
| `sequenceRepository` | |
| `ruleRepository` | |
| `ruleCriteria` | |
| `showHelpElement` | |
| `modalName` | |
| `ruleDescription` | |
| `advanceSelectionParameters` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-condition
    v-if="isConditionSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

{% block sw_flow_sequence_action %}
<sw-flow-sequence-action
    v-show="isActionSequence"
    :sequence="sequenceData"
    :disabled="disabled"
    :is-unknown-trigger="isUnknownTrigger"
/>
{% endblock %}
```

## sw-flow-sequence-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| modalName | `any` | — | yes |  |
| action | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `processSuccess` | |
| `onClose` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
    <sw-flow-sequence-modal
        :sequence="currentSequence"
        :action="selectedAction"
        :modal-name="modalName"
        @process-finish="onSaveActionSuccess"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-flow-sequence-selector

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| helpText | — | |

### Methods

| Method | Description |
|--------|-------------|
| `addIfCondition` | |
| `addThenAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `title` | |
| `helpText` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-selector
    v-if="isSelectorSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

{% block sw_flow_sequence_condition %}
<sw-flow-sequence-condition
    v-if="isConditionSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

```

## sw-flow-sequence

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| isUnknownTrigger | `any` | `false` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `sequenceData` | |
| `isSelectorSequence` | |
| `isConditionSequence` | |
| `isActionSequence` | |
| `trueBlockClasses` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
<sw-flow-sequence-selector
    v-if="isSelectorSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

{% block sw_flow_sequence_condition %}
<sw-flow-sequence-condition
    v-if="isConditionSequence"
    :disabled="disabled"
    :sequence="sequenceData"
/>
{% endblock %}

```

#### Example 2
Source: `sw-flow/component/sw-flow-sequence/sw-flow-sequence.html.twig`
```twig
        <sw-flow-sequence
            :sequence="sequenceData.trueBlock"
            :disabled="disabled"
        />
    </div>
    {% endblock %}

    {% block sw_flow_sequence_false_block %}
    <div
        v-if="sequenceData.falseBlock"
        class="sw-flow-sequence__false-block"
    >
        <sw-flow-sequence
            :sequence="sequenceData.falseBlock"
            :disabled="disabled"
```

#### Example 3
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-flow-sequence-action-error
    v-if="!isValidAction(item.actionName)"
    :sequence="item"
>
    <template #content>
        <div class="sw-flow-sequence-action__error-action">
            <div class="sw-flow-sequence-action__error-action-title">
                <mt-icon
                    name="regular-question-circle-s"
                    size="14px"
                    class="mt-icon-action"
                />

                <span>{{ $tc('sw-flow.actions.unknownLabel') }}</span>
            </div>
```

#### Example 4
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
    <sw-flow-sequence-modal
        :sequence="currentSequence"
        :action="selectedAction"
        :modal-name="modalName"
        @process-finish="onSaveActionSuccess"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 5
Source: `sw-flow/view/detail/sw-flow-detail-flow/sw-flow-detail-flow.html.twig`
```twig
                        <sw-flow-sequence
                            name="root-sequence"
                            :sequence="sequence"
                            :disabled="!acl.can('flow.editor')"
                            :is-unknown-trigger="isUnknownTrigger"
                        />
                    </div>
                    {% endblock %}
                </div>
                {% endblock %}
            </transition-group>
            {% endblock %}
        </div>
        {% endblock %}
    </div>
```

## sw-flow-set-entity-custom-field-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| action | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getCustomFieldRendered` | |
| `onEntityChange` | |
| `onCustomFieldSetChange` | |
| `onCustomFieldChange` | |
| `validateOptionSelectFieldLabel` | |
| `onClose` | |
| `onAddAction` | |
| `fieldError` | |
| `getFieldOptions` | |
| `getEntityOptions` | |
| `convertToEntityTechnicalName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `customFieldCriteria` | |
| `customFieldSetCriteria` | |
| `showFieldValue` | |
| `defaultFieldOptions` | |
| `multipleFieldOptions` | |
| `labelProperty` | |
| `triggerEvent` | |
| `customFieldSets` | |
| `customFields` | |
| `triggerActions` | |

### Examples

#### Basic Usage
```twig
<sw-flow-set-entity-custom-field-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-set-entity-custom-field-modal>
```

## sw-flow-set-order-state-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| process-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getAllStates` | |
| `generateOptions` | |
| `buildTransitionOptions` | |
| `onClose` | |
| `onAddAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineStateCriteria` | |
| `stateMachineState` | |

### Examples

#### Basic Usage
```twig
<sw-flow-set-order-state-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-set-order-state-modal>
```

## sw-flow-tag-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sequence | `any` | — | yes |  |
| action | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getTagCollection` | |
| `createTagCollection` | |
| `onAddTag` | |
| `onRemoveTag` | |
| `getEntityOptions` | |
| `getConfig` | |
| `fieldError` | |
| `onSaveTag` | |
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `tagCriteria` | |
| `isNewTag` | |
| `tagRepository` | |
| `tagTitle` | |
| `triggerEvent` | |
| `triggerActions` | |

### Examples

#### Basic Usage
```twig
<sw-flow-tag-modal
    sequence="..."
>
    <!-- content -->
</sw-flow-tag-modal>
```

## sw-flow-trigger

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| overlay | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| eventName | `any` | — | yes |  |
| isUnknownTrigger | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| option-select | — | |

### Methods

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

### Computed Properties

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

### Examples

#### Example 1
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

## sw-form-field-renderer

> Dynamic form field renderer that generates form inputs from custom field definitions.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | `null` | no |  |
| config | `any` | `null` | no |  |
| value | `any` | — | yes |  |
| error | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| slotName | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitUpdate` | |
| `getTranslations` | |
| `getComponentFromType` | |
| `createRepository` | |
| `fetchSystemCurrency` | |
| `getScopedSlots` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `bind` | |
| `hasConfig` | |
| `componentName` | |
| `swFieldType` | |
| `translations` | |
| `optionTranslations` | |
| `componentPropName` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/sw-bulk-edit-custom-fields/sw-bulk-edit-custom-fields.html.twig`
```twig
                    <sw-form-field-renderer
                        v-bind="getBind(customField, props)"
                        :key="props.isInherited"
                        :class="'sw-form-field-renderer-input-field__' + customField.name"
                        :disabled="disabled || props.isInherited"
                        :value="props.currentValue"
                        @update:value="props.updateCurrentValue"
                    />
                </template>
            </sw-inherit-wrapper>
            {% endblock %}
        </sw-container>
    </template>
</div>
{% endblock %}
```

#### Example 2
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
        <sw-form-field-renderer
            v-else-if="formField"
            v-model:value="documentConfig.config[formField.name]"
            :disabled="!acl.can('document.editor') || undefined"
            class="sw-settings-document-detail__form-field-renderer"
            v-bind="formField"
        />

        <div
            v-else
            :key="`else-formField-${index}`"
        ></div>
        {% endblock %}
    </template>
</template>
```

#### Example 3
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
                            <sw-form-field-renderer
                                v-model:value="documentConfig.config[formField.name]"
                                :disabled="!acl.can('document.editor') || undefined"
                                v-bind="formField"
                            />
                            {% endblock %}
                        </template>
                    </template>
                    {% endblock %}
                </sw-container>
            </mt-card>
            {% endblock %}

            {% block sw_settings_document_detail_custom_field_sets %}
            <mt-card
```

#### Example 4
Source: `sw-settings/component/sw-system-config/sw-system-config.html.twig`
```twig
            <sw-form-field-renderer
                v-if="props"
                v-bind="getMeteorElementBind(element, props)"
                v-on="getMeteorElementEventsHandler(element, props)"
            />
        </template>
    </sw-inherit-wrapper>
</template>

<template v-else>
{% block sw_system_config_content_card_field %}
    <sw-inherit-wrapper
        v-model:value="actualConfigData[currentSalesChannelId][element.name]"
        v-bind="getInheritWrapperBind(element)"
        :has-parent="isNotDefaultSalesChannel"
```

#### Example 5
Source: `sw-flow/component/modals/sw-flow-app-action-modal/sw-flow-app-action-modal.html.twig`
```twig
<sw-form-field-renderer
    v-for="field in fields"
    :key="field.name"
    v-model:value="config[field.name]"
    :type="field.type"
    :config="getConfig(field)"
    :error="errors[field.name]"
    @update:value="onChange($event, field)"
/>

{% endblock %}
<template #modal-footer>
    {% block sw_flow_app_action_modal_footer_cancel_button %}
    <mt-button
        class="sw-flow-app-action-modal__cancel-button"
```

## sw-generic-cms-page-assignment

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| cmsPageId | `any` | `null` | no |  |
| slotOverrides | `any` | `null` | no |  |
| allowedPageTypes | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `openLayoutModal` | |
| `closeLayoutModal` | |
| `onLayoutSelect` | |
| `openInCmsEditor` | |
| `createNewLayout` | |
| `applySlotOverrides` | |
| `getCmsPage` | |
| `deleteSpecificKeys` | |
| `emitCmsPageOverrides` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cmsPageRepository` | |
| `changesetGenerator` | |
| `cmsPageCriteria` | |
| `pageTypeTitle` | |

### Examples

#### Example 1
Source: `sw-custom-entity/page/sw-generic-custom-entity-detail/sw-generic-custom-entity-detail.html.twig`
```twig
<sw-generic-cms-page-assignment
    v-if="active === 'cms-aware-tab-layout'"
    :cms-page-id="customEntityData?.swCmsPageId"
    :slot-overrides="customEntityData?.swSlotConfig"
    class="sw-generic-custom-entity-detail__tab sw-generic-custom-entity-detail__tab-cms-aware"
    @update:cms-page-id="updateCmsPageId"
    @update:slot-overrides="updateCmsSlotOverwrites"
    @create-layout="onCreateLayout"
/>

<template
    v-else-if="active === 'cms-aware-tab-seo'"
>
    <sw-generic-seo-general-card
        :seo-meta-title="customEntityData?.swSeoMetaTitle"
```

## sw-generic-custom-entity-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initializeCustomEntity` | |
| `loadData` | |
| `onSave` | |
| `saveFinish` | |
| `onChangeLanguage` | |
| `getFieldTranslation` | |
| `getLabel` | |
| `getPlaceholder` | |
| `getHelpText` | |
| `getType` | |
| `updateCmsPageId` | |
| `updateCmsSlotOverwrites` | |
| `updateSeoMetaTitle` | |
| `updateSeoMetaDescription` | |
| `updateSeoUrl` | |
| `updateOgTitle` | |
| `updateOgDescription` | |
| `updateOgImageId` | |
| `onCreateLayout` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customEntityDataId` | |
| `customEntityName` | |
| `customEntityDataDefinition` | |
| `customEntityDataRepository` | |
| `customEntityProperties` | |
| `adminConfig` | |
| `entityAccentColor` | |
| `detailTabs` | |
| `mainTabName` | |
| `titlePropertyName` | |

### Examples

#### Basic Usage
```twig
<sw-generic-custom-entity-detail>
    <!-- content -->
</sw-generic-custom-entity-detail>
```

## sw-generic-custom-entity-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `onChangeLanguage` | |
| `parseSortDirection` | |
| `parseRoute` | |
| `updateRoute` | |
| `onSearch` | |
| `onColumnSort` | |
| `onPageChange` | |
| `onUpdateRecords` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customEntityName` | |
| `customEntityDefinition` | |
| `customEntityRepository` | |
| `adminConfig` | |
| `entityAccentColor` | |
| `columnConfig` | |
| `customEntityCriteria` | |
| `emptyStateTitle` | |
| `emptyStateSubline` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-generic-custom-entity-list>
    <!-- content -->
</sw-generic-custom-entity-list>
```

## sw-generic-seo-general-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| seoMetaTitle | `any` | `''` | no |  |
| seoMetaDescription | `any` | `''` | no |  |
| seoUrl | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `emitSeoMetaTitle` | |
| `emitSeoMetaDescription` | |
| `emitSeoUrl` | |

### Examples

#### Example 1
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

## sw-generic-social-media-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ogTitle | `any` | `''` | no |  |
| ogDescription | `any` | `''` | no |  |
| ogImageId | `any` | `null` | no |  |

### Methods

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

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `uploadTag` | |

### Examples

#### Example 1
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

## sw-grid-column

> Shopware Administration component.

- [Slots](#slots)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `any` | `null` | no |  |
| iconLabel | `any` | `null` | no |  |
| align | `any` | `'left'` | no |  |
| flex | `any` | `1` | no |  |
| sortable | `any` | `false` | no |  |
| dataIndex | `any` | `''` | no |  |
| editable | `any` | `false` | no |  |
| truncate | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| inline-edit | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerColumn` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `parentGrid` | |

### Examples

#### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid-column
    :label="$tc('sw-product.visibility.columnSalesChannel')"
    flex="0.5fr"
    align="left"
>
    {% block sw_settings_listing_visibility_detail_columns_sales_channel_label %}
    <span
        v-tooltip="{ message: item.name, disabled: item.name.length < 10 }"
        class="sw-product-visibility-detail__name"
    >
        {{ truncateFilter(item.name, 30) }}
    </span>
    {% endblock %}
</sw-grid-column>
```

#### Example 2
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid-column
    :label="$tc('sw-product.visibility.columnAll')"
    flex="0.3fr"
    align="left"
>
    <sw-radio-field
        :disabled="disabled"
        :value="item.visibility"
        :name="'visibility' + item.id"
        :options="[{ value: 30 }]"
        @update:value="changeVisibilityValue($event, item)"
    />
</sw-grid-column>
```

#### Example 3
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
<sw-grid-column
    flex="minmax(100px, 2fr)"
    :label="$tc('sw-import-export.activity.result.entityName')"
    :class="`sw-import-export-activity-result-modal__column-${item.entityName}-label`"
>
    {{ item.entityName }}
</sw-grid-column>
```

#### Example 4
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
<sw-grid-column
    flex="minmax(50px, 1fr)"
    :label="$tc('sw-import-export.activity.result.changes')"
    :class="`sw-import-export-activity-result-modal__column-${item.entityName}-changes`"
>
    {{ item.insert + item.update }}
</sw-grid-column>
```

#### Example 5
Source: `sw-settings-document/page/sw-settings-document-list/sw-settings-document-list.html.twig`
```twig
<sw-grid-column
    class="sw-document-list__column-name"
    flex="minmax(100px, 1fr)"
    :label="$tc('sw-settings-document.list.columnName')"
>
    {% block sw_settings_document_list_columns_name_link %}
    <mt-link :to="{ name: 'sw.settings.document.detail', params: { id: item.id } }">
            {% block sw_settings_document_list_columns_name_link_inner %}
        {{ item.name }}
            {% endblock %}
    </mt-link>
    {% endblock %}
</sw-grid-column>
```

## sw-grid-row

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| index | `any` | `null` | no |  |
| allowInlineEdit | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| actions | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inline-edit-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onInlineEditStart` | |
| `onInlineEditCancel` | |
| `onInlineEditFinish` | |
| `startInlineEditing` | |

### Examples

#### Basic Usage
```twig
<sw-grid-row
    item="..."
>
    <!-- content -->
</sw-grid-row>
```

## sw-grid

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | `null` | no |  |
| selectable | `any` | `true` | no |  |
| variant | `any` | `'normal'` | no |  |
| header | `any` | `true` | no |  |
| sortBy | `any` | `null` | no |  |
| sortDirection | `any` | `'ASC'` | no |  |
| isFullpage | `any` | `false` | no |  |
| table | `any` | `false` | no |  |
| allowInlineEdit | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |
| header | — | |
| body | — | |
| items | — | |
| columns | item: item | |
| empty | — | |
| pagination | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inline-edit-finish | — | |
| inline-edit-start | — | |
| sw-grid-disable-inline-editing | — | |
| inline-edit-cancel | — | |
| sw-grid-select-all | — | |
| sw-grid-select-item | — | |
| sort-column | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updatedComponent` | |
| `registerGridDisableInlineEditListener` | |
| `unregisterGridDisableInlineEditListener` | |
| `onInlineEditFinish` | |
| `onInlineEditStart` | |
| `registerInlineEditingEvents` | |
| `inlineEditingStart` | |
| `disableActiveInlineEditing` | |
| `selectAll` | |
| `getSelection` | |
| `selectItem` | |
| `isSelected` | |
| `checkSelection` | |
| `getScrollBarWidth` | |
| `onGridCellClick` | |
| `setScrollbarOffset` | |
| `setColumns` | |
| `getKey` | |
| `startInlineEditing` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sort` | |
| `sortDir` | |
| `sizeClass` | |
| `hasPaginationSlot` | |
| `gridClasses` | |
| `gridContentClasses` | |
| `columnFlex` | |

### Examples

#### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid
    class="sw-settings-listing-visibility-detail"
    table
    :items="items"
    :selectable="false"
>
    {% block sw_settings_listing_visibility_detail_columns %}
    <template #columns="{ item }">
        {% block sw_settings_listing_visibility_detail_columns_sales_channel %}
        <sw-grid-column
            :label="$tc('sw-product.visibility.columnSalesChannel')"
            flex="0.5fr"
            align="left"
        >
            {% block sw_settings_listing_visibility_detail_columns_sales_channel_label %}
```

#### Example 2
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
<sw-grid-column
    :label="$tc('sw-product.visibility.columnSearchOnly')"
    flex="0.7fr"
    align="left"
>
    <sw-radio-field
        :disabled="disabled"
        :value="item.visibility"
        :name="'visibility' + item.id"
        :options="[{ value: 20 }]"
        @update:value="changeVisibilityValue($event, item)"
    />
</sw-grid-column>
{% endblock %}

```

#### Example 3
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
<sw-grid
    table
    :items="result"
    :selectable="false"
>
    {% block sw_import_export_activity_result_modal_activity_table_columns %}
    <template #columns="{ item }">
        {% block sw_import_export_activity_result_modal_activity_table_columns_label %}
        <sw-grid-column
            flex="minmax(100px, 2fr)"
            :label="$tc('sw-import-export.activity.result.entityName')"
            :class="`sw-import-export-activity-result-modal__column-${item.entityName}-label`"
        >
            {{ item.entityName }}
        </sw-grid-column>
```

#### Example 4
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
        <sw-grid-column
            flex="minmax(50px, 1fr)"
            :label="$tc('sw-import-export.activity.result.skipped')"
            :class="`sw-import-export-activity-result-modal__column-${item.entityName}-skipped`"
        >
            {{ item.insertSkip + item.updateSkip }}
        </sw-grid-column>
        {% endblock %}
    </template>
    {% endblock %}
</sw-grid>
```

#### Example 5
Source: `sw-settings-document/page/sw-settings-document-list/sw-settings-document-list.html.twig`
```twig
<sw-grid
    class="sw-settings-document-list-grid"
    :items="items"
    :selectable="false"
    table
>
    <template #columns="{ item }">
        {% block sw_product_list_grid_columns %}

        {% block sw_settings_document_list_columns_name %}
        <sw-grid-column
            class="sw-document-list__column-name"
            flex="minmax(100px, 1fr)"
            :label="$tc('sw-settings-document.list.columnName')"
        >
```

## sw-grouped-single-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| groups | `any` | — | yes |  |
| groupIdProperty | `any` | `'id'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-group | — | |
| result-item | — | |
| result-label-property | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getGroupClasses` | |
| `getGroupLabel` | |
| `shouldShowGroupTitle` | |

### Examples

#### Example 1
Source: `sw-flow/component/sw-flow-sequence-action/sw-flow-sequence-action.html.twig`
```twig
<sw-grouped-single-select
    class="sw-flow-sequence-action__selection-action"
    size="small"
    value=""
    :placeholder="$tc('sw-flow.actions.placeholderSelectAction')"
    :options="actionOptions"
    :groups="groups"
    :popover-classes="['sw-flow-sequence-action__popover']"
    :error="fieldError"
    :disabled="isUnknownTrigger"
    @update:value="openDynamicModal"
>
    <template #result-item="{ item, index, labelProperty, highlightSearchTerm, isSelected, setValue, getKey }">
        <sw-select-result
            v-tooltip="{
```

## sw-gtc-checkbox

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation/sw-extension-review-creation.html.twig`
```twig
    <sw-gtc-checkbox
        v-model:value="tocAccepted"
    />
    {% endblock %}

    {% block sw_extension_review_creation_buttons %}
    <div class="sw-extension-review-creation__buttons">
        {% block sw_extension_review_creation_buttons_submit_button %}
        <sw-button-process
            class="sw-extension-review-creation__submit"
            variant="primary"
            size="small"
            :is-loading="isLoading"
            :process-success="isCreatedSuccessful"
            :disabled="disabled"
```

#### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-rating-modal/sw-extension-rating-modal.html.twig`
```twig
<sw-gtc-checkbox
    v-model:value="tocAccepted"
/>
{% endblock %}

{% block sw_extension_rating_modal_slot_footer_buttons %}
<div class="sw-extension-rating-modal__buttons">
    {% block sw_extension_rating_modal_slot_footer_buttons_cancel %}
    <mt-button
        size="small"
        :disabled="isLoading"
        variant="secondary"
        @click="emitClose"
    >
        {{ $tc('global.default.cancel') }}
```

## sw-help-center-v2

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `openHelpSidebar` | |
| `openShortcutModal` | |
| `closeShortcutModal` | |
| `setFocusToSidebar` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showHelpSidebar` | |
| `showShortcutModal` | |

### Examples

#### Basic Usage
```twig
<sw-help-center-v2>
    <!-- content -->
</sw-help-center-v2>
```

## sw-help-sidebar

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selector | `any` | `'body'` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeUnmountComponent` | |
| `unmountedComponent` | |
| `setFocusToSidebar` | |
| `mouseDown` | |
| `escKey` | |
| `closeHelpSidebar` | |
| `openShortcutModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showHelpSidebar` | |

### Examples

#### Basic Usage
```twig
<sw-help-sidebar>
    <!-- content -->
</sw-help-sidebar>
```

## sw-help-text

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | `''` | yes |  |
| width | `any` | `200` | no |  |
| tooltipPosition | `any` | `'top'` | no | Valid: `top`, `bottom`, `left`, `right` |
| showDelay | `any` | `100` | no |  |
| hideDelay | `any` | `100` | no |  |

### Examples

#### Example 1
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
        <sw-help-text
            :width="380"
            :text="$t('sw-settings-number-range.detail.helpTextAdvancedField')"
        />
    </div>
    {% endblock %}
</sw-container>

<sw-container
    columns="repeat(auto-fit, minmax(250px, 1fr))"
    gap="0px 30px"
>
    {% block sw_settings_number_range_detail_content_field_current_number %}
    <mt-text-field
        v-if="state"
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-help-text
        class="sw-import-export-activity__invalid-records-help-text"
        :text="$t('sw-import-export.activity.invalidHelpText')"
    />
</template>
{% block sw_import_export_activity_listing_invalid_records %}

<template #column-invalidRecords="{ item }">
    <template v-if="item.invalidRecordsLog">
        {{ item.invalidRecordsLog.records }}
    </template>

    <template v-else>
        0
    </template>
```

#### Example 3
Source: `sw-first-run-wizard/view/sw-first-run-wizard-mailer-selection/sw-first-run-wizard-mailer-selection.html.twig`
```twig
    <sw-help-text
        class="sw-first-run-wizard-mailer-selection__help-text"
        :text="$tc('sw-first-run-wizard.mailerSelection.localOptionHelptext')"
    />

    <mt-icon
        name="regular-paper-plane"
        class="sw-first-run-wizard-mailer-selection__selection-icon"
    />

    <p>
        <span>{{ $tc('sw-first-run-wizard.mailerSelection.localOption') }}</span>
        <br>
        <span>{{ $tc('sw-first-run-wizard.mailerSelection.localOptionSubline') }}</span>
    </p>
```

#### Example 4
Source: `sw-customer/component/sw-customer-base-info/sw-customer-base-info.html.twig`
```twig
<sw-help-text :text="$tc('sw-customer.baseInfo.helpTextBoundSalesChannel')" />
```

#### Example 5
Source: `sw-settings-custom-field/page/sw-settings-custom-field-set-list/sw-settings-custom-field-set-list.html.twig`
```twig
        <sw-help-text
            class="sw-settings-custom-field-set-list__help-text-global-set"
            :text="$tc('sw-settings-custom-field.set.list.helpTextGlobalSet')"
        />
    </template>
    <template v-else>
        <router-link
            :title="$tc('sw-settings-custom-field.set.list.contextMenuEdit')"
            class="sw-custom-field-set-list__column-name"
            :to="{ name: 'sw.settings.custom.field.detail', params: { id: item.id } }"
        >
            {{ getInlineSnippet(item.config.label) || item.name }}
        </router-link>
    </template>
</sw-grid-column>
```

## sw-hidden-iframes

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `extensions` | |
| `MAIN_HIDDEN` | |

### Examples

#### Basic Usage
```twig
<sw-hidden-iframes>
    <!-- content -->
</sw-hidden-iframes>
```

## sw-highlight-text

> Shopware Administration component.

- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `null` | no |  |
| text | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `searchAndReplace` | |
| `escapeRegExp` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
                <sw-highlight-text
                    v-if="highlightSearchTerm && !isSelected(item)"
                    :text="getKey(item, labelProperty)"
                    :search-term="searchTerm"
                />
                {% endblock %}

                {% block sw_import_export_edit_profile_general_container_object_type_select_result_text %}
                <template v-else>
                    {{ getKey(item, labelProperty) }}
                </template>
                {% endblock %}
            </sw-select-result>
            {% endblock %}
        </template>
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
                    <sw-highlight-text
                        v-if="highlightSearchTerm && !isSelected(item)"
                        :text="getKey(item, labelProperty)"
                        :search-term="searchTerm"
                    />
                    {% endblock %}

                    {% block sw_import_export_edit_profile_general_container_type_result_text %}
                    <template v-else>
                        {{ getKey(item, labelProperty) }}
                    </template>
                    {% endblock %}
                </sw-select-result>
                {% endblock %}
            </template>
```

#### Example 3
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
                    <sw-highlight-text
                        v-if="highlightSearchTerm"
                        :text="getKey(item, labelProperty)"
                        :search-term="searchTerm"
                    />

                    <template v-else>
                        {{ getKey(item, labelProperty) }}
                    </template>

                    <mt-icon
                        v-if="item.relation && item.relation !== 'many_to_many'"
                        name="regular-chevron-right-xs"
                        size="10px"
                    />
```

#### Example 4
Source: `sw-cms/component/sw-cms-product-assignment/sw-cms-product-assignment.html.twig`
```twig
                                <sw-highlight-text
                                    v-if="highlightSearchTerm"
                                    :text="getKey(item, `translated.${labelProperty}`)"
                                    :search-term="searchTerm"
                                />

                                <template v-else>
                                    {{ getKey(item, `translated.${labelProperty}`) }}
                                </template>
                            </slot>
                        {% endblock %}
                        </sw-select-result>
                    {% endblock %}
                    </slot>
                {% endblock %}
```

#### Example 5
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
                                <sw-highlight-text
                                    v-if="highlightSearchTerm"
                                    :text="getKey(item,labelProperty) || getKey(item, `translated.${labelProperty}`)"
                                    :search-term="searchTerm"
                                />
                                <template v-else>
                                    {{ getKey(item,labelProperty) || getKey(item, `translated.${labelProperty}`) }}
                                </template>
                            </slot>
                            {% endblock %}
                        </sw-select-result>
                    </slot>
                </template>
            </sw-entity-multi-select>
            {% endblock %}
```

## sw-icon-deprecated

> **Deprecated in 6.7** — Use `mt-icon` instead. Will be removed in 6.8.
> See [mt-icon](COMPONENTS-SHOPWARE-6.7-MIGRATION-MT-ICON.md) for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-icon>` | `<mt-icon>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | — | yes |  |
| color | `any` | `null` | no |  |
| small | `any` | `false` | no |  |
| large | `any` | `false` | no |  |
| size | `any` | `null` | no |  |
| decorative | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `loadIconSvgData` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `iconName` | |
| `classes` | |
| `styles` | |

### Examples

#### Basic Usage
```twig
<sw-icon-deprecated
    name="..."
>
    <!-- content -->
</sw-icon-deprecated>
```

## sw-icon

> **Migration wrapper** — Delegates to `mt-icon` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-icon](COMPONENTS-SHOPWARE-6.7-MIGRATION-MT-ICON.md) for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | — | yes |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Basic Usage
```twig
<sw-icon
    name="..."
>
    <!-- content -->
</sw-icon>
```

## sw-iframe-renderer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| src | `any` | — | yes |  |
| locationId | `any` | — | yes |  |
| fullScreen | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `signIframeSrc` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `locationIdHashQueryKey` | |
| `locationIdPathnameQueryKey` | |
| `locationIdSearchParamsQueryKey` | |
| `componentName` | |
| `extension` | |
| `extensionIsApp` | |
| `iFrameSrc` | |
| `iFrameHeight` | |
| `classes` | |

### Examples

#### Example 1
Source: `sw-extension-sdk/page/sw-extension-sdk-module/sw-extension-sdk-module.html.twig`
```twig
    <sw-iframe-renderer
        v-if="!isLoading"
        ref="iframeRenderer"
        :src="module.baseUrl"
        :location-id="module.locationId"
        full-screen
    />
    {% endblock %}

    {% block sw_extension_sdk_module_content_loader %}
    <sw-loader v-else-if="!timedOut" />
    {% endblock %}

    {% block sw_extension_sdk_module_content_error_state %}
    <sw-my-apps-error-page v-if="timedOut" />
```

#### Example 2
Source: `sw-cms/elements/location-renderer/config/sw-cms-el-config-location-renderer.html.twig`
```twig
    <sw-iframe-renderer
        :src="src"
        :location-id="configLocation"
    />
</div>
{% endblock %}

```

#### Example 3
Source: `sw-cms/elements/location-renderer/component/sw-cms-el-location-renderer.html.twig`
```twig
    <sw-iframe-renderer
        :src="src"
        :location-id="elementLocation"
    />
</div>
{% endblock %}

```

#### Example 4
Source: `sw-cms/elements/location-renderer/preview/sw-cms-el-preview-location-renderer.html.twig`
```twig
    <sw-iframe-renderer
        :src="src"
        :location-id="previewLocation"
    />
</div>
{% endblock %}

```

## sw-ignore-class

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-ignore-class>
    <!-- content -->
</sw-ignore-class>
```

## sw-image-preview-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaItems | `any` | — | yes |  |
| activeItemId | `any` | `''` | no |  |
| zoomSteps | `any` | `5` | no |  |
| itemPerPage | `any` | `10` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `afterComponentsMounted` | |
| `updatedComponent` | |
| `beforeDestroyComponent` | |
| `destroyedComponent` | |
| `buttonClass` | |
| `getActiveImage` | |
| `loadImage` | |
| `onClickClose` | |
| `onClickZoomIn` | |
| `onClickZoomOut` | |
| `onClickReset` | |
| `onImageSliderChange` | |
| `onThumbnailSliderChange` | |
| `setTransition` | |
| `updateTransform` | |
| `setActionButtonState` | |
| `onMouseWheel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `images` | |
| `maxZoomValue` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-variants-media-upload/sw-product-variants-media-upload.html.twig`
```twig
    <sw-image-preview-modal
        v-if="showPreviewModal"
        :active-item-id="activeItemId"
        :media-items="mediaSource"
        @modal-close="onClosePreviewModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-image-slider

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| images | `any` | — | yes |  |
| canvasWidth | `any` | `0` | no |  |
| canvasHeight | `any` | `0` | no |  |
| gap | `any` | `20` | no |  |
| elementPadding | `any` | `0` | no |  |
| navigationType | `any` | `'arrow'` | no |  |
| enableDescriptions | `any` | `false` | no |  |
| overflow | `any` | `'hidden'` | no |  |
| rewind | `any` | `false` | no |  |
| bordered | `any` | `true` | no |  |
| rounded | `any` | `true` | no |  |
| autoWidth | `any` | `false` | no |  |
| itemPerPage | `any` | `1` | no |  |
| initialIndex | `any` | `0` | no |  |
| arrowStyle | `any` | `'inside'` | no |  |
| buttonStyle | `any` | `'outside'` | no |  |
| displayMode | `any` | `'cover'` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| image-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `setCurrentPageNumber` | |
| `isImageObject` | |
| `hasValidDescription` | |
| `getImage` | |
| `imageAlt` | |
| `goToPreviousImage` | |
| `goToNextImage` | |
| `elementClasses` | |
| `elementStyles` | |
| `imageClasses` | |
| `borderStyles` | |
| `onSetCurrentItem` | |
| `isHiddenItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `totalPage` | |
| `remainder` | |
| `buttonList` | |
| `wrapperStyles` | |
| `componentStyles` | |
| `containerStyles` | |
| `scrollableContainerStyles` | |
| `imageStyles` | |
| `buttonClasses` | |
| `showButtons` | |
| `showArrows` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal-detail/sw-sales-channel-modal-detail.html.twig`
```twig
        <sw-image-slider
            class="sw-sales-channel-modal-detail__screenshot"
            :images="detailType.screenshotUrls || []"
            :canvas-width="580"
            :canvas-height="272"
            overflow="visible"
            navigation-type="arrow"
            enable-descriptions
        />
    </div>
    {% endblock %}
</div>
{% endblock %}

```

## sw-import-export-activity-log-info-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| logEntity | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| log-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `calculateFileSize` | |
| `openDownload` | |
| `getStateLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `typeText` | |
| `stateClass` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-activity-log-info-modal
        v-if="showDetailModal"
        :log-entity="selectedLog"
        @log-close="closeSelectedLog"
    />
    {% endblock %}

    {% block sw_import_export_activity_result_modal %}
    <sw-import-export-activity-result-modal
        v-if="showResultModal"
        :log-entity="selectedLog"
        :result="selectedResult"
        @result-close="closeSelectedResult"
    />
    {% endblock %}
```

## sw-import-export-activity-result-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| logEntity | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| result-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `calculateFileSize` | |
| `openDownload` | |
| `getStateLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mainEntity` | |
| `mainEntityResult` | |
| `result` | |
| `logTypeText` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-activity-result-modal
        v-if="showResultModal"
        :log-entity="selectedLog"
        :result="selectedResult"
        @result-close="closeSelectedResult"
    />
    {% endblock %}

    {% block sw_import_export_activity_modal %}
    <sw-import-export-edit-profile-modal
        v-if="selectedProfile"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @profile-close="closeSelectedProfile"
    />
```

## sw-import-export-activity

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | `'import'` | no | Valid: `import`, `export` |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `addActivity` | |
| `fetchActivities` | |
| `updateActivitiesInProgress` | |
| `updateActivitiesFromLogs` | |
| `onOpenProfile` | |
| `onAbortProcess` | |
| `closeSelectedProfile` | |
| `onShowLog` | |
| `onShowResult` | |
| `closeSelectedLog` | |
| `closeSelectedResult` | |
| `openProcessFileDownload` | |
| `saveSelectedProfile` | |
| `calculateFileSize` | |
| `getStateLabel` | |
| `getStateClass` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `logRepository` | |
| `profileRepository` | |
| `activityCriteria` | |
| `exportActivityColumns` | |
| `hasActivitiesInProgress` | |
| `downloadFileText` | |
| `showGrid` | |
| `showEmptyState` | |
| `showSpinner` | |
| `emptyStateSubLine` | |
| `emptyStateTitle` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-activity-log-info-modal
        v-if="showDetailModal"
        :log-entity="selectedLog"
        @log-close="closeSelectedLog"
    />
    {% endblock %}

    {% block sw_import_export_activity_result_modal %}
    <sw-import-export-activity-result-modal
        v-if="showResultModal"
        :log-entity="selectedLog"
        :result="selectedResult"
        @result-close="closeSelectedResult"
    />
    {% endblock %}
```

#### Example 2
Source: `sw-import-export/view/sw-import-export-view-import/sw-import-export-view-import.html.twig`
```twig
            <sw-import-export-activity
                ref="activityGrid"
                type="import"
            />
        </template>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```

#### Example 3
Source: `sw-import-export/view/sw-import-export-view-export/sw-import-export-view-export.html.twig`
```twig
            <sw-import-export-activity
                ref="activityGrid"
                type="export"
            />
        </template>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```

## sw-import-export-edit-profile-field-indicators

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `profileDelimiterError` | |
| `profileEnclosureError` | |
| `supportedDelimiter` | |
| `supportedEnclosures` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-field-indicators :profile="profile" />
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
<sw-import-export-edit-profile-field-indicators :profile="profile" />
```

## sw-import-export-edit-profile-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `shouldDisableProfileType` | |
| `shouldDisableObjectType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `profileNameError` | |
| `profileSourceEntityError` | |
| `profileTypeError` | |
| `supportedProfileTypes` | |
| `supportedEntities` | |
| `mappingLength` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-general :profile="profile" />
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
<sw-import-export-edit-profile-general :profile="profile" />
```

## sw-import-export-edit-profile-import-settings

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `handleCreateEntities` | |
| `handleUpdateEntities` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
    <sw-import-export-edit-profile-import-settings
        v-if="profile.type !== 'export'"
        :profile="profile"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
<sw-import-export-edit-profile-import-settings :profile="profile" />
```

## sw-import-export-edit-profile-modal-identifiers

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChangeIdentifier` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `languageRepository` | |
| `currencyRepository` | |
| `customFieldSetRepository` | |
| `languageCriteria` | |
| `currencyCriteria` | |
| `customFieldSetCriteria` | |
| `identifierColumns` | |
| `identifiers` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
            <sw-import-export-edit-profile-modal-identifiers
                :profile="profile"
            />
            {% endblock %}
            {% endblock %}
        </template>

        <template v-if="active === 'fieldIndicators'">
            <p class="sw-import-export-edit-profile-modal__text">
                {{ $tc('sw-import-export.profile.csvDescriptionBlock') }}
            </p>
        </template>
    </template>
</sw-tabs>
{% endblock %}
```

## sw-import-export-edit-profile-modal-mapping

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | `null` | no |  |
| systemRequiredFields | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-mapping | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `toggleAddMappingActionState` | |
| `onDeleteMapping` | |
| `loadMappings` | |
| `onAddMapping` | |
| `onSearch` | |
| `debouncedSearch` | |
| `isDefaultValueCheckboxDisabled` | |
| `isDefaultValueTextFieldDisabled` | |
| `isRequiredBySystem` | |
| `updateSorting` | |
| `swapItems` | |
| `isFirstMapping` | |
| `isLastMapping` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `languageRepository` | |
| `currencyRepository` | |
| `customFieldSetRepository` | |
| `languageCriteria` | |
| `currencyCriteria` | |
| `customFieldSetCriteria` | |
| `mappingColumns` | |
| `mappingsExist` | |
| `sortedMappings` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-mapping-page/sw-import-export-new-profile-wizard-mapping-page.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        class="sw-import-export-new-profile-wizard-mapping-page__mapping"
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
    {% endblock %}
</template>

<template v-if="active === 'advanced' && profile.type !== 'export' && profile.config.updateEntities !== false">
    {% block sw_import_export_edit_profile_modal_tabs_advanced %}
    {% block sw_import_export_edit_profile_modal_tabs_advanced_text %}
    <p class="sw-import-export-edit-profile-modal__text">
        {{ $tc('sw-import-export.profile.advancedDescription') }}
    </p>
```

## sw-import-export-edit-profile-modal

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | no |  |
| show | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| profile-close | — | |
| profile-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `saveProfile` | |
| `updateMapping` | |
| `getParentProfileSelected` | |
| `checkValidation` | |
| `resetViolations` | |
| `loadSystemRequiredFieldsForEntity` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `profileNameError` | |
| `profileSourceEntityError` | |
| `profileDelimiterError` | |
| `profileEnclosureError` | |
| `profileTypeError` | |
| `isNew` | |
| `modalTitle` | |
| `saveLabelSnippet` | |
| `showValidationError` | |
| `profileRepository` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-edit-profile-modal
        v-if="selectedProfile"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @profile-close="closeSelectedProfile"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 2
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-mapping-page/sw-import-export-new-profile-wizard-mapping-page.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        class="sw-import-export-new-profile-wizard-mapping-page__mapping"
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 3
Source: `sw-import-export/component/sw-import-export-edit-profile-modal/sw-import-export-edit-profile-modal.html.twig`
```twig
    <sw-import-export-edit-profile-modal-mapping
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @update-mapping="updateMapping"
    />
    {% endblock %}
    {% endblock %}
</template>

<template v-if="active === 'advanced' && profile.type !== 'export' && profile.config.updateEntities !== false">
    {% block sw_import_export_edit_profile_modal_tabs_advanced %}
    {% block sw_import_export_edit_profile_modal_tabs_advanced_text %}
    <p class="sw-import-export-edit-profile-modal__text">
        {{ $tc('sw-import-export.profile.advancedDescription') }}
    </p>
```

#### Example 4
Source: `sw-import-export/view/sw-import-export-view-profiles/sw-import-export-view-profiles.html.twig`
```twig
    <sw-import-export-edit-profile-modal
        :show="showProfileEditModal"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @profile-close="closeSelectedProfile"
    />
    {% endblock %}

    {% block sw_import_export_view_new_profile_wizard %}
    <sw-import-export-new-profile-wizard
        v-if="showNewProfileWizard"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @close="onCloseNewProfileWizard"
    />
```

## sw-import-export-entity-path-select

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| entityType | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| searchFunction | `any` | — | no |  |
| currencies | `any` | — | no |  |
| languages | `any` | — | no |  |
| customFieldSets | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| paginate | — | |
| update:value | — | |
| before-selection-clear | — | |
| search | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getDefinition` | |
| `propertyFilter` | |
| `isSelected` | |
| `onSelectExpanded` | |
| `tryGetSearchText` | |
| `onSelectCollapsed` | |
| `closeResultList` | |
| `setValue` | |
| `resetActiveItem` | |
| `onInputSearch` | |
| `debouncedSearch` | |
| `search` | |
| `getKey` | |
| `processTranslations` | |
| `getTranslationProperties` | |
| `processPrice` | |
| `getPriceProperties` | |
| `generatePriceProperties` | |
| `processLineItems` | |
| `generateLineItemProperties` | |
| `processTransactions` | |
| `generateTransactionsProperties` | |
| `processDeliveries` | |
| `generateDeliveryProperties` | |
| `processProperties` | |
| `processVisibilities` | |
| `getVisibilityProperties` | |
| `processMedia` | |
| `getMediaProperties` | |
| `processAssignedProducts` | |
| `getAssignedProductsProperties` | |
| `processCategories` | |
| `getCategoryProperties` | |
| `sortOptions` | |
| `getCustomFields` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `inputClasses` | |
| `selectionTextClasses` | |
| `resultListClasses` | |
| `singleSelection` | |
| `visibleResults` | |
| `actualPathPrefix` | |
| `actualPathParts` | |
| `currentEntity` | |
| `processFunctions` | |
| `options` | |
| `results` | |
| `availableIsoCodes` | |
| `lowerCaseIsoCodes` | |
| `availableLocales` | |
| `lowerCaseLocales` | |
| `searchTerm` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-identifiers/sw-import-export-edit-profile-modal-identifiers.html.twig`
```twig
<sw-import-export-entity-path-select
    v-else
    :value="item.selected"
    :languages="languages"
    :currencies="currencies"
    :entity-type="item.entityName"
    :disabled="profile.systemDefault"
    :custom-field-sets="customFieldSets"
    @update:value="onChangeIdentifier($event, item.entityName)"
>
    <template #before-item-list>
        <span></span>
    </template>
</sw-import-export-entity-path-select>
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-mapping/sw-import-export-edit-profile-modal-mapping.html.twig`
```twig
    <sw-import-export-entity-path-select
        v-model:value="item.key"
        :languages="languages"
        :currencies="currencies"
        :entity-type="profile.sourceEntity"
        :disabled="profile.systemDefault"
        :custom-field-sets="customFieldSets"
    />
</template>
{% endblock %}

{% block sw_import_export_edit_profile_modal_mapping_grid_required_column %}
<template #column-required="{ item }">
    <mt-switch
        v-show="isRequiredBySystem(item)"
```

## sw-import-export-exporter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sourceEntity | `any` | `''` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| export-started | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onProfileSelect` | |
| `onStartProcess` | |
| `handleProgress` | |
| `setExportModalProfile` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `profileCriteria` | |
| `disableExporting` | |
| `showProductVariantsInfo` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-exporter/sw-import-export-exporter.html.twig`
```twig
        <sw-import-export-exporter
            :source-entity="exportModalProfile"
            @export-started="$emit('export-started', $event)"
        />
        {% endblock %}

        <template #modal-footer>
            {% block sw_import_export_exporter_modal_footer %}
            <mt-button
                size="small"
                variant="secondary"
                @click="setExportModalProfile(null)"
            >
                {{ $tc('sw-import-export.exporter.close') }}
            </mt-button>
```

#### Example 2
Source: `sw-import-export/view/sw-import-export-view-export/sw-import-export-view-export.html.twig`
```twig
        <sw-import-export-exporter
            @export-started="reloadContent"
        />
    </mt-card>
    {% endblock %}

    {% block sw_import_export_view_export_activity %}
    <mt-card
        class="sw-import-export-view-export__activity"
        position-identifier="sw-import-export-view-export-activity"
        :title="$tc('sw-import-export.exporter.exportActivityLabel')"
        :subtitle="$tc('sw-import-export.exporter.exportActivityDescription')"
    >
        {# @deprecated tag:v6.8.0 - Block will be removed. #}
        {% block sw_import_export_view_export_activity_title %}
```

## sw-import-export-importer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sourceEntity | `any` | `''` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| import-started | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onProfileSelect` | |
| `onStartProcess` | |
| `onStartDryRunProcess` | |
| `handleProgress` | |
| `setImportModalProfile` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `profileCriteria` | |
| `logRepository` | |
| `disableImporting` | |
| `showProductVariantsInfo` | |
| `logCriteria` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-importer/sw-import-export-importer.html.twig`
```twig
        <sw-import-export-importer
            :source-entity="importModalProfile"
            @import-started="$emit('import-started', $event)"
        />
        {% endblock %}

        <template #modal-footer>
            {% block sw_import_export_importer_modal_footer %}
            <mt-button
                size="small"
                variant="secondary"
                @click="setImportModalProfile(null)"
            >
                {{ $tc('sw-import-export.importer.close') }}
            </mt-button>
```

#### Example 2
Source: `sw-import-export/view/sw-import-export-view-import/sw-import-export-view-import.html.twig`
```twig
        <sw-import-export-importer
            @import-started="reloadContent"
        />
    </mt-card>
    {% endblock %}

    {% block sw_import_export_view_import_activity %}
    <mt-card
        class="sw-import-export-view-import__activity"
        position-identifier="sw-import-export-view-import-log-activity"
        :title="$tc('sw-import-export.importer.importActivityLabel')"
        :subtitle="$tc('sw-import-export.exporter.exportActivityDescription')"
    >
        {# @deprecated tag:v6.8.0 - Block will be removed. #}
        {% block sw_import_export_view_import_activity_title %}
```

## sw-import-export-new-profile-wizard-csv-page

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| next-disable | — | |
| next-allow | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onFileChange` | |
| `transformMapping` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
    <sw-import-export-new-profile-wizard-csv-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_page_mapping %}
<sw-wizard-page
    :position="2"
    :title="pageTitleSnippet('sw-import-export.profile.mappingsTab')"
>
    <sw-import-export-new-profile-wizard-mapping-page
        :profile="profile"
```

## sw-import-export-new-profile-wizard-general-page

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| next-allow | — | |
| next-disable | — | |

### Methods

| Method | Description |
|--------|-------------|
| `isFieldFilled` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `inputValid` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
    <sw-import-export-new-profile-wizard-general-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_page_csv %}
<sw-wizard-page
    :position="csvUploadPagePosition"
    :title="pageTitleSnippet('sw-import-export.profile.csvUploadTab')"
>
    <sw-import-export-new-profile-wizard-csv-page
        :profile="profile"
```

## sw-import-export-new-profile-wizard-mapping-page

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |
| systemRequiredFields | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| next-allow | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mergeMappings` | |
| `updateMapping` | |
| `countAutomatedValues` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
    <sw-import-export-new-profile-wizard-mapping-page
        :profile="profile"
        :system-required-fields="systemRequiredFields"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_footer_right_button %}
<template #footer-right-button>
    <div class="sw-import-export-new-profile-wizard__footer-right-button-group">
        {% block sw_import_export_new_profile_wizard_footer_right_button_finish %}
        <mt-button
            v-if="showNextButton"
```

## sw-import-export-new-profile-wizard

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| profile | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| profile-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `onFinish` | |
| `pageTitleSnippet` | |
| `onNextAllow` | |
| `onNextDisable` | |
| `loadSystemRequiredFieldsForEntity` | |
| `saveProfile` | |
| `getParentProfileSelected` | |
| `checkValidation` | |
| `resetViolations` | |
| `onCurrentPageChange` | |
| `onNextPage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `profileRepository` | |
| `showValidationError` | |
| `showNextButton` | |
| `showCsvSkipButton` | |
| `parentProfileCriteria` | |

### Examples

#### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
    <sw-import-export-new-profile-wizard-general-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
{% endblock %}

{% block sw_import_export_new_profile_wizard_page_csv %}
<sw-wizard-page
    :position="csvUploadPagePosition"
    :title="pageTitleSnippet('sw-import-export.profile.csvUploadTab')"
>
    <sw-import-export-new-profile-wizard-csv-page
        :profile="profile"
```

#### Example 2
Source: `sw-import-export/view/sw-import-export-view-profiles/sw-import-export-view-profiles.html.twig`
```twig
    <sw-import-export-new-profile-wizard
        v-if="showNewProfileWizard"
        :profile="selectedProfile"
        @profile-save="saveSelectedProfile"
        @close="onCloseNewProfileWizard"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-import-export-progress

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| activityType | `any` | `'import'` | no | Valid: `import`, `export` |
| disableButton | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-start | — | |
| process-start-dryrun | — | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-exporter/sw-import-export-exporter.html.twig`
```twig
    <sw-import-export-progress
        activity-type="export"
        :disable-button="disableExporting"
        @process-start="onStartProcess"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 2
Source: `sw-import-export/component/sw-import-export-importer/sw-import-export-importer.html.twig`
```twig
    <sw-import-export-progress
        activity-type="import"
        :disable-button="disableImporting"
        @process-start="onStartProcess"
        @process-start-dryrun="onStartDryRunProcess"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-import-export-view-export

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `reloadContent` | |

### Examples

#### Basic Usage
```twig
<sw-import-export-view-export>
    <!-- content -->
</sw-import-export-view-export>
```

## sw-import-export-view-import

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `reloadContent` | |

### Examples

#### Basic Usage
```twig
<sw-import-export-view-import>
    <!-- content -->
</sw-import-export-view-import>
```

## sw-import-export-view-profiles

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadProfiles` | |
| `reloadContent` | |
| `onSearch` | |
| `onAddNewProfile` | |
| `onEditProfile` | |
| `onDuplicateProfile` | |
| `onDownloadTemplate` | |
| `onDeleteProfile` | |
| `closeSelectedProfile` | |
| `saveSelectedProfile` | |
| `onError` | |
| `getTypeLabel` | |
| `onCloseNewProfileWizard` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `profileRepository` | |
| `profileCriteria` | |
| `profilesColumns` | |
| `isNotSystemLanguage` | |
| `createTooltip` | |

### Examples

#### Basic Usage
```twig
<sw-import-export-view-profiles>
    <!-- content -->
</sw-import-export-view-profiles>
```

## sw-import-export

> Shopware Administration component.

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-identifiers/sw-import-export-edit-profile-modal-identifiers.html.twig`
```twig
            <sw-import-export-entity-path-select
                v-else
                :value="item.selected"
                :languages="languages"
                :currencies="currencies"
                :entity-type="item.entityName"
                :disabled="profile.systemDefault"
                :custom-field-sets="customFieldSets"
                @update:value="onChangeIdentifier($event, item.entityName)"
            >
                <template #before-item-list>
                    <span></span>
                </template>
            </sw-import-export-entity-path-select>
        </template>
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-exporter/sw-import-export-exporter.html.twig`
```twig
        <sw-import-export-exporter
            :source-entity="exportModalProfile"
            @export-started="$emit('export-started', $event)"
        />
        {% endblock %}

        <template #modal-footer>
            {% block sw_import_export_exporter_modal_footer %}
            <mt-button
                size="small"
                variant="secondary"
                @click="setExportModalProfile(null)"
            >
                {{ $tc('sw-import-export.exporter.close') }}
            </mt-button>
```

#### Example 3
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-import-export-activity-log-info-modal
        v-if="showDetailModal"
        :log-entity="selectedLog"
        @log-close="closeSelectedLog"
    />
    {% endblock %}

    {% block sw_import_export_activity_result_modal %}
    <sw-import-export-activity-result-modal
        v-if="showResultModal"
        :log-entity="selectedLog"
        :result="selectedResult"
        @result-close="closeSelectedResult"
    />
    {% endblock %}
```

#### Example 4
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-general :profile="profile" />
```

#### Example 5
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard-general-page/sw-import-export-new-profile-wizard-general-page.html.twig`
```twig
<sw-import-export-edit-profile-field-indicators :profile="profile" />
```

## sw-in-app-purchase-checkout

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `entry` | |

### Examples

#### Basic Usage
```twig
<sw-in-app-purchase-checkout>
    <!-- content -->
</sw-in-app-purchase-checkout>
```

## sw-inactivity-login

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| hash | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `loginUserWithPassword` | |
| `handleLoginSuccess` | |
| `forwardLogin` | |
| `onBackToLogin` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `title` | |

### Examples

#### Basic Usage
```twig
<sw-inactivity-login
    hash="..."
>
    <!-- content -->
</sw-inactivity-login>
```

## sw-inherit-wrapper

> Wrapper component that handles value inheritance from parent entities.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| inheritedValue | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| label | `any` | `null` | no |  |
| required | `any` | `false` | no |  |
| isAssociation | `any` | `false` | no |  |
| hasParent | `any` | — | no |  |
| customInheritationCheckFunction | `any` | `null` | no |  |
| customRestoreInheritanceFunction | `any` | `null` | no |  |
| customRemoveInheritanceFunction | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| error | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `updateCurrentValue` | |
| `updateValue` | |
| `toggleInheritance` | |
| `restoreInheritance` | |
| `removeInheritance` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `isInheritField` | |
| `isInherited` | |
| `labelClasses` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-visibility/sw-bulk-edit-product-visibility.html.twig`
```twig
<sw-inherit-wrapper
    ref="productVisibilitiesInheritance"
    v-model:value="product.visibilities"
    :inherited-value="product.visibilities"
    class="sw-product-category-form__visibility_field"
    :custom-remove-inheritance-function="visibilitiesRemoveInheritanceFunction"
    is-association
>
    <template #content="{ currentValue, isInherited, updateCurrentValue }">
        <sw-product-visibility-select
            ref="productVisibility"
            :key="isInherited"
            class="sw-product-detail__select-visibility"
            :entity-collection="currentValue"
            :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
```

#### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-custom-fields/sw-bulk-edit-custom-fields.html.twig`
```twig
<sw-inherit-wrapper
    v-if="entity && customField.config"
    v-model:value="entity.customFields[customField.name]"
    v-bind="getInheritWrapperBind(customField)"
    :class="'sw-form-field-renderer-field__' + customField.name"
    :has-parent="hasParent"
    :required="customField.config.validation === 'required'"
    :inherited-value="getInheritedCustomField(customField.name)"
    @update:value="updateCustomField(customField)"
>
    <template #content="props">
        <sw-form-field-renderer
            v-bind="getBind(customField, props)"
            :key="props.isInherited"
            :class="'sw-form-field-renderer-input-field__' + customField.name"
```

#### Example 3
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-inherit-wrapper
    v-if="config && index === 0"
    v-model:value="config['core.listing.defaultSorting']"
    :label="$tc('sw-settings-listing.general.labelDefaultSorting')"
    :has-parent="isNotDefaultSalesChannel"
    :inherited-value="inheritance['core.listing.defaultSorting']"
    required
>
    <template #content="{ isInherited, currentValue, updateCurrentValue }">
        <sw-single-select
            class="sw-settings-listing-index__default-sorting-select"
            :placeholder="$tc('sw-settings-listing.general.placeholderDefaultSorting')"
            :disabled="isInherited"
            :value="currentValue"
            :options="productSortingOptions"
```

#### Example 4
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-inherit-wrapper
    v-if="config && index === 0"
    v-model:value="config['core.listing.defaultSearchResultSorting']"
    :label="$tc('sw-settings-listing.general.labelDefaultSearchResultSorting')"
    :has-parent="isNotDefaultSalesChannel"
    :inherited-value="inheritance['core.listing.defaultSearchResultSorting']"
    required
>
    <template #content="{ isInherited, currentValue, updateCurrentValue }">
        <sw-single-select
            class="sw-settings-listing-index__default-search-result-sorting-select"
            :placeholder="$tc('sw-settings-listing.general.placeholderDefaultSearchResultSorting')"
            :disabled="isInherited"
            :value="currentValue"
            :options="searchResultSortingOptions"
```

#### Example 5
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
<sw-inherit-wrapper
    v-model:value="selectedShopPages[shopPageSalesChannelId]"
    :inherited-value="selectedShopPages.null"
    :has-parent="shopPageSalesChannelId !== null"
    :label="$tc('sw-cms.components.cmsLayoutAssignmentModal.labelShopPages')"
>
    <template #content="props">
        <sw-multi-select
            class="sw-cms-layout-assignment-modal__shop-page-select"
            :options="shopPages"
            :disabled="props.isInherited"
            :value="props.currentValue"
            :map-inheritance="props"
            @update:value="props.updateCurrentValue"
        />
```

## sw-inheritance-switch

> Toggle switch for enabling/disabling value inheritance.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isInherited | `any` | `false` | yes |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClickRestoreInheritance` | |
| `onClickRemoveInheritance` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `unInheritClasses` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-inheritance-switch
    v-if="isChild"
    :is-inherited="bulkEditProduct[formField.name].isInherited"
    @inheritance-restore="onInheritanceRestore(formField)"
    @inheritance-remove="onInheritanceRemove(formField)"
/>

<a
    v-if="['add', 'overwrite'].includes(bulkEditProduct[formField.name].type)"
    :class="{ 'is--disabled': !!bulkEditProduct[formField.name].isInherited }"
    class="quick-link"
    role="link"
    tabindex="0"
    @click="displayAdvancePricesModal = true"
    @keydown.enter="displayAdvancePricesModal = true"
```

#### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
                    <sw-inheritance-switch
                        :is-inherited="bulkEditData[formField.name].isInherited"
                        @inheritance-restore="onInheritanceRestore(formField)"
                        @inheritance-remove="onInheritanceRemove(formField)"
                    />
                    <sw-bulk-edit-form-field-renderer
                        v-bind="formField"
                        :key="`formField-${index}`"
                        v-model:value="entity[formField.name]"
                        @update:value="onChangeValue($event, formField.name)"
                    />
                </div>
            </template>
            <template v-else>
                <sw-bulk-edit-form-field-renderer
```

#### Example 3
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
                            <sw-inheritance-switch
                                :is-inherited="bulkEditData[formField.name].isInherited"
                                @inheritance-restore="onInheritanceRestore(formField)"
                                @inheritance-remove="onInheritanceRemove(formField)"
                            />
                            <sw-bulk-edit-form-field-renderer
                                v-bind="formField"
                                :key="`formField-${index}`"
                                v-model:value="entity[formField.name]"
                                @update:value="onChangeValue($event, formField.name)"
                            />
                        </div>
                    </template>
                    <template v-else>
                        <sw-bulk-edit-form-field-renderer
```

#### Example 4
Source: `sw-cms/component/sw-cms-inherit-wrapper/sw-cms-inherit-wrapper.html.twig`
```twig
        <sw-inheritance-switch
            v-if="supportsInheritance"
            :is-inherited="isInherited"
            @inheritance-restore="showModal = true;"
            @inheritance-remove="onInheritanceRemove"
        />

        <!-- eslint-disable-next-line vuejs-accessibility/label-has-for -->
        <label v-if="label">{{ label }}</label>
    </div>

    <slot v-bind="{ isInherited }"></slot>

    <sw-confirm-modal
        v-if="showModal"
```

#### Example 5
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrix/sw-settings-shipping-price-matrix.html.twig`
```twig
            <sw-inheritance-switch
                v-if="!currency.isSystemDefault"
                class="sw-settings-shipping-price-matrix__price-inherit-icon"
                :is-inherited="props.isInherited"
                :disabled="disabled"
                @inheritance-restore="props.restoreInheritance"
                @inheritance-remove="props.removeInheritance"
            />

            <mt-number-field
                v-model="props.currentValue.gross"
                :name="`sw-field--${item.id}-${currency.id}-gross`"
                :size="compact ? 'small' : 'default'"
                class="sw-settings-shipping-price-matrix__price-input"
                :digits="50"
```

## sw-inheritance-warning

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | — | yes |  |

### Examples

#### Example 1
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
<sw-inheritance-warning
    v-if="isChild"
    :name="$tc('sw-product.general.inheritanceModuleName')"
/>
{% endblock %}

{% block sw_product_detail_content_tabs %}
<sw-tabs
    v-if="productId"
    class="sw-product-detail-page__tabs"
    position-identifier="sw-product-detail"
>
    {% block sw_product_detail_content_tabs_general %}
    <sw-tabs-item
        class="sw-product-detail__tab-general"
```

## sw-integration-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `onSaveIntegration` | |
| `updateIntegration` | |
| `createIntegration` | |
| `createSavedSuccessNotification` | |
| `createSavedErrorNotification` | |
| `onGenerateKeys` | |
| `onShowDetailModal` | |
| `onCreateIntegration` | |
| `onCloseDetailModal` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `integrationRepository` | |
| `integrationCriteria` | |
| `secretAccessKeyFieldTypeIsText` | |
| `secretAccessKeyFieldTypeIsPassword` | |
| `integrationColumns` | |

### Examples

#### Basic Usage
```twig
<sw-integration-list>
    <!-- content -->
</sw-integration-list>
```

## sw-internal-link

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| routerLink | `any` | — | no |  |
| target | `any` | `null` | no |  |
| icon | `any` | `'regular-long-arrow-right'` | no |  |
| inline | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| hideIcon | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `elementType` | |
| `componentClasses` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-measurement-form/sw-product-measurement-form.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.sales.channel.list' }"
    hide-icon
    inline
>
    {{ $tc('sw-product.measurementForm.linkText') }}
</sw-internal-link>
```

#### Example 2
Source: `sw-settings-payment/component/sw-payment-card/sw-payment-card.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.settings.payment.detail', params: { id: paymentMethod.id }}"
    :disabled="!acl.can('payment.editor') || undefined"
    hide-icon
>
    {{ $tc('sw-settings-payment.overview.editDetails') }}
</sw-internal-link>
```

#### Example 3
Source: `sw-settings-usage-data/component/sw-usage-data-consent-banner/sw-usage-data-consent-banner.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.settings.usage.data.index' }"
>
    {{ $tc('sw-usage-data-consent-banner.togglePath') }}
</sw-internal-link>
```

#### Example 4
Source: `sw-settings-measurement/component/sw-settings-measurement-default-units/sw-settings-measurement-default-units.html.twig`
```twig
<sw-internal-link
    :router-link="{ name: 'sw.sales.channel.list' }"
    inline
    hide-icon
>
    {{ $tc('sw-settings-measurement.defaultUnits.linkText') }}
</sw-internal-link>
```

## sw-label

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `''` | no | Valid: `info`, `danger`, `success`, `warning`, `neutral`, `neutral-reversed`, `primary` |
| size | `any` | `'default'` | no | Valid: `small`, `medium`, `default` |
| appearance | `any` | `'default'` | no | Valid: `default`, `pill`, `circle`, `badged` |
| ghost | `any` | `false` | no |  |
| caps | `any` | `false` | no |  |
| dismissable | `any` | `true` | no |  |
| light | `any` | `false` | no |  |
| onDismiss | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| dismiss-icon | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selected | — | |
| dismiss | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `labelClasses` | |
| `showDismissable` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-label
    v-droppable="{ ...mergedDropConfig, data: { snippet, index, linePosition }}"
    v-draggable="{ ...mergedDragConfig, data: { snippet, index, linePosition }}"
    :dismissable="!isSelectionDisabled(snippet)"
    :size="size"
    @dismiss="onClickDismiss(index)"
>
    <span class="sw-select-selection-list__item">
        <slot
            name="label-property"
            v-bind="{ item: snippet, index, getLabelProperty }"
        >
            {{ getLabelProperty(snippet) }}
        </slot>
    </span>
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-label
    :dismissable="true"
    :size="size"
    @dismiss="onClickDismiss(index)"
>
    <span class="sw-select-selection-list__item">
        <slot
            name="label-property"
            v-bind="{ item: snippet, index }"
        >
            {{ getLabelProperty(snippet) }}
        </slot>
    </span>
</sw-label>
```

#### Example 3
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-error/sw-bulk-edit-save-modal-error.html.twig`
```twig
<sw-label
    class="sw-bulk-edit-save-modal__icon"
    appearance="pill"
    variant="danger"
>
    <mt-icon
        name="regular-times-hexagon"
        size="30px"
    />
</sw-label>
```

#### Example 4
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-success/sw-bulk-edit-save-modal-success.html.twig`
```twig
<sw-label
    class="sw-bulk-edit-save-modal__icon"
    appearance="pill"
    variant="success"
>
    <mt-icon
        name="regular-check-circle"
        size="30px"
    />
</sw-label>
```

#### Example 5
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-process/sw-bulk-edit-save-modal-process.html.twig`
```twig
<sw-label
    class="sw-bulk-edit-save-modal__icon"
    appearance="pill"
    variant="info"
>
    <sw-loader
        class="sw-bulk-edit-save-modal__loading-icon"
        size="30px"
    />
</sw-label>
```

## sw-landing-page-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldSetsArray` | |
| `landingPageNameError` | |
| `landingPageUrlError` | |
| `landingPageSalesChannelsError` | |
| `landingPage` | |
| `cmsPage` | |
| `isLayoutSet` | |

### Examples

#### Basic Usage
```twig
<sw-landing-page-detail-base
    isLoading="..."
>
    <!-- content -->
</sw-landing-page-detail-base>
```

## sw-landing-page-detail-cms

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `landingPage` | |
| `cmsPage` | |

### Examples

#### Basic Usage
```twig
<sw-landing-page-detail-cms
    isLoading="..."
>
    <!-- content -->
</sw-landing-page-detail-cms>
```

## sw-landing-page-tree

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| landingPageId | `any` | `null` | no |  |
| currentLanguageId | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |
| allowCreate | `any` | `true` | no |  |
| allowDelete | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| landing-page-checked-elements-count | — | |
| unsaved-changes | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadLandingPages` | |
| `checkedElementsCount` | |
| `deleteCheckedItems` | |
| `onDeleteLandingPage` | |
| `changeLandingPage` | |
| `duplicateElement` | |
| `createNewElement` | |
| `syncLandingPages` | |
| `createNewLandingPage` | |
| `addLandingPage` | |
| `addLandingPages` | |
| `removeFromStore` | |
| `getLandingPageUrl` | |
| `newLandingPageUrl` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `landingPagesToDelete` | |
| `cmsLandingPageCriteria` | |
| `landingPage` | |
| `landingPageRepository` | |
| `landingPages` | |
| `disableContextMenu` | |
| `contextMenuTooltipText` | |

### Examples

#### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
            <sw-landing-page-tree
                ref="landingPageTree"
                :landing-page-id="landingPageId"
                :current-language-id="currentLanguageId"
                :allow-edit="acl.can('landing_page.editor')"
                :allow-create="acl.can('landing_page.creator')"
                :allow-delete="acl.can('landing_page.deleter')"
                @unsaved-changes="openChangeModal"
                @landing-page-checked-elements-count="landingPageCheckedElementsCount"
            />
            {% endblock %}

        </template>
    </sw-sidebar-collapse>
    {% endblock %}
```

## sw-landing-page-view

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `landingPage` | |
| `cmsPage` | |

### Examples

#### Example 1
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

## sw-language-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entityDescription | `any` | `''` | no |  |
| isNewEntity | `any` | `false` | no |  |
| changeLanguageOnParentClick | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `refreshParentLanguage` | |
| `onClickParentLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `languageId` | |
| `systemLanguageId` | |
| `language` | |
| `languageRepository` | |
| `infoParent` | |
| `infoText` | |
| `isDefaultLanguage` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-language-info
    :entity-description="placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline'))"
/>
{% endblock %}

{% block sw_settings_country_tabs_header %}
<sw-tabs position-identifier="sw-settings-country-detail-header">
    {% block sw_setting_country_tabs_setting %}
    <sw-tabs-item
        v-bind="$props"
        class="sw-settings-country__setting-tab"
        :route="{ name: isNewCountry ? 'sw.settings.country.create.general' : 'sw.settings.country.detail.general' }"
    >
        {{ $tc('sw-settings-country.page.generalTab') }}
    </sw-tabs-item>
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-create/sw-settings-country-create.html.twig`
```twig
<sw-language-info
    :entity-description="placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline'))"
    is-new-entity
/>
{% endblock %}

```

#### Example 3
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-language-info :entity-description="entityDescription" />
```

#### Example 4
Source: `sw-settings-product-feature-sets/page/sw-settings-product-feature-sets-detail/sw-settings-product-feature-sets-detail.html.twig`
```twig
<sw-language-info
    :entity-description="placeholder(productFeatureSet, 'name', $tc('sw-settings-product-feature-sets.detail.textHeadline'))"
/>
{% endblock %}

{% block sw_settings_product_feature_set_detail_content_card %}
<mt-card
    :title="$tc('sw-settings-product-feature-sets.detail.titleCard')"
    position-identifier="sw-settings-product-feature-sets-detail"
>

    {% block sw_settings_product_feature_set_detail_content_field_name %}

    <mt-text-field
        v-model="productFeatureSet.name"
```

#### Example 5
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
<sw-language-info :entity-description="identifier" />
```

## sw-language-switch

> Language selector for switching the admin editing language.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| changeGlobalLanguage | `any` | `true` | no |  |
| abortChangeFunction | `any` | — | no |  |
| saveChangesFunction | `any` | — | no |  |
| savePermission | `any` | `true` | no |  |
| allowEdit | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `onInput` | |
| `checkAbort` | |
| `emitChange` | |
| `onCloseChangesModal` | |
| `onClickSaveChanges` | |
| `onClickRevertUnsavedChanges` | |
| `changeToNewLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `languageCriteria` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-language-switch @on-change="onChangeLanguage" />
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
    <sw-language-switch
        :save-changes-function="saveOnLanguageChange"
        :abort-change-function="abortOnLanguageChange"
        @on-change="onChangeLanguage"
    />
</template>
{% endblock %}

{% block sw_settings_country_detail_content %}
<template #content>
    <sw-card-view>
        {% block sw_settings_country_detail_content_language_info %}
        <sw-language-info
            :entity-description="placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline'))"
        />
```

#### Example 3
Source: `sw-settings-country/page/sw-settings-country-create/sw-settings-country-create.html.twig`
```twig
<sw-language-switch disabled />
```

#### Example 4
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-language-switch @on-change="onChangeLanguage" />
```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
    <sw-language-switch
        :disabled="salutationId == null || undefined"
        @on-change="onChangeLanguage"
    />
</template>
{% endblock %}

{% block sw_settings_salutation_detail_actions %}
<template #smart-bar-actions>
    {% block sw_settings_salutation_detail_actions_cancel %}
    <mt-button
        v-tooltip.bottom="tooltipCancel"
        class="sw-settings-salutation-detail__cancel"
        variant="secondary"
        size="default"
```

## sw-license-violation

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getPluginViolation` | |
| `reloadViolations` | |
| `deactivateTemporary` | |
| `fetchPlugins` | |
| `deletePlugin` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `getPluginForViolation` | |
| `addLoading` | |
| `finishLoading` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `violations` | |
| `warnings` | |
| `visible` | |
| `pluginCriteria` | |
| `isLoading` | |

### Examples

#### Basic Usage
```twig
<sw-license-violation>
    <!-- content -->
</sw-license-violation>
```

## sw-list-price-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| price | `any` | — | yes |  |
| purchasePrices | `any` | — | no |  |
| defaultPrice | `any` | — | no |  |
| label | `any` | `true` | no |  |
| taxRate | `any` | — | yes |  |
| currency | `any` | — | yes |  |
| compact | `any` | `false` | no |  |
| error | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| enableInheritance | `any` | `false` | no |  |
| disableSuffix | `any` | `false` | no |  |
| vertical | `any` | `false` | no |  |
| hideListPrices | `any` | `false` | no |  |
| hidePurchasePrices | `any` | `false` | no |  |
| hideRegulationPrices | `any` | `false` | no |  |
| showSettingPrice | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `listPriceChanged` | |
| `regulationPriceChanged` | |
| `convertPrice` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `priceForCurrency` | |
| `listPrice` | |
| `regulationPrice` | |
| `defaultListPrice` | |
| `defaultRegulationPrice` | |
| `isInherited` | |
| `listPriceHelpText` | |
| `regulationPriceHelpText` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-price-form/sw-product-price-form.html.twig`
```twig
            <sw-list-price-field
                vertical
                :price="currentValue.price"
                :purchase-prices="currentValue.purchasePrices"
                :tax-rate="productTaxRate"
                :disabled="isInherited || !allowEdit || undefined"
                :error="productPriceError ? productPriceError[0] : null"
                :currency="defaultCurrency"
                :show-setting-price="showModeSetting"
            />
        </template>
    </sw-inherit-wrapper>
    {% endblock %}

</sw-container>
```

#### Example 2
Source: `sw-product/view/sw-product-detail-context-prices/sw-product-detail-context-prices.html.twig`
```twig
                <sw-list-price-field
                    :price="item.price"
                    :default-price="findDefaultPriceOfRule(item)"
                    :vertical="true"
                    :tax-rate="productTaxRate"
                    :label="false"
                    :compact="compact"
                    :disabled="!acl.can('product.editor')"
                    :currency="currency"
                    hide-purchase-prices
                />
            </div>
        </template>
    </template>
{% endblock %}
```

## sw-loader-deprecated

> **Deprecated in 6.7** — Use `mt-loader` instead. Will be removed in 6.8.
> See [mt-loader](COMPONENTS-SHOPWARE-6.7-MIGRATION-MT-LOADER.md) for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-loader>` | `<mt-loader>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | `any` | `'50px'` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `loaderSize` | |
| `numericSize` | |
| `borderWidth` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
<sw-loader v-if="isLoading" />
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
        <sw-loader
            v-if="isLoading"
            class="sw-settings-country-new-snippet-modal__loader"
            size="16px"
        />

        <mt-icon
            class="sw-settings-country-new-snippet-modal__search-icon"
            name="regular-search-s"
            size="16px"
        />
    </template>
</sw-contextual-field>

<sw-tree
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-loader v-if="searchInProgress" />
```

#### Example 4
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-process/sw-bulk-edit-save-modal-process.html.twig`
```twig
    <sw-loader
        class="sw-bulk-edit-save-modal__loading-icon"
        size="30px"
    />
</sw-label>
{% endblock %}

{% block sw_bulk_edit_save_modal_process_generate_document %}
<ul
    v-if="selectedDocumentTypes.length > 0"
    class="sw-bulk-edit-save-modal-process__generate-document-container"
>
    <li
        v-for="selectedDocumentType in selectedDocumentTypes"
        :key="selectedDocumentType.id"
```

#### Example 5
Source: `sw-extension/page/sw-extension-app-module-page/sw-extension-app-module-page.html.twig`
```twig
<sw-loader />
```

## sw-loader

> **Migration wrapper** — Delegates to `mt-loader` by default. The deprecated implementation is available via the `deprecated` prop.
> See [mt-loader](COMPONENTS-SHOPWARE-6.7-MIGRATION-MT-LOADER.md) for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `any` | `null` | no |  |
| value | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `useMeteorComponent` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
<sw-loader v-if="isLoading" />
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
        <sw-loader
            v-if="isLoading"
            class="sw-settings-country-new-snippet-modal__loader"
            size="16px"
        />

        <mt-icon
            class="sw-settings-country-new-snippet-modal__search-icon"
            name="regular-search-s"
            size="16px"
        />
    </template>
</sw-contextual-field>

<sw-tree
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-loader v-if="searchInProgress" />
```

#### Example 4
Source: `sw-bulk-edit/component/sw-bulk-edit-save-modal-process/sw-bulk-edit-save-modal-process.html.twig`
```twig
    <sw-loader
        class="sw-bulk-edit-save-modal__loading-icon"
        size="30px"
    />
</sw-label>
{% endblock %}

{% block sw_bulk_edit_save_modal_process_generate_document %}
<ul
    v-if="selectedDocumentTypes.length > 0"
    class="sw-bulk-edit-save-modal-process__generate-document-container"
>
    <li
        v-for="selectedDocumentType in selectedDocumentTypes"
        :key="selectedDocumentType.id"
```

#### Example 5
Source: `sw-extension/page/sw-extension-app-module-page/sw-extension-app-module-page.html.twig`
```twig
<sw-loader />
```

## sw-login-login

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| is-loading | — | |
| is-not-loading | — | |
| login-success | — | |
| login-error | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `doSsoForwarding` | |
| `loginUserWithPassword` | |
| `handleLoginSuccess` | |
| `forwardLogin` | |
| `handleLoginError` | |
| `createNotificationFromResponse` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showLoginAlert` | |

### Examples

#### Basic Usage
```twig
<sw-login-login>
    <!-- content -->
</sw-login-login>
```

## sw-login-recovery-info

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| is-not-loading | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `rateLimitTime` | |

### Examples

#### Basic Usage
```twig
<sw-login-recovery-info>
    <!-- content -->
</sw-login-recovery-info>
```

## sw-login-recovery-recovery

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| hash | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `validatePasswords` | |
| `updatePassword` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `userPasswordError` | |

### Examples

#### Basic Usage
```twig
<sw-login-recovery-recovery
    hash="..."
>
    <!-- content -->
</sw-login-recovery-recovery>
```

## sw-login-recovery

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| is-loading | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `isEmailValid` | |
| `sendRecoveryMail` | |
| `displayRecoveryInfo` | |

### Examples

#### Basic Usage
```twig
<sw-login-recovery>
    <!-- content -->
</sw-login-recovery>
```

## sw-login

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| hash | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `setLoading` | |
| `loginError` | |
| `loginSuccess` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `title` | |

### Examples

#### Basic Usage
```twig
<sw-login>
    <!-- content -->
</sw-login>
```

## sw-mail-header-footer-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |
| `onSave` | |

### Examples

#### Basic Usage
```twig
<sw-mail-header-footer-create>
    <!-- content -->
</sw-mail-header-footer-create>
```

## sw-mail-header-footer-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `createdComponent` | |
| `loadEntityData` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `saveFinish` | |
| `onCancel` | |
| `onSave` | |
| `confirmSave` | |
| `findAlreadyAssignedSalesChannels` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mailHeaderFooterNameError` | |
| `identifier` | |
| `mailHeaderFooterRepository` | |
| `mailHeaderFooterCriteria` | |
| `salesChannelRepository` | |
| `completerFunction` | |
| `allowSave` | |
| `tooltipSave` | |

### Examples

#### Basic Usage
```twig
<sw-mail-header-footer-detail>
    <!-- content -->
</sw-mail-header-footer-detail>
```

## sw-mail-header-footer-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onEdit` | |
| `getList` | |
| `getListColumns` | |
| `getSalesChannelsString` | |
| `onDuplicate` | |
| `checkCanBeDeleted` | |
| `onDelete` | |
| `getMailHeaderFooterCriteria` | |
| `onMultipleDelete` | |
| `showDeleteErrorNotification` | |
| `updateRecords` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mailHeaderFooterRepository` | |
| `skeletonItemAmount` | |
| `showListing` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-mail-template/page/sw-mail-template-index/sw-mail-template-index.html.twig`
```twig
                <sw-mail-header-footer-list
                    ref="mailHeaderFooterList"
                    :search-term="term"
                />
            </template>
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 2
Source: `sw-mail-template/view/sw-mail-template-view-header-footer/sw-mail-template-view-header-footer.html.twig`
```twig
<sw-mail-header-footer-list ref="mailHeaderFooterList" />
```

## sw-mail-template-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |
| `onSave` | |

### Examples

#### Basic Usage
```twig
<sw-mail-template-create>
    <!-- content -->
</sw-mail-template-create>
```

## sw-mail-template-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `getMailTemplateType` | |
| `createMediaCollection` | |
| `getMailTemplateMedia` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `saveFinish` | |
| `onCancel` | |
| `onSave` | |
| `onClickTestMailTemplate` | |
| `onClickShowPreview` | |
| `mailPreviewContent` | |
| `replaceContent` | |
| `onCancelShowPreview` | |
| `onCopyVariable` | |
| `onChangeType` | |
| `getMediaColumns` | |
| `successfulUpload` | |
| `onMediaDrop` | |
| `createMailTemplateMediaAssoc` | |
| `openMediaSidebar` | |
| `onDeleteMedia` | |
| `onSelectionChanged` | |
| `onDeleteSelectedMedia` | |
| `_checkIfMediaIsAlreadyUsed` | |
| `onAddItemToAttachment` | |
| `loadAvailableVariables` | |
| `isToManyAssociationVariable` | |
| `onGetTreeItems` | |
| `addVariables` | |
| `loadInitialAvailableVariables` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mailTemplateContentHtmlError` | |
| `mailTemplateContentPlainError` | |
| `mailTemplateMailTemplateTypeIdError` | |
| `mailTemplateSubjectError` | |
| `loadedAvailableVariables` | |
| `identifier` | |
| `mailTemplateRepository` | |
| `mediaRepository` | |
| `mailTemplateMediaRepository` | |
| `salesChannelRepository` | |
| `outerCompleterFunction` | |
| `mailTemplateTypeRepository` | |
| `testMailRequirementsMet` | |
| `mediaColumns` | |
| `allowSave` | |
| `tooltipSave` | |
| `showPreview` | |
| `hasTemplateData` | |
| `lacksEmailSendPermission` | |
| `isSendButtonDisabled` | |

### Examples

#### Basic Usage
```twig
<sw-mail-template-detail>
    <!-- content -->
</sw-mail-template-detail>
```

## sw-mail-template-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onChangeLanguage` | |
| `getList` | |
| `onCreateMailTemplate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `searchType` | |

### Examples

#### Basic Usage
```twig
<sw-mail-template-index>
    <!-- content -->
</sw-mail-template-index>
```

## sw-mail-template-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchTerm | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `getListColumns` | |
| `onChangeLanguage` | |
| `onDuplicate` | |
| `updateRecords` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mailTemplateRepository` | |
| `skeletonItemAmount` | |
| `showListing` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-mail-template/page/sw-mail-template-index/sw-mail-template-index.html.twig`
```twig
                <sw-mail-template-list
                    ref="mailTemplateList"
                    :search-term="term"
                />

                <sw-mail-header-footer-list
                    ref="mailHeaderFooterList"
                    :search-term="term"
                />
            </template>
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
```

#### Example 2
Source: `sw-mail-template/view/sw-mail-template-view-templates/sw-mail-template-view-templates.html.twig`
```twig
<sw-mail-template-list ref="mailTemplateList" />
```

## sw-mail-template-view-header-footer

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |

### Examples

#### Basic Usage
```twig
<sw-mail-template-view-header-footer>
    <!-- content -->
</sw-mail-template-view-header-footer>
```

## sw-mail-template-view-templates

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |

### Examples

#### Basic Usage
```twig
<sw-mail-template-view-templates>
    <!-- content -->
</sw-mail-template-view-templates>
```

## sw-maintain-currencies-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencies | `any` | — | no |  |
| prices | `any` | — | yes |  |
| defaultPrice | `any` | — | yes |  |
| taxRate | `any` | — | yes |  |
| hideListPrices | `any` | `false` | no |  |
| hideRegulationPrices | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-prices | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCurrencies` | |
| `updateCurrencyCollectionFromCurrencies` | |
| `sortCurrencies` | |
| `convertPrice` | |
| `isCurrencyInherited` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `onCancel` | |
| `onApply` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `maintainCurrencyColumns` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-price-form/sw-product-price-form.html.twig`
```twig
    <sw-maintain-currencies-modal
        v-if="displayMaintainCurrencies"
        variant="full"
        :currencies="currencies"
        :prices="product.price"
        :default-price="defaultPrice"
        :tax-rate="productTaxRate"
        :disabled="!allowEdit || undefined"
        @modal-close="onMaintainCurrenciesClose"
        @update-prices="updatePrices"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-manufacturer-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| manufacturerId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `setMediaItem` | |
| `setMediaFromSidebar` | |
| `onUnlinkLogo` | |
| `openMediaSidebar` | |
| `onDropMedia` | |
| `onMediaSelectionChange` | |
| `getMediaDefaultFolderId` | |
| `onSave` | |
| `onCancel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `manufacturerIsLoading` | |
| `manufacturerRepository` | |
| `mediaRepository` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `mediaUploadTag` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `manufacturerDescriptionError` | |
| `manufacturerLinkError` | |
| `manufacturerNameError` | |

### Examples

#### Basic Usage
```twig
<sw-manufacturer-detail>
    <!-- content -->
</sw-manufacturer-detail>
```

## sw-manufacturer-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onChangeLanguage` | |
| `getList` | |
| `updateTotal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `manufacturerRepository` | |
| `manufacturerColumns` | |
| `manufacturerCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-manufacturer-list>
    <!-- content -->
</sw-manufacturer-list>
```

## sw-many-to-many-assignment-card

> Card component for managing many-to-many entity relationships.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| columns | `any` | — | yes |  |
| entityCollection | `any` | — | yes |  |
| localMode | `any` | — | yes |  |
| resultLimit | `any` | `25` | no |  |
| criteria | `any` | — | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| labelProperty | `any` | `'name'` | no |  |
| selectLabel | `any` | `''` | no |  |
| placeholder | `any` | — | no |  |
| searchableFields | `any` | — | no |  |
| disabled | `any` | `false` | no |  |
| displayVariants | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| prepend-select | — | |
| select | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| data-grid | — | |
| `column-${column.property}` | — | |
| empty-state | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:entityCollection | — | |
| paginate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initData` | |
| `onSearchTermChange` | |
| `debouncedSearch` | |
| `onSelectExpanded` | |
| `paginateResult` | |
| `searchItems` | |
| `onItemSelect` | |
| `removeItem` | |
| `isSelected` | |
| `resetActiveItem` | |
| `onSelectCollapsed` | |
| `resetSearchCriteria` | |
| `getKey` | |
| `paginateGrid` | |
| `setGridFilter` | |
| `addContainsFilter` | |
| `removeFromGrid` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `context` | |
| `languageId` | |
| `assignmentRepository` | |
| `searchRepository` | |
| `page` | |
| `limit` | |
| `total` | |
| `focusEl` | |
| `originalFilters` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-products/sw-category-detail-products.html.twig`
```twig
<sw-many-to-many-assignment-card
    v-if="category.type !== 'folder'"
    display-variants
    :title="$tc('sw-category.base.products.productAssignmentHeadline')"
    :entity-collection="category.products"
    :columns="productColumns"
    :is-loading="isLoading"
    :disabled="!acl.can('category.editor')"
    :local-mode="category.isNew()"
    :criteria="productCriteria"
    :select-label="$tc('sw-category.base.products.productAssignmentLabel')"
    :placeholder="$tc('sw-category.base.products.productAssignmentPlaceholder')"
    @paginate="onPaginateManualProductAssignment"
>

```

#### Example 2
Source: `sw-category/view/sw-category-detail-custom-entity/sw-category-detail-custom-entity.html.twig`
```twig
<sw-many-to-many-assignment-card
    v-else
    :entity-collection="customEntityAssignments"
    :title="$tc('sw-category.base.customEntity.cardTitle')"
    :columns="customEntityColumns"
    :local-mode="category.isNew()"
    label-property="cmsAwareTitle"
    :criteria="sortingCriteria"
    :select-label="$tc('sw-category.base.customEntity.instanceAssignment.label')"
    :placeholder="$tc('sw-category.base.customEntity.instanceAssignment.placeholder')"
    @update:entity-collection="onAssignmentChange"
>
    <template #prepend-select>
        <sw-entity-single-select
            class="sw-category-detail-custom-entity__assignment"
```

## sw-media-add-thumbnail-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| thumbnail-form-size-add | — | |
| on-input | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onLockSwitch` | |
| `onAdd` | |
| `widthInputChanged` | |
| `heightInputChanged` | |
| `inputChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `lockedButtonClass` | |

### Examples

#### Basic Usage
```twig
<sw-media-add-thumbnail-form>
    <!-- content -->
</sw-media-add-thumbnail-form>
```

## sw-media-base-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| isList | `any` | `false` | no |  |
| showSelectionIndicator | `any` | `false` | no |  |
| showContextMenuButton | `any` | `true` | no |  |
| selected | `any` | `false` | no |  |
| editable | `any` | `true` | no |  |
| allowMultiSelect | `any` | `true` | no |  |
| truncateRight | `any` | `false` | no |  |
| allowEdit | `any` | `true` | no |  |
| allowDelete | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| preview | — | |
| name | — | |
| metadata | — | |
| context-menu | — | |
| modal-windows | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-click | — | |
| media-item-selection-add | — | |
| media-item-selection-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `handleItemClick` | |
| `isSelectionIndicatorClicked` | |
| `onClickedItem` | |
| `selectItem` | |
| `removeFromSelection` | |
| `startInlineEdit` | |
| `endInlineEdit` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaItemClasses` | |
| `mediaNameContainerClasses` | |
| `listSelected` | |
| `selectionIndicatorClasses` | |
| `isLoading` | |
| `isSpatial` | |

### Examples

#### Basic Usage
```twig
<sw-media-base-item
    item="..."
>
    <!-- content -->
</sw-media-base-item>
```

## sw-media-breadcrumbs

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentFolderId | `any` | `null` | no |  |
| small | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:currentFolderId | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateFolder` | |
| `onBreadcrumbsItemClicked` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `rootFolder` | |
| `swMediaBreadcrumbsClasses` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-media/component/sw-media-save-modal/sw-media-save-modal.html.twig`
```twig
        <sw-media-breadcrumbs
            v-model:current-folder-id="folderId"
            :small="compact"
            :disabled="isLoading"
        />
        {% endblock %}
    </div>
    {% endblock %}

    {% block sw_media_save_modal_media_library %}
    <sw-media-library
        ref="mediaLibrary"
        :selection="[]"
        :folder-id="folderId"
        :compact="compact"
```

#### Example 2
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
        <sw-media-breadcrumbs
            v-model:current-folder-id="folderId"
            :small="compact"
        />
        {% endblock %}

        {% block sw_media_modal_v2_search_field %}
        <!-- Bound and updated manually to use debounced search term -->
        <sw-simple-search-field
            :value="term"
            @search-term-change="onSearchTermChange"
        />
        {% endblock %}
    </div>
    {% endblock %}
```

## sw-media-collapse

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `expandButtonClass` | |
| `collapseButtonClass` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-collapse
    v-if="editable"
    :title="$tc('sw-media.sidebar.sections.actions')"
    :expand-on-loading="true"
>

    {% block sw_media_quickinfo_folder_quickactions_content %}
    <template #content>
        <ul class="sw-media-sidebar__quickactions-list">
            {% block sw_media_quickinfo_folder_quickactions_move %}
            <li
                v-tooltip="{
                    message: $tc('sw-privileges.tooltip.warning'),
                    disabled: acl.can('media.editor'),
                    showOnDisabledElements: true
```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-collapse
    :expand-on-loading="true"
    :title="$tc('sw-media.sidebar.sections.metadata')"
>

    {% block sw_media_quickinfo_folder_metadata_content %}
    <template #content>
        <dl class="sw-media-sidebar__metadata-list">
            {% block sw_media_quickinfo_folder_metadata_content_base %}
            <sw-media-quickinfo-metadata-item
                class="sw-media-quickinfo-metadata-name"
                :class="nameItemClasses"
                :label-name="$tc('sw-media.sidebar.metadata.name')"
                :truncated="false"
            >
```

#### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-collapse
    v-if="editable"
    :title="$t('sw-media.sidebar.sections.actions')"
    :expand-on-loading="true"
>

    <template #content>
        {% block sw_media_quickinfo_quickactions_content %}
        <ul
            :key="item.id"
            class="sw-media-sidebar__quickactions-list"
        >
            {% block sw_media_quickinfo_quickactions_replace %}
            <li
                v-if="!item.private"
```

#### Example 4
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-collapse
    v-if="isSpatial"
    :title="$t('sw-media.sidebar.sections.configuration')"
    :expand-on-loading="true"
>
    <template #content>
        <sw-inherit-wrapper
            v-model:value="arReady"
            :inherited-value="defaultArReady"
            @update:value="toggleAR"
        >
            <template #content="props">

                <mt-switch
                    :is-inheritance-field="props.isInheritField"
```

#### Example 5
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
<sw-media-collapse
    v-if="editable"
    :title="$tc('sw-media.sidebar.sections.actions')"
    :expand-on-loading="true"
>

    {% block sw_media_quickinfo_multiple_quickactions_content %}
    <template #content>
        <ul class="sw-media-sidebar__quickactions-list">
            {% block sw_media_quickinfo_multiple_quickactions_move %}
            <li
                class="quickaction--move"
                :class="quickActionClasses(!acl.can('media.editor'))"
                role="button"
                tabindex="0"
```

## sw-media-compact-upload-v2

> Compact variant of the media upload component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowMultiSelect | `any` | `false` | no |  |
| disableDeletionForLastItem | `any` | — | no |  |
| variant | `any` | `'regular'` | no | Valid: `compact`, `regular` |
| source | `null \| null` | `''` | no |  |
| sourceMultiselect | `any` | — | no |  |
| fileAccept | `any` | `'image/*'` | no |  |
| removeButtonLabel | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| context-menu-items | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| delete-item | — | |
| selection-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `onModalClosed` | |
| `getFileName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaPreview` | |
| `removeFileButtonLabel` | |
| `isDeletionDisabled` | |
| `mediaNameFilter` | |

### Examples

#### Example 1
Source: `sw-property/component/sw-property-option-detail/sw-property-option-detail.html.twig`
```twig
<sw-media-compact-upload-v2
    default-folder="product"
    :label="$tc('sw-property.detail.labelMediaUpload')"
    :source="currentOption.mediaId"
    :upload-tag="currentOption.id"
    :disabled="!allowEdit"
    @media-upload-remove-image="removeMedia"
    @selection-change="setMedia"
/>
{% endblock %}

<sw-custom-field-set-renderer
    v-if="showCustomFields"
    :entity="currentOption"
    :sets="customFieldSets"
```

#### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section-config/sw-cms-section-config.html.twig`
```twig
        <sw-media-compact-upload-v2
            :source="section && section.backgroundMedia && section.backgroundMedia.id ? section.backgroundMedia : null"
            :upload-tag="uploadTag"
            :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
            :default-folder="cmsPageState.pageEntityName"
            :allow-multi-select="false"
            @media-upload-remove-image="removeMedia"
            @selection-change="onSetBackgroundMedia"
        />
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

```

#### Example 3
Source: `sw-cms/component/sw-cms-block/sw-cms-block-config/sw-cms-block-config.html.twig`
```twig
        <sw-media-compact-upload-v2
            :source="block && block.backgroundMedia && block.backgroundMedia.id ? block.backgroundMedia : null"
            :upload-tag="uploadTag"
            :label="$tc('sw-cms.detail.label.backgroundMediaLabel')"
            :default-folder="cmsPageState.pageEntityName"
            :allow-multi-select="false"
            @media-upload-remove-image="removeMedia"
            @selection-change="onSetBackgroundMedia"
        />
        <sw-upload-listener
            :upload-tag="uploadTag"
            auto-upload
            @media-upload-finish="successfulUpload"
        />

```

#### Example 4
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
        <sw-media-compact-upload-v2
            v-if="productDownloadFolderId"
            :button-label="$tc('sw-product.variations.configuratorModal.uploadAllButton')"
            :remove-button-label="$tc('sw-product.variations.configuratorModal.removeAllButton')"
            upload-tag="upload_all"
            private-filesystem
            :source-multiselect="downloadFilesForAllVariants.length > 0 ? downloadFilesForAllVariants : null"
            allow-multi-select
            add-files-on-multiselect
            :target-folder-id="productDownloadFolderId"
            file-accept="*/*"
            @delete-item="(file) => removeFileForAllVariants(file)"
        />
    </div>
</div>
```

#### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
                    <sw-media-compact-upload-v2
                        v-if="productDownloadFolderId"
                        :upload-tag="item.productNumber"
                        :disabled="item.type !== 'digital'"
                        private-filesystem
                        allow-multi-select
                        add-files-on-multiselect
                        :source-multiselect="item.downloads.length > 0 ? item.downloads : null"
                        :target-folder-id="productDownloadFolderId"
                        file-accept="*/*"
                        @delete-item="(file) => removeFile(`${file.fileName}.${file.fileExtension}`, item)"
                    />
                </div>
            </template>

```

## sw-media-display-options

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| presentation | `any` | `'medium-preview'` | no | Valid: `small-preview`, `medium-preview`, `large-preview`, `list-preview` |
| sorting | `any` | — | no |  |
| hidePresentation | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-sorting-change | — | |
| media-presentation-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSortingChanged` | |
| `onPresentationChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sortingConCat` | |
| `sortOptions` | |
| `previewOptions` | |
| `presentationOptions` | |
| `sortOptionsSelect` | |

### Examples

#### Example 1
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-display-options
    class="sw-media-library__display-options"
    :presentation="presentation"
    :sorting="sorting"
    :hide-presentation="compact"
    :disabled="disabled"
    @media-presentation-change="presentation = $event"
    @media-sorting-change="sorting = $event"
/>

<sw-extension-teaser-popover
    position-identifier="sw-media-generate-image-button"
/>

{% block sw_media_index_create_folder %}
```

## sw-media-entity-mapper

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `mapEntity` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
        <sw-media-entity-mapper
            v-for="mediaItem in items"
            :key="mediaItem.id"
            :item="mediaItem"
            :selected="true"
            :is-list="true"
            :show-context-menu-button="false"
            :show-selection-indicator="true"
            @media-item-selection-remove="onRemoveItemFromSelection"
        />
    </template>
    {% endblock %}
</sw-media-collapse>
{% endblock %}

```

#### Example 2
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-entity-mapper
    v-for="(gridItem, index) in selectableItems"
    :key="gridItem.getEntityName() + '_' + gridItem.id"
    :class="`sw-media-grid-item__item--${index}`"
    :item="gridItem"
    :disabled="disabled"
    :allow-edit="acl.can('media.editor')"
    :allow-delete="acl.can('media.deleter')"
    :selected="showItemSelected(gridItem)"
    :show-selection-indicator="isListSelect"
    :show-context-menu-button="editable"
    :is-list="showItemsAsList"
    :editable="editable"
    :allow-multi-select="allowMultiSelect"
    @media-item-replaced="refreshList"
```

## sw-media-field

> Media selection field for picking images/files from the media library.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| label | `any` | `null` | no |  |
| defaultFolder | `any` | `null` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |
| `fetchItem` | |
| `fetchSuggestions` | |
| `onTogglePicker` | |
| `mediaItemChanged` | |
| `removeLink` | |
| `computePickerPositionAndStyle` | |
| `toggleUploadField` | |
| `exposeNewId` | |
| `showLabel` | |
| `onPageChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaId` | |
| `mediaRepository` | |
| `popoverConfig` | |
| `mediaFieldClasses` | |
| `toggleButtonLabel` | |
| `suggestionCriteria` | |

### Examples

#### Example 1
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
    <sw-media-field
        :value="documentConfig.logoId"
        @update:value="(v) => documentConfig.logoId = v"
        name="sw-field--documentConfig-logoId"
        :disabled="!acl.can('document.editor')"
        :label="$tc('sw-settings-document.detail.labelOptionMedia')"
    />
</div>
{% endblock %}

{% block sw_settings_document_detail_content_field_file_name_prefix %}
<div class="sw-settings-document-detail__field_file_name_prefix">

    <mt-text-field
        v-model="documentConfig.filenamePrefix"
```

## sw-media-folder-content

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| startFolderId | `any` | `null` | no |  |
| selectedId | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selected | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getSubFolders` | |
| `getChildCount` | |
| `fetchParentFolder` | |
| `updateParentFolder` | |
| `emitInput` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-media-folder-content>
    <!-- content -->
</sw-media-folder-content>
```

## sw-media-folder-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaFolder | `any` | — | yes |  |
| editable | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-folder-renamed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeFolderName` | |
| `quickActionClasses` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `createdAt` | |
| `mediaFolderNameError` | |
| `nameItemClasses` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-sidebar/sw-media-sidebar.html.twig`
```twig
    <sw-media-folder-info
        v-else-if="isSingleFile && firstEntity.getEntityName() === 'media_folder'"
        :media-folder="firstEntity"
        :editable="editable"
        v-bind="filteredAttributes"
    />

    <sw-media-quickinfo-multiple
        v-else-if="isMultipleFile"
        :editable="editable"
        :items="items"
        v-bind="filteredAttributes"
    />

    <sw-media-folder-info
```

## sw-media-folder-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isParent | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-folder-remove | — | |
| media-folder-changed | — | |
| media-folder-delete | — | |
| media-folder-dissolve | — | |
| media-folder-move | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getIconConfigFromFolder` | |
| `onChangeName` | |
| `onBlur` | |
| `rejectRenaming` | |
| `navigateToFolder` | |
| `openSettings` | |
| `closeSettings` | |
| `openDissolveModal` | |
| `closeDissolveModal` | |
| `openDeleteModal` | |
| `closeDeleteModal` | |
| `emitItemDeleted` | |
| `onFolderDissolved` | |
| `onFolderMoved` | |
| `openMoveModal` | |
| `closeMoveModal` | |
| `refreshIconConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaDefaultFolderRepository` | |
| `moduleFactory` | |
| `mediaFolder` | |
| `iconName` | |
| `assetFilter` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-folder-item
    v-if="parentFolder && (!isLoading || selectableItems.length > 0)"
    :allow-edit="acl.can('media.editor')"
    :allow-delete="acl.can('media.deleter')"
    :disabled="disabled"
    class="sw-media-library__parent-folder"
    :item="parentFolder"
    :show-selection-indicator="false"
    :show-context-menu-button="false"
    :allow-multi-select="allowMultiSelect"
    :is-list="showItemsAsList"
    is-parent
    @media-item-click="goToParentFolder"
/>
{% endblock %}
```

## sw-media-grid

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| presentation | `any` | `'medium-preview'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| content | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-grid-selection-clear | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `clearSelectionOnClickOutside` | |
| `originatesFromExcludedComponent` | |
| `isEmittedFromChildren` | |
| `emitSelectionCleared` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaColumnDefinitions` | |
| `presentationClass` | |
| `nonDeselectingComponents` | |

### Examples

#### Example 1
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
<sw-media-grid
    ref="mediaGrid"
    class="sw-media-library_media-grid"
    :presentation="gridPresentation"
    @media-grid-selection-clear="clearSelection"
>

    {% block sw_media_library_back_to_parent_item %}
    <sw-media-folder-item
        v-if="parentFolder && (!isLoading || selectableItems.length > 0)"
        :allow-edit="acl.can('media.editor')"
        :allow-delete="acl.can('media.deleter')"
        :disabled="disabled"
        class="sw-media-library__parent-folder"
        :item="parentFolder"
```

#### Example 2
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
<sw-media-grid
    :presentation="compact ? 'list-preview' : 'medium-preview'"
    :class="{'sw-media-modal-v2__upload-media-grid--compact': compact }"
>
    <sw-media-media-item
        v-for="upload in uploads"
        :key="`sw-media-modal-v2-upload-${upload.id}`"
        :item="upload"
        :show-context-menu-button="false"
        :show-selection-indicator="allowMultiSelect"
        :allow-multi-select="allowMultiSelect"
        :selected="checkMediaItem(upload)"
        :editable="false"
        :is-list="compact"
        @media-item-selection-remove="onMediaRemoveSelected"
```

## sw-media-index

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| routeFolderId | `any` | `null` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateFolder` | |
| `destroyedComponent` | |
| `onUploadsAdded` | |
| `onUploadFinished` | |
| `onUploadFailed` | |
| `onUploadCanceled` | |
| `onChangeLanguage` | |
| `onSearch` | |
| `onItemsDeleted` | |
| `onMediaFoldersDissolved` | |
| `reloadList` | |
| `decrementPendingUploads` | |
| `clearSelection` | |
| `onMediaUnselect` | |
| `updateRoute` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaRepository` | |
| `rootFolder` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-media-index>
    <!-- content -->
</sw-media-index>
```

## sw-media-library

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selection | `any` | — | yes |  |
| folderId | `any` | `null` | no |  |
| pendingUploads | `any` | — | no |  |
| limit | `any` | `25` | no | Valid: `1`, `5`, `25`, `50`, `100`, `500` |
| term | `any` | `''` | no |  |
| compact | `any` | `false` | no |  |
| editable | `any` | `false` | no |  |
| allowMultiSelect | `any` | `true` | no |  |
| allowCreateFolder | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:selection | — | |
| media-folder-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `refreshList` | |
| `isValidTerm` | |
| `loadNextItems` | |
| `mapFolderSorting` | |
| `isLoaderDone` | |
| `loadItems` | |
| `nextMedia` | |
| `nextFolders` | |
| `fetchAssociatedFolders` | |
| `goToParentFolder` | |
| `clearSelection` | |
| `injectItem` | |
| `injectMedia` | |
| `createFolder` | |
| `removeNewFolder` | |
| `refreshItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shouldDisplayEmptyState` | |
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaFolderConfigurationRepository` | |
| `selectableItems` | |
| `rootFolder` | |
| `gridPresentation` | |
| `showItemsAsList` | |
| `showLoadMoreButton` | |
| `nextMediaCriteria` | |
| `nextFoldersCriteria` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-media/page/sw-media-index/sw-media-index.html.twig`
```twig
    <sw-media-library
        ref="mediaLibrary"
        v-model:selection="selectedItems"
        class="sw-media-index__media-library"
        :folder-id="routeFolderId"
        :pending-uploads="uploads"
        :term="term"
        editable
        @media-folder-change="updateRoute"
    />
    {% endblock %}

    {% block sw_media_index_sidebar %}
    <sw-media-sidebar
        :items="selectedItems"
```

#### Example 2
Source: `sw-media/component/sw-media-save-modal/sw-media-save-modal.html.twig`
```twig
    <sw-media-library
        ref="mediaLibrary"
        :selection="[]"
        :folder-id="folderId"
        :compact="compact"
        :disabled="isLoading"
        allow-create-folder
        :allow-multi-select="false"
        @media-folder-change="folderId = $event"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_media_save_modal_modal_footer %}
```

#### Example 3
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
    <sw-media-library
        ref="mediaLibrary"
        :selection="selection"
        :folder-id="folderId"
        :term="term"
        :compact="compact"
        :allow-multi-select="allowMultiSelect"
        @update:selection="selection = $event"
        @media-folder-change="folderId = $event"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_media_modal_v2_tab_content_upload %}
```

## sw-media-list-selection-item-v2

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| hideActions | `any` | `false` | no |  |
| hideTooltip | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |
| item-remove | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isPlaceholder` | |
| `productImageClasses` | |
| `sourceId` | |

### Examples

#### Example 1
Source: `sw-cms/elements/image-gallery/component/sw-cms-el-image-gallery.html.twig`
```twig
            <sw-media-list-selection-item-v2
                v-if="index < galleryLimit"
                :item="sliderItem.media"
                :class="activeMediaClass(sliderItem.media)"
                hide-actions
                hide-tooltip
                @click="onChangeGalleryImage(sliderItem.media, index)"
            />
        </template>
        {% endblock %}
    </div>
</template>

<template v-else>
    {% block sw_cms_element_image_gallery_empty %}
```

## sw-media-list-selection-v2

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entity | `any` | — | yes |  |
| entityMediaItems | `any` | — | yes |  |
| uploadTag | `any` | `null` | no |  |
| defaultFolderName | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| open-sidebar | — | |
| upload-finish | — | |
| item-sort | — | |
| item-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `updateColumnCount` | |
| `createPlaceholders` | |
| `onUploadsAdded` | |
| `onMediaUploadButtonOpenSidebar` | |
| `successfulUpload` | |
| `onUploadFailed` | |
| `onMediaItemDragSort` | |
| `onDeboundDragDrop` | |
| `removeItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `currentCount` | |
| `mediaItems` | |
| `gridAutoRows` | |
| `uploadId` | |
| `defaultFolder` | |

### Examples

#### Example 1
Source: `sw-cms/elements/image-slider/config/sw-cms-el-config-image-slider.html.twig`
```twig
        <sw-media-list-selection-v2
            :entity-media-items="mediaItems"
            :entity="entity"
            :upload-tag="uploadTag"
            :default-folder-name="defaultFolderName"
            :disabled="isInherited"
            @upload-finish="onImageUpload"
            @item-remove="onItemRemove"
            @open-sidebar="onOpenMediaModal"
            @item-sort="onItemSort"
        />
    </template>
</sw-cms-inherit-wrapper>
{% endblock %}

```

#### Example 2
Source: `sw-cms/elements/image-gallery/config/sw-cms-el-config-image-gallery.html.twig`
```twig
<sw-media-list-selection-v2
    :entity-media-items="mediaItems"
    :entity="entity"
    :upload-tag="uploadTag"
    :default-folder-name="defaultFolderName"
    :disabled="isInherited"
    @upload-finish="onImageUpload"
    @item-remove="onItemRemove"
    @open-sidebar="onOpenMediaModal"
    @item-sort="onItemSort"
/>
{% endblock %}

{% block sw_cms_element_image_gallery_config_media_mapping_preview %}
<template #preview="{ demoValue }">
```

## sw-media-media-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-rename-success | — | |
| media-item-play | — | |
| media-item-delete | — | |
| media-folder-move | — | |
| media-item-replaced | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeName` | |
| `handleErrorMessage` | |
| `rejectRenaming` | |
| `onBlur` | |
| `emitPlayEvent` | |
| `copyItemLink` | |
| `openModalDelete` | |
| `closeModalDelete` | |
| `emitItemDeleted` | |
| `openModalReplace` | |
| `closeModalReplace` | |
| `openModalMove` | |
| `closeModalMove` | |
| `onMediaItemMoved` | |
| `emitRefreshMediaLibrary` | |
| `runAppAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `locale` | |
| `defaultContextMenuClass` | |
| `mediaNameFilter` | |
| `dateFilter` | |
| `fileSizeFilter` | |
| `extensionSdkButtons` | |

### Examples

#### Example 1
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
                    <sw-media-media-item
                        v-for="upload in uploads"
                        :key="`sw-media-modal-v2-upload-${upload.id}`"
                        :item="upload"
                        :show-context-menu-button="false"
                        :show-selection-indicator="allowMultiSelect"
                        :allow-multi-select="allowMultiSelect"
                        :selected="checkMediaItem(upload)"
                        :editable="false"
                        :is-list="compact"
                        @media-item-selection-remove="onMediaRemoveSelected"
                        @media-item-selection-add="onMediaAddSelected"
                        @media-item-click="onMediaItemSelect"
                    />
                </sw-media-grid>
```

## sw-media-modal-delete

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemsToDelete | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-delete-modal-close | — | |
| media-delete-modal-items-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `closeDeleteModal` | |
| `getEntityRepository` | |
| `_deleteSelection` | |
| `deleteSelection` | |
| `updateSuccessNotification` | |
| `_checkInUsage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaNameFilter` | |
| `snippets` | |
| `mediaQuickInfo` | |
| `mediaInUsages` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
    <sw-media-modal-delete
        v-if="showModalDelete"
        :items-to-delete="[mediaFolder]"
        @media-delete-modal-close="closeModalDelete"
        @media-delete-modal-items-delete="deleteSelectedItems"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-modal-delete
    v-if="showModalDelete"
    :items-to-delete="[item]"
    @media-delete-modal-close="closeModalDelete"
    @media-delete-modal-items-delete="deleteSelectedItems"
/>
{% endblock %}

{% block sw_media_quickinfo_move_modal %}
<sw-media-modal-move
    v-if="showModalMove"
    :items-to-move="[item]"
    @media-move-modal-close="closeModalMove"
    @media-move-modal-items-move="onFolderMoved"
/>
```

#### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
    <sw-media-modal-delete
        v-if="showModalDelete"
        :items-to-delete="items"
        @media-delete-modal-close="closeModalDelete"
        @media-delete-modal-items-delete="deleteSelectedItems"
    />
    {% endblock %}

    {% block sw_media_sidebar_folder_dissolve_modal %}
    <sw-media-modal-folder-dissolve
        v-if="!hasMedia && showFolderDissolve"
        :items-to-dissolve="items"
        @media-folder-dissolve-modal-dissolve="onFolderDissolved"
        @media-folder-dissolve-modal-close="closeFolderDissolve"
    />
```

## sw-media-modal-folder-dissolve

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemsToDissolve | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-folder-dissolve-modal-close | — | |
| media-folder-dissolve-modal-dissolve | — | |

### Methods

| Method | Description |
|--------|-------------|
| `closeDissolveModal` | |
| `_dissolveSelection` | |
| `dissolveSelection` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
    <sw-media-modal-folder-dissolve
        v-if="showFolderDissolve"
        :items-to-dissolve="[mediaFolder]"
        @media-folder-dissolve-modal-dissolve="onFolderDissolved"
        @media-folder-dissolve-modal-close="closeFolderDissolve"
    />
    {% endblock %}

    {% block sw_media_folder_info_move_modal %}
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="[mediaFolder]"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
    <sw-media-modal-folder-dissolve
        v-if="!hasMedia && showFolderDissolve"
        :items-to-dissolve="items"
        @media-folder-dissolve-modal-dissolve="onFolderDissolved"
        @media-folder-dissolve-modal-close="closeFolderDissolve"
    />
    {% endblock %}

    {% block sw_media_sidebar_folder_move_modal %}
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="items"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
```

## sw-media-modal-folder-settings

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaFolderId | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-settings-modal-save | — | |
| media-settings-modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getItemName` | |
| `getUnusedThumbnailSizes` | |
| `getThumbnailSizes` | |
| `addThumbnail` | |
| `checkIfThumbnailExists` | |
| `deleteThumbnail` | |
| `isThumbnailSizeActive` | |
| `thumbnailSizeCheckboxName` | |
| `onActiveTabChanged` | |
| `onChangeThumbnailSize` | |
| `onChangeInheritance` | |
| `onClickSave` | |
| `ensureUniqueDefaultFolder` | |
| `onClickCancel` | |
| `closeModal` | |
| `onInputDefaultFolder` | |
| `loadMediaFolder` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaDefaultFolderRepository` | |
| `mediaThumbnailSizeRepository` | |
| `mediaFolderConfigurationRepository` | |
| `unusedMediaThumbnailSizeCriteria` | |
| `mediaThumbnailSizeCriteria` | |
| `notEditable` | |
| `thumbnailSizeFilter` | |
| `mediaFolderNameError` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-modal-folder-settings
    v-if="showFolderSettings"
    :disabled="!acl.can('media.editor')"
    :media-folder-id="mediaFolder.id"
    @media-settings-modal-save="closeFolderSettings"
    @media-settings-modal-close="closeFolderSettings"
/>
{% endblock %}

{% block sw_media_folder_info_dissolve_modal %}
<sw-media-modal-folder-dissolve
    v-if="showFolderDissolve"
    :items-to-dissolve="[mediaFolder]"
    @media-folder-dissolve-modal-dissolve="onFolderDissolved"
    @media-folder-dissolve-modal-close="closeFolderDissolve"
```

## sw-media-modal-move

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemsToMove | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-move-modal-close | — | |
| media-move-modal-items-move | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `closeMoveModal` | |
| `isNotPartOfItemsToMove` | |
| `updateParentFolder` | |
| `fetchParentFolder` | |
| `onSelection` | |
| `_moveSelection` | |
| `moveSelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaNameFilter` | |
| `targetFolderId` | |
| `rootFolderName` | |
| `isMoveDisabled` | |
| `startFolderId` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="[mediaFolder]"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
    {% endblock %}

    {% block sw_media_folder_info_modal_delete %}
    <sw-media-modal-delete
        v-if="showModalDelete"
        :items-to-delete="[mediaFolder]"
        @media-delete-modal-close="closeModalDelete"
        @media-delete-modal-items-delete="deleteSelectedItems"
    />
```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-modal-move
    v-if="showModalMove"
    :items-to-move="[item]"
    @media-move-modal-close="closeModalMove"
    @media-move-modal-items-move="onFolderMoved"
/>
{% endblock %}

{% block sw_media_quickinfo_cover_modal %}
<sw-media-modal-v2
    v-if="showCoverSelectionModal"
    :allow-multi-select="false"
    file-accept="image/*"
    @modal-close="closeCoverSelectionModal"
    @media-modal-selection-change="onCoverSelectionChange"
```

#### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo-multiple/sw-media-quickinfo-multiple.html.twig`
```twig
    <sw-media-modal-move
        v-if="showModalMove"
        :items-to-move="items"
        @media-move-modal-close="closeModalMove"
        @media-move-modal-items-move="onFolderMoved"
    />
    {% endblock %}
</div>
{% endblock %}


```

## sw-media-modal-renderer

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `closeSaveModal` | |
| `onSelectionChange` | |
| `getValueByPath` | |
| `transformObjectsByPaths` | |
| `setValueByPath` | |
| `onSaveMedia` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaModal` | |
| `saveMediaModal` | |

### Examples

#### Basic Usage
```twig
<sw-media-modal-renderer>
    <!-- content -->
</sw-media-modal-renderer>
```

## sw-media-modal-replace

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemToReplace | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-replace-modal-close | — | |
| media-replace-modal-item-replaced | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onNewUpload` | |
| `emitCloseReplaceModal` | |
| `replaceMediaItem` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-modal-replace
    v-if="showModalReplace"
    :item-to-replace="item"
    @media-replace-modal-item-replaced="emitRefreshMediaLibrary"
    @media-replace-modal-close="closeModalReplace"
/>
{% endblock %}

{% block sw_media_quickinfo_modal_delete %}
<sw-media-modal-delete
    v-if="showModalDelete"
    :items-to-delete="[item]"
    @media-delete-modal-close="closeModalDelete"
    @media-delete-modal-items-delete="deleteSelectedItems"
/>
```

## sw-media-modal-v2

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isOpen | `any` | `true` | no |  |
| initialFolderId | `any` | `null` | no |  |
| entityContext | `any` | `null` | no |  |
| defaultTab | `any` | `'library'` | no | Valid: `upload`, `library` |
| allowMultiSelect | `any` | `true` | no |  |
| fileAccept | `any` | `'image/*'` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| media-modal-selection-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `fetchCurrentFolder` | |
| `addResizeListener` | |
| `removeOnResizeListener` | |
| `getComponentWidth` | |
| `onModalRootChange` | |
| `onEmitModalClosed` | |
| `onEmitSelection` | |
| `refreshList` | |
| `onMediaRemoveSelected` | |
| `onMediaAddSelected` | |
| `onMediaItemSelect` | |
| `resetSelection` | |
| `onItemsDeleted` | |
| `onMediaFoldersDissolved` | |
| `onUploadsAdded` | |
| `onUploadFinished` | |
| `onUploadFailed` | |
| `selectMediaItem` | |
| `checkMediaItem` | |
| `onSearchTermChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `tabNameUpload` | |
| `tabNameLibrary` | |
| `hasUploads` | |
| `uploadTag` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-media/sw-bulk-edit-product-media.html.twig`
```twig
    <sw-media-modal-v2
        v-if="showMediaModal"
        :initial-folder-id="mediaDefaultFolderId"
        :entity-context="product.getEntityName()"
        @media-modal-selection-change="onAddMedia"
        @modal-close="showMediaModal = false"
    />
    {% endblock %}
</div>
{% endblock %}

```

#### Example 2
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
<sw-media-modal-v2
    v-if="showMediaModal"
    :allow-multi-select="false"
    :entity-context="category.getEntityName()"
    @media-modal-selection-change="onMediaSelectionChange"
    @modal-close="showMediaModal = false"
/>
{% endblock %}

{% block sw_category_detail_menu_description %}
<sw-text-editor
    v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
    :key="category.id + 'description'"
    v-model:value="category.description"
    class="sw-category-detail-base__description"
```

#### Example 3
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
<sw-media-modal-v2
    v-if="showMediaModal"
    :caption="$tc('sw-cms.components.cmsListItem.modal.captionMediaUpload')"
    :entity-context="'cms_page'"
    :allow-multi-select="false"
    @media-modal-selection-change="onPreviewImageChange"
    @modal-close="onModalClose"
/>
{% endblock %}

<sw-confirm-modal
    v-if="showLayoutSetAsDefaultModal"
    class="sw-cms-list__confirm-set-as-default-modal"
    :title="$tc('sw-cms.components.setDefaultLayoutModal.title')"
    :text="$tc('sw-cms.components.setDefaultLayoutModal.infoText', {}, newDefaultLayout.type === 'product_detail')"
```

#### Example 4
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
        <sw-media-modal-v2
            v-if="showMediaModal"
            variant="full"
            :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
            :entity-context="cmsPageState.entityName"
            :allow-multi-select="false"
            :initial-folder-id="cmsPageState.defaultMediaFolderId"
            file-accept="video/*"
            @media-upload-remove-video="onVideoRemove"
            @media-modal-selection-change="onSelectionChanges"
            @modal-close="onCloseModal"
        />
        {% endblock %}
    </template>
</sw-cms-inherit-wrapper>
```

#### Example 5
Source: `sw-cms/elements/youtube-video/config/sw-cms-el-config-youtube-video.html.twig`
```twig
            <sw-media-modal-v2
                v-if="mediaModalIsOpen"
                variant="full"
                :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
                :entity-context="cmsPageState.entityName"
                :allow-multi-select="false"
                :initial-folder-id="cmsPageState.defaultMediaFolderId"
                @media-upload-remove-image="onImageRemove"
                @media-modal-selection-change="onSelectionChanges"
                @modal-close="onCloseModal"
            />
            {% endblock %}
        </template>
    </sw-cms-inherit-wrapper>
    {% endblock %}
```

## sw-media-preview-v2

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `any` | — | yes |  |
| showControls | `any` | `false` | no |  |
| autoplay | `any` | `false` | no |  |
| transparency | `any` | `true` | no |  |
| useThumbnails | `any` | `true` | no |  |
| hideTooltip | `any` | `true` | no |  |
| mediaIsPrivate | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |
| media-preview-play | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `mountedComponent` | |
| `fetchSourceIfNecessary` | |
| `onPlayClick` | |
| `getDataUrlFromFile` | |
| `reloadMediaElement` | |
| `removeUrlPreview` | |
| `showEvent` | |
| `onMediaLibraryItemUpdated` | |
| `getCurrentMediaId` | |
| `ensureVideoCoverMedia` | |
| `getVideoCoverMediaId` | |
| `buildSourceSet` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaPreviewClasses` | |
| `transparencyClass` | |
| `canBeTransparent` | |
| `mimeType` | |
| `mimeTypeGroup` | |
| `isPlayable` | |
| `showUnsupportedFormatWarning` | |
| `isIcon` | |
| `placeholderIcon` | |
| `placeholderIconPath` | |
| `lockIsVisible` | |
| `previewUrl` | |
| `isUrl` | |
| `isFile` | |
| `isRelativePath` | |
| `alt` | |
| `mediaName` | |
| `mediaNameFilter` | |
| `assetFilter` | |
| `sourceSet` | |
| `videoCoverMedia` | |
| `videoCoverPoster` | |
| `hasVideoCover` | |
| `videoPreloadValue` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
                <sw-media-preview-v2
                    class="sw-media-quickinfo__media-preview"
                    :source="item.id"
                    :show-controls="true"
                    :use-thumbnails="false"
                />
            </template>
            {% endblock %}
        </div>
    </template>
    {% endblock %}
</sw-media-collapse>
{% endblock %}

{% block sw_media_quickinfo_metadata %}
```

#### Example 2
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
<sw-media-preview-v2 :source="item.cover ? item.cover.media : null" />
```

#### Example 3
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
<sw-media-preview-v2 :source="getItemMedia(item)" />
```

#### Example 4
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
<sw-media-preview-v2 :source="getItemMedia(item)" />
```

#### Example 5
Source: `sw-product/component/sw-product-media-form/sw-product-media-form.html.twig`
```twig
            <sw-media-preview-v2
                :key="cover ? cover.media?.url : product.cover.media?.url"
                class="sw-product-media-form__cover-image"
                :source="cover ? cover.mediaId : product.cover.mediaId"
            />
            {% endblock %}
            <span>{{ $tc('sw-product.mediaForm.coverSubline') }}</span>
        </div>
    </div>
    <div
        v-else
        class="sw-product-media-form__cover-image is--placeholder"
    >
        {{ $tc('sw-product.mediaForm.coverSubline') }}
    </div>
```

## sw-media-quickinfo-metadata-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| labelName | `any` | — | yes |  |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-name"
    :class="nameItemClasses"
    :label-name="$tc('sw-media.sidebar.metadata.name')"
    :truncated="false"
>
    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        :disabled="!acl.can('media.creator')"
        compact
        :value="mediaFolder.name"
        :error="mediaFolderNameError"
        @input="onChangeFolderName"
    />
```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-createdAt"
    :label-name="$tc('sw-media.sidebar.metadata.createdAt')"
>
    {{ createdAt }}
</sw-media-quickinfo-metadata-item>
```

#### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-name"
    :class="fileNameClasses"
    :label-name="$t('sw-media.sidebar.metadata.name')"
    :truncated="false"
>

    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        class="sw-media-quickinfo-metadata-name"
        :disabled="!acl.can('media.editor')"
        compact
        :value="item.fileName"
        :error="fileNameError"
```

#### Example 4
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-file-type"
    :label-name="$t('sw-media.sidebar.metadata.fileType')"
>
    {{ item.fileExtension.toUpperCase() }}
</sw-media-quickinfo-metadata-item>
```

## sw-media-quickinfo-multiple

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| editable | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-selection-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onRemoveItemFromSelection` | |
| `quickActionClassesDelete` | |
| `quickActionClasses` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `itemsIsAvailable` | |
| `getFileSize` | |
| `getFileSizeLabel` | |
| `hasFolder` | |
| `hasMedia` | |
| `isPrivate` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-sidebar/sw-media-sidebar.html.twig`
```twig
        <sw-media-quickinfo-multiple
            v-else-if="isMultipleFile"
            :editable="editable"
            :items="items"
            v-bind="filteredAttributes"
        />

        <sw-media-folder-info
            v-else-if="currentFolder"
            :media-folder="currentFolder"
            :editable="editable"
            v-bind="filteredAttributes"
            @media-folder-renamed="onMediaFolderRenamed"
        />

```

## sw-media-quickinfo-usage

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| routerLinkTarget | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadSlotConfigAssociations` | |
| `loadProductAssociations` | |
| `loadCategoryAssociations` | |
| `loadManufacturerAssociations` | |
| `loadMailTemplateAssociations` | |
| `loadDocumentBaseConfigAssociations` | |
| `loadAvatarUserAssociations` | |
| `loadPaymentMethodAssociations` | |
| `loadShippingMethodAssociations` | |
| `loadLayoutAssociations` | |
| `isExistedCmsMedia` | |
| `getProductUsage` | |
| `getCategoryUsage` | |
| `getManufacturerUsage` | |
| `getMailTemplateUsage` | |
| `getDocumentBaseConfigUsage` | |
| `getAvatarUserUsage` | |
| `getPaymentMethodUsage` | |
| `getShippingMethodUsage` | |
| `getLayoutUsage` | |
| `getLandingPageUsage` | |
| `getIconForModule` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `landingPageRepository` | |
| `categoryRepository` | |
| `cmsPageRepository` | |
| `moduleFactory` | |
| `slotConfigCriteria` | |
| `cmsPageBlockConfigCriteria` | |
| `getUsages` | |
| `isNotUsed` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-usage :item="item" />
```

## sw-media-quickinfo

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| editable | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-item-rename-success | — | |
| media-item-replaced | — | |
| update:item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchSpatialItemConfig` | |
| `buildAugmentedRealityTooltip` | |
| `loadCustomFieldSets` | |
| `onSave` | |
| `onSaveCustomFields` | |
| `saveFinish` | |
| `copyLinkToClipboard` | |
| `onSubmitTitle` | |
| `onSubmitAltText` | |
| `onChangeFileName` | |
| `handleErrorMessage` | |
| `openModalReplace` | |
| `closeModalReplace` | |
| `emitRefreshMediaLibrary` | |
| `quickActionClasses` | |
| `onRemoveFileNameError` | |
| `toggleAR` | |
| `changeARPlacement` | |
| `runAppAction` | |
| `openModelEditorModal` | |
| `closeModelEditorModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `isMediaObject` | |
| `fileSize` | |
| `createdAt` | |
| `fileNameClasses` | |
| `isSpatial` | |
| `extensionSdkButtons` | |
| `isPlayable` | |
| `showUnsupportedFormatWarning` | |
| `canManageVideoCover` | |
| `editorTooltip` | |
| `deleterTooltip` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
        <sw-media-quickinfo-metadata-item
            class="sw-media-quickinfo-metadata-name"
            :class="nameItemClasses"
            :label-name="$tc('sw-media.sidebar.metadata.name')"
            :truncated="false"
        >
            <sw-confirm-field
                v-if="editable"
                ref="inlineEditFieldName"
                :disabled="!acl.can('media.creator')"
                compact
                :value="mediaFolder.name"
                :error="mediaFolderNameError"
                @input="onChangeFolderName"
            />
```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-name"
    :class="fileNameClasses"
    :label-name="$t('sw-media.sidebar.metadata.name')"
    :truncated="false"
>

    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        class="sw-media-quickinfo-metadata-name"
        :disabled="!acl.can('media.editor')"
        compact
        :value="item.fileName"
        :error="fileNameError"
```

#### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-quickinfo-metadata-item
    class="sw-media-quickinfo-metadata-alt-field"
    :label-name="$t('sw-media.sidebar.metadata.title')"
    :truncated="false"
>
    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldTitle"
        :disabled="!acl.can('media.editor')"
        compact
        :placeholder="placeholder(item, 'title', $t('sw-media.sidebar.metadata.title'))"
        :value="item.title"
        @input="onSubmitTitle"
    />
    <template v-else>
```

#### Example 4
Source: `sw-media/component/sidebar/sw-media-sidebar/sw-media-sidebar.html.twig`
```twig
<sw-media-quickinfo
    v-if="isSingleFile && firstEntity.getEntityName() === 'media'"
    :item="firstEntity"
    :editable="editable"
    v-bind="filteredAttributes"
    @update:item="onFirstItemUpdated"
/>

<sw-media-folder-info
    v-else-if="isSingleFile && firstEntity.getEntityName() === 'media_folder'"
    :media-folder="firstEntity"
    :editable="editable"
    v-bind="filteredAttributes"
/>

```

## sw-media-replace

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemToReplace | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `getMediaEntityForUpload` | |
| `cleanUpFailure` | |

### Examples

#### Basic Usage
```twig
<sw-media-replace
    itemToReplace="..."
>
    <!-- content -->
</sw-media-replace>
```

## sw-media-save-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialFolderId | `any` | `null` | no |  |
| initialFileName | `any` | `null` | no |  |
| fileType | `any` | `'png'` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-media | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `addResizeListener` | |
| `removeOnResizeListener` | |
| `getComponentWidth` | |
| `fetchCurrentFolder` | |
| `getMediaEntityForUpload` | |
| `onSaveMedia` | |
| `onEmitModalClosed` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaFolderRepository` | |
| `mediaRepository` | |

### Examples

#### Basic Usage
```twig
<sw-media-save-modal>
    <!-- content -->
</sw-media-save-modal>
```

## sw-media-sidebar

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| currentFolderId | `any` | `null` | no |  |
| editable | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-sidebar-folder-renamed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchCurrentFolder` | |
| `onMediaFolderRenamed` | |
| `onFirstItemUpdated` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `mediaNameFilter` | |
| `mediaSidebarClasses` | |
| `isSingleFile` | |
| `isMultipleFile` | |
| `headLine` | |
| `getSelectedFilesCount` | |
| `firstEntity` | |
| `assetFilter` | |
| `filteredAttributes` | |

### Examples

#### Example 1
Source: `sw-media/page/sw-media-index/sw-media-index.html.twig`
```twig
            <sw-media-sidebar
                :items="selectedItems"
                :current-folder-id="routeFolderId"
                editable
                @media-sidebar-folder-renamed="updateFolder"
                @media-sidebar-items-delete="onItemsDeleted"
                @media-sidebar-folder-items-dissolve="onMediaFoldersDissolved"
                @media-sidebar-items-move="reloadList"
                @media-item-replaced="reloadList"
                @media-item-selection-remove="onMediaUnselect"
            />
            {% endblock %}

            {% block sw_media_index_list_grid_loader %}
            <sw-loader v-if="isLoading" />
```

#### Example 2
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
    <sw-media-sidebar
        :items="selection"
        :current-folder-id="null"
        @media-sidebar-items-delete="onItemsDeleted"
        @media-sidebar-folder-items-dissolve="onMediaFoldersDissolved"
        @media-sidebar-items-move="refreshList"
        @media-item-selection-remove="onMediaRemoveSelected"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_media_modal_v2_modal_footer %}
<template #footer>
    <div class="sw-media-modal-v2__footer">
```

## sw-media-tag

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| media | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `handleChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-media-tag
    :disabled="!acl.can('media.editor')"
    :media="item"
/>
{% endblock %}

{% block sw_media_quickinfo_usage %}
<sw-media-collapse
    v-if="editable && item.hasFile"
    :expand-on-loading="true"
    :title="$t('sw-media.sidebar.sections.usage')"
>

    <template #content>
        <sw-media-quickinfo-usage :item="item" />
```

## sw-media-upload-v2

> Media upload component supporting drag & drop, URL upload, and multi-file upload.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `null \| null \| null` | `null` | no |  |
| variant | `any` | `'regular'` | no | Valid: `compact`, `regular`, `small` |
| uploadTag | `any` | — | yes |  |
| allowMultiSelect | `any` | `true` | no |  |
| addFilesOnMultiselect | `any` | `false` | no |  |
| label | `any` | `null` | no |  |
| buttonLabel | `any` | `''` | no |  |
| defaultFolder | `any` | `null` | no |  |
| targetFolderId | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| sourceContext | `any` | `null` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |
| extensionAccept | `any` | `null` | no |  |
| maxFileSize | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| privateFilesystem | `any` | `false` | no |  |
| useFileData | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| onMediaUploadSidebarOpen | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-drop | — | |
| media-upload-sidebar-open | — | |
| media-upload-remove-image | — | |
| media-upload-add-file | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `onDrop` | |
| `onDropMedia` | |
| `onDragEnter` | |
| `onDragLeave` | |
| `stopEventPropagation` | |
| `onClickUpload` | |
| `useUrlUpload` | |
| `useFileUpload` | |
| `onClickOpenMediaSidebar` | |
| `onRemoveMediaItem` | |
| `onUrlUpload` | |
| `onFileInputChange` | |
| `handleUpload` | |
| `getMediaEntityForUpload` | |
| `getDefaultFolderId` | |
| `handleMediaServiceUploadEvent` | |
| `checkFileSize` | |
| `checkFileType` | |
| `handleFileCheck` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `defaultFolderRepository` | |
| `mediaRepository` | |
| `showPreview` | |
| `hasOpenMediaButtonListener` | |
| `isDragActiveClass` | |
| `mediaFolderId` | |
| `isUrlUpload` | |
| `isFileUpload` | |
| `uploadUrlFeatureEnabled` | |
| `swFieldLabelClasses` | |
| `buttonFileUploadLabel` | |
| `mediaNameFilter` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-detail-menu/sw-category-detail-menu.html.twig`
```twig
<sw-media-upload-v2
    :key="category.id + 'upload'"
    :label="$tc('sw-category.base.menu.imageLabel')"
    variant="regular"
    :disabled="!acl.can('category.editor')"
    :source="mediaItem"
    :upload-tag="category.id"
    :allow-multi-select="false"
    :default-folder="category.getEntityName()"
    @media-drop="onMediaDropped"
    @media-upload-sidebar-open="showMediaModal = true"
    @media-upload-remove-image="onRemoveMediaItem"
/>
{% endblock %}

```

#### Example 2
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-media-upload-v2
    variant="regular"
    :upload-tag="uploadTag"
    :source="previewSource"
    :allow-multi-select="false"
    :default-folder="cmsPageState.pageEntityName"
    :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
    :disabled="isInherited"
    file-accept="video/*"
    @media-upload-sidebar-open="onOpenMediaModal"
    @media-upload-remove-image="onVideoRemove"
/>

<template #preview="{ demoValue }">
    <div class="sw-cms-el-config-video__mapping-preview">
```

#### Example 3
Source: `sw-cms/elements/youtube-video/config/sw-cms-el-config-youtube-video.html.twig`
```twig
<sw-media-upload-v2
    variant="regular"
    :upload-tag="uploadTag"
    :source="previewSource"
    :allow-multi-select="false"
    :default-folder="cmsPageState.pageEntityName"
    :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
    :disabled="isInherited"
    @media-upload-sidebar-open="onOpenMediaModal"
    @media-upload-remove-image="onImageRemove"
/>

{% block sw_cms_element_youtube_video_config_preview_media_display %}
<template #preview="{ demoValue }">
    <div class="sw-cms-el-config-image__mapping-preview">
```

#### Example 4
Source: `sw-cms/elements/image/config/sw-cms-el-config-image.html.twig`
```twig
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
        @media-upload-remove-image="onImageRemove"
    />

    <template #preview="{ demoValue }">
        <div class="sw-cms-el-config-image__mapping-preview">
            <img
```

#### Example 5
Source: `sw-cms/elements/vimeo-video/config/sw-cms-el-config-vimeo-video.html.twig`
```twig
<sw-media-upload-v2
    variant="regular"
    :upload-tag="uploadTag"
    :source="previewSource"
    :allow-multi-select="false"
    :default-folder="cmsPageState.pageEntityName"
    :caption="$tc('sw-cms.elements.general.config.caption.mediaUpload')"
    :disabled="isInherited"
    @media-upload-sidebar-open="onOpenMediaModal"
    @media-upload-remove-image="onImageRemove"
/>

{% block sw_cms_element_vimeo_video_config_preview_media_display %}
<template #preview="{ demoValue }">
    <div class="sw-cms-el-config-image__mapping-preview">
```

## sw-media-url-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'inline'` | yes | Valid: `modal`, `inline` |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-url-form-submit | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `emitUrl` | |
| `onModalChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `urlObject` | |
| `hasInvalidInput` | |
| `invalidUrlError` | |
| `missingFileExtension` | |
| `fileExtension` | |
| `isValid` | |

### Examples

#### Basic Usage
```twig
<sw-media-url-form
    variant="..."
>
    <!-- content -->
</sw-media-url-form>
```

## sw-meteor-card

> A flexible and extensible content container (card) used in the Shopware Administration. Supports tabs, toolbars, action slots, grid content, and footers. Commonly used in extension and settings pages.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Data](#data)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `String` | `null` | no | Title displayed in the card header |
| hero | `Boolean` | `false` | no | Enables hero styling for the card |
| isLoading | `Boolean` | `false` | no | Shows a loader overlay on the card content |
| large | `Boolean` | `false` | no | Applies large card styling |
| defaultTab | `String` | `null` | no | Name of the tab to activate by default |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | `{ activeTab: String }` | Main content area, receives the currently active tab name |
| title | — | Custom title content, replaces the default title rendering |
| action | — | Header action area (e.g. buttons, links) displayed next to the title |
| toolbar | — | Toolbar area below the title and above tabs |
| tabs | `{ activeTab: String }` | Tab items area, should contain `sw-tabs-item` components |
| grid | `{ title: String }` | Grid content area, alternative to default slot for grid layouts |
| footer | — | Footer area below the content |

### Events / Emits

This component does not emit custom events.

### Methods

| Method | Parameters | Return | Description |
|--------|-----------|--------|-------------|
| setActiveTab | `(name: String)` | `void` | Sets the active tab by name |
| createdComponent | — | `void` | Lifecycle method called on created, sets the default tab |

### Data

| Name | Type | Default | Description |
|------|------|---------|-------------|
| activeTab | `String` | `null` | Tracks the currently active tab name |

### Computed Properties

| Name | Type | Description |
|------|------|-------------|
| hasTabs | `Boolean` | Whether the tabs slot is provided |
| hasToolbar | `Boolean` | Whether the toolbar slot is provided |
| hasContent | `Boolean` | Whether the default or grid slot is provided |
| hasDefaultSlot | `Boolean` | Whether the default slot is provided |
| hasHeader | `Boolean` | Whether any header element (toolbar, tabs, title, action) is present |
| isToolbarLastHeaderElement | `Boolean` | Whether the toolbar is the last header element (no tabs) |
| cardClasses | `Object` | Dynamic CSS classes for card styling |

### Examples

#### Example 1: Basic Usage with Tabs
Source: component definition (JSDoc example)
```html
<sw-meteor-card defaultTab="tab1">
    <template #tabs="{ activeTab }">
        <sw-tabs-item name="tab1" :activeTab="activeTab">Tab 1</sw-tabs-item>
        <sw-tabs-item name="tab2" :activeTab="activeTab">Tab 2</sw-tabs-item>
    </template>

    <template #default="{ activeTab }">
        <p v-if="activeTab === 'tab1'">Tab 1</p>
        <p v-if="activeTab === 'tab2'">Tab 2</p>
    </template>
</sw-meteor-card>
```

#### Example 2: Extension Card Base
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```html
<sw-meteor-card
    class="sw-extension-card-base"
    :class="extensionCardClasses"
>
    <sw-loader v-if="isLoading" />
    <div class="sw-extension-card-base__switch">
        <mt-switch
            v-model="isActive"
            :disabled="!allowActivation"
        />
    </div>
    <!-- card content -->
</sw-meteor-card>
```

#### Example 3: With Title and Action Slot
```html
<sw-meteor-card title="Account Settings">
    <template #action>
        <sw-button variant="primary" @click="save">Save</sw-button>
    </template>

    <div class="account-form">
        <!-- form content -->
    </div>
</sw-meteor-card>
```

#### Example 4: Hero Card with Loading State
```html
<sw-meteor-card
    :hero="true"
    :is-loading="isLoadingData"
    title="Dashboard Overview"
>
    <div class="dashboard-content">
        <!-- dashboard widgets -->
    </div>
</sw-meteor-card>
```

#### Example 5: Card with Footer
```html
<sw-meteor-card title="Product List">
    <div class="product-grid">
        <!-- product items -->
    </div>

    <template #footer>
        <sw-pagination :total="total" :page="page" @page-change="onPageChange" />
    </template>
</sw-meteor-card>
```

## sw-meteor-navigation

> A back-navigation component used within `sw-meteor-page`. Displays a "Back" link that navigates to the parent route. Automatically determines the parent route from the current route's meta data or from an explicit `fromLink` prop.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| fromLink | `RouteLocationNamedRaw \| null` | `null` | no | Explicit parent route to navigate back to. If not provided, falls back to `$route.meta.parentPath`. |

### Slots

This component does not provide slots.

### Events / Emits

This component does not emit custom events.

### Methods

This component does not define public methods.

### Computed Properties

| Name | Type | Description |
|------|------|-------------|
| hasParentRoute | `Boolean` | Whether a parent route is available (determines visibility) |
| parentRoute | `RouteLocationNamedRaw \| null` | Resolved parent route — uses `fromLink` if provided, otherwise derives from `$route.meta.parentPath` |

### Examples

#### Example 1: Default Usage (inside sw-meteor-page)
The component is primarily used internally by `sw-meteor-page`:
```html
<sw-meteor-navigation :from-link="fromLink" />
```

#### Example 2: With Explicit fromLink
```html
<sw-meteor-navigation
    :from-link="{ name: 'sw.extension.my-extensions.listing' }"
/>
```

#### Example 3: Automatic Parent Route
When no `fromLink` is provided, the component reads `$route.meta.parentPath` to determine the back link:
```html
<!-- In a route with meta: { parentPath: 'sw.settings.index' } -->
<sw-meteor-navigation />
<!-- Renders a back link to sw.settings.index -->
```

## sw-meteor-page

> A full-page layout component for the Shopware Administration. Provides a structured page with a search bar, notification center, smart bar (icon, title, actions, tabs), and main content area. Used as the top-level layout for extension and settings pages.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Data](#data)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| fullWidth | `Boolean` | `false` | no | Enables full-width content layout (wraps content in a scrollable container) |
| hideIcon | `Boolean` | `false` | no | Hides the module icon in the smart bar |
| fromLink | `RouteLocationNamedRaw \| null` | `null` | no | Explicit parent route for the back navigation link |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | Main content area of the page |
| search-bar | — | Custom search bar, replaces the default `sw-search-bar` |
| smart-bar-back | — | Custom back navigation, replaces the default `sw-meteor-navigation` |
| smart-bar-icon | — | Custom module icon in the smart bar |
| smart-bar-header | — | Custom page title/header text |
| smart-bar-header-meta | — | Meta information displayed below the header |
| smart-bar-description | — | Description text below the module info |
| smart-bar-actions | — | Action buttons in the smart bar (e.g. Save, Cancel) |
| smart-bar-context-buttons | — | Context/dropdown buttons in the smart bar |
| page-tabs | — | Tab items for page-level navigation |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-item-active | `tabItem: String` | Emitted when a new tab becomes active |

### Methods

| Method | Parameters | Return | Description |
|--------|-----------|--------|-------------|
| mountedComponent | — | `void` | Lifecycle method, calls `initPage` on mount |
| emitNewTab | `(tabItem: String)` | `void` | Emits the `new-item-active` event when a tab changes |
| initPage | — | `void` | Reads module info and parent route from `$route.meta` |

### Data

| Name | Type | Default | Description |
|------|------|---------|-------------|
| module | `ModuleManifest \| null` | `null` | Module manifest data (icon, title, color) from route meta |
| parentRoute | `String \| null` | `null` | Parent route path from route meta |

### Computed Properties

| Name | Type | Description |
|------|------|-------------|
| pageClasses | `Object` | Dynamic CSS classes (full-width modifier) |
| hasIcon | `Boolean` | Whether the module has an icon string |
| hasIconOrIconSlot | `Boolean` | Whether an icon exists or the smart-bar-icon slot is provided |
| hasTabs | `Boolean` | Whether the page-tabs slot is provided |
| pageColor | `String` | Module color from manifest, defaults to `#d8dde6` |

### Examples

#### Example 1: Extension Config Page
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```html
<sw-meteor-page
    class="sw-extension-config"
    :from-link="fromLink"
>
    <template #smart-bar-icon>
        <sw-extension-icon
            class="sw-extension-config__extension-icon"
            :src="image"
            :alt="extensionLabel"
        />
    </template>

    <template #smart-bar-header>
        {{ extensionLabel }}
    </template>

    <sw-extension-config-renderer
        :extension="extension"
        @save="onSave"
    />
</sw-meteor-page>
```

#### Example 2: My Extensions Index Page
Source: `sw-extension/page/sw-extension-my-extensions-index/sw-extension-my-extensions-index.html.twig`
```html
<sw-meteor-page>
    <template #smart-bar-header>
        {{ $tc('sw-extension.my-extensions.title') }}
    </template>

    <template #smart-bar-actions>
        <sw-button variant="primary" @click="onUploadExtension">
            {{ $tc('sw-extension.my-extensions.upload') }}
        </sw-button>
    </template>

    <template #page-tabs>
        <sw-tabs-item :route="{ name: 'sw.extension.my-extensions.listing' }">
            {{ $tc('sw-extension.my-extensions.listing.title') }}
        </sw-tabs-item>
        <sw-tabs-item :route="{ name: 'sw.extension.my-extensions.account' }">
            {{ $tc('sw-extension.my-extensions.account.title') }}
        </sw-tabs-item>
    </template>

    <router-view />
</sw-meteor-page>
```

#### Example 3: Simple Full-Width Page
```html
<sw-meteor-page :full-width="true" :hide-icon="true">
    <template #smart-bar-header>
        Custom Page Title
    </template>

    <template #smart-bar-actions>
        <sw-button variant="primary" @click="onSave">Save</sw-button>
    </template>

    <div class="page-content">
        <!-- full-width content -->
    </div>
</sw-meteor-page>
```

#### Example 4: Page with Custom Back Navigation
```html
<sw-meteor-page
    :from-link="{ name: 'sw.settings.index' }"
>
    <template #smart-bar-header>
        Settings Detail
    </template>

    <div class="settings-detail-content">
        <!-- settings form -->
    </div>
</sw-meteor-page>
```

## sw-meteor-single-select

> A compact single-select dropdown component with search functionality. Displays a label and selected value inline, opening a result list on click. Automatically enables search when there are 7 or more options.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Data](#data)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `Array` | — | yes | Array of option objects to select from |
| value | `any` | — | yes | The currently selected value |
| label | `String` | `''` | no | Label text displayed before the selected value |
| isLoading | `Boolean` | `false` | no | Shows a loading state in the result list |
| highlightSearchTerm | `Boolean` | `true` | no | Whether to highlight matching search terms in results |
| placeholder | `String` | `''` | no | Placeholder text when no value is selected |
| labelProperty | `String` | `'label'` | no | Property path to use as the display label in option objects |
| valueProperty | `String` | `'value'` | no | Property path to use as the value in option objects |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| before-item-list | — | Content before the result items (default: search field when searchable) |
| result-item | `{ item, index, labelProperty, searchTerm, highlightSearchTerm, isSelected, setValue, getKey }` | Custom rendering for each result item |
| result-label-property | `{ item, index, labelProperty, valueProperty, searchTerm, highlightSearchTerm, getKey }` | Custom rendering for the label within a result item |
| after-item-list | — | Content after the result items |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | `value: any` | Emitted when the selected value changes |
| search | `searchTerm: String` | Emitted when the search term changes |
| paginate | — | Emitted when pagination is triggered in the result list |

### Methods

| Method | Parameters | Return | Description |
|--------|-----------|--------|-------------|
| isSelected | `(item: Object)` | `Boolean` | Checks if the given item is currently selected |
| toggleResultList | — | `void` | Toggles the result dropdown open/closed |
| openResultList | — | `void` | Opens the result dropdown and resets results to all options |
| closeResultList | — | `void` | Closes the result dropdown and clears the search term |
| setValue | `(item: Object)` | `void` | Sets the selected value from the given item and closes the dropdown |
| onInputSearchTerm | — | `void` | Triggers a debounced search on input |
| search | — | `void` | Filters options by search term and emits the search event |
| getKey | `(object: Object, keyPath: String, defaultValue?: any)` | `any` | Gets a nested value from an object by key path |

### Data

| Name | Type | Default | Description |
|------|------|---------|-------------|
| searchTerm | `String` | `''` | Current search/filter term |
| isExpanded | `Boolean` | `false` | Whether the result dropdown is open |
| results | `Array` | `options` | Filtered result list (initially all options) |
| itemRecentlySelected | `Boolean` | `false` | Tracks if an item was just selected |

### Computed Properties

| Name | Type | Description |
|------|------|-------------|
| currentValue | `any` | Get/set wrapper for the value prop, emits `update:value` on set |
| inputClasses | `Object` | CSS classes based on expanded state |
| selectionTextClasses | `Object` | CSS classes for selection text (placeholder styling) |
| singleSelection | `Object \| undefined` | The currently selected option object |
| selectedValueLabel | `String` | Display label of the selected option, or placeholder if none |
| searchable | `Boolean` | Whether search is enabled (true when options >= 7) |

### Examples

#### Example 1: Basic Usage
```html
<sw-meteor-single-select
    label="Sort by"
    :options="sortOptions"
    :value="currentSort"
    @update:value="currentSort = $event"
/>
```

#### Example 2: With Custom Label and Value Properties
```html
<sw-meteor-single-select
    label="Language"
    :options="languages"
    :value="selectedLanguageId"
    label-property="name"
    value-property="id"
    placeholder="Select a language..."
    @update:value="onLanguageChange"
/>
```

#### Example 3: With Loading State
```html
<sw-meteor-single-select
    label="Category"
    :options="categories"
    :value="selectedCategory"
    :is-loading="isCategoriesLoading"
    @update:value="selectedCategory = $event"
    @paginate="loadMoreCategories"
/>
```

#### Example 4: Custom Result Item Rendering
```html
<sw-meteor-single-select
    label="Status"
    :options="statusOptions"
    :value="currentStatus"
    @update:value="currentStatus = $event"
>
    <template #result-item="{ item, isSelected, setValue }">
        <sw-select-result
            :selected="isSelected(item)"
            @item-select="setValue"
        >
            <sw-color-badge :color="item.color" />
            {{ item.label }}
        </sw-select-result>
    </template>
</sw-meteor-single-select>
```

#### Example 5: Disabled Search Highlighting
```html
<sw-meteor-single-select
    label="Filter"
    :options="filterOptions"
    :value="activeFilter"
    :highlight-search-term="false"
    @update:value="activeFilter = $event"
/>
```

## sw-modal

> Modal dialog overlay with title, subtitle, body content, and footer actions.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | `''` | no |  |
| subtitle | `any` | `null` | no |  |
| size | `any` | `''` | no |  |
| variant | `any` | `'default'` | no | Valid: `default`, `small`, `large`, `full` |
| isLoading | `any` | `false` | no |  |
| selector | `any` | `'body'` | no |  |
| showHeader | `any` | `true` | no |  |
| showFooter | `any` | `true` | no |  |
| closable | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| modal-header | — | |
| modal-title | — | |
| body | — | |
| modal-loader | — | |
| modal-footer | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `destroyedComponent` | |
| `setFocusToModal` | |
| `closeModalOnClickOutside` | |
| `closeModal` | |
| `closeModalOnEscapeKey` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalClasses` | |
| `modalDialogClasses` | |
| `modalBodyClasses` | |
| `hasFooterSlot` | |
| `showHelpSidebar` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-modal
    v-if="showDeleteModal === item.id"
    :title="$tc('global.default.warning')"
    variant="small"
    @modal-close="onCloseDeleteModal"
>
    {% block sw_settings_country_list_delete_modal_confirm_delete_text %}
    <p class="sw-settings-country-list__confirm-delete-text">
        {{ $tc('sw-settings-country.list.textDeleteConfirm', { name: item.name }, 0) }}
    </p>
    {% endblock %}

    {% block sw_settings_country_list_delete_modal_footer %}
    <template #modal-footer>
        {% block sw_settings_country_list_delete_modal_cancel %}
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
<sw-modal
    class="sw-settings-country-currency-dependent-modal"
    :title="$tc('sw-settings-country.detail.currencyDependentValues')"
    @modal-close="closeModal"
>

    {% block sw_settings_country_currency_dependent_modal_content %}
    <sw-data-grid
        class="sw-settings-country-currency-dependent-modal__grid"
        :data-source="currencyDependsValue"
        :is-loading="isLoading"
        :show-selection="false || undefined"
        :plain-appearance="true"
        :columns="countryCurrencyColumns"
    >
```

#### Example 3
Source: `sw-settings-country/component/sw-country-state-detail/sw-country-state-detail.html.twig`
```twig
<sw-modal
    class="sw-country-state-detail"
    :title="modalTitle"
    @modal-close="onCancel"
>
    {% block sw_country_state_detail_modal %}
    <sw-container
        columns="1fr 1fr"
        gap="20px"
    >
        <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks, vue/attributes-order -->
        {% block sw_country_state_detail_modal_technical_name %}

        <mt-text-field
            v-model="countryState.name"
```

#### Example 4
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-modal
    class="sw-settings-country-new-snippet-modal"
    :title="$tc('sw-settings-country.detail.newSnippetModalTitle')"
    @modal-close="onCloseModal"
>
    <sw-contextual-field
        class="sw-settings-country-new-snippet-modal__search-field"
        required
        :disabled="disabled"
        :error="null"
    >
        <template #sw-field-input="{ identification, disabled, error, size, setFocusClass, removeFocusClass }">
            <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
            <input
                ref="searchInput"
```

#### Example 5
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
<sw-modal
    :title="$tc('sw-settings-logging.entryInfo.title')"
    @modal-close="onClose"
>

    {% block sw_settings_logging_entry_info_tabs %}
    <sw-tabs position-identifier="sw-settings-logging-entry-info">

        {% block sw_settings_logging_entry_info_tab_items %}
        <sw-tabs-item
            :active="activeTab === 'raw'"
            @click="activeTab = 'raw'"
        >
            {{ $tc('sw-settings-logging.entryInfo.tabRaw') }}
        </sw-tabs-item>
```

## sw-modals-renderer

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `buttonProps` | |
| `sanitizeTextContent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modals` | |

### Examples

#### Basic Usage
```twig
<sw-modals-renderer>
    <!-- content -->
</sw-modals-renderer>
```

## sw-model-editor

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `mountedComponent` | |
| `initializeQuickView` | |
| `disposeQuickView` | |
| `onMediaLibraryItemUpdated` | |
| `setGizmoMode` | |
| `save` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
                    <sw-model-editor
                        ref="modelEditorRef"
                        :source="item"
                        @save="onSaveComplete"
                    />
                </div>
                <template #modal-footer>
                    <mt-button
                        variant="primary"
                        @click="$refs.modelEditorRef.save()"
                    >
                        {{ $tc('sw-media.sw-model-editor.saveChanges') }}
                    </mt-button>
                </template>
            </sw-modal>
```

## sw-model-viewer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `mountedComponent` | |
| `initializeQuickView` | |
| `disposeQuickView` | |
| `onMediaLibraryItemUpdated` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
    <sw-model-viewer
        :source="item"
    />
</div>

{% block sw_model_editor_modal %}
<sw-modal
    v-if="showModelEditorModal"
    class="sw-model-editor-modal"
    :title="$tc('sw-media.sw-model-editor.titleModal')"
    variant="full"
    @modal-close="closeModelEditorModal()"
>
    <div class="sw-model-editor-modal-wrapper">
        <sw-model-editor
```

## sw-multi-select-filter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-item | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-update | — | |
| filter-reset | — | |

### Methods

| Method | Description |
|--------|-------------|
| `changeValue` | |
| `resetFilter` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isEntityMultiSelect` | |
| `labelProperty` | |
| `values` | |

### Examples

#### Basic Usage
```twig
<sw-multi-select-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-multi-select-filter>
```

## sw-multi-select

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `any` | — | yes |  |
| value | `any` | — | yes |  |
| labelProperty | `any` | `'label'` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| placeholder | `any` | `''` | no |  |
| valueLimit | `any` | `5` | no |  |
| isLoading | `any` | `false` | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| searchFunction | `any` | — | no |  |
| label | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| item-add | — | |
| item-remove | — | |
| search-term-change | — | |
| display-values-expand | — | |
| paginate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `isSelected` | |
| `addItem` | |
| `remove` | |
| `removeLastItem` | |
| `expandValueLimit` | |
| `onSearchTermChange` | |
| `resetActiveItem` | |
| `onSelectExpanded` | |
| `onSelectCollapsed` | |
| `getKey` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `visibleValues` | |
| `totalValuesCount` | |
| `invisibleValueCount` | |
| `currentValue` | |
| `visibleResults` | |

### Examples

#### Example 1
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
        <sw-multi-select
            v-if="numberRange && (!numberRange.global || numberRange.global === false)"
            class="sw-number-range-detail__select-type"
            :label="$tc('sw-settings-number-range.detail.labelSalesChannel')"
            :disabled="!numberRange.typeId || !acl.can('number_ranges.editor')"
            :value="selectedNumberRangeSalesChannels"
            :options="salesChannels"
            name="sw-field--selectedNumberRangeSalesChannels"
            label-property="translated.name"
            value-property="id"
            @item-add="addSalesChannel"
            @item-remove="removeSalesChannel"
        />
        {% endblock %}
    </sw-container>
```

#### Example 2
Source: `sw-settings-basic-information/component/sw-settings-captcha-select-v2/sw-settings-captcha-select-v2.html.twig`
```twig
<sw-multi-select
    v-model:value="activeCaptchaSelect"
    v-bind="attributes"
    :options="availableCaptchas"
/>
{% endblock %}

{% block sw_settings_captcha_select_v2_google_recaptcha_v2 %}
<sw-container
    v-if="currentValue.googleReCaptchaV2.isActive"
    class="sw-settings-captcha-select-v2__google-recaptcha-v2"
>

    {% block sw_settings_captcha_select_v2_google_recaptcha_v2_description %}
    <p class="sw-settings-captcha-select-v2__description sw-settings-captcha-select-v2__google-recaptcha-v2-description">
```

#### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
            <sw-multi-select
                class="sw-cms-layout-assignment-modal__shop-page-select"
                :options="shopPages"
                :disabled="props.isInherited"
                :value="props.currentValue"
                :map-inheritance="props"
                @update:value="props.updateCurrentValue"
            />
        </template>
    </sw-inherit-wrapper>
    {% endblock %}
</template>
{% endblock %}

{% block sw_cms_layout_assignment_modal_product_detail_pages_select %}
```

#### Example 4
Source: `sw-promotion-v2/component/sw-promotion-v2-sales-channel-select/sw-promotion-v2-sales-channel-select.html.twig`
```twig
<sw-multi-select
    v-model:value="salesChannelIds"
    v-bind="$attrs"
    :options="salesChannels"
    value-property="id"
    label-property="name"
>

    {% block sw_promotion_v2_sales_channel_selection_label %}
    <template #selection-label-property="{ item }">
        {{ item.name || item.translated.name }}
    </template>
    {% endblock %}

    {% block sw_promotion_v2_sales_channel_selection_result_label %}
```

#### Example 5
Source: `sw-settings-document/page/sw-settings-document-detail/sw-settings-document-detail.html.twig`
```twig
<sw-multi-select
    v-if="documentConfig.salesChannels && (!documentConfig.global || documentConfig.global === false)"
    id="documentSalesChannel"
    v-model:value="documentConfigSalesChannels"
    @update:value="(v) => documentConfigSalesChannels = v"
    name="sw-field--documentConfigSalesChannels"
    v-tooltip="{
        showDelay: 300,
        message: $tc('sw-settings-document.detail.disabledSalesChannelSelect'),
        disabled: !!documentConfig.documentType
    }"
    label-property="name"
    value-property="id"
    :options="documentConfigSalesChannelOptionsCollection"
    :label="$tc('sw-settings-document.detail.labelSalesChannel')"
```

## sw-multi-snippet-drag-and-drop

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| totalLines | `any` | — | yes |  |
| linePosition | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| dragConfig | `any` | — | no |  |
| dropConfig | `any` | — | no |  |
| getLabelProperty | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selected-option | — | |
| label-property | — | |
| input | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onDragStart` | |
| `onDragEnter` | |
| `onDrop` | |
| `isSelectionDisabled` | |
| `onClickDismiss` | |
| `addNewLineAt` | |
| `moveToNewPosition` | |
| `onDelete` | |
| `openModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `errorObject` | |
| `mergedDragConfig` | |
| `mergedDropConfig` | |
| `isMaxLines` | |
| `isMinLines` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
    <sw-multi-snippet-drag-and-drop
        v-for="(snippet, index) in addressFormat"
        :key="index"
        v-droppable="{ data: { snippet, index }, dragGroup: 'sw-multi-snippet' }"
        v-draggable="{ ...dragConf, data: { snippet, index }}"
        :value="snippet"
        :line-position="index"
        :get-label-property="getLabelProperty"
        :total-lines="addressFormat.length"
        @update:value="change"
        @drop-end="onDropEnd"
        @position-move="moveToNewPosition"
        @add-new-line="addNewLineAt"
        @open-snippet-modal="openSnippetModal"
    />
```

## sw-multi-tag-ip-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| validate | `any` | — | no |  |
| knownIps | `any` | — | no |  |
| errorCode | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |

### Methods

| Method | Description |
|--------|-------------|
| `addSpecific` | |
| `getKnownIp` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `errorObject` | |
| `validKnownIps` | |
| `validUnselectedKnownIps` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
    <sw-multi-tag-ip-select
        v-model:value="maintenanceIpAllowlist"
        :is-loading="isLoading"
        :disabled="!acl.can('sales_channel.editor') || undefined"
        class="sw-order-user-card__tag-select"
        :label="$tc('sw-sales-channel.detail.ipAddressAllowlist')"
        :help-text="$tc('sw-sales-channel.detail.ipAddressAllowlistHelpText')"
        :known-ips="knownIps"
        :validate="validateMaintenanceIpCidr"
        error-code="SHOPWARE_INVALID_IP_CIDR"
    />
    {% endblock %}

    {% block sw_sales_channel_detail_base_settings_link %}
    <div class="sw-sales-channel-detail-base__settings-link">
```

## sw-multi-tag-select

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| valueLimit | `any` | `5` | no |  |
| placeholder | `any` | `''` | no |  |
| isLoading | `any` | `false` | no |  |
| validMessage | `any` | `''` | no |  |
| invalidMessage | `any` | `''` | no |  |
| validate | `any` | — | no |  |
| disabled | `any` | `false` | no |  |
| autocomplete | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| message-add-data | — | |
| message-enter-valid-data | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| add-item-is-valid | — | |
| update:value | — | |
| display-values-expand | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSelectionListKeyDownEnter` | |
| `addItem` | |
| `remove` | |
| `removeLastItem` | |
| `onSearchTermChange` | |
| `getKey` | |
| `setDropDown` | |
| `expandValueLimit` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `errorObject` | |
| `inputIsValid` | |
| `visibleValues` | |
| `totalValuesCount` | |
| `invisibleValueCount` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
<sw-multi-tag-select
    class="sw-product-category-form__search-keyword-field"
    :value="currentValue ? currentValue : []"
    :placeholder="$tc('sw-product.categoryForm.placeholderSearchKeywords')"
    :disabled="isInherited || !allowEdit"
    @update:value="updateCurrentValue"
>
    <template #message-add-data>
        <span>{{ $tc('sw-product.categoryForm.textAddSearchKeyword') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-product.categoryForm.textEnterValidSearchKeyword') }}</span>
    </template>
</sw-multi-tag-select>
```

#### Example 2
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
<sw-multi-tag-select
    v-model:value="delivery.trackingCodes"
    class="sw-order-user-card__tracking-code-select"
    :placeholder="$tc('sw-order.detailBase.placeholderTrackingCodeSelect')"
    @update:value="emitChange"
>
    <template #message-add-data>
        <span>{{ $tc('sw-order.detailBase.addTrackingCode') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-order.detailBase.enterValidTrackingCode') }}</span>
    </template>
</sw-multi-tag-select>
```

#### Example 3
Source: `sw-order/component/sw-order-create-options/sw-order-create-options.html.twig`
```twig
<sw-multi-tag-select
    class="sw-order-create-options__promotion-code"
    :value="promotionCodes"
    :label="$tc('sw-order.createBase.labelPromotions')"
    :validate="validatePromotions"
    @update:value="changePromotionCodes"
>
    <template #message-add-data>
        <span>{{ $tc('sw-order.initialModal.options.placeholderAddPromotion') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-order.createBase.placeholderAddPromotion') }}</span>
    </template>
</sw-multi-tag-select>
```

#### Example 4
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-multi-tag-select
    v-model:value="delivery.trackingCodes"
    class="sw-order-user-card__tracking-code-select"
    :disabled="!acl.can('order.editor') || undefined"
    :placeholder="$tc('sw-order.detailBase.placeholderTrackingCodeSelect')"
    :label="$tc('sw-order.detailBase.labelTrackingCodes')"
    :validate="validateTrackingCode"
    @update:value="saveAndReload"
>
    <template #message-add-data>
        <span>{{ $tc('sw-order.detailBase.addTrackingCode') }}</span>
    </template>
    <template #message-enter-valid-data>
        <span>{{ $tc('sw-order.detailBase.enterValidTrackingCode') }}</span>
    </template>
```
