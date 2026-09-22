# Administration (sw-*) components

> **`size="default"` on every `mt-button` you write.** The component defaults to
> `size="small"` — 32 pixels against the 40 of every core control beside it. Examples below
> that are quoted from Shopware's own source keep the core's spelling; **a plugin's own
> template sets the size explicitly.**
> → `shopware-admin` → `sw-meteor` → `COMPONENTS.md`

391 components, each with its props, slots, events and examples exactly as the generator extracted them. One file per component cost 1044 unreachable references; grouped, every component stays one direct link from SKILL.md.

## Contents

- [`sw-address`](#sw-address)
- [`sw-admin-menu-item`](#sw-admin-menu-item)
- [`sw-admin-menu`](#sw-admin-menu)
- [`sw-admin`](#sw-admin)
- [`sw-advanced-selection-product`](#sw-advanced-selection-product)
- [`sw-advanced-selection-rule`](#sw-advanced-selection-rule)
- [`sw-ai-copilot-badge`](#sw-ai-copilot-badge)
- [`sw-ai-copilot-warning`](#sw-ai-copilot-warning)
- [`sw-alert-deprecated`](#sw-alert-deprecated)
- [`sw-alert`](#sw-alert)
- [`sw-app-action-button`](#sw-app-action-button)
- [`sw-app-actions`](#sw-app-actions)
- [`sw-app-shop-id-change-modal`](#sw-app-shop-id-change-modal)
- [`sw-app-topbar-button`](#sw-app-topbar-button)
- [`sw-app-topbar-sidebar`](#sw-app-topbar-sidebar)
- [`sw-app-wrong-app-url-modal`](#sw-app-wrong-app-url-modal)
- [`sw-arrow-field`](#sw-arrow-field)
- [`sw-avatar`](#sw-avatar)
- [`sw-base-field`](#sw-base-field)
- [`sw-base-filter`](#sw-base-filter)
- [`sw-block-field`](#sw-block-field)
- [`sw-block-parent`](#sw-block-parent)
- [`sw-block`](#sw-block)
- [`sw-boolean-filter`](#sw-boolean-filter)
- [`sw-boolean-radio-group`](#sw-boolean-radio-group)
- [`sw-bulk-edit-change-type-field-renderer`](#sw-bulk-edit-change-type-field-renderer)
- [`sw-bulk-edit-change-type`](#sw-bulk-edit-change-type)
- [`sw-bulk-edit-custom-fields`](#sw-bulk-edit-custom-fields)
- [`sw-bulk-edit-customer`](#sw-bulk-edit-customer)
- [`sw-bulk-edit-form-field-renderer`](#sw-bulk-edit-form-field-renderer)
- [`sw-bulk-edit-modal`](#sw-bulk-edit-modal)
- [`sw-bulk-edit-order-documents-download-documents`](#sw-bulk-edit-order-documents-download-documents)
- [`sw-bulk-edit-order-documents-generate-cancellation-invoice`](#sw-bulk-edit-order-documents-generate-cancellation-invoice)
- [`sw-bulk-edit-order-documents-generate-credit-note`](#sw-bulk-edit-order-documents-generate-credit-note)
- [`sw-bulk-edit-order-documents-generate-delivery-note`](#sw-bulk-edit-order-documents-generate-delivery-note)
- [`sw-bulk-edit-order-documents-generate-invoice`](#sw-bulk-edit-order-documents-generate-invoice)
- [`sw-bulk-edit-order-documents`](#sw-bulk-edit-order-documents)
- [`sw-bulk-edit-order`](#sw-bulk-edit-order)
- [`sw-bulk-edit-product-description`](#sw-bulk-edit-product-description)
- [`sw-bulk-edit-product-media-form`](#sw-bulk-edit-product-media-form)
- [`sw-bulk-edit-product-media`](#sw-bulk-edit-product-media)
- [`sw-bulk-edit-product-visibility`](#sw-bulk-edit-product-visibility)
- [`sw-bulk-edit-product`](#sw-bulk-edit-product)
- [`sw-bulk-edit-save-modal-confirm`](#sw-bulk-edit-save-modal-confirm)
- [`sw-bulk-edit-save-modal-error`](#sw-bulk-edit-save-modal-error)
- [`sw-bulk-edit-save-modal-process`](#sw-bulk-edit-save-modal-process)
- [`sw-bulk-edit-save-modal-success`](#sw-bulk-edit-save-modal-success)
- [`sw-bulk-edit-save-modal`](#sw-bulk-edit-save-modal)
- [`sw-button-deprecated`](#sw-button-deprecated)
- [`sw-button-group`](#sw-button-group)
- [`sw-button-process`](#sw-button-process)
- [`sw-button`](#sw-button)
- [`sw-card-deprecated`](#sw-card-deprecated)
- [`sw-card-filter`](#sw-card-filter)
- [`sw-card-section`](#sw-card-section)
- [`sw-card-view`](#sw-card-view)
- [`sw-card`](#sw-card)
- [`sw-category-detail-base`](#sw-category-detail-base)
- [`sw-category-detail-cms`](#sw-category-detail-cms)
- [`sw-category-detail-custom-entity`](#sw-category-detail-custom-entity)
- [`sw-category-detail-menu`](#sw-category-detail-menu)
- [`sw-category-detail-products`](#sw-category-detail-products)
- [`sw-category-detail-seo`](#sw-category-detail-seo)
- [`sw-category-detail`](#sw-category-detail)
- [`sw-category-entry-point-card`](#sw-category-entry-point-card)
- [`sw-category-entry-point-modal`](#sw-category-entry-point-modal)
- [`sw-category-entry-point-overwrite-modal`](#sw-category-entry-point-overwrite-modal)
- [`sw-category-layout-card`](#sw-category-layout-card)
- [`sw-category-link-settings`](#sw-category-link-settings)
- [`sw-category-sales-channel-multi-select`](#sw-category-sales-channel-multi-select)
- [`sw-category-seo-form`](#sw-category-seo-form)
- [`sw-category-tree-field`](#sw-category-tree-field)
- [`sw-category-tree`](#sw-category-tree)
- [`sw-category-view`](#sw-category-view)
- [`sw-chart-card`](#sw-chart-card)
- [`sw-chart`](#sw-chart)
- [`sw-checkbox-field-deprecated`](#sw-checkbox-field-deprecated)
- [`sw-checkbox-field`](#sw-checkbox-field)
- [`sw-circle-icon`](#sw-circle-icon)
- [`sw-cms-block-app-preview-renderer`](#sw-cms-block-app-preview-renderer)
- [`sw-cms-block-app-renderer`](#sw-cms-block-app-renderer)
- [`sw-cms-block-category-navigation`](#sw-cms-block-category-navigation)
- [`sw-cms-block-center-text`](#sw-cms-block-center-text)
- [`sw-cms-block-config`](#sw-cms-block-config)
- [`sw-cms-block-cross-selling`](#sw-cms-block-cross-selling)
- [`sw-cms-block-form`](#sw-cms-block-form)
- [`sw-cms-block-gallery-buybox`](#sw-cms-block-gallery-buybox)
- [`sw-cms-block-html`](#sw-cms-block-html)
- [`sw-cms-block-image-bubble-row`](#sw-cms-block-image-bubble-row)
- [`sw-cms-block-image-cover`](#sw-cms-block-image-cover)
- [`sw-cms-block-image-four-column`](#sw-cms-block-image-four-column)
- [`sw-cms-block-image-gallery`](#sw-cms-block-image-gallery)
- [`sw-cms-block-image-highlight-row`](#sw-cms-block-image-highlight-row)
- [`sw-cms-block-image-simple-grid`](#sw-cms-block-image-simple-grid)
- [`sw-cms-block-image-slider`](#sw-cms-block-image-slider)
- [`sw-cms-block-image-text-bubble`](#sw-cms-block-image-text-bubble)
- [`sw-cms-block-image-text-cover`](#sw-cms-block-image-text-cover)
- [`sw-cms-block-image-text-gallery`](#sw-cms-block-image-text-gallery)
- [`sw-cms-block-image-text-row`](#sw-cms-block-image-text-row)
- [`sw-cms-block-image-text`](#sw-cms-block-image-text)
- [`sw-cms-block-image-three-column`](#sw-cms-block-image-three-column)
- [`sw-cms-block-image-three-cover`](#sw-cms-block-image-three-cover)
- [`sw-cms-block-image-two-column`](#sw-cms-block-image-two-column)
- [`sw-cms-block-image`](#sw-cms-block-image)
- [`sw-cms-block-layout-config`](#sw-cms-block-layout-config)
- [`sw-cms-block-product-description-reviews`](#sw-cms-block-product-description-reviews)
- [`sw-cms-block-product-heading`](#sw-cms-block-product-heading)
- [`sw-cms-block-product-listing`](#sw-cms-block-product-listing)
- [`sw-cms-block-product-slider`](#sw-cms-block-product-slider)
- [`sw-cms-block-product-three-column`](#sw-cms-block-product-three-column)
- [`sw-cms-block-sidebar-filter`](#sw-cms-block-sidebar-filter)
- [`sw-cms-block-text-hero`](#sw-cms-block-text-hero)
- [`sw-cms-block-text-on-image`](#sw-cms-block-text-on-image)
- [`sw-cms-block-text-teaser-section`](#sw-cms-block-text-teaser-section)
- [`sw-cms-block-text-teaser`](#sw-cms-block-text-teaser)
- [`sw-cms-block-text-three-column`](#sw-cms-block-text-three-column)
- [`sw-cms-block-text-two-column`](#sw-cms-block-text-two-column)
- [`sw-cms-block-text`](#sw-cms-block-text)
- [`sw-cms-block-video`](#sw-cms-block-video)
- [`sw-cms-block-vimeo-video`](#sw-cms-block-vimeo-video)
- [`sw-cms-block-youtube-video`](#sw-cms-block-youtube-video)
- [`sw-cms-block`](#sw-cms-block)
- [`sw-cms-create-wizard`](#sw-cms-create-wizard)
- [`sw-cms-create`](#sw-cms-create)
- [`sw-cms-detail`](#sw-cms-detail)
- [`sw-cms-el-buy-box`](#sw-cms-el-buy-box)
- [`sw-cms-el-category-navigation`](#sw-cms-el-category-navigation)
- [`sw-cms-el-config-buy-box`](#sw-cms-el-config-buy-box)
- [`sw-cms-el-config-category-navigation`](#sw-cms-el-config-category-navigation)
- [`sw-cms-el-config-cross-selling`](#sw-cms-el-config-cross-selling)
- [`sw-cms-el-config-form`](#sw-cms-el-config-form)
- [`sw-cms-el-config-html`](#sw-cms-el-config-html)
- [`sw-cms-el-config-image-gallery`](#sw-cms-el-config-image-gallery)
- [`sw-cms-el-config-image-slider`](#sw-cms-el-config-image-slider)
- [`sw-cms-el-config-image`](#sw-cms-el-config-image)
- [`sw-cms-el-config-location-renderer`](#sw-cms-el-config-location-renderer)
- [`sw-cms-el-config-manufacturer-logo`](#sw-cms-el-config-manufacturer-logo)
- [`sw-cms-el-config-product-box`](#sw-cms-el-config-product-box)
- [`sw-cms-el-config-product-description-reviews`](#sw-cms-el-config-product-description-reviews)
- [`sw-cms-el-config-product-listing-config-sorting-grid`](#sw-cms-el-config-product-listing-config-sorting-grid)
- [`sw-cms-el-config-product-listing`](#sw-cms-el-config-product-listing)
- [`sw-cms-el-config-product-name`](#sw-cms-el-config-product-name)
- [`sw-cms-el-config-product-slider`](#sw-cms-el-config-product-slider)
- [`sw-cms-el-config-sidebar-filter`](#sw-cms-el-config-sidebar-filter)
- [`sw-cms-el-config-text`](#sw-cms-el-config-text)
- [`sw-cms-el-config-video`](#sw-cms-el-config-video)
- [`sw-cms-el-config-vimeo-video`](#sw-cms-el-config-vimeo-video)
- [`sw-cms-el-config-youtube-video`](#sw-cms-el-config-youtube-video)
- [`sw-cms-el-cross-selling`](#sw-cms-el-cross-selling)
- [`sw-cms-el-form-template-contact`](#sw-cms-el-form-template-contact)
- [`sw-cms-el-form-template-newsletter`](#sw-cms-el-form-template-newsletter)
- [`sw-cms-el-form`](#sw-cms-el-form)
- [`sw-cms-el-html`](#sw-cms-el-html)
- [`sw-cms-el-image-gallery`](#sw-cms-el-image-gallery)
- [`sw-cms-el-image-slider`](#sw-cms-el-image-slider)
- [`sw-cms-el-image`](#sw-cms-el-image)
- [`sw-cms-el-location-renderer`](#sw-cms-el-location-renderer)
- [`sw-cms-el-manufacturer-logo`](#sw-cms-el-manufacturer-logo)
- [`sw-cms-el-preview-buy-box`](#sw-cms-el-preview-buy-box)
- [`sw-cms-el-preview-category-navigation`](#sw-cms-el-preview-category-navigation)
- [`sw-cms-el-preview-cross-selling`](#sw-cms-el-preview-cross-selling)
- [`sw-cms-el-preview-form`](#sw-cms-el-preview-form)
- [`sw-cms-el-preview-html`](#sw-cms-el-preview-html)
- [`sw-cms-el-preview-image-gallery`](#sw-cms-el-preview-image-gallery)
- [`sw-cms-el-preview-image-slider`](#sw-cms-el-preview-image-slider)
- [`sw-cms-el-preview-image`](#sw-cms-el-preview-image)
- [`sw-cms-el-preview-location-renderer`](#sw-cms-el-preview-location-renderer)
- [`sw-cms-el-preview-product-box`](#sw-cms-el-preview-product-box)
- [`sw-cms-el-preview-product-description-reviews`](#sw-cms-el-preview-product-description-reviews)
- [`sw-cms-el-preview-product-listing`](#sw-cms-el-preview-product-listing)
- [`sw-cms-el-preview-product-slider`](#sw-cms-el-preview-product-slider)
- [`sw-cms-el-preview-sidebar-filter`](#sw-cms-el-preview-sidebar-filter)
- [`sw-cms-el-preview-text`](#sw-cms-el-preview-text)
- [`sw-cms-el-preview-video`](#sw-cms-el-preview-video)
- [`sw-cms-el-preview-vimeo-video`](#sw-cms-el-preview-vimeo-video)
- [`sw-cms-el-preview-youtube-video`](#sw-cms-el-preview-youtube-video)
- [`sw-cms-el-product-box`](#sw-cms-el-product-box)
- [`sw-cms-el-product-description-reviews`](#sw-cms-el-product-description-reviews)
- [`sw-cms-el-product-listing`](#sw-cms-el-product-listing)
- [`sw-cms-el-product-name`](#sw-cms-el-product-name)
- [`sw-cms-el-product-slider`](#sw-cms-el-product-slider)
- [`sw-cms-el-sidebar-filter`](#sw-cms-el-sidebar-filter)
- [`sw-cms-el-text`](#sw-cms-el-text)
- [`sw-cms-el-video`](#sw-cms-el-video)
- [`sw-cms-el-vimeo-video`](#sw-cms-el-vimeo-video)
- [`sw-cms-el-youtube-video`](#sw-cms-el-youtube-video)
- [`sw-cms-form-sync`](#sw-cms-form-sync)
- [`sw-cms-inherit-wrapper`](#sw-cms-inherit-wrapper)
- [`sw-cms-layout-assignment-modal`](#sw-cms-layout-assignment-modal)
- [`sw-cms-layout-modal`](#sw-cms-layout-modal)
- [`sw-cms-list-item`](#sw-cms-list-item)
- [`sw-cms-list`](#sw-cms-list)
- [`sw-cms-mapping-field`](#sw-cms-mapping-field)
- [`sw-cms-missing-element-modal`](#sw-cms-missing-element-modal)
- [`sw-cms-page-form`](#sw-cms-page-form)
- [`sw-cms-page-select`](#sw-cms-page-select)
- [`sw-cms-preview-category-navigation`](#sw-cms-preview-category-navigation)
- [`sw-cms-preview-center-text`](#sw-cms-preview-center-text)
- [`sw-cms-preview-cross-selling`](#sw-cms-preview-cross-selling)
- [`sw-cms-preview-form`](#sw-cms-preview-form)
- [`sw-cms-preview-gallery-buybox`](#sw-cms-preview-gallery-buybox)
- [`sw-cms-preview-html`](#sw-cms-preview-html)
- [`sw-cms-preview-image-bubble-row`](#sw-cms-preview-image-bubble-row)
- [`sw-cms-preview-image-cover`](#sw-cms-preview-image-cover)
- [`sw-cms-preview-image-four-column`](#sw-cms-preview-image-four-column)
- [`sw-cms-preview-image-gallery`](#sw-cms-preview-image-gallery)
- [`sw-cms-preview-image-highlight-row`](#sw-cms-preview-image-highlight-row)
- [`sw-cms-preview-image-simple-grid`](#sw-cms-preview-image-simple-grid)
- [`sw-cms-preview-image-slider`](#sw-cms-preview-image-slider)
- [`sw-cms-preview-image-text-bubble`](#sw-cms-preview-image-text-bubble)
- [`sw-cms-preview-image-text-cover`](#sw-cms-preview-image-text-cover)
- [`sw-cms-preview-image-text-gallery`](#sw-cms-preview-image-text-gallery)
- [`sw-cms-preview-image-text-row`](#sw-cms-preview-image-text-row)
- [`sw-cms-preview-image-text`](#sw-cms-preview-image-text)
- [`sw-cms-preview-image-three-column`](#sw-cms-preview-image-three-column)
- [`sw-cms-preview-image-three-cover`](#sw-cms-preview-image-three-cover)
- [`sw-cms-preview-image-two-column`](#sw-cms-preview-image-two-column)
- [`sw-cms-preview-image`](#sw-cms-preview-image)
- [`sw-cms-preview-product-description-reviews`](#sw-cms-preview-product-description-reviews)
- [`sw-cms-preview-product-heading`](#sw-cms-preview-product-heading)
- [`sw-cms-preview-product-listing`](#sw-cms-preview-product-listing)
- [`sw-cms-preview-product-slider`](#sw-cms-preview-product-slider)
- [`sw-cms-preview-product-three-column`](#sw-cms-preview-product-three-column)
- [`sw-cms-preview-sidebar-filter`](#sw-cms-preview-sidebar-filter)
- [`sw-cms-preview-text-hero`](#sw-cms-preview-text-hero)
- [`sw-cms-preview-text-on-image`](#sw-cms-preview-text-on-image)
- [`sw-cms-preview-text-teaser-section`](#sw-cms-preview-text-teaser-section)
- [`sw-cms-preview-text-teaser`](#sw-cms-preview-text-teaser)
- [`sw-cms-preview-text-three-column`](#sw-cms-preview-text-three-column)
- [`sw-cms-preview-text-two-column`](#sw-cms-preview-text-two-column)
- [`sw-cms-preview-text`](#sw-cms-preview-text)
- [`sw-cms-preview-video`](#sw-cms-preview-video)
- [`sw-cms-preview-vimeo-video`](#sw-cms-preview-vimeo-video)
- [`sw-cms-preview-youtube-video`](#sw-cms-preview-youtube-video)
- [`sw-cms-product-assignment`](#sw-cms-product-assignment)
- [`sw-cms-product-box-preview`](#sw-cms-product-box-preview)
- [`sw-cms-reset-inheritance`](#sw-cms-reset-inheritance)
- [`sw-cms-section-actions`](#sw-cms-section-actions)
- [`sw-cms-section-config`](#sw-cms-section-config)
- [`sw-cms-section`](#sw-cms-section)
- [`sw-cms-sidebar-nav-element`](#sw-cms-sidebar-nav-element)
- [`sw-cms-sidebar`](#sw-cms-sidebar)
- [`sw-cms-slot`](#sw-cms-slot)
- [`sw-cms-stage-add-block`](#sw-cms-stage-add-block)
- [`sw-cms-stage-add-section`](#sw-cms-stage-add-section)
- [`sw-cms-stage-section-selection`](#sw-cms-stage-section-selection)
- [`sw-cms-toolbar`](#sw-cms-toolbar)
- [`sw-cms-visibility-config`](#sw-cms-visibility-config)
- [`sw-cms-visibility-toggle`](#sw-cms-visibility-toggle)
- [`sw-code-editor`](#sw-code-editor)
- [`sw-collapse`](#sw-collapse)
- [`sw-color-badge`](#sw-color-badge)
- [`sw-colorpicker-deprecated`](#sw-colorpicker-deprecated)
- [`sw-colorpicker`](#sw-colorpicker)
- [`sw-compact-colorpicker`](#sw-compact-colorpicker)
- [`sw-condition-all-line-items-container`](#sw-condition-all-line-items-container)
- [`sw-condition-and-container`](#sw-condition-and-container)
- [`sw-condition-base-line-item`](#sw-condition-base-line-item)
- [`sw-condition-base`](#sw-condition-base)
- [`sw-condition-billing-zip-code`](#sw-condition-billing-zip-code)
- [`sw-condition-customer-custom-field`](#sw-condition-customer-custom-field)
- [`sw-condition-date-range`](#sw-condition-date-range)
- [`sw-condition-generic-line-item`](#sw-condition-generic-line-item)
- [`sw-condition-generic`](#sw-condition-generic)
- [`sw-condition-goods-count`](#sw-condition-goods-count)
- [`sw-condition-goods-price`](#sw-condition-goods-price)
- [`sw-condition-is-always-valid`](#sw-condition-is-always-valid)
- [`sw-condition-is-net-select`](#sw-condition-is-net-select)
- [`sw-condition-line-item-custom-field`](#sw-condition-line-item-custom-field)
- [`sw-condition-line-item-goods-total`](#sw-condition-line-item-goods-total)
- [`sw-condition-line-item-in-category`](#sw-condition-line-item-in-category)
- [`sw-condition-line-item-property`](#sw-condition-line-item-property)
- [`sw-condition-line-item-purchase-price`](#sw-condition-line-item-purchase-price)
- [`sw-condition-line-item-with-quantity`](#sw-condition-line-item-with-quantity)
- [`sw-condition-line-item`](#sw-condition-line-item)
- [`sw-condition-modal`](#sw-condition-modal)
- [`sw-condition-not-found`](#sw-condition-not-found)
- [`sw-condition-operator-select`](#sw-condition-operator-select)
- [`sw-condition-or-container`](#sw-condition-or-container)
- [`sw-condition-order-custom-field`](#sw-condition-order-custom-field)
- [`sw-condition-script`](#sw-condition-script)
- [`sw-condition-shipping-zip-code`](#sw-condition-shipping-zip-code)
- [`sw-condition-time-range`](#sw-condition-time-range)
- [`sw-condition-tree-node`](#sw-condition-tree-node)
- [`sw-condition-tree`](#sw-condition-tree)
- [`sw-condition-type-select`](#sw-condition-type-select)
- [`sw-condition-unit-menu`](#sw-condition-unit-menu)
- [`sw-confirm-field`](#sw-confirm-field)
- [`sw-confirm-modal`](#sw-confirm-modal)
- [`sw-container`](#sw-container)
- [`sw-context-button`](#sw-context-button)
- [`sw-context-menu-divider`](#sw-context-menu-divider)
- [`sw-context-menu-item`](#sw-context-menu-item)
- [`sw-context-menu`](#sw-context-menu)
- [`sw-contextual-field`](#sw-contextual-field)
- [`sw-country-state-detail`](#sw-country-state-detail)
- [`sw-custom-entity-input-field`](#sw-custom-entity-input-field)
- [`sw-custom-field-detail`](#sw-custom-field-detail)
- [`sw-custom-field-list`](#sw-custom-field-list)
- [`sw-custom-field-set-detail-base`](#sw-custom-field-set-detail-base)
- [`sw-custom-field-set-renderer`](#sw-custom-field-set-renderer)
- [`sw-custom-field-translated-labels`](#sw-custom-field-translated-labels)
- [`sw-custom-field-type-base`](#sw-custom-field-type-base)
- [`sw-custom-field-type-checkbox`](#sw-custom-field-type-checkbox)
- [`sw-custom-field-type-colorpicker`](#sw-custom-field-type-colorpicker)
- [`sw-custom-field-type-date`](#sw-custom-field-type-date)
- [`sw-custom-field-type-entity`](#sw-custom-field-type-entity)
- [`sw-custom-field-type-number`](#sw-custom-field-type-number)
- [`sw-custom-field-type-select`](#sw-custom-field-type-select)
- [`sw-custom-field-type-text-editor`](#sw-custom-field-type-text-editor)
- [`sw-custom-field-type-text`](#sw-custom-field-type-text)
- [`sw-customer-address-form-options`](#sw-customer-address-form-options)
- [`sw-customer-address-form`](#sw-customer-address-form)
- [`sw-customer-base-form`](#sw-customer-base-form)
- [`sw-customer-base-info`](#sw-customer-base-info)
- [`sw-customer-card`](#sw-customer-card)
- [`sw-customer-create`](#sw-customer-create)
- [`sw-customer-default-addresses`](#sw-customer-default-addresses)
- [`sw-customer-detail-addresses`](#sw-customer-detail-addresses)
- [`sw-customer-detail-base`](#sw-customer-detail-base)
- [`sw-customer-detail-order`](#sw-customer-detail-order)
- [`sw-customer-detail`](#sw-customer-detail)
- [`sw-customer-imitate-customer-modal`](#sw-customer-imitate-customer-modal)
- [`sw-customer-list`](#sw-customer-list)
- [`sw-dashboard-index`](#sw-dashboard-index)
- [`sw-dashboard-statistics`](#sw-dashboard-statistics)
- [`sw-data-grid-column-boolean`](#sw-data-grid-column-boolean)
- [`sw-data-grid-column-position`](#sw-data-grid-column-position)
- [`sw-data-grid-inline-edit`](#sw-data-grid-inline-edit)
- [`sw-data-grid-settings`](#sw-data-grid-settings)
- [`sw-data-grid-skeleton`](#sw-data-grid-skeleton)
- [`sw-data-grid`](#sw-data-grid)
- [`sw-date-filter`](#sw-date-filter)
- [`sw-datepicker-deprecated`](#sw-datepicker-deprecated)
- [`sw-datepicker`](#sw-datepicker)
- [`sw-description-list`](#sw-description-list)
- [`sw-desktop`](#sw-desktop)
- [`sw-discard-changes-modal`](#sw-discard-changes-modal)
- [`sw-duplicated-media-v2`](#sw-duplicated-media-v2)
- [`sw-dynamic-url-field`](#sw-dynamic-url-field)
- [`sw-email-field-deprecated`](#sw-email-field-deprecated)
- [`sw-email-field`](#sw-email-field)
- [`sw-empty-state`](#sw-empty-state)
- [`sw-entity-advanced-selection-modal-grid`](#sw-entity-advanced-selection-modal-grid)
- [`sw-entity-advanced-selection-modal`](#sw-entity-advanced-selection-modal)
- [`sw-entity-listing`](#sw-entity-listing)
- [`sw-entity-many-to-many-select`](#sw-entity-many-to-many-select)
- [`sw-entity-multi-id-select`](#sw-entity-multi-id-select)
- [`sw-entity-multi-select`](#sw-entity-multi-select)
- [`sw-entity-single-select`](#sw-entity-single-select)
- [`sw-entity-tag-select`](#sw-entity-tag-select)
- [`sw-error-boundary`](#sw-error-boundary)
- [`sw-error-summary`](#sw-error-summary)
- [`sw-error`](#sw-error)
- [`sw-existence-filter`](#sw-existence-filter)
- [`sw-extension-adding-failed`](#sw-extension-adding-failed)
- [`sw-extension-adding-success`](#sw-extension-adding-success)
- [`sw-extension-app-module-error-page`](#sw-extension-app-module-error-page)
- [`sw-extension-app-module-page`](#sw-extension-app-module-page)
- [`sw-extension-card-base`](#sw-extension-card-base)
- [`sw-extension-card-bought`](#sw-extension-card-bought)
- [`sw-extension-component-section`](#sw-extension-component-section)
- [`sw-extension-config`](#sw-extension-config)
- [`sw-extension-deactivation-modal`](#sw-extension-deactivation-modal)
- [`sw-extension-domains-modal`](#sw-extension-domains-modal)
- [`sw-extension-file-upload`](#sw-extension-file-upload)
- [`sw-extension-icon`](#sw-extension-icon)
- [`sw-extension-my-extensions-account`](#sw-extension-my-extensions-account)
- [`sw-extension-my-extensions-index`](#sw-extension-my-extensions-index)
- [`sw-extension-my-extensions-listing-controls`](#sw-extension-my-extensions-listing-controls)
- [`sw-extension-my-extensions-listing`](#sw-extension-my-extensions-listing)
- [`sw-extension-my-extensions-recommendation`](#sw-extension-my-extensions-recommendation)
- [`sw-extension-permissions-details-modal`](#sw-extension-permissions-details-modal)
- [`sw-extension-permissions-modal`](#sw-extension-permissions-modal)
- [`sw-extension-privacy-policy-extensions-modal`](#sw-extension-privacy-policy-extensions-modal)
- [`sw-extension-rating-modal`](#sw-extension-rating-modal)
- [`sw-extension-rating-stars`](#sw-extension-rating-stars)
- [`sw-extension-ratings-card`](#sw-extension-ratings-card)
- [`sw-extension-ratings-summary`](#sw-extension-ratings-summary)
- [`sw-extension-removal-modal`](#sw-extension-removal-modal)
- [`sw-extension-review-creation-inputs`](#sw-extension-review-creation-inputs)
- [`sw-extension-review-creation`](#sw-extension-review-creation)
- [`sw-extension-review-reply`](#sw-extension-review-reply)
- [`sw-extension-review`](#sw-extension-review)
- [`sw-extension-sdk-module`](#sw-extension-sdk-module)
- [`sw-extension-select-rating`](#sw-extension-select-rating)
- [`sw-extension-store-landing-page`](#sw-extension-store-landing-page)
- [`sw-extension-teaser-popover`](#sw-extension-teaser-popover)
- [`sw-extension-teaser-sales-channel`](#sw-extension-teaser-sales-channel)
- [`sw-extension-uninstall-modal`](#sw-extension-uninstall-modal)
- [`sw-external-link`](#sw-external-link)

## sw-address

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| address | `any` | — | no |  |
| headline | `any` | `''` | no |  |
| formattingAddress | `any` | `null` | no |  |
| showEditButton | `any` | `false` | no |  |
| editLink | `any` | `null` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `addressClasses` | |
| `displayFormattingAddress` | |

### Examples

#### Example 1
Source: `sw-customer/component/sw-customer-default-addresses/sw-customer-default-addresses.html.twig`
```twig
        <sw-address
            :address="customer.defaultShippingAddress"
            :headline="$tc('sw-customer.detailBase.titleDefaultShippingAddress')"
            :show-edit-button="customerEditMode"
            :edit-link="defaultShippingAddressLink"
            :formatting-address="formattingShippingAddress"
        />
        {% endblock %}
    </sw-card-section>
    {% endblock %}

    {% block sw_customer_default_addresses_billing %}
    <sw-card-section v-if="customer.defaultBillingAddress.id">
        {% block sw_customer_default_addresses_billing_postal %}
        <sw-address
```

#### Example 2
Source: `sw-customer/view/sw-customer-detail-addresses/sw-customer-detail-addresses.html.twig`
```twig
    <sw-address
        class="sw-customer-detail-addresses__confirm-delete-address"
        :address="item"
    />
    {% endblock %}

    {% block sw_customer_detail_addresses_delete_modal_footer %}
    <template #modal-footer>
        {% block sw_customer_detail_addresses_delete_modal_cancel %}
        <mt-button
            size="small"
            variant="secondary"
            @click="onCloseDeleteAddressModal"
        >
            {{ $tc('global.default.cancel') }}
```

#### Example 3
Source: `sw-order/component/sw-order-delivery-metadata/sw-order-delivery-metadata.html.twig`
```twig
            <sw-address
                class="sw-order-delivery-metdata__address"
                :headline="$tc('sw-order.detailBase.headlineDeliveryAddress')"
                :address="delivery.shippingOrderAddress"
                :formatting-address="formattingAddress"
            />
            {% block sw_order_delivery_metadata_delivery_phone_number %}
            <dt>{{ $tc('sw-order.detailBase.labelCustomerPhoneNumber') }}</dt>
            <dd v-if="delivery.shippingOrderAddress.phoneNumber">
                {{ delivery.shippingOrderAddress.phoneNumber }}
            </dd>
            <dd v-else>
                {{ $tc('sw-order.detailBase.labelNoPhoneNumber') }}
            </dd>
            {% endblock %}
```

#### Example 4
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
        <sw-address
            :address="billingAddress"
            :formatting-address="formattingAddress"
        />
    </dd>
    {% endblock %}

    {% block sw_order_detail_base_order_overview_left_column_slot %}
    {% endblock %}

</sw-description-list>
{% endblock %}

{% block sw_order_detail_base_order_overview_right_column %}
<sw-description-list
```

#### Example 5
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
                <sw-address
                    :address="delivery.shippingOrderAddress"
                    :formatting-address="formattingAddress"
                />
            </dd>

            <dd v-else>
                {{ $tc('sw-order.detailBase.labelNoDeliveriesYet') }}
            </dd>
            {% endblock %}

            {% block sw_order_detail_base_order_overview_right_column_slot %}
            {% endblock %}

        </sw-description-list>
```

## sw-admin-menu-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entry | `any` | — | yes |  |
| parentEntries | `any` | — | no |  |
| displayIcon | `any` | `true` | no |  |
| iconSize | `any` | `'20px'` | no |  |
| collapsibleText | `any` | `true` | no |  |
| sidebarExpanded | `any` | `true` | no |  |
| borderColor | `any` | `'#333'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additional-text | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| menu-item-click | — | |
| menu-item-enter | — | |
| sub-menu-item-enter | — | |

### Methods

| Method | Description |
|--------|-------------|
| `hasAccessToRoute` | |
| `getIconName` | |
| `getItemName` | |
| `subIsActive` | |
| `getElementClasses` | |
| `onSubMenuItemEnter` | |
| `isFirstPluginInMenuEntries` | |
| `getCustomKey` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `getLinkToProp` | |
| `getEntryLabel` | |
| `showMenuItem` | |
| `entryPath` | |
| `children` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
<sw-admin-menu-item
    v-for="(entry, index) in buildMenuTree"
    :key="entry.id || index"
    class="sw-admin-menu__sales-channel-item"
    :entry="entry"
    icon-size="16px"
    :class="['sw-admin-menu__sales-channel-item--' + index]"
>
    <template #additional-text>
        {% block sw_sales_channel_menu_navigation_item_additional_text %}
        <button
            v-if="entry.domainLink && entry.active"
            class="sw-sales-channel-menu-domain-link"
            :title="$tc('sw-sales-channel.general.tooltipOpenStorefront')"
            @click.prevent="openStorefrontLink(entry.domainLink)"
```

#### Example 2
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
            <sw-admin-menu-item
                v-if="moreSalesChannelAvailable"
                :entry="moreItemsEntry"
                class="sw-admin-menu__sales-channel-more-items"
                icon-size="16px"
            />
            {% endblock %}
        </ul>
        {% endblock %}

        {% block sw_sales_channel_menu_context_button_collapsed %}
        <sw-context-button
            class="sw-sales-channel-menu__collapsed-context-menu"
            icon="regular-ellipsis-v"
            aria-label="sw-sales-channel.general.manageSalesChannels"
```

## sw-admin-menu

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mouseLocationsTracked | `any` | — | no |  |
| subMenuDelay | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountedComponent` | |
| `onToggleCanvas` | |
| `initNavigation` | |
| `refreshApps` | |
| `collapseAdminMenu` | |
| `expandAdminMenu` | |
| `mountedComponent` | |
| `getUser` | |
| `collapseMenuOnSmallViewports` | |
| `isActiveItem` | |
| `onToggleSidebar` | |
| `toggleSidebar` | |
| `onToggleUserActions` | |
| `openUserActions` | |
| `closeUserActions` | |
| `onLogoutUser` | |
| `addScrollbarOffset` | |
| `onMouseMoveDocument` | |
| `onMenuItemClick` | |
| `onMenuLeave` | |
| `onMenuItemEnter` | |
| `onSubMenuItemEnter` | |
| `getChildren` | |
| `isPositionInPolygon` | |
| `possiblyActivate` | |
| `activateMenuItem` | |
| `deactivatePreviousMenuItem` | |
| `getPolygonFromMenuItem` | |
| `getActivationDelay` | |
| `onFlyoutEnter` | |
| `onFlyoutLeave` | |
| `removeClassesFromElements` | |
| `isFirstPluginInMenuEntries` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentUser` | |
| `isExpanded` | |
| `userTitle` | |
| `currentLocale` | |
| `currentExpandedMenuEntries` | |
| `adminModuleNavigation` | |
| `appModuleNavigation` | |
| `navigationEntries` | |
| `mainMenuEntries` | |
| `sidebarCollapseIcon` | |
| `userActionsToggleIcon` | |
| `scrollbarOffsetStyle` | |
| `adminMenuClasses` | |
| `userName` | |
| `avatarUrl` | |
| `firstName` | |
| `lastName` | |
| `extensionMenuItems` | |
| `extensionModuleNavigation` | |
| `adminMenuStore` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
<sw-admin-menu-item
    v-for="(entry, index) in buildMenuTree"
    :key="entry.id || index"
    class="sw-admin-menu__sales-channel-item"
    :entry="entry"
    icon-size="16px"
    :class="['sw-admin-menu__sales-channel-item--' + index]"
>
    <template #additional-text>
        {% block sw_sales_channel_menu_navigation_item_additional_text %}
        <button
            v-if="entry.domainLink && entry.active"
            class="sw-sales-channel-menu-domain-link"
            :title="$tc('sw-sales-channel.general.tooltipOpenStorefront')"
            @click.prevent="openStorefrontLink(entry.domainLink)"
```

## sw-admin

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onUserActivity` | |
| `onRemoveToast` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isLoggedIn` | |
| `overrideComponents` | |
| `snackbar` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
<sw-admin-menu-item
    v-for="(entry, index) in buildMenuTree"
    :key="entry.id || index"
    class="sw-admin-menu__sales-channel-item"
    :entry="entry"
    icon-size="16px"
    :class="['sw-admin-menu__sales-channel-item--' + index]"
>
    <template #additional-text>
        {% block sw_sales_channel_menu_navigation_item_additional_text %}
        <button
            v-if="entry.domainLink && entry.active"
            class="sw-sales-channel-menu-domain-link"
            :title="$tc('sw-sales-channel.general.tooltipOpenStorefront')"
            @click.prevent="openStorefrontLink(entry.domainLink)"
```

## sw-advanced-selection-product

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-submit | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `productHasVariants` | |
| `getCurrencyPriceByCurrencyId` | |
| `getCategoryBreadcrumb` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currencyRepository` | |
| `productContext` | |
| `currenciesColumns` | |
| `productColumns` | |
| `productFilters` | |
| `productAssociations` | |
| `currencyFilter` | |
| `dateFilter` | |
| `stockColorVariantFilter` | |

### Examples

#### Basic Usage
```twig
<sw-advanced-selection-product>
    <!-- content -->
</sw-advanced-selection-product>
```

## sw-advanced-selection-rule

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleAwareGroupKey | `any` | — | yes |  |
| restrictedRuleIds | `any` | — | no |  |
| restrictedRuleIdsTooltipLabel | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-submit | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getColumnClass` | |
| `tooltipConfig` | |
| `isRestricted` | |
| `isRecordSelectable` | |
| `getCounts` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `getRuleDefinition` | |
| `assignmentProperties` | |
| `context` | |
| `columns` | |
| `filters` | |
| `conditionFilterOptions` | |
| `groupFilterOptions` | |
| `associationFilterOptions` | |
| `associations` | |
| `aggregations` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-advanced-selection-rule
    ruleAwareGroupKey="..."
>
    <!-- content -->
</sw-advanced-selection-rule>
```

## sw-ai-copilot-badge

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `any` | `true` | no |  |

### Examples

#### Example 1
Source: `sw-settings/component/sw-system-config/sw-system-config.html.twig`
```twig
<sw-ai-copilot-badge v-if="card.aiBadge" />
```

## sw-ai-copilot-warning

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | `''` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `warningText` | |

### Examples

#### Basic Usage
```twig
<sw-ai-copilot-warning>
    <!-- content -->
</sw-ai-copilot-warning>
```

## sw-alert-deprecated

> **Deprecated in 6.7** — Use `mt-banner` instead. Will be removed in 6.8.
> See mt-banner for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-alert>` | `<mt-banner>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'info'` | no | Valid: `info`, `warning`, `error`, `success`, `neutral` |
| appearance | `any` | `'default'` | no | Valid: `default`, `notification`, `system` |
| title | `any` | `''` | no |  |
| showIcon | `any` | `true` | no |  |
| closable | `any` | `false` | no |  |
| notificationIndex | `any` | `null` | no |  |
| icon | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| customIcon | — | |
| actions | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `alertIcon` | |
| `hasActionSlot` | |
| `alertClasses` | |
| `alertBodyClasses` | |

### Examples

#### Basic Usage
```twig
<sw-alert-deprecated>
    <!-- content -->
</sw-alert-deprecated>
```

## sw-alert

> **Migration wrapper** — Delegates to `mt-banner` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-banner for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| actions | — | |

### Examples

#### Basic Usage
```twig
<sw-alert>
    <!-- content -->
</sw-alert>
```

## sw-app-action-button

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| action | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| run-app-action | — | |

### Methods

| Method | Description |
|--------|-------------|
| `runAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `buttonLabel` | |

### Examples

#### Basic Usage
```twig
<sw-app-action-button
    action="..."
>
    <!-- content -->
</sw-app-action-button>
```

## sw-app-actions

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `runAction` | |
| `loadActions` | |
| `onCloseModal` | |
| `onOpenModalConfirm` | |
| `onCloseModalConfirm` | |
| `onConfirmClose` | |
| `onChangeCheckboxShow` | |
| `getUserConfig` | |
| `saveConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `entity` | |
| `view` | |
| `areActionsAvailable` | |
| `params` | |
| `userConfigRepository` | |
| `currentUser` | |
| `userConfigCriteria` | |
| `extensionSdkButtons` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-toolbar/sw-cms-toolbar.html.twig`
```twig
<sw-app-actions />
```

## sw-app-shop-id-change-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| shopIdCheck | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `fetchStrategies` | |
| `closeModal` | |
| `setSelectedStrategy` | |
| `isSelected` | |
| `getStrategyLabel` | |
| `getStrategyDescription` | |
| `getActiveStyle` | |
| `confirm` | |
| `getHumanReadableFingerprintName` | |
| `getFingerprintDescription` | |

### Examples

#### Basic Usage
```twig
<sw-app-shop-id-change-modal
    shopIdCheck="..."
>
    <!-- content -->
</sw-app-shop-id-change-modal>
```

## sw-app-topbar-button

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `runAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `topBarButtons` | |

### Examples

#### Basic Usage
```twig
<sw-app-topbar-button>
    <!-- content -->
</sw-app-topbar-button>
```

## sw-app-topbar-sidebar

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `setActiveSidebar` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sidebars` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-toolbar/sw-cms-toolbar.html.twig`
```twig
<sw-app-topbar-sidebar />
```

## sw-app-wrong-app-url-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `createAlertNotification` | |
| `removeAlertNotification` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isAppUrlReachable` | |
| `hasAppsThatRequireAppUrl` | |
| `display` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-app-wrong-app-url-modal>
    <!-- content -->
</sw-app-wrong-app-url-modal>
```

## sw-arrow-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| primary | `any` | `'#ffffff'` | no |  |
| secondary | `any` | `'#d1d9e0'` | no |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getArrow` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `arrowFill` | |

### Examples

#### Example 1
Source: `sw-product-stream/component/sw-product-stream-field-select/sw-product-stream-field-select.html.twig`
```twig
<sw-arrow-field
    v-if="options.length > 1"
    class="sw-product-stream-field-select"
    :class="{ 'has--error': hasError }"
    :primary="arrowPrimaryColor"
    secondary="#ffffff"
>
    <sw-single-select
        size="medium"
        :options="options"
        :value="field"
        :placeholder="$tc('sw-product-stream.filter.placeholderFieldSelect')"
        :disabled="disabled"
        show-clearable-button
        @update:value="changeField"
```

#### Example 2
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-arrow-field
    ref="product-stream-value-operator-select"
    class="sw-product-stream-value__operator-select"
    :disabled="!acl.can('product_stream.editor')"
>
    <sw-single-select
        v-model:value="filterType"
        name="sw-field--filterType"
        size="medium"
        :options="operators"
        :placeholder="$tc('sw-product-stream.filter.placeholderOperatorSelect')"
        :disabled="disabled"
        show-clearable-button
    />
</sw-arrow-field>
```

#### Example 3
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-arrow-field
    ref="product-stream-value-range-from-arrow-field"
    :disabled="disabled"
>
    <component
        :is="inputComponent"
        v-model:value="gte"
        size="medium"
        :disabled="disabled"
        :step="1"
    />
</sw-arrow-field>
```

## sw-avatar

> Avatar component displaying user initials, images, or placeholder icons.

- [Slots](#slots)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| color | `any` | `''` | no |  |
| size | `any` | `null` | no |  |
| firstName | `any` | `''` | no |  |
| lastName | `any` | `''` | no |  |
| imageUrl | `any` | `null` | no |  |
| placeholder | `any` | `false` | no |  |
| sourceContext | `any` | `null` | no |  |
| variant | `any` | `'circle'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `generateAvatarInitialsSize` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `avatarSize` | |
| `avatarInitials` | |
| `avatarInitialsSize` | |
| `avatarImage` | |
| `avatarColor` | |
| `hasAvatarImage` | |
| `showPlaceholder` | |
| `showInitials` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-account/sw-extension-my-extensions-account.html.twig`
```twig
        <sw-avatar
            size="36px"
            color="#E3F3FF"
            placeholder
        />

        <span class="sw-extension-my-extensions-account__wrapper-content-login-status-id">{{ userInfo.email }}</span>

        <mt-button
            class="sw-extension-my-extensions-account__logout-button"
            variant="primary"
            size="small"
            @click="logout"
        >
            {{ $tc('sw-extension.my-extensions.account.logout') }}
```

#### Example 2
Source: `sw-customer/page/sw-customer-list/sw-customer-list.html.twig`
```twig
    <sw-avatar
        :size="compact ? '32px' : '48px'"
        :source-context="item"
        :first-name="item.firstName"
        :last-name="item.lastName"
    />
</template>
{% endblock %}

{% block sw_customer_list_grid_columns_name %}
<template #column-firstName="{ item, compact, isInlineEdit }">

    {% block sw_customer_list_grid_inline_edit_name %}
    <template v-if="isInlineEdit">
        {% block sw_customer_list_grid_inline_edit_first_name %}
```

#### Example 3
Source: `sw-customer/component/sw-customer-card/sw-customer-card.html.twig`
```twig
<sw-avatar
    size="80px"
    :source-context="customer"
    :first-name="customer.firstName"
    :last-name="customer.lastName"
/>
{% endblock %}

{% block sw_customer_card_metadata %}
<div class="sw-customer-card__metadata">
    {% block sw_customer_card_metadata_customer_name %}
    {% block sw_custsomer_card_metadata_customer_name_label %}
    <template v-if="!editMode">
        <div
            v-if="customer"
```

#### Example 4
Source: `sw-users-permissions/components/sw-users-permissions-user-listing/sw-users-permissions-user-listing.html.twig`
```twig
    <sw-avatar
        v-if="!isSso"
        :size="compact ? '32px' : '48px'"
        :first-name="item.firstName"
        :last-name="item.lastName"
        variant="square"
        :source-context="item"
    />
</template>
{% endblock %}

{% block sw_settings_user_list_column_username %}
<template #column-username="{ item }">
    {% block sw_settings_user_list_column_username_content %}
    <router-link
```

#### Example 5
Source: `sw-order/component/sw-order-create-details-header/sw-order-create-details-header.html.twig`
```twig
<sw-avatar
    v-if="customer"
    size="80px"
    :color="$route.meta.$module.color"
    :first-name="customer.firstName"
    :last-name="customer.lastName"
/>
<sw-avatar
    v-else
    size="80px"
    color="#f9fafb"
/>
{% endblock %}

{% block sw_order_create_details_header_profile_searching %}
```

## sw-base-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | `null` | no |  |
| label | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| hint | `any` | `null` | no |  |
| isInvalid | `any` | `false` | no |  |
| aiBadge | `any` | `false` | no |  |
| error | `null` | — | no |  |
| disabled | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| isInherited | `any` | `false` | no |  |
| isInheritanceField | `any` | `false` | no |  |
| disableInheritanceToggle | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| sw-field-input | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| base-field-mounted | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identification` | |
| `hasLabel` | |
| `hasError` | |
| `hasHint` | |
| `swFieldClasses` | |
| `swFieldLabelClasses` | |
| `showLabel` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-select-rating/sw-extension-select-rating.html.twig`
```twig
<sw-base-field
    class="sw-field--rating-select"
    v-bind="$attrs"
>
    {% block sw_select_rating_input %}
    <template #sw-field-input>
        {% block sw_select_rating_input_stars %}
        <sw-extension-rating-stars
            v-model:rating="currentValue"
            editable
            @update:rating="onChange"
        />
        {% endblock %}
    </template>
    {% endblock %}
```

## sw-base-filter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| showResetButton | `any` | — | yes |  |
| active | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-reset | — | |

### Methods

| Method | Description |
|--------|-------------|
| `resetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-base-filter
    title="..."
    showResetButton="..."
    active="..."
>
    <!-- content -->
</sw-base-filter>
```

## sw-block-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | `any` | `'default'` | no | Valid: `small`, `medium`, `default` |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-field-input | — | |
| hint | — | |
| label | — | |

### Methods

| Method | Description |
|--------|-------------|
| `setFocusClass` | |
| `removeFocusClass` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `swBlockSize` | |
| `swBlockFieldClasses` | |

### Examples

#### Example 1
Source: `sw-cms/elements/buy-box/component/sw-cms-el-buy-box.html.twig`
```twig
<sw-block-field class="sw-cms-el-buy-box__quantity">
    <template #sw-field-input>
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <select>
            <option
                :value="product.minPurchase"
                selected
            >
                {{ product.minPurchase }}
            </option>
        </select>
        <div class="sw-cms-el-buy-box__icon">
            <mt-icon
                name="regular-chevron-up-xxs"
                decorative
```

#### Example 2
Source: `sw-cms/elements/buy-box/component/sw-cms-el-buy-box.html.twig`
```twig
<sw-block-field class="sw-cms-el-buy-box__quantity">
    <template #sw-field-input>
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <select>
            <option
                value="1"
                selected
            >
                1
            </option>
        </select>
        <div class="sw-cms-el-buy-box__icon">
            <mt-icon
                name="regular-chevron-up-xxs"
                size="16px"
```

#### Example 3
Source: `sw-order/component/sw-order-promotion-tag-field/sw-order-promotion-tag-field.html.twig`
```twig
<sw-block-field
    class="sw-tagged-field sw-order-promotion-tag-field"
    :class="taggedFieldClasses"
    v-bind="$attrs"
    :disabled="disabled"
>
    <template #sw-field-input="{ identification, error, disabled, size, setFocusClass, removeFocusClass }">

        {% block sw_tagged_field_inner %}
        <ul
            class="sw-tagged-field__tag-list"
            :class="taggedFieldListClasses"
            role="listbox"
            tabindex="0"
            @click="setFocus(true)"
```

## sw-block-parent

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-block-parent>
    <!-- content -->
</sw-block-parent>
```

## sw-block

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| name | `any` | — | no |  |
| extends | `any` | — | no |  |
| data | `any` | `null` | no |  |

### Examples

#### Example 1
Source: `sw-cms/elements/buy-box/component/sw-cms-el-buy-box.html.twig`
```twig
<sw-block-field class="sw-cms-el-buy-box__quantity">
    <template #sw-field-input>
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <select>
            <option
                :value="product.minPurchase"
                selected
            >
                {{ product.minPurchase }}
            </option>
        </select>
        <div class="sw-cms-el-buy-box__icon">
            <mt-icon
                name="regular-chevron-up-xxs"
                decorative
```

#### Example 2
Source: `sw-cms/elements/buy-box/component/sw-cms-el-buy-box.html.twig`
```twig
<sw-block-field class="sw-cms-el-buy-box__quantity">
    <template #sw-field-input>
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <select>
            <option
                value="1"
                selected
            >
                1
            </option>
        </select>
        <div class="sw-cms-el-buy-box__icon">
            <mt-icon
                name="regular-chevron-up-xxs"
                size="16px"
```

#### Example 3
Source: `sw-order/component/sw-order-promotion-tag-field/sw-order-promotion-tag-field.html.twig`
```twig
<sw-block-field
    class="sw-tagged-field sw-order-promotion-tag-field"
    :class="taggedFieldClasses"
    v-bind="$attrs"
    :disabled="disabled"
>
    <template #sw-field-input="{ identification, error, disabled, size, setFocusClass, removeFocusClass }">

        {% block sw_tagged_field_inner %}
        <ul
            class="sw-tagged-field__tag-list"
            :class="taggedFieldListClasses"
            role="listbox"
            tabindex="0"
            @click="setFocus(true)"
```

## sw-boolean-filter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |

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
| `value` | |
| `options` | |

### Examples

#### Basic Usage
```twig
<sw-boolean-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-boolean-filter>
```

## sw-boolean-radio-group

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `true` | no |  |
| labelOptionTrue | `any` | — | yes |  |
| labelOptionFalse | `any` | — | yes |  |
| bordered | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `options` | |
| `castedValue` | |

### Examples

#### Example 1
Source: `sw-settings-customer-group/page/sw-settings-customer-group-detail/sw-settings-customer-group-detail.html.twig`
```twig
            <sw-boolean-radio-group
                v-model:value="customerGroup.displayGross"
                bordered
                :label="$tc('sw-settings-customer-group.detail.fieldDisplayGrossLabel')"
                :label-option-true="$tc('sw-settings-customer-group.detail.fieldDisplayGrossValues', {}, 1)"
                :label-option-false="$tc('sw-settings-customer-group.detail.fieldDisplayGrossValues', {}, 0)"
                :disabled="!acl.can('customer_groups.editor') || undefined"
            />
            {% endblock %}

            <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks,vue/attributes-order -->
            {% block sw_settings_customer_group_detail_content_card_registration_form %}

            <mt-switch
                v-model="customerGroup.registrationActive"
```

## sw-bulk-edit-change-type-field-renderer

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| bulkEditData | `any` | — | yes |  |
| formFields | `any` | — | yes |  |
| entity | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| valueFieldWithBoxType | — | |
| valueField | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-value | — | |
| update:default-unit | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `hasFormFieldConfig` | |
| `getConfigValue` | |
| `showSelectBoxType` | |
| `onChangeValue` | |
| `onChangeToggle` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
    <sw-bulk-edit-change-type-field-renderer
        :form-fields="generalFormFields"
        :bulk-edit-data="bulkEditProduct"
        :entity="product"
        @inheritance-restore="onInheritanceRestore"
        @inheritance-remove="onInheritanceRemove"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_bulk_edit_product_content_prices_card %}
<mt-card
    class="sw-bulk-edit-product-base__prices"
    position-identifier="sw-bulk-edit-product-prices"
```

#### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-bulk-edit-change-type-field-renderer
    :form-fields="advancedPricesFormFields"
    :bulk-edit-data="bulkEditProduct"
    :entity="product"
>
    <template #valueFieldWithBoxType="{ formField, entity, index }">
        <sw-inheritance-switch
            v-if="isChild"
            :is-inherited="bulkEditProduct[formField.name].isInherited"
            @inheritance-restore="onInheritanceRestore(formField)"
            @inheritance-remove="onInheritanceRemove(formField)"
        />

        <a
            v-if="['add', 'overwrite'].includes(bulkEditProduct[formField.name].type)"
```

#### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
    <sw-bulk-edit-change-type-field-renderer
        :form-fields="statusFormFields"
        :bulk-edit-data="bulkEditData"
        :entity="order"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_bulk_edit_order_content_documents %}
<mt-card
    class="sw-bulk-edit-order-base__documents"
    position-identifier="sw-bulk-edit-order-documents"
    :title="$tc('sw-bulk-edit.order.documents.cardTitle')"
    :is-loading="isLoading"
```

#### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
        <sw-bulk-edit-change-type-field-renderer
            :form-fields="tagsFormFields"
            :bulk-edit-data="bulkEditData"
            :entity="order"
        />
        {% endblock %}
    </mt-card>
    {% endblock %}

    {% block sw_bulk_edit_order_custom_field_card %}
    <mt-card
        class="sw-bulk-edit-order-base__custom_fields"
        position-identifier="sw-bulk-edit-order-custom-fields"
        :title="$tc('sw-bulk-edit.order.customFields.cardTitle')"
        :is-loading="isLoading"
```

#### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-customer/sw-bulk-edit-customer.html.twig`
```twig
        <sw-bulk-edit-change-type-field-renderer
            :form-fields="accountFormFields"
            :bulk-edit-data="bulkEditData"
            :entity="customer"
        />
        {% endblock %}
    </template>
</mt-card>
{% endblock %}

{% block sw_bulk_edit_customer_tags_card %}
<mt-card
    class="sw-bulk-edit-customer-base__tags"
    position-identifier="sw-bulk-edit-customer-tags"
    :title="$tc('sw-bulk-edit.customer.tags.cardTitle')"
```

## sw-bulk-edit-change-type

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
| allowOverwrite | `any` | `false` | no |  |
| allowClear | `any` | `false` | no |  |
| allowAdd | `any` | `false` | no |  |
| allowRemove | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| value-field | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `options` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
    <sw-bulk-edit-change-type-field-renderer
        :form-fields="generalFormFields"
        :bulk-edit-data="bulkEditProduct"
        :entity="product"
        @inheritance-restore="onInheritanceRestore"
        @inheritance-remove="onInheritanceRemove"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_bulk_edit_product_content_prices_card %}
<mt-card
    class="sw-bulk-edit-product-base__prices"
    position-identifier="sw-bulk-edit-product-prices"
```

#### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-bulk-edit-change-type-field-renderer
    :form-fields="advancedPricesFormFields"
    :bulk-edit-data="bulkEditProduct"
    :entity="product"
>
    <template #valueFieldWithBoxType="{ formField, entity, index }">
        <sw-inheritance-switch
            v-if="isChild"
            :is-inherited="bulkEditProduct[formField.name].isInherited"
            @inheritance-restore="onInheritanceRestore(formField)"
            @inheritance-remove="onInheritanceRemove(formField)"
        />

        <a
            v-if="['add', 'overwrite'].includes(bulkEditProduct[formField.name].type)"
```

#### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
    <sw-bulk-edit-change-type-field-renderer
        :form-fields="statusFormFields"
        :bulk-edit-data="bulkEditData"
        :entity="order"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_bulk_edit_order_content_documents %}
<mt-card
    class="sw-bulk-edit-order-base__documents"
    position-identifier="sw-bulk-edit-order-documents"
    :title="$tc('sw-bulk-edit.order.documents.cardTitle')"
    :is-loading="isLoading"
```

#### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
        <sw-bulk-edit-change-type-field-renderer
            :form-fields="tagsFormFields"
            :bulk-edit-data="bulkEditData"
            :entity="order"
        />
        {% endblock %}
    </mt-card>
    {% endblock %}

    {% block sw_bulk_edit_order_custom_field_card %}
    <mt-card
        class="sw-bulk-edit-order-base__custom_fields"
        position-identifier="sw-bulk-edit-order-custom-fields"
        :title="$tc('sw-bulk-edit.order.customFields.cardTitle')"
        :is-loading="isLoading"
```

#### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-customer/sw-bulk-edit-customer.html.twig`
```twig
        <sw-bulk-edit-change-type-field-renderer
            :form-fields="accountFormFields"
            :bulk-edit-data="bulkEditData"
            :entity="customer"
        />
        {% endblock %}
    </template>
</mt-card>
{% endblock %}

{% block sw_bulk_edit_customer_tags_card %}
<mt-card
    class="sw-bulk-edit-customer-base__tags"
    position-identifier="sw-bulk-edit-customer-tags"
    :title="$tc('sw-bulk-edit.customer.tags.cardTitle')"
```

## sw-bulk-edit-custom-fields

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entity | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `initializeCustomFields` | |
| `toggleItemCheck` | |
| `updateCustomField` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <sw-bulk-edit-custom-fields
            class="sw-bulk-edit__custom-fields"
            :sets="customFieldSets"
            :entity="product"
            :parent-entity="parentProduct"
            @change="onCustomFieldsChange"
        />
    </mt-card>
    {% endblock %}
</sw-card-view>
<mt-empty-state
    v-if="!isLoading && selectedIds.length == 0"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-bulk-edit.product.messageEmptyTitle')"
    :description="$tc('sw-bulk-edit.product.messageEmptySubline')"
```

#### Example 2
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
        <sw-bulk-edit-custom-fields
            class="sw-bulk-edit__custom-fields"
            :sets="customFieldSets"
            @change.self="onCustomFieldsChange"
        />
    </mt-card>
    {% endblock %}
</sw-card-view>

{% block sw_bulk_edit_order_empty_state %}
<mt-empty-state
    v-if="selectedIds.length <= 0 && !isLoading"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-bulk-edit.order.messageEmptyTitle')"
    :description="$tc('sw-bulk-edit.order.messageEmptySubline')"
```

#### Example 3
Source: `sw-bulk-edit/page/sw-bulk-edit-customer/sw-bulk-edit-customer.html.twig`
```twig
            <sw-bulk-edit-custom-fields
                class="sw-bulk-edit__custom-fields"
                :sets="customFieldSets"
                @change="onCustomFieldsChange"
            />
        </template>
    </mt-card>
    {% endblock %}
</sw-card-view>

{% block sw_bulk_edit_customer_empty_state %}
<mt-empty-state
    v-if="selectedIds.length <= 0 && !isLoading"
    icon="solid-users"
    :headline="$tc('sw-bulk-edit.customer.messageEmptyTitle')"
```

## sw-bulk-edit-customer

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setRouteMetaModule` | |
| `defineBulkEditData` | |
| `loadBulkEditData` | |
| `loadCustomFieldSets` | |
| `onCustomFieldsChange` | |
| `onProcessData` | |
| `openModal` | |
| `onSave` | |
| `closeModal` | |
| `onChangeLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectedIds` | |
| `customFieldSetRepository` | |
| `customerRepository` | |
| `customFieldSetCriteria` | |
| `hasChanges` | |
| `actionsRequestGroup` | |
| `accountFormFields` | |
| `tagsFormFields` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-customer>
    <!-- content -->
</sw-bulk-edit-customer>
```

## sw-bulk-edit-form-field-renderer

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:default-unit | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onUpdateDefaultUnit` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
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
                    v-if="isDisplayingValue"
                    v-bind="formField"
                    :key="`formField-${index}`"
                    v-model="entity[formField.name]"
                    v-model:value="entity[formField.name]"
```

#### Example 2
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type-field-renderer/sw-bulk-edit-change-type-field-renderer.html.twig`
```twig
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
                            v-bind="formField"
                            :key="`formField-${index}`"
                            v-model:value="entity[formField.name]"
                            @update:value="onChangeValue($event, formField.name)"
                            @update:default-unit="$emit('update:default-unit', $event)"
```

## sw-bulk-edit-modal

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selection | `any` | — | no |  |
| steps | `any` | — | no |  |
| bulkGridEditColumns | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| slot | — | |
| sw-bulk-edit-modal-cancel | — | |
| sw-bulk-edit-modal-confirm | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| edit-items | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `paginate` | |
| `updateBulkEditSelection` | |
| `editItems` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `itemCount` | |
| `paginateRecords` | |
| `getSlots` | |

### Examples

#### Example 1
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    class="sw-product-bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="productBulkEditColumns"
    @edit-items="onBulkEditItems"
    @modal-close="showBulkEditModal = false"
>
    {% block sw_product_list_bulk_edit_grid_columns_name %}
    <template #column-name="{ item }">
        <router-link
            :to="{ name: 'sw.product.detail', params: { id: item.id } }"
            target="_blank"
            rel="noreferrer noopener"
        >
```

#### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    class="sw-product-variant-modal__bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="gridColumns"
    @edit-items="onEditItems"
    @modal-close="toggleBulkEditModal"
>
    {% block sw_product_variant_modal_bulk_edit_modal_column_name %}
    <template #column-name="{ item }">
        <sw-media-preview-v2 :source="getItemMedia(item)" />
        <router-link :to="{ name: 'sw.product.detail', params: { id: item.id } }">
            <span
                v-if="item.translated.name"
                class="sw-product-variant-modal__variant-name"
```

#### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    class="sw-product-variants-overview__bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="variantColumns"
    @edit-items="onEditItems"
    @modal-close="toggleBulkEditModal"
>
    {% block sw_product_variants_overview_bulk_edit_modal_column_name %}
    <template #column-name="{ item }">
        <template v-if="item.options">
            <router-link
                class="sw-product-variants-overview__variation-link"
                :to="{ name: 'sw.product.detail.base', params: { id: item.id } }"
                @click="onOptionEdit(item)"
```

#### Example 4
Source: `sw-customer/page/sw-customer-list/sw-customer-list.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    ref="bulkEditModal"
    class="sw-customer-bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="customerColumns"
    @edit-items="onBulkEditItems"
    @modal-close="onBulkEditModalClose"
>
    {% block sw_customer_list_bulk_edit_grid_columns_name %}
    <template #column-firstName="{ item }">
        <router-link
            :to="{ name: 'sw.customer.detail', params: { id: item.id } }"
            target="_blank"
            rel="noreferrer noopener"
```

#### Example 5
Source: `sw-order/page/sw-order-list/sw-order-list.html.twig`
```twig
<sw-bulk-edit-modal
    v-if="showBulkEditModal"
    ref="bulkEditModal"
    class="sw-order-bulk-edit-modal"
    :selection="selection"
    :bulk-grid-edit-columns="orderColumns"
    @edit-items="onBulkEditItems"
    @modal-close="showBulkEditModal = false"
>
    {% block sw_order_list_bulk_edit_grid_columns_order_number %}
    <template #column-orderNumber="{ item }">
        {% block sw_order_list_bulk_edit_grid_order_number_link %}
        <router-link
            :to="{ name: 'sw.order.detail', params: { id: item.id } }"
            target="_blank"
```

## sw-bulk-edit-order-documents-download-documents

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getDocumentTypes` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `documentTypeRepository` | |
| `documentTypeCriteria` | |
| `documentTypes` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-order-documents-download-documents>
    <!-- content -->
</sw-bulk-edit-order-documents-download-documents>
```

## sw-bulk-edit-order-documents-generate-cancellation-invoice

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `generateData` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-order-documents-generate-cancellation-invoice>
    <!-- content -->
</sw-bulk-edit-order-documents-generate-cancellation-invoice>
```

## sw-bulk-edit-order-documents-generate-credit-note

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `generateData` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-order-documents-generate-credit-note>
    <!-- content -->
</sw-bulk-edit-order-documents-generate-credit-note>
```

## sw-bulk-edit-order-documents-generate-delivery-note

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `generateData` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-order-documents-generate-delivery-note>
    <!-- content -->
</sw-bulk-edit-order-documents-generate-delivery-note>
```

## sw-bulk-edit-order-documents-generate-invoice

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `generateData` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-order-documents-generate-invoice>
    <!-- content -->
</sw-bulk-edit-order-documents-generate-invoice>
```

## sw-bulk-edit-order-documents

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| documents | `any` | — | yes |  |
| value | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `documentTypeRepository` | |
| `documentTypeCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-order-documents
    documents="..."
    value="..."
>
    <!-- content -->
</sw-bulk-edit-order-documents>
```

## sw-bulk-edit-order

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setRouteMetaModule` | |
| `loadBulkEditData` | |
| `fetchStatusOptions` | |
| `fetchStateMachineStates` | |
| `fetchToStateMachineTransitions` | |
| `toStateMachineStatesCriteria` | |
| `onProcessData` | |
| `openModal` | |
| `closeModal` | |
| `onSave` | |
| `getLatestOrderStatus` | |
| `loadCustomFieldSets` | |
| `onCustomFieldsChange` | |
| `onChangeDocument` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectedIds` | |
| `stateMachineStateRepository` | |
| `orderRepository` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `hasChanges` | |
| `restrictedFields` | |
| `statusFormFields` | |
| `documentsFormFields` | |
| `tagsFormFields` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-order>
    <!-- content -->
</sw-bulk-edit-order>
```

## sw-bulk-edit-product-description

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-product-description>
    <!-- content -->
</sw-bulk-edit-product-description>
```

## sw-bulk-edit-product-media-form

> Shopware Administration component.

### Examples

#### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-media/sw-bulk-edit-product-media.html.twig`
```twig
    <sw-bulk-edit-product-media-form
        :disabled="disabled || undefined"
        @media-open="showMediaModal = true"
    />
    {% endblock %}

    {% block sw_bulk_edit_product_media_modal %}
    <sw-media-modal-v2
        v-if="showMediaModal"
        :initial-folder-id="mediaDefaultFolderId"
        :entity-context="product.getEntityName()"
        @media-modal-selection-change="onAddMedia"
        @modal-close="showMediaModal = false"
    />
    {% endblock %}
```

## sw-bulk-edit-product-media

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadMediaDefaultFolder` | |
| `getMediaDefaultFolderId` | |
| `onAddMedia` | |
| `addMedia` | |
| `isExistingMedia` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `productMediaRepository` | |
| `mediaDefaultFolderRepository` | |
| `mediaDefaultFolderCriteria` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-media/sw-bulk-edit-product-media.html.twig`
```twig
    <sw-bulk-edit-product-media-form
        :disabled="disabled || undefined"
        @media-open="showMediaModal = true"
    />
    {% endblock %}

    {% block sw_bulk_edit_product_media_modal %}
    <sw-media-modal-v2
        v-if="showMediaModal"
        :initial-folder-id="mediaDefaultFolderId"
        :entity-context="product.getEntityName()"
        @media-modal-selection-change="onAddMedia"
        @modal-close="showMediaModal = false"
    />
    {% endblock %}
```

## sw-bulk-edit-product-visibility

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| bulkEditProduct | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `visibilitiesRemoveInheritanceFunction` | |
| `openModal` | |
| `closeModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `productVisibilityRepository` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-product-visibility
    bulkEditProduct="..."
>
    <!-- content -->
</sw-bulk-edit-product-visibility>
```

## sw-bulk-edit-product

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-bulk-edit-modal-cancel | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setRouteMetaModule` | |
| `setBulkEditProductValue` | |
| `getParentProduct` | |
| `loadDefaultCurrency` | |
| `defineBulkEditData` | |
| `loadBulkEditData` | |
| `loadCustomFieldSets` | |
| `loadTaxes` | |
| `productTaxRate` | |
| `loadCurrencies` | |
| `definePricesBulkEdit` | |
| `setProductPrice` | |
| `onChangePrices` | |
| `onCustomFieldsChange` | |
| `onProcessData` | |
| `processListPrice` | |
| `processRegulationPrice` | |
| `openModal` | |
| `onSave` | |
| `savePreferenceUnits` | |
| `closeModal` | |
| `onChangeLanguage` | |
| `loadRules` | |
| `loadPreferenceUnits` | |
| `onRuleChange` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `setProductSearchKeywords` | |
| `setProductAssociation` | |
| `onUpdateDefaultUnit` | |
| `convertWidth` | |
| `convertHeight` | |
| `convertLength` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `taxes` | |
| `defaultCurrency` | |
| `defaultPrice` | |
| `selectedIds` | |
| `customFieldSetRepository` | |
| `currencyRepository` | |
| `taxRepository` | |
| `productRepository` | |
| `hasSelectedChanges` | |
| `customFieldSetCriteria` | |
| `taxCriteria` | |
| `productCriteria` | |
| `isChild` | |
| `restrictedFields` | |
| `generalFormFields` | |
| `pricesFormFields` | |
| `advancedPricesFormFields` | |
| `propertyFormFields` | |
| `deliverabilityFormFields` | |
| `assignmentFormFields` | |
| `mediaFormFields` | |
| `labellingFormFields` | |
| `seoFormFields` | |
| `measuresPackagingFields` | |
| `sellingPackagingFields` | |
| `essentialCharacteristicsFormFields` | |
| `ruleRepository` | |
| `priceRepository` | |
| `ruleCriteria` | |
| `priceRuleGroups` | |
| `hasPreferenceUnitsChanged` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-media/sw-bulk-edit-product-media.html.twig`
```twig
    <sw-bulk-edit-product-media-form
        :disabled="disabled || undefined"
        @media-open="showMediaModal = true"
    />
    {% endblock %}

    {% block sw_bulk_edit_product_media_modal %}
    <sw-media-modal-v2
        v-if="showMediaModal"
        :initial-folder-id="mediaDefaultFolderId"
        :entity-context="product.getEntityName()"
        @media-modal-selection-change="onAddMedia"
        @modal-close="showMediaModal = false"
    />
    {% endblock %}
```

## sw-bulk-edit-save-modal-confirm

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemTotal | `any` | — | yes |  |
| bulkEditData | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| title-set | — | |
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
| `isFlowTriggered` | |
| `triggeredFlows` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-save-modal-confirm
    itemTotal="..."
>
    <!-- content -->
</sw-bulk-edit-save-modal-confirm>
```

## sw-bulk-edit-save-modal-error

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| title-set | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-save-modal-error>
    <!-- content -->
</sw-bulk-edit-save-modal-error>
```

## sw-bulk-edit-save-modal-process

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| changes-apply | — | |
| title-set | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `createDocuments` | |
| `createDocument` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectedIds` | |
| `documentTypes` | |
| `documentTypeConfigs` | |
| `selectedDocumentTypes` | |
| `createDocumentPayload` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-save-modal-process>
    <!-- content -->
</sw-bulk-edit-save-modal-process>
```

## sw-bulk-edit-save-modal-success

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| title-set | — | |
| buttons-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTitle` | |
| `updateButtons` | |
| `getLatestDocuments` | |
| `downloadDocument` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `documentRepository` | |
| `selectedIds` | |
| `downloadOrderDocuments` | |
| `latestDocumentsCriteria` | |
| `selectedDocumentTypes` | |
| `description` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-save-modal-success>
    <!-- content -->
</sw-bulk-edit-save-modal-success>
```

## sw-bulk-edit-save-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemTotal | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| processStatus | `any` | — | yes |  |
| bulkEditData | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| bulk-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `addEventListeners` | |
| `removeEventListeners` | |
| `beforeUnloadListener` | |
| `onModalClose` | |
| `applyChanges` | |
| `redirect` | |
| `setTitle` | |
| `updateButtons` | |
| `onButtonClick` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentStep` | |
| `buttons` | |

### Examples

#### Basic Usage
```twig
<sw-bulk-edit-save-modal
    itemTotal="..."
    isLoading="..."
    processStatus="..."
>
    <!-- content -->
</sw-bulk-edit-save-modal>
```

## sw-button-deprecated

> **Deprecated in 6.7** — Use `mt-button` instead. Will be removed in 6.8.
> See mt-button for the replacement.

- [Props](#props)
- [Slots](#slots)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-button>` | `<mt-button>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| variant | `any` | `''` | no | Valid: `primary`, `ghost`, `danger`, `ghost-danger`, `contrast`, `context` |
| size | `any` | `''` | no | Valid: `x-small`, `small` |
| square | `any` | `false` | no |  |
| block | `any` | `false` | no |  |
| routerLink | `any` | — | no |  |
| link | `any` | `null` | no |  |
| isLoading | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `buttonClasses` | |
| `contentVisibilityClass` | |
| `filteredAttributes` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-country-detail__save-action"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        :disabled="!country || !allowSave || undefined"
        variant="primary"
        @update:process-success="saveFinish"
        @click.prevent="onSave"
    >
        {{ $tc('sw-settings-country.detail.buttonSave') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}
```

#### Example 2
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-search__button-save"
        variant="primary"
        :disabled="!allowSave"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        @update:process-success="saveFinish"
        @click.prevent="onSaveSearchSettings"
    >
        {{ $tc('global.default.save') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
<sw-button-process
    variant="primary"
    ghost
    class="sw-settings-search__search-index-rebuild-button"
    :is-loading="isRebuildInProgress"
    :disabled="isRebuildInProgress || !acl.can('product_search_config.editor')"
    :process-success="isRebuildSuccess"
    @update:process-success="buildFinish"
    @click="rebuildSearchIndex"
>
    {{ $tc('sw-settings-search.generalTab.buttonRebuildSearchIndex') }}
</sw-button-process>

{% block sw_settings_search_search_index_lastest_build %}
<span class="sw-settings-search__search-index-latest-build">
```

#### Example 4
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-salutation-detail__save"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        :disabled="invalidKey || isKeyChecking || !allowSave || undefined"
        variant="primary"
        @update:process-success="saveFinish"
        @click="onSave"
    >
        {{ $tc('sw-settings-salutation.general.buttonSave') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}
```

#### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
    <sw-button-process
        class="sw-bulk-edit-product__save-action"
        variant="primary"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        :disabled="isLoading || !hasSelectedChanges || undefined"
        @click="openModal"
    >
        {{ $tc('sw-bulk-edit.applyChanges') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}

{% block sw_bulk_edit_product_content %}
```

## sw-button-group

> Groups multiple buttons together with consistent spacing.

- [Slots](#slots)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | `false` | no |  |
| splitButton | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `buttonGroupClasses` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-edit-profile-modal-mapping/sw-import-export-edit-profile-modal-mapping.html.twig`
```twig
<sw-button-group class="sw-import-export-edit-profile-modal-mapping__position-buttons">
    {% block sw_import_export_edit_profile_modal_mapping_grid_position_column_button_group_up %}
    <mt-button
        size="x-small"
        square
        :disabled="isFirstMapping(item) || !!searchTerm"
        variant="secondary"
        @click="updateSorting(itemIndex, 'up')"
    >
        {% block sw_import_export_edit_profile_modal_mapping_grid_position_column_button_group_up_icon %}
        <mt-icon
            name="regular-chevron-up-xs"
            size="10px"
        />
        {% endblock %}
```

#### Example 2
Source: `sw-settings-rule/page/sw-settings-rule-detail/sw-settings-rule-detail.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('rule.editor'),
        showOnDisabledElements: true
    }"
    class="sw-settings-rule-detail__save-button-group"
    :split-button="true"
>
    {% block sw_settings_rule_detail_actions_save %}
    <sw-button-process
        v-model:process-success="isSaveSuccessful"
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-rule-detail__save-action"
        :is-loading="isLoading"
```

#### Example 3
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product.creator'),
        showOnDisabledElements: true
    }"
    class="sw-product-list__add-button-group"
    split-button
>
    {% block sw_product_list_smart_bar_actions_add %}
    <mt-button
        v-tooltip="{
            message: $tc('sw-privileges.tooltip.warning'),
            disabled: acl.can('product.creator'),
            showOnDisabledElements: true
```

#### Example 4
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product.editor'),
        showOnDisabledElements: true
    }"
    class="sw-product-detail__save-button-group"
    :split-button="true"
>
    {% block sw_product_detail_actions_save %}
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-product-detail__save-action"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
```

#### Example 5
Source: `sw-product-stream/page/sw-product-stream-detail/sw-product-stream-detail.html.twig`
```twig
<sw-button-group
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product_stream.editor'),
        showOnDisabledElements: true
    }"
    class="sw-product-stream-detail__save-button-group"
    :split-button="true"
>
    {% block sw_product_stream_detail_actions_save %}
    <sw-button-process
        v-model:process-success="isSaveSuccessful"
        v-tooltip.bottom="tooltipSave"
        class="sw-product-stream-detail__save-action"
        :is-loading="isLoading"
```

## sw-button-process

> Button with integrated progress/loading state visualization.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| processSuccess | `any` | — | yes |  |
| animationTimeout | `any` | `1250` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:processSuccess | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `contentVisibilityClass` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-button-process
    v-tooltip.bottom="tooltipSave"
    class="sw-settings-country-detail__save-action"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    :disabled="!country || !allowSave || undefined"
    variant="primary"
    @update:process-success="saveFinish"
    @click.prevent="onSave"
>
    {{ $tc('sw-settings-country.detail.buttonSave') }}
</sw-button-process>
```

#### Example 2
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-button-process
    v-tooltip.bottom="tooltipSave"
    class="sw-settings-search__button-save"
    variant="primary"
    :disabled="!allowSave"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    @update:process-success="saveFinish"
    @click.prevent="onSaveSearchSettings"
>
    {{ $tc('global.default.save') }}
</sw-button-process>
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
<sw-button-process
    variant="primary"
    ghost
    class="sw-settings-search__search-index-rebuild-button"
    :is-loading="isRebuildInProgress"
    :disabled="isRebuildInProgress || !acl.can('product_search_config.editor')"
    :process-success="isRebuildSuccess"
    @update:process-success="buildFinish"
    @click="rebuildSearchIndex"
>
    {{ $tc('sw-settings-search.generalTab.buttonRebuildSearchIndex') }}
</sw-button-process>
```

#### Example 4
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-button-process
    v-tooltip.bottom="tooltipSave"
    class="sw-settings-salutation-detail__save"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    :disabled="invalidKey || isKeyChecking || !allowSave || undefined"
    variant="primary"
    @update:process-success="saveFinish"
    @click="onSave"
>
    {{ $tc('sw-settings-salutation.general.buttonSave') }}
</sw-button-process>
```

#### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-button-process
    class="sw-bulk-edit-product__save-action"
    variant="primary"
    :is-loading="isLoading"
    :process-success="isSaveSuccessful"
    :disabled="isLoading || !hasSelectedChanges || undefined"
    @click="openModal"
>
    {{ $tc('sw-bulk-edit.applyChanges') }}
</sw-button-process>
```

## sw-button

> **Migration wrapper** — Delegates to `mt-button` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-button for the new component.

- [Slots](#slots)
- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| routerLink | `null \| null` | `null` | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClick` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-country-detail__save-action"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        :disabled="!country || !allowSave || undefined"
        variant="primary"
        @update:process-success="saveFinish"
        @click.prevent="onSave"
    >
        {{ $tc('sw-settings-country.detail.buttonSave') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}
```

#### Example 2
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-search__button-save"
        variant="primary"
        :disabled="!allowSave"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        @update:process-success="saveFinish"
        @click.prevent="onSaveSearchSettings"
    >
        {{ $tc('global.default.save') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
<sw-button-process
    variant="primary"
    ghost
    class="sw-settings-search__search-index-rebuild-button"
    :is-loading="isRebuildInProgress"
    :disabled="isRebuildInProgress || !acl.can('product_search_config.editor')"
    :process-success="isRebuildSuccess"
    @update:process-success="buildFinish"
    @click="rebuildSearchIndex"
>
    {{ $tc('sw-settings-search.generalTab.buttonRebuildSearchIndex') }}
</sw-button-process>

{% block sw_settings_search_search_index_lastest_build %}
<span class="sw-settings-search__search-index-latest-build">
```

#### Example 4
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
    <sw-button-process
        v-tooltip.bottom="tooltipSave"
        class="sw-settings-salutation-detail__save"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        :disabled="invalidKey || isKeyChecking || !allowSave || undefined"
        variant="primary"
        @update:process-success="saveFinish"
        @click="onSave"
    >
        {{ $tc('sw-settings-salutation.general.buttonSave') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}
```

#### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
    <sw-button-process
        class="sw-bulk-edit-product__save-action"
        variant="primary"
        :is-loading="isLoading"
        :process-success="isSaveSuccessful"
        :disabled="isLoading || !hasSelectedChanges || undefined"
        @click="openModal"
    >
        {{ $tc('sw-bulk-edit.applyChanges') }}
    </sw-button-process>
    {% endblock %}
</template>
{% endblock %}

{% block sw_bulk_edit_product_content %}
```

## sw-card-deprecated

> **Deprecated in 6.7** — Use `mt-card` instead. Will be removed in 6.8.
> See mt-card for the replacement.

- [Props](#props)
- [Slots](#slots)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-card>` | `<mt-card>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| positionIdentifier | `any` | `null` | yes |  |
| title | `any` | `''` | no |  |
| subtitle | `any` | `''` | no |  |
| hero | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |
| large | `any` | `false` | no |  |
| aiBadge | `any` | `false` | no |  |
| contentPadding | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| avatar | — | |
| title | — | |
| subtitle | — | |
| header-right | — | |
| tabs | — | |
| toolbar | — | |
| context-actions | — | |
| grid | title: title | |
| footer | — | |

### Methods

| Method | Description |
|--------|-------------|
| `cardClasses` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showHeader` | |
| `hasAvatar` | |
| `cardContentClasses` | |
| `contextSlot` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_list_content_card %}
    <mt-card
        v-if="isLoading || country"
        position-identifier="sw-settings-country-list"
    >
        {% block sw_settings_country_list_grid %}
        <template #grid>
            {% block sw_settings_country_list_grid_inner %}
            <sw-entity-listing
                ref="swSettingsCountryGrid"
                class="sw-settings-country-list-grid"
                :data-source="country"
                :columns="getCountryColumns()"
                :repository="countryRepository"
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_detail_content_language_info %}
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
```

#### Example 3
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_search_tabs_header %}
    <sw-tabs position-identifier="sw-settings-search-header">
        {% block sw_setting_search_tabs_general %}
        <sw-tabs-item
            v-bind="$props"
            class="sw-settings-search__general-tab"
            :route="{ name: 'sw.settings.search.index.general' }"
            @click="onTabChange"
        >
            {{ $tc('sw-settings-search.page.generalTab') }}
        </sw-tabs-item>
        {% endblock %}

        {% block sw_setting_search_tabs_live_search %}
```

#### Example 4
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-card-filter
    ref="itemFilter"
    :placeholder="$tc('sw-settings-search.generalTab.textPlaceholderTermsFilter')"
    @sw-card-filter-term-change="onSearchTermChange"
/>
{% endblock %}

{% block sw_settings_search_excluded_search_terms_actions %}
<div class="sw-settings-search-excluded-search-terms-group-actions">
    {% block sw_settings_search_excluded_search_terms_add_button %}
    <mt-button
        class="sw-settings-search-excluded-search-terms__insert-button"
        ghost
        size="small"
        :disabled="!acl.can('product_search_config.creator')"
```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-card-view>
    <sw-skeleton v-if="isLoading" />

    <template v-else>
        {% block sw_settings_salutation_detail_content_language_info %}
        <sw-language-info :entity-description="entityDescription" />
        {% endblock %}

        {% block sw_settings_salutation_detail_content_card %}
        <mt-card
            position-identifier="sw-settings-salutation-detail-content"
            :is-loading="isLoading"
            :title="$tc('sw-settings-salutation.detail.cardTitle')"
        >

```

## sw-card-filter

> Filter card with integrated search functionality.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| placeholder | `any` | `''` | no |  |
| delay | `any` | `500` | no |  |
| initialSearchTerm | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| filter | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-card-filter-term-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasFilter` | |
| `hasFilterClass` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-card-filter
    ref="itemFilter"
    :placeholder="$tc('sw-settings-search.generalTab.textPlaceholderTermsFilter')"
    @sw-card-filter-term-change="onSearchTermChange"
/>
{% endblock %}

{% block sw_settings_search_excluded_search_terms_actions %}
<div class="sw-settings-search-excluded-search-terms-group-actions">
    {% block sw_settings_search_excluded_search_terms_add_button %}
    <mt-button
        class="sw-settings-search-excluded-search-terms__insert-button"
        ghost
        size="small"
        :disabled="!acl.can('product_search_config.creator')"
```

#### Example 2
Source: `sw-settings-tax/component/sw-tax-rule-card/sw-tax-rule-card.html.twig`
```twig
<sw-card-filter
    :placeholder="$tc('sw-settings-tax.taxRuleCard.searchBarPlaceholder')"
    @sw-card-filter-term-change="onSearchTermChange"
>
    <template #filter>
        {% block sw_tax_rule_card_header_create_rule_button %}
        <mt-button
            v-tooltip.bottom="{
                message: $tc('sw-privileges.tooltip.warning'),
                disabled: acl.can('tax.editor'),
                showOnDisabledElements: true
            }"
            class="sw-tax-rule-grid-button"
            size="small"
            :disabled="!acl.can('tax.editor') || undefined"
```

#### Example 3
Source: `sw-promotion-v2/component/promotion-codes/sw-promotion-v2-individual-codes-behavior/sw-promotion-v2-individual-codes-behavior.html.twig`
```twig
<sw-card-filter
    :placeholder="$tc('sw-promotion-v2.detail.base.codes.individual.searchPlaceholder')"
    @sw-card-filter-term-change="onSearchTermChange"
>
    <template #filter>

        {% block sw_promotion_v2_individual_codes_behavior_toolbar_filter_add_codes %}
        <mt-button
            class="sw-promotion-v2-individual-codes-behavior__add-codes-action"
            ghost
            size="small"
            :disabled="!acl.can('promotion.editor')"
            variant="secondary"
            @click="onOpenAddCodesModal"
        >
```

#### Example 4
Source: `sw-settings-rule/component/sw-settings-rule-add-assignment-listing/sw-settings-rule-add-assignment-listing.html.twig`
```twig
    <sw-card-filter
        :placeholder="$tc('global.sw-simple-search-field.defaultPlaceholder')"
        @sw-card-filter-term-change="doSearch"
    />
    {% endblock %}
</template>

{% block sw_settings_rule_add_assignment_listing_grid %}
<sw-data-grid
    class="sw-settings-rule-add-assignment-listing__grid"
    :is-loading="loading"
    :data-source="items"
    :columns="entityContext.addContext.gridColumns"
    :is-record-selectable="isNotAssigned"
    :show-actions="false"
```

#### Example 5
Source: `sw-settings-rule/component/sw-settings-rule-category-tree/sw-settings-rule-category-tree.html.twig`
```twig
<sw-card-filter @sw-card-filter-term-change="searchTreeItems" />
```

## sw-card-section

> Section divider within a sw-card with configurable appearance.

- [Slots](#slots)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| divider | `any` | `''` | no | Valid: `top`, `right`, `bottom`, `left` |
| secondary | `any` | `false` | no |  |
| slim | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cardSectionClasses` | |

### Examples

#### Example 1
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-card-section divider="bottom">
    {% block sw_customer_card_metadata_container %}
    <sw-container>
        {% block sw_customer_card_metadata %}
        <div class="sw-review-detail__metadata">
            {% block sw_customer_card_metadata_customer_name %}
            {% block sw_custsomer_card_metadata_customer_name_label %}

            <div class="sw-review-detail__metadata-review-headline">
                <div>
                    <div class="sw-review-detail__metadata-review-title">
                        {{ review.title }}
                    </div>

                    <p class="sw-review-detail__metadata-review-content">
```

#### Example 2
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-card-section
    class="sw-review-detail__base-info-section"
    secondary
    slim
>
    <slot name="default">
        <sw-container
            class="sw-review-base-info"
            columns="repeat(auto-fit, minmax(250px, 1fr))"
            gap="0px 15px"
        >
            <div class="sw-review-base-info-columns">
                {% block sw_customer_base_metadata_created_at %}
                <sw-description-list>
                    {% block sw_customer_base_metadata_created_at_label %}
```

#### Example 3
Source: `sw-settings-tax/component/sw-tax-rule-card/sw-tax-rule-card.html.twig`
```twig
<sw-card-section
    divider="bottom"
    secondary
    slim
>
    {% block sw_tax_rule_card_header_filter %}
    <sw-card-filter
        :placeholder="$tc('sw-settings-tax.taxRuleCard.searchBarPlaceholder')"
        @sw-card-filter-term-change="onSearchTermChange"
    >
        <template #filter>
            {% block sw_tax_rule_card_header_create_rule_button %}
            <mt-button
                v-tooltip.bottom="{
                    message: $tc('sw-privileges.tooltip.warning'),
```

#### Example 4
Source: `sw-product/component/sw-product-properties/sw-product-properties.html.twig`
```twig
<sw-card-section
    secondary
    divider="bottom"
>
    <sw-container
        columns="1fr auto"
        gap="0 15px"
    >
        {% block sw_product_properties_filled_state_header_form_control %}
        <sw-simple-search-field
            v-model:value="searchTerm"
            variant="form"
            size="small"
            :placeholder="$tc('sw-product.properties.placeholderSearchAddedProperties')"
            :disabled="isPropertiesLoading || undefined"
```

#### Example 5
Source: `sw-customer/component/sw-customer-default-addresses/sw-customer-default-addresses.html.twig`
```twig
<sw-card-section
    v-if="customer.defaultShippingAddress.id"
    divider="right"
>
    {% block sw_customer_default_addresses_shipping_postal %}
    <sw-address
        :address="customer.defaultShippingAddress"
        :headline="$tc('sw-customer.detailBase.titleDefaultShippingAddress')"
        :show-edit-button="customerEditMode"
        :edit-link="defaultShippingAddressLink"
        :formatting-address="formattingShippingAddress"
    />
    {% endblock %}
</sw-card-section>
```

## sw-card-view

> Container for organizing multiple sw-card components in a scrollable view.

- [Slots](#slots)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| showErrorSummary | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_list_content_card %}
    <mt-card
        v-if="isLoading || country"
        position-identifier="sw-settings-country-list"
    >
        {% block sw_settings_country_list_grid %}
        <template #grid>
            {% block sw_settings_country_list_grid_inner %}
            <sw-entity-listing
                ref="swSettingsCountryGrid"
                class="sw-settings-country-list-grid"
                :data-source="country"
                :columns="getCountryColumns()"
                :repository="countryRepository"
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_detail_content_language_info %}
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
```

#### Example 3
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_search_tabs_header %}
    <sw-tabs position-identifier="sw-settings-search-header">
        {% block sw_setting_search_tabs_general %}
        <sw-tabs-item
            v-bind="$props"
            class="sw-settings-search__general-tab"
            :route="{ name: 'sw.settings.search.index.general' }"
            @click="onTabChange"
        >
            {{ $tc('sw-settings-search.page.generalTab') }}
        </sw-tabs-item>
        {% endblock %}

        {% block sw_setting_search_tabs_live_search %}
```

#### Example 4
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-card-view>
    <sw-skeleton v-if="isLoading" />

    <template v-else>
        {% block sw_settings_salutation_detail_content_language_info %}
        <sw-language-info :entity-description="entityDescription" />
        {% endblock %}

        {% block sw_settings_salutation_detail_content_card %}
        <mt-card
            position-identifier="sw-settings-salutation-detail-content"
            :is-loading="isLoading"
            :title="$tc('sw-settings-salutation.detail.cardTitle')"
        >

```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-list/sw-settings-salutation-list.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_salutation_list_card_content %}
    <mt-card
        position-identifier="sw-settings-salutation-list-content"
    >

        {% block sw_settings_salutation_list_grid %}
        <template #grid>
            <sw-entity-listing
                class="sw-settings-salutation-list-grid"
                :repository="salutationRepository"
                :is-loading="isLoading"
                :data-source="salutations"
                :columns="columns"
                identifier="sw-settings-salutation-list"
```

## sw-card

> **Migration wrapper** — Delegates to `mt-card` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-card for the new component.

- [Slots](#slots)
- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_list_content_card %}
    <mt-card
        v-if="isLoading || country"
        position-identifier="sw-settings-country-list"
    >
        {% block sw_settings_country_list_grid %}
        <template #grid>
            {% block sw_settings_country_list_grid_inner %}
            <sw-entity-listing
                ref="swSettingsCountryGrid"
                class="sw-settings-country-list-grid"
                :data-source="country"
                :columns="getCountryColumns()"
                :repository="countryRepository"
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_country_detail_content_language_info %}
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
```

#### Example 3
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-card-view>
    {% block sw_settings_search_tabs_header %}
    <sw-tabs position-identifier="sw-settings-search-header">
        {% block sw_setting_search_tabs_general %}
        <sw-tabs-item
            v-bind="$props"
            class="sw-settings-search__general-tab"
            :route="{ name: 'sw.settings.search.index.general' }"
            @click="onTabChange"
        >
            {{ $tc('sw-settings-search.page.generalTab') }}
        </sw-tabs-item>
        {% endblock %}

        {% block sw_setting_search_tabs_live_search %}
```

#### Example 4
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-card-filter
    ref="itemFilter"
    :placeholder="$tc('sw-settings-search.generalTab.textPlaceholderTermsFilter')"
    @sw-card-filter-term-change="onSearchTermChange"
/>
{% endblock %}

{% block sw_settings_search_excluded_search_terms_actions %}
<div class="sw-settings-search-excluded-search-terms-group-actions">
    {% block sw_settings_search_excluded_search_terms_add_button %}
    <mt-button
        class="sw-settings-search-excluded-search-terms__insert-button"
        ghost
        size="small"
        :disabled="!acl.can('product_search_config.creator')"
```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-card-view>
    <sw-skeleton v-if="isLoading" />

    <template v-else>
        {% block sw_settings_salutation_detail_content_language_info %}
        <sw-language-info :entity-description="entityDescription" />
        {% endblock %}

        {% block sw_settings_salutation_detail_content_card %}
        <mt-card
            position-identifier="sw-settings-salutation-detail-content"
            :is-loading="isLoading"
            :title="$tc('sw-settings-salutation.detail.cardTitle')"
        >

```

## sw-category-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldSetsArray` | |
| `categoryNameError` | |
| `categoryTypeError` | |
| `categoryTypes` | |
| `typeLinkLabel` | |
| `categoryTypeHelpText` | |
| `isSalesChannelEntryPoint` | |
| `category` | |
| `isCategoryColumn` | |

### Examples

#### Basic Usage
```twig
<sw-category-detail-base
    isLoading="..."
>
    <!-- content -->
</sw-category-detail-base>
```

## sw-category-detail-cms

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `category` | |
| `cmsPage` | |

### Examples

#### Basic Usage
```twig
<sw-category-detail-cms
    isLoading="..."
>
    <!-- content -->
</sw-category-detail-cms>
```

## sw-category-detail-custom-entity

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onAssignmentChange` | |
| `onEntityChange` | |
| `fetchCustomEntityName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customEntityAssignments` | |
| `customEntityColumns` | |
| `category` | |
| `customEntityCriteria` | |
| `sortingCriteria` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-category-detail-custom-entity>
    <!-- content -->
</sw-category-detail-custom-entity>
```

## sw-category-detail-menu

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onMediaSelectionChange` | |
| `onSetMediaItem` | |
| `onRemoveMediaItem` | |
| `onMediaDropped` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `reversedVisibility` | |
| `mediaItem` | |
| `mediaRepository` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
<sw-category-detail-menu v-bind="{ category, isLoading }" />
```

## sw-category-detail-products

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadProductStreamPreview` | |
| `onPaginateManualProductAssignment` | |
| `getParentProducts` | |
| `getItemName` | |
| `getManufacturer` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `category` | |
| `productStreamRepository` | |
| `productRepository` | |
| `productColumns` | |
| `manufacturerColumn` | |
| `nameColumn` | |
| `productCriteria` | |
| `productStreamCriteria` | |
| `productStreamInvalidError` | |
| `categoryProductStreamIdError` | |
| `categoryProductAssignmentTypeError` | |
| `productAssignmentTypes` | |
| `dynamicProductGroupHelpText` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-category-detail-products
    isLoading="..."
>
    <!-- content -->
</sw-category-detail-products>
```

## sw-category-detail-seo

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `category` | |

### Examples

#### Basic Usage
```twig
<sw-category-detail-seo
    isLoading="..."
>
    <!-- content -->
</sw-category-detail-seo>
```

## sw-category-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| categoryId | `any` | `null` | no |  |
| landingPageId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `categoryCheckedElementsCount` | |
| `landingPageCheckedElementsCount` | |
| `registerListener` | |
| `onSearch` | |
| `checkViewport` | |
| `getAssignedCmsPage` | |
| `updateCmsPageDataMapping` | |
| `getAssignedCmsPageForLandingPage` | |
| `updateCmsPageDataMappingForLandingPage` | |
| `setLandingPage` | |
| `setCategory` | |
| `loadCustomFieldSet` | |
| `loadLandingPageCustomFieldSet` | |
| `onSaveCategories` | |
| `openChangeModal` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `cancelEdit` | |
| `resetCategory` | |
| `onChangeLanguage` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `saveFinish` | |
| `onSave` | |
| `checkForEntryPointOverwrite` | |
| `cancelEntryPointOverwrite` | |
| `confirmEntryPointOverwrite` | |
| `onSaveLandingPage` | |
| `addLandingPageSalesChannelError` | |
| `extractSlotOverrides` | |
| `getCmsPageOverrides` | |
| `deleteSpecifcKeys` | |
| `updateSeoUrls` | |
| `onLandingPageDelete` | |
| `onCategoryDelete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `changesetGenerator` | |
| `showEmptyState` | |
| `identifier` | |
| `landingPageRepository` | |
| `categoryRepository` | |
| `cmsPageRepository` | |
| `landingPage` | |
| `category` | |
| `showEntryPointOverwriteModal` | |
| `cmsPage` | |
| `cmsPageState` | |
| `cmsPageId` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `customFieldSetLandingPageCriteria` | |
| `mediaRepository` | |
| `pageClasses` | |
| `tooltipSave` | |
| `landingPageTooltipSave` | |
| `tooltipCancel` | |
| `categoryCriteria` | |
| `landingPageCriteria` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
<sw-category-detail-menu v-bind="{ category, isLoading }" />
```

## sw-category-entry-point-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getInitialEntryPointFromCategory` | |
| `onEntryPointChange` | |
| `onSalesChannelChange` | |
| `resetSalesChannelCollections` | |
| `openConfigureHomeModal` | |
| `closeConfigureHomeModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `entryPoints` | |
| `associatedCollection` | |
| `helpText` | |
| `hasExistingNavigation` | |
| `salesChannelSelectionLabel` | |
| `salesChannelCriteria` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
<sw-category-entry-point-card
    v-if="(category.type === 'folder' || category.type === 'page') && !isCategoryColumn"
    v-bind="{ category, isLoading }"
/>
{% endblock %}

{% block sw_category_detail_link %}
<sw-category-link-settings
    v-if="category.type === 'link'"
    v-bind="{ category, isLoading }"
/>
{% endblock %}

<template v-if="category.type !== 'link'">
    {% block sw_category_detail_menu %}
```

## sw-category-entry-point-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannelCollection | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `closeModal` | |
| `getCmsPageTypeName` | |
| `onLayoutSelect` | |
| `onLayoutReset` | |
| `openInPagebuilder` | |
| `openLayoutModal` | |
| `closeLayoutModal` | |
| `applyChanges` | |
| `hasNotAppliedChanges` | |
| `isAttributeEqual` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectedSalesChannel` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-entry-point-card/sw-category-entry-point-card.html.twig`
```twig
    <sw-category-entry-point-modal
        v-if="configureHomeModalVisible"
        :sales-channel-collection="category.navigationSalesChannels"
        @modal-close="closeConfigureHomeModal"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```

## sw-category-entry-point-overwrite-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannels | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| cancel | — | |
| confirm | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onConfirm` | |

### Examples

#### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-category-entry-point-overwrite-modal
    v-if="showEntryPointOverwriteModal"
    :sales-channels="entryPointOverwriteSalesChannels"
    @cancel="cancelEntryPointOverwrite"
    @confirm="confirmEntryPointOverwrite"
/>
{% endblock %}

{% block sw_landing_page_content_view %}
<sw-landing-page-view
    v-if="landingPage"
    ref="landingPageView"
    :is-loading="isLoading"
/>
{% endblock %}
```

## sw-category-layout-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| cmsPage | `any` | `null` | no |  |
| isLoading | `any` | `false` | no |  |
| pageTypes | `any` | — | no |  |
| headline | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onLayoutSelect` | |
| `onLayoutReset` | |
| `openInPagebuilder` | |
| `openLayoutModal` | |
| `closeLayoutModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pageTypeTitle` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-cms/sw-category-detail-cms.html.twig`
```twig
    <sw-category-layout-card
        v-if="category.type === 'page'"
        v-bind="{ category, cmsPage, isLoading }"
    />
    {% endblock %}

    {% block sw_category_detail_cms_form %}
    <sw-cms-page-form
        v-if="cmsPage && acl.can('category.editor')"
        :page="cmsPage"
    />
    {% endblock %}

</div>
{% endblock %}
```

#### Example 2
Source: `sw-category/view/sw-landing-page-detail-cms/sw-landing-page-detail-cms.html.twig`
```twig
    <sw-category-layout-card
        v-bind="{ cmsPage, isLoading }"
        :category="landingPage"
        :page-types="['landingpage']"
        :headline="$tc('sw-landing-page.base.cms.cmsLayoutModalHeadline')"
    />
    {% endblock %}

    {% block sw_landing_page_detail_cms_form %}
    <sw-cms-page-form
        v-if="cmsPage"
        :page="cmsPage"
    />
    {% endblock %}

```

## sw-category-link-settings

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `changeEntity` | |
| `createCategoryCollection` | |
| `onSelectionAdd` | |
| `onSelectionRemove` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `linkTypeValues` | |
| `entityValues` | |
| `mainType` | |
| `isExternal` | |
| `isInternal` | |
| `productCriteria` | |
| `categoryCriteria` | |
| `internalLinkCriteria` | |
| `categoryRepository` | |
| `categoryLinkPlaceholder` | |
| `allowedCategoryTypes` | |
| `categoryLinkHelpText` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
    <sw-category-link-settings
        v-if="category.type === 'link'"
        v-bind="{ category, isLoading }"
    />
    {% endblock %}

    <template v-if="category.type !== 'link'">
        {% block sw_category_detail_menu %}
        <sw-category-detail-menu v-bind="{ category, isLoading }" />
        {% endblock %}
    </template>

    {% block sw_category_detail_attribute_sets %}
    <mt-card
        v-if="customFieldSetsArray.length > 0"
```

## sw-category-sales-channel-multi-select

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-label-property | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-add | — | |

### Methods

| Method | Description |
|--------|-------------|
| `isSelected` | |
| `addItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-entry-point-card/sw-category-entry-point-card.html.twig`
```twig
<sw-category-sales-channel-multi-select
    v-if="associatedCollection"
    class="sw-category-entry-point-card__sales-channel-selection"
    :entity-collection="associatedCollection"
    :label="salesChannelSelectionLabel"
    :criteria="salesChannelCriteria"
    :placeholder="$tc('sw-category.base.entry-point-card.placeholderSalesChannels')"
    :disabled="!selectedEntryPoint || !acl.can('category.editor')"
    @update:entity-collection="onSalesChannelChange"
/>
{% endblock %}

{% block sw_category_entry_point_card_button_configure_home %}
<mt-button
    v-if="selectedEntryPoint === 'navigationSalesChannels' && category.navigationSalesChannels.length > 0"
```

## sw-category-seo-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| category | `any` | — | yes |  |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-seo/sw-category-detail-seo.html.twig`
```twig
<sw-category-seo-form :category="category" />
```

## sw-category-tree-field

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| categoriesCollection | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| placeholder | `any` | — | yes |  |
| categoryCriteria | `any` | — | no |  |
| singleSelect | `any` | `false` | no |  |
| pageId | `any` | `null` | no |  |
| isCategoriesLoading | `any` | `false` | no |  |
| allowedTypes | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| labelProperty | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-add | — | |
| selection-remove | — | |
| categories-load-more | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `getTreeItems` | |
| `disableCategories` | |
| `onCheckSearchItem` | |
| `onCheckItem` | |
| `removeItem` | |
| `searchCategories` | |
| `isSearchItemChecked` | |
| `isSearchResultInFocus` | |
| `getBreadcrumb` | |
| `getLabelName` | |
| `onDeleteKeyup` | |
| `removeTagLimit` | |
| `openDropdown` | |
| `closeDropdown` | |
| `closeDropdownOnClickOutside` | |
| `handleGeneralKeyEvents` | |
| `handleArrowKeyEvents` | |
| `changeSearchSelection` | |
| `getFirstChildById` | |
| `getSibling` | |
| `toggleSelectedTreeItem` | |
| `findTreeItemVNodeById` | |
| `removeCheckedItems` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `globalCategoryRepository` | |
| `categoryRepository` | |
| `visibleTags` | |
| `numberOfHiddenTags` | |
| `selectedCategoriesItemsIds` | |
| `selectedCategoriesItemsTotal` | |
| `selectedCategoriesPathIds` | |
| `pageCategoryCriteria` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-link-settings/sw-category-link-settings.html.twig`
```twig
    <sw-category-tree-field
        :allowed-types="allowedCategoryTypes"
        :categories-collection="categoriesCollection"
        :placeholder="categoryLinkPlaceholder"
        :category-criteria="categoryCriteria"
        :single-select="true"
        :label="$t('global.entities.category')"
        :help-text="categoryLinkHelpText"
        class="sw-category-link-settings__selection-category"
        @selection-add="onSelectionAdd"
        @selection-remove="onSelectionRemove"
    />
</template>
{% endblock %}

```

#### Example 2
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
    <sw-category-tree-field
        key="categorySelect"
        :categories-collection="page.categories"
        :label="$tc('sw-cms.components.cmsLayoutAssignmentModal.labelCategories')"
        :placeholder="$tc('sw-cms.components.cmsLayoutAssignmentModal.placeholderCategories')"
        :page-id="page.id"
        :is-categories-loading="isCategoriesLoading"
        class="sw-cms-layout-assignment-modal__category-select"
        @categories-load-more="onExtraCategories"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_cms_layout_assignment_modal_shop_pages_select %}
```

#### Example 3
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
            <sw-category-tree-field
                :key="isInherited"
                class="sw-product-detail__select-category"
                :categories-collection="currentValue ? currentValue : []"
                :disabled="isInherited || !allowEdit"
                :placeholder="$tc('sw-product.categoryForm.placeholderCategory')"
            />
        </template>
    </sw-inherit-wrapper>
</sw-container>
{% endblock %}

{% block sw_product_category_form_tags_field %}
<sw-inherit-wrapper
    v-if="showModeSetting"
```

#### Example 4
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
    <sw-category-tree-field
        v-if="!isProductComparison"
        id="navigationCategoryId"
        required
        :categories-collection="mainCategories"
        :placeholder="navigationCategoryPlaceholder"
        :single-select="true"
        :label="$tc('sw-sales-channel.detail.navigationCategoryId')"
        :disabled="!acl.can('sales_channel.editor') || undefined"
        :help-text="$tc('sw-sales-channel.detail.navigationCategoryHelpText')"
        :error="salesChannelNavigationCategoryIdError"
        class="sw-sales-channel-detail__select-navigation-category-id"
        @selection-add="onMainSelectionAdd"
        @selection-remove="onMainSelectionRemove"
    />
```

#### Example 5
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-category-tree-field
    v-if="!isProductComparison"
    :categories-collection="footerCategories"
    :placeholder="footerCategoryPlaceholder"
    :single-select="true"
    :label="$tc('sw-sales-channel.detail.footerCategory')"
    :disabled="!acl.can('sales_channel.editor')"
    class="sw-sales-channel-detail__select-footer-category-id"
    @selection-add="onFooterSelectionAdd"
    @selection-remove="onFooterSelectionRemove"
/>
{% endblock %}

{% block sw_sales_channel_detail_base_general_input_service_category %}
<sw-category-tree-field
```

## sw-category-tree

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| categoryId | `any` | `null` | no |  |
| currentLanguageId | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |
| allowCreate | `any` | `true` | no |  |
| allowDelete | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| category-checked-elements-count | — | |
| unsaved-changes | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `openInitialTree` | |
| `loadActiveCategory` | |
| `onUpdatePositions` | |
| `syncProducts` | |
| `indexProducts` | |
| `checkedElementsCount` | |
| `deleteCheckedItems` | |
| `onDeleteCategory` | |
| `fixSortingForCategories` | |
| `getNextCategory` | |
| `changeCategory` | |
| `onGetTreeItems` | |
| `getChildrenFromParent` | |
| `loadRootCategories` | |
| `createNewElement` | |
| `createNewCategory` | |
| `syncSiblings` | |
| `addCategory` | |
| `addCategories` | |
| `removeFromStore` | |
| `getDeletedIds` | |
| `getCategoryUrl` | |
| `isHighlighted` | |
| `isErrorNavigationEntryPoint` | |
| `entryPointWarningMessage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `categoriesToDelete` | |
| `categoryRepository` | |
| `category` | |
| `categories` | |
| `disableContextMenu` | |
| `contextMenuTooltipText` | |
| `criteria` | |
| `criteriaWithChildren` | |
| `cmsPageRepository` | |
| `productRepository` | |

### Examples

#### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
        <sw-category-tree
            ref="categoryTree"
            :category-id="categoryId"
            :current-language-id="currentLanguageId"
            :allow-edit="acl.can('category.editor')"
            :allow-create="acl.can('category.creator')"
            :allow-delete="acl.can('category.deleter')"
            @unsaved-changes="openChangeModal"
            @category-checked-elements-count="categoryCheckedElementsCount"
        />
        {% endblock %}

    </template>
</sw-sidebar-collapse>
{% endblock %}
```

#### Example 2
Source: `sw-category/component/sw-category-link-settings/sw-category-link-settings.html.twig`
```twig
    <sw-category-tree-field
        :allowed-types="allowedCategoryTypes"
        :categories-collection="categoriesCollection"
        :placeholder="categoryLinkPlaceholder"
        :category-criteria="categoryCriteria"
        :single-select="true"
        :label="$t('global.entities.category')"
        :help-text="categoryLinkHelpText"
        class="sw-category-link-settings__selection-category"
        @selection-add="onSelectionAdd"
        @selection-remove="onSelectionRemove"
    />
</template>
{% endblock %}

```

#### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
    <sw-category-tree-field
        key="categorySelect"
        :categories-collection="page.categories"
        :label="$tc('sw-cms.components.cmsLayoutAssignmentModal.labelCategories')"
        :placeholder="$tc('sw-cms.components.cmsLayoutAssignmentModal.placeholderCategories')"
        :page-id="page.id"
        :is-categories-loading="isCategoriesLoading"
        class="sw-cms-layout-assignment-modal__category-select"
        @categories-load-more="onExtraCategories"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_cms_layout_assignment_modal_shop_pages_select %}
```

#### Example 4
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
            <sw-category-tree-field
                :key="isInherited"
                class="sw-product-detail__select-category"
                :categories-collection="currentValue ? currentValue : []"
                :disabled="isInherited || !allowEdit"
                :placeholder="$tc('sw-product.categoryForm.placeholderCategory')"
            />
        </template>
    </sw-inherit-wrapper>
</sw-container>
{% endblock %}

{% block sw_product_category_form_tags_field %}
<sw-inherit-wrapper
    v-if="showModeSetting"
```

#### Example 5
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
    <sw-category-tree-field
        v-if="!isProductComparison"
        id="navigationCategoryId"
        required
        :categories-collection="mainCategories"
        :placeholder="navigationCategoryPlaceholder"
        :single-select="true"
        :label="$tc('sw-sales-channel.detail.navigationCategoryId')"
        :disabled="!acl.can('sales_channel.editor') || undefined"
        :help-text="$tc('sw-sales-channel.detail.navigationCategoryHelpText')"
        :error="salesChannelNavigationCategoryIdError"
        class="sw-sales-channel-detail__select-navigation-category-id"
        @selection-add="onMainSelectionAdd"
        @selection-remove="onMainSelectionRemove"
    />
```

## sw-category-view

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | yes |  |
| type | `any` | `'page'` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `category` | |
| `isCategoryColumn` | |
| `cmsPage` | |
| `isPage` | |
| `isCustomEntity` | |
| `swCategoryViewError` | |

### Examples

#### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-category-view
    v-if="category"
    ref="categoryView"
    :is-loading="isLoading"
    :type="category.type"
/>
{% endblock %}

{% block sw_category_content_entry_point_overwrite_modal %}
<sw-category-entry-point-overwrite-modal
    v-if="showEntryPointOverwriteModal"
    :sales-channels="entryPointOverwriteSalesChannels"
    @cancel="cancelEntryPointOverwrite"
    @confirm="confirmEntryPointOverwrite"
/>
```

## sw-chart-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| availableRanges | `any` | — | no |  |
| defaultRangeIndex | `any` | — | no |  |
| cardTitle | `any` | `''` | no |  |
| cardSubtitle | `any` | `''` | no |  |
| positionIdentifier | `any` | `''` | yes |  |
| helpText | `null \| null` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header-title | — | |
| header-link | — | |
| range-option | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-chart-card-range-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `dispatchRangeUpdate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasHeaderLink` | |

### Examples

#### Example 1
Source: `sw-dashboard/component/sw-dashboard-statistics/sw-dashboard-statistics.html.twig`
```twig
<sw-chart-card
    class="sw-dashboard-statistics__statistics-count"
    :available-ranges="availableRanges"
    :card-subtitle="getCardSubtitle(ordersDateRange)"
    :series="orderCountSeries"
    :options="chartOptionsOrderCount"
    :fill-empty-values="ordersDateRange.aggregate"
    :card-title="$tc('sw-dashboard.monthStats.orderNumber')"
    type="line"
    sort
    position-identifier=""
    @sw-chart-card-range-update="onOrdersRangeUpdate"
>
    <template #range-option="{ range }">
        {{ $tc(`sw-dashboard.monthStats.dateRanges.${range}`) }}
```

#### Example 2
Source: `sw-dashboard/component/sw-dashboard-statistics/sw-dashboard-statistics.html.twig`
```twig
<sw-chart-card
    class="sw-dashboard-statistics__statistics-sum"
    :available-ranges="availableRanges"
    :card-subtitle="getCardSubtitle(turnoverDateRange)"
    :series="orderSumSeries"
    :options="chartOptionsOrderSum"
    :fill-empty-values="turnoverDateRange.aggregate"
    :card-title="$tc('sw-dashboard.monthStats.turnover')"
    :help-text="$tc('sw-dashboard.monthStats.helperText')"
    type="line"
    sort
    position-identifier=""
    @sw-chart-card-range-update="onTurnoverRangeUpdate"
>
    <template #range-option="{ range }">
```

## sw-chart

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | — | yes | Valid: `line`, `area`, `bar`, `radar`, `histogram`, `pie`, `donut`, `scatter`, `bubble`, `heatmap` |
| options | `any` | — | yes |  |
| series | `any` | — | yes |  |
| height | `any` | `400` | no |  |
| fillEmptyValues | `any` | `null` | no |  |
| sort | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `sortSeries` | |
| `addZeroValuesToSeries` | |
| `setDateTime` | |
| `incrementByTimeUnit` | |
| `getZeroValues` | |
| `loadLocaleConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mergedOptions` | |
| `mergedLabels` | |
| `optimizedSeries` | |
| `convertedSeriesStructure` | |
| `generatedLabels` | |
| `needOneDimensionalArray` | |
| `defaultLocale` | |
| `defaultOptions` | |

### Examples

#### Example 1
Source: `sw-dashboard/component/sw-dashboard-statistics/sw-dashboard-statistics.html.twig`
```twig
<sw-chart-card
    class="sw-dashboard-statistics__statistics-count"
    :available-ranges="availableRanges"
    :card-subtitle="getCardSubtitle(ordersDateRange)"
    :series="orderCountSeries"
    :options="chartOptionsOrderCount"
    :fill-empty-values="ordersDateRange.aggregate"
    :card-title="$tc('sw-dashboard.monthStats.orderNumber')"
    type="line"
    sort
    position-identifier=""
    @sw-chart-card-range-update="onOrdersRangeUpdate"
>
    <template #range-option="{ range }">
        {{ $tc(`sw-dashboard.monthStats.dateRanges.${range}`) }}
```

## sw-checkbox-field-deprecated

> **Deprecated in 6.7** — Use `mt-checkbox` instead. Will be removed in 6.8.
> See mt-checkbox for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-checkbox-field>` | `<mt-checkbox>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| id | `any` | — | no |  |
| disabled | `any` | `false` | no |  |
| label | `any` | — | no |  |
| value | `any` | `null` | no |  |
| inheritedValue | `any` | `null` | no |  |
| ghostValue | `any` | `null` | no |  |
| error | `any` | `null` | no |  |
| bordered | `any` | `false` | no |  |
| padded | `any` | `false` | no |  |
| partlyChecked | `any` | `false` | no |  |
| ariaLabel | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `swCheckboxFieldClasses` | |
| `swCheckboxFieldContentClasses` | |
| `identification` | |
| `hasError` | |
| `inputState` | |
| `isInheritanceField` | |
| `isInherited` | |
| `isPartlyChecked` | |
| `iconName` | |
| `attrsWithoutClass` | |

### Examples

#### Basic Usage
```twig
<sw-checkbox-field-deprecated>
    <!-- content -->
</sw-checkbox-field-deprecated>
```

## sw-checkbox-field

> **Migration wrapper** — Delegates to `mt-checkbox` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-checkbox for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `any` | `null` | no |  |
| value | `any` | `null` | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |
| `handleUpdateChecked` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `compatValue` | |

### Examples

#### Basic Usage
```twig
<sw-checkbox-field>
    <!-- content -->
</sw-checkbox-field>
```

## sw-circle-icon

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | `any` | `50` | no |  |
| iconName | `any` | — | yes |  |
| variant | `any` | `''` | no | Valid: `info`, `danger`, `success`, `warning`, `neutral`, `primary` |

### Computed Properties

| Name | Description |
|------|-------------|
| `iconSize` | |
| `backgroundStyles` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-adding-failed/sw-extension-adding-failed.html.twig`
```twig
<sw-circle-icon
    :size="72"
    icon-name="regular-times-circle-s"
    variant="danger"
/>
{% endblock %}

{% block sw_extension_adding_failed_headline %}
<h3>{{ title || headline }}</h3>
{% endblock %}

{% block sw_extension_adding_failed_notification %}
<p>{{ detail || text }}</p>
<p v-if="documentationLink">
    <a :href="documentationLink">
```

#### Example 2
Source: `sw-extension/component/sw-extension-adding-success/sw-extension-adding-success.html.twig`
```twig
        <sw-circle-icon
            :size="72"
            icon-name="regular-checkmark"
            variant="success"
        />
        {% endblock %}

        {% block sw_extension_adding_success_headline %}
        <h3>{{ $tc('sw-extension-store.component.sw-extension-adding-success.titleSuccess') }}</h3>
        {% endblock %}

        {% block sw_extension_adding_success_sub_headline %}
        <p>{{ $tc('sw-extension-store.component.sw-extension-adding-success.subtitleSuccess') }}</p>
        {% endblock %}

```

## sw-cms-block-app-preview-renderer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `previewImage` | |
| `blockLabel` | |
| `appName` | |

### Examples

#### Basic Usage
```twig
<sw-cms-block-app-preview-renderer>
    <!-- content -->
</sw-cms-block-app-preview-renderer>
```

## sw-cms-block-app-renderer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `slots` | |
| `blockStyle` | |

### Examples

#### Basic Usage
```twig
<sw-cms-block-app-renderer>
    <!-- content -->
</sw-cms-block-app-renderer>
```

## sw-cms-block-category-navigation

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-category-navigation>
    <!-- content -->
</sw-cms-block-category-navigation>
```

## sw-cms-block-center-text

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-center-text>
    <!-- content -->
</sw-cms-block-center-text>
```

## sw-cms-block-config

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| block-delete | — | |
| block-duplicate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSetBackgroundMedia` | |
| `successfulUpload` | |
| `removeMedia` | |
| `onBlockDelete` | |
| `onBlockDuplicate` | |
| `onBlockNameChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `uploadTag` | |
| `mediaRepository` | |
| `cmsPageState` | |
| `cmsBlocks` | |
| `blockConfig` | |
| `quickactionsDisabled` | |
| `duplicateDisabled` | |
| `combinedDuplicateDisabled` | |
| `combinedDuplicateClasses` | |
| `quickactionClasses` | |
| `backgroundModeOptions` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
        <sw-cms-block-config
            :block="selectedBlock"
            @block-delete="onBlockDelete"
            @block-duplicate="onBlockDuplicate"
        />
    </template>
    {% endblock %}
</sw-sidebar-collapse>
{% endblock %}

{% block sw_cms_sidebar_block_layout_settings_content %}
<sw-sidebar-collapse :expand-on-loading="false">

    {% block sw_cms_sidebar_block_layout_settings_header %}
    <template #header>
```

## sw-cms-block-cross-selling

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-cross-selling>
    <!-- content -->
</sw-cms-block-cross-selling>
```

## sw-cms-block-form

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-form>
    <!-- content -->
</sw-cms-block-form>
```

## sw-cms-block-gallery-buybox

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `currentDeviceView` | |
| `currentDeviceViewClass` | |

### Examples

#### Basic Usage
```twig
<sw-cms-block-gallery-buybox>
    <!-- content -->
</sw-cms-block-gallery-buybox>
```

## sw-cms-block-html

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-html>
    <!-- content -->
</sw-cms-block-html>
```

## sw-cms-block-image-bubble-row

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-bubble-row>
    <!-- content -->
</sw-cms-block-image-bubble-row>
```

## sw-cms-block-image-cover

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-cover>
    <!-- content -->
</sw-cms-block-image-cover>
```

## sw-cms-block-image-four-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-four-column>
    <!-- content -->
</sw-cms-block-image-four-column>
```

## sw-cms-block-image-gallery

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-gallery>
    <!-- content -->
</sw-cms-block-image-gallery>
```

## sw-cms-block-image-highlight-row

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-highlight-row>
    <!-- content -->
</sw-cms-block-image-highlight-row>
```

## sw-cms-block-image-simple-grid

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-simple-grid>
    <!-- content -->
</sw-cms-block-image-simple-grid>
```

## sw-cms-block-image-slider

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-slider>
    <!-- content -->
</sw-cms-block-image-slider>
```

## sw-cms-block-image-text-bubble

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-text-bubble>
    <!-- content -->
</sw-cms-block-image-text-bubble>
```

## sw-cms-block-image-text-cover

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-text-cover>
    <!-- content -->
</sw-cms-block-image-text-cover>
```

## sw-cms-block-image-text-gallery

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-text-gallery>
    <!-- content -->
</sw-cms-block-image-text-gallery>
```

## sw-cms-block-image-text-row

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-text-row>
    <!-- content -->
</sw-cms-block-image-text-row>
```

## sw-cms-block-image-text

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-text>
    <!-- content -->
</sw-cms-block-image-text>
```

## sw-cms-block-image-three-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-three-column>
    <!-- content -->
</sw-cms-block-image-three-column>
```

## sw-cms-block-image-three-cover

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-three-cover>
    <!-- content -->
</sw-cms-block-image-three-cover>
```

## sw-cms-block-image-two-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image-two-column>
    <!-- content -->
</sw-cms-block-image-two-column>
```

## sw-cms-block-image

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-image>
    <!-- content -->
</sw-cms-block-image>
```

## sw-cms-block-layout-config

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | yes |  |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-cms-block-layout-config :block="selectedBlock" />
```

## sw-cms-block-product-description-reviews

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-product-description-reviews>
    <!-- content -->
</sw-cms-block-product-description-reviews>
```

## sw-cms-block-product-heading

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `currentDeviceView` | |
| `currentDeviceViewClass` | |

### Examples

#### Basic Usage
```twig
<sw-cms-block-product-heading>
    <!-- content -->
</sw-cms-block-product-heading>
```

## sw-cms-block-product-listing

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-product-listing>
    <!-- content -->
</sw-cms-block-product-listing>
```

## sw-cms-block-product-slider

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-product-slider>
    <!-- content -->
</sw-cms-block-product-slider>
```

## sw-cms-block-product-three-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-product-three-column>
    <!-- content -->
</sw-cms-block-product-three-column>
```

## sw-cms-block-sidebar-filter

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-sidebar-filter>
    <!-- content -->
</sw-cms-block-sidebar-filter>
```

## sw-cms-block-text-hero

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-text-hero>
    <!-- content -->
</sw-cms-block-text-hero>
```

## sw-cms-block-text-on-image

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-text-on-image>
    <!-- content -->
</sw-cms-block-text-on-image>
```

## sw-cms-block-text-teaser-section

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-text-teaser-section>
    <!-- content -->
</sw-cms-block-text-teaser-section>
```

## sw-cms-block-text-teaser

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-text-teaser>
    <!-- content -->
</sw-cms-block-text-teaser>
```

## sw-cms-block-text-three-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-text-three-column>
    <!-- content -->
</sw-cms-block-text-three-column>
```

## sw-cms-block-text-two-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-text-two-column>
    <!-- content -->
</sw-cms-block-text-two-column>
```

## sw-cms-block-text

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-text>
    <!-- content -->
</sw-cms-block-text>
```

## sw-cms-block-video

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-video>
    <!-- content -->
</sw-cms-block-video>
```

## sw-cms-block-vimeo-video

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-vimeo-video>
    <!-- content -->
</sw-cms-block-vimeo-video>
```

## sw-cms-block-youtube-video

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-block-youtube-video>
    <!-- content -->
</sw-cms-block-youtube-video>
```

## sw-cms-block

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | yes |  |
| active | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| hasWarnings | `any` | `false` | no |  |
| hasErrors | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| block-overlay-click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onBlockOverlayClick` | |
| `toggleVisibility` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customBlockClass` | |
| `blockStyles` | |
| `blockPadding` | |
| `overlayClasses` | |
| `toolbarClasses` | |
| `assetFilter` | |
| `isVisible` | |
| `toggleButtonText` | |
| `expandedClass` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-block
    class="sw-cms-stage-block"
    :block="block"
    :disabled="disabled || undefined"
    :active="selectedBlock !== null && selectedBlock.id === block.id"
    :has-errors="hasBlockErrors(block)"
    @block-overlay-click="onBlockSelection(block)"
>

    {% block sw_cms_section_sidebar_block_component %}
    <component
        :is="getBlockComponent(block.type)"
        :block="block"
    >
        {% block sw_cms_section_content_block_slot %}
```

#### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-block
    class="sw-cms-stage-block"
    :block="block"
    :disabled="disabled || undefined"
    :active="selectedBlock !== null && selectedBlock.id === block.id"
    :has-errors="hasBlockErrors(block)"
    @block-overlay-click="onBlockSelection(block)"
>

    {% block sw_cms_section_content_block_component %}
    <component
        :is="getBlockComponent(block.type)"
        :block="block"
    >
        {% block sw_cms_section_content_block_component_slot %}
```

#### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
        <sw-cms-block-config
            :block="selectedBlock"
            @block-delete="onBlockDelete"
            @block-duplicate="onBlockDuplicate"
        />
    </template>
    {% endblock %}
</sw-sidebar-collapse>
{% endblock %}

{% block sw_cms_sidebar_block_layout_settings_content %}
<sw-sidebar-collapse :expand-on-loading="false">

    {% block sw_cms_sidebar_block_layout_settings_header %}
    <template #header>
```

## sw-cms-create-wizard

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-section-select | — | |
| wizard-complete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `goToStep` | |
| `getStepName` | |
| `onPageTypeSelect` | |
| `onSectionSelect` | |
| `onCompletePageCreation` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `visiblePageTypes` | |
| `currentPageType` | |
| `isCustomEntityType` | |
| `isCompletable` | |
| `customEntities` | |
| `pagePreviewMedia` | |
| `pagePreviewStyle` | |
| `assetFilter` | |
| `cmsPageStore` | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-create/sw-cms-create.html.twig`
```twig
<sw-cms-create-wizard
    :page="page"
    @on-section-select="onAddSection($event, 0)"
    @wizard-complete="onWizardComplete"
/>
{% endblock %}

```

## sw-cms-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |
| `assignToEntity` | |
| `onWizardComplete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pageHasSections` | |
| `categoryRepository` | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-create/sw-cms-create.html.twig`
```twig
<sw-cms-create-wizard
    :page="page"
    @on-section-select="onAddSection($event, 0)"
    @wizard-complete="onWizardComplete"
/>
{% endblock %}

```

## sw-cms-detail

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyedComponent` | |
| `setPageContext` | |
| `resetCmsPageState` | |
| `getDefaultFolderId` | |
| `loadPage` | |
| `hydratePage` | |
| `restoreActiveBlock` | |
| `updateDataMapping` | |
| `onDeviceViewChange` | |
| `setSelectedBlock` | |
| `onChangeLanguage` | |
| `abortOnLanguageChange` | |
| `hasUnsavedChanges` | |
| `saveOnLanguageChange` | |
| `loadDemoProduct` | |
| `loadDemoCategory` | |
| `loadDemoCategoryProducts` | |
| `onDemoEntityChange` | |
| `onAddSection` | |
| `onCloseBlockConfig` | |
| `pageConfigOpen` | |
| `saveFinish` | |
| `onPageSave` | |
| `debouncedPageSave` | |
| `onSave` | |
| `onSaveEntity` | |
| `addError` | |
| `getError` | |
| `getSlotValidations` | |
| `pageIsValid` | |
| `missingFieldsValidation` | |
| `listingPageValidation` | |
| `pageSectionCountValidation` | |
| `slotValidation` | |
| `deleteEntityAndRequiredConfigKey` | |
| `checkRequiredSlotConfigField` | |
| `updateSectionAndBlockPositions` | |
| `updateBlockPositions` | |
| `onPageUpdate` | |
| `onBlockDuplicate` | |
| `onSectionDuplicate` | |
| `onPageTypeChange` | |
| `processProductListingType` | |
| `processProductDetailType` | |
| `processBlock` | |
| `processElements` | |
| `checkSlotMappings` | |
| `isProductPageElement` | |
| `onOpenLayoutAssignment` | |
| `openLayoutAssignmentModal` | |
| `closeLayoutAssignmentModal` | |
| `onOpenLayoutSetAsDefault` | |
| `onCloseLayoutSetAsDefault` | |
| `onConfirmLayoutSetAsDefault` | |
| `setDefaultLayout` | |
| `onCloseMissingElementModal` | |
| `onSaveMissingElementModal` | |
| `onChangeDontRemindCheckbox` | |
| `onClickBack` | |
| `resetRelatedStores` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `pageRepository` | |
| `sectionRepository` | |
| `blockRepository` | |
| `slotRepository` | |
| `defaultFolderRepository` | |
| `cmsBlocks` | |
| `productRepository` | |
| `cmsStageClasses` | |
| `cmsPageTypeSettings` | |
| `blockConfigDefaults` | |
| `tooltipSave` | |
| `addBlockTitle` | |
| `pageHasSections` | |
| `loadPageCriteria` | |
| `demoProductCriteria` | |
| `currentDeviceView` | |
| `isProductPage` | |
| `requiredFieldErrors` | |
| `pageErrors` | |
| `hasPageErrors` | |
| `pageType` | |
| `layoutVersionContext` | |
| `pageNameError` | |
| `pageSectionsError` | |
| `pageBlocksError` | |
| `pageSlotsError` | |
| `pageSlotConfigError` | |

### Examples

#### Basic Usage
```twig
<sw-cms-detail>
    <!-- content -->
</sw-cms-detail>
```

## sw-cms-el-buy-box

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `pageType` | |
| `isProductPageType` | |
| `alignStyle` | |
| `currentDemoEntity` | |
| `currencyFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-buy-box>
    <!-- content -->
</sw-cms-el-buy-box>
```

## sw-cms-el-category-navigation

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-category-navigation>
    <!-- content -->
</sw-cms-el-category-navigation>
```

## sw-cms-el-config-buy-box

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onProductChange` | |
| `fetchProduct` | |
| `deleteProduct` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productSelectContext` | |
| `productCriteria` | |
| `selectedProductCriteria` | |
| `isProductPage` | |
| `alignmentOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-buy-box>
    <!-- content -->
</sw-cms-el-config-buy-box>
```

## sw-cms-el-config-category-navigation

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-category-navigation>
    <!-- content -->
</sw-cms-el-config-category-navigation>
```

## sw-cms-el-config-cross-selling

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onProductChange` | |
| `fetchProduct` | |
| `deleteProduct` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productSelectContext` | |
| `productCriteria` | |
| `selectedProductCriteria` | |
| `isProductPageType` | |
| `boxLayoutOptions` | |
| `displayModeOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-cross-selling>
    <!-- content -->
</sw-cms-el-config-cross-selling>
```

## sw-cms-el-config-form

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getShopMail` | |
| `setShopMail` | |
| `updateMailReceiver` | |
| `validateMail` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `getLastMailClass` | |
| `formTypeOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-form>
    <!-- content -->
</sw-cms-el-config-form>
```

## sw-cms-el-config-html

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onBlur` | |
| `onInput` | |
| `emitChanges` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-html>
    <!-- content -->
</sw-cms-el-config-html>
```

## sw-cms-el-config-image-gallery

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `initGalleryItems` | |
| `initConfig` | |
| `updateColumnWidth` | |
| `onOpenMediaModal` | |
| `onCloseMediaModal` | |
| `onImageUpload` | |
| `getMediaItem` | |
| `onItemRemove` | |
| `onMediaSelectionChange` | |
| `updateMediaDataValue` | |
| `onItemSort` | |
| `onChangeMinHeight` | |
| `onChangeDisplayMode` | |
| `onChangeUseFetchPriorityOnFirstItem` | |
| `emitUpdateEl` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `uploadTag` | |
| `defaultFolderName` | |
| `sliderItems` | |
| `sliderItemsConfigValue` | |
| `gridAutoRows` | |
| `isProductPage` | |
| `displayModeValueOptions` | |
| `verticalAlignValueOptions` | |
| `navigationArrowsValueOptions` | |
| `navigationDotsValueOptions` | |
| `galleryPositionValueOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-image-gallery>
    <!-- content -->
</sw-cms-el-config-image-gallery>
```

## sw-cms-el-config-image-slider

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initSliderItems` | |
| `onImageUpload` | |
| `getMediaItem` | |
| `onItemRemove` | |
| `onCloseMediaModal` | |
| `onMediaSelectionChange` | |
| `onItemSort` | |
| `updateMediaDataValue` | |
| `onOpenMediaModal` | |
| `onChangeMinHeight` | |
| `onChangeAutoSlide` | |
| `onChangeDisplayMode` | |
| `emitUpdateEl` | |
| `onChangeIsDecorative` | |
| `onChangeUseFetchPriorityOnFirstItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `uploadTag` | |
| `mediaRepository` | |
| `defaultFolderName` | |
| `items` | |
| `speedDefault` | |
| `autoplayTimeoutDefault` | |
| `displayModeValueOptions` | |
| `verticalAlignValueOptions` | |
| `navigationArrowsValueOptions` | |
| `navigationDotsValueOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-image-slider>
    <!-- content -->
</sw-cms-el-config-image-slider>
```

## sw-cms-el-config-image

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onImageUpload` | |
| `onImageRemove` | |
| `onCloseModal` | |
| `onSelectionChanges` | |
| `updateElementData` | |
| `onOpenMediaModal` | |
| `onChangeMinHeight` | |
| `onChangeDisplayMode` | |
| `onChangeIsDecorative` | |
| `emitUpdate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `uploadTag` | |
| `previewSource` | |
| `displayModeOptions` | |
| `verticalAlignOptions` | |
| `horizontalAlignOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-image>
    <!-- content -->
</sw-cms-el-config-image>
```

## sw-cms-el-config-location-renderer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| elementData | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onBlur` | |
| `onInput` | |
| `emitChanges` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `src` | |
| `configLocation` | |
| `publishingKey` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-location-renderer
    elementData="..."
>
    <!-- content -->
</sw-cms-el-config-location-renderer>
```

## sw-cms-el-config-manufacturer-logo

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isProductPage` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-manufacturer-logo>
    <!-- content -->
</sw-cms-el-config-manufacturer-logo>
```

## sw-cms-el-config-product-box

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onProductChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productSelectContext` | |
| `productCriteria` | |
| `boxLayoutOptions` | |
| `displayModeOptions` | |
| `verticalAlignOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-product-box>
    <!-- content -->
</sw-cms-el-config-product-box>
```

## sw-cms-el-config-product-description-reviews

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onProductChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productSelectContext` | |
| `productCriteria` | |
| `selectedProductCriteria` | |
| `isProductPage` | |
| `alignmentOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-product-description-reviews>
    <!-- content -->
</sw-cms-el-config-product-description-reviews>
```

## sw-cms-el-config-product-listing-config-sorting-grid

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productSortings | `any` | — | yes |  |
| defaultSorting | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sorting-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchCustomFields` | |
| `formatProductSortingFields` | |
| `isItemACustomField` | |
| `stripCustomFieldPath` | |
| `getCustomFieldLabelByCriteriaName` | |
| `getCustomFieldByName` | |
| `onDelete` | |
| `isDefaultSorting` | |
| `onPageChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `visibleProductSortings` | |
| `paginationVisible` | |
| `customFieldRepository` | |
| `customFieldCriteria` | |
| `total` | |
| `gridColumns` | |

### Examples

#### Example 1
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
            <sw-cms-el-config-product-listing-config-sorting-grid
                :product-sortings="productSortings"
                :default-sorting="defaultSorting"
                :disabled="isInherited"
            />
            {% endblock %}
        </template>
    </sw-cms-inherit-wrapper>
</template>

<template v-if="active === 'filter'">
    <sw-cms-inherit-wrapper
        field="filters"
        :element="element"
        :label="$t('sw-cms.elements.productListing.config.tab.filter')"
```

## sw-cms-el-config-product-listing

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onUpdateProductSortings` | |
| `initProductSorting` | |
| `fetchProductSortings` | |
| `updateValuesFromConfig` | |
| `transformProductSortings` | |
| `initDefaultSorting` | |
| `loadFilterableProperties` | |
| `sortProperties` | |
| `onDefaultSortingChange` | |
| `isDefaultSorting` | |
| `isActiveFilter` | |
| `updateFilters` | |
| `unpackFilters` | |
| `onFilterProperties` | |
| `onPropertiesPageChange` | |
| `propertyStatusChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showSortingGrid` | |
| `showFilterGrid` | |
| `productSortingRepository` | |
| `propertyRepository` | |
| `productSortingsCriteria` | |
| `propertyCriteria` | |
| `allProductSortingsCriteria` | |
| `excludedDefaultSortingCriteria` | |
| `productSortingsConfigValue` | |
| `filterByManufacturer` | |
| `filterByRating` | |
| `filterByPrice` | |
| `filterByFreeShipping` | |
| `filterByProperties` | |
| `showPropertySelection` | |
| `gridColumns` | |
| `gridClasses` | |
| `assetFilter` | |
| `boxLayoutOptions` | |
| `boxHeadlineLevel` | |

### Examples

#### Example 1
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
            <sw-cms-el-config-product-listing-config-sorting-grid
                :product-sortings="productSortings"
                :default-sorting="defaultSorting"
                :disabled="isInherited"
            />
            {% endblock %}
        </template>
    </sw-cms-inherit-wrapper>
</template>

<template v-if="active === 'filter'">
    <sw-cms-inherit-wrapper
        field="filters"
        :element="element"
        :label="$t('sw-cms.elements.productListing.config.tab.filter')"
```

## sw-cms-el-config-product-name

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isProductPage` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-product-name>
    <!-- content -->
</sw-cms-el-config-product-name>
```

## sw-cms-el-config-product-slider

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadManualAssignment` | |
| `getProductAssignmentTypes` | |
| `getProductStreamSortingOptions` | |
| `onChangeAssignmentType` | |
| `loadProductStream` | |
| `onChangeProductStream` | |
| `onClickProductStreamPreview` | |
| `onCloseProductStreamModal` | |
| `onProductsChange` | |
| `isSelected` | |
| `onRestoreInheritance` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productStreamRepository` | |
| `products` | |
| `productMediaFilter` | |
| `productMultiSelectContext` | |
| `productAssignmentTypes` | |
| `productStreamSortingOptions` | |
| `displayModeOptions` | |
| `alignmentOptions` | |
| `boxLayoutOptions` | |
| `arrowOptions` | |
| `productStreamCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-product-slider>
    <!-- content -->
</sw-cms-el-config-product-slider>
```

## sw-cms-el-config-sidebar-filter

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-sidebar-filter>
    <!-- content -->
</sw-cms-el-config-sidebar-filter>
```

## sw-cms-el-config-text

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onBlur` | |
| `onInput` | |
| `emitChanges` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `availableDataMappings` | |
| `customTextEditorButtons` | |
| `alignmentOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-text>
    <!-- content -->
</sw-cms-el-config-text>
```

## sw-cms-el-config-video

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onVideoUpload` | |
| `onVideoRemove` | |
| `onCloseModal` | |
| `onSelectionChanges` | |
| `updateElementData` | |
| `onOpenMediaModal` | |
| `onChangeMinHeight` | |
| `emitUpdate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `uploadTag` | |
| `previewSource` | |
| `displayModeOptions` | |
| `verticalAlignOptions` | |
| `horizontalAlignOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-video>
    <!-- content -->
</sw-cms-el-config-video>
```

## sw-cms-el-config-vimeo-video

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `shortenLink` | |
| `onImageUpload` | |
| `onImageRemove` | |
| `onCloseModal` | |
| `onSelectionChanges` | |
| `updateElementData` | |
| `onOpenMediaModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `videoID` | |
| `mediaRepository` | |
| `uploadTag` | |
| `previewSource` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-vimeo-video>
    <!-- content -->
</sw-cms-el-config-vimeo-video>
```

## sw-cms-el-config-youtube-video

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setTimeValue` | |
| `convertTimeToInputFormat` | |
| `convertTimeToUrlFormat` | |
| `shortenLink` | |
| `onImageUpload` | |
| `onImageRemove` | |
| `onCloseModal` | |
| `onSelectionChanges` | |
| `updateElementData` | |
| `onOpenMediaModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `startValue` | |
| `endValue` | |
| `videoID` | |
| `mediaRepository` | |
| `uploadTag` | |
| `previewSource` | |
| `displayModeOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-config-youtube-video>
    <!-- content -->
</sw-cms-el-config-youtube-video>
```

## sw-cms-el-cross-selling

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeUnmountComponent` | |
| `initResizeObserver` | |
| `destroyResizeObserver` | |
| `setSliderRowLimit` | |
| `getProductEl` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `demoProductElement` | |
| `sliderBoxMinWidth` | |
| `currentDeviceView` | |
| `crossSelling` | |
| `crossSellingProducts` | |
| `currentDemoEntity` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-cross-selling>
    <!-- content -->
</sw-cms-el-cross-selling>
```

## sw-cms-el-form-template-contact

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| formSettings | `any` | — | no | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salutationOptions` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-form-template-contact>
    <!-- content -->
</sw-cms-el-form-template-contact>
```

## sw-cms-el-form-template-newsletter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| formSettings | `any` | — | no | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-form-template-newsletter>
    <!-- content -->
</sw-cms-el-form-template-newsletter>
```

## sw-cms-el-form

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectedForm` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-form>
    <!-- content -->
</sw-cms-el-form>
```

## sw-cms-el-html

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-html>
    <!-- content -->
</sw-cms-el-html>
```

## sw-cms-el-image-gallery

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `getPlaceholderItems` | |
| `onChangeGalleryImage` | |
| `activeMediaClass` | |
| `setGalleryLimit` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentDeviceView` | |
| `galleryPositionClass` | |
| `currentDeviceViewClass` | |
| `verticalAlignStyle` | |
| `mediaUrls` | |
| `isProductPage` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-image-gallery>
    <!-- content -->
</sw-cms-el-image-gallery>
```

## sw-cms-el-image-slider

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| activeMedia | `null \| null` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| active-image-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setSliderItem` | |
| `activeButtonClass` | |
| `setSliderArrowItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `gridAutoRows` | |
| `uploadTag` | |
| `sliderItems` | |
| `displayModeClass` | |
| `styles` | |
| `outsideNavArrows` | |
| `navDotsClass` | |
| `navArrowsClass` | |
| `verticalAlignStyle` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-cms/elements/image-gallery/component/sw-cms-el-image-gallery.html.twig`
```twig
    <sw-cms-el-image-slider
        :element="element"
        :active-media="activeMedia"
        @active-image-change="onChangeGalleryImage"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-cms-el-image

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateDemoValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `displayModeClass` | |
| `styles` | |
| `imgStyles` | |
| `horizontalAlign` | |
| `mediaUrl` | |
| `assetFilter` | |
| `mediaConfigValue` | |

### Examples

#### Example 1
Source: `sw-cms/elements/image-gallery/component/sw-cms-el-image-gallery.html.twig`
```twig
    <sw-cms-el-image-slider
        :element="element"
        :active-media="activeMedia"
        @active-image-change="onChangeGalleryImage"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-cms-el-location-renderer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| elementData | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updatePublishData` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `src` | |
| `elementLocation` | |
| `publishingKey` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-location-renderer
    elementData="..."
>
    <!-- content -->
</sw-cms-el-location-renderer>
```

## sw-cms-el-manufacturer-logo

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isProductPage` | |
| `styles` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-manufacturer-logo>
    <!-- content -->
</sw-cms-el-manufacturer-logo>
```

## sw-cms-el-preview-buy-box

> Shopware Administration component.

### Examples

#### Example 1
Source: `sw-cms/blocks/commerce/gallery-buybox/preview/sw-cms-preview-gallery-buybox.html.twig`
```twig
<sw-cms-el-preview-buy-box />
```

## sw-cms-el-preview-category-navigation

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-category-navigation>
    <!-- content -->
</sw-cms-el-preview-category-navigation>
```

## sw-cms-el-preview-cross-selling

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-cross-selling>
    <!-- content -->
</sw-cms-el-preview-cross-selling>
```

## sw-cms-el-preview-form

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-form>
    <!-- content -->
</sw-cms-el-preview-form>
```

## sw-cms-el-preview-html

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-html>
    <!-- content -->
</sw-cms-el-preview-html>
```

## sw-cms-el-preview-image-gallery

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-image-gallery>
    <!-- content -->
</sw-cms-el-preview-image-gallery>
```

## sw-cms-el-preview-image-slider

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-cms/elements/image-gallery/preview/sw-cms-el-preview-image-gallery.html.twig`
```twig
<sw-cms-el-preview-image-slider class="sw-cms-el-preview-gallery__slider" />
```

## sw-cms-el-preview-image

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-cms/elements/image-gallery/preview/sw-cms-el-preview-image-gallery.html.twig`
```twig
<sw-cms-el-preview-image-slider class="sw-cms-el-preview-gallery__slider" />
```

## sw-cms-el-preview-location-renderer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| elementData | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `src` | |
| `previewLocation` | |
| `publishingKey` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-location-renderer
    elementData="..."
>
    <!-- content -->
</sw-cms-el-preview-location-renderer>
```

## sw-cms-el-preview-product-box

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-product-box>
    <!-- content -->
</sw-cms-el-preview-product-box>
```

## sw-cms-el-preview-product-description-reviews

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-product-description-reviews>
    <!-- content -->
</sw-cms-el-preview-product-description-reviews>
```

## sw-cms-el-preview-product-listing

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-product-listing>
    <!-- content -->
</sw-cms-el-preview-product-listing>
```

## sw-cms-el-preview-product-slider

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-product-slider>
    <!-- content -->
</sw-cms-el-preview-product-slider>
```

## sw-cms-el-preview-sidebar-filter

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-sidebar-filter>
    <!-- content -->
</sw-cms-el-preview-sidebar-filter>
```

## sw-cms-el-preview-text

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-text>
    <!-- content -->
</sw-cms-el-preview-text>
```

## sw-cms-el-preview-video

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-video>
    <!-- content -->
</sw-cms-el-preview-video>
```

## sw-cms-el-preview-vimeo-video

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-vimeo-video>
    <!-- content -->
</sw-cms-el-preview-vimeo-video>
```

## sw-cms-el-preview-youtube-video

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-preview-youtube-video>
    <!-- content -->
</sw-cms-el-preview-youtube-video>
```

## sw-cms-el-product-box

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `displaySkeleton` | |
| `mediaUrl` | |
| `altTag` | |
| `displayModeClass` | |
| `verticalAlignStyle` | |
| `assetFilter` | |
| `truncateFilter` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-cms/elements/product-listing/component/sw-cms-el-product-listing.html.twig`
```twig
    <sw-cms-el-product-box
        v-for="index in demoProductCount"
        :key="index"
        :element="getProduct(index)"
    />
</div>

<div class="sw-cms-el-product-listing__pagination">
    <div class="sw-cms-el-product-listing__pagination-entry">
        <mt-icon
            name="regular-chevron-left-xxs"
            size="20px"
        />
    </div>

```

#### Example 2
Source: `sw-cms/elements/cross-selling/component/sw-cms-el-cross-selling.html.twig`
```twig
        <sw-cms-el-product-box
            v-for="index in sliderBoxLimit"
            :key="index"
            :element="demoProductElement"
        />
        {% endblock %}
    </template>

    <template v-else>
        {% block sw_cms_element_cross_selling_products %}
        <template
            v-for="(crossSelling, index) in crossSellingProducts"
            :key="index"
        >
            <sw-cms-el-product-box
```

#### Example 3
Source: `sw-cms/elements/product-slider/component/sw-cms-el-product-slider.html.twig`
```twig
        <sw-cms-el-product-box
            v-for="index in sliderBoxLimit"
            :key="index"
            :element="demoProductElement"
        />
        {% endblock %}
    </template>

    <template v-else>
        {% block sw_cms_element_product_slider_products %}
        <template
            v-for="(product, index) in element.data.products"
            :key="index"
        >
            <sw-cms-el-product-box
```

## sw-cms-el-product-description-reviews

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `pageType` | |
| `isProductPageType` | |
| `alignStyle` | |
| `currentDemoEntity` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-product-description-reviews>
    <!-- content -->
</sw-cms-el-product-description-reviews>
```

## sw-cms-el-product-listing

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `getProduct` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentDemoProducts` | |
| `demoProductCount` | |
| `demoProductElement` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-product-listing>
    <!-- content -->
</sw-cms-el-product-listing>
```

## sw-cms-el-product-name

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateDemoValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isProductPage` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-product-name>
    <!-- content -->
</sw-cms-el-product-name>
```

## sw-cms-el-product-slider

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `setSliderRowLimit` | |
| `getProductEl` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `demoProductElement` | |
| `hasNavigationArrows` | |
| `classes` | |
| `navArrowsClasses` | |
| `sliderBoxMinWidth` | |
| `currentDeviceView` | |
| `verticalAlignStyle` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-product-slider>
    <!-- content -->
</sw-cms-el-product-slider>
```

## sw-cms-el-sidebar-filter

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `componentClasses` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-sidebar-filter>
    <!-- content -->
</sw-cms-el-sidebar-filter>
```

## sw-cms-el-text

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| element-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateDemoValue` | |
| `onBlur` | |
| `onInput` | |
| `emitChanges` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `availableDataMappings` | |
| `customTextEditorButtons` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-text>
    <!-- content -->
</sw-cms-el-text>
```

## sw-cms-el-video

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadVideoCoverMedia` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `styles` | |
| `wrapperStyles` | |
| `placeholderStyles` | |
| `contentClasses` | |
| `mediaUrl` | |
| `coverUrl` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-video>
    <!-- content -->
</sw-cms-el-video>
```

## sw-cms-el-vimeo-video

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `videoID` | |
| `byLine` | |
| `color` | |
| `doNotTrack` | |
| `loop` | |
| `mute` | |
| `title` | |
| `portrait` | |
| `controls` | |
| `videoUrl` | |
| `iframeTitle` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-vimeo-video>
    <!-- content -->
</sw-cms-el-vimeo-video>
```

## sw-cms-el-youtube-video

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `videoID` | |
| `relatedVideos` | |
| `loop` | |
| `showControls` | |
| `start` | |
| `end` | |
| `disableKeyboard` | |
| `videoUrl` | |
| `displayModeClass` | |
| `iframeTitle` | |

### Examples

#### Basic Usage
```twig
<sw-cms-el-youtube-video>
    <!-- content -->
</sw-cms-el-youtube-video>
```

## sw-cms-form-sync

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| element | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createFieldWatcher` | |
| `createWatcher` | |
| `fieldChangeHandler` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cmsElements` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-page-form/sw-cms-page-form.html.twig`
```twig
<sw-cms-form-sync :element="element">
    <component
        :is="cmsElements[element.type].configComponent"
        :element="element"
        :element-data="cmsElements[element.type]"
        @element-update="elementUpdate"
    />
</sw-cms-form-sync>
```

## sw-cms-inherit-wrapper

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| element | `any` | — | yes |  |
| field | `any` | — | yes |  |
| fieldPath | `any` | — | no |  |
| label | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance:restore | — | |
| inheritance:remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cmsElements` | |
| `baseConfig` | |
| `childConfig` | |
| `runtimeConfig` | |
| `supportsInheritance` | |
| `isInherited` | |
| `fullPath` | |
| `fieldDefaultValue` | |

### Examples

#### Example 1
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="boxLayout"
    :element="element"
    :label="$t('sw-cms.elements.productBox.config.label.layoutType')"
>

    <template #default="{ isInherited }">
        <mt-select
            v-model="element.config.boxLayout.value"
            :options="boxLayoutOptions"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
```

#### Example 2
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="boxHeadlineLevel"
    :element="element"
    :label="$t('sw-cms.elements.productBox.config.label.headlineLevel')"
>
    <template #default="{ isInherited }">
        <mt-select
            v-model="element.config.boxHeadlineLevel.value"
            :help-text="$t('sw-cms.elements.productBox.config.label.headlineLevelHelp')"
            :options="boxHeadlineLevel"
            :hide-clearable-button="true"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
```

#### Example 3
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="media"
    :element="element"
    :label="$t('sw-cms.elements.video.label')"
>
    <template #default="{ isInherited }">
        {% block sw_cms_element_video_config_media_upload %}
        <sw-cms-mapping-field
            v-model:config="element.config.media"
            value-types="entity"
            entity="media"
            :disabled="isInherited"
        >
            <sw-media-upload-v2
                variant="regular"
```

#### Example 4
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="autoPlay"
    :element="element"
>
    <template #default="{ isInherited }">
        <mt-switch
            v-model="element.config.autoPlay.value"
            class="sw-cms-el-config-video__checkboxes-auto-play"
            :disabled="isInherited"
            :label="$t('sw-cms.elements.video.config.label.autoPlay')"
            :help-text="$t('sw-cms.elements.video.config.helpText.autoPlay')"
        />
    </template>
</sw-cms-inherit-wrapper>
```

#### Example 5
Source: `sw-cms/elements/form/config/sw-cms-el-config-form.html.twig`
```twig
<sw-cms-inherit-wrapper
    field="type"
    :element="element"
    :label="$t('sw-cms.elements.form.config.label.type')"
>
    <template #default="{ isInherited }">
        <mt-select
            v-model="element.config.type.value"
            :options="formTypeOptions"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>
```

## sw-cms-layout-assignment-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onModalClose` | |
| `saveShopPages` | |
| `loadSystemConfig` | |
| `validateCategories` | |
| `validateLandingPages` | |
| `validateProducts` | |
| `onConfirm` | |
| `openConfirmChangesModal` | |
| `closeConfirmChangesModal` | |
| `onDiscardChanges` | |
| `discardCategoryChanges` | |
| `discardLandingPageChanges` | |
| `discardShopPageChanges` | |
| `discardProductChanges` | |
| `onAbort` | |
| `onKeepEditing` | |
| `onConfirmChanges` | |
| `onInputSalesChannelSelect` | |
| `onExtraCategories` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `systemConfigDomain` | |
| `shopPages` | |
| `productColumns` | |
| `productCriteria` | |
| `isProductDetailPage` | |
| `assetFilter` | |
| `categoryRepository` | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
            <sw-cms-layout-assignment-modal
                v-if="showLayoutAssignmentModal"
                :page="page"
                @modal-close="closeLayoutAssignmentModal"
            />
            {% endblock %}

            <sw-confirm-modal
                v-if="showLayoutSetAsDefaultModal"
                class="sw-cms-detail__confirm-set-as-default-modal"
                :title="$tc('sw-cms.components.setDefaultLayoutModal.title')"
                :text="$tc('sw-cms.components.setDefaultLayoutModal.infoText', {}, page.type === 'product_detail')"
                @confirm="onConfirmLayoutSetAsDefault"
                @cancel="onCloseLayoutSetAsDefault"
                @close="onCloseLayoutSetAsDefault"
```

## sw-cms-layout-modal

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| headline | `any` | `''` | no |  |
| cmsPageTypes | `any` | — | no |  |
| preSelection | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-layout-select | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `selectLayout` | |
| `selectInGrid` | |
| `selectItem` | |
| `onSearch` | |
| `toggleListMode` | |
| `gridItemClasses` | |
| `closeModal` | |
| `getPageType` | |
| `getDefaultLayouts` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pageRepository` | |
| `cmsPageCriteria` | |
| `columnConfig` | |
| `gridPreSelection` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :cms-page-types="pageTypes"
    :headline="headline"
    :pre-selection="cmsPage"
    @modal-layout-select="onLayoutSelect"
    @modal-close="closeLayoutModal"
/>
{% endblock %}

{% block sw_category_detail_layout_desc %}
<div class="sw-category-layout-card__desc">

    {% block sw_category_detail_layout_desc_info %}
    <div class="sw-category-layout-card__desc-info">
```

#### Example 2
Source: `sw-category/component/sw-category-entry-point-modal/sw-category-entry-point-modal.html.twig`
```twig
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :pre-selection="selectedSalesChannel.homeCmsPage"
    :cms-page-types="pageTypes"
    @modal-layout-select="onLayoutSelect"
    @modal-close="closeLayoutModal"
/>
{% endblock %}

{% block sw_category_entry_point_modal_layout_desc %}
<div class="sw-category-entry-point-modal__desc">

    {% block sw_category_entry_point_modal_layout_desc_info %}
    <div class="sw-category-entry-point-modal__desc-info">

```

#### Example 3
Source: `sw-custom-entity/component/sw-generic-cms-page-assignment/sw-generic-cms-page-assignment.html.twig`
```twig
    <sw-cms-layout-modal
        v-if="showLayoutSelection"
        :cms-page-types="allowedPageTypes"
        :pre-selection="cmsPage"
        @modal-layout-select="onLayoutSelect"
        @modal-close="closeLayoutModal"
    />
</div>
{% endblock %}

```

#### Example 4
Source: `sw-product/view/sw-product-detail-layout/sw-product-detail-layout.html.twig`
```twig
    <sw-cms-layout-modal
        v-if="showLayoutModal"
        :headline="$tc('sw-product.layoutAssignment.subtitle')"
        :pre-selection="currentPage"
        :cms-page-types="['product_detail']"
        @modal-layout-select="onSelectLayout"
        @modal-close="onCloseLayoutModal"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_layout_cms_config %}
<template v-if="acl.can('product.editor') && currentPage">
    {% block sw_product_detail_layout_cms_config_form %}
```

## sw-cms-list-item

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | `null` | no |  |
| active | `any` | `false` | no |  |
| isDefault | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| contextMenu | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| preview-image-change | — | |
| on-item-click | — | |
| element-click | — | |
| item-click | — | |
| cms-page-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangePreviewImage` | |
| `onElementClick` | |
| `onItemClick` | |
| `onDelete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `previewMedia` | |
| `defaultLayoutAsset` | |
| `defaultItemLayoutAssetBackground` | |
| `componentClasses` | |
| `statusClasses` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
    <sw-cms-list-item
        :page="cmsPage"
        :disabled="!acl.can('category.editor')"
        active
    />
</div>
{% endblock %}

{% block sw_category_detail_layout_modal %}
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :cms-page-types="pageTypes"
    :headline="headline"
    :pre-selection="cmsPage"
    @modal-layout-select="onLayoutSelect"
```

#### Example 2
Source: `sw-category/component/sw-category-entry-point-modal/sw-category-entry-point-modal.html.twig`
```twig
    <sw-cms-list-item
        class="sw-category-entry-point-modal__layout-item"
        :page="selectedSalesChannel.homeCmsPage"
        :disabled="!acl.can('category.editor') || undefined"
        active
    />
</div>
{% endblock %}

{% block sw_category_entry_point_modal_layout_modal %}
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :pre-selection="selectedSalesChannel.homeCmsPage"
    :cms-page-types="pageTypes"
    @modal-layout-select="onLayoutSelect"
```

#### Example 3
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
<sw-cms-list-item
    v-for="(cmsPage, index) in pages"
    :key="cmsPage.id"
    :class="'sw-cms-list-item--' + index"
    :page="cmsPage"
    :active="layoutIsLinked(cmsPage.id)"
    :is-default="[defaultProductId, defaultCategoryId].includes(cmsPage.id)"
    @item-click="onListItemClick"
    @preview-image-change="onPreviewChange"
    @cms-page-delete="onDeleteCmsPage"
>
    <template #contextMenu>
        <sw-context-button class="sw-cms-list-item__options">
            {% block sw_cms_list_listing_list_item_option_add_preview %}
            <sw-context-menu-item
```

#### Example 4
Source: `sw-cms/component/sw-cms-layout-modal/sw-cms-layout-modal.html.twig`
```twig
            <sw-cms-list-item
                :page="cmsPage"
                :is-default="[defaultProductId, defaultCategoryId].includes(cmsPage.id)"
                @element-click="selectItem(cmsPage)"
                @item-click="selectItem(cmsPage)"
            />
            {% endblock %}

            {% endblock %}
        </div>
    </sw-container>

    {% block sw_cms_layout_modal_content_pagination %}
    <sw-pagination
        class="sw-cms-layout-modal__content-pagination"
```

#### Example 5
Source: `sw-custom-entity/component/sw-generic-cms-page-assignment/sw-generic-cms-page-assignment.html.twig`
```twig
<sw-cms-list-item
    active
    :page="cmsPage"
    @on-item-click="openLayoutModal"
/>

<div class="sw-generic-cms-page-assignment__page-selection">
    <div class="sw-generic-cms-page-assignment__page-selection-info">
        <div
            class="sw-generic-cms-page-assignment__page-selection-headline"
            :class="{ 'is--empty': !cmsPage }"
        >
            {{ cmsPage ? cmsPage.name : $tc('sw-category.base.cms.defaultTitle') }}
        </div>
        <div
```

## sw-cms-list

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadGridUserSettings` | |
| `updateLimit` | |
| `saveGridUserSettings` | |
| `setPageContext` | |
| `getList` | |
| `addLinkedLayoutsAggregation` | |
| `showDefaultLayoutContextMenu` | |
| `getDefaultLayouts` | |
| `onOpenLayoutSetAsDefault` | |
| `onCloseLayoutSetAsDefault` | |
| `onConfirmLayoutSetAsDefault` | |
| `layoutIsLinked` | |
| `resetList` | |
| `getDefaultFolderId` | |
| `onChangeLanguage` | |
| `onListItemClick` | |
| `onSortingChanged` | |
| `onSearch` | |
| `onSortPageType` | |
| `onPageChange` | |
| `onCreateNewLayout` | |
| `onListModeChange` | |
| `onPreviewChange` | |
| `onPreviewImageRemove` | |
| `onModalClose` | |
| `onPreviewImageChange` | |
| `onRenameCmsPage` | |
| `onCloseRenameModal` | |
| `onConfirmPageRename` | |
| `onDeleteCmsPage` | |
| `onDuplicateCmsPage` | |
| `onCloseDeleteModal` | |
| `onConfirmPageDelete` | |
| `saveCmsPage` | |
| `deleteCmsPage` | |
| `getColumnConfig` | |
| `deleteDisabledToolTip` | |
| `getPageType` | |
| `getPageCategoryCount` | |
| `getPageProductCount` | |
| `getPageLandingPageCount` | |
| `getPageCount` | |
| `getPages` | |
| `getPagesString` | |
| `getPagesTooltip` | |
| `optionContextDeleteDisabled` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pageRepository` | |
| `defaultFolderRepository` | |
| `columnConfig` | |
| `sortPageTypes` | |
| `listCriteria` | |
| `associatedCategoryBuckets` | |
| `associatedProductBuckets` | |
| `isLinkedCriteria` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
    <sw-cms-list-item
        :page="cmsPage"
        :disabled="!acl.can('category.editor')"
        active
    />
</div>
{% endblock %}

{% block sw_category_detail_layout_modal %}
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :cms-page-types="pageTypes"
    :headline="headline"
    :pre-selection="cmsPage"
    @modal-layout-select="onLayoutSelect"
```

#### Example 2
Source: `sw-category/component/sw-category-entry-point-modal/sw-category-entry-point-modal.html.twig`
```twig
    <sw-cms-list-item
        class="sw-category-entry-point-modal__layout-item"
        :page="selectedSalesChannel.homeCmsPage"
        :disabled="!acl.can('category.editor') || undefined"
        active
    />
</div>
{% endblock %}

{% block sw_category_entry_point_modal_layout_modal %}
<sw-cms-layout-modal
    v-if="showLayoutSelectionModal"
    :pre-selection="selectedSalesChannel.homeCmsPage"
    :cms-page-types="pageTypes"
    @modal-layout-select="onLayoutSelect"
```

#### Example 3
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
<sw-cms-list-item
    v-for="(cmsPage, index) in pages"
    :key="cmsPage.id"
    :class="'sw-cms-list-item--' + index"
    :page="cmsPage"
    :active="layoutIsLinked(cmsPage.id)"
    :is-default="[defaultProductId, defaultCategoryId].includes(cmsPage.id)"
    @item-click="onListItemClick"
    @preview-image-change="onPreviewChange"
    @cms-page-delete="onDeleteCmsPage"
>
    <template #contextMenu>
        <sw-context-button class="sw-cms-list-item__options">
            {% block sw_cms_list_listing_list_item_option_add_preview %}
            <sw-context-menu-item
```

#### Example 4
Source: `sw-cms/component/sw-cms-layout-modal/sw-cms-layout-modal.html.twig`
```twig
            <sw-cms-list-item
                :page="cmsPage"
                :is-default="[defaultProductId, defaultCategoryId].includes(cmsPage.id)"
                @element-click="selectItem(cmsPage)"
                @item-click="selectItem(cmsPage)"
            />
            {% endblock %}

            {% endblock %}
        </div>
    </sw-container>

    {% block sw_cms_layout_modal_content_pagination %}
    <sw-pagination
        class="sw-cms-layout-modal__content-pagination"
```

#### Example 5
Source: `sw-custom-entity/component/sw-generic-cms-page-assignment/sw-generic-cms-page-assignment.html.twig`
```twig
<sw-cms-list-item
    active
    :page="cmsPage"
    @on-item-click="openLayoutModal"
/>

<div class="sw-generic-cms-page-assignment__page-selection">
    <div class="sw-generic-cms-page-assignment__page-selection-info">
        <div
            class="sw-generic-cms-page-assignment__page-selection-headline"
            :class="{ 'is--empty': !cmsPage }"
        >
            {{ cmsPage ? cmsPage.name : $tc('sw-category.base.cms.defaultTitle') }}
        </div>
        <div
```

## sw-cms-mapping-field

> Shopware Administration component.

- [Slots](#slots)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| config | `any` | — | yes |  |
| valueTypes | `null \| null` | `'string'` | no |  |
| entity | `any` | `null` | no |  |
| label | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| preview | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateMappingTypes` | |
| `updateDemoValue` | |
| `onMappingSelect` | |
| `onMappingRemove` | |
| `getAllowedMappingTypes` | |
| `getDemoValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isMapped` | |
| `hasPreview` | |
| `cmsPageState` | |

### Examples

#### Example 1
Source: `sw-cms/elements/video/config/sw-cms-el-config-video.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.media"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        file-accept="video/*"
```

#### Example 2
Source: `sw-cms/elements/youtube-video/config/sw-cms-el-config-youtube-video.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.previewMedia"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
```

#### Example 3
Source: `sw-cms/elements/image/config/sw-cms-el-config-image.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.media"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$t('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
```

#### Example 4
Source: `sw-cms/elements/vimeo-video/config/sw-cms-el-config-vimeo-video.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.previewMedia"
    value-types="entity"
    entity="media"
    :disabled="isInherited"
>
    <sw-media-upload-v2
        variant="regular"
        :upload-tag="uploadTag"
        :source="previewSource"
        :allow-multi-select="false"
        :default-folder="cmsPageState.pageEntityName"
        :caption="$tc('sw-cms.elements.general.config.caption.mediaUpload')"
        :disabled="isInherited"
        @media-upload-sidebar-open="onOpenMediaModal"
```

#### Example 5
Source: `sw-cms/elements/text/config/sw-cms-el-config-text.html.twig`
```twig
<sw-cms-mapping-field
    v-model:config="element.config.content"
    value-types="string"
    :disabled="isInherited"
>
    <sw-text-editor
        v-if="!feature.isActive('METEOR_TEXT_EDITOR')"
        :key="isInherited"
        :value="element.config.content.value"
        :disabled="isInherited"
        :allow-inline-data-mapping="true"
        :sanitize-info-warn="true"
        enable-transparent-background
        @update:value="onInput"
        @blur="onBlur"
```

## sw-cms-missing-element-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| missingElements | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| modal-save | — | |
| modal-dont-remind-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `onSave` | |
| `onChangeDontRemindCheckbox` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `element` | |
| `title` | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
                <sw-cms-missing-element-modal
                    v-if="showMissingElementModal"
                    :missing-elements="missingElements"
                    @modal-close="onCloseMissingElementModal"
                    @modal-save="onSaveMissingElementModal"
                    @modal-dont-remind-change="onChangeDontRemindCheckbox"
                />
                {% endblock %}
            </div>
            {% endblock %}
        </div>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}
```

## sw-cms-page-form

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |
| elementUpdate | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `sortSlots` | |
| `initVisibility` | |
| `getBlockTitle` | |
| `displaySectionType` | |
| `getSectionName` | |
| `getSectionPosition` | |
| `getDeviceActive` | |
| `displayNotification` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cmsBlocks` | |
| `cmsElements` | |
| `slotPositions` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-cms/sw-category-detail-cms.html.twig`
```twig
    <sw-cms-page-form
        v-if="cmsPage && acl.can('category.editor')"
        :page="cmsPage"
    />
    {% endblock %}

</div>
{% endblock %}

```

#### Example 2
Source: `sw-category/view/sw-landing-page-detail-cms/sw-landing-page-detail-cms.html.twig`
```twig
    <sw-cms-page-form
        v-if="cmsPage"
        :page="cmsPage"
    />
    {% endblock %}

</div>
{% endblock %}

```

#### Example 3
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
    <sw-cms-page-form
        v-if="!isLoading"
        :page="page"
    />
</div>
{% endblock %}

{% block sw_cms_detail_stage_wrapper %}
<div
    v-else
    class="sw-cms-detail__stage"
>

    {% block sw_cms_detail_toolbar_notification %}
    {% block sw_cms_detail_toolbar_notification_errors %}
```

#### Example 4
Source: `sw-custom-entity/component/sw-generic-cms-page-assignment/sw-generic-cms-page-assignment.html.twig`
```twig
    <sw-cms-page-form
        v-if="cmsPage"
        :page="cmsPage"
    />

    <sw-cms-layout-modal
        v-if="showLayoutSelection"
        :cms-page-types="allowedPageTypes"
        :pre-selection="cmsPage"
        @modal-layout-select="onLayoutSelect"
        @modal-close="closeLayoutModal"
    />
</div>
{% endblock %}

```

#### Example 5
Source: `sw-product/view/sw-product-detail-layout/sw-product-detail-layout.html.twig`
```twig
        <sw-cms-page-form
            v-if="showCmsForm"
            :page="currentPage"
            :element-update="elementUpdate"
        />

        <mt-card
            v-else
            class="sw-product-detail-layout__no-config"
            position-identifier="sw-product-detail-layout-no-config"
            :is-loading="isConfigLoading"
        >
            <p>{{ $tc('sw-product.layout.textNoConfig') }}</p>
        </mt-card>
        {% endblock %}
```

## sw-cms-page-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| pageType | `any` | — | yes |  |
| value | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getTranslations` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `bind` | |
| `translations` | |
| `pageTypeCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-cms-page-select
    pageType="..."
>
    <!-- content -->
</sw-cms-page-select>
```

## sw-cms-preview-category-navigation

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-category-navigation>
    <!-- content -->
</sw-cms-preview-category-navigation>
```

## sw-cms-preview-center-text

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-center-text>
    <!-- content -->
</sw-cms-preview-center-text>
```

## sw-cms-preview-cross-selling

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-cross-selling>
    <!-- content -->
</sw-cms-preview-cross-selling>
```

## sw-cms-preview-form

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-form>
    <!-- content -->
</sw-cms-preview-form>
```

## sw-cms-preview-gallery-buybox

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-gallery-buybox>
    <!-- content -->
</sw-cms-preview-gallery-buybox>
```

## sw-cms-preview-html

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-html>
    <!-- content -->
</sw-cms-preview-html>
```

## sw-cms-preview-image-bubble-row

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-bubble-row>
    <!-- content -->
</sw-cms-preview-image-bubble-row>
```

## sw-cms-preview-image-cover

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-cover>
    <!-- content -->
</sw-cms-preview-image-cover>
```

## sw-cms-preview-image-four-column

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-four-column>
    <!-- content -->
</sw-cms-preview-image-four-column>
```

## sw-cms-preview-image-gallery

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-gallery>
    <!-- content -->
</sw-cms-preview-image-gallery>
```

## sw-cms-preview-image-highlight-row

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-highlight-row>
    <!-- content -->
</sw-cms-preview-image-highlight-row>
```

## sw-cms-preview-image-simple-grid

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-simple-grid>
    <!-- content -->
</sw-cms-preview-image-simple-grid>
```

## sw-cms-preview-image-slider

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-cms/blocks/image/image-gallery/preview/sw-cms-preview-image-gallery.html.twig`
```twig
<sw-cms-preview-image-slider />
```

## sw-cms-preview-image-text-bubble

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-text-bubble>
    <!-- content -->
</sw-cms-preview-image-text-bubble>
```

## sw-cms-preview-image-text-cover

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-text-cover>
    <!-- content -->
</sw-cms-preview-image-text-cover>
```

## sw-cms-preview-image-text-gallery

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-text-gallery>
    <!-- content -->
</sw-cms-preview-image-text-gallery>
```

## sw-cms-preview-image-text-row

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-text-row>
    <!-- content -->
</sw-cms-preview-image-text-row>
```

## sw-cms-preview-image-text

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-text>
    <!-- content -->
</sw-cms-preview-image-text>
```

## sw-cms-preview-image-three-column

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-three-column>
    <!-- content -->
</sw-cms-preview-image-three-column>
```

## sw-cms-preview-image-three-cover

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-three-cover>
    <!-- content -->
</sw-cms-preview-image-three-cover>
```

## sw-cms-preview-image-two-column

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-image-two-column>
    <!-- content -->
</sw-cms-preview-image-two-column>
```

## sw-cms-preview-image

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-cms/blocks/image/image-gallery/preview/sw-cms-preview-image-gallery.html.twig`
```twig
<sw-cms-preview-image-slider />
```

## sw-cms-preview-product-description-reviews

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-product-description-reviews>
    <!-- content -->
</sw-cms-preview-product-description-reviews>
```

## sw-cms-preview-product-heading

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-product-heading>
    <!-- content -->
</sw-cms-preview-product-heading>
```

## sw-cms-preview-product-listing

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-product-listing>
    <!-- content -->
</sw-cms-preview-product-listing>
```

## sw-cms-preview-product-slider

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-product-slider>
    <!-- content -->
</sw-cms-preview-product-slider>
```

## sw-cms-preview-product-three-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-product-three-column>
    <!-- content -->
</sw-cms-preview-product-three-column>
```

## sw-cms-preview-sidebar-filter

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-sidebar-filter>
    <!-- content -->
</sw-cms-preview-sidebar-filter>
```

## sw-cms-preview-text-hero

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-text-hero>
    <!-- content -->
</sw-cms-preview-text-hero>
```

## sw-cms-preview-text-on-image

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-text-on-image>
    <!-- content -->
</sw-cms-preview-text-on-image>
```

## sw-cms-preview-text-teaser-section

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-text-teaser-section>
    <!-- content -->
</sw-cms-preview-text-teaser-section>
```

## sw-cms-preview-text-teaser

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-text-teaser>
    <!-- content -->
</sw-cms-preview-text-teaser>
```

## sw-cms-preview-text-three-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-text-three-column>
    <!-- content -->
</sw-cms-preview-text-three-column>
```

## sw-cms-preview-text-two-column

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-text-two-column>
    <!-- content -->
</sw-cms-preview-text-two-column>
```

## sw-cms-preview-text

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-cms-preview-text>
    <!-- content -->
</sw-cms-preview-text>
```

## sw-cms-preview-video

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-video>
    <!-- content -->
</sw-cms-preview-video>
```

## sw-cms-preview-vimeo-video

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-vimeo-video>
    <!-- content -->
</sw-cms-preview-vimeo-video>
```

## sw-cms-preview-youtube-video

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-cms-preview-youtube-video>
    <!-- content -->
</sw-cms-preview-youtube-video>
```

## sw-cms-product-assignment

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| select | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| after-item-list | — | |
| `column-${column.property}` | — | |
| empty-state | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| paginate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initData` | |
| `searchItems` | |
| `onItemSelect` | |
| `removeItem` | |
| `onSelectCollapsed` | |
| `paginateGrid` | |
| `removeFromGrid` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
<sw-cms-product-assignment
    class="sw-cms-layout-assignment-modal__product-select"
    :local-mode="true"
    :entity-collection="page.products"
    :columns="productColumns"
    :criteria="productCriteria"
    :select-label="$tc('sw-cms.components.cmsLayoutAssignmentModal.products.productAssignmentLabel')"
    :placeholder="$tc('sw-cms.components.cmsLayoutAssignmentModal.products.productAssignmentPlaceholder')"
>
    {% block sw_cms_layout_assignment_modal_product_detail_pages_column_name %}
    <template #column-name="{ item, column }">
        <router-link
            :to="{ name: column.routerLink, params: { id: item.id } }"
        >
            <sw-product-variant-info
```

## sw-cms-product-box-preview

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| hasText | `any` | — | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-cms/blocks/commerce/product-listing/preview/sw-cms-preview-product-listing.html.twig`
```twig
<sw-cms-product-box-preview has-text />
```

#### Example 2
Source: `sw-cms/blocks/commerce/product-listing/preview/sw-cms-preview-product-listing.html.twig`
```twig
<sw-cms-product-box-preview has-text />
```

#### Example 3
Source: `sw-cms/blocks/commerce/product-three-column/preview/sw-cms-preview-product-three-column.html.twig`
```twig
<sw-cms-product-box-preview has-text />
```

#### Example 4
Source: `sw-cms/blocks/commerce/product-three-column/preview/sw-cms-preview-product-three-column.html.twig`
```twig
<sw-cms-product-box-preview has-text />
```

#### Example 5
Source: `sw-cms/blocks/commerce/product-slider/preview/sw-cms-preview-product-slider.html.twig`
```twig
<sw-cms-product-box-preview has-text />
```

## sw-cms-reset-inheritance

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `resetSlotOverrides` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cmsPageStore` | |
| `hasOverrides` | |

### Examples

#### Example 1
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
<sw-cms-reset-inheritance />
```

#### Example 2
Source: `sw-product/component/sw-product-layout-assignment/sw-product-layout-assignment.html.twig`
```twig
<sw-cms-reset-inheritance v-if="product" />
```

## sw-cms-section-actions

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| section | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `selectSection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `componentClasses` | |
| `cmsPageStateStore` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-section-actions
    :section="section"
    :disabled="disabled || undefined"
/>
{% endblock %}

<div
    class="sw-cms-section__wrapper"
    :style="sectionStyles"
>
    <sw-cms-visibility-toggle
        v-if="isVisible"
        :text="toggleButtonText"
        :is-collapsed="isCollapsed"
        :class="expandedClass"
```

## sw-cms-section-config

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| section | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| section-delete | — | |
| section-duplicate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSetBackgroundMedia` | |
| `successfulUpload` | |
| `removeMedia` | |
| `onSectionDelete` | |
| `onSectionDuplicate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `uploadTag` | |
| `mediaRepository` | |
| `cmsPageState` | |
| `quickactionsDisabled` | |
| `quickactionClasses` | |
| `sizingModeOptions` | |
| `mobileBehaviorOptions` | |
| `backgroundMediaModeOptions` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-section-config
                        :section="selectedSection"
                        @section-duplicate="onSectionDuplicate"
                        @section-delete="onSectionDelete"
                    />
                </template>
                {% endblock %}
            </sw-sidebar-collapse>

            <sw-sidebar-collapse :expand-on-loading="false">
                <template #header>
                    <span>{{ $tc('sw-cms.sidebar.contentMenu.visibilitySettings') }}</span>
                </template>
                <template #content>
                    <sw-cms-visibility-config
```

## sw-cms-section

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |
| section | `any` | — | yes |  |
| active | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-config-open | — | |
| block-duplicate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `openBlockBar` | |
| `emitPageConfigOpen` | |
| `onAddSectionBlock` | |
| `onBlockSelection` | |
| `onBlockDuplicate` | |
| `onBlockDelete` | |
| `updateBlockPositions` | |
| `getDropData` | |
| `blockTypeExists` | |
| `hasBlockErrors` | |
| `hasUniqueBlockErrors` | |
| `hasSlotConfigErrors` | |
| `toggleVisibility` | |
| `getBlockComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `blockRepository` | |
| `slotRepository` | |
| `sectionClasses` | |
| `sectionTypeClass` | |
| `customSectionClass` | |
| `sectionStyles` | |
| `sectionSidebarClasses` | |
| `sectionMobileAndHidden` | |
| `isSideBarType` | |
| `sideBarEmpty` | |
| `blockCount` | |
| `mainContentEmpty` | |
| `sideBarBlocks` | |
| `mainContentBlocks` | |
| `assetFilter` | |
| `blockTypes` | |
| `isVisible` | |
| `toggleButtonText` | |
| `expandedClass` | |
| `sectionContentClasses` | |
| `pageSlotsError` | |
| `pageSlotConfigError` | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
                <sw-cms-section
                    class="sw-cms-stage-section"
                    :page="page"
                    :section="section"
                    :active="selectedSection !== null && selectedSection.id === section.id"
                    :disabled="!acl.can('cms.editor') || undefined"
                    @page-config-open="pageConfigOpen"
                    @block-duplicate="onBlockDuplicate"
                />
                {% endblock %}
            </template>
        </template>
        {% endblock %}

        {% block sw_cms_detail_stage_add_last_section %}
```

#### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-section-actions
    :section="section"
    :disabled="disabled || undefined"
/>
{% endblock %}

<div
    class="sw-cms-section__wrapper"
    :style="sectionStyles"
>
    <sw-cms-visibility-toggle
        v-if="isVisible"
        :text="toggleButtonText"
        :is-collapsed="isCollapsed"
        :class="expandedClass"
```

#### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-section-config
                        :section="selectedSection"
                        @section-duplicate="onSectionDuplicate"
                        @section-delete="onSectionDelete"
                    />
                </template>
                {% endblock %}
            </sw-sidebar-collapse>

            <sw-sidebar-collapse :expand-on-loading="false">
                <template #header>
                    <span>{{ $tc('sw-cms.sidebar.contentMenu.visibilitySettings') }}</span>
                </template>
                <template #content>
                    <sw-cms-visibility-config
```

## sw-cms-sidebar-nav-element

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| block | `any` | — | yes |  |
| removable | `any` | — | no |  |
| duplicable | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| block-duplicate | — | |
| block-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onBlockDuplicate` | |
| `onBlockDelete` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
        <sw-cms-sidebar-nav-element
            v-draggable="getDragData(block, sectionIndex)"
            v-droppable="getDropData(block, sectionIndex)"
            :block="block"
            class="sw-cms-sidebar__navigator-block"
            :removable="blockIsRemovable(block)"
            :duplicable="blockIsDuplicable(block)"
            :class="{ 'is--dragging': block.isDragging }"
            @block-delete="onBlockDelete($event, section)"
            @block-duplicate="onBlockDuplicate($event, section)"
        />
    </template>
    {% endblock %}
</template>

```

#### Example 2
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-sidebar-nav-element
                        v-draggable="getDragData(block, sectionIndex)"
                        v-droppable="getDropData(block, sectionIndex)"
                        :block="block"
                        :removable="blockIsRemovable(block)"
                        class="sw-cms-sidebar__navigator-block is--sidebar"
                        :class="{ 'is--dragging': block.isDragging }"
                        @block-delete="onBlockDelete($event, section)"
                        @block-duplicate="onBlockDuplicate($event, section)"
                    />
                </template>
                {% endblock %}
            </template>

            <template v-else>
```

## sw-cms-sidebar

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| page | `any` | — | yes |  |
| demoEntity | `any` | `null` | no |  |
| demoEntityIdProp | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| isDefaultLayout | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-type-change | — | |
| demo-entity-change | — | |
| page-save | — | |
| block-stage-drop | — | |
| current-block-change | — | |
| section-duplicate | — | |
| block-duplicate | — | |
| page-update | — | |
| open-layout-assignment | — | |
| open-layout-set-as-default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onPageTypeChange` | |
| `onDemoEntityChange` | |
| `onCloseBlockConfig` | |
| `isDisabledPageType` | |
| `openSectionSettings` | |
| `blockIsRemovable` | |
| `blockIsUnique` | |
| `blockIsDuplicable` | |
| `sectionIsDuplicable` | |
| `onBlockDragSort` | |
| `refreshPosition` | |
| `onSidebarNavigatorClick` | |
| `onSidebarNavigationConfirm` | |
| `onSidebarNavigationCancel` | |
| `getDragData` | |
| `getDropData` | |
| `onBlockDragStop` | |
| `onBlockDropAbort` | |
| `onBlockStageDrop` | |
| `moveSectionUp` | |
| `moveSectionDown` | |
| `onSectionDuplicate` | |
| `onSectionDelete` | |
| `onBlockDelete` | |
| `onBlockDuplicate` | |
| `onRemoveSectionBackgroundMedia` | |
| `onSetSectionBackgroundMedia` | |
| `onToggleBlockFavorite` | |
| `successfulUpload` | |
| `uploadTag` | |
| `getMainContentBlocks` | |
| `getSidebarContentBlocks` | |
| `pageUpdate` | |
| `onOpenLayoutAssignment` | |
| `onOpenLayoutSetAsDefault` | |
| `blockTypeExists` | |
| `onVisibilityChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pageTypes` | |
| `pageTypesOptions` | |
| `blockRepository` | |
| `slotRepository` | |
| `cmsBlocks` | |
| `cmsBlockCategories` | |
| `cmsBlockCategoriesOptions` | |
| `mediaRepository` | |
| `addBlockTitle` | |
| `pageSections` | |
| `sidebarItemSettings` | |
| `tooltipDisabled` | |
| `demoCriteria` | |
| `demoContext` | |
| `blockTypes` | |
| `pageConfigErrors` | |
| `hasPageConfigErrors` | |
| `showDefaultLayoutSelection` | |
| `cmsBlocksBySelectedBlockCategory` | |
| `isLayoutAssignmentDisabled` | |
| `pageNameError` | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
<sw-cms-sidebar
    ref="cmsSidebar"
    :page="page"
    :demo-entity="currentMappingEntity"
    :demo-entity-id-prop="demoEntityId"
    :disabled="!acl.can('cms.editor') || undefined"
    :is-default-layout="isDefaultLayout"
    @demo-entity-change="onDemoEntityChange"
    @block-duplicate="onBlockDuplicate"
    @section-duplicate="onSectionDuplicate"
    @block-stage-drop="onPageUpdate"
    @page-type-change="onPageTypeChange"
    @page-update="onPageUpdate"
    @page-save="onPageSave"
    @open-layout-assignment="onOpenLayoutAssignment"
```

#### Example 2
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
        <sw-cms-sidebar-nav-element
            v-draggable="getDragData(block, sectionIndex)"
            v-droppable="getDropData(block, sectionIndex)"
            :block="block"
            class="sw-cms-sidebar__navigator-block"
            :removable="blockIsRemovable(block)"
            :duplicable="blockIsDuplicable(block)"
            :class="{ 'is--dragging': block.isDragging }"
            @block-delete="onBlockDelete($event, section)"
            @block-duplicate="onBlockDuplicate($event, section)"
        />
    </template>
    {% endblock %}
</template>

```

#### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-sidebar-nav-element
                        v-draggable="getDragData(block, sectionIndex)"
                        v-droppable="getDropData(block, sectionIndex)"
                        :block="block"
                        :removable="blockIsRemovable(block)"
                        class="sw-cms-sidebar__navigator-block is--sidebar"
                        :class="{ 'is--dragging': block.isDragging }"
                        @block-delete="onBlockDelete($event, section)"
                        @block-duplicate="onBlockDuplicate($event, section)"
                    />
                </template>
                {% endblock %}
            </template>

            <template v-else>
```

## sw-cms-slot

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| element | `any` | — | yes |  |
| active | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `onSettingsButtonClick` | |
| `onCloseSettingsModal` | |
| `onElementButtonClick` | |
| `onCloseElementModal` | |
| `onSelectElement` | |
| `onToggleElementFavorite` | |
| `toggleHoverElement` | |
| `getFavoriteIconToggleState` | |
| `elementInElementGroup` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `slotElementId` | |
| `cmsServiceState` | |
| `elementConfig` | |
| `elementModalTitle` | |
| `cmsElements` | |
| `groupedCmsElements` | |
| `componentClasses` | |
| `cmsSlotSettingsClasses` | |
| `tooltipDisabled` | |
| `modalVariant` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
                        <sw-cms-slot
                            :element="el"
                            :disabled="disabled || undefined"
                            :active="selectedBlock !== null && selectedBlock.id === block.id"
                        />
                    </template>
                    {% endblock %}
                </component>
                {% endblock %}
            </sw-cms-block>
            {% endblock %}

            {% block sw_cms_section_add_sidebar_block %}
            <sw-cms-stage-add-block
                v-if="isSystemDefaultLanguage && !disabled"
```

#### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
                                <sw-cms-slot
                                    :element="el"
                                    :disabled="disabled || undefined"
                                    :active="selectedBlock !== null && selectedBlock.id === block.id"
                                />
                            </template>
                            {% endblock %}
                        </component>
                        {% endblock %}
                    </sw-cms-block>
                    {% endblock %}

                    {% block sw_cms_section_add_content_block %}
                    <sw-cms-stage-add-block
                        v-if="isSystemDefaultLanguage && !disabled"
```

## sw-cms-stage-add-block

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| stage-block-add | — | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-stage-add-block
    v-if="isSystemDefaultLanguage && !disabled"
    :key="0"
    v-droppable="{ dragGroup: 'cms-stage', data: getDropData(0, 'sidebar') }"
    @stage-block-add="onAddSectionBlock"
/>
{% endblock %}

<template
    v-for="(block, index) in sideBarBlocks"
    :key="block.id"
>
    {% block sw_cms_section_sidebar_block %}
    <sw-cms-block
        class="sw-cms-stage-block"
```

#### Example 2
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
            <sw-cms-stage-add-block
                v-if="isSystemDefaultLanguage && !disabled"
                :key="index + 1"
                v-droppable="{ dragGroup: 'cms-stage', data: getDropData(block.position + 1, 'sidebar') }"
                @stage-block-add="onAddSectionBlock"
            />
            {% endblock %}
        </template>
    </template>
</div>
{% endblock %}

{% block sw_cms_section_content %}
<div
    v-if="!isCollapsed || !isVisible"
```

## sw-cms-stage-add-section

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| forceChoose | `any` | — | no |  |
| disabled | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| stage-section-add | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onAddSection` | |
| `toggleSelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `componentClasses` | |

### Examples

#### Example 1
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

#### Example 2
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

## sw-cms-stage-section-selection

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| section-select | — | |

### Methods

| Method | Description |
|--------|-------------|
| `selectSection` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-stage-add-section/sw-cms-stage-add-section.html.twig`
```twig
    <sw-cms-stage-section-selection
        v-if="showSelection"
        @section-select="onAddSection"
    />
    {% endblock %}

    {% block sw_cms_add_section_button %}
    <div
        v-if="!forceChoose"
        class="sw-cms-stage-add-section__button"
        :class="{ 'is--open': showSelection }"
        role="button"
        tabindex="0"
        @click="toggleSelection"
        @keydown.enter="toggleSelection"
```

#### Example 2
Source: `sw-cms/component/sw-cms-create-wizard/sw-cms-create-wizard.html.twig`
```twig
<sw-cms-stage-section-selection @section-select="onSectionSelect" />
```

## sw-cms-toolbar

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| tools | — | |
| language-switch | — | |
| actions | — | |
| sidebar | — | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
<sw-cms-toolbar>
    {% block sw_cms_detail_toolbar_language_switch %}
    <template #language-switch>
        <sw-language-switch
            :disabled="isLoading || page.locked || undefined"
            :allow-edit="acl.can('cms.editor')"
            :save-changes-function="saveOnLanguageChange"
            :abort-change-function="abortOnLanguageChange"
            @on-change="onChangeLanguage"
        />
    </template>
    {% endblock %}

    {% block sw_cms_detail_toolbar_title %}
    <template #title>
```

## sw-cms-visibility-config

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| visibility | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `onVisibilityChange` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                <sw-cms-visibility-config
                    class="sw-cms-sidebar__visibility-config-block"
                    :visibility="selectedBlock.visibility"
                    @visibility-change="(viewport, isVisible) => onVisibilityChange(selectedBlock, viewport, isVisible)"
                />
            </template>
        </sw-sidebar-collapse>
    </template>
</div>
{% endblock %}

{% block sw_cms_sidebar_section_settings %}
<div class="sw-cms-sidebar__section-settings">
    <template v-if="selectedSection !== null">

```

#### Example 2
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
                    <sw-cms-visibility-config
                        class="sw-cms-sidebar__visibility-config-section"
                        :visibility="selectedSection.visibility"
                        @visibility-change="(viewport, isVisible) => onVisibilityChange(selectedSection, viewport, isVisible)"
                    />
                </template>
            </sw-sidebar-collapse>
            {% endblock %}
        </template>
    </div>
    {% endblock %}
</sw-sidebar-item>
{% endblock %}

{% block sw_cms_sidebar_navigator %}
```

## sw-cms-visibility-toggle

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | — | yes |  |
| isCollapsed | `any` | — | yes |  |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-section/sw-cms-section.html.twig`
```twig
<sw-cms-visibility-toggle
    v-if="isVisible"
    :text="toggleButtonText"
    :is-collapsed="isCollapsed"
    :class="expandedClass"
    @toggle="toggleVisibility"
/>
{% block sw_cms_section_sidebar %}
<div
    v-if="isSideBarType && (!isCollapsed || !isVisible)"
    class="sw-cms-section__sidebar"
    :class="sectionSidebarClasses"
>

    <template v-if="sideBarEmpty">
```

#### Example 2
Source: `sw-cms/component/sw-cms-block/sw-cms-block.html.twig`
```twig
<sw-cms-visibility-toggle
    v-if="isVisible"
    :text="toggleButtonText"
    :is-collapsed="isCollapsed"
    :class="expandedClass"
    @toggle="toggleVisibility"
/>
{% block sw_cms_block_content %}
<div
    v-if="!isCollapsed || !isVisible"
    class="sw-cms-block__content"
    :class="expandedClass"
    :style="blockPadding"
>
    <slot>
```

## sw-code-editor

> Code editor component with syntax highlighting (based on Ace editor).

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| label | `any` | `''` | no |  |
| completerFunction | `any` | `null` | no |  |
| editorConfig | `any` | — | no |  |
| completionMode | `any` | `'text'` | no | Valid: `entity`, `text` |
| mode | `any` | `'twig'` | no | Valid: `twig`, `text` |
| softWraps | `any` | `true` | no |  |
| setFocus | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| sanitizeInfoWarn | `any` | `false` | no |  |
| sanitizeInput | `any` | `false` | no |  |
| sanitizeFieldName | `any` | `null` | no |  |
| error | `any` | `null` | no |  |
| placeholder | `any` | `''` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| mounted | — | |
| update:value | — | |
| blur | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `beforeUnmountedComponent` | |
| `destroyedComponent` | |
| `onInput` | |
| `onBlur` | |
| `sanitizeEditorInput` | |
| `defineAutocompletion` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `aceConfig` | |
| `classes` | |
| `enableHtmlSanitizer` | |
| `attrsWithoutClass` | |

### Examples

#### Example 1
Source: `sw-cms/blocks/html/html/preview/sw-cms-preview-html.html.twig`
```twig
    <sw-code-editor
        v-model:value="demoValue"
        :disabled="true"
        :editor-config="editorConfig"
    />
</div>
{% endblock %}

```

#### Example 2
Source: `sw-cms/elements/html/config/sw-cms-el-config-html.html.twig`
```twig
            <sw-code-editor
                v-model:value="element.config.content.value"
                :disabled="isInherited"
                :set-focus="true"
                @update:value="onInput"
                @blur="onBlur"
            />
        </template>
    </sw-cms-inherit-wrapper>

    <mt-banner variant="attention">
        {{ $t('sw-cms.elements.html.config.warning') }}
    </mt-banner>
</div>
{% endblock %}
```

#### Example 3
Source: `sw-cms/elements/html/component/sw-cms-el-html.html.twig`
```twig
    <sw-code-editor
        v-model:value="element.config.content.value"
        :disabled="true"
        :editor-config="editorConfig"
    />
</div>
{% endblock %}

```

#### Example 4
Source: `sw-cms/elements/html/preview/sw-cms-el-preview-html.html.twig`
```twig
    <sw-code-editor
        v-model:value="demoValue"
        :disabled="true"
        :editor-config="editorConfig"
    />
</div>
{% endblock %}

```

#### Example 5
Source: `sw-flow/component/modals/sw-flow-create-mail-template-modal/sw-flow-create-mail-template-modal.html.twig`
```twig
<sw-code-editor
    ref="plainEditor"
    :key="`${mailTemplate.mailTemplateTypeId}plain`"
    v-model:value="mailTemplate.contentPlain"
    class="sw-flow-create-mail-template-modal__content-plain"
    name="content_plain"
    completion-mode="entity"
    :label="$tc('sw-flow.modals.mail.labelContentPlain')"
    :placeholder="placeholder(mailTemplate, 'contentPlain', $tc('sw-flow.modals.mail.placeholderPlain'))"
    :completer-function="outerCompleterFunction"
    :editor-config="editorConfig"
    :error="mailTemplateContentPlainError"
    required
/>
{% endblock %}
```

## sw-collapse

> Collapsible content panel with animated expand/collapse.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| expandOnLoading | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header | — | |
| content | — | |

### Methods

| Method | Description |
|--------|-------------|
| `collapseItem` | |

### Examples

#### Example 1
Source: `sw-settings-language/page/sw-settings-language-list/sw-settings-language-list.html.twig`
```twig
<sw-collapse expand-on-loading>

    {% block sw_settings_language_list_grid_sidebar_filter_header %}
    <template #header="{ expanded }">
        <div class="sw-settings-language-list__collapse-header">

            {% block sw_settings_language_list_grid_sidebar_filter_header_title %}
            <h4 class="sw-settings-language-list__collapse-title">
                {{ $t('sw-settings-language.list.titleSidebarQuickFilter') }}
            </h4>
            {% endblock %}

            {% block sw_settings_language_list_grid_sidebar_filter_header_icon %}
            {% block sw_settings_language_list_grid_sidebar_filter_header_icon_expanded %}
            <mt-icon
```

## sw-color-badge

> Shopware Administration component.

- [Slots](#slots)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'default'` | no |  |
| color | `any` | `''` | no |  |
| rounded | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `colorStyle` | |
| `variantClass` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-activity/sw-import-export-activity.html.twig`
```twig
    <sw-color-badge
        v-if="item.state === 'failed'"
        variant="error"
        rounded
    />

    <sw-color-badge
        v-else-if="item.state === 'succeeded'"
        variant="success"
        rounded
    />

    <sw-color-badge
        v-else
        rounded
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-activity-result-modal/sw-import-export-activity-result-modal.html.twig`
```twig
        <sw-color-badge
            v-if="logEntity.state === 'failed'"
            class="sw-import-export-activity-result-modal__color-badge"
            variant="error"
            rounded
        />

        <sw-color-badge
            v-else-if="logEntity.state === 'succeeded'"
            class="sw-import-export-activity-result-modal__color-badge"
            variant="success"
            rounded
        />

        <sw-color-badge
```

#### Example 3
Source: `sw-import-export/component/sw-import-export-activity-log-info-modal/sw-import-export-activity-log-info-modal.html.twig`
```twig
        <sw-color-badge
            v-if="logEntity.state === 'failed'"
            class="sw-import-export-activity-log-info-modal__color-badge"
            variant="error"
            rounded
        />

        <sw-color-badge
            v-else-if="logEntity.state === 'succeeded'"
            class="sw-import-export-activity-log-info-modal__color-badge"
            variant="success"
            rounded
        />

        <sw-color-badge
```

#### Example 4
Source: `sw-settings-shopware-updates/view/sw-settings-shopware-updates-plugins/sw-shopware-updates-plugins.html.twig`
```twig
    <sw-color-badge
        v-if="item.statusVariant"
        :variant="item.statusVariant"
        :rounded="true"
    />
    <sw-color-badge
        v-else
        :color="item.statusColor"
        :rounded="true"
    />&nbsp;

    <template v-if="item.statusMessage === 'notCompatible'">
        {{ item.statusMessage }} {{ $t('sw-settings-shopware-updates.plugins.pluginWillBeDeactivatedHint') }}
    </template>
    <template v-else-if="item.statusMessage">
```

#### Example 5
Source: `sw-settings-shopware-updates/view/sw-settings-shopware-updates-requirements/sw-shopware-updates-requirements.html.twig`
```twig
                    <sw-color-badge
                        variant="success"
                        :rounded="true"
                    />&nbsp;
                    {{ $t('sw-settings-shopware-updates.requirements.ready') }}
                </template>

                <template v-else>
                    <sw-color-badge
                        variant="error"
                        :rounded="true"
                    />&nbsp;
                    {{ $t('sw-settings-shopware-updates.requirements.notReady') }}
                </template>
            </template>
```

## sw-colorpicker-deprecated

> **Deprecated in 6.7** — Use `mt-colorpicker` instead. Will be removed in 6.8.
> See mt-colorpicker for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-colorpicker>` | `<mt-colorpicker>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| colorOutput | `any` | `'auto'` | no | Valid: `auto`, `hex`, `hsl`, `rgb` |
| alpha | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| readonly | `any` | `false` | no |  |
| colorLabels | `any` | `true` | no |  |
| zIndex | `null \| null` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `componentBeforeDestroy` | |
| `debounceEmitColorValue` | |
| `outsideClick` | |
| `setOutsideClickEvent` | |
| `removeOutsideClickEvent` | |
| `toggleColorPicker` | |
| `moveSelector` | |
| `setDragging` | |
| `removeDragging` | |
| `setSingleRGBValue` | |
| `setHslaValues` | |
| `splitRGBValues` | |
| `splitHSLValues` | |
| `convertHSLtoRGB` | |
| `convertHSLtoHEX` | |
| `convertHSL` | |
| `convertRGBtoHSL` | |
| `convertHEXtoHSL` | |
| `onClickInput` | |
| `roundingFloat` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `colorValue` | |
| `integerAlpha` | |
| `sliderBackground` | |
| `isColorValid` | |
| `previewColorValue` | |
| `selectorBackground` | |
| `redValue` | |
| `greenValue` | |
| `blueValue` | |
| `rgbValue` | |
| `hslValue` | |
| `hexValue` | |
| `convertedValue` | |
| `selectorPositionX` | |
| `selectorPositionY` | |
| `selectorStyles` | |

### Examples

#### Basic Usage
```twig
<sw-colorpicker-deprecated>
    <!-- content -->
</sw-colorpicker-deprecated>
```

## sw-colorpicker

> **Migration wrapper** — Delegates to `mt-colorpicker` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-colorpicker for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `null \| null` | `null` | no |  |
| modelValue | `any` | — | no |  |
| deprecated | `any` | `false` | no |  |

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
| `currentValue` | |

### Examples

#### Basic Usage
```twig
<sw-colorpicker>
    <!-- content -->
</sw-colorpicker>
```

## sw-compact-colorpicker

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `emitColor` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `colorValue` | |

### Examples

#### Basic Usage
```twig
<sw-compact-colorpicker>
    <!-- content -->
</sw-compact-colorpicker>
```

## sw-condition-all-line-items-container

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| create-before | — | |
| create-after | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setConditionValue` | |
| `onAddPlaceholder` | |
| `unwrapCondition` | |
| `onInsertBefore` | |
| `onInsertAfter` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `children` | |
| `childType` | |
| `childrenLength` | |

### Examples

#### Basic Usage
```twig
<sw-condition-all-line-items-container>
    <!-- content -->
</sw-condition-all-line-items-container>
```

## sw-condition-and-container

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddPlaceholder` | |
| `onAddOrContainer` | |
| `onDeleteAll` | |
| `getNoPermissionsTooltip` | |

### Examples

#### Basic Usage
```twig
<sw-condition-and-container>
    <!-- content -->
</sw-condition-and-container>
```

## sw-condition-base-line-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| parentCondition | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `wrapCondition` | |
| `createEntity` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `ruleConditionRepository` | |
| `allowMatchesAll` | |
| `matchesAllOptions` | |
| `matchesAll` | |

### Examples

#### Basic Usage
```twig
<sw-condition-base-line-item>
    <!-- content -->
</sw-condition-base-line-item>
```

## sw-condition-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| condition | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| create-before | — | |
| create-after | — | |
| condition-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCreateBefore` | |
| `onCreateAfter` | |
| `onDeleteCondition` | |
| `ensureValueExist` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `conditionClasses` | |
| `conditionTypeError` | |
| `currentError` | |
| `hasError` | |
| `valueErrorPath` | |
| `value` | |
| `isDisabled` | |
| `hasNoComponent` | |
| `operator` | |
| `isEmpty` | |

### Examples

#### Basic Usage
```twig
<sw-condition-base>
    <!-- content -->
</sw-condition-base>
```

## sw-condition-billing-zip-code

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChangeNumeric` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `zipCodes` | |
| `taggedFieldPlaceholder` | |
| `conditionValueOperatorError` | |
| `conditionValueZipCodesError` | |
| `currentError` | |
| `numericOptions` | |

### Examples

#### Basic Usage
```twig
<sw-condition-billing-zip-code>
    <!-- content -->
</sw-condition-billing-zip-code>
```

## sw-condition-customer-custom-field

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getFieldDescription` | |
| `onFieldChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldCriteria` | |
| `operator` | |
| `renderedField` | |
| `selectedField` | |
| `selectedFieldSet` | |
| `renderedFieldValue` | |
| `operators` | |
| `currentError` | |
| `truncateFilter` | |
| `conditionValueRenderedFieldError` | |
| `conditionValueSelectedFieldError` | |
| `conditionValueSelectedFieldSetError` | |
| `conditionValueOperatorError` | |
| `conditionValueRenderedFieldValueError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-customer-custom-field>
    <!-- content -->
</sw-condition-customer-custom-field>
```

## sw-condition-date-range

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `formatDate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectValues` | |
| `useTime` | |
| `fromDate` | |
| `toDate` | |
| `timezone` | |
| `isDateTime` | |
| `conditionValueUseTimeError` | |
| `conditionValueFromDateError` | |
| `conditionValueToDateError` | |
| `conditionValueTimezoneError` | |
| `timezoneOptions` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-date-range>
    <!-- content -->
</sw-condition-date-range>
```

## sw-condition-generic-line-item

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getPlaceholder` | |

### Examples

#### Basic Usage
```twig
<sw-condition-generic-line-item>
    <!-- content -->
</sw-condition-generic-line-item>
```

## sw-condition-generic

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getPlaceholder` | |

### Examples

#### Basic Usage
```twig
<sw-condition-generic>
    <!-- content -->
</sw-condition-generic>
```

## sw-condition-goods-count

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `count` | |
| `conditionValueOperatorError` | |
| `conditionValueCountError` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-goods-count>
    <!-- content -->
</sw-condition-goods-count>
```

## sw-condition-goods-price

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `amount` | |
| `conditionValueOperatorError` | |
| `conditionValueAmountError` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-goods-price>
    <!-- content -->
</sw-condition-goods-price>
```

## sw-condition-is-always-valid

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `isAlwaysValid` | |
| `defaultValues` | |
| `selectValues` | |
| `conditionValueIsNewError` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-is-always-valid>
    <!-- content -->
</sw-condition-is-always-valid>
```

## sw-condition-is-net-select

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `operator` | |

### Examples

#### Basic Usage
```twig
<sw-condition-is-net-select>
    <!-- content -->
</sw-condition-is-net-select>
```

## sw-condition-line-item-custom-field

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getTooltipConfig` | |
| `getFieldDescription` | |
| `onFieldChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldCriteria` | |
| `operator` | |
| `renderedField` | |
| `selectedField` | |
| `selectedFieldSet` | |
| `renderedFieldValue` | |
| `operators` | |
| `currentError` | |
| `truncateFilter` | |
| `conditionValueRenderedFieldError` | |
| `conditionValueSelectedFieldError` | |
| `conditionValueSelectedFieldSetError` | |
| `conditionValueOperatorError` | |
| `conditionValueRenderedFieldValueError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-line-item-custom-field>
    <!-- content -->
</sw-condition-line-item-custom-field>
```

## sw-condition-line-item-goods-total

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `count` | |
| `conditionValueOperatorError` | |
| `conditionValueCountError` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-line-item-goods-total>
    <!-- content -->
</sw-condition-line-item-goods-total>
```

## sw-condition-line-item-in-category

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-description-property | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setCategoryIds` | |
| `getCategoryBreadcrumb` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `categoryRepository` | |
| `operators` | |
| `categoryIds` | |
| `conditionValueOperatorError` | |
| `conditionValueCategoryIdsError` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-line-item-in-category>
    <!-- content -->
</sw-condition-line-item-in-category>
```

## sw-condition-line-item-property

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-label-property | — | |
| result-description-property | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setOptions` | |
| `setSearchTerm` | |
| `onSelectCollapsed` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `optionRepository` | |
| `identifiers` | |
| `conditionValueOperatorError` | |
| `conditionValueIdentifiersError` | |
| `currentError` | |
| `optionCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-condition-line-item-property>
    <!-- content -->
</sw-condition-line-item-property>
```

## sw-condition-line-item-purchase-price

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `isNetOperators` | |
| `amount` | |
| `conditionValueOperatorError` | |
| `conditionValueIsNetError` | |
| `conditionValueAmountError` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-line-item-purchase-price>
    <!-- content -->
</sw-condition-line-item-purchase-price>
```

## sw-condition-line-item-with-quantity

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `productRepository` | |
| `quantity` | |
| `id` | |
| `conditionValueOperatorError` | |
| `conditionValueQuantityError` | |
| `conditionValueIdError` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-line-item-with-quantity>
    <!-- content -->
</sw-condition-line-item-with-quantity>
```

## sw-condition-line-item

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setIds` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `productRepository` | |
| `productIds` | |
| `conditionValueOperatorError` | |
| `conditionValueIdentifiersError` | |
| `currentError` | |
| `productCriteria` | |
| `resultCriteria` | |
| `productContext` | |

### Examples

#### Basic Usage
```twig
<sw-condition-line-item>
    <!-- content -->
</sw-condition-line-item>
```

## sw-condition-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| conditionDataProviderService | `any` | — | yes |  |
| condition | `any` | `null` | no |  |
| scopes | `any` | — | no |  |
| allowedTypes | `any` | `null` | no |  |
| childAssociationField | `any` | `'children'` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onConditionsChanged` | |
| `deleteAndClose` | |
| `saveAndCloseModal` | |
| `deleteChildren` | |
| `closeModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `conditionRepository` | |
| `initialConditions` | |

### Examples

#### Basic Usage
```twig
<sw-condition-modal
    conditionDataProviderService="..."
>
    <!-- content -->
</sw-condition-modal>
```

## sw-condition-not-found

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `extendedTypes` | |
| `value` | |

### Examples

#### Basic Usage
```twig
<sw-condition-not-found>
    <!-- content -->
</sw-condition-not-found>
```

## sw-condition-operator-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| operators | `any` | — | yes |  |
| condition | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| plural | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `changeOperator` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `operator` | |
| `operatorClasses` | |
| `hasError` | |
| `translatedOperators` | |
| `conditionValueOperatorError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-operator-select
    operators="..."
    condition="..."
>
    <!-- content -->
</sw-condition-operator-select>
```

## sw-condition-or-container

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddPlaceholder` | |
| `onAddAndContainer` | |
| `onDeleteAll` | |
| `getNoPermissionsTooltip` | |

### Examples

#### Basic Usage
```twig
<sw-condition-or-container>
    <!-- content -->
</sw-condition-or-container>
```

## sw-condition-order-custom-field

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getFieldDescription` | |
| `onFieldChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldCriteria` | |
| `operator` | |
| `renderedField` | |
| `selectedField` | |
| `selectedFieldSet` | |
| `renderedFieldValue` | |
| `operators` | |
| `currentError` | |
| `truncateFilter` | |
| `conditionValueRenderedFieldError` | |
| `conditionValueSelectedFieldError` | |
| `conditionValueSelectedFieldSetError` | |
| `conditionValueOperatorError` | |
| `conditionValueRenderedFieldValueError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-order-custom-field>
    <!-- content -->
</sw-condition-order-custom-field>
```

## sw-condition-script

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getBind` | |
| `updateFieldValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `config` | |
| `values` | |
| `currentError` | |
| `conditionClasses` | |

### Examples

#### Basic Usage
```twig
<sw-condition-script>
    <!-- content -->
</sw-condition-script>
```

## sw-condition-shipping-zip-code

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChangeNumeric` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `operators` | |
| `zipCodes` | |
| `taggedFieldPlaceholder` | |
| `conditionValueOperatorError` | |
| `conditionValueZipCodesError` | |
| `currentError` | |
| `numericOptions` | |

### Examples

#### Basic Usage
```twig
<sw-condition-shipping-zip-code>
    <!-- content -->
</sw-condition-shipping-zip-code>
```

## sw-condition-time-range

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `fromTime` | |
| `toTime` | |
| `timezone` | |
| `conditionValueFromTimeError` | |
| `conditionValueToTimeError` | |
| `conditionValueTimezoneError` | |
| `timezoneOptions` | |
| `currentError` | |

### Examples

#### Basic Usage
```twig
<sw-condition-time-range>
    <!-- content -->
</sw-condition-time-range>
```

## sw-condition-tree-node

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| level | `any` | — | yes |  |
| condition | `any` | — | yes |  |
| parentCondition | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| insertBefore | `any` | `null` | no |  |
| insertAfter | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `deleteNode` | |
| `insertNewNodeBefore` | |
| `insertNewNodeAfter` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `conditionNodeComponent` | |

### Examples

#### Basic Usage
```twig
<sw-condition-tree-node
    level="..."
    condition="..."
>
    <!-- content -->
</sw-condition-tree-node>
```

## sw-condition-tree

> Visual rule/condition tree builder with AND/OR grouping.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| conditionDataProviderService | `any` | — | yes |  |
| conditionRepository | `any` | `null` | no |  |
| initialConditions | `any` | `null` | no |  |
| rootCondition | `any` | `null` | no |  |
| allowedTypes | `any` | `null` | no |  |
| scopes | `any` | `null` | no |  |
| associationField | `any` | — | yes |  |
| associationValue | `any` | — | yes |  |
| associationEntity | `any` | `null` | no |  |
| childAssociationField | `any` | `'children'` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| conditions-changed | — | |
| initial-loading-done | — | |

### Methods

| Method | Description |
|--------|-------------|
| `buildTree` | |
| `createTreeRecursive` | |
| `getRootNodes` | |
| `needsRootOrContainer` | |
| `applyRoot` | |
| `createCondition` | |
| `insertNodeIntoTree` | |
| `removeNodeFromTree` | |
| `validatePosition` | |
| `getDeletedIds` | |
| `getDeletedIdsRecursive` | |
| `emitChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `availableTypes` | |
| `rootId` | |
| `availableGroups` | |
| `restrictedConditions` | |

### Examples

#### Example 1
Source: `sw-settings-rule/view/sw-settings-rule-detail-base/sw-settings-rule-detail-base.html.twig`
```twig
    <sw-condition-tree
        :initial-conditions="conditions"
        :condition-repository="conditionRepository"
        :condition-data-provider-service="ruleConditionDataProviderService"
        association-field="ruleId"
        :association-value="rule.id"
        :association-entity="rule"
        :root-condition="null"
        :disabled="!acl.can('rule.editor') || undefined"
        @conditions-changed="$emit('conditions-changed', $event)"
        @initial-loading-done="$emit('tree-finished-loading')"
    />
</mt-card>
{% endblock %}

```

#### Example 2
Source: `sw-product/component/sw-product-cross-selling-form/sw-product-cross-selling-form.html.twig`
```twig
    <sw-condition-tree
        v-if="productStreamFilterRepository"
        v-show="false"
        association-field="productStreamId"
        child-association-field="queries"
        :initial-conditions="productStreamFilter"
        :condition-repository="productStreamFilterRepository"
        :condition-data-provider-service="productStreamConditionService"
        :association-value="associationValue"
        :root-condition="null"
        @conditions-changed="updateProductStreamFilterTree"
    />
    {% endblock %}
</div>
{% endblock %}
```

#### Example 3
Source: `sw-flow/component/modals/sw-flow-rule-modal/sw-flow-rule-modal.html.twig`
```twig
                <sw-condition-tree
                    v-if="conditionRepository"
                    class="sw-flow-rule-modal__rule"
                    association-field="ruleId"
                    :initial-conditions="conditions"
                    :condition-repository="conditionRepository"
                    :condition-data-provider-service="ruleConditionDataProviderService"
                    :association-value="rule.id"
                    :association-entity="rule"
                    :root-condition="null"
                    @conditions-changed="onConditionsChanged"
                />
                {% endblock %}
            </div>
            {% endblock %}
```

#### Example 4
Source: `sw-product-stream/page/sw-product-stream-detail/sw-product-stream-detail.html.twig`
```twig
    <sw-condition-tree
        v-if="productStream"
        :initial-conditions="productStreamFilters"
        :condition-repository="productStreamFiltersRepository"
        :condition-data-provider-service="productStreamConditionService"
        child-association-field="queries"
        association-field="productStreamId"
        :association-value="productStream.id"
        :root-condition="null"
        :disabled="!acl.can('product_stream.editor')"
        @conditions-changed="updateFilterTree"
    />
    {% endblock %}

    {% block sw_product_stream_detail_filter_preview_button %}
```

## sw-condition-type-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| availableTypes | `any` | — | yes |  |
| condition | `any` | — | yes |  |
| hasError | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| availableGroups | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `changeItem` | |
| `changeType` | |
| `getTooltipConfig` | |
| `groupAssignments` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `valueProperty` | |
| `ucTerm` | |
| `typeOptions` | |
| `typeSelectClasses` | |
| `arrowColor` | |

### Examples

#### Basic Usage
```twig
<sw-condition-type-select
    availableTypes="..."
    condition="..."
>
    <!-- content -->
</sw-condition-type-select>
```

## sw-condition-unit-menu

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| type | `any` | — | yes |  |
| value | `null \| null` | — | no |  |
| visibleValue | `null \| null` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| set-default-unit | — | |
| change-unit | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onUnitChange` | |
| `getConvertedValue` | |
| `isSelected` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `defaultUnit` | |
| `unitSnippet` | |
| `unitOptions` | |

### Examples

#### Basic Usage
```twig
<sw-condition-unit-menu
    type="..."
>
    <!-- content -->
</sw-condition-unit-menu>
```

## sw-confirm-field

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| compact | `any` | `false` | no |  |
| preventEmptySubmit | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| error | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| remove-error | — | |
| blur | — | |
| submit-cancel | — | |
| input | — | |

### Methods

| Method | Description |
|--------|-------------|
| `removeActionButtons` | |
| `onStartEditing` | |
| `onBlurField` | |
| `cancelSubmit` | |
| `onCancelFromKey` | |
| `onCancelSubmit` | |
| `submitValue` | |
| `onSubmitFromKey` | |
| `onSubmitValue` | |
| `onInput` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `confirmFieldClasses` | |

### Examples

#### Example 1
Source: `sw-media/component/sidebar/sw-media-folder-info/sw-media-folder-info.html.twig`
```twig
                <sw-confirm-field
                    v-if="editable"
                    ref="inlineEditFieldName"
                    :disabled="!acl.can('media.creator')"
                    compact
                    :value="mediaFolder.name"
                    :error="mediaFolderNameError"
                    @input="onChangeFolderName"
                />
                <template v-else>
                    {{ mediaFolder.name }}
                </template>
            </sw-media-quickinfo-metadata-item>

            <sw-media-quickinfo-metadata-item
```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
    <sw-confirm-field
        v-if="editable"
        ref="inlineEditFieldName"
        class="sw-media-quickinfo-metadata-name"
        :disabled="!acl.can('media.editor')"
        compact
        :value="item.fileName"
        :error="fileNameError"
        @input="onChangeFileName"
        @remove-error="onRemoveFileNameError"
    /><template v-else>
        {{ item.fileName }}
    </template>
</sw-media-quickinfo-metadata-item>

```

#### Example 3
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
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
        {{ placeholder(item, 'title') }}
    </template>
</sw-media-quickinfo-metadata-item>

<sw-media-quickinfo-metadata-item
```

#### Example 4
Source: `sw-order/component/sw-order-inline-field/sw-order-inline-field.html.twig`
```twig
        <sw-confirm-field
            :value="value"
            :required="required"
            @input="onInput"
        />
    </slot>
    <span v-else>
        {{ displayValue }}
    </span>
</div>
{% endblock %}

```

## sw-confirm-modal

> Confirmation modal dialog with confirm and cancel actions.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | `''` | no |  |
| text | `any` | `''` | no |  |
| textConfirm | `any` | `''` | no |  |
| variant | `any` | `'small'` | no | Valid: `default`, `small`, `large`, `full` |
| type | `any` | `'confirm'` | no | Valid: `confirm`, `delete`, `yesno`, `discard` |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| cancel | — | |
| confirm | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `titleText` | |
| `descriptionText` | |
| `confirmText` | |
| `cancelText` | |
| `confirmButtonVariant` | |

### Examples

#### Example 1
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

#### Example 2
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

#### Example 3
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

#### Example 4
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

#### Example 5
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

## sw-container

> Flexible layout container with configurable columns and gap.

- [Slots](#slots)
- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| columns | `any` | `''` | no |  |
| rows | `any` | `''` | no |  |
| gap | `any` | `''` | no |  |
| justify | `any` | `'stretch'` | no | Valid: `start`, `end`, `center`, `stretch`, `left`, `right` |
| align | `any` | `'stretch'` | no | Valid: `start`, `end`, `center`, `stretch` |
| breakpoints | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerResizeListener` | |
| `updateCssGrid` | |
| `buildCssGrid` | |
| `cssGridDefaults` | |
| `buildCssGridProps` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<sw-container class="sw-settings-country-address-handling__options-container">

    <mt-switch
        :model-value="country.forceStateInRegistration"
        class="sw-settings-country-address-handling__option-items"
        bordered
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-settings-country.detail.labelForceStateInRegistration')"
        @update:model-value="updateCountry('forceStateInRegistration', $event)"
    />

    <mt-switch
        :model-value="country.postalCodeRequired"
        class="sw-settings-country-address-handling__option-items"
        bordered
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<sw-container class="sw-settings-country-address-handling__options-container">
    <div class="sw-settings-country-address-handling__address-markup">
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
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<sw-container
    columns="repeat(auto-fit, minmax(250px, 1fr))"
    gap="0px 30px"
>

    <!-- eslint-disable sw-deprecation-rules/no-twigjs-blocks, vue/attributes-order -->
    {% block sw_settings_country_general_content_field_name %}

    <mt-text-field
        v-model="country.name"
        name="sw-field--country-name"
        required
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-settings-country.detail.labelName')"
        :placeholder="placeholder(country, 'name', $tc('sw-settings-country.detail.placeholderName'))"
```

#### Example 4
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<sw-container class="sw-settings-country-general__options-container">

    {% block sw_settings_country_general_content_field_active %}

    <mt-switch
        v-model="country.active"
        name="sw-field--country-active"
        class="sw-settings-country-general__option-items"
        bordered
        :disabled="!acl.can('country.editor') || undefined"
        :label="$tc('sw-settings-country.detail.labelActive')"
    />
    {% endblock %}

    {% block sw_settings_country_general_content_field_shipping_available %}
```

#### Example 5
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
<sw-container
    columns="1fr 32px minmax(100px, 200px)"
    gap="0 10px"
>

    {% block sw_attribute_list_toolbar_searchfield %}
    <sw-simple-search-field
        v-model:value="term"
        size="small"
        variant="form"
        @search-term-change="onSearchCountryState"
    />
    {% endblock %}

    {% block sw_settings_country_state_list_toolbar_delete %}
```

## sw-context-button

> Trigger button that opens a context menu dropdown.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| showMenuOnStartup | `any` | `false` | no |  |
| menuWidth | `any` | `220` | no |  |
| menuHorizontalAlign | `any` | `'right'` | no |  |
| menuVerticalAlign | `any` | `'bottom'` | no |  |
| icon | `any` | `'solid-ellipsis-h-s'` | no |  |
| iconSize | `any` | `'16px'` | no |  |
| disabled | `any` | `false` | no |  |
| autoClose | `any` | `true` | no |  |
| autoCloseOutsideClick | `any` | `false` | no |  |
| additionalContextMenuClasses | `any` | — | no |  |
| zIndex | `any` | `1100` | no |  |
| ariaLabel | `any` | `'sw-context-button.ariaLabel'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| button | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-open-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClickButton` | |
| `openMenu` | |
| `handleClickEvent` | |
| `closeMenu` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `menuStyles` | |
| `contextClass` | |
| `contextButtonClass` | |
| `contextMenuClass` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-hamburger-menu/sw-settings-country-currency-hamburger-menu.html.twig`
```twig
<sw-context-button
    :menu-width="300"
    :auto-close="false"
    :auto-close-outside-click="true"
>
    <template #button>

        {% block sw_settings_country_currency_hamburger_menu_trigger %}
        <mt-button
            class="sw-settings-country-currency-hamburger-menu__button"
            size="x-small"
            square
            variant="secondary"
        >

```

#### Example 2
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-context-button class="sw-multi-snippet-drag-and-drop__context-button">
    <sw-context-menu-item
        :disabled="isMaxLines"
        @click="openModal"
    >
        {{ $tc('sw-settings-country.general.actions.newSnippet') }}
    </sw-context-menu-item>

    <sw-context-menu-item
        :disabled="isMaxLines"
        @click="addNewLineAt('above')"
    >
        {{ $tc('sw-settings-country.general.actions.createBefore') }}
    </sw-context-menu-item>

```

#### Example 3
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-context-button
    v-if="showContextMenu"
    class="sw-extension-card-base__context-menu"
    :menu-width="180"
>
    {% block sw_extension_card_base_context_menu_actions %}
    <sw-context-menu-item
        v-if="openLinkExists && extension.active"
        :disabled="!openLinkExists"
        :router-link="link"
    >
        {{ $tc('sw-extension-store.component.sw-extension-card-base.contextMenu.openExtension') }}
    </sw-context-menu-item>

    <sw-context-menu-item
```

#### Example 4
Source: `sw-category/component/sw-category-layout-card/sw-category-layout-card.html.twig`
```twig
<sw-context-button class="sw-category-layout-card__desc-actions-menu">
    {% block sw_category_detail_layout_desc_actions_designer %}
    <sw-context-menu-item
        class="sw-category-detail-layout__open-in-pagebuilder"
        :disabled="!acl.can('category.editor')"
        @click="openInPagebuilder"
    >
        {{ $t('global.default.edit') }}
    </sw-context-menu-item>
    {% endblock %}

    {% block sw_category_detail_layout_desc_actions_remove %}
    <sw-context-menu-item
        v-if="cmsPage"
        :disabled="!acl.can('category.editor')"
```

#### Example 5
Source: `sw-category/component/sw-landing-page-tree/sw-landing-page-tree.html.twig`
```twig
<sw-context-button
    v-tooltip="toolTip"
    class="sw-tree-item__context_button"
    :disabled="disableContextMenu || undefined"
>

    {% block sw_landing_page_tree_items_actions_edit %}
    <sw-context-menu-item @click="onChangeRoute(item)">
        {{ $tc('global.default.edit') }}
    </sw-context-menu-item>
    {% endblock %}

    {% block sw_landing_page_tree_items_actions_duplicate %}
    <sw-context-menu-item
        class="sw-context-menu__duplicate-action"
```

## sw-context-menu-divider

> Visual divider between context menu item groups.

### Examples

#### Example 1
Source: `sw-settings-units/page/sw-settings-units-list/sw-settings-units.html.twig`
```twig
<sw-context-menu-divider />
```

#### Example 2
Source: `sw-product/component/sw-product-settings-mode/sw-product-settings-mode.html.twig`
```twig
<sw-context-menu-divider />
```

#### Example 3
Source: `sw-settings-tag/page/sw-settings-tag-list/sw-settings-tag-list.html.twig`
```twig
<sw-context-menu-divider />
```

## sw-context-menu-item

> Individual menu item within a context menu.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| icon | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| routerLink | `any` | `null` | no |  |
| target | `any` | `null` | no |  |
| variant | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| icon | — | |

### Methods

| Method | Description |
|--------|-------------|
| `handleClick` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `contextMenuItemStyles` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-context-menu-item
    :router-link="{ name: 'sw.settings.country.detail', params: { id: item.id, edit: 'edit' }}"
    :disabled="!acl.can('country.editor') && !acl.can('country.viewer') || undefined"
    class="sw-country-list__edit-action"
>
    {{ detailPageLinkText }}
</sw-context-menu-item>
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-context-menu-item
    class="sw-country-list__delete-action"
    variant="danger"
    :disabled="!acl.can('country.deleter') || undefined"
    @click="onDelete(item.id)"
>
    {{ $tc('sw-settings-country.list.contextMenuDelete') }}
</sw-context-menu-item>
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
<sw-context-menu-item
    variant="danger"
    :disabled="(item.enabled || !acl.can('country.editor')) || undefined"
    @click="changeCurrencyDependentRow(item.currencyId, false)"
>
    {{ $tc('global.default.delete') }}
</sw-context-menu-item>
```

#### Example 4
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
<sw-context-menu-item
    v-tooltip.top="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('country.editor'),
        showOnDisabledElements: true
    }"
    class="sw-settings-country-state__edit-country-state-action"
    :disabled="!acl.can('country.editor') || undefined"
    @click="onClickCountryState(item)"
>
    {{ $tc('sw-settings-country.detail.editAction') }}
</sw-context-menu-item>
```

#### Example 5
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-context-menu-item
    :disabled="isMaxLines"
    @click="openModal"
>
    {{ $tc('sw-settings-country.general.actions.newSnippet') }}
</sw-context-menu-item>
```

## sw-context-menu

> Context menu container with menu items and dividers.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
    <sw-context-menu-item
        :router-link="{ name: 'sw.settings.country.detail', params: { id: item.id, edit: 'edit' }}"
        :disabled="!acl.can('country.editor') && !acl.can('country.viewer') || undefined"
        class="sw-country-list__edit-action"
    >
        {{ detailPageLinkText }}
    </sw-context-menu-item>
    {% endblock %}

    {% block sw_settings_country_list_grid_columns_actions_delete %}
    <sw-context-menu-item
        class="sw-country-list__delete-action"
        variant="danger"
        :disabled="!acl.can('country.deleter') || undefined"
        @click="onDelete(item.id)"
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
        <sw-context-menu-item
            variant="danger"
            :disabled="(item.enabled || !acl.can('country.editor')) || undefined"
            @click="changeCurrencyDependentRow(item.currencyId, false)"
        >
            {{ $tc('global.default.delete') }}
        </sw-context-menu-item>
        {% endblock %}

    </template>
    {% endblock %}

</sw-data-grid>
{% endblock %}

```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
            <sw-context-menu-item
                v-tooltip.top="{
                    message: $tc('sw-privileges.tooltip.warning'),
                    disabled: acl.can('country.editor'),
                    showOnDisabledElements: true
                }"
                class="sw-settings-country-state__edit-country-state-action"
                :disabled="!acl.can('country.editor') || undefined"
                @click="onClickCountryState(item)"
            >
                {{ $tc('sw-settings-country.detail.editAction') }}
            </sw-context-menu-item>
            {% endblock %}
        </template>
    </sw-one-to-many-grid>
```

#### Example 4
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-context-menu-item
    :disabled="isMaxLines"
    @click="openModal"
>
    {{ $tc('sw-settings-country.general.actions.newSnippet') }}
</sw-context-menu-item>

<sw-context-menu-item
    :disabled="isMaxLines"
    @click="addNewLineAt('above')"
>
    {{ $tc('sw-settings-country.general.actions.createBefore') }}
</sw-context-menu-item>

<sw-context-menu-item
```

#### Example 5
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
        <sw-context-menu-item
            variant="danger"
            :disabled="isMinLines"
            @click="onDelete"
        >
            {{ $tc('global.default.delete') }}
        </sw-context-menu-item>
    </sw-context-button>
</div>
{% endblock %}

```

## sw-contextual-field

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-contextual-field-prefix | — | |
| sw-field-input | — | |
| sw-contextual-field-suffix | — | |
| hint | — | |
| label | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasPrefix` | |
| `hasSuffix` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
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
            v-model="searchTerm"
            type="text"
            class="sw-settings-country-new-snippet-modal__input-field"
            :placeholder="$tc('sw-settings-country.detail.placeholderSearchSnippet')"
            :disabled="disabled"
```

#### Example 2
Source: `sw-flow/component/sw-flow-trigger/sw-flow-trigger.html.twig`
```twig
<sw-contextual-field
    v-tooltip="{
        message: getEventName(eventName),
        disabled: !eventName || isUnknownTrigger,
    }"
    class="sw-flow-trigger__search-field"
    :required="!isTemplate"
    :label="$tc('sw-flow.detail.trigger.name')"
    :disabled="disabled"
    :error="flowEventNameError"
>
    <template #sw-field-input="{ identification, disabled, error, size, setFocusClass, removeFocusClass }">
        {% block sw_flow_trigger_select_field_input %}
        <!-- eslint-disable-next-line vuejs-accessibility/form-control-has-label -->
        <input
```

## sw-country-state-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| countryState | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| attribute-edit-cancel | — | |
| attribute-edit-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `tooltipSave` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
    <sw-country-state-detail
        v-if="currentCountryState"
        :country-state="currentCountryState"
        @attribute-edit-save="onSaveCountryState"
        @attribute-edit-cancel="onCancelCountryState"
    />
    {% endblock %}
</mt-card>
{% endblock %}


```

## sw-custom-entity-input-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `null \| null \| null \| null` | `null` | no |  |
| type | `any` | — | yes |  |
| label | `any` | `''` | no |  |
| placeholder | `any` | `''` | no |  |
| helpText | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |

### Examples

#### Example 1
Source: `sw-custom-entity/page/sw-generic-custom-entity-detail/sw-generic-custom-entity-detail.html.twig`
```twig
                <sw-custom-entity-input-field
                    v-for="field in card.fields"
                    :key="field.ref"
                    v-model:value="customEntityData[field.ref]"
                    class="sw-generic-custom-entity-detail__field"
                    :type="getType(field.ref)"
                    :label="getLabel('fields', field.ref)"
                    :placeholder="getPlaceholder('fields', field.ref)"
                    :help-text="getHelpText('fields', field.ref)"
                />
            </template>
        </mt-card>
    </div>
</template>

```

## sw-custom-field-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentCustomField | `any` | — | yes |  |
| set | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| custom-field-edit-cancel | — | |
| custom-field-edit-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCancel` | |
| `onSave` | |
| `createNameNotUniqueNotification` | |
| `createEntityTypeRequiredNotification` | |
| `applyTypeConfiguration` | |
| `getCartExposeTooltipConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `locales` | |
| `canSave` | |
| `renderComponentName` | |
| `modalTitle` | |
| `labelSaveButton` | |
| `isProductCustomField` | |
| `ruleConditionRepository` | |
| `customFieldTypeOptions` | |
| `currentCustomFieldNameError` | |

### Examples

#### Example 1
Source: `sw-settings-custom-field/component/sw-custom-field-list/sw-custom-field-list.html.twig`
```twig
<sw-custom-field-detail
    v-if="currentCustomField"
    :set="set"
    :current-custom-field="currentCustomField"
    @custom-field-edit-save="onSaveCustomField"
    @custom-field-edit-cancel="onCancelCustomField"
/>
{% endblock %}

{% block sw_custom_field_list_custom_field_delete %}
<sw-modal
    v-if="deleteCustomField"
    :title="$tc('sw-settings-custom-field.customField.list.titleDeleteAction', {}, deleteCustomField.length)"
    variant="small"
    @modal-close="onCancelDeleteCustomField"
```

## sw-custom-field-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| set | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-changed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `createdComponent` | |
| `loadCustomFields` | |
| `selectionChanged` | |
| `onCustomFieldDelete` | |
| `onDeleteCustomFields` | |
| `onAddCustomField` | |
| `onCancelCustomField` | |
| `onInlineEditFinish` | |
| `onSaveCustomField` | |
| `onInlineEditCancel` | |
| `onCustomFieldEdit` | |
| `removeEmptyProperties` | |
| `isCustomFieldNameUnique` | |
| `onPageChange` | |
| `onCancelDeleteCustomField` | |
| `onDeleteCustomField` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `globalCustomFieldRepository` | |

### Examples

#### Example 1
Source: `sw-settings-custom-field/page/sw-settings-custom-field-set-detail/sw-settings-custom-field-set-detail.html.twig`
```twig
                <sw-custom-field-list
                    v-if="set.id"
                    ref="customFieldList"
                    :set="set"
                    @loading-changed="onLoadingChanged"
                />
                {% endblock %}
            </div>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-custom-field-set-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| set | `any` | — | yes |  |
| technicalNameError | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| reset-errors | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onAddRelation` | |
| `onRemoveRelation` | |
| `searchRelationEntityNames` | |
| `onTechnicalNameChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `locales` | |
| `customFieldSetRelationRepository` | |
| `selectedRelationEntityNames` | |
| `relationEntityNames` | |

### Examples

#### Example 1
Source: `sw-settings-custom-field/page/sw-settings-custom-field-set-detail/sw-settings-custom-field-set-detail.html.twig`
```twig
                <sw-custom-field-set-detail-base
                    :set="set"
                    :technical-name-error="technicalNameError"
                    @reset-errors="onResetErrors"
                />
                {% endblock %}

                {% block sw_settings_custom_field_set_detail_content_detail_custom_field_list %}
                <sw-custom-field-list
                    v-if="set.id"
                    ref="customFieldList"
                    :set="set"
                    @loading-changed="onLoadingChanged"
                />
                {% endblock %}
```

## sw-custom-field-set-renderer

> Renders a complete set of custom fields with their configured field types.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sets | `any` | — | yes |  |
| entity | `any` | — | yes |  |
| parentEntity | `any` | `null` | no |  |
| variant | `any` | `'tabs'` | no | Valid: `tabs`, `media-collapse` |
| disabled | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |
| isSaveSuccessful | `any` | `false` | no |  |
| showCustomFieldSetSelection | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| process-finish | — | |
| save | — | |
| change-active-selection | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initializeCustomFields` | |
| `getInheritedCustomField` | |
| `getCustomFieldInformation` | |
| `getInheritValue` | |
| `getParentCustomFieldSetSelectionSwitchState` | |
| `supportsMapInheritance` | |
| `isMeteorComponent` | |
| `getBind` | |
| `getElementEventListeners` | |
| `getInheritWrapperBind` | |
| `customFieldSetCriteriaById` | |
| `loadCustomFieldSet` | |
| `resetTabs` | |
| `waitForTabComponent` | |
| `getTabLabel` | |
| `onChangeCustomFieldSets` | |
| `onChangeCustomFieldSetSelectionActive` | |
| `sortSets` | |
| `onUpdateActiveSelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasParent` | |
| `visibleCustomFieldSets` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `globalCustomFieldSets` | |
| `componentsWithMapInheritanceSupport` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="country"
                        :disabled="!acl.can('country.editor')"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 2
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="salutation"
                        :disabled="!acl.can('salutation.editor') || undefined"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}

</sw-page>
{% endblock %}

```

#### Example 3
Source: `sw-settings-units/page/sw-settings-units-detail/sw-settings-units-detail.html.twig`
```twig
                <sw-custom-field-set-renderer
                    :entity="unit"
                    :sets="customFieldSets"
                    :disabled="!acl.can('unit.editor')"
                />
            </mt-card>

            <sw-skeleton v-else />
        </sw-card-view>
    </template>
</sw-page>
{% endblock %}

```

#### Example 4
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="numberRange"
                        :disabled="!acl.can('number_ranges.editor')"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 5
Source: `sw-property/page/sw-property-detail/sw-property-detail.html.twig`
```twig
                    <sw-custom-field-set-renderer
                        :entity="propertyGroup"
                        :disabled="!acl.can('property.editor') || undefined"
                        :sets="customFieldSets"
                    />
                </mt-card>
                {% endblock %}
            </div>
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-custom-field-translated-labels

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| locales | `any` | `[]` | yes |  |
| config | `any` | — | yes |  |
| propertyNames | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initializeConfiguration` | |
| `getLabel` | |
| `onInput` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `fallbackLocale` | |
| `localeCount` | |

### Examples

#### Example 1
Source: `sw-settings-custom-field/component/sw-custom-field-set-detail-base/sw-custom-field-set-detail-base.html.twig`
```twig
<sw-custom-field-translated-labels
    v-if="set.config"
    v-model:config="set.config"
    :disabled="!acl.can('custom_field.editor') || undefined"
    :property-names="propertyNames"
    :locales="locales"
/>
{% endblock %}

{% block sw_settings_custom_field_set_detail_base_multi_select %}
<sw-multi-select
    id="entities"
    class="sw-settings-custom-field-set-detail-base__label-entities"
    :disabled="!acl.can('custom_field.editor') || undefined"
    :label="$tc('sw-settings-custom-field.set.detail.labelEntities')"
```

#### Example 2
Source: `sw-settings-custom-field/component/sw-custom-field-type-base/sw-custom-field-type-base.html.twig`
```twig
    <sw-custom-field-translated-labels
        v-model:config="currentCustomField.config"
        :disabled="!acl.can('custom_field.editor')"
        :property-names="propertyNames"
        :locales="locales"
    />
    {% endblock %}
    {% endblock %}
</div>
{% endblock %}

```

## sw-custom-field-type-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentCustomField | `any` | — | yes |  |
| set | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `locales` | |

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-base
    currentCustomField="..."
    set="..."
>
    <!-- content -->
</sw-custom-field-type-base>
```

## sw-custom-field-type-checkbox

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-checkbox>
    <!-- content -->
</sw-custom-field-type-checkbox>
```

## sw-custom-field-type-colorpicker

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-colorpicker>
    <!-- content -->
</sw-custom-field-type-colorpicker>
```

## sw-custom-field-type-date

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-date>
    <!-- content -->
</sw-custom-field-type-date>
```

## sw-custom-field-type-entity

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChangeEntityType` | |
| `onChangeMultiSelectSwitch` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `entityTypes` | |
| `customFieldsAwareCustomEntities` | |
| `customEntityRepository` | |
| `sortedEntityTypes` | |

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-entity>
    <!-- content -->
</sw-custom-field-type-entity>
```

## sw-custom-field-type-number

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isIntField` | |

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-number>
    <!-- content -->
</sw-custom-field-type-number>
```

## sw-custom-field-type-select

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `addOption` | |
| `onClickAddOption` | |
| `getLabel` | |
| `onDeleteOption` | |
| `onChangeMultiSelectSwitch` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isOptionAddable` | |

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-select>
    <!-- content -->
</sw-custom-field-type-select>
```

## sw-custom-field-type-text-editor

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-text-editor>
    <!-- content -->
</sw-custom-field-type-text-editor>
```

## sw-custom-field-type-text

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-custom-field-type-text>
    <!-- content -->
</sw-custom-field-type-text>
```

## sw-customer-address-form-options

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| address | `any` | — | yes |  |
| customFieldSets | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| default-address-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChangeDefaultShippingAddress` | |
| `onChangeDefaultBillingAddress` | |

### Examples

#### Example 1
Source: `sw-customer/view/sw-customer-detail-addresses/sw-customer-detail-addresses.html.twig`
```twig
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="customerAddressCustomFieldSets"
        @default-address-change="onChangeDefaultAddress"
    />

</sw-customer-address-form>
{% endblock %}

{% block sw_customer_detail_addresses_add_modal_footer %}
<template #modal-footer>
    {% block sw_customer_detail_addresses_add_modal_cancel %}
    <mt-button
        size="small"
```

#### Example 2
Source: `sw-order/component/sw-order-address-selection/sw-order-address-selection.html.twig`
```twig
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="customer"
        :custom-field-sets="customerAddressCustomFieldSets"
        @default-address-change="onChangeDefaultAddress"
    />
</sw-customer-address-form>
{% endblock %}

{% block sw_order_address_modal_actions %}
<template #modal-footer>
    {% block sw_order_address_modal_action_close %}
    <mt-button
        size="small"
        variant="secondary"
```

#### Example 3
Source: `sw-order/component/sw-order-create-address-modal/sw-order-create-address-modal.html.twig`
```twig
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="[]"
        @default-address-change="onChangeDefaultAddress"
    />
</sw-customer-address-form>
{% endblock %}

{% block sw_order_create_address_form_modal_footer %}
<template #modal-footer>
    {% block sw_order_create_address_form_modal_cancel_button %}
    <mt-button
        size="small"
        variant="secondary"
```

## sw-customer-address-form

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| address | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getCountryStates` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `addressRepository` | |
| `countryRepository` | |
| `countryStateRepository` | |
| `addressCompanyError` | |
| `addressDepartmentError` | |
| `addressSalutationIdError` | |
| `addressTitleError` | |
| `addressFirstNameError` | |
| `addressLastNameError` | |
| `addressStreetError` | |
| `addressAdditionalAddressLine1Error` | |
| `addressAdditionalAddressLine2Error` | |
| `addressZipcodeError` | |
| `addressCityError` | |
| `addressCountryIdError` | |
| `addressPhoneNumberError` | |
| `addressCountryStateIdError` | |
| `countryId` | |
| `countryCriteria` | |
| `stateCriteria` | |
| `salutationCriteria` | |
| `hasStates` | |
| `isBusinessAccountType` | |

### Examples

#### Example 1
Source: `sw-customer/page/sw-customer-create/sw-customer-create.html.twig`
```twig
                <sw-customer-address-form
                    v-if="customer"
                    v-bind="{ customer, address }"
                />
            </mt-card>
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 2
Source: `sw-customer/view/sw-customer-detail-addresses/sw-customer-detail-addresses.html.twig`
```twig
<sw-customer-address-form
    :address="currentAddress"
    :customer="activeCustomer"
>

    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="customerAddressCustomFieldSets"
        @default-address-change="onChangeDefaultAddress"
    />

</sw-customer-address-form>
{% endblock %}

```

#### Example 3
Source: `sw-order/component/sw-order-address-modal/sw-order-address-modal.html.twig`
```twig
    <sw-customer-address-form
        :address="address"
        :customer="orderCustomer"
        :countries="countries"
    />
    <sw-custom-field-set-renderer
        :entity="address"
        variant="tabs"
        :sets="addressCustomFieldSets"
    />
    {% endblock %}
</div>
<div v-if="active==='addresses'">
    {% block sw_order_address_modal_tabs_content_select_address %}
    <mt-button
```

#### Example 4
Source: `sw-order/component/sw-order-address-selection/sw-order-address-selection.html.twig`
```twig
<sw-customer-address-form
    :address="currentAddress"
    :customer="customer"
>
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="customer"
        :custom-field-sets="customerAddressCustomFieldSets"
        @default-address-change="onChangeDefaultAddress"
    />
</sw-customer-address-form>
{% endblock %}

{% block sw_order_address_modal_actions %}
<template #modal-footer>
```

#### Example 5
Source: `sw-order/component/sw-order-create-address-modal/sw-order-create-address-modal.html.twig`
```twig
<sw-customer-address-form
    :address="currentAddress"
    :customer="activeCustomer"
    :disabled="isLoading"
>
    <sw-customer-address-form-options
        :address="currentAddress"
        :customer="activeCustomer"
        :custom-field-sets="[]"
        @default-address-change="onChangeDefaultAddress"
    />
</sw-customer-address-form>
{% endblock %}

{% block sw_order_create_address_form_modal_footer %}
```

## sw-customer-base-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sales-channel-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSalesChannelChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerSalutationIdError` | |
| `customerFirstNameError` | |
| `customerLastNameError` | |
| `customerEmailError` | |
| `customerGroupIdError` | |
| `customerSalesChannelIdError` | |
| `customerCustomerNumberError` | |
| `customerPasswordError` | |
| `customerVatIdsError` | |
| `customerCompanyError` | |
| `customerPasswordNewError` | |
| `customerPasswordConfirmError` | |
| `salutationCriteria` | |
| `accountTypeOptions` | |
| `isBusinessAccountType` | |

### Examples

#### Example 1
Source: `sw-customer/page/sw-customer-create/sw-customer-create.html.twig`
```twig
                <sw-customer-base-form
                    v-if="customer"
                    :is-loading="isLoading"
                    :customer="customer"
                    @sales-channel-change="onChangeSalesChannel"
                />
            </mt-card>
            {% endblock %}

            {% block sw_customer_create_adress_form %}
            <mt-card
                :title="$tc('sw-customer.detailBase.labelAddressesCard')"
                position-identifier="sw-customer-create-address-form"
            >
                <sw-customer-address-form
```

#### Example 2
Source: `sw-order/component/sw-order-new-customer-modal/sw-order-new-customer-modal.html.twig`
```twig
    <sw-customer-base-form
        :is-loading="isLoading"
        :customer="customer"
        @sales-channel-change="onChangeSalesChannel"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_order_new_customer_modal_content_shipping %}
<div v-if="active === 'shippingAddress'">
    {% block sw_order_new_customer_modal_content_shipping_same_billing %}

    <mt-switch
        v-model="isSameBilling"
```

## sw-customer-base-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | `false` | yes |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `orderRepository` | |
| `languageRepository` | |
| `languageId` | |
| `customerLanguageName` | |
| `languageCriteria` | |
| `orderCriteria` | |
| `customerSalutationIdError` | |
| `customerFirstNameError` | |
| `customerLastNameError` | |
| `customerEmailError` | |
| `customerGroupIdError` | |
| `customerSalesChannelIdError` | |
| `customerCustomerNumberError` | |
| `customerPasswordError` | |
| `customerVatIdsError` | |
| `customerCompanyError` | |
| `customerPasswordNewError` | |
| `customerPasswordConfirmError` | |
| `isBusinessAccountType` | |
| `dateFilter` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-customer/view/sw-customer-detail-base/sw-customer-detail-base.html.twig`
```twig
    <sw-customer-base-info
        :customer="customer"
        :is-loading="isLoading"
        :customer-edit-mode="customerEditMode"
    />
    {% endblock %}
</sw-customer-card>
{% endblock %}

{% block sw_customer_detail_base_default_addresses_card %}
<mt-card
    v-if="customer.defaultShippingAddress || customer.defaultBillingAddress"
    :title="$tc('sw-customer.detailBase.labelAddressesCard')"
    position-identifier="sw-customer-detail-base-default-addresses"
    class="sw-customer-detail-base__default-addresses"
```

## sw-customer-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| title | `any` | — | yes |  |
| editMode | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| metadata-additional | — | |
| actions | — | |
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getMailTo` | |
| `onImitateCustomer` | |
| `onCloseImitateCustomerModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasActionSlot` | |
| `hasAdditionalDataSlot` | |
| `hasSummarySlot` | |
| `moduleColor` | |
| `fullName` | |
| `salutationCriteria` | |
| `customerSalutationIdError` | |
| `customerFirstNameError` | |
| `customerLastNameError` | |
| `customerEmailError` | |
| `customerGroupIdError` | |
| `customerSalesChannelIdError` | |
| `customerCustomerNumberError` | |
| `customerPasswordError` | |
| `customerVatIdsError` | |
| `customerCompanyError` | |
| `customerPasswordNewError` | |
| `customerPasswordConfirmError` | |
| `accountTypeOptions` | |
| `isBusinessAccountType` | |
| `canUseCustomerImitation` | |
| `customerImitationWarning` | |
| `hasSingleBoundSalesChannelUrl` | |
| `currentUser` | |
| `emailIdnFilter` | |

### Examples

#### Example 1
Source: `sw-customer/view/sw-customer-detail-base/sw-customer-detail-base.html.twig`
```twig
<sw-customer-card
    :title="$tc('sw-customer.detailBase.labelAccountCard')"
    :customer="customer"
    :edit-mode="customerEditMode"
    :is-loading="isLoading"
>
    {% block sw_customer_detail_base_info_metadata %}
    <sw-customer-base-info
        :customer="customer"
        :is-loading="isLoading"
        :customer-edit-mode="customerEditMode"
    />
    {% endblock %}
</sw-customer-card>
```

## sw-customer-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |
| `validateEmail` | |
| `onSave` | |
| `onChangeSalesChannel` | |
| `createErrorMessageForCompanyField` | |
| `loadLanguage` | |
| `getDefaultSalutation` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `addressCompanyError` | |
| `customerRepository` | |
| `validCompanyField` | |
| `languageRepository` | |
| `languageCriteria` | |
| `languageId` | |
| `salutationRepository` | |
| `salutationCriteria` | |
| `salutationFilter` | |

### Examples

#### Basic Usage
```twig
<sw-customer-create>
    <!-- content -->
</sw-customer-create>
```

## sw-customer-default-addresses

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `renderFormattingAddress` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `defaultShippingAddressLink` | |
| `defaultBillingAddressLink` | |

### Examples

#### Example 1
Source: `sw-customer/view/sw-customer-detail-base/sw-customer-detail-base.html.twig`
```twig
                <sw-customer-default-addresses
                    :customer-edit-mode="customerEditMode"
                    :customer="customer"
                />
            </template>
            {% endblock %}
        </mt-card>
        {% endblock %}

        {% block sw_customer_detail_custom_field_sets %}
        <mt-card
            v-if="!!customerCustomFieldSets && customerCustomFieldSets.length > 0"
            position-identifier="sw-customer-detail-base-custom-field-sets"
            :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
            :is-loading="customer.isLoading"
```

## sw-customer-detail-addresses

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getAddressColumns` | |
| `setAddressSorting` | |
| `onCreateNewAddress` | |
| `createNewCustomerAddress` | |
| `onSaveAddress` | |
| `isValidAddress` | |
| `onCloseAddressModal` | |
| `onEditAddress` | |
| `onDeleteAddress` | |
| `onConfirmDeleteAddress` | |
| `onCloseDeleteAddressModal` | |
| `isDefaultAddress` | |
| `onChangeDefaultBillingAddress` | |
| `onChangeDefaultShippingAddress` | |
| `onDuplicateAddress` | |
| `onChangeDefaultAddress` | |
| `onChange` | |
| `refreshList` | |
| `createPrefix` | |
| `getDefaultSalutation` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerRepository` | |
| `customFieldSetRepository` | |
| `customerAddressRepository` | |
| `addressColumns` | |
| `addressRepository` | |
| `sortedAddresses` | |
| `salutationRepository` | |
| `salutationCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-customer-detail-addresses
    customer="..."
    customerEditMode="..."
>
    <!-- content -->
</sw-customer-detail-addresses>
```

## sw-customer-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| customerEditMode | `any` | `false` | yes |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-customer-detail-base
    customer="..."
    customerEditMode="..."
>
    <!-- content -->
</sw-customer-detail-base>
```

## sw-customer-detail-order

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChange` | |
| `getOrderColumns` | |
| `refreshList` | |
| `navigateToCreateOrder` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `orderColumns` | |
| `orderRepository` | |
| `emptyTitle` | |
| `currencyFilter` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-customer-detail-order
    customer="..."
>
    <!-- content -->
</sw-customer-detail-order>
```

## sw-customer-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customerId | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `loadCustomer` | |
| `createdComponent` | |
| `saveFinish` | |
| `validateEmail` | |
| `onSave` | |
| `onAbortButtonClick` | |
| `onActivateCustomerEditMode` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `validPassword` | |
| `acceptCustomerGroupRegistration` | |
| `declineCustomerGroupRegistration` | |
| `createErrorMessageForCompanyField` | |
| `getDefaultSalutation` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `customerRepository` | |
| `editMode` | |
| `defaultCriteria` | |
| `generalRoute` | |
| `addressesRoute` | |
| `ordersRoute` | |
| `emailHasChanged` | |
| `validCompanyField` | |
| `salutationRepository` | |
| `salutationCriteria` | |
| `swCustomerDetailBaseError` | |

### Examples

#### Basic Usage
```twig
<sw-customer-detail
    customerId="..."
>
    <!-- content -->
</sw-customer-detail>
```

## sw-customer-imitate-customer-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSalesChannelDomainMenuItemClick` | |
| `onCancel` | |
| `fetchSalesChannelDomains` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `modalDescription` | |
| `salesChannelDomainRepository` | |
| `currentUser` | |
| `salesChannelDomainCriteria` | |
| `hasSalesChannelDomains` | |

### Examples

#### Example 1
Source: `sw-customer/component/sw-customer-card/sw-customer-card.html.twig`
```twig
<sw-customer-imitate-customer-modal
    v-if="showImitateCustomerModal"
    :customer="customer"
    @modal-close="onCloseImitateCustomerModal"
/>
{% endblock %}

{% block sw_customer_card_action_customer_impersonation %}
<mt-button
    v-tooltip="{
        message: customerImitationWarning,
        disabled: canUseCustomerImitation,
        showOnDisabledElements: true
    }"
    :disabled="!canUseCustomerImitation"
```

## sw-customer-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onInlineEditSave` | |
| `getList` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `onChangeLanguage` | |
| `getCustomerColumns` | |
| `loadFilterValues` | |
| `updateCriteria` | |
| `onBulkEditItems` | |
| `onBulkEditModalOpen` | |
| `onBulkEditModalClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerRepository` | |
| `customerColumns` | |
| `defaultCriteria` | |
| `filterSelectCriteria` | |
| `listFilterOptions` | |
| `listFilters` | |
| `assetFilter` | |
| `emailIdnFilter` | |

### Examples

#### Basic Usage
```twig
<sw-customer-list>
    <!-- content -->
</sw-customer-list>
```

## sw-dashboard-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getGreetingTimeKey` | |
| `getGreetings` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `welcomeMessage` | |
| `welcomeSubline` | |
| `greetingName` | |

### Examples

#### Basic Usage
```twig
<sw-dashboard-index>
    <!-- content -->
</sw-dashboard-index>
```

## sw-dashboard-statistics

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `calculateTodayBucket` | |
| `initializeOrderData` | |
| `getHistoryOrderData` | |
| `fetchHistoryOrderDataCount` | |
| `fetchHistoryOrderDataSum` | |
| `fetchHistory` | |
| `fetchTodayData` | |
| `formatDateToISO` | |
| `formatChartHeadlineDate` | |
| `orderGridColumns` | |
| `getVariantFromOrderState` | |
| `parseDate` | |
| `onOrdersRangeUpdate` | |
| `onTurnoverRangeUpdate` | |
| `getCardSubtitle` | |
| `getDateAgo` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `rangesValueMap` | |
| `availableRanges` | |
| `chartOptionsOrderCount` | |
| `chartOptionsOrderSum` | |
| `orderRepository` | |
| `orderCountSeries` | |
| `orderCountToday` | |
| `orderSumMonthSeries` | |
| `orderSumSeries` | |
| `orderSumToday` | |
| `hasOrderToday` | |
| `hasOrderInMonth` | |
| `today` | |
| `todayBucketCount` | |
| `todayBucketSum` | |
| `systemCurrencyISOCode` | |
| `isSessionLoaded` | |
| `currencyFilter` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-dashboard/page/sw-dashboard-index/sw-dashboard-index.html.twig`
```twig
<sw-dashboard-statistics />
```

## sw-data-grid-column-boolean

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isInlineEdit | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| value | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.searchable" />
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.tokenize" />
```

#### Example 3
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
    <sw-data-grid-column-boolean
        v-model:value="item.status"
        :is-inline-edit="false"
    />
</template>
{% endblock %}

{% block sw_review_list_content_list_title %}
<template #column-title="{ item }">
    <div class="sw-review-text_ellipsis">
        <router-link :to="{ name: 'sw.review.detail', params: { id: item.id } }">
            {{ item.title }}
        </router-link>
    </div>
</template>
```

#### Example 4
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
                <sw-data-grid-column-boolean
                    :value="item.comment && item.comment.length > 0"
                    :is-inline-edit="false"
                />
            </template>
            {% endblock %}
        </sw-entity-listing>
        {% endblock %}
    </div>
    {% endblock %}
</template>
{% endblock %}

{% block sw_review_list_sidebar %}
<template #sidebar>
```

#### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-data-grid-column-boolean
        v-model:value="item.active"
        :is-inline-edit="isInlineEdit"
        :disabled="isActiveFieldInherited(item)"
    />

    <sw-inheritance-switch
        :is-inherited="isActiveFieldInherited(item)"
        class="sw-product-variants-overview__active-inherited-icon"
        @inheritance-restore="onActiveInheritanceRestore(item)"
        @inheritance-remove="onActiveInheritanceRemove(item)"
    />
</template>

<template v-else>
```

## sw-data-grid-column-position

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| item | `any` | — | yes |  |
| field | `any` | `'position'` | no |  |
| showValue | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| lower-position-value | — | |
| position-changed | — | |
| raise-position-value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onLowerPositionValue` | |
| `onRaisePositionValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `itemMin` | |
| `itemMax` | |

### Examples

#### Example 1
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-values-card/sw-settings-product-feature-sets-values-card.html.twig`
```twig
                <sw-data-grid-column-position
                    ref="columnPosition"
                    v-model:value="values"
                    :show-value="false"
                    :item="item"
                    :disabled="!allowEdit || undefined"
                    @position-changed="onPositionChange"
                />
            </template>
            {% endblock %}

        </sw-data-grid>
        {% endblock %}

    </div>
```

#### Example 2
Source: `sw-product/component/sw-product-cross-selling-assignment/sw-product-cross-selling-assignment.html.twig`
```twig
                <sw-data-grid-column-position
                    ref="columnPosition"
                    v-model:value="assignedProducts"
                    :show-value="true"
                    :item="item"
                />
            </template>
            {% endblock %}
        </sw-data-grid>
        {% endblock %}
        {% block sw_product_cross_selling_assignment_empty_state %}
        <mt-empty-state
            v-if="!total && !isLoadingGrid"
            class="sw-product-cross-selling-assignment__option-list-empty-state"
            :icon="$route.meta.$module.icon"
```

## sw-data-grid-inline-edit

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| column | `any` | — | yes |  |
| value | `any` | — | yes |  |
| compact | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitInput` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `inputFieldSize` | |

### Examples

#### Basic Usage
```twig
<sw-data-grid-inline-edit
    column="..."
    value="..."
>
    <!-- content -->
</sw-data-grid-inline-edit>
```

## sw-data-grid-settings

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| columns | `any` | — | yes |  |
| compact | `any` | `false` | yes |  |
| previews | `any` | `false` | yes |  |
| enablePreviews | `any` | `false` | yes |  |
| disabled | `any` | `false` | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additionalSettings | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-compact-mode | — | |
| change-preview-images | — | |
| change-column-visibility | — | |
| change-column-order | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeCompactMode` | |
| `onChangePreviews` | |
| `onChangeColumnVisibility` | |
| `onClickChangeColumnOrderUp` | |
| `onClickChangeColumnOrderDown` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `contextMenuClasses` | |

### Examples

#### Basic Usage
```twig
<sw-data-grid-settings
    columns="..."
    compact="..."
    previews="..."
>
    <!-- content -->
</sw-data-grid-settings>
```

## sw-data-grid-skeleton

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentColumns | `any` | — | yes |  |
| itemAmount | `any` | `7` | no |  |
| showSelection | `any` | `true` | no |  |
| showActions | `any` | `true` | no |  |
| hasResizeColumns | `any` | `false` | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `getRandomLength` | |

### Examples

#### Basic Usage
```twig
<sw-data-grid-skeleton
    currentColumns="..."
>
    <!-- content -->
</sw-data-grid-skeleton>
```

## sw-data-grid

> Advanced data grid with sorting, filtering, inline editing, column resizing, and selection.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| dataSource | `any` | — | yes |  |
| columns | `any` | — | yes |  |
| identifier | `any` | `''` | no |  |
| showSelection | `any` | `true` | no |  |
| showActions | `any` | `true` | no |  |
| showHeader | `any` | `true` | no |  |
| showSettings | `any` | `false` | no |  |
| fullPage | `any` | `false` | no |  |
| allowInlineEdit | `any` | `false` | no |  |
| allowColumnEdit | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |
| skeletonItemAmount | `any` | `7` | no |  |
| sortBy | `any` | `null` | no |  |
| sortDirection | `any` | `'ASC'` | no |  |
| naturalSorting | `any` | `false` | no |  |
| compactMode | `any` | `true` | no |  |
| plainAppearance | `any` | `false` | no |  |
| showPreviews | `any` | `true` | no |  |
| isRecordEditable | `any` | — | no |  |
| isRecordSelectable | `any` | — | no |  |
| rowsClickable | `any` | `false` | no |  |
| itemIdentifierProperty | `any` | `'id'` | no |  |
| maximumSelectItems | `any` | `null` | no |  |
| preSelection | `any` | `null` | no |  |
| isRecordDisabled | `any` | — | no |  |
| contextButtonMenuWidth | `any` | `220` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| bulk | — | |
| bulk-modals | — | |
| `column-label-${column.property}` | — | |
| additionalSettings | — | |
| customSettings | — | |
| selection-content | — | |
| `preview-${column.property}` | — | |
| `column-${column.property}` | — | |
| actions | item: item | |
| action-modals | item: item | |
| pagination | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |
| select-all-items | — | |
| select-item | — | |
| inline-edit-assign | — | |
| inline-edit-save | — | |
| inline-edit-cancel | — | |
| column-sort | — | |
| row-click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `initGridColumns` | |
| `findUserSetting` | |
| `findUserSettingById` | |
| `applyUserSettings` | |
| `findResizeColumns` | |
| `findPreviewSlots` | |
| `getDefaultColumns` | |
| `createUserGridSetting` | |
| `saveUserSettings` | |
| `getHeaderCellClasses` | |
| `getRowClasses` | |
| `getCellClasses` | |
| `onChangeCompactMode` | |
| `onChangePreviews` | |
| `onChangeColumnVisibility` | |
| `onChangeColumnOrder` | |
| `orderColumns` | |
| `enableInlineEdit` | |
| `hasColumnWithInlineEdit` | |
| `isInlineEdit` | |
| `disableInlineEdit` | |
| `hideColumn` | |
| `renderColumn` | |
| `selectAll` | |
| `selectItem` | |
| `isSelected` | |
| `resetSelection` | |
| `onClickSaveInlineEdit` | |
| `onClickCancelInlineEdit` | |
| `onDbClickCell` | |
| `onClickHeaderCell` | |
| `onRowClick` | |
| `onStartResize` | |
| `onStopResize` | |
| `onResize` | |
| `_handleColumnResizeClasses` | |
| `enableResizeMode` | |
| `setAllColumnElementWidths` | |
| `trackScrollX` | |
| `save` | |
| `revert` | |
| `sort` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `selectionCount` | |
| `reachMaximumSelectionExceed` | |
| `isSelectAllDisabled` | |
| `allSelectedChecked` | |
| `userConfigRepository` | |
| `currentUser` | |
| `userGridSettingCriteria` | |
| `hasInvisibleSelection` | |
| `currentVisibleColumns` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
<sw-data-grid
    class="sw-settings-country-currency-dependent-modal__grid"
    :data-source="currencyDependsValue"
    :is-loading="isLoading"
    :show-selection="false || undefined"
    :plain-appearance="true"
    :columns="countryCurrencyColumns"
>

    {% block sw_settings_country_currency_dependent_modal_content_hamburger_menu %}
    <template #customSettings>
        <sw-settings-country-currency-hamburger-menu
            :options="menuOptions"
            @currency-change="changeCurrencyDependentRow"
        />
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-data-grid
    v-if="items.length !== 0"
    ref="dataGrid"
    :data-source="items"
    :allow-inline-edit="acl.can('product_search_config.editor')"
    :is-loading="isLoading || isExcludedTermsLoading"
    :columns="getSearchableGeneralColumns"
    class="sw-settings-search__grid sw-settings-search-excluded-search-terms_grid"
    @inline-edit-save="onSaveEdit"
    @inline-edit-cancel="onCancelEdit"
    @select-item="selectionChanged"
>
    <template #bulk>
        <mt-button
            variant="critical"
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-data-grid
    v-if="products && products.length > 0"
    class="sw-settings-search-live-search__grid-result"
    :plain-appearance="true"
    :show-selection="false"
    :show-actions="false"
    :data-source="products"
    :is-loading="searchInProgress"
    :columns="searchColumns"
>

    {% block sw_settings_search_view_live_search_results_search_grid_columns %}
    {% block sw_settings_search_view_live_search_results_search_grid_name %}
    <template #column-name="{ item }">
        <sw-product-variant-info
```

#### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.searchable" />
```

#### Example 5
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-data-grid-column-boolean v-model:value="item.tokenize" />
```

## sw-date-filter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-reset | — | |
| filter-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `fromToFieldLabel` | |
| `updateFilter` | |
| `onTimeframeSelect` | |
| `resetFilter` | |
| `resetTimeframe` | |
| `getPreviousQuarterDates` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `dateType` | |
| `isDateTimeType` | |
| `showDivider` | |

### Examples

#### Basic Usage
```twig
<sw-date-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-date-filter>
```

## sw-datepicker-deprecated

> **Deprecated in 6.7** — Use `mt-datepicker` instead. Will be removed in 6.8.
> See mt-datepicker for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-datepicker>` | `<mt-datepicker>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
| config | `any` | — | no |  |
| dateType | `any` | `'date'` | no | Valid: `time`, `date`, `datetime` |
| placeholder | `any` | `''` | no |  |
| required | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| hideHint | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `beforeDestroyComponent` | |
| `setDatepickerValue` | |
| `getMergedConfig` | |
| `updateFlatpickrInstance` | |
| `createFlatpickrInstance` | |
| `getEventNames` | |
| `openDatepicker` | |
| `kebabToCamel` | |
| `unsetValue` | |
| `emitValue` | |
| `createConfig` | |
| `getDateStringFormat` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `locale` | |
| `currentFlatpickrConfig` | |
| `placeholderText` | |
| `suffixName` | |
| `noCalendar` | |
| `enableTime` | |
| `additionalAttrs` | |
| `userTimeZone` | |
| `timezoneFormattedValue` | |
| `showTimeZoneHint` | |
| `timeZoneHint` | |
| `is24HourFormat` | |

### Examples

#### Basic Usage
```twig
<sw-datepicker-deprecated>
    <!-- content -->
</sw-datepicker-deprecated>
```

## sw-datepicker

> **Migration wrapper** — Delegates to `mt-datepicker` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-datepicker for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
| placeholder | `any` | — | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `realValue` | |

### Examples

#### Basic Usage
```twig
<sw-datepicker>
    <!-- content -->
</sw-datepicker>
```

## sw-description-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| grid | `any` | `'1fr'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `descriptionListStyles` | |

### Examples

#### Example 1
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-description-list>
    {% block sw_customer_base_metadata_created_at_label %}
    <dt class="sw-review-base-info__label">
        {{ $tc('sw-review.detail.labelCreatedAt') }}
    </dt>
    {% endblock %}

    {% block sw_customer_base_metadata_created_at_content %}
    <dd>
        <sw-time-ago
            :date="review.createdAt"
            :date-time-format="{ month: '2-digit', day: '2-digit' }"
        />
    </dd>
    {% endblock %}
```

#### Example 2
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
<sw-description-list>
    {% block sw_customer_base_metadata_sales_channel_label %}
    <dt class="sw-review-base-info__label">
        {{ $tc('sw-review.detail.labelSalesChannel') }}
    </dt>
    {% endblock %}

    {% block sw_customer_base_metadata_sales_channel_content %}
    <dd>
        {{ review.salesChannel.name }}
    </dd>
    {% endblock %}
</sw-description-list>
```

#### Example 3
Source: `sw-customer/component/sw-customer-base-info/sw-customer-base-info.html.twig`
```twig
<sw-description-list>
    <dt class="sw-customer-base-info__label">
        {{ $tc('sw-customer.baseInfo.labelCompany') }}
    </dt>

    <dd>
        {{ customer.company }}
    </dd>
</sw-description-list>
```

#### Example 4
Source: `sw-customer/component/sw-customer-base-info/sw-customer-base-info.html.twig`
```twig
<sw-description-list>
    <dt class="sw-customer-base-info__label">
        {{ $tc('sw-customer.baseInfo.labelVatId') }}
    </dt>

    <dd>
        {{ customer.vatIds[0] || '-' }}
    </dd>
</sw-description-list>
```

#### Example 5
Source: `sw-order/component/sw-order-send-document-modal/sw-order-send-document-modal.html.twig`
```twig
<sw-description-list>
    <dt>{{ $tc('sw-order.documentSendModal.labelNumber') }}</dt>
    <dd>{{ document.config.documentNumber }}</dd>
</sw-description-list>
```

## sw-desktop

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `checkRouteSettings` | |
| `updateShopIdChangeModal` | |
| `closeModal` | |
| `onUpdateSearchFrequently` | |
| `getModuleMetadata` | |
| `getModuleMetadataWithSearchMatcher` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `desktopClasses` | |
| `currentUser` | |
| `isStaging` | |

### Examples

#### Basic Usage
```twig
<sw-desktop>
    <!-- content -->
</sw-desktop>
```

## sw-discard-changes-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| keep-editing | — | |
| discard-changes | — | |

### Methods

| Method | Description |
|--------|-------------|
| `keepEditing` | |
| `discardChanges` | |

### Examples

#### Example 1
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

#### Example 2
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

#### Example 3
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

## sw-duplicated-media-v2

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `loadDefaultOption` | |
| `saveDefaultOption` | |
| `handleMediaServiceUploadEvent` | |
| `isDuplicatedNameError` | |
| `updatePreviewData` | |
| `solveDuplicate` | |
| `renameFile` | |
| `skipAll` | |
| `skipCurrentFile` | |
| `skipFile` | |
| `replaceFile` | |
| `keepFile` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `additionalErrorCount` | |
| `hasAdditionalErrors` | |
| `currentTask` | |
| `buttonLabel` | |
| `dateFilter` | |
| `fileSizeFilter` | |
| `currentTaskDetails` | |
| `showModal` | |
| `isWorkingOnMultipleTasks` | |
| `options` | |

### Examples

#### Basic Usage
```twig
<sw-duplicated-media-v2>
    <!-- content -->
</sw-duplicated-media-v2>
```

## sw-dynamic-url-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getEmptyCategoryCollection` | |
| `getCategoryCollection` | |
| `parseLink` | |
| `replaceCategorySelection` | |
| `removeCategorySelection` | |
| `prepareLink` | |
| `removeLink` | |
| `onSelectFieldChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `seoUrlReplacePrefix` | |
| `entityFilter` | |
| `categoryRepository` | |
| `linkCategoryOptions` | |

### Examples

#### Example 1
Source: `sw-cms/elements/image/config/sw-cms-el-config-image.html.twig`
```twig
        <sw-dynamic-url-field
            v-model:value="element.config.url.value"
            :disabled="isInherited"
        />
    </template>
</sw-cms-inherit-wrapper>

<sw-cms-inherit-wrapper
    field="ariaLabel"
    :element="element"
    :label="$t('sw-cms.elements.image.config.label.ariaLabel')"
>
    <template #default="{ isInherited }">
        <mt-text-field
            v-model="element.config.ariaLabel.value"
```

## sw-email-field-deprecated

> **Deprecated in 6.7** — Use `mt-email-field` instead. Will be removed in 6.8.
> See mt-email-field for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-email-field>` | `<mt-email-field>` |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| prefix | — | |
| suffix | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |

### Examples

#### Example 1
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
<sw-email-field
    v-else-if="type === 'email'"
    class="sw-custom-entity-input-field__email"
    :value="currentValue"
    :label="label"
    :placeholder="placeholder"
    :help-text="helpText"
    @change="onChange"
/>-->

<!-- ToDo NEXT-22874 - Implement json field -->
<!--<sw-????
    v-else-if="type === 'json'"
    class="sw-custom-entity-input-field__json"
    :value="currentValue"
```

## sw-email-field

> **Migration wrapper** — Delegates to `mt-email-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-email-field for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modelValue | `any` | `null` | no |  |
| value | `any` | `null` | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| name | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSlots` | |
| `handleUpdateModelValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `compatValue` | |

### Examples

#### Example 1
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
<sw-email-field
    v-else-if="type === 'email'"
    class="sw-custom-entity-input-field__email"
    :value="currentValue"
    :label="label"
    :placeholder="placeholder"
    :help-text="helpText"
    @change="onChange"
/>-->

<!-- ToDo NEXT-22874 - Implement json field -->
<!--<sw-????
    v-else-if="type === 'json'"
    class="sw-custom-entity-input-field__json"
    :value="currentValue"
```

## sw-empty-state

> Shopware Administration component.

- [Slots](#slots)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | `null` | yes |  |
| subline | `any` | `null` | no |  |
| showDescription | `any` | `true` | no |  |
| color | `any` | `null` | no |  |
| icon | `any` | `null` | no |  |
| absolute | `any` | `true` | no |  |
| emptyModule | `any` | `false` | no |  |
| autoHeight | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| icon | — | |
| actions | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `moduleColor` | |
| `moduleDescription` | |
| `moduleIcon` | |
| `hasActionSlot` | |
| `classes` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
<sw-empty-state
    v-if="showEmptyState"
    :title="$tc('sw-settings-search.generalTab.textEmptyStateExcludedSearchTerms')"
    :show-description="false"
    :has-action-slot="true"
    :absolute="false"
    class="sw-empty-state"
>
    <template #icon>
        {% block sw_settings_search_excluded_search_terms_empty_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-search.generalTab.textEmptyStateExcludedSearchTerms')"
        >
        {% endblock %}
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-empty-state
    v-if="isEmpty"
    :title="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
    :show-description="false"
    :has-action-slot="true"
    :absolute="false"
>
    <template #icon>
        {% block sw_settings_search_searchable_content_general_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
        >
        {% endblock %}
    </template>
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content-customfields/sw-settings-search-searchable-content-customfields.html.twig`
```twig
<sw-empty-state
    v-if="isEmpty"
    :title="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
    :show-description="false"
    :has-action-slot="true"
    :absolute="false"
>
    <template #icon>
        {% block sw_settings_search_searchable_content_customfields_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-search.generalTab.textEmptyStateSearchableContent')"
        >
        {% endblock %}
    </template>
```

#### Example 4
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-empty-state
    v-else
    class="sw-settings-listing-index__sorting-options-empty-state"
    :title="$tc('sw-settings-listing.index.productSorting.emptyState.title')"
    :subline="$tc('sw-settings-listing.index.productSorting.emptyState.subline')"
    :absolute="false"
>

    {% block sw_settings_listing_content_card_view_options_card_empty_state_icon %}
    <template #icon>
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            :alt="$tc('sw-settings-listing.index.productSorting.emptyState.title')"
        >
    </template>
```

#### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-option-criteria-grid/sw-settings-listing-option-criteria-grid.html.twig`
```twig
<sw-empty-state
    v-else
    class="sw-settings-listing-option-criteria-grid__criteria-empty-state"
    title=""
    :subline="$tc('sw-settings-listing.base.criteria.emptyStateSubline')"
>

    {% block sw_settings_listing_option_criteria_card_empty_state_icon %}
    <template #icon>
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            alt=""
        >
    </template>
    {% endblock %}
```

## sw-entity-advanced-selection-modal-grid

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isRecordSelectable | `any` | — | no |  |
| isRecordSelectableCallback | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getSelectableTooltip` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isSelectAllDisabled` | |
| `allSelectedChecked` | |

### Examples

#### Basic Usage
```twig
<sw-entity-advanced-selection-modal-grid>
    <!-- content -->
</sw-entity-advanced-selection-modal-grid>
```

## sw-entity-advanced-selection-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entityName | `any` | — | yes |  |
| entityDisplayText | `any` | — | yes |  |
| storeKey | `any` | — | yes |  |
| entityColumns | `any` | — | yes |  |
| entityFilters | `any` | — | yes |  |
| emptyImagePath | `any` | — | no |  |
| emptyIcon | `any` | `'solid-content'` | no |  |
| entityAssociations | `any` | — | no |  |
| isSingleSelect | `any` | `false` | no |  |
| isRecordSelectableCallback | `any` | — | no |  |
| criteriaFilters | `any` | — | no |  |
| criteriaAggregations | `any` | — | no |  |
| entityContext | `any` | — | no |  |
| initialSearchTerm | `any` | — | no |  |
| initialSelection | `any` | — | no |  |
| disablePreviews | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| `preview-${column.property}` | — | |
| `column-${column.property}` | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| selection-submit | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `onSelectionChange` | |
| `onApply` | |
| `updateCriteria` | |
| `debouncedGetList` | |
| `clearFilters` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `entityRepository` | |
| `entityDefinition` | |
| `assignmentProperties` | |
| `allEntityAssociations` | |
| `entityCriteria` | |
| `activeFilterNumber` | |
| `defaultFilters` | |
| `listFilters` | |
| `previewColumns` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-entity-advanced-selection-modal
    entityName="..."
    entityDisplayText="..."
    storeKey="..."
>
    <!-- content -->
</sw-entity-advanced-selection-modal>
```

## sw-entity-listing

> Extended data grid for entity listing with pagination, search, and CRUD operations.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| detailRoute | `any` | `null` | no |  |
| repository | `any` | — | yes |  |
| items | `any` | `null` | no |  |
| dataSource | `null \| null` | — | no |  |
| showSettings | `any` | `true` | no |  |
| steps | `any` | — | no |  |
| fullPage | `any` | `true` | no |  |
| allowInlineEdit | `any` | `true` | no |  |
| allowColumnEdit | `any` | `true` | no |  |
| criteriaLimit | `any` | `25` | no |  |
| allowEdit | `any` | `true` | no |  |
| allowView | `any` | `false` | no |  |
| allowDelete | `any` | `true` | no |  |
| disableDataFetching | `any` | `false` | no |  |
| naturalSorting | `any` | `false` | no |  |
| allowBulkEdit | `any` | `false` | no |  |
| showBulkEditModal | `any` | `false` | no |  |
| bulkGridEditColumns | `any` | — | no |  |
| maximumSelectItems | `any` | `1000` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| bulk-additional | — | |
| bulk-edit-modal | — | |
| bulk-modal-delete-confirm-text | — | |
| bulk-modal-cancel | — | |
| bulk-modal-delete-items | — | |
| bulk-modals-additional | — | |
| detail-action | — | |
| more-actions | — | |
| delete-action | — | |
| delete-confirm-text | — | |
| delete-modal-footer | — | |
| delete-modal-cancel | — | |
| delete-modal-delete-item | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-records | — | |
| delete-item-finish | — | |
| delete-item-failed | — | |
| delete-items-failed | — | |
| items-delete-finish | — | |
| inline-edit-save | — | |
| inline-edit-cancel | — | |
| column-sort | — | |
| page-change | — | |
| bulk-edit-modal-open | — | |
| bulk-edit-modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `applyResult` | |
| `deleteItem` | |
| `deleteItems` | |
| `deleteItemsFinish` | |
| `doSearch` | |
| `save` | |
| `revert` | |
| `sort` | |
| `paginate` | |
| `showDelete` | |
| `closeModal` | |
| `onClickBulkEdit` | |
| `onCloseBulkEditModal` | |
| `mountedComponent` | |
| `initGridColumns` | |
| `findUserSetting` | |
| `findUserSettingById` | |
| `applyUserSettings` | |
| `findResizeColumns` | |
| `findPreviewSlots` | |
| `getDefaultColumns` | |
| `createUserGridSetting` | |
| `saveUserSettings` | |
| `getHeaderCellClasses` | |
| `getRowClasses` | |
| `getCellClasses` | |
| `onChangeCompactMode` | |
| `onChangePreviews` | |
| `onChangeColumnVisibility` | |
| `onChangeColumnOrder` | |
| `orderColumns` | |
| `enableInlineEdit` | |
| `hasColumnWithInlineEdit` | |
| `isInlineEdit` | |
| `disableInlineEdit` | |
| `hideColumn` | |
| `renderColumn` | |
| `selectAll` | |
| `selectItem` | |
| `isSelected` | |
| `resetSelection` | |
| `onClickSaveInlineEdit` | |
| `onClickCancelInlineEdit` | |
| `onDbClickCell` | |
| `onClickHeaderCell` | |
| `onRowClick` | |
| `onStartResize` | |
| `onStopResize` | |
| `onResize` | |
| `_handleColumnResizeClasses` | |
| `enableResizeMode` | |
| `setAllColumnElementWidths` | |
| `trackScrollX` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `detailPageLinkText` | |
| `internalDataSource` | |
| `classes` | |
| `selectionCount` | |
| `reachMaximumSelectionExceed` | |
| `isSelectAllDisabled` | |
| `allSelectedChecked` | |
| `userConfigRepository` | |
| `currentUser` | |
| `userGridSettingCriteria` | |
| `hasInvisibleSelection` | |
| `currentVisibleColumns` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-entity-listing
    ref="swSettingsCountryGrid"
    class="sw-settings-country-list-grid"
    :data-source="country"
    :columns="getCountryColumns()"
    :repository="countryRepository"
    :full-page="false"
    detail-route="sw.settings.country.detail"
    :show-selection="true"
    :is-loading="isLoading"
    :allow-view="acl.can('country.viewer') || undefined"
    :allow-edit="acl.can('country.editor') || undefined"
    :allow-inline-edit="acl.can('country.editor') || undefined"
    :allow-delete="acl.can('country.deleter') || undefined"
    @inline-edit-save="onInlineEditSave"
```

#### Example 2
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
<sw-entity-listing
    :data-source="logs"
    :columns="logColumns"
    :full-page="true"
    :show-settings="true"
    :show-selection="undefined"
    :show-actions="true"
    :sort-by="sortBy"
    :sort-direction="sortDirection"
    :is-loading="isLoading"
    :allow-column-edit="true"
    :repository="logEntryRepository"
    identifier="sw-log-entry-list"
>

```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
<sw-entity-listing
    v-if="!isEmpty"
    ref="swSettingsSearchableContentGrid"
    class="sw-settings-search__searchable-content-list"
    :columns="columns"
    :repository="repository"
    :allow-column-edit="false"
    :full-page="false"
    :show-settings="false"
    :show-selection="false"
    :is-loading="isLoading"
    :data-source="searchConfigs"
    :skeleton-item-amount="searchConfigs && searchConfigs.length"
    :allow-inline-edit="acl.can('product_search_config.editor')"
    @inline-edit-save="onInlineEditSave"
```

#### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content-customfields/sw-settings-search-searchable-content-customfields.html.twig`
```twig
<sw-entity-listing
    v-if="!isEmpty"
    ref="customGrid"
    class="sw-settings-search__searchable-content-list"
    :columns="columns"
    :repository="repository"
    :allow-column-edit="false"
    :full-page="false"
    :show-settings="false"
    :show-selection="false"
    :is-loading="isLoading"
    :data-source="searchConfigs"
    :allow-inline-edit="acl.can('product_search_config.editor')"
    :allow-edit="acl.can('product_search_config.editor')"
    :allow-delete="acl.can('product_search_config.deleter')"
```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-list/sw-settings-salutation-list.html.twig`
```twig
                    <sw-entity-listing
                        class="sw-settings-salutation-list-grid"
                        :repository="salutationRepository"
                        :is-loading="isLoading"
                        :data-source="salutations"
                        :columns="columns"
                        identifier="sw-settings-salutation-list"
                        :sort-by="sortBy"
                        :sort-direction="sortDirection"
                        :full-page="false"
                        detail-route="sw.settings.salutation.detail"
                        :disable-data-fetching="true"
                        :show-selection="acl.can('salutation.deleter') || undefined"
                        :allow-edit="acl.can('salutation.editor') || undefined"
                        :allow-inline-edit="acl.can('salutation.editor') || undefined"
```

## sw-entity-many-to-many-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| labelProperty | `any` | `'name'` | no |  |
| resultLimit | `any` | `25` | no |  |
| valueLimit | `any` | `5` | no |  |
| localMode | `any` | `false` | no |  |
| criteria | `any` | — | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| entityCollection | `any` | — | yes |  |
| context | `any` | — | no |  |
| advancedSelectionComponent | `any` | `''` | no |  |
| advancedSelectionParameters | `any` | — | no |  |

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
| search | — | |
| update:entityCollection | — | |
| item-add | — | |
| item-remove | — | |
| search-term-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initData` | |
| `isSelected` | |
| `fetchDisplayItems` | |
| `displayAssigned` | |
| `displaySearch` | |
| `sendSearchRequest` | |
| `findAssignedEntities` | |
| `search` | |
| `paginateResult` | |
| `paginateDisplayList` | |
| `emitChanges` | |
| `addItem` | |
| `remove` | |
| `removeIdFromList` | |
| `resetSearchCriteria` | |
| `onSelectExpanded` | |
| `onSelectCollapsed` | |
| `onSearchTermChange` | |
| `resetActiveItem` | |
| `debouncedSearch` | |
| `resetResultCollection` | |
| `getKey` | |
| `openAdvancedSelectionModal` | |
| `closeAdvancedSelectionModal` | |
| `onAdvancedSelectionSubmit` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `repository` | |
| `searchRepository` | |
| `selectedIds` | |
| `visibleValues` | |
| `invisibleValueCount` | |
| `isAdvancedSelectionActive` | |

### Examples

#### Basic Usage
```twig
<sw-entity-many-to-many-select>
    <!-- content -->
</sw-entity-many-to-many-select>
```

## sw-entity-multi-id-select

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| repository | `any` | — | yes |  |
| criteria | `any` | — | no |  |
| context | `any` | — | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-label-property | — | |
| result-description-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateIds` | |

### Examples

#### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
<sw-entity-multi-id-select
    v-model:value="configData[null]['core.defaultSalesChannel.salesChannel']"
    :repository="salesChannelRepository"
    :label="$tc('sw-settings.system-config.labelSalesChannelSelect')"
    :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
    @update:value="updateSalesChannel"
/>
{% endblock %}

{% block sw_settings_listing_default_sales_channeld_setting %}
<div class="sw-settings-listing-default-sales-channel__options-container">
    {% block sw_settings_listing_default_sales_channel_setting_active %}
    <mt-switch
        v-model="configData[null]['core.defaultSalesChannel.active']"
        class="sw-settings-listing-default-sales-channel__active-switch"
```

#### Example 2
Source: `sw-flow/component/modals/sw-flow-mail-send-modal/sw-flow-mail-send-modal.html.twig`
```twig
<sw-entity-multi-id-select
    v-model:value="documentTypeIds"
    name="sw-field--documentTypeIds"
    :repository="documentTypeRepository"
    class="sw-flow-mail-send-modal__document-types"
    :label="$tc('sw-flow.modals.mail.labelLatestDocuments')"
    :placeholder="$tc('sw-flow.modals.mail.placeholderLatestDocuments')"
/>
{% endblock %}

{% block sw_flow_mail_send_create_new_template %}
<sw-flow-create-mail-template-modal
    v-if="showCreateMailTemplateModal"
    class="sw-flow-mail-send-modal__create-mail-template"
    @process-finish="onCreateMailTemplateSuccess"
```

#### Example 3
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-entity-multi-id-select
    v-else-if="isMultiSelectValue"
    ref="product-stream-value-select-entity-multi-id-select"
    v-model:value="multiValue"
    size="medium"
    :repository="entityCustomFieldRepository"
    :criteria="customFieldCriteria"
    :context="context"
    :disabled="disabled"
    @select-collapsed="onSelectCollapsed"
    @search-term-change="setSearchTerm"
>
    <template #result-label-property="{ item, searchTerm, highlightSearchTerm }">
        <slot
            name="result-label-property"
```

#### Example 4
Source: `sw-product-stream/component/sw-product-stream-value/sw-product-stream-value.html.twig`
```twig
<sw-entity-multi-id-select
    v-else-if="definition.entity === 'property_group_option' && (actualCondition.type === 'equalsAny' || actualCondition.type === 'equalsAll')"
    ref="product-stream-value-select-multi-value"
    v-model:value="multiValue"
    size="medium"
    :repository="repository"
    :criteria="propertyCriteria"
    :context="context"
    :disabled="disabled"
    @select-collapsed="onSelectCollapsed"
    @search-term-change="setSearchTerm"
>

    <template #selection-label-property="{ item }">
        <slot
```

## sw-entity-multi-select

> Multi-select dropdown for Shopware entities with tag display.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| labelProperty | `null \| null` | `'name'` | no |  |
| resultLimit | `any` | `25` | no |  |
| valueLimit | `any` | `5` | no |  |
| placeholder | `any` | `''` | no |  |
| alwaysShowPlaceholder | `any` | `false` | no |  |
| criteria | `any` | — | no |  |
| disabled | `any` | — | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| entityCollection | `any` | — | yes |  |
| entityName | `any` | `null` | no |  |
| context | `any` | — | no |  |
| hideLabels | `any` | `false` | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| descriptionPosition | `any` | `'right'` | no | Valid: `bottom`, `right` |
| advancedSelectionComponent | `any` | — | no |  |
| advancedSelectionParameters | `any` | — | no |  |
| displayVariants | `any` | `false` | no |  |
| label | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-preview | — | |
| result-label-property | — | |
| result-description-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| search | — | |
| update:entityCollection | — | |
| item-add | — | |
| item-remove | — | |
| display-values-expand | — | |
| search-term-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `refreshCurrentCollection` | |
| `createEmptyCollection` | |
| `isSelected` | |
| `loadData` | |
| `search` | |
| `displaySearch` | |
| `displayLabelProperty` | |
| `resetActiveItem` | |
| `resetCriteria` | |
| `paginate` | |
| `emitChanges` | |
| `addItem` | |
| `remove` | |
| `removeLastItem` | |
| `onSelectExpanded` | |
| `onSelectCollapsed` | |
| `expandValueLimit` | |
| `onSearchTermChange` | |
| `debouncedSearch` | |
| `resetResultCollection` | |
| `getKey` | |
| `isSelectionDisabled` | |
| `openAdvancedSelectionModal` | |
| `closeAdvancedSelectionModal` | |
| `onAdvancedSelectionSubmit` | |
| `clearSelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `repository` | |
| `visibleValues` | |
| `totalValuesCount` | |
| `invisibleValueCount` | |
| `isAdvancedSelectionActive` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-entity-multi-select
    v-else-if="bulkEditProduct[formField.name].type === 'remove'"
    class="sw-bulk-edit-product-base__advanced-prices-selection"
    :placeholder="$tc('sw-bulk-edit.product.advancedPrices.selectRule')"
    :criteria="ruleCriteria"
    entity-name="rule"
    :entity-collection="!!bulkEditProduct[formField.name].isInherited ? [] : entity[formField.name]"
    :disabled="!!bulkEditProduct[formField.name].isInherited || undefined"
    @update:entity-collection="onRuleChange"
>
    <template #selection-label-property="{ item }">
        {{ item.ruleName }}
    </template>

    <template #result-item="{ item, index, labelProperty, isSelected, addItem, getKey }">
```

#### Example 2
Source: `sw-category/view/sw-landing-page-detail-base/sw-landing-page-detail-base.html.twig`
```twig
    <sw-entity-multi-select
        v-model:entity-collection="landingPage.salesChannels"
        required
        class="sw-landing-page-detail-base__sales_channel"
        entity-name="sales_channel"
        :disabled="!acl.can('landing_page.editor')"
        :label="$tc('sw-landing-page.base.seo.labelSalesChannel')"
        :placeholder="$tc('sw-landing-page.base.seo.placeholderSalesChannel')"
        :error="landingPageSalesChannelsError"
    />
    {% endblock %}

    {% block sw_landing_page_detail_base_information_tags %}
    <sw-entity-tag-select
        v-if="landingPage && !isLoading"
```

#### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
    <sw-entity-multi-select
        v-model:entity-collection="page.landingPages"
        class="sw-cms-layout-assignment-modal__landing-page-select"
        :label="$tc('global.entities.landing_page')"
        :placeholder="$tc('sw-cms.components.cmsLayoutAssignmentModal.placeholderLandingPages')"
        entity-name="landing_page"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_cms_layout_assignment_modal_category_select %}
<template v-if="!isProductDetailPage && active === 'categories'">

    {% block sw_cms_layout_assignment_modal_category_select_field %}
```

#### Example 4
Source: `sw-cms/elements/product-listing/config/sw-cms-el-config-product-listing.html.twig`
```twig
<sw-entity-multi-select
    v-model:entity-collection="productSortings"
    class="sw-cms-el-config-product-listing-config-sorting-grid__select"
    label-property="label"
    :criteria="allProductSortingsCriteria"
    :hide-labels="true"
    :placeholder="$t('sw-cms.elements.productListing.config.sorting.placeHolderProductSortings')"
    :disabled="isInherited"
>
    <template #result-item="{ item, index, labelProperty, valueProperty, searchTerm, highlightSearchTerm, isSelected, addItem, getKey }">
        <slot
            name="result-item"
            v-bind="{ item, index, labelProperty, valueProperty: 'id', searchTerm, highlightSearchTerm, isSelected, addItem, getKey }"
        >
            <sw-select-result
```

#### Example 5
Source: `sw-cms/elements/product-slider/config/sw-cms-el-config-product-slider.html.twig`
```twig
<sw-entity-multi-select
    v-model:entity-collection="productCollection"
    class="sw-cms-el-config-product-slider__tab-content-products"
    :placeholder="$tc('sw-cms.elements.productSlider.config.placeholder.selection')"
    :context="productMultiSelectContext"
    :criteria="productMediaFilter"
    :disabled="isInherited"
    @update:entity-collection="onProductsChange"
>
    <template #selection-label-property="{ item }">
        <sw-product-variant-info :variations="item.variation">
            {{ item.translated.name || item.name }}
        </sw-product-variant-info>
    </template>
    <template #result-item="{ item, index }">
```

## sw-entity-single-select

> Single-select dropdown for Shopware entities with search and API integration.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| resetOption | `any` | `''` | no |  |
| labelProperty | `null \| null` | `'name'` | no |  |
| labelCallback | `any` | `null` | no |  |
| entity | `any` | — | yes |  |
| resultLimit | `any` | `25` | no |  |
| criteria | `any` | — | no |  |
| context | `any` | — | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| disableAutoClose | `any` | `false` | no |  |
| disabledSelectionTooltip | `any` | — | no |  |
| descriptionPosition | `any` | `'right'` | no | Valid: `bottom`, `right`, `left` |
| allowEntityCreation | `any` | `false` | no |  |
| entityCreationLabel | `any` | — | no |  |
| advancedSelectionComponent | `any` | `''` | no |  |
| advancedSelectionParameters | `any` | — | no |  |
| displayVariants | `any` | `false` | no |  |
| shouldShowActiveState | `any` | `false` | no |  |
| disabled | `any` | — | no |  |
| label | `any` | — | no |  |
| size | `any` | `'default'` | no |  |
| popoverClasses | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| before-item-list | — | |
| result-item | — | |
| result-label-property | — | |
| result-description-property | — | |
| after-item-list | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| search | — | |
| option-select | — | |
| before-selection-clear | — | |
| search-term-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadSelected` | |
| `createCollection` | |
| `isSelected` | |
| `debouncedSearch` | |
| `search` | |
| `handleSearchPromise` | |
| `paginate` | |
| `loadData` | |
| `checkEntityExists` | |
| `displaySearch` | |
| `displayLabelProperty` | |
| `onSelectExpanded` | |
| `tryGetSearchText` | |
| `onSelectCollapsed` | |
| `closeResultList` | |
| `setValue` | |
| `addItem` | |
| `clearSelection` | |
| `clearInput` | |
| `resetActiveItem` | |
| `onInputSearchTerm` | |
| `getKey` | |
| `isSelectionDisabled` | |
| `getDisabledSelectionTooltip` | |
| `createNewEntity` | |
| `filterSearchGeneratedTags` | |
| `openAdvancedSelectionModal` | |
| `closeAdvancedSelectionModal` | |
| `onAdvancedSelectionSubmit` | |
| `getActiveIconColor` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `inputClasses` | |
| `selectionTextClasses` | |
| `repository` | |
| `results` | |
| `isAdvancedSelectionActive` | |
| `advancedSelectionInitialSearchTerm` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
            <sw-entity-single-select
                v-model:value="customerId"
                class="sw-settings-country-address-handling__customer-select"
                :label="$tc('sw-settings-country.detail.labelCustomer')"
                :placeholder="$tc('sw-settings-country.detail.placeholderSelectCustomer')"
                entity="customer"
                show-clearable-button
                :criteria="customerCriteria"
                :label-callback="customerLabel"
                @update:value="onChangeCustomer"
            />

            <sw-settings-country-preview-template :formatting-address="formattingAddress" />

            <mt-button
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
        <sw-entity-single-select
            v-model:value="country.customerTax.currencyId"
            name="sw-field--country-customerTax-currencyId"
            class="sw-settings-country-general__customer-select-currency sw-settings-country-general__select"
            entity="currency"
            bordered
            show-clearable-button
            :disabled="!acl.can('country.editor') || undefined"
        />
    </template>
</mt-number-field>
{% endblock %}
{% endblock %}

{% block sw_settings_country_general_content_show_tax_free_currency_dependent_values %}
```

#### Example 3
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
        <sw-entity-single-select
            v-model:value="country.companyTax.currencyId"
            name="sw-field--country-companyTax-currencyId"
            class="sw-settings-country-general__company-select-currency sw-settings-country-general__select"
            entity="currency"
            show-clearable-button
            :disabled="!acl.can('country.editor') || undefined"
        />
    </template>
</mt-number-field>
{% endblock %}
{% endblock %}

{% block sw_settings_country_general_content_show_company_tax_free_currency_dependent_values %}
<sw-container
```

#### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content-customfields/sw-settings-search-searchable-content-customfields.html.twig`
```twig
<sw-entity-single-select
    v-model:value="currentCustomFieldId"
    class="sw-settings-search-custom-field-select"
    entity="custom_field"
    :criteria="customFieldFilteredCriteria"
    show-clearable-button
    @update:value="(id, customfield) => onSelectCustomField(customfield)"
>

    <template #selection-label-property="{ item }">
        {{ showCustomFieldWithSet(item) }}
    </template>

    <template #result-label-property="{ item }">
        {{ showCustomFieldWithSet(item) }}
```

#### Example 5
Source: `sw-settings-number-range/page/sw-settings-number-range-detail/sw-settings-number-range-detail.html.twig`
```twig
<sw-entity-single-select
    v-if="numberRange.type"
    id="numberRangeTypes"
    v-model:value="numberRange.typeId"
    name="sw-field--numberRange-typeId"
    entity="number_range_type"
    class="sw-number-range-detail__select-type"
    :disabled="disableNumberRangeTypeSelect"
    required
    show-clearable-button
    label-property="typeName"
    :label="$tc('sw-settings-number-range.detail.labelType')"
    :criteria="numberRange.type.global ? numberRangeTypeCriteriaGlobal : numberRangeTypeCriteria"
    :error="numberRangeTypeIdError"
    @update:value="onChangeType"
```

## sw-entity-tag-select

> Tag-based multi-select for entity associations.

### Methods

| Method | Description |
|--------|-------------|
| `resetActiveItem` | |
| `search` | |
| `addItem` | |
| `createNewTag` | |
| `checkTagExists` | |
| `filterSearchGeneratedTags` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-base/sw-category-detail-base.html.twig`
```twig
    <sw-entity-tag-select
        v-if="category && !isLoading"
        v-model:entity-collection="category.tags"
        class="sw-category-detail-base__tags"
        :label="$tc('sw-category.base.general.labelCategoryTags')"
        :placeholder="$tc('sw-category.base.general.labelCategoryTagsPlaceholder')"
        :disabled="!acl.can('category.editor')"
    />
    {% endblock %}

    {% block sw_category_detail_information_type %}
    <div class="sw-category-detail-base__type-container">

        {% block sw_category_detail_information_type_select %}
        <sw-single-select
```

#### Example 2
Source: `sw-category/view/sw-landing-page-detail-base/sw-landing-page-detail-base.html.twig`
```twig
    <sw-entity-tag-select
        v-if="landingPage && !isLoading"
        v-model:entity-collection="landingPage.tags"
        class="sw-landing-page-detail-base__tags"
        :label="$tc('sw-landing-page.base.general.labelTags')"
        :placeholder="$tc('sw-landing-page.base.general.labelTagsPlaceholder')"
        :disabled="!acl.can('landing_page.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_landing_page_detail_base_seo %}
<mt-card
    position-identifier="sw-landing-page-detail-seo"
```

#### Example 3
Source: `sw-media/component/sidebar/sw-media-tag/sw-media-tag.html.twig`
```twig
            <sw-entity-tag-select
                v-model:entity-collection="media.tags"
                :disabled="disabled"
                @update:entity-collection="handleChange"
            />
        </template>
        {% endblock %}
    </sw-media-collapse>
</div>
{% endblock %}

```

#### Example 4
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
    <sw-entity-tag-select
        v-if="!isLoading"
        v-model:entity-collection="shippingMethod.tags"
        :disabled="!acl.can('shipping.editor') || undefined"
        :placeholder="$tc('sw-product.categoryForm.placeholderTags')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_settings_shipping_detail_top_ruleshippingPriceStore %}
<mt-card
    position-identifier="sw-settings-shipping-detail-condition-container"
    class="sw-settings-shipping-detail__condition_container"
    :title="$tc('sw-settings-shipping.detail.topRule')"
```

#### Example 5
Source: `sw-settings-rule/view/sw-settings-rule-detail-base/sw-settings-rule-detail-base.html.twig`
```twig
            <sw-entity-tag-select
                v-if="rule"
                v-model:entity-collection="rule.tags"
                name="sw-field--rule-tags"
                class="sw-settings-rule-detail__tags-field"
                :label="$tc('global.sw-tag-field.title')"
                :disabled="!acl.can('rule.editor') || undefined"
                :placeholder="$tc('sw-settings-rule.detail.placeholderTags')"
            />
            {% endblock %}
        </div>
    </template>
    <sw-loader v-else />
</mt-card>
{% endblock %}
```

## sw-error-boundary

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `logErrorInEntries` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `logEntryRepository` | |

### Examples

#### Basic Usage
```twig
<sw-error-boundary>
    <!-- content -->
</sw-error-boundary>
```

## sw-error-summary

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `errors` | |
| `errorEntries` | |
| `errorCount` | |

### Examples

#### Basic Usage
```twig
<sw-error-summary>
    <!-- content -->
</sw-error-summary>
```

## sw-error

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| errorObject | `any` | — | no |  |
| routerLink | `any` | — | no |  |
| linkText | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `error` | |
| `imagePath` | |
| `message` | |
| `statusCode` | |
| `showStack` | |
| `showLink` | |

### Examples

#### Basic Usage
```twig
<sw-error>
    <!-- content -->
</sw-error>
```

## sw-existence-filter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |

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
| `value` | |
| `filterOptions` | |

### Examples

#### Basic Usage
```twig
<sw-existence-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-existence-filter>
```

## sw-extension-adding-failed

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| title | `any` | `null` | no |  |
| detail | `any` | `null` | no |  |
| documentationLink | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `myExtensions` | |
| `extension` | |
| `isRent` | |
| `headline` | |
| `text` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-card-bought/sw-extension-card-bought.html.twig`
```twig
    <sw-extension-adding-failed
        :extension-name="extension.name"
        :title="installationFailedError && installationFailedError.title"
        :detail="installationFailedError && installationFailedError.message"
        :documentation-link="installationFailedError && installationFailedError.parameters && installationFailedError.parameters.documentationLink"
        @close="closeInstallationFailedNotification"
    />
</sw-modal>
{% endblock %}

```

## sw-extension-adding-success

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

### Examples

#### Basic Usage
```twig
<sw-extension-adding-success>
    <!-- content -->
</sw-extension-adding-success>
```

## sw-extension-app-module-error-page

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `goBack` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-app-module-page/sw-extension-app-module-page.html.twig`
```twig
<sw-extension-app-module-error-page />
```

## sw-extension-app-module-page

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| appName | `any` | — | yes |  |
| moduleName | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `translate` | |
| `onContentLoaded` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentLocale` | |
| `fallbackLocale` | |
| `appDefinition` | |
| `moduleDefinition` | |
| `showSmartBar` | |
| `suspend` | |
| `heading` | |
| `entryPoint` | |
| `origin` | |
| `loadedMessage` | |

### Examples

#### Basic Usage
```twig
<sw-extension-app-module-page
    appName="..."
>
    <!-- content -->
</sw-extension-app-module-page>
```

## sw-extension-card-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-list | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitUpdateList` | |
| `getHelp` | |
| `openPrivacyAndSafety` | |
| `openRemovalModal` | |
| `openUninstallModal` | |
| `closeRemovalModal` | |
| `closeUninstallModal` | |
| `closeModalAndUninstallExtension` | |
| `updateExtension` | |
| `closeModalAndRemoveExtension` | |
| `openExtension` | |
| `openPermissionsModalForInstall` | |
| `openPermissionsModal` | |
| `closePermissionsModal` | |
| `closePermissionsModalAndInstallExtension` | |
| `changeExtensionStatus` | |
| `installExtension` | |
| `installAndActivateExtension` | |
| `removeExtension` | |
| `cancelAndRemoveExtension` | |
| `openPrivacyModal` | |
| `closePrivacyModal` | |
| `clearCacheAndReloadPage` | |
| `openConsentAffirmationModal` | |
| `closeConsentAffirmationModal` | |
| `closeConsentAffirmationModalAndUpdateExtension` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `dateFilter` | |
| `defaultThemeAsset` | |
| `extensionCardClasses` | |
| `licensedExtension` | |
| `image` | |
| `isActive` | |
| `allowDisable` | |
| `isInstalled` | |
| `privacyPolicyLink` | |
| `permissions` | |
| `assetFilter` | |
| `isRemovable` | |
| `isUninstallable` | |
| `isUpdateable` | |
| `openLinkExists` | |
| `extensionMainModule` | |
| `link` | |
| `consentAffirmationModalActionLabel` | |
| `consentAffirmationModalCloseLabel` | |
| `consentAffirmationModalTitle` | |
| `consentAffirmationModalDescription` | |
| `extensionManagementDisabled` | |
| `showContextMenu` | |

### Examples

#### Basic Usage
```twig
<sw-extension-card-base
    extension="..."
>
    <!-- content -->
</sw-extension-card-base>
```

## sw-extension-card-bought

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `changeExtensionStatus` | |
| `activateExtension` | |
| `deactivateExtension` | |
| `closeDeactivationModal` | |
| `closeModalAndDeactivateExtension` | |
| `installExtension` | |
| `installAndActivateExtension` | |
| `cancelAndRemoveExtension` | |
| `openRatingModal` | |
| `closeRatingModal` | |
| `closeInstallationFailedNotification` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `extensionCardClasses` | |
| `priceInfo` | |
| `detailLink` | |
| `subscriptionExpiredText` | |
| `isExpiredRent` | |
| `isExpiredTestPhase` | |
| `subscriptionExpiredTextClasses` | |
| `showContextMenu` | |

### Examples

#### Basic Usage
```twig
<sw-extension-card-bought>
    <!-- content -->
</sw-extension-card-bought>
```

## sw-extension-component-section

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| positionIdentifier | `any` | — | yes |  |
| deprecated | `any` | `false` | no |  |
| deprecationMessage | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `setActiveTab` | |
| `getActiveTab` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `componentSections` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
<sw-extension-component-section
    v-if="isThemeRoute"
    position-identifier="sw-extension-my-extensions-listing__before-content"
/>

<sw-meteor-card
    v-if="!extensionListPaginated.length && filterByActiveState"
    class="sw-extension-my-extensions-listing__empty-state"
>
    <img
        :src="assetFilter('administration/administration/static/img/empty-states/extensions-empty-state.svg')"
        alt=""
    >

    <h3 v-if="isThemeRoute">
```

#### Example 2
Source: `sw-settings-tax/page/sw-settings-tax-provider-detail/sw-settings-tax-provider-detail.html.twig`
```twig
                <sw-extension-component-section
                    v-if="hasIdentifier"
                    :position-identifier="positionIdentifier"
                />
            </template>
        </sw-card-view>
    </template>
</sw-page>
{% endblock %}

```

#### Example 3
Source: `sw-settings/page/sw-settings-index/sw-settings-index.html.twig`
```twig
<sw-extension-component-section
    position-identifier="sw-settings-index"
/>

{% block sw_settings_content_card_view_header %}
<div class="sw-settings__content-header">
    <h1 class="sw-settings__content-header-title">
        {{ $tc('sw-settings.index.title') }}
    </h1>

    <mt-search
        v-model="searchQuery"
        class="sw-settings__content-header-search"
        :placeholder="$t('sw-settings.index.search.placeholder')"
        size="small"
```

#### Example 4
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
<sw-extension-component-section
    position-identifier="sw-product-detail__before-content"
/>

{% block sw_product_detail_content_view %}
<router-view
    v-slot="{ Component }"
>
    <component
        :is="Component"
        @cover-change="onCoverChange"
    />
</router-view>
{% endblock %}

```

#### Example 5
Source: `sw-customer/page/sw-customer-detail/sw-customer-detail.html.twig`
```twig
            <sw-extension-component-section
                position-identifier="sw-customer-detail__before-content"
            />

            {% block sw_customer_detail_content_view %}
            <template v-if="isLoading">
                <sw-skeleton variant="detail-bold" />
                <sw-skeleton />
            </template>

            <router-view
                v-if="customer"
                v-slot="{ Component }"
            >
                {# v-show is used here as underlying components influence the loading state and v-if would destroy this behaviour #}
```

## sw-extension-config

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| namespace | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `refreshExtension` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `domain` | |
| `myExtensions` | |
| `defaultThemeAsset` | |
| `image` | |
| `extensionLabel` | |

### Examples

#### Basic Usage
```twig
<sw-extension-config
    namespace="..."
>
    <!-- content -->
</sw-extension-config>
```

## sw-extension-deactivation-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| isLicensed | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| extension-deactivate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |
| `emitDeactivate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `removeHint` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-card-bought/sw-extension-card-bought.html.twig`
```twig
<sw-extension-deactivation-modal
    v-if="showDeactivationModal"
    :extension-name="label"
    :is-licensed="license !== null"
    :is-loading="isLoading"
    @modal-close="closeDeactivationModal"
    @extension-deactivate="closeModalAndDeactivateExtension"
/>
{% endblock %}

{% block sw_extension_card_base_info_content %}
    {% parent %}

<section v-if="priceInfo && extension.storeLicense.variant === 'rent'">
    <span class="sw-extension-card-bought__info-price">
```

## sw-extension-domains-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionLabel | `any` | — | yes |  |
| domains | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `close` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
    <sw-extension-domains-modal
        v-if="showDomainsModal"
        :extension-label="extensionLabel"
        :domains="domainsList"
        @modal-close="toggleDomainsModal(false)"
    />
    {% endblock %}
</sw-modal>
{% endblock %}

```

## sw-extension-file-upload

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onClickUpload` | |
| `onFileInputChange` | |
| `handleUpload` | |
| `showStoreError` | |
| `showConfirmModal` | |
| `closeConfirmModal` | |
| `getUserConfig` | |
| `saveConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `userConfigRepository` | |
| `currentUser` | |
| `userConfigCriteria` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-index/sw-extension-my-extensions-index.html.twig`
```twig
<sw-extension-file-upload v-if="acl.can('system.plugin_upload') || !extensionManagementDisabled" />
```

## sw-extension-icon

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| src | `any` | — | yes |  |
| alt | `any` | `''` | no |  |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```twig
    <sw-extension-icon
        class="sw-extension-config__extension-icon"
        :src="image"
        :alt="$tc('sw-extension-store.component.sw-extension-config.imageDescription', { extensionName: extensionLabel}, 0)"
    />
</template>

<template #smart-bar-header>
    {{ extensionLabel }}
</template>

<template
    v-if="extension"
    #smart-bar-header-meta
>
```

#### Example 2
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-icon :src="image" />
```

#### Example 3
Source: `sw-first-run-wizard/component/sw-plugin-card/sw-plugin-card.html.twig`
```twig
<sw-extension-icon
    :src="plugin.iconPath"
/>

<div class="sw-plugin-card__info">
    <div class="sw-plugin-card__label">
        {{ plugin.label }}
    </div>

    <div class="sw-plugin-card__manufacturer">
        {{ plugin.manufacturer }}
    </div>

    <div
        v-if="showDescription"
```

#### Example 4
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<sw-extension-icon
    class="sw-settings-services-service-card__icon"
    :src="icon"
    :alt="`Icon for ${service.name}`"
/>

<div>
    <h4>{{ service.label }}</h4>
    <sw-status
        :color="serviceStatus"
    >
        {{ $t(statusText) }}
    </sw-status>
</div>

```

## sw-extension-my-extensions-account

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `logout` | |
| `login` | |
| `showErrorNotification` | |
| `showApiNotification` | |
| `commitErrors` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `userInfo` | |
| `isLoggedIn` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-extension-my-extensions-account>
    <!-- content -->
</sw-extension-my-extensions-account>
```

## sw-extension-my-extensions-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onSearch` | |
| `updateRouteQueryTerm` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `searchValue` | |
| `queryParams` | |
| `extensionManagementDisabled` | |

### Examples

#### Basic Usage
```twig
<sw-extension-my-extensions-index>
    <!-- content -->
</sw-extension-my-extensions-index>
```

## sw-extension-my-extensions-listing-controls

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:active-state | — | |
| update:sorting-option | — | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
<sw-extension-my-extensions-listing-controls
    @update:active-state="changeActiveState"
    @update:sorting-option="changeSortingOption"
/>

<sw-extension-component-section
    v-if="isThemeRoute"
    position-identifier="sw-extension-my-extensions-listing__before-content"
/>

<sw-meteor-card
    v-if="!extensionListPaginated.length && filterByActiveState"
    class="sw-extension-my-extensions-listing__empty-state"
>
    <img
```

## sw-extension-my-extensions-listing

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `updateList` | |
| `openStore` | |
| `openThemesStore` | |
| `updateRouteQuery` | |
| `changePage` | |
| `filterExtensionsByType` | |
| `sortExtensions` | |
| `changeSortingOption` | |
| `changeActiveState` | |
| `filterExtensionsByActiveState` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isAppUrlReachable` | |
| `isLoading` | |
| `myExtensions` | |
| `extensionList` | |
| `extensionListPaginated` | |
| `extensionListSearched` | |
| `isAppRoute` | |
| `isThemeRoute` | |
| `total` | |
| `limit` | |
| `page` | |
| `term` | |
| `skeletonVariant` | |
| `assetFilter` | |
| `extensionManagementDisabled` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
<sw-extension-my-extensions-listing-controls
    @update:active-state="changeActiveState"
    @update:sorting-option="changeSortingOption"
/>

<sw-extension-component-section
    v-if="isThemeRoute"
    position-identifier="sw-extension-my-extensions-listing__before-content"
/>

<sw-meteor-card
    v-if="!extensionListPaginated.length && filterByActiveState"
    class="sw-extension-my-extensions-listing__empty-state"
>
    <img
```

## sw-extension-my-extensions-recommendation

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `finishLoading` | |

### Examples

#### Basic Usage
```twig
<sw-extension-my-extensions-recommendation>
    <!-- content -->
</sw-extension-my-extensions-recommendation>
```

## sw-extension-permissions-details-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| permissions | `any` | — | yes |  |
| modalTitle | `any` | — | yes |  |
| selectedEntity | `any` | `''` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `scrollSelectedEntityIntoView` | |
| `close` | |
| `categoryLabel` | |
| `entityLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `operations` | |
| `ankerId` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-permissions-modal/sw-extension-permissions-modal.html.twig`
```twig
    <sw-extension-permissions-details-modal
        v-if="showDetailsModal"
        :modal-title="modalTitle"
        :permissions="permissionsWithGroupedOperations"
        :selected-entity="selectedEntity"
        @modal-close="closeDetailsModal"
    />
    {% endblock %}

    {% block sw_extension_permissions_modal_domains %}
    <sw-extension-domains-modal
        v-if="showDomainsModal"
        :extension-label="extensionLabel"
        :domains="domainsList"
        @modal-close="toggleDomainsModal(false)"
```

## sw-extension-permissions-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| permissions | `any` | — | yes |  |
| domains | `any` | — | no |  |
| extensionLabel | `any` | — | yes |  |
| actionLabel | `any` | `null` | no |  |
| closeLabel | `any` | `null` | no |  |
| title | `any` | `null` | no |  |
| description | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| close-with-action | — | |

### Methods

| Method | Description |
|--------|-------------|
| `close` | |
| `closeWithAction` | |
| `categoryLabel` | |
| `openDetailsModal` | |
| `closeDetailsModal` | |
| `toggleDomainsModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `permissionsWithGroupedOperations` | |
| `domainsList` | |
| `closeBtnLabel` | |
| `descriptionText` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-permissions-modal
    v-if="showPermissionsModal"
    :extension-label="extension.label"
    :permissions="permissions"
    :domains="extension.domains"
    :action-label="permissionModalActionLabel"
    @modal-close="closePermissionsModal"
    @close-with-action="closePermissionsModalAndInstallExtension"
/>

<sw-extension-privacy-policy-extensions-modal
    v-if="showPrivacyModal"
    :extension-name="extension.label"
    :privacy-policy-extension="extension.privacyPolicyExtension"
    @modal-close="closePrivacyModal"
```

#### Example 2
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
    <sw-extension-permissions-modal
        v-if="showPermissionsModal"
        :extension-label="service.label"
        :permissions="categorizedPermissions"
        :domains="service.domains"
        @modal-close="showPermissionsModal = false"
    />
</li>

```

## sw-extension-privacy-policy-extensions-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| privacyPolicyExtension | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `close` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `title` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
    <sw-extension-privacy-policy-extensions-modal
        v-if="showPrivacyModal"
        :extension-name="extension.label"
        :privacy-policy-extension="extension.privacyPolicyExtension"
        @modal-close="closePrivacyModal"
    />

    <sw-extension-permissions-modal
        v-if="showConsentAffirmationModal"
        :title="consentAffirmationModalTitle"
        :extension-label="extension.label"
        :permissions="consentAffirmationDeltas.permissions"
        :domains="consentAffirmationDeltas.domains"
        :action-label="consentAffirmationModalActionLabel"
        :close-label="consentAffirmationModalCloseLabel"
```

## sw-extension-rating-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-card-bought/sw-extension-card-bought.html.twig`
```twig
<sw-extension-rating-modal
    v-if="showRatingModal"
    :extension="extension"
    @modal-close="closeRatingModal"
/>

<sw-modal
    v-if="showExtensionInstallationFailedModal"
    :title="extension.label"
    variant="small"
    class="sw-extension-card-bought__installation-failed-modal"
    @modal-close="closeInstallationFailedNotification"
>
    <sw-extension-adding-failed
        :extension-name="extension.name"
```

## sw-extension-rating-stars

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| editable | `any` | `false` | no |  |
| size | `any` | `8` | no |  |
| rating | `any` | `0` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:rating | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `colorClass` | |
| `addRating` | |
| `showPartialStar` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `editableClass` | |
| `sizeValue` | |
| `starSize` | |
| `partialStarSize` | |
| `partialStarWidth` | |
| `defaultSizeForEditable` | |
| `scaleFactor` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review/sw-extension-review.html.twig`
```twig
<sw-extension-rating-stars
    :rating="review.rating"
    :size="12"
/>
{% endblock %}

{% block sw_extension_review_text %}
<p
    v-if="review.text"
    class="sw-extension-review__text"
>
    {{ review.text }}
</p>
{% endblock %}

```

#### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-select-rating/sw-extension-select-rating.html.twig`
```twig
        <sw-extension-rating-stars
            v-model:rating="currentValue"
            editable
            @update:rating="onChange"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-base-field>
    {% endblock %}
{% endblock %}

```

#### Example 3
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-summary/sw-extension-ratings-summary.html.twig`
```twig
        <sw-extension-rating-stars
            :rating="Number(ratingGroup.rating)"
            :size="12"
        />
        {% endblock %}
    </template>
</div>
{% endblock %}

{% block sw_extension_ratings_summary_grid_rating_progress_bars %}
<div class="sw-extension-ratings-summary__progress-bars">
    {% block sw_extension_ratings_summary_grid_rating_progress_bars_count_rows %}
    <div class="sw-extension-ratings-summary__rows">
        <template
            v-for="ratingGroup in summary.ratingAssignment"
```

## sw-extension-ratings-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |
| producerName | `any` | — | yes |  |
| isInstalledAndLicensed | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-extension | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchReviews` | |
| `loadMoreReviews` | |
| `getReviews` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `canShowMore` | |
| `numberOfRatingsHasChanged` | |
| `extensionStoreDataService` | |
| `hasReviews` | |

### Examples

#### Basic Usage
```twig
<sw-extension-ratings-card
    extension="..."
    producerName="..."
>
    <!-- content -->
</sw-extension-ratings-card>
```

## sw-extension-ratings-summary

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| summary | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `maxProgressValue` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-card/sw-extension-ratings-card.html.twig`
```twig
<sw-extension-ratings-summary :summary="summary" />
```

## sw-extension-removal-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| isLicensed | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| remove-extension | — | |

### Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |
| `emitRemoval` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `title` | |
| `alert` | |
| `btnLabel` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-removal-modal
    v-if="showRemovalModal"
    :extension-name="extension.label"
    :is-licensed="extension.storeLicense !== null && extension.storeLicense.variant === 'rent'"
    :is-loading="isLoading"
    @modal-close="closeRemovalModal"
    @remove-extension="closeModalAndRemoveExtension"
/>

<sw-extension-permissions-modal
    v-if="showPermissionsModal"
    :extension-label="extension.label"
    :permissions="permissions"
    :domains="extension.domains"
    :action-label="permissionModalActionLabel"
```

## sw-extension-review-creation-inputs

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| errors | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| changed | — | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation/sw-extension-review-creation.html.twig`
```twig
<sw-extension-review-creation-inputs
    :errors="errors"
    @changed="onChange"
/>
{% endblock %}

{% block sw_extension_review_creation_gtc_checkbox %}
<sw-gtc-checkbox
    v-model:value="tocAccepted"
/>
{% endblock %}

{% block sw_extension_review_creation_buttons %}
<div class="sw-extension-review-creation__buttons">
    {% block sw_extension_review_creation_buttons_submit_button %}
```

#### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-rating-modal/sw-extension-rating-modal.html.twig`
```twig
    <sw-extension-review-creation-inputs
        :errors="errors"
        @changed="onChange"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_extension_rating_modal_slot_footer %}
<template #modal-footer>
    {% block sw_extension_rating_modal_slot_footer_gtc_checkbox %}
    <sw-gtc-checkbox
        v-model:value="tocAccepted"
    />
    {% endblock %}
```

## sw-extension-review-creation

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| created | — | |

### Methods

| Method | Description |
|--------|-------------|
| `handleCreateReview` | |
| `createReview` | |
| `validateInputs` | |
| `validateHeadline` | |
| `validateRating` | |
| `onChange` | |
| `emitCreated` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentUser` | |
| `userName` | |
| `installedVersion` | |
| `hasError` | |
| `disabled` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation/sw-extension-review-creation.html.twig`
```twig
<sw-extension-review-creation-inputs
    :errors="errors"
    @changed="onChange"
/>
{% endblock %}

{% block sw_extension_review_creation_gtc_checkbox %}
<sw-gtc-checkbox
    v-model:value="tocAccepted"
/>
{% endblock %}

{% block sw_extension_review_creation_buttons %}
<div class="sw-extension-review-creation__buttons">
    {% block sw_extension_review_creation_buttons_submit_button %}
```

#### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-rating-modal/sw-extension-rating-modal.html.twig`
```twig
    <sw-extension-review-creation-inputs
        :errors="errors"
        @changed="onChange"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_extension_rating_modal_slot_footer %}
<template #modal-footer>
    {% block sw_extension_rating_modal_slot_footer_gtc_checkbox %}
    <sw-gtc-checkbox
        v-model:value="tocAccepted"
    />
    {% endblock %}
```

#### Example 3
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-card/sw-extension-ratings-card.html.twig`
```twig
        <sw-extension-review-creation
            :extension="extension"
            @created="$emit('update-extension')"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-meteor-card>
{% endblock %}

```

## sw-extension-review-reply

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| reply | `any` | — | yes |  |
| producerName | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `creationDate` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review/sw-extension-review.html.twig`
```twig
        <sw-extension-review-reply
            v-for="(reply, index) in review.replies"
            :key="`sw-extension-review__reply-${index}`"
            :producer-name="producerName"
            :reply="reply"
        />
        {% endblock %}
    </template>
    {% endblock %}
</div>
{% endblock %}

```

## sw-extension-review

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| review | `any` | — | yes |  |
| producerName | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `lastChangeDate` | |
| `reviewHasReplies` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation/sw-extension-review-creation.html.twig`
```twig
<sw-extension-review-creation-inputs
    :errors="errors"
    @changed="onChange"
/>
{% endblock %}

{% block sw_extension_review_creation_gtc_checkbox %}
<sw-gtc-checkbox
    v-model:value="tocAccepted"
/>
{% endblock %}

{% block sw_extension_review_creation_buttons %}
<div class="sw-extension-review-creation__buttons">
    {% block sw_extension_review_creation_buttons_submit_button %}
```

#### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-review/sw-extension-review.html.twig`
```twig
        <sw-extension-review-reply
            v-for="(reply, index) in review.replies"
            :key="`sw-extension-review__reply-${index}`"
            :producer-name="producerName"
            :reply="reply"
        />
        {% endblock %}
    </template>
    {% endblock %}
</div>
{% endblock %}

```

#### Example 3
Source: `sw-extension/component/sw-ratings/sw-extension-rating-modal/sw-extension-rating-modal.html.twig`
```twig
    <sw-extension-review-creation-inputs
        :errors="errors"
        @changed="onChange"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_extension_rating_modal_slot_footer %}
<template #modal-footer>
    {% block sw_extension_rating_modal_slot_footer_gtc_checkbox %}
    <sw-gtc-checkbox
        v-model:value="tocAccepted"
    />
    {% endblock %}
```

#### Example 4
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-card/sw-extension-ratings-card.html.twig`
```twig
        <sw-extension-review
            v-for="(review, index) in reviews"
            :key="`sw-extension-ratings-card__reviews-review-${index}`"
            :producer-name="producerName"
            :review="review"
        />
        {% endblock %}

        {% block sw_extension_ratings_card_has_reviews_wrapper_more_button %}
        <mt-button
            v-if="canShowMore"
            size="small"
            variant="secondary"
            @click="loadMoreReviews"
        >
```

#### Example 5
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-card/sw-extension-ratings-card.html.twig`
```twig
        <sw-extension-review-creation
            :extension="extension"
            @created="$emit('update-extension')"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-meteor-card>
{% endblock %}

```

## sw-extension-sdk-module

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| id | `any` | — | yes |  |
| back | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `module` | |
| `isLoading` | |
| `showSearchBar` | |
| `showSmartBar` | |
| `showLanguageSwitch` | |
| `smartBarButtons` | |

### Examples

#### Basic Usage
```twig
<sw-extension-sdk-module
    id="..."
>
    <!-- content -->
</sw-extension-sdk-module>
```

## sw-extension-select-rating

> Shopware Administration component.

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
Source: `sw-extension/component/sw-ratings/sw-extension-review-creation-inputs/sw-extension-review-creation-inputs.html.twig`
```twig
            <sw-extension-select-rating
                v-model:value="rating"
                :error="errors.ratingError"
                required
                :label="$tc('sw-extension-store.component.sw-extension-ratings.sw-extension-review-creation-inputs.labelRating')"
            />
            {% endblock %}
        </div>
        {% endblock %}
    </div>
    {% endblock %}

    {% block sw_extension_review_creation_inputs_description_input %}
    <mt-textarea
        v-model="text"
```

## sw-extension-store-landing-page

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| insideModal | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `activateStore` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `extensionName` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-extension-store-landing-page>
    <!-- content -->
</sw-extension-store-landing-page>
```

## sw-extension-teaser-popover

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| positionIdentifier | `any` | — | yes |  |
| component | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onMouseEnterTrigger` | |
| `onMouseEnterContent` | |
| `onMouseLeaveContent` | |
| `onMouseLeaveTrigger` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `popoverComponent` | |
| `isInsideComponent` | |

### Examples

#### Example 1
Source: `sw-cms/blocks/app/app-renderer/preview/sw-cms-block-app-preview-renderer.html.twig`
```twig
    <sw-extension-teaser-popover
        v-else-if="appName === 'SwagRecommendations'"
        position-identifier="sw-cms-block-3d-object"
    />

    <section
        v-else
        class="sw-cms-block-app-preview-renderer__fallback-preview"
    >
        <h2>
            {{ $tc(appName) }}
        </h2>
    </section>
</div>
{% endblock %}
```

#### Example 2
Source: `sw-media/component/sw-media-library/sw-media-library.html.twig`
```twig
    <sw-extension-teaser-popover
        position-identifier="sw-media-generate-image-button"
    />

    {% block sw_media_index_create_folder %}
    <mt-button
        v-if="editable || allowCreateFolder"
        v-tooltip="{
            message: $tc('sw-privileges.tooltip.warning'),
            disabled: acl.can('media.creator'),
            showOnDisabledElements: true
        }"
        :disabled="!acl.can('media.creator') || disabled"
        class="sw-media-index__create-folder-action"
        ghost
```

#### Example 3
Source: `sw-settings-rule/view/sw-settings-rule-detail-base/sw-settings-rule-detail-base.html.twig`
```twig
    <sw-extension-teaser-popover
        position-identifier="sw-settings-rule-preview-mode-switch"
    />
</template>

<div
    v-if="showProductStreamIndexingWarning"
    class="sw-settings-rule-detail-base__product-stream-warning"
>
    <mt-banner
        variant="attention"
        :title="$tc('sw-settings-rule.detail.productStreamIndexingWarning.title')"
    >
        <p>
            {{ $tc('sw-settings-rule.detail.productStreamIndexingWarning.message') }}
```

#### Example 4
Source: `sw-product/component/sw-product-add-properties-modal/sw-product-add-properties-modal.html.twig`
```twig
                <sw-extension-teaser-popover
                    position-identifier="sw-product-add-properties-assistant-button"
                />
            </div>
            {% endblock %}
        </template>
    </sw-property-search>
    {% endblock %}
    {% endblock %}
</div>
{% endblock %}

<template #modal-footer>
    {% block sw_product_add_properties_modal_button_cancel %}
    <mt-button
```

#### Example 5
Source: `sw-product/component/sw-product-basic-form/sw-product-basic-form.html.twig`
```twig
        <sw-extension-teaser-popover
            position-identifier="sw-product-generated-description-button"
        />
    </div>
</div>
{% endblock %}

```

## sw-extension-teaser-sales-channel

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `teaserSalesChannels` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal-grid/sw-sales-channel-modal-grid.html.twig`
```twig
<sw-extension-teaser-sales-channel
    v-if="!isLoading"
/>

{% endblock %}

```

## sw-extension-uninstall-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extensionName | `any` | — | yes |  |
| isLicensed | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| uninstall-extension | — | |

### Methods

| Method | Description |
|--------|-------------|
| `emitClose` | |
| `emitUninstall` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `title` | |

### Examples

#### Example 1
Source: `sw-extension/component/sw-extension-card-base/sw-extension-card-base.html.twig`
```twig
<sw-extension-uninstall-modal
    v-if="showUninstallModal"
    :extension-name="extension.label"
    :is-licensed="extension.storeLicense !== null"
    :is-loading="isLoading"
    @modal-close="closeUninstallModal"
    @uninstall-extension="closeModalAndUninstallExtension"
/>

<sw-extension-removal-modal
    v-if="showRemovalModal"
    :extension-name="extension.label"
    :is-licensed="extension.storeLicense !== null && extension.storeLicense.variant === 'rent'"
    :is-loading="isLoading"
    @modal-close="closeRemovalModal"
```

## sw-external-link

> **Migration wrapper** — Delegates to `mt-link` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-link for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| small | `any` | `false` | no |  |
| icon | `any` | `'regular-external-link-s'` | no |  |
| rel | `any` | `'noopener'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClick` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `iconSize` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```twig
<sw-external-link
    small
    :href="extension.producerWebsite"
    class="sw-extension-config__producer-link"
>
    {{ extension.producerName }}
</sw-external-link>
```

#### Example 2
Source: `sw-media/component/sidebar/sw-media-quickinfo/sw-media-quickinfo.html.twig`
```twig
<sw-external-link
    :href="item.url"
    download
>

    <mt-icon
        size="16px"
        name="regular-cloud-download"
        class="sw-media-sidebar__quickactions-icon"
    />
    {{ $t('sw-media.sidebar.actions.download') }}
</sw-external-link>
```

#### Example 3
Source: `sw-settings-usage-data/component/sw-usage-data-consent-banner/sw-usage-data-consent-banner.html.twig`
```twig
<sw-external-link :href="$tc('sw-usage-data-consent-banner.privacyPolicyLink')">
    {{ $tc('sw-usage-data-consent-banner.privacyPolicy') }}
</sw-external-link>
```

#### Example 4
Source: `sw-order/component/sw-order-details-state-card/sw-order-details-state-card.html.twig`
```twig
<sw-external-link
    class="sw-order-detail-state-card__state-history-button"
    icon="regular-long-arrow-right"
    @click="onShowStatusHistory"
>
    {{ $tc('sw-order.stateCard.labelShowHistoryModal') }}
</sw-external-link>
```

#### Example 5
Source: `sw-dashboard/page/sw-dashboard-index/sw-dashboard-index.html.twig`
```twig
<sw-external-link :href="$tc(`sw-dashboard.helpcard.${key}Link`)">
    {{ $tc(`sw-dashboard.helpcard.${key}`) }}
</sw-external-link>
```
