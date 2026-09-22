# Administration (sw-*) components

> **`size="default"` on every `mt-button` you write.** The component defaults to
> `size="small"` — 32 pixels against the 40 of every core control beside it. Examples below
> that are quoted from Shopware's own source keep the core's spelling; **a plugin's own
> template sets the size explicitly.**
> → `shopware-admin` → `sw-meteor` → `COMPONENTS.md`

370 components, each with its props, slots, events and examples exactly as the generator extracted them. One file per component cost 1044 unreachable references; grouped, every component stays one direct link from SKILL.md.

## Contents

- [`sw-newsletter-recipient-detail`](#sw-newsletter-recipient-detail)
- [`sw-newsletter-recipient-filter-switch`](#sw-newsletter-recipient-filter-switch)
- [`sw-newsletter-recipient-list`](#sw-newsletter-recipient-list)
- [`sw-notification-center-item`](#sw-notification-center-item)
- [`sw-notification-center`](#sw-notification-center)
- [`sw-notifications`](#sw-notifications)
- [`sw-number-field-deprecated`](#sw-number-field-deprecated)
- [`sw-number-field`](#sw-number-field)
- [`sw-number-filter`](#sw-number-filter)
- [`sw-one-to-many-grid`](#sw-one-to-many-grid)
- [`sw-order-address-modal`](#sw-order-address-modal)
- [`sw-order-address-selection`](#sw-order-address-selection)
- [`sw-order-create-address-modal`](#sw-order-create-address-modal)
- [`sw-order-create-base`](#sw-order-create-base)
- [`sw-order-create-details-body`](#sw-order-create-details-body)
- [`sw-order-create-details-footer`](#sw-order-create-details-footer)
- [`sw-order-create-details-header`](#sw-order-create-details-header)
- [`sw-order-create-details`](#sw-order-create-details)
- [`sw-order-create-general-info`](#sw-order-create-general-info)
- [`sw-order-create-general`](#sw-order-create-general)
- [`sw-order-create-initial-modal`](#sw-order-create-initial-modal)
- [`sw-order-create-initial`](#sw-order-create-initial)
- [`sw-order-create-invalid-promotion-modal`](#sw-order-create-invalid-promotion-modal)
- [`sw-order-create-options`](#sw-order-create-options)
- [`sw-order-create-promotion-modal`](#sw-order-create-promotion-modal)
- [`sw-order-create`](#sw-order-create)
- [`sw-order-customer-address-select`](#sw-order-customer-address-select)
- [`sw-order-customer-comment`](#sw-order-customer-comment)
- [`sw-order-customer-grid`](#sw-order-customer-grid)
- [`sw-order-delivery-metadata`](#sw-order-delivery-metadata)
- [`sw-order-detail-details`](#sw-order-detail-details)
- [`sw-order-detail-documents`](#sw-order-detail-documents)
- [`sw-order-detail-general`](#sw-order-detail-general)
- [`sw-order-detail`](#sw-order-detail)
- [`sw-order-details-state-card`](#sw-order-details-state-card)
- [`sw-order-document-card`](#sw-order-document-card)
- [`sw-order-document-settings-credit-note-modal`](#sw-order-document-settings-credit-note-modal)
- [`sw-order-document-settings-delivery-note-modal`](#sw-order-document-settings-delivery-note-modal)
- [`sw-order-document-settings-invoice-modal`](#sw-order-document-settings-invoice-modal)
- [`sw-order-document-settings-modal`](#sw-order-document-settings-modal)
- [`sw-order-document-settings-storno-modal`](#sw-order-document-settings-storno-modal)
- [`sw-order-general-info`](#sw-order-general-info)
- [`sw-order-inline-field`](#sw-order-inline-field)
- [`sw-order-leave-page-modal`](#sw-order-leave-page-modal)
- [`sw-order-line-items-grid-sales-channel`](#sw-order-line-items-grid-sales-channel)
- [`sw-order-line-items-grid`](#sw-order-line-items-grid)
- [`sw-order-list`](#sw-order-list)
- [`sw-order-nested-line-items-modal`](#sw-order-nested-line-items-modal)
- [`sw-order-nested-line-items-row`](#sw-order-nested-line-items-row)
- [`sw-order-new-customer-modal`](#sw-order-new-customer-modal)
- [`sw-order-product-select`](#sw-order-product-select)
- [`sw-order-promotion-field`](#sw-order-promotion-field)
- [`sw-order-promotion-tag-field`](#sw-order-promotion-tag-field)
- [`sw-order-save-changes-beforehand-modal`](#sw-order-save-changes-beforehand-modal)
- [`sw-order-saveable-field`](#sw-order-saveable-field)
- [`sw-order-select-document-type-modal`](#sw-order-select-document-type-modal)
- [`sw-order-send-document-modal`](#sw-order-send-document-modal)
- [`sw-order-state-change-modal-attach-documents`](#sw-order-state-change-modal-attach-documents)
- [`sw-order-state-change-modal`](#sw-order-state-change-modal)
- [`sw-order-state-history-card-entry`](#sw-order-state-history-card-entry)
- [`sw-order-state-history-card`](#sw-order-state-history-card)
- [`sw-order-state-history-modal`](#sw-order-state-history-modal)
- [`sw-order-state-select-v2`](#sw-order-state-select-v2)
- [`sw-order-user-card`](#sw-order-user-card)
- [`sw-overlay`](#sw-overlay)
- [`sw-page`](#sw-page)
- [`sw-pagination`](#sw-pagination)
- [`sw-password-field-deprecated`](#sw-password-field-deprecated)
- [`sw-password-field`](#sw-password-field)
- [`sw-payment-card`](#sw-payment-card)
- [`sw-plugin-box`](#sw-plugin-box)
- [`sw-plugin-card`](#sw-plugin-card)
- [`sw-popover-deprecated`](#sw-popover-deprecated)
- [`sw-popover`](#sw-popover)
- [`sw-price-field`](#sw-price-field)
- [`sw-price-preview`](#sw-price-preview)
- [`sw-price-rule-modal`](#sw-price-rule-modal)
- [`sw-privilege-error`](#sw-privilege-error)
- [`sw-product-add-properties-modal`](#sw-product-add-properties-modal)
- [`sw-product-basic-form`](#sw-product-basic-form)
- [`sw-product-category-form`](#sw-product-category-form)
- [`sw-product-clone-modal`](#sw-product-clone-modal)
- [`sw-product-cross-selling-assignment`](#sw-product-cross-selling-assignment)
- [`sw-product-cross-selling-form`](#sw-product-cross-selling-form)
- [`sw-product-deliverability-downloadable-form`](#sw-product-deliverability-downloadable-form)
- [`sw-product-deliverability-form`](#sw-product-deliverability-form)
- [`sw-product-detail-base`](#sw-product-detail-base)
- [`sw-product-detail-context-prices`](#sw-product-detail-context-prices)
- [`sw-product-detail-cross-selling`](#sw-product-detail-cross-selling)
- [`sw-product-detail-layout`](#sw-product-detail-layout)
- [`sw-product-detail-reviews`](#sw-product-detail-reviews)
- [`sw-product-detail-seo`](#sw-product-detail-seo)
- [`sw-product-detail-specifications`](#sw-product-detail-specifications)
- [`sw-product-detail-variants`](#sw-product-detail-variants)
- [`sw-product-detail`](#sw-product-detail)
- [`sw-product-download-form`](#sw-product-download-form)
- [`sw-product-feature-set-form`](#sw-product-feature-set-form)
- [`sw-product-image`](#sw-product-image)
- [`sw-product-layout-assignment`](#sw-product-layout-assignment)
- [`sw-product-list`](#sw-product-list)
- [`sw-product-measurement-form`](#sw-product-measurement-form)
- [`sw-product-media-form`](#sw-product-media-form)
- [`sw-product-modal-delivery`](#sw-product-modal-delivery)
- [`sw-product-modal-variant-generation`](#sw-product-modal-variant-generation)
- [`sw-product-packaging-form`](#sw-product-packaging-form)
- [`sw-product-price-form`](#sw-product-price-form)
- [`sw-product-properties`](#sw-product-properties)
- [`sw-product-restriction-selection`](#sw-product-restriction-selection)
- [`sw-product-seo-form`](#sw-product-seo-form)
- [`sw-product-settings-form`](#sw-product-settings-form)
- [`sw-product-settings-mode`](#sw-product-settings-mode)
- [`sw-product-stream-detail`](#sw-product-stream-detail)
- [`sw-product-stream-field-select`](#sw-product-stream-field-select)
- [`sw-product-stream-filter`](#sw-product-stream-filter)
- [`sw-product-stream-grid-preview`](#sw-product-stream-grid-preview)
- [`sw-product-stream-list`](#sw-product-stream-list)
- [`sw-product-stream-modal-preview`](#sw-product-stream-modal-preview)
- [`sw-product-stream-value`](#sw-product-stream-value)
- [`sw-product-variant-info`](#sw-product-variant-info)
- [`sw-product-variant-modal`](#sw-product-variant-modal)
- [`sw-product-variants-configurator-prices`](#sw-product-variants-configurator-prices)
- [`sw-product-variants-configurator-restrictions`](#sw-product-variants-configurator-restrictions)
- [`sw-product-variants-configurator-selection`](#sw-product-variants-configurator-selection)
- [`sw-product-variants-delivery-listing`](#sw-product-variants-delivery-listing)
- [`sw-product-variants-delivery-media`](#sw-product-variants-delivery-media)
- [`sw-product-variants-delivery-order`](#sw-product-variants-delivery-order)
- [`sw-product-variants-media-upload`](#sw-product-variants-media-upload)
- [`sw-product-variants-overview`](#sw-product-variants-overview)
- [`sw-product-variants-price-field`](#sw-product-variants-price-field)
- [`sw-product-visibility-detail`](#sw-product-visibility-detail)
- [`sw-product-visibility-select`](#sw-product-visibility-select)
- [`sw-profile-index-general`](#sw-profile-index-general)
- [`sw-profile-index-privacy-preferences`](#sw-profile-index-privacy-preferences)
- [`sw-profile-index-search-preferences`](#sw-profile-index-search-preferences)
- [`sw-profile-index`](#sw-profile-index)
- [`sw-progress-bar`](#sw-progress-bar)
- [`sw-promotion-detail-discounts`](#sw-promotion-detail-discounts)
- [`sw-promotion-discount-component`](#sw-promotion-discount-component)
- [`sw-promotion-v2-cart-condition-form`](#sw-promotion-v2-cart-condition-form)
- [`sw-promotion-v2-conditions`](#sw-promotion-v2-conditions)
- [`sw-promotion-v2-detail-base`](#sw-promotion-v2-detail-base)
- [`sw-promotion-v2-detail`](#sw-promotion-v2-detail)
- [`sw-promotion-v2-empty-state-hero`](#sw-promotion-v2-empty-state-hero)
- [`sw-promotion-v2-generate-codes-modal`](#sw-promotion-v2-generate-codes-modal)
- [`sw-promotion-v2-individual-codes-behavior`](#sw-promotion-v2-individual-codes-behavior)
- [`sw-promotion-v2-list`](#sw-promotion-v2-list)
- [`sw-promotion-v2-sales-channel-select`](#sw-promotion-v2-sales-channel-select)
- [`sw-promotion-v2-settings-discount-type`](#sw-promotion-v2-settings-discount-type)
- [`sw-promotion-v2-settings-rule-selection`](#sw-promotion-v2-settings-rule-selection)
- [`sw-promotion-v2-settings-trigger`](#sw-promotion-v2-settings-trigger)
- [`sw-promotion-v2-wizard-description`](#sw-promotion-v2-wizard-description)
- [`sw-promotion-v2-wizard-discount-selection`](#sw-promotion-v2-wizard-discount-selection)
- [`sw-property-create`](#sw-property-create)
- [`sw-property-detail-base`](#sw-property-detail-base)
- [`sw-property-detail`](#sw-property-detail)
- [`sw-property-list`](#sw-property-list)
- [`sw-property-option-detail`](#sw-property-option-detail)
- [`sw-property-option-list`](#sw-property-option-list)
- [`sw-property-search`](#sw-property-search)
- [`sw-provide`](#sw-provide)
- [`sw-purchase-price-field`](#sw-purchase-price-field)
- [`sw-radio-field`](#sw-radio-field)
- [`sw-radio-panel`](#sw-radio-panel)
- [`sw-range-filter`](#sw-range-filter)
- [`sw-rating-stars`](#sw-rating-stars)
- [`sw-review-detail`](#sw-review-detail)
- [`sw-review-list`](#sw-review-list)
- [`sw-rule-modal`](#sw-rule-modal)
- [`sw-sales-channel-config`](#sw-sales-channel-config)
- [`sw-sales-channel-create-base`](#sw-sales-channel-create-base)
- [`sw-sales-channel-create`](#sw-sales-channel-create)
- [`sw-sales-channel-defaults-select`](#sw-sales-channel-defaults-select)
- [`sw-sales-channel-detail-analytics`](#sw-sales-channel-detail-analytics)
- [`sw-sales-channel-detail-base`](#sw-sales-channel-detail-base)
- [`sw-sales-channel-detail-domains`](#sw-sales-channel-detail-domains)
- [`sw-sales-channel-detail-hreflang`](#sw-sales-channel-detail-hreflang)
- [`sw-sales-channel-detail-product-comparison-preview`](#sw-sales-channel-detail-product-comparison-preview)
- [`sw-sales-channel-detail-product-comparison`](#sw-sales-channel-detail-product-comparison)
- [`sw-sales-channel-detail-products`](#sw-sales-channel-detail-products)
- [`sw-sales-channel-detail`](#sw-sales-channel-detail)
- [`sw-sales-channel-list`](#sw-sales-channel-list)
- [`sw-sales-channel-measurement`](#sw-sales-channel-measurement)
- [`sw-sales-channel-menu`](#sw-sales-channel-menu)
- [`sw-sales-channel-modal-detail`](#sw-sales-channel-modal-detail)
- [`sw-sales-channel-modal-grid`](#sw-sales-channel-modal-grid)
- [`sw-sales-channel-modal`](#sw-sales-channel-modal)
- [`sw-sales-channel-product-assignment-categories`](#sw-sales-channel-product-assignment-categories)
- [`sw-sales-channel-products-assignment-dynamic-product-groups`](#sw-sales-channel-products-assignment-dynamic-product-groups)
- [`sw-sales-channel-products-assignment-modal`](#sw-sales-channel-products-assignment-modal)
- [`sw-sales-channel-products-assignment-single-products`](#sw-sales-channel-products-assignment-single-products)
- [`sw-sales-channel-switch`](#sw-sales-channel-switch)
- [`sw-search-bar-item`](#sw-search-bar-item)
- [`sw-search-bar`](#sw-search-bar)
- [`sw-search-more-results`](#sw-search-more-results)
- [`sw-search-preferences-modal`](#sw-search-preferences-modal)
- [`sw-select-base`](#sw-select-base)
- [`sw-select-field-deprecated`](#sw-select-field-deprecated)
- [`sw-select-field`](#sw-select-field)
- [`sw-select-number-field`](#sw-select-number-field)
- [`sw-select-option`](#sw-select-option)
- [`sw-select-result-list`](#sw-select-result-list)
- [`sw-select-result`](#sw-select-result)
- [`sw-select-rule-create`](#sw-select-rule-create)
- [`sw-select-selection-list`](#sw-select-selection-list)
- [`sw-self-maintained-extension-card`](#sw-self-maintained-extension-card)
- [`sw-seo-main-category`](#sw-seo-main-category)
- [`sw-seo-url-template-card`](#sw-seo-url-template-card)
- [`sw-seo-url`](#sw-seo-url)
- [`sw-settings-basic-information`](#sw-settings-basic-information)
- [`sw-settings-cache-index`](#sw-settings-cache-index)
- [`sw-settings-cache-modal`](#sw-settings-cache-modal)
- [`sw-settings-captcha-select-v2`](#sw-settings-captcha-select-v2)
- [`sw-settings-cart`](#sw-settings-cart)
- [`sw-settings-country-address-handling`](#sw-settings-country-address-handling)
- [`sw-settings-country-create`](#sw-settings-country-create)
- [`sw-settings-country-currency-dependent-modal`](#sw-settings-country-currency-dependent-modal)
- [`sw-settings-country-currency-hamburger-menu`](#sw-settings-country-currency-hamburger-menu)
- [`sw-settings-country-detail`](#sw-settings-country-detail)
- [`sw-settings-country-general`](#sw-settings-country-general)
- [`sw-settings-country-list`](#sw-settings-country-list)
- [`sw-settings-country-new-snippet-modal`](#sw-settings-country-new-snippet-modal)
- [`sw-settings-country-preview-template`](#sw-settings-country-preview-template)
- [`sw-settings-country-state`](#sw-settings-country-state)
- [`sw-settings-currency-country-modal`](#sw-settings-currency-country-modal)
- [`sw-settings-currency-detail`](#sw-settings-currency-detail)
- [`sw-settings-currency-list`](#sw-settings-currency-list)
- [`sw-settings-custom-field-set-create`](#sw-settings-custom-field-set-create)
- [`sw-settings-custom-field-set-detail`](#sw-settings-custom-field-set-detail)
- [`sw-settings-custom-field-set-list`](#sw-settings-custom-field-set-list)
- [`sw-settings-customer-group-create`](#sw-settings-customer-group-create)
- [`sw-settings-customer-group-detail`](#sw-settings-customer-group-detail)
- [`sw-settings-customer-group-list`](#sw-settings-customer-group-list)
- [`sw-settings-delivery-time-create`](#sw-settings-delivery-time-create)
- [`sw-settings-delivery-time-detail`](#sw-settings-delivery-time-detail)
- [`sw-settings-delivery-time-list`](#sw-settings-delivery-time-list)
- [`sw-settings-document-detail`](#sw-settings-document-detail)
- [`sw-settings-document-list`](#sw-settings-document-list)
- [`sw-settings-index`](#sw-settings-index)
- [`sw-settings-item`](#sw-settings-item)
- [`sw-settings-language-detail`](#sw-settings-language-detail)
- [`sw-settings-language-list`](#sw-settings-language-list)
- [`sw-settings-listing-default-sales-channel`](#sw-settings-listing-default-sales-channel)
- [`sw-settings-listing-delete-modal`](#sw-settings-listing-delete-modal)
- [`sw-settings-listing-option-base`](#sw-settings-listing-option-base)
- [`sw-settings-listing-option-create`](#sw-settings-listing-option-create)
- [`sw-settings-listing-option-criteria-grid`](#sw-settings-listing-option-criteria-grid)
- [`sw-settings-listing-option-general-info`](#sw-settings-listing-option-general-info)
- [`sw-settings-listing-visibility-detail`](#sw-settings-listing-visibility-detail)
- [`sw-settings-listing`](#sw-settings-listing)
- [`sw-settings-logging-entry-info`](#sw-settings-logging-entry-info)
- [`sw-settings-logging-list`](#sw-settings-logging-list)
- [`sw-settings-logging-mail-sent-info`](#sw-settings-logging-mail-sent-info)
- [`sw-settings-login-registration`](#sw-settings-login-registration)
- [`sw-settings-mailer-smtp`](#sw-settings-mailer-smtp)
- [`sw-settings-mailer`](#sw-settings-mailer)
- [`sw-settings-measurement-default-units`](#sw-settings-measurement-default-units)
- [`sw-settings-measurement`](#sw-settings-measurement)
- [`sw-settings-media`](#sw-settings-media)
- [`sw-settings-message-stats`](#sw-settings-message-stats)
- [`sw-settings-newsletter`](#sw-settings-newsletter)
- [`sw-settings-number-range-create`](#sw-settings-number-range-create)
- [`sw-settings-number-range-detail`](#sw-settings-number-range-detail)
- [`sw-settings-number-range-list`](#sw-settings-number-range-list)
- [`sw-settings-payment-create`](#sw-settings-payment-create)
- [`sw-settings-payment-detail`](#sw-settings-payment-detail)
- [`sw-settings-payment-overview`](#sw-settings-payment-overview)
- [`sw-settings-payment-sorting-modal`](#sw-settings-payment-sorting-modal)
- [`sw-settings-price-rounding`](#sw-settings-price-rounding)
- [`sw-settings-product-feature-sets-detail`](#sw-settings-product-feature-sets-detail)
- [`sw-settings-product-feature-sets-list`](#sw-settings-product-feature-sets-list)
- [`sw-settings-product-feature-sets-modal`](#sw-settings-product-feature-sets-modal)
- [`sw-settings-product-feature-sets-values-card`](#sw-settings-product-feature-sets-values-card)
- [`sw-settings-rule-add-assignment-listing`](#sw-settings-rule-add-assignment-listing)
- [`sw-settings-rule-add-assignment-modal`](#sw-settings-rule-add-assignment-modal)
- [`sw-settings-rule-assignment-listing`](#sw-settings-rule-assignment-listing)
- [`sw-settings-rule-category-tree`](#sw-settings-rule-category-tree)
- [`sw-settings-rule-detail-assignments`](#sw-settings-rule-detail-assignments)
- [`sw-settings-rule-detail-base`](#sw-settings-rule-detail-base)
- [`sw-settings-rule-detail`](#sw-settings-rule-detail)
- [`sw-settings-rule-list`](#sw-settings-rule-list)
- [`sw-settings-rule-tree-item`](#sw-settings-rule-tree-item)
- [`sw-settings-rule-tree`](#sw-settings-rule-tree)
- [`sw-settings-salutation-detail`](#sw-settings-salutation-detail)
- [`sw-settings-salutation-list`](#sw-settings-salutation-list)
- [`sw-settings-search-example-modal`](#sw-settings-search-example-modal)
- [`sw-settings-search-excluded-search-terms`](#sw-settings-search-excluded-search-terms)
- [`sw-settings-search-live-search-keyword`](#sw-settings-search-live-search-keyword)
- [`sw-settings-search-live-search`](#sw-settings-search-live-search)
- [`sw-settings-search-search-behaviour`](#sw-settings-search-search-behaviour)
- [`sw-settings-search-search-index`](#sw-settings-search-search-index)
- [`sw-settings-search-searchable-content-customfields`](#sw-settings-search-searchable-content-customfields)
- [`sw-settings-search-searchable-content-general`](#sw-settings-search-searchable-content-general)
- [`sw-settings-search-searchable-content`](#sw-settings-search-searchable-content)
- [`sw-settings-search-view-general`](#sw-settings-search-view-general)
- [`sw-settings-search-view-live-search`](#sw-settings-search-view-live-search)
- [`sw-settings-search`](#sw-settings-search)
- [`sw-settings-seo`](#sw-settings-seo)
- [`sw-settings-services-dashboard-banner`](#sw-settings-services-dashboard-banner)
- [`sw-settings-services-grant-permissions-modal`](#sw-settings-services-grant-permissions-modal)
- [`sw-settings-services-index`](#sw-settings-services-index)
- [`sw-settings-shipping-detail`](#sw-settings-shipping-detail)
- [`sw-settings-shipping-list`](#sw-settings-shipping-list)
- [`sw-settings-shipping-price-matrices`](#sw-settings-shipping-price-matrices)
- [`sw-settings-shipping-price-matrix`](#sw-settings-shipping-price-matrix)
- [`sw-settings-shipping-tax-cost`](#sw-settings-shipping-tax-cost)
- [`sw-settings-shopware-updates-index`](#sw-settings-shopware-updates-index)
- [`sw-settings-shopware-updates-info`](#sw-settings-shopware-updates-info)
- [`sw-settings-shopware-updates-plugins`](#sw-settings-shopware-updates-plugins)
- [`sw-settings-shopware-updates-requirements`](#sw-settings-shopware-updates-requirements)
- [`sw-settings-shopware-updates-wizard`](#sw-settings-shopware-updates-wizard)
- [`sw-settings-sitemap`](#sw-settings-sitemap)
- [`sw-settings-snippet-create`](#sw-settings-snippet-create)
- [`sw-settings-snippet-detail`](#sw-settings-snippet-detail)
- [`sw-settings-snippet-filter-switch`](#sw-settings-snippet-filter-switch)
- [`sw-settings-snippet-list`](#sw-settings-snippet-list)
- [`sw-settings-snippet-set-list`](#sw-settings-snippet-set-list)
- [`sw-settings-snippet-sidebar`](#sw-settings-snippet-sidebar)
- [`sw-settings-state-machine-detail`](#sw-settings-state-machine-detail)
- [`sw-settings-state-machine-list`](#sw-settings-state-machine-list)
- [`sw-settings-state-machine-state-detail`](#sw-settings-state-machine-state-detail)
- [`sw-settings-state-machine-state-list`](#sw-settings-state-machine-state-list)
- [`sw-settings-store`](#sw-settings-store)
- [`sw-settings-tag-detail-assignments`](#sw-settings-tag-detail-assignments)
- [`sw-settings-tag-detail-modal`](#sw-settings-tag-detail-modal)
- [`sw-settings-tag-list`](#sw-settings-tag-list)
- [`sw-settings-tax-detail`](#sw-settings-tax-detail)
- [`sw-settings-tax-list`](#sw-settings-tax-list)
- [`sw-settings-tax-provider-detail`](#sw-settings-tax-provider-detail)
- [`sw-settings-tax-provider-sorting-modal`](#sw-settings-tax-provider-sorting-modal)
- [`sw-settings-tax-rule-modal`](#sw-settings-tax-rule-modal)
- [`sw-settings-tax-rule-type-individual-states-cell`](#sw-settings-tax-rule-type-individual-states-cell)
- [`sw-settings-tax-rule-type-individual-states`](#sw-settings-tax-rule-type-individual-states)
- [`sw-settings-tax-rule-type-zip-code-cell`](#sw-settings-tax-rule-type-zip-code-cell)
- [`sw-settings-tax-rule-type-zip-code-range-cell`](#sw-settings-tax-rule-type-zip-code-range-cell)
- [`sw-settings-tax-rule-type-zip-code-range`](#sw-settings-tax-rule-type-zip-code-range)
- [`sw-settings-tax-rule-type-zip-code`](#sw-settings-tax-rule-type-zip-code)
- [`sw-settings-units-detail`](#sw-settings-units-detail)
- [`sw-settings-units-list`](#sw-settings-units-list)
- [`sw-settings-usage-data-consent-modal`](#sw-settings-usage-data-consent-modal)
- [`sw-settings-usage-data-general`](#sw-settings-usage-data-general)
- [`sw-settings-usage-data-profile-consent`](#sw-settings-usage-data-profile-consent)
- [`sw-settings-usage-data`](#sw-settings-usage-data)
- [`sw-shortcut-overview-item`](#sw-shortcut-overview-item)
- [`sw-shortcut-overview`](#sw-shortcut-overview)
- [`sw-sidebar-collapse`](#sw-sidebar-collapse)
- [`sw-sidebar-filter-panel`](#sw-sidebar-filter-panel)
- [`sw-sidebar-item`](#sw-sidebar-item)
- [`sw-sidebar-media-item`](#sw-sidebar-media-item)
- [`sw-sidebar-navigation-item`](#sw-sidebar-navigation-item)
- [`sw-sidebar-renderer`](#sw-sidebar-renderer)
- [`sw-sidebar`](#sw-sidebar)
- [`sw-simple-search-field`](#sw-simple-search-field)
- [`sw-single-select`](#sw-single-select)
- [`sw-skeleton-bar-deprecated`](#sw-skeleton-bar-deprecated)
- [`sw-skeleton-bar`](#sw-skeleton-bar)
- [`sw-skeleton`](#sw-skeleton)
- [`sw-skip-link`](#sw-skip-link)
- [`sw-snippet-field-edit-modal`](#sw-snippet-field-edit-modal)
- [`sw-snippet-field`](#sw-snippet-field)
- [`sw-sortable-list`](#sw-sortable-list)
- [`sw-sorting-select`](#sw-sorting-select)
- [`sw-sso-error-index`](#sw-sso-error-index)
- [`sw-sso-users-permission-user-detail`](#sw-sso-users-permission-user-detail)
- [`sw-status`](#sw-status)
- [`sw-step-display`](#sw-step-display)
- [`sw-step-item`](#sw-step-item)
- [`sw-string-filter`](#sw-string-filter)
- [`sw-switch-field-deprecated`](#sw-switch-field-deprecated)
- [`sw-switch-field`](#sw-switch-field)
- [`sw-system-config`](#sw-system-config)

## sw-newsletter-recipient-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |
| `onSaveFinish` | |
| `onCancel` | |
| `loadCustomFieldSets` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `newsletterRecipientStore` | |

### Examples

#### Basic Usage
```twig
<sw-newsletter-recipient-detail>
    <!-- content -->
</sw-newsletter-recipient-detail>
```

## sw-newsletter-recipient-filter-switch

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| id | `any` | — | yes |  |
| label | `any` | `''` | no |  |
| group | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| field | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

### Examples

#### Basic Usage
```twig
<sw-newsletter-recipient-filter-switch
    id="..."
>
    <!-- content -->
</sw-newsletter-recipient-filter-switch>
```

## sw-newsletter-recipient-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `onStatusSelectionChanged` | |
| `onLanguageSelectionChanged` | |
| `onSalesChannelSelectionChanged` | |
| `onTagSelectionChanged` | |
| `closeContent` | |
| `getColumns` | |
| `handleTagFilter` | |
| `handleBooleanFilter` | |
| `onChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `columns` | |
| `salesChannelRepository` | |
| `newsletterRecipientRepository` | |
| `tagRepository` | |
| `dateFilter` | |
| `emailIdnFilter` | |
| `statusData` | |

### Examples

#### Basic Usage
```twig
<sw-newsletter-recipient-list>
    <!-- content -->
</sw-newsletter-recipient-list>
```

## sw-notification-center-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| notification | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| center-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `isNotificationFromSameDay` | |
| `onDelete` | |
| `handleAction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `itemHeaderClass` | |
| `notificationActions` | |

### Examples

#### Basic Usage
```twig
<sw-notification-center-item
    notification="..."
>
    <!-- content -->
</sw-notification-center-item>
```

## sw-notification-center

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onContextMenuOpen` | |
| `onContextMenuClose` | |
| `openDeleteModal` | |
| `onConfirmDelete` | |
| `onCloseDeleteModal` | |
| `changeVisibility` | |
| `createNotificationFromSystemError` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `notifications` | |
| `additionalContextButtonClass` | |

### Examples

#### Basic Usage
```twig
<sw-notification-center>
    <!-- content -->
</sw-notification-center>
```

## sw-notifications

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| position | `any` | `'topRight'` | no |  |
| notificationsGap | `any` | `'20px'` | no |  |
| notificationsTopGap | `any` | `'165px'` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `handleAction` | |
| `getNotificationVariant` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `notifications` | |
| `notificationsStyle` | |

### Examples

#### Basic Usage
```twig
<sw-notifications>
    <!-- content -->
</sw-notifications>
```

## sw-number-field-deprecated

> **Deprecated in 6.7** — Use `mt-number-field` instead. Will be removed in 6.8.
> See mt-number-field for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-number-field>` | `<mt-number-field>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| numberType | `any` | `'float'` | no | Valid: `float`, `int` |
| step | `any` | `null` | no |  |
| min | `any` | `null` | no |  |
| max | `any` | `null` | no |  |
| value | `any` | `null` | no |  |
| digits | `any` | `2` | no |  |
| fillDigits | `any` | `false` | no |  |
| allowEmpty | `any` | `false` | no |  |
| numberAlignEnd | `any` | `false` | no |  |
| ariaLabel | `any` | — | no |  |

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
| update:value | — | |
| input-change | — | |
| inheritance-restore | — | |
| inheritance-remove | — | |
| ends-with-decimal-separator | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `onInput` | |
| `increaseNumberByStep` | |
| `decreaseNumberByStep` | |
| `computeValue` | |
| `parseValue` | |
| `checkBoundaries` | |
| `getNumberFromString` | |
| `checkForInteger` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `realStep` | |
| `realMinimum` | |
| `realMaximum` | |
| `stringRepresentation` | |

### Examples

#### Basic Usage
```twig
<sw-number-field-deprecated>
    <!-- content -->
</sw-number-field-deprecated>
```

## sw-number-field

> **Migration wrapper** — Delegates to `mt-number-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-number-field for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
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
<sw-number-field>
    <!-- content -->
</sw-number-field>
```

## sw-number-filter

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
| `resetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-number-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-number-filter>
```

## sw-one-to-many-grid

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| collection | `any` | — | yes |  |
| localMode | `any` | `true` | no |  |
| dataSource | `null \| null` | — | no |  |
| allowDelete | `any` | `true` | no |  |
| tooltipDelete | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| more-actions | — | |
| delete-action | item: item | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| load-finish | — | |
| delete-item-failed | — | |
| items-delete-finish | — | |
| column-sort | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `applyResult` | |
| `save` | |
| `revert` | |
| `load` | |
| `deleteItem` | |
| `deleteItems` | |
| `deleteItemsFinish` | |
| `sort` | |
| `paginate` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
<sw-one-to-many-grid
    ref="countryStateGrid"
    class="sw-settings-country-state-list__content"
    :is-loading="countryStateLoading"
    :collection="country.states"
    :full-page="undefined"
    :local-mode="country.isNew()"
    :columns="stateColumns"
    :allow-delete="acl.can('country.editor')"
    :tooltip-delete="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('country.editor'),
        showOnDisabledElements: true
    }"
    @selection-change="countryStateSelectionChanged"
```

#### Example 2
Source: `sw-property/component/sw-property-option-list/sw-property-option-list.html.twig`
```twig
<sw-one-to-many-grid
    ref="grid"
    :is-loading="isLoading"
    :collection="propertyGroup.options"
    :columns="getGroupColumns()"
    :full-page="false"
    :local-mode="false"
    :allow-inline-edit="allowInlineEdit"
    :sort-by="sortBy"
    :sort-direction="sortDirection"
    @load-finish="checkEmptyState"
    @selection-change="onGridSelectionChanged"
>
    <template #column-name="{ item, isInlineEdit }">
        <template v-if="isInlineEdit">
```

#### Example 3
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-discount-type/sw-promotion-v2-settings-discount-type.html.twig`
```twig
<sw-one-to-many-grid
    :collection="discount.promotionDiscountPrices"
    :local-mode="true"
    :columns="currencyPriceColumns"
    :show-selection="false"
    :show-actions="!acl.can('promotion.editor')"
>

    {% block sw_promotion_v2_settings_discount_type_advanced_prices_modal_grid_column_name %}
    <template #column-currency.translated.name="{ item }">
        <p class="sw-promotion-v2-settings-discounts-type__advances-prices-column-name">
            {{ item.currency.translated.name }}
        </p>
    </template>
    {% endblock %}
```

#### Example 4
Source: `sw-promotion-v2/component/sw-promotion-discount-component/sw-promotion-discount-component.html.twig`
```twig
<sw-one-to-many-grid
    :collection="discount.promotionDiscountPrices"
    :local-mode="true"
    :columns="currencyPriceColumns"
    :show-selection="false"
    :is-loading="isLoading"
    :show-actions="!isEditingDisabled"
>

    <template #column-currency.translated.name="{ item }">
        <p>{{ item.currency.translated.name }}</p>
    </template>

    <template #column-price="{ item }">
        <mt-number-field
```

#### Example 5
Source: `sw-promotion-v2/component/promotion-codes/sw-promotion-v2-individual-codes-behavior/sw-promotion-v2-individual-codes-behavior.html.twig`
```twig
<sw-one-to-many-grid
    ref="individualCodesGrid"
    class="sw-promotion-v2-individual-codes-behavior__grid"
    :is-loading="isGridLoading"
    :collection="promotion.individualCodes"
    :columns="codeColumns"
    :local-mode="false"
    sort-by="code"
    sort-direction="ASC"
    @selection-change="onSelectionChange"
    @items-delete-finish="$emit('delete-finish')"
>

    {% block sw_promotion_v2_individual_codes_behavior_grid_redeemed %}
    <template #column-payload="{ item }">
```

## sw-order-address-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| address | `any` | — | yes |  |
| countries | `any` | — | yes |  |
| order | `any` | — | yes |  |
| versionContext | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| reset | — | |
| address-select | — | |
| save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getCustomerInfo` | |
| `onNewActiveItem` | |
| `addressButtonClasses` | |
| `onExistingAddressSelected` | |
| `onClose` | |
| `onSave` | |
| `getCustomFieldSetData` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerCriteria` | |
| `customFieldSetCriteria` | |
| `customerRepository` | |
| `orderRepository` | |
| `orderCustomer` | |
| `customFieldSetRepository` | |
| `salutationFilter` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
<sw-order-address-modal
    v-if="addressBeingEdited"
    :countries="countries"
    :address="addressBeingEdited"
    :order="currentOrder"
    :version-context="versionContext"
    @address-select="onAddressModalAddressSelected"
    @reset="onResetOrder"
    @save="onAddressModalSave"
    @error="$emit('error')"
/>
{% endblock %}

<template #grid>
    <sw-container rows="auto auto">
```

## sw-order-address-selection

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| address | `any` | — | no |  |
| label | `any` | `''` | no |  |
| addressId | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| type | `any` | `''` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-address | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onEditAddress` | |
| `onCreateNewAddress` | |
| `createNewCustomerAddress` | |
| `onSaveAddress` | |
| `isValidAddress` | |
| `onChangeDefaultAddress` | |
| `createPrefix` | |
| `onAddressChange` | |
| `getCustomer` | |
| `getCustomFieldSet` | |
| `addressLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `order` | |
| `versionContext` | |
| `orderCustomer` | |
| `orderRepository` | |
| `addressRepository` | |
| `customerRepository` | |
| `customerCriteria` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `addressOptions` | |
| `modalTitle` | |
| `selectedAddressId` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
    <sw-order-address-selection
        class="sw-order-detail-details__billing-address"
        type="billing"
        :address="billingAddress"
        :address-id="selectedBillingAddressId"
        :disabled="!acl.can('order.editor') || undefined"
        :label="$tc('sw-order.createBase.detailsBody.labelBillingAddress')"
        @change-address="onChangeOrderAddress"
    />
    {% endblock %}

    {% block sw_order_detail_details_payment_method_select %}
    <sw-entity-single-select
        v-model:value="transaction.paymentMethodId"
        entity="payment_method"
```

#### Example 2
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-address-selection
    class="sw-order-detail-details__shipping-address"
    type="shipping"
    :address="shippingAddress"
    :address-id="selectedShippingAddressId"
    :disabled="!acl.can('order.editor') || undefined"
    :label="$tc('sw-order.createBase.detailsBody.labelShippingAddress')"
    @change-address="onChangeOrderAddress"
/>
{% endblock %}

{% block sw_order_detail_details_shipping_method_select %}
<sw-entity-single-select
    v-model:value="delivery.shippingMethodId"
    entity="shipping_method"
```

## sw-order-create-address-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| address | `any` | — | yes |  |
| addAddressModalTitle | `any` | — | yes |  |
| editAddressModalTitle | `any` | — | yes |  |
| cart | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| set-customer-address | — | |
| close-modal | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getCustomerAddresses` | |
| `onNewActiveItem` | |
| `isCurrentSelected` | |
| `onSearchAddress` | |
| `onSelectExistingAddress` | |
| `findSelectedAddress` | |
| `updateOrderContext` | |
| `saveCurrentCustomer` | |
| `saveCurrentAddress` | |
| `closeModal` | |
| `onCancel` | |
| `onSave` | |
| `onCloseAddressModal` | |
| `onAddNewAddress` | |
| `onEditAddress` | |
| `onChangeDefaultAddress` | |
| `onSubmitAddressForm` | |
| `getAddressFormModalTitle` | |
| `createNewCustomerAddress` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `addressCriteria` | |
| `customerRepository` | |
| `addressRepository` | |
| `isValidCompanyField` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-create-address-modal
    v-if="showAddressModal"
    :address="address"
    :add-address-modal-title="addAddressModalTitle"
    :edit-address-modal-title="editAddressModalTitle"
    :customer="customer"
    :cart="cart"
    @close-modal="closeModal"
    @set-customer-address="setCustomerAddress"
/>
{% endblock %}

{% block sw_order_create_promotion_modal %}
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
```

## sw-order-create-base

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| error | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `createCart` | |
| `loadCart` | |
| `onSelectExistingCustomer` | |
| `updateCustomerContext` | |
| `setCustomer` | |
| `setCurrency` | |
| `onEditBillingAddress` | |
| `onEditShippingAddress` | |
| `setCustomerAddress` | |
| `closeModal` | |
| `save` | |
| `onSaveItem` | |
| `onRemoveItems` | |
| `updateLoading` | |
| `sortByTaxRate` | |
| `onSubmitCode` | |
| `onRemoveExistingCode` | |
| `updatePromotionList` | |
| `handlePromotionCodeTags` | |
| `onShippingChargeEdited` | |
| `switchAutomaticPromotions` | |
| `enableAutomaticPromotions` | |
| `onClosePromotionModal` | |
| `onSavePromotionModal` | |
| `onShippingChargeUpdated` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cartErrors` | |
| `customerRepository` | |
| `customerAddressRepository` | |
| `currencyRepository` | |
| `customerAddressCriteria` | |
| `defaultCriteria` | |
| `orderDate` | |
| `customer` | |
| `salesChannelId` | |
| `isCustomerActive` | |
| `cart` | |
| `cartLineItems` | |
| `cartAutomaticPromotionItems` | |
| `cartPrice` | |
| `currency` | |
| `cartDelivery` | |
| `promotionCodeTags` | |
| `cartDeliveryDiscounts` | |
| `filteredCalculatedTaxes` | |
| `promotionCodeLineItems` | |
| `hasLineItem` | |
| `shippingCostsDetail` | |
| `disabledAutoPromotionVisibility` | |
| `taxStatus` | |
| `displayRounded` | |
| `orderTotal` | |
| `currencyFilter` | |

### Examples

#### Basic Usage
```twig
<sw-order-create-base>
    <!-- content -->
</sw-order-create-base>
```

## sw-order-create-details-body

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | no |  |
| isCustomerActive | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-edit-billing-address | — | |
| on-edit-shipping-address | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onEditBillingAddress` | |
| `onEditShippingAddress` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `email` | |
| `phoneNumber` | |
| `billingAddress` | |
| `shippingAddress` | |
| `isAddressIdentical` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
                <sw-order-create-details-body
                    :customer="customer"
                    :is-customer-active="isCustomerActive"
                    @on-edit-billing-address="onEditBillingAddress"
                    @on-edit-shipping-address="onEditShippingAddress"
                />
                {% endblock %}
            </sw-card-section>
            <sw-card-section
                secondary
                divider="top"
            >
                {% block sw_order_create_details_footer %}
                <sw-order-create-details-footer
                    :customer="customer"
```

## sw-order-create-details-footer

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| cart | `any` | — | yes |  |
| customer | `any` | `null` | no |  |
| isCustomerActive | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `updateContext` | |
| `updateOrderContext` | |
| `updateCustomerContext` | |
| `getCart` | |
| `getCurrency` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `context` | |
| `salesChannelId` | |
| `salesChannelCriteria` | |
| `paymentMethodCriteria` | |
| `currencyRepository` | |
| `currentCurrencyId` | |
| `defaultSalesChannel` | |
| `isCartTokenAvailable` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
                <sw-order-create-details-footer
                    :customer="customer"
                    :is-customer-active="isCustomerActive"
                    :cart="cart"
                    @loading-change="updateLoading"
                />
                {% endblock %}
            </sw-card-section>
        </sw-container>
    </template>
</mt-card>
{% endblock %}

{% block sw_order_create_base_line_items_card %}
<mt-card
```

## sw-order-create-details-header

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | no |  |
| orderDate | `any` | — | yes |  |
| cartPrice | `any` | — | no |  |
| currency | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-select-existing-customer | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSelectExistingCustomer` | |
| `onShowNewCustomerModal` | |
| `onCloseNewCustomerModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerId` | |
| `customerCriteria` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
    <sw-order-create-details-header
        :customer="customer"
        :order-date="orderDate"
        :cart-price="cartPrice"
        :currency="currency"
        @on-select-existing-customer="onSelectExistingCustomer"
    />
    {% endblock %}
    {% block sw_order_create_details_body %}
    <sw-order-create-details-body
        :customer="customer"
        :is-customer-active="isCustomerActive"
        @on-edit-billing-address="onEditBillingAddress"
        @on-edit-shipping-address="onEditShippingAddress"
    />
```

## sw-order-create-details

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateContext` | |
| `loadCart` | |
| `onRemoveExistingCode` | |
| `onRemoveItems` | |
| `updatePromotionList` | |
| `toggleAutomaticPromotions` | |
| `onClosePromotionModal` | |
| `onSavePromotionModal` | |
| `modifyShippingCosts` | |
| `handlePromotionCodeTags` | |
| `onSubmitCode` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelId` | |
| `customer` | |
| `cart` | |
| `currency` | |
| `salesChannelContext` | |
| `email` | |
| `phoneNumber` | |
| `cartDelivery` | |
| `shippingCosts` | |
| `deliveryDate` | |
| `shippingMethodCriteria` | |
| `paymentMethodCriteria` | |
| `languageCriteria` | |
| `currencyCriteria` | |
| `currencyRepository` | |
| `isCartTokenAvailable` | |
| `hasLineItem` | |
| `promotionCodeLineItems` | |
| `disabledAutoPromotion` | |
| `promotionCodeTags` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
    <sw-order-create-details-header
        :customer="customer"
        :order-date="orderDate"
        :cart-price="cartPrice"
        :currency="currency"
        @on-select-existing-customer="onSelectExistingCustomer"
    />
    {% endblock %}
    {% block sw_order_create_details_body %}
    <sw-order-create-details-body
        :customer="customer"
        :is-customer-active="isCustomerActive"
        @on-edit-billing-address="onEditBillingAddress"
        @on-edit-shipping-address="onEditShippingAddress"
    />
```

## sw-order-create-general-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| cart | `any` | — | yes |  |
| context | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `summaryMainHeader` | |
| `paymentMethodName` | |
| `shippingMethodName` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
    <sw-order-create-general-info
        :cart="cart"
        :context="context"
        :is-loading="isLoading"
    />
</mt-card>

<sw-extension-component-section
    position-identifier="sw-order-create-base-line-items__before"
/>

<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
```

## sw-order-create-general

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSaveItem` | |
| `onShippingChargeEdited` | |
| `onRemoveItems` | |
| `loadCart` | |
| `sortByTaxRate` | |
| `onShippingChargeUpdated` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customer` | |
| `cart` | |
| `currency` | |
| `context` | |
| `isCustomerActive` | |
| `cartDelivery` | |
| `cartDeliveryDiscounts` | |
| `taxStatus` | |
| `shippingCostsDetail` | |
| `filteredCalculatedTaxes` | |
| `displayRounded` | |
| `orderTotal` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
    <sw-order-create-general-info
        :cart="cart"
        :context="context"
        :is-loading="isLoading"
    />
</mt-card>

<sw-extension-component-section
    position-identifier="sw-order-create-base-line-items__before"
/>

<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
```

## sw-order-create-initial-modal

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onCloseModal` | |
| `onPreviewOrder` | |
| `onSaveItem` | |
| `addPromotionCodes` | |
| `updatePromotion` | |
| `onRemoveItems` | |
| `updateAutoPromotionToggle` | |
| `updateShippingCost` | |
| `updateOrderContext` | |
| `disableAutoAppliedPromotions` | |
| `modifyShippingCost` | |
| `cancelCart` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelId` | |
| `salesChannelContext` | |
| `currency` | |
| `cart` | |
| `customer` | |
| `isCustomerActive` | |
| `promotionCodeItems` | |
| `cartDelivery` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-initial/sw-order-create-initial.html.twig`
```twig
    <sw-order-create-initial-modal
        v-if="routeCustomerReady"
        @modal-close="onCloseCreateModal"
        @order-preview="onPreviewOrder"
    />
    <sw-loader v-else />
</div>
{% endblock %}

```

## sw-order-create-initial

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCloseCreateModal` | |
| `onPreviewOrder` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerRepository` | |
| `customerCriteria` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-initial/sw-order-create-initial.html.twig`
```twig
    <sw-order-create-initial-modal
        v-if="routeCustomerReady"
        @modal-close="onCloseCreateModal"
        @order-preview="onPreviewOrder"
    />
    <sw-loader v-else />
</div>
{% endblock %}

```

## sw-order-create-invalid-promotion-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| confirm | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClose` | |
| `onConfirm` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `invalidPromotionCodes` | |

### Examples

#### Example 1
Source: `sw-order/page/sw-order-create/sw-order-create.html.twig`
```twig
<sw-order-create-invalid-promotion-modal
    v-if="showInvalidCodeModal"
    @confirm="removeInvalidCode"
    @close="closeInvalidCodeModal"
/>
{% endblock %}

{% block sw_order_create_remind_payment_modal %}
<sw-modal
    v-if="showRemindPaymentModal"
    class="sw-order-create__remind-payment-modal"
    :title="$tc('sw-order.create.remindPaymentModal.title')"
    :is-loading="remindPaymentModalLoading"
    @modal-close="onRemindPaymentModalClose"
>
```

## sw-order-create-options

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotionCodes | `any` | — | yes |  |
| disabledAutoPromotion | `any` | — | yes |  |
| context | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `updateSameAsBillingAddressToggle` | |
| `createdComponent` | |
| `validatePromotions` | |
| `onToggleAutoPromotion` | |
| `changePromotionCodes` | |
| `updateCartContext` | |
| `updateOrderContext` | |
| `loadCart` | |
| `onChangeShippingCost` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelId` | |
| `salesChannelCriteria` | |
| `shippingMethodCriteria` | |
| `paymentMethodCriteria` | |
| `customer` | |
| `currency` | |
| `cart` | |
| `cartDelivery` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-create-initial-modal/sw-order-create-initial-modal.html.twig`
```twig
                <sw-order-create-options
                    v-show="active === 'options'"
                    :disabled="!customer || undefined"
                    :disabled-auto-promotion="disabledAutoPromotion"
                    :promotion-codes="promotionCodes"
                    :context="context"
                    @promotions-change="updatePromotion"
                    @auto-promotion-toggle="updateAutoPromotionToggle"
                    @shipping-cost-change="updateShippingCost"
                />
                {% endblock %}
            </div>
            {% endblock %}
        </template>
    </sw-tabs>
```

## sw-order-create-promotion-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currency | `any` | — | yes |  |
| salesChannelId | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |
| `disableAutomaticPromotions` | |
| `getDescription` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cart` | |
| `cartAutomaticPromotionItems` | |
| `hasNoAutomaticPromotions` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
    :is-loading="isLoading"
    :currency="currency"
    :sales-channel-id="salesChannelId"
    @close="onClosePromotionModal"
    @save="onSavePromotionModal"
/>
{% endblock %}

{% block sw_order_create_details_payment %}
<mt-card
    class="sw-order-create-details__payment"
    position-identifier="sw-order-create-details-payment"
    :title="$tc('sw-order.createBase.detailsTab.labelTransactionCard')"
```

#### Example 2
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
    :is-loading="isLoading"
    :currency="currency"
    :sales-channel-id="customer.salesChannelId"
    @close="onClosePromotionModal"
    @save="onSavePromotionModal"
/>
{% endblock %}

{% block sw_order_create_details %}
<mt-card
    :title="$tc('sw-order.createBase.labelDetailsCard')"
    :is-loading="isLoadingDetail"
    position-identifier="sw-order-create-base-details"
```

## sw-order-create

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `redirectToOrderList` | |
| `saveFinish` | |
| `onSaveOrder` | |
| `fetchPaymentMethodName` | |
| `onCancelOrder` | |
| `showError` | |
| `openInvalidCodeModal` | |
| `closeInvalidCodeModal` | |
| `removeInvalidCode` | |
| `onRemindPaymentModalClose` | |
| `onRemindCustomer` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customer` | |
| `cart` | |
| `invalidPromotionCodes` | |
| `isSaveOrderValid` | |
| `orderValidateErrorMessage` | |
| `paymentMethodRepository` | |
| `showInitialModal` | |

### Examples

#### Example 1
Source: `sw-order/page/sw-order-create/sw-order-create.html.twig`
```twig
<sw-order-create-invalid-promotion-modal
    v-if="showInvalidCodeModal"
    @confirm="removeInvalidCode"
    @close="closeInvalidCodeModal"
/>
{% endblock %}

{% block sw_order_create_remind_payment_modal %}
<sw-modal
    v-if="showRemindPaymentModal"
    class="sw-order-create__remind-payment-modal"
    :title="$tc('sw-order.create.remindPaymentModal.title')"
    :is-loading="remindPaymentModalLoading"
    @modal-close="onRemindPaymentModalClose"
>
```

#### Example 2
Source: `sw-order/component/sw-order-create-initial-modal/sw-order-create-initial-modal.html.twig`
```twig
                <sw-order-create-options
                    v-show="active === 'options'"
                    :disabled="!customer || undefined"
                    :disabled-auto-promotion="disabledAutoPromotion"
                    :promotion-codes="promotionCodes"
                    :context="context"
                    @promotions-change="updatePromotion"
                    @auto-promotion-toggle="updateAutoPromotionToggle"
                    @shipping-cost-change="updateShippingCost"
                />
                {% endblock %}
            </div>
            {% endblock %}
        </template>
    </sw-tabs>
```

#### Example 3
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
    <sw-order-create-general-info
        :cart="cart"
        :context="context"
        :is-loading="isLoading"
    />
</mt-card>

<sw-extension-component-section
    position-identifier="sw-order-create-base-line-items__before"
/>

<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
```

#### Example 4
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
    :is-loading="isLoading"
    :currency="currency"
    :sales-channel-id="salesChannelId"
    @close="onClosePromotionModal"
    @save="onSavePromotionModal"
/>
{% endblock %}

{% block sw_order_create_details_payment %}
<mt-card
    class="sw-order-create-details__payment"
    position-identifier="sw-order-create-details-payment"
    :title="$tc('sw-order.createBase.detailsTab.labelTransactionCard')"
```

#### Example 5
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-create-address-modal
    v-if="showAddressModal"
    :address="address"
    :add-address-modal-title="addAddressModalTitle"
    :edit-address-modal-title="editAddressModalTitle"
    :customer="customer"
    :cart="cart"
    @close-modal="closeModal"
    @set-customer-address="setCustomerAddress"
/>
{% endblock %}

{% block sw_order_create_promotion_modal %}
<sw-order-create-promotion-modal
    v-if="showPromotionModal"
```

## sw-order-customer-address-select

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customer | `any` | — | yes |  |
| value | `any` | — | yes |  |
| sameAddressLabel | `any` | `''` | no |  |
| sameAddressValue | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getSelectionLabel` | |
| `getCustomerAddress` | |
| `getCustomerAddresses` | |
| `searchAddress` | |
| `searchAddressResults` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `addressId` | |
| `isSameAddress` | |
| `addressRepository` | |
| `addressCriteria` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-create-options/sw-order-create-options.html.twig`
```twig
    <sw-order-customer-address-select
        v-model:value="context.billingAddressId"
        class="sw-order-create-options__billing-address"
        :label="$tc('sw-order.createBase.labelBillingAddress')"
        :placeholder="$tc('sw-order.createBase.placeholderBillingAddress')"
        :same-address-value="context.shippingAddressId"
        :customer="customer"
    />
    {% endblock %}

    {% block sw_order_create_options_order_currency %}
    <sw-entity-single-select
        v-model:value="context.currencyId"
        class="sw-order-create-options__currency-select"
        entity="currency"
```

#### Example 2
Source: `sw-order/component/sw-order-create-options/sw-order-create-options.html.twig`
```twig
        <sw-order-customer-address-select
            v-model:value="context.shippingAddressId"
            class="sw-order-create-options__shipping-address"
            :label="$tc('sw-order.createBase.labelShippingAddress')"
            :placeholder="$tc('sw-order.createBase.placeholderShippingAddress')"
            :same-address-label="$tc('sw-order.initialModal.options.textSameAsBillingAddress')"
            :same-address-value="context.billingAddressId"
            :customer="customer"
            :disabled="isSameAsBillingAddress"
        />
        {% endblock %}
    </sw-container>
    {% endblock %}
    {% endblock %}
</div>
```

#### Example 3
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-customer-address-select
    v-model:value="context.billingAddressId"
    :label="$tc('sw-order.createBase.labelBillingAddress')"
    :placeholder="$tc('sw-order.createBase.placeholderBillingAddress')"
    :same-address-value="context.shippingAddressId"
    :customer="customer"
/>

<sw-entity-single-select
    v-model:value="context.paymentMethodId"
    entity="payment_method"
    label-property="distinguishableName"
    class="sw_order_create-details__payment-method"
    :criteria="paymentMethodCriteria"
    :label="$tc('sw-order.createBase.labelPaymentMethod')"
```

#### Example 4
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
<sw-order-customer-address-select
    v-model:value="context.shippingAddressId"
    :label="$tc('sw-order.createBase.labelShippingAddress')"
    :placeholder="$tc('sw-order.createBase.placeholderShippingAddress')"
    :same-address-label="$tc('sw-order.initialModal.options.textSameAsBillingAddress')"
    :same-address-value="context.billingAddressId"
    :customer="customer"
/>

<sw-entity-single-select
    v-model:value="context.shippingMethodId"
    show-clearable-button
    class="sw_order_create-details__shipping"
    entity="shipping_method"
    :criteria="shippingMethodCriteria"
```

## sw-order-customer-comment

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customerComment | `any` | `''` | yes |  |
| isLoading | `any` | `false` | no |  |

### Examples

#### Basic Usage
```twig
<sw-order-customer-comment
    customerComment="..."
>
    <!-- content -->
</sw-order-customer-comment>
```

## sw-order-customer-grid

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getList` | |
| `onShowNewCustomerModal` | |
| `isChecked` | |
| `onCheckCustomer` | |
| `createCart` | |
| `setCustomer` | |
| `handleSelectCustomer` | |
| `onAddNewCustomer` | |
| `updateCustomerContext` | |
| `getCart` | |
| `loadSalesChannel` | |
| `onSalesChannelChange` | |
| `onCloseSalesChannelSelectModal` | |
| `onSelectSalesChannel` | |
| `customerUnavailable` | |
| `onChangeCustomer` | |
| `onCloseCustomerChangesModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerData` | |
| `customerRepository` | |
| `customerCriteria` | |
| `customerCriterion` | |
| `customerColumns` | |
| `showEmptyState` | |
| `emptyTitle` | |
| `cart` | |
| `assetFilter` | |
| `salesChannelRepository` | |
| `salesChannelCriteria` | |
| `isSelectSalesChannelDisabled` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-create-initial-modal/sw-order-create-initial-modal.html.twig`
```twig
<sw-order-customer-grid />
```

## sw-order-delivery-metadata

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| delivery | `any` | — | yes |  |
| order | `any` | — | yes |  |
| title | `any` | `null` | no |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `renderFormattingAddress` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currencyFilter` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-order-delivery-metadata
    delivery="..."
    order="..."
>
    <!-- content -->
</sw-order-delivery-metadata>
```

## sw-order-detail-details

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| orderId | `any` | — | yes |  |
| isSaveSuccessful | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-loading | — | |
| save-and-recalculate | — | |
| save-and-reload | — | |
| save-edits | — | |
| reload-entity-data | — | |
| error | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onShippingChargeEdited` | |
| `loadingChange` | |
| `saveAndRecalculate` | |
| `saveAndReload` | |
| `onSaveEdits` | |
| `reloadEntityData` | |
| `showError` | |
| `updateLoading` | |
| `validateTrackingCode` | |
| `onChangeOrderAddress` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `order` | |
| `versionContext` | |
| `orderAddressIds` | |
| `orderOrderCustomerEmailError` | |
| `delivery` | |
| `transaction` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `salesChannelCriteria` | |
| `paymentMethodCriteria` | |
| `taxStatus` | |
| `currency` | |
| `billingAddress` | |
| `shippingAddress` | |
| `selectedBillingAddressId` | |
| `selectedShippingAddressId` | |
| `shippingCosts` | |

### Examples

#### Basic Usage
```twig
<sw-order-detail-details
    orderId="..."
>
    <!-- content -->
</sw-order-detail-details>
```

## sw-order-detail-documents

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-and-reload | — | |
| update-loading | — | |

### Methods

| Method | Description |
|--------|-------------|
| `saveAndReload` | |
| `onUpdateLoading` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `order` | |
| `versionContext` | |

### Examples

#### Basic Usage
```twig
<sw-order-detail-documents>
    <!-- content -->
</sw-order-detail-documents>
```

## sw-order-detail-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| orderId | `any` | — | yes |  |
| isSaveSuccessful | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-and-recalculate | — | |
| save-edits | — | |
| recalculate-and-reload | — | |
| save-and-reload | — | |
| reload-entity-data | — | |
| error | — | |

### Methods

| Method | Description |
|--------|-------------|
| `sortByTaxRate` | |
| `onShippingChargeEdited` | |
| `onShippingChargeUpdated` | |
| `saveAndRecalculate` | |
| `onSaveEdits` | |
| `recalculateAndReload` | |
| `updateLoading` | |
| `reloadEntityData` | |
| `saveAndReload` | |
| `showError` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `loading` | |
| `order` | |
| `versionContext` | |
| `delivery` | |
| `deliveryDiscounts` | |
| `shippingCostsDetail` | |
| `sortedCalculatedTaxes` | |
| `taxStatus` | |
| `displayRounded` | |
| `orderTotal` | |
| `currency` | |
| `currencyFilter` | |

### Examples

#### Basic Usage
```twig
<sw-order-detail-general
    orderId="..."
>
    <!-- content -->
</sw-order-detail-general>
```

## sw-order-detail

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| orderId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `updateCreatedById` | |
| `onChangeLanguage` | |
| `saveEditsFinish` | |
| `onStartEditing` | |
| `onSaveEdits` | |
| `handleOrderAddressUpdate` | |
| `onCancelEditing` | |
| `onSaveAndRecalculate` | |
| `onRecalculateAndReload` | |
| `onSaveAndReload` | |
| `saveAndReload` | |
| `onUpdateLoading` | |
| `onUpdateEditing` | |
| `onError` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `reloadEntityData` | |
| `createNewVersionId` | |
| `updateOrderAddresses` | |
| `updateEditing` | |
| `convertMissingProductLineItems` | |
| `handleCartErrors` | |
| `askAndSaveEdits` | |
| `onAskAndSaveEditsConfirm` | |
| `onAskAndSaveEditsCancel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `order` | |
| `versionContext` | |
| `orderAddressIds` | |
| `editing` | |
| `loading` | |
| `isLoading` | |
| `isSaveSuccessful` | |
| `orderIdentifier` | |
| `orderChanges` | |
| `showTabs` | |
| `showWarningTabStyle` | |
| `isOrderEditing` | |
| `orderRepository` | |
| `automaticPromotions` | |
| `deliveryDiscounts` | |
| `orderCriteria` | |
| `convertedProductLineItems` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-details-state-card
    v-if="transaction"
    position="transaction"
    :title="$tc('sw-order.detailsTab.labelTransactionCard')"
    :order="order"
    :entity="transaction"
    :state-label="$tc('sw-order.stateCard.headlineTransactionState')"
    :disabled="!acl.can('order.editor') || undefined"
    @show-status-history="showStateHistoryModal = true"
    @save-edits="onSaveEdits"
>

    {% block sw_order_detail_details_payment_billing_address %}
    <sw-order-address-selection
        class="sw-order-detail-details__billing-address"
```

#### Example 2
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-details-state-card
    v-if="delivery"
    position="delivery"
    :title="$tc('sw-order.detailsTab.labelDeliveryCard')"
    :order="order"
    :entity="delivery"
    :state-label="$tc('sw-order.stateCard.headlineDeliveryState')"
    :disabled="!acl.can('order.editor') || undefined"
    @show-status-history="showStateHistoryModal = true"
    @save-edits="onSaveEdits"
>

    {% block sw_order_detail_details_shipping_address %}
    <sw-order-address-selection
        class="sw-order-detail-details__shipping-address"
```

## sw-order-details-state-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| title | `any` | `''` | no |  |
| entity | `any` | — | yes |  |
| stateLabel | `any` | `''` | no |  |
| isLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| position | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| show-status-history | — | |
| save-edits | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onShowStatusHistory` | |
| `getTransitionOptions` | |
| `buildTransitionOptions` | |
| `onStateSelected` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `createStateChangeErrorNotification` | |
| `getLastChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineHistoryRepository` | |
| `stateMachineStateCriteria` | |
| `stateMachineHistoryCriteria` | |
| `entityName` | |
| `stateName` | |
| `stateSelectBackgroundStyle` | |
| `stateTransitionMethod` | |
| `cardPosition` | |
| `lastChangeAuthorLabel` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-details-state-card
    v-if="transaction"
    position="transaction"
    :title="$tc('sw-order.detailsTab.labelTransactionCard')"
    :order="order"
    :entity="transaction"
    :state-label="$tc('sw-order.stateCard.headlineTransactionState')"
    :disabled="!acl.can('order.editor') || undefined"
    @show-status-history="showStateHistoryModal = true"
    @save-edits="onSaveEdits"
>

    {% block sw_order_detail_details_payment_billing_address %}
    <sw-order-address-selection
        class="sw-order-detail-details__billing-address"
```

#### Example 2
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
<sw-order-details-state-card
    v-if="delivery"
    position="delivery"
    :title="$tc('sw-order.detailsTab.labelDeliveryCard')"
    :order="order"
    :entity="delivery"
    :state-label="$tc('sw-order.stateCard.headlineDeliveryState')"
    :disabled="!acl.can('order.editor') || undefined"
    @show-status-history="showStateHistoryModal = true"
    @save-edits="onSaveEdits"
>

    {% block sw_order_detail_details_shipping_address %}
    <sw-order-address-selection
        class="sw-order-detail-details__shipping-address"
```

## sw-order-document-card

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| attachView | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-loading | — | |
| document-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `convertStoreEventToVueEvent` | |
| `getList` | |
| `documentTypeAvailable` | |
| `invoiceExists` | |
| `onSearchTermChange` | |
| `createDocument` | |
| `onCancelCreation` | |
| `onPrepareDocument` | |
| `openDocument` | |
| `downloadDocument` | |
| `markDocumentAsSent` | |
| `markDocumentAsUnsent` | |
| `onCreateDocument` | |
| `onPreview` | |
| `onOpenDocument` | |
| `onDownload` | |
| `onSendDocument` | |
| `onMarkDocumentAsSent` | |
| `onMarkDocumentAsUnsent` | |
| `onCloseSendDocumentModal` | |
| `onDocumentSent` | |
| `onLoadingDocument` | |
| `onLoadingPreview` | |
| `onShowSelectDocumentTypeModal` | |
| `onCloseSelectDocumentTypeModal` | |
| `availableFormatsFilter` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isEditing` | |
| `creditItems` | |
| `documentTypeRepository` | |
| `documentRepository` | |
| `documentsEmpty` | |
| `documentModal` | |
| `documentCardStyles` | |
| `documentTypeCriteria` | |
| `documentCriteria` | |
| `getDocumentColumns` | |
| `isDataLoading` | |
| `showCardFilter` | |
| `showCreateDocumentButton` | |
| `emptyStateTitle` | |
| `tooltipCreateDocumentButton` | |
| `assetFilter` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-state-change-modal/sw-order-state-change-modal-attach-documents/sw-order-state-change-modal-attach-documents.html.twig`
```twig
<sw-order-document-card
    ref="attachDocuments"
    class="sw-order-detail-base__documents-grid"
    :order="order"
    :is-loading="isLoading"
    attach-view
/>
{% endblock %}

{% block sw_order_state_change_modal_attach_documents_internal_comment %}
<mt-textarea
    v-model="internalComment"
    :label="$tc('sw-order.stateCard.labelInternalComment')"
    :is-loading="isLoading"
/>
```

#### Example 2
Source: `sw-order/view/sw-order-detail-documents/sw-order-detail-documents.html.twig`
```twig
    <sw-order-document-card
        :order="order"
        @document-save="saveAndReload"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-order-document-settings-credit-note-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-document | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCreateDocument` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `highlightedItems` | |
| `documentPreconditionsFulfilled` | |
| `documentNumber` | |
| `invoices` | |
| `invoiceNumberOptions` | |

### Examples

#### Basic Usage
```twig
<sw-order-document-settings-credit-note-modal>
    <!-- content -->
</sw-order-document-settings-credit-note-modal>
```

## sw-order-document-settings-delivery-note-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-document | — | |
| loading-preview | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCreateDocument` | |
| `onPreview` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `documentPreconditionsFulfilled` | |

### Examples

#### Basic Usage
```twig
<sw-order-document-settings-delivery-note-modal>
    <!-- content -->
</sw-order-document-settings-delivery-note-modal>
```

## sw-order-document-settings-invoice-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-preview | — | |

### Methods

| Method | Description |
|--------|-------------|
| `addAdditionalInformationToDocument` | |
| `onPreview` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `documentNumber` | |

### Examples

#### Basic Usage
```twig
<sw-order-document-settings-invoice-modal>
    <!-- content -->
</sw-order-document-settings-invoice-modal>
```

## sw-order-document-settings-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| currentDocumentType | `any` | — | yes |  |
| isLoadingDocument | `any` | — | yes |  |
| isLoadingPreview | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-document | — | |
| document-create | — | |
| preview-show | — | |
| page-leave-confirm | — | |
| page-leave | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCreateDocument` | |
| `callDocumentCreate` | |
| `reserveDocumentNumber` | |
| `addAdditionalInformationToDocument` | |
| `onPreview` | |
| `onConfirm` | |
| `onCancel` | |
| `openMediaModal` | |
| `closeMediaModal` | |
| `onAddMediaFromLibrary` | |
| `successfulUploadFromUrl` | |
| `validateFile` | |
| `removeCustomDocument` | |
| `onAddDocument` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `invalidInput` | |
| `documentNumberErrorMessage` | |
| `documentPreconditionsFulfilled` | |
| `modalTitle` | |
| `mediaRepository` | |
| `htmlPreviewDisabled` | |
| `documentNumber` | |

### Examples

#### Basic Usage
```twig
<sw-order-document-settings-modal
    order="..."
    currentDocumentType="..."
    isLoadingDocument="..."
>
    <!-- content -->
</sw-order-document-settings-modal>
```

## sw-order-document-settings-storno-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| currentDocumentType | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-document | — | |
| loading-preview | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCreateDocument` | |
| `onPreview` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `documentPreconditionsFulfilled` | |
| `invoices` | |
| `documentNumber` | |
| `invoiceOptions` | |

### Examples

#### Basic Usage
```twig
<sw-order-document-settings-storno-modal
    order="..."
    currentDocumentType="..."
>
    <!-- content -->
</sw-order-document-settings-storno-modal>
```

## sw-order-general-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-edits | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getLiveOrder` | |
| `onTagAdd` | |
| `onTagRemove` | |
| `getAllStates` | |
| `buildTransitionOptions` | |
| `backgroundStyle` | |
| `getTransitionOptions` | |
| `onStateSelected` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `loadHistory` | |
| `createStateChangeErrorNotification` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `savedSuccessful` | |
| `lastChangedUser` | |
| `lastChangedDateTime` | |
| `lastChangedByCriteria` | |
| `orderRepository` | |
| `orderTagRepository` | |
| `stateMachineStateRepository` | |
| `stateMachineStateCriteria` | |
| `transaction` | |
| `delivery` | |
| `currencyFilter` | |
| `dateFilter` | |
| `emailIdnFilter` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
    <sw-order-general-info
        ref="swOrderGeneralInfo"
        :order="order"
        @save-edits="onSaveEdits"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_order_detail_general_line_items_card %}
<sw-extension-component-section
    position-identifier="sw-order-detail-base-line-items__before"
/>

<mt-card
```

## sw-order-inline-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| displayValue | `any` | `''` | yes |  |
| editable | `any` | `false` | yes |  |
| required | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onInput` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
    <sw-order-inline-field
        v-model:value="currentOrder.orderCustomer.email"
        :display-value="currentOrder.orderCustomer.email ? currentOrder.orderCustomer.email : $tc('sw-order.detailBase.labelNoEmail')"
        required
        :editable="isEditing"
        @update:value="$emit('order-change')"
    />
</dd>
{% endblock %}

{% block sw_order_detail_base_order_overview_billing_address %}
<dt>
    {{ $tc('sw-order.detailBase.headlineBillingAddress') }}
    <mt-button
        v-if="isEditing"
```

#### Example 2
Source: `sw-order/component/sw-order-user-card/sw-order-user-card.html.twig`
```twig
    <sw-order-inline-field
        v-model:value="billingAddress.phoneNumber"
        :display-value="billingAddress.phoneNumber? billingAddress.phoneNumber : $tc('sw-order.detailBase.labelNoPhoneNumber')"
        :editable="isEditing"
        class="sw-order-inline-field__truncateable"
        @update:value="$emit('order-change')"
    />
</dd>
{% endblock %}

{% block sw_order_detail_base_order_overview_shipping_address %}
<dt>
    {{ $tc('sw-order.detailBase.headlineDeliveryAddress') }}
    <mt-button
        v-show="hasDifferentBillingAndShippingAddress && isEditing"
```

## sw-order-leave-page-modal

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
Source: `sw-order/page/sw-order-detail/sw-order-detail.html.twig`
```twig
<sw-order-leave-page-modal
    v-if="isDisplayingLeavePageWarning"
    @page-leave-cancel="onLeaveModalClose"
    @page-leave-confirm="onLeaveModalConfirm"
/>
{% endblock %}
{% block sw_order_detail_content_save_changes_beforehand_modal %}
<sw-order-save-changes-beforehand-modal
    v-if="askForSaveBeforehand"
    @cancel="onAskAndSaveEditsCancel"
    @confirm="onAskAndSaveEditsConfirm"
>
    {{ askForSaveBeforehand.reason }}
</sw-order-save-changes-beforehand-modal>
{% endblock %}
```

## sw-order-line-items-grid-sales-channel

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannelId | `any` | `''` | yes |  |
| cart | `any` | — | yes |  |
| currency | `any` | — | yes |  |
| isCustomerActive | `any` | `false` | no |  |
| isLoading | `any` | `false` | no |  |
| title | `any` | `''` | no |  |
| positionIdentifier | `any` | `'sw-order-line-items-grid-sales-channel'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| footer | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-save-item | — | |
| on-remove-items | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `createNewOrderLineItem` | |
| `initLineItem` | |
| `onInsertExistingItem` | |
| `onInsertBlankItem` | |
| `onInsertCreditItem` | |
| `onSelectionChanged` | |
| `onDeleteSelectedItems` | |
| `onDeleteItem` | |
| `itemCreatedFromProduct` | |
| `onSearchTermChange` | |
| `isCreditItem` | |
| `isProductItem` | |
| `getMinItemPrice` | |
| `isPromotionItem` | |
| `isAutoPromotionItem` | |
| `showTaxValue` | |
| `checkItemPrice` | |
| `tooltipTaxDetail` | |
| `hasMultipleTaxes` | |
| `changeItemQuantity` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `orderLineItemRepository` | |
| `cartLineItems` | |
| `lineItemTypes` | |
| `isCartTokenAvailable` | |
| `isAddNewItemButtonDisabled` | |
| `taxStatus` | |
| `unitPriceLabel` | |
| `getLineItemColumns` | |
| `assetFilter` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-create-initial-modal/sw-order-create-initial-modal.html.twig`
```twig
                <sw-order-line-items-grid-sales-channel
                    v-show="active === 'products'"
                    :is-loading="isProductGridLoading"
                    :sales-channel-id="salesChannelId"
                    :cart="cart"
                    :currency="currency"
                    :is-customer-active="isCustomerActive"
                    @on-save-item="onSaveItem"
                    @on-remove-items="onRemoveItems"
                />
                {% endblock %}

                {% block sw_order_create_modal_tabs_content_options %}
                <sw-order-create-options
                    v-show="active === 'options'"
```

#### Example 2
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
    :title="$tc('sw-order.createBase.generalTab.labelLineItemsCard')"
    editable
    :cart="cart"
    :currency="currency"
    :sales-channel-id="context.salesChannel.id"
    :is-customer-active="isCustomerActive"
    @on-save-item="onSaveItem"
    @on-remove-items="onRemoveItems"
>

    <template #footer>
```

#### Example 3
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-line-items-grid-sales-channel
    ref="sw-order-line-item-grid-sales-channel"
    :cart="cart"
    :currency="currency"
    :sales-channel-id="salesChannelId"
    :is-loading="isLoading"
    :is-customer-active="isCustomerActive"
    editable
    @on-save-item="onSaveItem"
    @on-remove-items="onRemoveItems"
/>
{% endblock %}

{% block sw_order_create_base_line_items_summary %}
<sw-card-section
```

## sw-order-line-items-grid

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| context | `any` | — | yes |  |
| editable | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-edit | — | |
| existing-item-edit | — | |
| item-cancel | — | |
| item-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `createNewOrderLineItem` | |
| `onInsertBlankItem` | |
| `onInsertExistingItem` | |
| `onInsertCreditItem` | |
| `onSelectionChanged` | |
| `onDeleteSelectedItems` | |
| `onDeleteItem` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `itemCreatedFromProduct` | |
| `onSearchTermChange` | |
| `isCreditItem` | |
| `isProductItem` | |
| `isPromotionItem` | |
| `isContainerItem` | |
| `getMinItemPrice` | |
| `showTaxValue` | |
| `checkItemPrice` | |
| `tooltipTaxDetail` | |
| `openNestedLineItemsModal` | |
| `closeNestedLineItemsModal` | |
| `hasChildren` | |
| `hasMultipleTaxes` | |
| `updateItemQuantity` | |
| `refreshChildrenQuantity` | |
| `showTaxRulesInlineEdit` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `canCreateDiscounts` | |
| `orderLineItemRepository` | |
| `orderLineItems` | |
| `lineItemTypes` | |
| `taxStatus` | |
| `unitPriceLabel` | |
| `getLineItemColumns` | |
| `salesChannelId` | |
| `isProductNumberColumnVisible` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-create-initial-modal/sw-order-create-initial-modal.html.twig`
```twig
                <sw-order-line-items-grid-sales-channel
                    v-show="active === 'products'"
                    :is-loading="isProductGridLoading"
                    :sales-channel-id="salesChannelId"
                    :cart="cart"
                    :currency="currency"
                    :is-customer-active="isCustomerActive"
                    @on-save-item="onSaveItem"
                    @on-remove-items="onRemoveItems"
                />
                {% endblock %}

                {% block sw_order_create_modal_tabs_content_options %}
                <sw-order-create-options
                    v-show="active === 'options'"
```

#### Example 2
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
<sw-order-line-items-grid-sales-channel
    class="sw-order-create-general__line-items"
    position-identifier="sw-order-create-line-items"
    :is-loading="isLoading"
    :title="$tc('sw-order.createBase.generalTab.labelLineItemsCard')"
    editable
    :cart="cart"
    :currency="currency"
    :sales-channel-id="context.salesChannel.id"
    :is-customer-active="isCustomerActive"
    @on-save-item="onSaveItem"
    @on-remove-items="onRemoveItems"
>

    <template #footer>
```

#### Example 3
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-line-items-grid-sales-channel
    ref="sw-order-line-item-grid-sales-channel"
    :cart="cart"
    :currency="currency"
    :sales-channel-id="salesChannelId"
    :is-loading="isLoading"
    :is-customer-active="isCustomerActive"
    editable
    @on-save-item="onSaveItem"
    @on-remove-items="onRemoveItems"
/>
{% endblock %}

{% block sw_order_create_base_line_items_summary %}
<sw-card-section
```

#### Example 4
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
<sw-order-line-items-grid
    ref="sw-order-line-item-grid"
    :order="order"
    :context="versionContext"
    :editable="acl.can('order.editor')"
    @item-delete="recalculateAndReload"
    @item-edit="recalculateAndReload"
    @existing-item-edit="saveAndRecalculate"
    @item-cancel="recalculateAndReload"
/>
{% endblock %}

{% block sw_order_detail_general_line_items_summary %}
<sw-card-section
    divider="top"
```

## sw-order-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `deliveryTooltip` | |
| `onEdit` | |
| `onInlineEditSave` | |
| `onChangeLanguage` | |
| `getList` | |
| `getBillingAddress` | |
| `disableDeletion` | |
| `getOrderColumns` | |
| `getVariantFromOrderState` | |
| `getVariantFromPaymentState` | |
| `getVariantFromDeliveryState` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `updateCriteria` | |
| `getStatusCriteria` | |
| `onBulkEditItems` | |
| `transaction` | |
| `getDelivery` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `orderRepository` | |
| `orderColumns` | |
| `orderCriteria` | |
| `salesChannelCriteria` | |
| `filterSelectCriteria` | |
| `listFilterOptions` | |
| `listFilters` | |
| `productCriteria` | |
| `currencyFilter` | |
| `dateFilter` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-order-list>
    <!-- content -->
</sw-order-list>
```

## sw-order-nested-line-items-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| lineItem | `any` | — | yes |  |
| order | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `enrichNestedLineItems` | |
| `naturalSort` | |
| `onCloseModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `lineItemRepository` | |
| `modalTitle` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-line-items-grid/sw-order-line-items-grid.html.twig`
```twig
    <sw-order-nested-line-items-modal
        v-if="nestedLineItemsModal"
        :line-item="nestedLineItemsModal"
        :order="order"
        @modal-close="closeNestedLineItemsModal"
    />
    {% endblock %}

</sw-container>
{% endblock %}

```

## sw-order-nested-line-items-row

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| lineItem | `any` | — | yes |  |
| currency | `any` | — | yes |  |
| renderParent | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getNestingClasses` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-nested-line-items-row/sw-order-nested-line-items-row.html.twig`
```twig
        <sw-order-nested-line-items-row
            v-for="child in lineItem.children"
            :key="child.id"
            :line-item="child"
            :currency="currency"
            :render-parent="true"
        />
    </template>
    {% endblock %}

</div>
{% endblock %}

```

#### Example 2
Source: `sw-order/component/sw-order-nested-line-items-modal/sw-order-nested-line-items-modal.html.twig`
```twig
        <sw-order-nested-line-items-row
            class="sw-order-nested-line-items-modal__content"
            :line-item="lineItem"
            :currency="order.currency"
        />
        {% endblock %}

    </div>
    {% endblock %}

    {% block sw_order_nested_line_item_modal_footer %}
    <template #modal-footer>

        {% block sw_order_nested_line_item_modal_footer_content %}
        <mt-button
```

## sw-order-new-customer-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-select-existing-customer | — | |
| close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |
| `saveCustomer` | |
| `onChangeSalesChannel` | |
| `onClose` | |
| `createErrorMessageForCompanyField` | |
| `validateEmail` | |
| `loadLanguage` | |
| `getDefaultSalutationId` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `swOrderNewCustomerDetailError` | |
| `swOrderNewCustomerAddressError` | |
| `customerRepository` | |
| `addressRepository` | |
| `shippingAddress` | |
| `billingAddress` | |
| `isSameBilling` | |
| `validCompanyField` | |
| `languageRepository` | |
| `languageCriteria` | |
| `languageId` | |
| `salutationRepository` | |
| `salutationCriteria` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-create-details-header/sw-order-create-details-header.html.twig`
```twig
<sw-order-new-customer-modal
    v-if="showNewCustomerModal"
    @close="onCloseNewCustomerModal"
    @on-select-existing-customer="onSelectExistingCustomer"
/>
{% endblock %}

{% block sw_order_create_details_header_profile %}
<sw-container
    class="sw-order-user-card__container"
    columns="80px 1fr max-content"
    gap="0 24px"
>
    {% block sw_order_create_details_header_profile_avatar %}
    <sw-avatar
```

#### Example 2
Source: `sw-order/component/sw-order-customer-grid/sw-order-customer-grid.html.twig`
```twig
<sw-order-new-customer-modal
    v-if="showNewCustomerModal"
    @on-select-existing-customer="onAddNewCustomer"
    @close="showNewCustomerModal = false"
/>
{% endblock %}

{% block sw_order_customer_grid_sales_channel_select_modal %}
<sw-modal
    v-if="showSalesChannelSelectModal"
    class="sw-order-customer-grid__sales-channel-selection-modal"
    :title="$tc('sw-order.initialModal.customerGrid.titleSelectSalesChannel')"
    @modal-close="onCloseSalesChannelSelectModal"
>
    <template #default>
```

## sw-order-product-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | yes |  |
| salesChannelId | `any` | `''` | yes |  |
| taxStatus | `any` | `''` | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onItemChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `lineItemTypes` | |
| `lineItemPriceTypes` | |
| `isShownProductSelect` | |
| `isShownItemLabelInput` | |
| `contextWithInheritance` | |
| `productCriteria` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-line-items-grid-sales-channel/sw-order-line-items-grid-sales-channel.html.twig`
```twig
<sw-order-product-select
    v-if="isInlineEdit"
    :item="item"
    :tax-status="taxStatus"
    :sales-channel-id="salesChannelId"
/>
{% endblock %}

{% block sw_order_line_items_grid_sales_channel_grid_columns_label_link %}
<div
    v-else-if="!isInlineEdit && isProductItem(item)"
>

    {% block sw_order_line_items_grid_column_payload_options %}
    <mt-link
```

#### Example 2
Source: `sw-order/component/sw-order-line-items-grid/sw-order-line-items-grid.html.twig`
```twig
<sw-order-product-select
    v-if="isInlineEdit"
    name="sw-field--item-label"
    :sales-channel-id="salesChannelId"
    :tax-status="taxStatus"
    :item="item"
/>
{% endblock %}

{% block sw_order_line_items_grid_grid_columns_label_link %}
<div
    v-else-if="!isInlineEdit && (isProductItem(item) || isContainerItem(item))"
    class="sw-order-line-items-grid__item-product"
>

```

## sw-order-promotion-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| error | — | |
| loading-change | — | |
| reload-entity-data | — | |
| save-and-reload | — | |
| save-and-recalculate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `emitEntityData` | |
| `emitLoadingChange` | |
| `saveAndReload` | |
| `saveAndRecalculate` | |
| `handleUnsavedOrderChangesResponse` | |
| `handleError` | |
| `deleteAutomaticPromotions` | |
| `toggleAutomaticPromotions` | |
| `applyAutomaticPromotions` | |
| `onSubmitCode` | |
| `handlePromotionResponse` | |
| `onRemoveExistingCode` | |
| `dismissPromotionUpdates` | |
| `getLineItemByPromotionCode` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `order` | |
| `isOrderLoading` | |
| `versionContext` | |
| `orderLineItemRepository` | |
| `hasLineItem` | |
| `currency` | |
| `manualPromotions` | |
| `automaticPromotions` | |
| `promotionCodeTags` | |
| `hasAutomaticPromotions` | |
| `changesetGenerator` | |
| `hasOrderUnsavedChanges` | |
| `promotionsRemoved` | |
| `promotionsAdded` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
        <sw-order-promotion-field
            class="sw-order-detail-general__promotions"
            @loading-change="updateLoading"
            @reload-entity-data="reloadEntityData"
            @save-and-reload="saveAndReload"
            @error="showError"
        />
    </mt-card>

    <sw-extension-component-section
        position-identifier="sw-order-detail-base-promotions__after"
    />
    {% endblock %}
</div>
{% endblock %}
```

## sw-order-promotion-tag-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currency | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| on-remove-code | — | |

### Methods

| Method | Description |
|--------|-------------|
| `performAddTag` | |
| `dismissTag` | |
| `setFocus` | |
| `getPromotionCodeDescription` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `taggedFieldListClasses` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-promotion-field/sw-order-promotion-field.html.twig`
```twig
<sw-order-promotion-tag-field
    v-model:value="promotionCodeTags"
    :disabled="!hasLineItem || isLoading || !acl.can('order.editor') || undefined"
    :currency="currency"
    :label="$t('sw-order.detailsTab.promotionsField.labelPromotions')"
    :placeholder="$t('sw-order.detailsTab.promotionsField.placeholderPromotions')"
    :error="promotionError"
    @on-remove-code="onRemoveExistingCode"
/>
{% endblock %}

{% block sw_order_promotion_field_switch %}
<h3 class="sw-order-promotion-field__apply_auto_promotions__title">
    {{ $t('sw-order.detailsTab.promotionsField.automaticPromotions.title') }}
</h3>
```

#### Example 2
Source: `sw-order/view/sw-order-create-details/sw-order-create-details.html.twig`
```twig
        <sw-order-promotion-tag-field
            v-model:value="promotionCodeTags"
            :disabled="!hasLineItem"
            :currency="currency"
            :label="$tc('sw-order.createBase.labelAddPromotion')"
            :placeholder="$tc('sw-order.createBase.placeholderAddPromotion')"
            :error="promotionError"
            @on-remove-code="onRemoveExistingCode"
        />
        {% endblock %}

        {% block sw_order_create_details_switch_disable_auto_promotion %}

        <mt-switch
            class="sw-order-create-details__disable-auto-promotion"
```

#### Example 3
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
    <sw-order-promotion-tag-field
        v-model:value="promotionCodeTags"
        :disabled="!hasLineItem"
        :currency="currency"
        :label="$tc('sw-order.createBase.labelAddPromotion')"
        :placeholder="$tc('sw-order.createBase.placeholderAddPromotion')"
        :error="promotionError"
        @on-remove-code="onRemoveExistingCode"
    />
    {% endblock %}
</div>
<sw-description-list
    grid="1fr 1fr"
    class="sw-order-create-summary__data"
>
```

## sw-order-save-changes-beforehand-modal

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| confirm | — | |
| cancel | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |
| `onCancel` | |

### Examples

#### Example 1
Source: `sw-order/page/sw-order-detail/sw-order-detail.html.twig`
```twig
<sw-order-save-changes-beforehand-modal
    v-if="askForSaveBeforehand"
    @cancel="onAskAndSaveEditsCancel"
    @confirm="onAskAndSaveEditsConfirm"
>
    {{ askForSaveBeforehand.reason }}
</sw-order-save-changes-beforehand-modal>
```

## sw-order-saveable-field

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | yes |  |
| type | `any` | `'text'` | yes |  |
| placeholder | `any` | `null` | no |  |
| editable | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| value-change | — | |
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClick` | |
| `onSaveButtonClicked` | |
| `onCancelButtonClicked` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `component` | |
| `valuePropName` | |
| `computedAttrs` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-create-general/sw-order-create-general.html.twig`
```twig
<sw-order-saveable-field
    v-tooltip="{
        showDelay: 300,
        message: shippingCostsDetail,
        disabled: taxStatus === 'tax-free'
    }"
    type="number"
    editable
    :value="cartDelivery.shippingCosts.totalPrice"
    @value-change="onShippingChargeEdited"
    @update:value="onShippingChargeUpdated"
>
    {{ currencyFilter(cartDelivery.shippingCosts.totalPrice, currency.isoCode, currency.totalRounding.decimals) }}
</sw-order-saveable-field>
```

#### Example 2
Source: `sw-order/view/sw-order-create-base/sw-order-create-base.html.twig`
```twig
<sw-order-saveable-field
    v-tooltip="{
        showDelay: 300,
        message: shippingCostsDetail,
        disabled: taxStatus === 'tax-free'
    }"
    type="number"
    editable
    :value="cartDelivery.shippingCosts.totalPrice"
    @value-change="onShippingChargeEdited"
    @update:value="onShippingChargeUpdated"
>
    {{ currencyFilter(cartDelivery.shippingCosts.totalPrice, currency.isoCode) }}
</sw-order-saveable-field>
```

#### Example 3
Source: `sw-order/view/sw-order-detail-general/sw-order-detail-general.html.twig`
```twig
<sw-order-saveable-field
    ref="editShippingCosts"
    v-tooltip="{
        showDelay: 300,
        message: shippingCostsDetail,
        disabled: taxStatus === 'tax-free'
    }"
    type="number"
    :editable="acl.can('order.editor')"
    :step="1"
    :min="0"
    :value="delivery.shippingCosts.totalPrice"
    @value-change="onShippingChargeEdited"
    @update:value="onShippingChargeUpdated"
>
```

## sw-order-select-document-type-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| value | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `documentTypeAvailable` | |
| `addHelpTextToOption` | |
| `onRadioFieldChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `creditItems` | |
| `documentRepository` | |
| `documentTypeRepository` | |
| `documentTypeCriteria` | |
| `documentCriteria` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-document-card/sw-order-document-card.html.twig`
```twig
<sw-order-select-document-type-modal
    v-if="showSelectDocumentTypeModal"
    v-model:value="currentDocumentType"
    :order="order"
    @modal-close="onCloseSelectDocumentTypeModal"
/>
{% endblock %}

{% block sw_order_document_card_grid_column_document_send_modal %}
<sw-order-send-document-modal
    v-if="showSendDocumentModal"
    :document="sendDocument"
    :order="order"
    @modal-close="onCloseSendDocumentModal"
    @document-sent="onDocumentSent"
```

## sw-order-send-document-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| document | `any` | — | yes |  |
| order | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| document-sent | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setEmailTemplateAccordingToDocumentType` | |
| `onMailTemplateChange` | |
| `onSendDocument` | |
| `loadTheLinksForA11y` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `truncateFilter` | |
| `mailTemplateRepository` | |
| `mailHeaderFooterRepository` | |
| `mailTemplateCriteria` | |
| `mailTemplateSendCriteria` | |
| `primaryActionDisabled` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-document-card/sw-order-document-card.html.twig`
```twig
<sw-order-send-document-modal
    v-if="showSendDocumentModal"
    :document="sendDocument"
    :order="order"
    @modal-close="onCloseSendDocumentModal"
    @document-sent="onDocumentSent"
/>
{% endblock %}

{% block sw_order_document_card_empty_state %}
<mt-empty-state
    v-if="documentsEmpty && !isDataLoading && !term"
    class="sw-order-document-card__empty-state"
    :icon="$route.meta.$module.icon"
    :headline="emptyStateTitle"
```

## sw-order-state-change-modal-attach-documents

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-confirm | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onConfirm` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-state-change-modal/sw-order-state-change-modal.html.twig`
```twig
    <sw-order-state-change-modal-attach-documents
        :order="order"
        :is-loading="isLoading"
        @on-confirm="onDocsConfirm"
    />
    {% endblock %}
</sw-modal>
{% endblock %}

```

## sw-order-state-change-modal

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| technicalName | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-leave | — | |
| page-leave-confirm | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onDocsConfirm` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-details-state-card/sw-order-details-state-card.html.twig`
```twig
        <sw-order-state-change-modal
            v-if="showStateChangeModal"
            :order="order"
            :is-loading="isLoading"
            :technical-name="''"
            @page-leave="onLeaveModalClose"
            @page-leave-confirm="onLeaveModalConfirm"
        />
        {% endblock %}
    </div>
    {% endblock %}

    {% block sw_order_state_change_card_divider %}
    <hr class="sw-order-detail-state-card__divider">
    {% endblock %}
```

#### Example 2
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
<sw-order-state-change-modal
    v-if="showModal"
    :order="order"
    :is-loading="isLoading"
    :technical-name="technicalName"
    @page-leave="onLeaveModalClose"
    @page-leave-confirm="onLeaveModalConfirm"
/>
{% endblock %}
{% block sw_order_state_history_card_container %}
<sw-container
    columns="repeat(auto-fit, minmax(250px, 1fr))"
    gap="30px 30px"
>
    {% block sw_order_state_history_card_transaction %}
```

#### Example 3
Source: `sw-order/component/sw-order-general-info/sw-order-general-info.html.twig`
```twig
<sw-order-state-change-modal
    v-if="showModal"
    :order="order"
    :is-loading="isLoading"
    :technical-name="''"
    @page-leave="onLeaveModalClose"
    @page-leave-confirm="onLeaveModalConfirm"
/>
{% endblock %}

{% block sw_order_detail_base_general_info_order_states %}
<div class="sw-order-general-info__order-states">
    {% block sw_order_detail_base_general_info_order_states_payment %}
    <div
        v-if="transaction"
```

#### Example 4
Source: `sw-order/component/sw-order-state-change-modal/sw-order-state-change-modal.html.twig`
```twig
    <sw-order-state-change-modal-attach-documents
        :order="order"
        :is-loading="isLoading"
        @on-confirm="onDocsConfirm"
    />
    {% endblock %}
</sw-modal>
{% endblock %}

```

## sw-order-state-history-card-entry

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| history | `any` | — | yes |  |
| transitionOptions | `any` | — | yes |  |
| stateMachineName | `any` | — | yes |  |
| title | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `userDisplayName` | |
| `integrationDisplayName` | |
| `getDisplayName` | |
| `getIconFromState` | |
| `getIconColorFromState` | |
| `getBackgroundColorFromState` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
<sw-order-state-history-card-entry
    v-if="transaction"
    v-tooltip="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('order.editor'),
        showOnDisabledElements: true
    }"
    class="sw-order-state-history-card__payment-state"
    :disabled="!acl.can('order.editor') || undefined"
    :history="transactionHistory"
    :transition-options="transactionOptions"
    state-machine-name="order_transaction.state"
    :title="$tc('sw-order.stateCard.headlineTransactionState')"
    @state-select="onTransactionStateSelected"
/>
```

#### Example 2
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
        <sw-order-state-history-card-entry
            v-tooltip="{
                message: $tc('sw-privileges.tooltip.warning'),
                disabled: acl.can('order.editor'),
                showOnDisabledElements: true
            }"
            class="sw-order-state-history-card__order-state"
            :history="orderHistory"
            :disabled="!acl.can('order.editor') || undefined"
            :transition-options="orderOptions"
            state-machine-name="order.state"
            :title="$tc('sw-order.stateCard.headlineOrderState')"
            @state-select="onOrderStateSelected"
        />
        {% endblock %}
```

## sw-order-state-history-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| order | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| options-change | — | |
| order-state-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadHistory` | |
| `getStateHistoryEntries` | |
| `fetchEntries` | |
| `buildStateHistory` | |
| `getTransitionOptions` | |
| `getAllStates` | |
| `stateMachineStateCriteria` | |
| `buildTransitionOptions` | |
| `onOrderStateSelected` | |
| `onCancelCreation` | |
| `onTransactionStateSelected` | |
| `onDeliveryStateSelected` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `createStateChangeErrorNotification` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `mailTemplateRepository` | |
| `stateMachineHistoryRepository` | |
| `transaction` | |
| `delivery` | |
| `stateMachineHistoryCriteria` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
<sw-order-state-history-card-entry
    v-if="transaction"
    v-tooltip="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('order.editor'),
        showOnDisabledElements: true
    }"
    class="sw-order-state-history-card__payment-state"
    :disabled="!acl.can('order.editor') || undefined"
    :history="transactionHistory"
    :transition-options="transactionOptions"
    state-machine-name="order_transaction.state"
    :title="$tc('sw-order.stateCard.headlineTransactionState')"
    @state-select="onTransactionStateSelected"
/>
```

#### Example 2
Source: `sw-order/component/sw-order-state-history-card/sw-order-state-history-card.html.twig`
```twig
        <sw-order-state-history-card-entry
            v-tooltip="{
                message: $tc('sw-privileges.tooltip.warning'),
                disabled: acl.can('order.editor'),
                showOnDisabledElements: true
            }"
            class="sw-order-state-history-card__order-state"
            :history="orderHistory"
            :disabled="!acl.can('order.editor') || undefined"
            :transition-options="orderOptions"
            state-machine-name="order.state"
            :title="$tc('sw-order.stateCard.headlineOrderState')"
            @state-select="onOrderStateSelected"
        />
        {% endblock %}
```

## sw-order-state-history-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| order | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadHistory` | |
| `getStateHistoryEntries` | |
| `buildStateHistory` | |
| `createEntry` | |
| `getVariantState` | |
| `onClose` | |
| `onPageChange` | |
| `enumerateTransaction` | |
| `getStateChangeAuthor` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineHistoryRepository` | |
| `stateMachineHistoryCriteria` | |
| `columns` | |
| `hasMultipleTransactions` | |
| `statesLoading` | |

### Examples

#### Example 1
Source: `sw-order/view/sw-order-detail-details/sw-order-detail-details.html.twig`
```twig
    <sw-order-state-history-modal
        v-if="showStateHistoryModal"
        :order="order"
        @modal-close="showStateHistoryModal = false"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-order-state-select-v2

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| transitionOptions | `any` | — | no |  |
| stateType | `any` | — | yes |  |
| roundedStyle | `any` | `false` | no |  |
| placeholder | `any` | `null` | no |  |
| label | `any` | `null` | no |  |
| backgroundStyle | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| state-select | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onStateChangeClicked` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectStyle` | |
| `selectPlaceholder` | |
| `selectable` | |

### Examples

#### Example 1
Source: `sw-order/component/sw-order-details-state-card/sw-order-details-state-card.html.twig`
```twig
<sw-order-state-select-v2
    v-tooltip="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('order.editor'),
        showOnDisabledElements: true
    }"
    :transition-options="stateOptions"
    :state-type="entityName"
    rounded-style
    :placeholder="entity.stateMachineState.translated.name"
    :label="stateLabel"
    :background-style="stateSelectBackgroundStyle"
    :disabled="disabled"
    :is-loading="statesLoading"
    @state-select="onStateSelected"
```

#### Example 2
Source: `sw-order/component/sw-order-create-general-info/sw-order-create-general-info.html.twig`
```twig
    <sw-order-state-select-v2
        class="sw-order-create-general-info__order-state-payment"
        state-type="order_transaction"
        rounded-style
        :placeholder="$tc('sw-order.stateCard.draftPlaceholder')"
        :label="$tc('sw-order.stateCard.headlineTransactionState')"
        disabled
    />
</div>
{% endblock %}

{% block sw_order_create_general_info_order_state_delivery %}
<div class="sw-order-create-general-info__order-state">
    <sw-order-state-select-v2
        class="sw-order-create-general-info__order-state-delivery"
```

#### Example 3
Source: `sw-order/component/sw-order-general-info/sw-order-general-info.html.twig`
```twig
    <sw-order-state-select-v2
        v-tooltip="{
            message: $tc('sw-privileges.tooltip.warning'),
            disabled: acl.can('order.editor'),
            showOnDisabledElements: true
        }"
        class="sw-order-general-info__order-state-payment"
        :transition-options="paymentStateOptions"
        state-type="order_transaction"
        rounded-style
        :placeholder="transaction.stateMachineState.translated.name"
        :label="$tc('sw-order.stateCard.headlineTransactionState')"
        :background-style="backgroundStyle('order_transaction')"
        :disabled="!acl.can('order.editor') || isLoading"
        @state-select="onStateSelected"
```

#### Example 4
Source: `sw-order/component/sw-order-general-info/sw-order-general-info.html.twig`
```twig
        <sw-order-state-select-v2
            v-tooltip="{
                message: $tc('sw-privileges.tooltip.warning'),
                disabled: acl.can('order.editor'),
                showOnDisabledElements: true
            }"
            class="sw-order-general-info__order-state-order"
            :transition-options="orderStateOptions"
            rounded-style
            state-type="order"
            :placeholder="order.stateMachineState.translated.name"
            :label="$tc('sw-order.stateCard.headlineOrderState')"
            :background-style="backgroundStyle('order')"
            :disabled="!acl.can('order.editor') || isLoading"
            @state-select="onStateSelected"
```

## sw-order-user-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentOrder | `any` | — | yes |  |
| versionContext | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| isEditing | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additional-actions | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| error | — | |
| order-change | — | |
| onEditDeliveryAddress | — | |
| order-reset | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `renderFormattingAddress` | |
| `reload` | |
| `countryCriteria` | |
| `onEditBillingAddress` | |
| `onEditDeliveryAddress` | |
| `onAddressModalSave` | |
| `onResetOrder` | |
| `onAddressModalAddressSelected` | |
| `onAddNewDeliveryAddress` | |
| `emitChange` | |
| `onAddTag` | |
| `onRemoveTag` | |
| `renderTrackingUrl` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `countryRepository` | |
| `orderAddressRepository` | |
| `OrderTagRepository` | |
| `billingAddress` | |
| `delivery` | |
| `orderDate` | |
| `hasDeliveries` | |
| `hasDeliveryTrackingCode` | |
| `hasDifferentBillingAndShippingAddress` | |
| `lastChangedDate` | |
| `hasTags` | |
| `fullName` | |
| `currencyFilter` | |

### Examples

#### Basic Usage
```twig
<sw-order-user-card
    currentOrder="..."
    versionContext="..."
    isLoading="..."
>
    <!-- content -->
</sw-order-user-card>
```

## sw-overlay

> Shopware Administration component.

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-detail/sw-cms-detail.html.twig`
```twig
<sw-overlay v-if="page.locked" />
```

## sw-page

> Base page layout component with smart bar, header, content area, and sidebar.

- [Slots](#slots)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| showSmartBar | `any` | `true` | no |  |
| showSearchBar | `any` | `true` | no |  |
| headerBorderColor | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| search-bar | — | |
| smart-bar-back | — | |
| smart-bar-header | — | |
| language-switch | — | |
| smart-bar-actions | — | |
| side-content | — | |
| content | — | |
| sidebar | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `updatedComponent` | |
| `beforeDestroyComponent` | |
| `readScreenWidth` | |
| `setSidebarOffset` | |
| `removeSidebarOffset` | |
| `setScrollbarOffset` | |
| `initPage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `routerBack` | |
| `pageColor` | |
| `hasSideContentSlot` | |
| `hasSidebarSlot` | |
| `showHeadArea` | |
| `pageClasses` | |
| `pageContainerClasses` | |
| `pageContentClasses` | |
| `pageOffset` | |
| `headerStyles` | |
| `topBarActionStyles` | |
| `smartBarContentStyle` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
<sw-page class="sw-settings-country-list">

    {% block sw_settings_country_list_search_bar %}
    <template #search-bar>
        <sw-search-bar
            initial-search-type="country"
            :placeholder="$tc('sw-settings-country.general.placeholderSearchBar')"
            :initial-search="term"
            @search="onSearch"
        />
    </template>
    {% endblock %}

    {% block sw_settings_country_list_smart_bar_header %}
    <template #smart-bar-header>
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-page class="sw-settings-country-detail">

    {% block sw_settings_country_detail_header %}
    <template #smart-bar-header>
        <h2>{{ placeholder(country, 'name', $tc('sw-settings-country.detail.textHeadline')) }}</h2>
    </template>
    {% endblock %}

    {% block sw_settings_country_detail_actions %}
    <template #smart-bar-actions>
        {% block sw_settings_country_detail_actions_abort %}
        <mt-button
            v-tooltip.bottom="{
                message: 'ESC',
                appearance: 'light'
```

#### Example 3
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
<sw-page class="sw-settings-logging-list">

    {% block sw_settings_logging_list_search_bar %}
    <template #search-bar>
        <sw-search-bar
            initial-search-type="Logs"
            :placeholder="$tc('sw-settings-logging.general.placeholderSearchBar')"
            :initial-search="term"
            @search="onSearch"
        />
    </template>
    {% endblock %}

    {% block sw_settings_logging_list_smart_bar_header %}
    <template #smart-bar-header>
```

#### Example 4
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-page class="sw-settings-search">
    {% block sw_settings_search_smart_bar_header %}
    <template #smart-bar-header>
        <h2>
            {% block sw_settings_search_smart_bar_header_title_text %}
            {{ $tc('sw-settings.index.title') }}
            <mt-icon
                name="regular-chevron-right-xs"
                size="12px"
            />
            {{ $tc('sw-settings-search.general.mainMenuItemGeneral') }}
            {% endblock %}
        </h2>
    </template>
    {% endblock %}
```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-page class="sw-settings-salutation-detail">

    {% block sw_settings_salutation_detail_search_bar %}
    <template #search-bar></template>
    {% endblock %}

    {% block sw_settings_salutation_detail_smart_bar_header %}
    <template #smart-bar-header>
        {% block sw_settings_salutation_detail_smart_bar_header_title %}
        <h2>
            {% block sw_settings_salutation_detail_smart_bar_header_title_text %}
            {{ placeholder(salutation, 'salutationKey', $tc('sw-settings-salutation.detail.placeholderNewSalutation')) }}
            {% endblock %}
        </h2>
        {% endblock %}
```

## sw-pagination

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| total | `any` | — | yes |  |
| limit | `any` | — | yes |  |
| page | `any` | — | yes |  |
| totalVisible | `any` | `7` | no |  |
| steps | `any` | — | no |  |
| autoHide | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `range` | |
| `pageChange` | |
| `onPageSizeChange` | |
| `firstPage` | |
| `prevPage` | |
| `nextPage` | |
| `lastPage` | |
| `changePageByPageNumber` | |
| `refresh` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `maxPage` | |
| `displayedPages` | |
| `shouldBeVisible` | |
| `possibleSteps` | |
| `possibleStepsOptions` | |

### Examples

#### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
        <sw-pagination
            :page="page"
            :limit="limit"
            :total="total"
            :total-visible="7"
            @page-change="onPageChange"
        />
        {% endblock %}
    </template>

    <template
        #actions="{ item }"
    >
        {% block sw_settings_logging_list_content_listing_actions %}
        <sw-context-menu-item @click="showInfoModal(item)">
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
                        <sw-pagination
                            :page="page"
                            :limit="limit"
                            :total="total"
                            :total-visible="7"
                            @page-change="onPagePagination"
                        />
                        {% endblock %}
                    </template>
                </sw-data-grid>
                {% block sw_search_excliuded_terms_no_results %}
                <div v-if="items.length === 0">
                    <p class="sw-settings-search__no-data-results">
                        {{ $tc('sw-settings-search.generalTab.labelExcludedSearchTermsNoResults') }}
                    </p>
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
            <sw-pagination
                :page="page"
                :limit="limit"
                :total="total"
                auto-hide
            />
        </template>
        {% endblock %}
    </sw-entity-listing>
    {% endblock %}
</div>
{% endblock %}

```

#### Example 4
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
                    <sw-pagination
                        :total="total"
                        :limit="limit"
                        :page="page"
                        @page-change="changePage"
                    />
                </template>
            </div>
        </template>
    </div>
</div>

```

#### Example 5
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
            <sw-pagination
                v-if="customFieldTotal > customFieldCriteria.limit"
                :total="customFieldTotal"
                :limit="customFieldCriteria.limit"
                :page="customFieldCriteria.page"
                :auto-hide="false"
                @page-change="paginateCustomFieldGrid"
            />
        </template>
        {% endblock %}

    </sw-data-grid>

</template>
{% endblock %}
```

## sw-password-field-deprecated

> **Deprecated in 6.7** — Use `mt-password-field` instead. Will be removed in 6.8.
> See mt-password-field for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-password-field>` | `<mt-password-field>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| passwordToggleAble | `any` | `true` | no |  |
| placeholderIsPassword | `any` | `false` | no |  |
| autocomplete | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-restore | — | |
| inheritance-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onTogglePasswordVisibility` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `typeFieldClass` | |
| `passwordPlaceholder` | |

### Examples

#### Basic Usage
```twig
<sw-password-field-deprecated>
    <!-- content -->
</sw-password-field-deprecated>
```

## sw-password-field

> **Migration wrapper** — Delegates to `mt-password-field` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-password-field for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
| placeholder | `any` | `''` | no |  |
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
<sw-password-field>
    <!-- content -->
</sw-password-field>
```

## sw-payment-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| paymentMethod | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| set-payment-active | — | |

### Methods

| Method | Description |
|--------|-------------|
| `setPaymentMethodActive` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `previewUrl` | |

### Examples

#### Example 1
Source: `sw-settings-payment/page/sw-settings-payment-overview/sw-settings-payment-overview.html.twig`
```twig
            <sw-payment-card
                :key="`default-${card.id}`"
                :payment-method="card.paymentMethod"
                @set-payment-active="togglePaymentMethodActive"
            />
            {% endblock %}
        </template>

    </template>
    {% endblock %}

    {% block sw_settings_payment_overview_empty_state %}
    <mt-empty-state
        v-if="isEmpty"
        :icon="$route.meta.$module.icon"
```

## sw-plugin-box

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| pluginId | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `checkPluginConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pluginRepository` | |

### Examples

#### Example 1
Source: `sw-settings-payment/page/sw-settings-payment-detail/sw-settings-payment-detail.html.twig`
```twig
<sw-plugin-box
    v-if="!!paymentMethod.pluginId"
    :plugin-id="paymentMethod.pluginId"
/>
{% endblock %}

<sw-container
    columns="3fr 3fr 1fr"
    gap="0px 30px"
>
    {% block sw_settings_payment_detail_content_field_name %}

    <mt-text-field
        v-model="paymentMethod.name"
        name="sw-field--paymentMethod-name"
```

## sw-plugin-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| plugin | `any` | — | yes |  |
| showDescription | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onInstall` | |
| `setupPlugin` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `pluginIsNotActive` | |
| `truncateFilter` | |

### Examples

#### Example 1
Source: `sw-first-run-wizard/view/sw-first-run-wizard-plugins/sw-first-run-wizard-plugins.html.twig`
```twig
    <sw-plugin-card
        v-for="plugin in categoryLead"
        :key="plugin.name"
        :plugin="plugin"
        @on-plugin-installed="reloadRecommendations"
        @extension-activated="$emit('extension-activated', $event)"
    />
</div>

<hr
    v-if="showSpacer"
    class="spacer"
>

<h3
```

#### Example 2
Source: `sw-first-run-wizard/view/sw-first-run-wizard-plugins/sw-first-run-wizard-plugins.html.twig`
```twig
            <sw-plugin-card
                v-for="plugin in notCategoryLead"
                :key="plugin.name"
                :plugin="plugin"
                :show-description="false"
                @on-plugin-installed="reloadRecommendations"
                @extension-activated="$emit('extension-activated', $event)"
            />
        </sw-container>
    </div>

</div>
{% endblock %}

```

## sw-popover-deprecated

> **Deprecated in 6.7** — Will be removed in 6.8.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| zIndex | `null \| null` | `null` | no |  |
| resizeWidth | `any` | `false` | no |  |
| popoverClass | `null \| null \| null` | `''` | no |  |
| popoverConfigExtension | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `componentStyle` | |
| `popoverConfig` | |

### Examples

#### Basic Usage
```twig
<sw-popover-deprecated>
    <!-- content -->
</sw-popover-deprecated>
```

## sw-popover

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isOpened | `any` | `true` | no |  |
| resizeWidth | `any` | `false` | no |  |

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
| `computedMatchReferenceWidth` | |

### Examples

#### Basic Usage
```twig
<sw-popover>
    <!-- content -->
</sw-popover>
```

## sw-price-field

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| allowModal | `any` | `false` | no |  |
| defaultPrice | `any` | — | no |  |
| hideListPrices | `any` | `false` | no |  |
| taxRate | `any` | — | no |  |
| currency | `any` | — | yes |  |
| validation | `any` | `null` | no |  |
| label | `any` | `true` | no |  |
| compact | `any` | `false` | no |  |
| error | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| disableSuffix | `any` | `false` | no |  |
| grossLabel | `any` | `null` | no |  |
| netLabel | `any` | `null` | no |  |
| name | `any` | `null` | no |  |
| allowEmpty | `any` | `false` | no |  |
| inherited | `any` | — | no |  |
| grossHelpText | `any` | `null` | no |  |
| netHelpText | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | — | |
| price-lock-change | — | |
| price-calculate | — | |
| price-gross-change | — | |
| price-net-change | — | |
| calculating | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onLockSwitch` | |
| `onEndsWithDecimalSeparator` | |
| `onPriceGrossInputChange` | |
| `onPriceNetInputChange` | |
| `onPriceGrossChange` | |
| `onPriceNetChange` | |
| `convertNetToGross` | |
| `convertGrossToNet` | |
| `requestTaxValue` | |
| `convertPrice` | |
| `keymonitor` | |
| `onCloseModal` | |
| `onPriceGrossChangeDebounce` | |
| `onPriceNetChangeDebounce` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `calculatePriceApiService` | |
| `priceForCurrency` | |
| `attributesWithoutListeners` | |
| `isInherited` | |
| `isDisabled` | |
| `labelGross` | |
| `labelNet` | |
| `grossError` | |
| `netError` | |
| `grossFieldName` | |
| `netFieldName` | |

### Examples

#### Example 1
Source: `sw-custom-entity/component/sw-custom-entity-input-field/sw-custom-entity-input-field.html.twig`
```twig
    <!--<sw-price-field
        v-else-if="type === 'json_object'"
        class="sw-custom-entity-input-field__price"
        :value="currentValue"
        :label="label"
        :placeholder="placeholder"
        :help-text="helpText"
        @change="onChange"
    />-->

    <!-- ToDo NEXT-22874 - Remove after Debug -->

    <mt-text-field
        v-else
        class="sw-custom-entity-input-field__undefined"
```

#### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
        <sw-price-field
            :value="item.price ? item.price : []"
            :default-price="productEntity.price[0]"
            :tax-rate="productEntity.tax"
            :label="false"
            :compact="true"
            :disable-suffix="true"
            enable-inheritance
            :currency="currency"
        />
    </template>

    <template v-else>
        <sw-inheritance-switch
            :is-inherited="item.price === null"
```

#### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-price-field
        :value="item.price ? item.price : []"
        :default-price="getDefaultPriceForVariant(item, currency)"
        :tax-rate="productTaxRate"
        :label="false"
        :compact="compact"
        enable-inheritance
        :currency="currency"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_product_variants_overview_data_grid_column_price_preview %}
<template v-else>
```

#### Example 4
Source: `sw-product/view/sw-product-detail-context-prices/sw-product-detail-context-prices.html.twig`
```twig
        <sw-price-field
            :value="item.price"
            :default-price="findDefaultPriceOfRule(item)"
            :tax-rate="productTaxRate"
            :label="false"
            :compact="compact"
            :name="`${item.ruleId}-${currency.isoCode}-${item.quantityStart}`"
            :currency="currency"
            :disabled="!acl.can('product.editor')"
        />
    {% endblock %}
    </div>
</template>

<template v-if="showListPrices[priceGroup.ruleId] !== false">
```

## sw-price-preview

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
    <sw-price-preview
        :value="item.price ? item.price : []"
        :default-price="productEntity.price[0]"
        :tax-rate="productEntity.tax"
        :currency="currency"
    />
</template>
{% endblock %}

{% block sw_product_variant_modal_bulk_edit_modal_column_stock %}
<template #column-stock="{ item }">
    {{ item.stock }}
    <sw-color-badge :variant="stockColorVariantFilter(item.stock)" />
</template>
{% endblock %}
```

#### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
        <sw-price-preview
            :value="item.price ? item.price : []"
            :default-price="productEntity.price[0]"
            :tax-rate="productEntity.tax"
            :currency="currency"
        />
    </template>
</template>
{% endblock %}

{% block sw_product_variant_modal_body_grid_column_stock %}
<template #column-stock="{item, isInlineEdit}">

    {% block sw_product_variant_modal_body_grid_column_stock_inline_edit %}
    <mt-number-field
```

#### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
        <sw-price-preview
            :key="`else-price-field-${currency.isoCode}`"
            :value="item.price ? item.price : []"
            :default-price="getDefaultPriceForVariant(item, currency)"
            :tax-rate="productTaxRate"
            :currency="currency"
        />
        {% endblock %}
    </template>
    {% endblock %}

</template>
{% endblock %}

{% block sw_product_variants_overview_data_grid_column_stock %}
```

#### Example 4
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-price-preview
        :key="`else-price-field-${currency.isoCode}`"
        :value="item.price ? item.price : []"
        :default-price="getDefaultPriceForVariant(item, currency)"
        :tax-rate="productTaxRate"
        :currency="currency"
    />
</template>
{% endblock %}

{% block sw_product_variants_overview_bulk_edit_modal_column_media %}
<template #column-media="{ item }">
    <sw-inheritance-switch
        class="sw-product-variants-overview_media__inherited-icon"
        :is-inherited="isMediaFieldInherited(item)"
```

## sw-price-rule-modal

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |

### Examples

#### Example 1
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrix/sw-settings-shipping-price-matrix.html.twig`
```twig
            <sw-price-rule-modal
                v-if="showRuleModal"
                rule-aware-group-key="shippingMethodPriceCalculations"
                @save="onSaveRule"
                @modal-close="onCloseRuleModal"
            />
        </template>
    </sw-select-rule-create>
</template>
{% endblock %}
{% block sw_settings_shipping_price_matrix_price_grid_column_quantity_start %}
<template
    #column-quantityStart="{ item, itemIndex, compact }"
>
    <mt-number-field
```

#### Example 2
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrix/sw-settings-shipping-price-matrix.html.twig`
```twig
                    <sw-price-rule-modal
                        v-if="showRuleModal"
                        rule-aware-group-key="shippingMethodPriceCalculations"
                        @save="onSaveRule"
                        @modal-close="onCloseRuleModal"
                    />
                </template>
            </sw-select-rule-create>
            {% endblock %}
        </sw-container>
    </div>
    {% endblock %}
</template>

{% block sw_settings_shipping_price_matrix_delete_modal %}
```

## sw-privilege-error

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `routerGoBack` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-privilege-error>
    <!-- content -->
</sw-privilege-error>
```

## sw-product-add-properties-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| newProperties | `any` | — | yes |  |
| propertiesAvailable | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| toolbar | — | |
| toolbar-search-field | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-cancel | — | |
| modal-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCancel` | |
| `onSave` | |
| `onOpenProperties` | |
| `onSelectOption` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showSaveButton` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-properties/sw-product-properties.html.twig`
```twig
        <sw-product-add-properties-modal
            v-if="showAddPropertiesModal"
            :new-properties="newProperties"
            :properties-available="propertiesAvailable"
            @modal-cancel="onCancelAddPropertiesModal"
            @modal-save="onSaveAddPropertiesModal($event, updateCurrentValue)"
        />
        {% endblock %}
    </template>
</sw-inherit-wrapper>
{% endblock %}

```

#### Example 2
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
    <sw-product-add-properties-modal
        v-if="showAddPropertiesModal"
        :new-properties="newProperties"
        @modal-cancel="onCancelAddPropertiesModal"
        @modal-save="onSaveAddPropertiesModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-product-basic-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |
| showSettingsInformation | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateIsTitleRequired` | |
| `getInheritValue` | |
| `loadProductNumberRangeId` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `productNameError` | |
| `productDescriptionError` | |
| `productProductNumberError` | |
| `productManufacturerIdError` | |
| `productActiveError` | |
| `productMarkAsTopsellerError` | |
| `numberRangeRepository` | |
| `isTitleRequired` | |
| `productNumberRangeLink` | |
| `productNumberHelpText` | |
| `highlightHelpText` | |
| `numberRangeCriteria` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
    <sw-product-basic-form
        :show-settings-information="showModeSetting"
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}

</mt-card>
{% endblock %}

<mt-card
    v-if="isDownloadCardVisible"
    class="sw-product-detail-base__downloads"
    :subtitle="$tc('sw-product.detailBase.cardSubtitleDownloads')"
    :is-loading="loading.product || loading.customFieldSets || loading.downloads"
    position-identifier="sw-product-detail-base-downloads"
```

## sw-product-category-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `displayAdvancedVisibility` | |
| `closeAdvancedVisibility` | |
| `visibilitiesRemoveInheritanceFunction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `loading` | |
| `isChild` | |
| `showModeSetting` | |
| `productTagsError` | |
| `productActiveError` | |
| `hasSelectedVisibilities` | |
| `productVisibilityRepository` | |
| `salesChannelRepository` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-category-form :allow-edit="acl.can('product.editor')" />
```

## sw-product-clone-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| clone-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `duplicate` | |
| `cloneParent` | |
| `verifyVariants` | |
| `getChildrenIds` | |
| `duplicateVariant` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `progressInPercentage` | |
| `repository` | |

### Examples

#### Example 1
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
    <sw-product-clone-modal
        v-if="cloning"
        :product="product"
        @clone-finish="onDuplicateFinish"
    />
    {% endblock %}

    {% block sw_product_list_content_variant_modal %}
    <sw-product-variant-modal
        v-if="showVariantModal"
        :product-entity="productEntityVariantModal"
        @modal-close="closeVariantModal"
    />
    {% endblock %}
</template>
```

#### Example 2
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
            <sw-product-clone-modal
                v-if="cloning"
                :product="product"
                @clone-finish="onDuplicateFinish"
            />
            {% endblock %}

            {% block sw_product_settings_mode %}
            <sw-product-settings-mode
                v-if="showAdvanceModeSetting"
                :is-loading="isLoading"
                :mode-settings="advancedModeSetting"
                @settings-item-change="onChangeSettingItem"
                @settings-change="onChangeSetting"
            />
```

## sw-product-cross-selling-assignment

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| assignedProducts | `any` | — | yes |  |
| crossSellingId | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onToggleProduct` | |
| `removeItem` | |
| `isSelected` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `isLoading` | |
| `isLoadingGrid` | |
| `assignmentRepository` | |
| `productRepository` | |
| `searchCriteria` | |
| `searchContext` | |
| `total` | |
| `assignedProductColumns` | |
| `variantProductIds` | |
| `variantCriteria` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-cross-selling-form/sw-product-cross-selling-form.html.twig`
```twig
        <sw-product-cross-selling-assignment
            v-else
            :assigned-products="crossSelling.assignedProducts"
            :cross-selling-id="crossSelling.id"
            :searchable-fields="['name', 'productNumber']"
            :allow-edit="allowEdit"
        />
        {% endblock %}

        {% block sw_product_detail_cross_selling_modal_preview_modal %}
        <sw-product-stream-modal-preview
            v-if="showModalPreview"
            ref="modalPreview"
            :filters="productStreamFilterTree"
            @modal-close="closeModalPreview"
```

## sw-product-cross-selling-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| crossSelling | `any` | — | yes |  |
| allowEdit | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onShowDeleteModal` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `openModalPreview` | |
| `closeModalPreview` | |
| `loadStreamPreview` | |
| `getProductStreamFilter` | |
| `updateProductStreamFilterTree` | |
| `onSortingChanged` | |
| `onTypeChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `crossSellingNameError` | |
| `crossSellingTypeError` | |
| `crossSellingPositionError` | |
| `product` | |
| `isLoading` | |
| `productCrossSellingRepository` | |
| `productStreamRepository` | |
| `productStreamFilterRepository` | |
| `productStreamFilterCriteria` | |
| `crossSellingAssigmentRepository` | |
| `crossSellingTitle` | |
| `sortingTypes` | |
| `crossSellingTypes` | |
| `previewDisabled` | |
| `sortingConCat` | |
| `disablePositioning` | |
| `associationValue` | |
| `crossSellingTypeOptions` | |
| `sortingTypeOptions` | |
| `productStreamCriteria` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-cross-selling/sw-product-detail-cross-selling.html.twig`
```twig
        <sw-product-cross-selling-form
            v-for="item in product.crossSellings"
            :key="item.id"
            :cross-selling="item"
            :allow-edit="acl.can('product.editor')"
        />
    </ul>
    {% endblock %}

    {% block sw_product_detail_cross_selling_add %}
    <mt-button
        v-tooltip="{
            message: onAddCrossSellingTooltipMessage,
            disabled: acl.can('product.editor') && isSystemDefaultLanguage,
            showOnDisabledElements: true
```

## sw-product-deliverability-downloadable-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSwitchInput` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `showModeSetting` | |
| `showStockSetting` | |
| `productStockError` | |
| `productDeliveryTimeIdError` | |
| `productIsCloseoutError` | |
| `productMaxPurchaseError` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-deliverability-downloadable-form :disabled="!acl.can('product.editor')" />
```

## sw-product-deliverability-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `loading` | |
| `showModeSetting` | |
| `productStockError` | |
| `productDeliveryTimeIdError` | |
| `productIsCloseoutError` | |
| `productMaxPurchaseError` | |
| `productPurchaseStepsError` | |
| `productMinPurchaseError` | |
| `productShippingFreeError` | |
| `productRestockTimeError` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-deliverability-form :allow-edit="acl.can('product.editor')" />
```

## sw-product-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `showProductCard` | |
| `getMediaDefaultFolderId` | |
| `mediaRemoveInheritanceFunction` | |
| `mediaRestoreInheritanceFunction` | |
| `onOpenMediaModal` | |
| `onCloseMediaModal` | |
| `onOpenDownloadMediaModal` | |
| `onCloseDownloadMediaModal` | |
| `onAddMedia` | |
| `addMedia` | |
| `isSpatial` | |
| `isExistingMedia` | |
| `setMediaAsCover` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `customFieldSets` | |
| `loading` | |
| `isLoading` | |
| `showModeSetting` | |
| `productStates` | |
| `productType` | |
| `isDownloadCardVisible` | |
| `mediaFormVisible` | |
| `productMediaRepository` | |
| `mediaDefaultFolderRepository` | |
| `mediaDefaultFolderCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-product-detail-base>
    <!-- content -->
</sw-product-detail-base>
```

## sw-product-detail-context-prices

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isSetDefaultPrice | `any` | `false` | no |  |
| canSetLoadingRules | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `sortCurrencies` | |
| `onRuleChange` | |
| `onAddNewPriceGroup` | |
| `onPriceGroupDelete` | |
| `onPriceGroupDuplicate` | |
| `onPriceRuleDelete` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `isPriceFieldInherited` | |
| `convertPrice` | |
| `findRuleById` | |
| `findPricesByRuleId` | |
| `findDefaultPriceOfRule` | |
| `onQuantityEndChange` | |
| `createPriceRule` | |
| `canCreatePriceRule` | |
| `duplicatePriceRule` | |
| `getPriceRuleGroupClass` | |
| `restoreInheritance` | |
| `removeInheritance` | |
| `onChangeShowListPrices` | |
| `getStartQuantityTooltip` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `taxes` | |
| `currencies` | |
| `isLoading` | |
| `defaultCurrency` | |
| `defaultPrice` | |
| `productTaxRate` | |
| `isChild` | |
| `priceRepository` | |
| `ruleRepository` | |
| `priceRuleGroups` | |
| `priceRuleGroupsExists` | |
| `canAddPriceRule` | |
| `emptyPriceRuleExists` | |
| `isLoaded` | |
| `currencyColumns` | |
| `pricesColumns` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <sw-product-detail-context-prices
            :is-set-default-price="true"
            :can-set-loading-rules="false"
        />

        {% block sw_bulk_edit_product_content_advanced_prices_modal_footer %}
        <template #modal-footer>
            <slot name="sw-bulk-edit-modal-cancel">
                <mt-button
                    size="small"
                    variant="secondary"
                    @click="displayAdvancePricesModal = false"
                >
                    {{ $tc('global.default.close') }}
                </mt-button>
```

## sw-product-detail-cross-selling

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `loadAssignedProducts` | |
| `onAddCrossSelling` | |
| `restoreInheritance` | |
| `removeInheritance` | |
| `onShowRestoreInheritanceModal` | |
| `onCloseRestoreInheritanceModal` | |
| `onConfirmRestoreInheritance` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `isChild` | |
| `isLoading` | |
| `isSystemDefaultLanguage` | |
| `showCrossSellingCard` | |
| `onAddCrossSellingTooltipMessage` | |
| `assetFilter` | |
| `crossSellingRepository` | |

### Examples

#### Basic Usage
```twig
<sw-product-detail-cross-selling>
    <!-- content -->
</sw-product-detail-cross-selling>
```

## sw-product-detail-layout

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onOpenLayoutModal` | |
| `onCloseLayoutModal` | |
| `onOpenInPageBuilder` | |
| `onSelectLayout` | |
| `handleGetCmsPage` | |
| `updateCmsPageDataMapping` | |
| `onResetLayout` | |
| `elementUpdate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `cmsPageRepository` | |
| `cmsPageId` | |
| `showCmsForm` | |
| `product` | |
| `isLoading` | |
| `cmsPageCriteria` | |
| `languageId` | |
| `currentPage` | |
| `cmsPageState` | |

### Examples

#### Basic Usage
```twig
<sw-product-detail-layout>
    <!-- content -->
</sw-product-detail-layout>
```

## sw-product-detail-reviews

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getReviews` | |
| `onStartReviewDelete` | |
| `onCancelReviewDelete` | |
| `onShowReviewDeleteModal` | |
| `onCloseReviewDeleteModal` | |
| `onConfirmReviewDelete` | |
| `onChangePage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `isLoading` | |
| `cardTitle` | |
| `reviewRepository` | |
| `reviewCriteria` | |
| `reviewColumns` | |
| `assetFilter` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-product-detail-reviews>
    <!-- content -->
</sw-product-detail-reviews>
```

## sw-product-detail-seo

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onAddMainCategory` | |
| `onRemoveMainCategory` | |
| `onChangeSalesChannel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `categories` | |
| `mainCategoryRepository` | |
| `parentMainCategory` | |
| `productMainCategory` | |

### Examples

#### Basic Usage
```twig
<sw-product-detail-seo>
    <!-- content -->
</sw-product-detail-seo>
```

## sw-product-detail-specifications

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `showProductCard` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `loading` | |
| `isLoading` | |
| `customFieldSets` | |
| `showModeSetting` | |
| `productStates` | |
| `productType` | |
| `isDigitalProduct` | |
| `customFieldsExists` | |
| `showCustomFieldsCard` | |

### Examples

#### Basic Usage
```twig
<sw-product-detail-specifications>
    <!-- content -->
</sw-product-detail-specifications>
```

## sw-product-detail-variants

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `setActiveTab` | |
| `loadData` | |
| `loadConfigSettingGroups` | |
| `loadOptions` | |
| `loadGroups` | |
| `updateVariations` | |
| `updateVariantListHasContent` | |
| `openModal` | |
| `onConfigurationClosed` | |
| `checkIfPropertiesExists` | |
| `openAddPropertiesModal` | |
| `closeAddPropertiesModal` | |
| `updateNewProperties` | |
| `onCancelAddPropertiesModal` | |
| `onSaveAddPropertiesModal` | |
| `loadAllPropertyGroups` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `variants` | |
| `isStoreLoading` | |
| `contextLanguageId` | |
| `productRepository` | |
| `groupRepository` | |
| `propertyRepository` | |
| `productProperties` | |
| `currentProductStates` | |
| `currentProductType` | |
| `assetFilter` | |
| `groupCriteria` | |
| `configSettingGroups` | |

### Examples

#### Basic Usage
```twig
<sw-product-detail-variants>
    <!-- content -->
</sw-product-detail-variants>
```

## sw-product-detail

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productId | `any` | `null` | no |  |
| creationStates | `any` | `null` | no |  |
| creationType | `any` | `'physical'` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initState` | |
| `initAdvancedModeSettings` | |
| `createUserModeSetting` | |
| `getAdvancedModeDefaultSetting` | |
| `getAdvancedModeSetting` | |
| `saveAdvancedMode` | |
| `onChangeSetting` | |
| `changeModeSettings` | |
| `onChangeSettingItem` | |
| `loadState` | |
| `loadAll` | |
| `createState` | |
| `adjustProductAccordingToType` | |
| `loadProduct` | |
| `getDefaultPurchasePrices` | |
| `loadParentProduct` | |
| `loadCurrencies` | |
| `loadTaxes` | |
| `getDefaultTaxRate` | |
| `loadAttributeSet` | |
| `loadDefaultFeatureSet` | |
| `getDefaultSalesChannels` | |
| `fetchSalesChannelByIds` | |
| `createProductVisibilityEntity` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `saveFinish` | |
| `onSave` | |
| `customValidate` | |
| `validateProductPrices` | |
| `validatePrices` | |
| `onSaveFinished` | |
| `onCancel` | |
| `saveProduct` | |
| `removeMediaItem` | |
| `onCoverChange` | |
| `getInheritTitle` | |
| `onDuplicate` | |
| `onDuplicateFinish` | |
| `validateProductPurchase` | |
| `getCmsPageOverrides` | |
| `deleteSpecifcKeys` | |
| `loadLanguage` | |
| `initProductMeasurementUnits` | |
| `getPreferredMeasurementUnits` | |
| `savePreferenceUnits` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `localMode` | |
| `advancedModeSetting` | |
| `modeSettings` | |
| `isLoading` | |
| `isChild` | |
| `defaultCurrency` | |
| `getDefaultFeatureSet` | |
| `showModeSetting` | |
| `advanceModeEnabled` | |
| `productStates` | |
| `productType` | |
| `swProductDetailBaseError` | |
| `swProductDetailCrossSellingError` | |
| `identifier` | |
| `productTitle` | |
| `productRepository` | |
| `propertyRepository` | |
| `syncRepository` | |
| `currencyRepository` | |
| `taxRepository` | |
| `customFieldSetRepository` | |
| `salesChannelRepository` | |
| `productVisibilityRepository` | |
| `mediaRepository` | |
| `featureSetRepository` | |
| `currentUser` | |
| `userModeSettingsRepository` | |
| `userModeSettingsCriteria` | |
| `productCriteria` | |
| `customFieldSetCriteria` | |
| `defaultFeatureSetCriteria` | |
| `taxCriteria` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `getModeSettingGeneralTab` | |
| `getModeSettingSpecificationsTab` | |
| `showAdvanceModeSetting` | |
| `cmsPageState` | |
| `currentPage` | |
| `languageRepository` | |
| `language` | |
| `translateFields` | |
| `ignoreFieldsValidation` | |
| `productApiContext` | |
| `lengthUnit` | |
| `weightUnit` | |
| `measurementUnitsChanged` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
        <sw-product-detail-context-prices
            :is-set-default-price="true"
            :can-set-loading-rules="false"
        />

        {% block sw_bulk_edit_product_content_advanced_prices_modal_footer %}
        <template #modal-footer>
            <slot name="sw-bulk-edit-modal-cancel">
                <mt-button
                    size="small"
                    variant="secondary"
                    @click="displayAdvancePricesModal = false"
                >
                    {{ $tc('global.default.close') }}
                </mt-button>
```

## sw-product-download-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| isInherited | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-open | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onOpenMedia` | |
| `getFileSize` | |
| `getFileName` | |
| `createdAt` | |
| `onRemoveDownload` | |
| `successfulUpload` | |
| `createDownloadAssociation` | |
| `onUploadFailed` | |
| `removeFile` | |
| `updateMediaItemPositions` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `isStoreLoading` | |
| `isLoading` | |
| `productDownloadRepository` | |
| `productDownloads` | |
| `mediaRepository` | |
| `error` | |
| `hasError` | |
| `swFieldClasses` | |
| `fileAccept` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
    <sw-product-download-form
        v-if="mediaFormVisible"
        :product-id="product.id"
        :label="$tc('sw-product.detailBase.downloadsLabel')"
        :disabled="!acl.can('product.editor')"
        required
        @media-open="onOpenDownloadMediaModal"
    />
</mt-card>

{% block sw_product_detail_base_price_card %}
<mt-card
    v-show="showProductCard('prices')"
    class="sw-product-detail-base__prices"
    position-identifier="sw-product-detail-base-prices"
```

## sw-product-feature-set-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `isLoading` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
<sw-product-feature-set-form :allow-edit="acl.can('product.editor')" />
```

## sw-product-image

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mediaId | `any` | — | yes |  |
| isSpatial | `any` | `false` | no |  |
| isArReady | `any` | `false` | no |  |
| isCover | `any` | `false` | no |  |
| isPlaceholder | `any` | `false` | no |  |
| showCoverLabel | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-product-image-cover | — | |
| sw-product-image-delete | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productImageClasses` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-media-form/sw-product-media-form.html.twig`
```twig
            <sw-product-image
                v-for="mediaItem in mediaItems"
                :key="mediaItem.id"
                v-draggable="{ dragGroup: 'product-media', data: mediaItem, onDragEnter: onMediaItemDragSort }"
                v-droppable="{ dragGroup: 'product-media', data: mediaItem }"
                :is-cover="isCover(mediaItem)"
                :is-spatial="isSpatial(mediaItem)"
                :is-ar-ready="isArReady(mediaItem)"
                :is-placeholder="mediaItem.isPlaceholder"
                :media-id="mediaItem.mediaId"
                :show-cover-label="showCoverLabel"
                @sw-product-image-delete="removeFile(mediaItem)"
                @sw-product-image-cover="markMediaAsCover(mediaItem)"
            />
            {% endblock %}
```

## sw-product-layout-assignment

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| cmsPage | `any` | `null` | no |  |
| product | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-layout-open | — | |
| button-edit-click | — | |
| button-delete-click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `openLayoutModal` | |
| `openInPageBuilder` | |
| `onLayoutReset` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-layout/sw-product-detail-layout.html.twig`
```twig
    <sw-product-layout-assignment
        :cms-page="currentPage"
        :product="product"
        @modal-layout-open="onOpenLayoutModal"
        @button-edit-click="onOpenInPageBuilder"
        @button-delete-click="onResetLayout"
    />
    {% endblock %}

    {% block sw_product_detail_layout_modal %}
    <sw-cms-layout-modal
        v-if="showLayoutModal"
        :headline="$tc('sw-product.layoutAssignment.subtitle')"
        :pre-selection="currentPage"
        :cms-page-types="['product_detail']"
```

## sw-product-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `updateTotal` | |
| `onChangeLanguage` | |
| `updateCriteria` | |
| `getCurrencyPriceByCurrencyId` | |
| `getProductColumns` | |
| `onDuplicate` | |
| `onDuplicateFinish` | |
| `onColumnSort` | |
| `productHasVariants` | |
| `productIsDigital` | |
| `openVariantModal` | |
| `closeVariantModal` | |
| `onBulkEditItems` | |
| `onBulkEditModalOpen` | |
| `onBulkEditModalClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productColumns` | |
| `currencyRepository` | |
| `currenciesColumns` | |
| `productCriteria` | |
| `currencyCriteria` | |
| `salesChannelCriteria` | |
| `showVariantModal` | |
| `listFilterOptions` | |
| `listFilters` | |
| `productBulkEditColumns` | |
| `assetFilter` | |
| `currencyFilter` | |
| `dateFilter` | |
| `stockColorVariantFilter` | |

### Examples

#### Basic Usage
```twig
<sw-product-list>
    <!-- content -->
</sw-product-list>
```

## sw-product-measurement-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `onUpdateLengthUnit` | |
| `convertWidth` | |
| `convertHeight` | |
| `convertLength` | |
| `onUpdateWeightUnit` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `lengthUnit` | |
| `weightUnit` | |
| `productWidthError` | |
| `productHeightError` | |
| `productLengthError` | |
| `productWeightError` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
    <sw-product-measurement-form
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_specifications_measures_packaging %}
<mt-card
    v-if="showProductCard('selling_packaging') && !isDigitalProduct"
    class="sw-product-detail-specification__selling-packaging"
    position-identifier="sw-product-detail-specifications-measures-packaging"
    :title="$tc('sw-product.specifications.cardTitleSellingPackaging')"
>
    {% block sw_product_detail_specifications_measures_packaging_content %}
```

## sw-product-media-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| isInherited | `any` | `false` | no |  |
| fileAccept | `any` | `'*/*'` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| media-open | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCreated` | |
| `onOpenMedia` | |
| `updateColumnCount` | |
| `getPlaceholderCount` | |
| `createPlaceholderMedia` | |
| `buildProductMedia` | |
| `successfulUpload` | |
| `createMediaAssociation` | |
| `onUploadFailed` | |
| `removeCover` | |
| `isCover` | |
| `isSpatial` | |
| `isArReady` | |
| `removeFile` | |
| `markMediaAsCover` | |
| `onDropMedia` | |
| `onMediaItemDragSort` | |
| `updateMediaItemPositions` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `mediaItems` | |
| `cover` | |
| `isStoreLoading` | |
| `isLoading` | |
| `productMediaRepository` | |
| `mediaRepository` | |
| `productMedia` | |
| `productMediaStore` | |
| `gridAutoRows` | |
| `currentCoverID` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
            <sw-product-media-form
                v-if="mediaFormVisible"
                :key="isInherited"
                :product-id="isInherited ? parentProduct.id : product.id"
                :is-inherited="isInherited"
                :disabled="isInherited || !acl.can('product.editor')"
                @media-open="onOpenMediaModal"
            />
            {% endblock %}

        </mt-card>
        {% endblock %}

    </template>
</sw-inherit-wrapper>
```

## sw-product-modal-delivery

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| configuration-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveDeliveryConfiguration` | |
| `cancelDeliveryConfiguration` | |
| `handleExpandedListing` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
    <sw-product-modal-delivery
        v-if="activeModal === 'deliveryModal'"
        :product="productEntity"
        :selected-groups="configSettingGroups"
        @configuration-close="onConfigurationClosed"
        @modal-close="activeModal = ''"
    />
    {% endblock %}

    {% block sw_product_properties_add_properties_modal %}
    <sw-product-add-properties-modal
        v-if="showAddPropertiesModal"
        :new-properties="newProperties"
        @modal-cancel="onCancelAddPropertiesModal"
        @modal-save="onSaveAddPropertiesModal"
```

## sw-product-modal-variant-generation

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| groups | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |
| actualStatus | `any` | `'is-physical'` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| variations-finish-generate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountComponent` | |
| `onQueuesHandler` | |
| `onProgressMaxHandler` | |
| `onProgressActualHandler` | |
| `removeFile` | |
| `removeFileForAllVariants` | |
| `getList` | |
| `handlePageChange` | |
| `generateVariants` | |
| `showNextStep` | |
| `calcVariantsNumber` | |
| `onChangeAllVariantValues` | |
| `onChangeVariantValue` | |
| `isUploadDisabled` | |
| `isExistingMedia` | |
| `successfulUpload` | |
| `updateUsageForAllVariantFiles` | |
| `pushFileToUsageList` | |
| `onModalCancel` | |
| `addOriginalConfiguratorSettings` | |
| `emptyConfiguratorSettings` | |
| `onTermChange` | |
| `removeDuplicateEntries` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currencies` | |
| `productRepository` | |
| `optionRepository` | |
| `mediaRepository` | |
| `progressInPercentage` | |
| `progressMessage` | |
| `buttonVariant` | |
| `buttonLabel` | |
| `isGenerateButtonDisabled` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
    <sw-product-modal-variant-generation
        v-if="activeModal === 'variantGeneration'"
        :product="productEntity"
        :groups="groups"
        :actual-status="activeTab"
        :selected-groups="configSettingGroups"
        @modal-close="activeModal = ''"
        @variations-finish-generate="updateVariations"
    />
    {% endblock %}

    {% block sw_product_detail_variants_modal_delivery %}
    <sw-product-modal-delivery
        v-if="activeModal === 'deliveryModal'"
        :product="productEntity"
```

## sw-product-packaging-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | — | yes |  |
| showSettingPackaging | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `productPurchaseUnitError` | |
| `productReferenceUnitError` | |
| `productPackUnitError` | |
| `productPackUnitPluralError` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
    <sw-product-packaging-form
        :show-setting-packaging="showModeSetting"
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_specifications_property %}
<sw-product-properties
    v-show="showProductCard('properties')"
/>
{% endblock %}

{% block sw_product_detail_specifications_essential_characteristics %}
```

## sw-product-price-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `removePriceInheritation` | |
| `inheritationCheckFunction` | |
| `onMaintainCurrenciesClose` | |
| `getTaxLabel` | |
| `updatePrices` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isLoading` | |
| `defaultPrice` | |
| `defaultCurrency` | |
| `productTaxRate` | |
| `showModeSetting` | |
| `product` | |
| `parentProduct` | |
| `taxes` | |
| `currencies` | |
| `productTaxIdError` | |
| `productPriceError` | |
| `productPurchasePricesError` | |
| `taxRateHelpText` | |
| `prices` | |
| `parentPrices` | |
| `taxRateOptions` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-price-form :allow-edit="acl.can('product.editor')" />
```

## sw-product-properties

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| isAssociation | `any` | `true` | no |  |
| showInheritanceSwitcher | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getGroupIds` | |
| `getProperties` | |
| `onDeletePropertyValue` | |
| `onDeleteProperty` | |
| `onDeleteProperties` | |
| `onChangeSearchTerm` | |
| `turnOnAddPropertiesModal` | |
| `turnOffAddPropertiesModal` | |
| `updateNewProperties` | |
| `onCancelAddPropertiesModal` | |
| `onSaveAddPropertiesModal` | |
| `checkIfPropertiesExists` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `propertyGroupRepository` | |
| `propertyOptionRepository` | |
| `propertyGroupCriteria` | |
| `propertyExistsCriteria` | |
| `propertyColumns` | |
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `isChild` | |
| `productProperties` | |
| `assetFilter` | |
| `productHasProperties` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-specifications/sw-product-detail-specifications.html.twig`
```twig
<sw-product-properties
    v-show="showProductCard('properties')"
/>
{% endblock %}

{% block sw_product_detail_specifications_essential_characteristics %}
<mt-card
    v-show="showProductCard('essential_characteristics')"
    class="sw-product-detail-specification__essential-characteristics"
    position-identifier="sw-product-detail-specifications-essential-characteristics"
    :title="$tc('sw-product.specifications.cardTitleEssentialCharacteristics')"
>
    {% block sw_product_detail_specifications_essential_characteristics_content %}
    <sw-product-feature-set-form :allow-edit="acl.can('product.editor')" />
    {% endblock %}
```

## sw-product-restriction-selection

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| groupsWithOptions | `any` | — | yes |  |
| restriction | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| contentAfter | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| restriction-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `deleteRestriction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `availableGroups` | |
| `availableGroupsOptions` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-variants-configurator/sw-product-variants-configurator-restrictions/sw-product-variants-configurator-restrictions.html.twig`
```twig
<sw-product-restriction-selection
    v-for="(restriction, index) in actualRestriction.values"
    :key="restriction.id"
    :groups-with-options="groupsWithOptions"
    :restriction="restriction"
    @restriction-delete="deleteRestriction"
>

    <template #contentAfter>
        <p
            v-if="index < actualRestrictionValueLength - 1"
            class="sw-product-variants-configurator-restrictions__seperator"
        >
            {{ $tc('sw-product.variations.configuratorModal.singleRestrictionSeperation') }}
        </p>
```

## sw-product-seo-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `fetchVariants` | |
| `getItemName` | |
| `onSearch` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `hasParent` | |
| `hasVariants` | |
| `variantCriteria` | |
| `isCanonicalUrlSelectLoading` | |
| `variantsWithResetOption` | |
| `product` | |
| `parentProduct` | |
| `isLoading` | |
| `productKeywordsError` | |
| `productMetaDescriptionError` | |
| `productMetaTitleError` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-seo/sw-product-detail-seo.html.twig`
```twig
    <sw-product-seo-form
        ref="seoForm"
        :allow-edit="acl.can('product.editor')"
    />
    {% endblock %}
</mt-card>
{% endblock %}

{% block sw_product_detail_seo_urls %}
<sw-seo-url
    v-if="product.seoUrls"
    :has-default-template="false"
    :disabled="!acl.can('product.editor')"
    :urls="product.seoUrls"
    @on-change-sales-channel="onChangeSalesChannel"
```

## sw-product-settings-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowEdit | `any` | `true` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `parentProduct` | |
| `productReleaseDateError` | |
| `productStockError` | |
| `productMinPurchaseError` | |
| `productMaxPurchaseError` | |
| `productEanError` | |
| `productManufacturerNumberError` | |
| `productShippingFreeError` | |
| `productMarkAsTopsellerError` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-base/sw-product-detail-base.html.twig`
```twig
<sw-product-settings-form :allow-edit="acl.can('product.editor')" />
```

## sw-product-settings-mode

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| modeSettings | `any` | — | yes |  |
| isLoading | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| settings-change | — | |
| settings-item-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeSetting` | |
| `onChangeSettingItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `advancedMode` | |
| `settings` | |

### Examples

#### Example 1
Source: `sw-product/page/sw-product-detail/sw-product-detail.html.twig`
```twig
            <sw-product-settings-mode
                v-if="showAdvanceModeSetting"
                :is-loading="isLoading"
                :mode-settings="advancedModeSetting"
                @settings-item-change="onChangeSettingItem"
                @settings-change="onChangeSetting"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}

    <template #sidebar>
        {% block sw_product_detail_sidebar %}
        {% endblock %}
```

## sw-product-stream-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productStreamId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `loadProductTypes` | |
| `createProductStream` | |
| `loadEntityData` | |
| `loadFilters` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `onDuplicate` | |
| `onSave` | |
| `showErrorNotification` | |
| `saveProductStream` | |
| `syncProductStreamFilters` | |
| `onCancel` | |
| `openModalPreview` | |
| `closeModalPreview` | |
| `getProductCustomFields` | |
| `getCustomFieldLabel` | |
| `mapCustomFieldType` | |
| `updateFilterTree` | |
| `getNoPermissionsTooltip` | |
| `normalizeFilterCollection` | |
| `hasProductStatesFilter` | |
| `isDeprecatedProductStatesField` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `productStreamRepository` | |
| `productStreamFiltersRepository` | |
| `customFieldSetRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `isSystemLanguage` | |
| `nameRequired` | |
| `productStreamNameError` | |
| `showCustomFields` | |
| `productStreamIndexingEnabled` | |
| `showProductStatesFilterWarning` | |

### Examples

#### Basic Usage
```twig
<sw-product-stream-detail>
    <!-- content -->
</sw-product-stream-detail>
```

## sw-product-stream-field-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| definition | `any` | — | yes |  |
| field | `any` | `null` | no |  |
| index | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| hasError | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| field-changed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `changeField` | |
| `getPropertyTranslation` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `options` | |
| `arrowPrimaryColor` | |

### Examples

#### Example 1
Source: `sw-product-stream/component/sw-product-stream-filter/sw-product-stream-filter.html.twig`
```twig
        <sw-product-stream-field-select
            v-bind="{ field: fields[index], definition, index }"
            :disabled="!acl.can('product_stream.editor') || undefined"
            :has-error="hasError"
            @field-changed="updateFields"
        />
        {% endblock %}
    </template>
    {% endblock %}

    {% block sw_product_stream_filter_value %}
    <sw-product-stream-value
        v-bind="{ condition, ...lastField }"
        :disabled="!acl.can('product_stream.editor') || undefined"
        @type-change="changeType"
```

## sw-product-stream-filter

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `updateFields` | |
| `handleWrapForTypeNull` | |
| `changeBooleanValue` | |
| `changeEmptyValue` | |
| `changeType` | |
| `wrapInNot` | |
| `unwrapNot` | |
| `copyParameters` | |
| `getNoPermissionsTooltip` | |
| `isCustomField` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `actualCondition` | |
| `fields` | |
| `fieldDefinitions` | |
| `lastField` | |

### Examples

#### Basic Usage
```twig
<sw-product-stream-filter>
    <!-- content -->
</sw-product-stream-filter>
```

## sw-product-stream-grid-preview

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filters | `any` | — | yes |  |
| columns | `any` | — | no |  |
| criteria | `any` | — | no |  |
| showSelection | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| additional-columns | — | |
| empty-state | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `createdComponent` | |
| `loadSystemDefaultCurrency` | |
| `loadProducts` | |
| `onPageChange` | |
| `getPriceForDefaultCurrency` | |
| `onSelectionChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `currencyRepository` | |
| `salesChannelRepository` | |
| `salesChannelCriteria` | |
| `defaultColumns` | |
| `productColumns` | |
| `emptyStateMessage` | |
| `assetFilter` | |
| `currencyFilter` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-products/sw-category-detail-products.html.twig`
```twig
    <sw-product-stream-grid-preview
        :filters="productStreamFilter"
        :columns="productColumns"
    />
</template>
{% endblock %}

{% block sw_category_detail_product_assignment_column_name %}
<template #[nameColumn]="{ item, column }">
    <router-link
        :to="{ name: column.routerLink, params: { id: item.id } }"
    >
        <sw-product-variant-info :variations="item.variation">
            {{ getItemName(item) }}
        </sw-product-variant-info>
```

## sw-product-stream-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onInlineEditSave` | |
| `onChangeLanguage` | |
| `getList` | |
| `getProductStreamColumns` | |
| `getNoPermissionsTooltip` | |
| `onDeleteItemFailed` | |
| `onDeleteItemsFailed` | |
| `onDuplicate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productStreamRepository` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-product-stream-list>
    <!-- content -->
</sw-product-stream-list>
```

## sw-product-stream-modal-preview

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filters | `any` | — | yes |  |
| defaultLimit | `any` | `25` | no |  |
| defaultSorting | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |
| `onSalesChannelChange` | |
| `loadEntityData` | |
| `loadSalesChannels` | |
| `mapFiltersForSearch` | |
| `closeModal` | |
| `getPriceForDefaultCurrency` | |
| `onPageChange` | |
| `loadSalesChannelById` | |
| `isNotEqualToAnyType` | |
| `addRandomSort` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `salesChannelCriteria` | |
| `previewCriteria` | |
| `previewSelectionCriteria` | |
| `productColumns` | |
| `currencyFilter` | |
| `stockColorVariantFilter` | |

### Examples

#### Example 1
Source: `sw-cms/elements/product-slider/config/sw-cms-el-config-product-slider.html.twig`
```twig
<sw-product-stream-modal-preview
    v-if="showProductStreamPreview"
    :filters="productStream.apiFilter"
    :default-limit="element.config.productStreamLimit.value"
    :default-sorting="element.config.productStreamSorting.value"
    @modal-close="onCloseProductStreamModal"
/>

<sw-container
    columns="1fr 1fr"
    gap="30px"
>
    {% block sw_cms_element_product_slider_config_content_product_stream_sorting %}
    <sw-cms-inherit-wrapper
        field="productStreamSorting"
```

#### Example 2
Source: `sw-product/component/sw-product-cross-selling-form/sw-product-cross-selling-form.html.twig`
```twig
        <sw-product-stream-modal-preview
            v-if="showModalPreview"
            ref="modalPreview"
            :filters="productStreamFilterTree"
            @modal-close="closeModalPreview"
        />
        {% endblock %}
    </div>
</mt-card>
{% endblock %}

{% block sw_product_detail_cross_selling_form_modal_delete %}
<sw-modal
    v-if="showDeleteModal"
    variant="small"
```

#### Example 3
Source: `sw-product-stream/page/sw-product-stream-detail/sw-product-stream-detail.html.twig`
```twig
                <sw-product-stream-modal-preview
                    v-if="showModalPreview"
                    ref="modalPreview"
                    :filters="productStreamFiltersTree"
                    @modal-close="closeModalPreview"
                />
                {% endblock %}

                {% block sw_prouct_stream_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-product-stream-detail-custom-field-sets"
                    :large="true"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                >
```

## sw-product-stream-value

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| condition | `any` | — | yes |  |
| fieldName | `any` | `null` | no |  |
| definition | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-label-property | — | |
| result-item | — | |
| result-description-property | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| empty-change | — | |
| type-change | — | |
| boolean-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeType` | |
| `getConditionType` | |
| `getRangeType` | |
| `getParameters` | |
| `getParameterName` | |
| `getParameterType` | |
| `setBooleanValue` | |
| `setSearchTerm` | |
| `onSelectCollapsed` | |
| `getCategoryBreadcrumb` | |
| `isEntityCustomField` | |
| `getCustomFieldEntityName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `repository` | |
| `entityCustomFieldRepository` | |
| `componentClasses` | |
| `growthClass` | |
| `disabledClass` | |
| `actualCondition` | |
| `isMultiSelectValue` | |
| `filterType` | |
| `fieldDefinition` | |
| `operators` | |
| `relativeTimeOperators` | |
| `productStateOptions` | |
| `productTypeOptions` | |
| `fieldType` | |
| `booleanOptions` | |
| `reversedEmptyOptions` | |
| `multiValue` | |
| `inputComponent` | |
| `currentParameter` | |
| `gte` | |
| `lte` | |
| `operator` | |
| `emptyValue` | |
| `stringValue` | |
| `context` | |
| `productCriteria` | |
| `propertyCriteria` | |
| `visibilitiesCriteria` | |
| `resultCriteria` | |
| `customFieldCriteria` | |
| `visibilitiesLabelCallback` | |
| `isProductEntity` | |

### Examples

#### Example 1
Source: `sw-product-stream/component/sw-product-stream-filter/sw-product-stream-filter.html.twig`
```twig
    <sw-product-stream-value
        v-bind="{ condition, ...lastField }"
        :disabled="!acl.can('product_stream.editor') || undefined"
        @type-change="changeType"
        @boolean-change="changeBooleanValue"
        @empty-change="changeEmptyValue"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_product_stream_filter_field_actions %}
<sw-context-button
    v-tooltip="getNoPermissionsTooltip('product_stream.editor', false)"
    class="sw-product-stream-filter__context-button"
```

## sw-product-variant-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variations | `any` | `null` | no |  |
| highlighted | `any` | `false` | no |  |
| searchTerm | `any` | `''` | no |  |
| titleTerm | `any` | `null` | no |  |
| showTooltip | `any` | `true` | no |  |
| ommitParenthesis | `any` | `false` | no |  |
| seperator | `any` | `'|'` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getFirstSlot` | |
| `setHelpText` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productName` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-product-variant-info
    :variations="item.variation"
    :show-tooltip="false"
>
    <sw-settings-search-live-search-keyword
        :text="(item.name || item.translated.name)"
        :search-term="liveSearchTerm"
    />
</sw-product-variant-info>
```

#### Example 2
Source: `sw-category/view/sw-category-detail-products/sw-category-detail-products.html.twig`
```twig
<sw-product-variant-info :variations="item.variation">
    {{ getItemName(item) }}
</sw-product-variant-info>
```

#### Example 3
Source: `sw-cms/component/sw-cms-layout-assignment-modal/sw-cms-layout-assignment-modal.html.twig`
```twig
<sw-product-variant-info
    :variations="item.options"
    @click="onAbort"
>
    {{ item.translated.name }}
</sw-product-variant-info>
```

#### Example 4
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-product-variant-info :variations="item.variation">
    {{ item.translated.name || item.name }}
</sw-product-variant-info>
```

#### Example 5
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-product-variant-info :variations="item.variation">
    {{ item.translated.name || item.name }}
</sw-product-variant-info>
```

## sw-product-variant-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productEntity | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchProductMedias` | |
| `fetchProductConfiguration` | |
| `fetchSystemCurrency` | |
| `fetchProductVariants` | |
| `getDefaultPriceForVariant` | |
| `onInheritanceRestore` | |
| `onInheritanceRemove` | |
| `sortOptions` | |
| `buildVariantOptions` | |
| `buildVariantName` | |
| `getVariantPrice` | |
| `onPageChange` | |
| `visitProduct` | |
| `getItemMedia` | |
| `deleteVariants` | |
| `canVariantsBeDeleted` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onClickBulkDelete` | |
| `closeDeleteModal` | |
| `onDeleteVariant` | |
| `onSearchTermChange` | |
| `onSortColumn` | |
| `getNoPermissionsTooltip` | |
| `isMediaFieldInherited` | |
| `onMediaInheritanceRestore` | |
| `onMediaInheritanceRemove` | |
| `loadGroups` | |
| `resetFilterOptions` | |
| `filterOptionChecked` | |
| `getOptionsForGroup` | |
| `toggleFilterMenu` | |
| `toggleBulkEditModal` | |
| `onEditItems` | |
| `variantIsDigital` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `openMainProductText` | |
| `productRepository` | |
| `productMediaRepository` | |
| `productConfigurationRepository` | |
| `currencyRepository` | |
| `groupRepository` | |
| `contextMenuEditText` | |
| `filterCriteria` | |
| `productVariantCriteria` | |
| `gridColumns` | |
| `canBeDeletedCriteria` | |
| `groupCriteria` | |
| `selectedGroups` | |
| `filterOptionsListing` | |
| `stockColorVariantFilter` | |

### Examples

#### Example 1
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
    <sw-product-variant-modal
        v-if="showVariantModal"
        :product-entity="productEntityVariantModal"
        @modal-close="closeVariantModal"
    />
    {% endblock %}
</template>

{% block sw_product_list_sidebar %}
<template #sidebar>
    <sw-sidebar>
        {% block sw_product_list_sidebar_refresh %}
        <sw-sidebar-item
            icon="regular-undo"
            :title="$tc('sw-product.list.titleSidebarItemRefresh')"
```

## sw-product-variants-configurator-prices

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `mountedComponent` | |
| `loadCurrencies` | |
| `getOptionsForGroup` | |
| `resetSurcharges` | |
| `getCurrencyOfOption` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currencyRepository` | |
| `currenciesList` | |
| `optionColumns` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
    <sw-product-variants-configurator-prices
        v-if="activeTab == 'prices'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

    {% block sw_product_modal_variant_generation_main_configurator_restrictions %}
    <sw-product-variants-configurator-restrictions
        v-if="activeTab == 'restrictions'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
```

## sw-product-variants-configurator-restrictions

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getOptionsForGroupId` | |
| `getRestrictionsWithNaming` | |
| `filterEmptyValues` | |
| `addEmptyRestrictionCombination` | |
| `addEmptyRestriction` | |
| `cancelAddRestriction` | |
| `saveAddRestriction` | |
| `editRestrictionCombination` | |
| `deleteRestrictionCombination` | |
| `deleteRestriction` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `restrictionColumns` | |
| `actualRestrictionValueLength` | |
| `filteredRestrictions` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
    <sw-product-variants-configurator-restrictions
        v-if="activeTab == 'restrictions'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_product_modal_variant_generation_footer %}
<template #modal-footer>
    {% block sw_product_modal_variant_generation_footer_cancel %}
    <mt-button
        size="small"
        variant="secondary"
```

## sw-product-variants-configurator-selection

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| toolbar | — | |
| toolbar-search-field | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| option-select | — | |

### Methods

| Method | Description |
|--------|-------------|
| `addOptionCount` | |
| `selectOptions` | |
| `onOptionSelect` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `configuratorSettingsRepository` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
    <sw-product-variants-configurator-selection
        v-show="activeTab == 'options'"
        :product="product"
        :options="product.configuratorSettings"
        :overlay="false"
        :collapsible="false"
        :is-add-only="isAddOnly"
        @variations-finish-generate="$emit('variations-finish-generate')"
        @option-select="calcVariantsNumber()"
    />
    {% endblock %}

    {% block sw_product_modal_variant_generation_main_configurator_prices %}
    <sw-product-variants-configurator-prices
        v-if="activeTab == 'prices'"
```

## sw-product-variants-delivery-listing

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selection-label-property | — | |
| result-item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updateListingMode` | |
| `updateVariantMode` | |
| `updateMainVariant` | |
| `isActiveGroupInListing` | |
| `onChangeGroupListing` | |
| `isActiveListingMode` | |
| `isDisabledListingMode` | |
| `isSelected` | |
| `onSearchTermChange` | |
| `onSelectCollapsed` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `listingModeOptions` | |
| `listingMode` | |
| `mainVariantModeOptions` | |
| `mainVariant` | |
| `variantCriteria` | |
| `context` | |
| `selectedGroupsSorted` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-delivery/sw-product-modal-delivery.html.twig`
```twig
    <sw-product-variants-delivery-listing
        v-if="activeTab == 'listing'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_product_modal_delivery_footer %}
<template #modal-footer>
    {% block sw_product_modal_delivery_footer_button_cancel %}
    <mt-button
        size="small"
        variant="secondary"
```

## sw-product-variants-delivery-media

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `onUploadsAdded` | |
| `successfulUpload` | |
| `removeMedia` | |
| `setMedia` | |
| `onChangeGroupListing` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selectedGroupsSorted` | |
| `optionColumns` | |
| `activeOptions` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-delivery/sw-product-modal-delivery.html.twig`
```twig
    <sw-product-variants-delivery-media
        v-if="activeTab == 'media'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

    {% block sw_product_modal_delivery_listing %}
    <sw-product-variants-delivery-listing
        v-if="activeTab == 'listing'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}
</div>
```

## sw-product-variants-delivery-order

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| product | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `createOrderObjects` | |
| `getOptionsForGroup` | |
| `orderChanged` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-modal-delivery/sw-product-modal-delivery.html.twig`
```twig
    <sw-product-variants-delivery-order
        v-if="activeTab == 'order'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

    {% block sw_product_modal_delivery_media %}
    <sw-product-variants-delivery-media
        v-if="activeTab == 'media'"
        :product="product"
        :selected-groups="selectedGroups"
    />
    {% endblock %}

```

## sw-product-variants-media-upload

> Shopware Administration component.

- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| source | `any` | — | yes |  |
| parentProduct | `any` | — | yes |  |
| isInherited | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getMediaDefaultFolderId` | |
| `isCover` | |
| `markMediaAsCover` | |
| `removeMedia` | |
| `onAddMedia` | |
| `addMedia` | |
| `isExistingMedia` | |
| `onUploadMediaSuccessful` | |
| `isReplacedMedia` | |
| `onUploadMediaFailed` | |
| `previewMedia` | |
| `onClosePreviewModal` | |
| `updateMediaItemPositions` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productMediaRepository` | |
| `product` | |
| `mediaSource` | |
| `cover` | |
| `coverImageSource` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
            <sw-product-variants-media-upload
                :source="item"
                :upload-tag="item.id"
                :is-inherited="isMediaFieldInherited(item)"
                :parent-product="productEntity"
                disabled
            />
        </template>
        {% endblock %}
    </sw-bulk-edit-modal>
</template>
{% endblock %}

{% block sw_product_variant_modal_body_grid_column_name %}
<template #column-name="{item, isInlineEdit}">
```

#### Example 2
Source: `sw-product/component/sw-product-variant-modal/sw-product-variant-modal.html.twig`
```twig
    <sw-product-variants-media-upload
        :source="item"
        :upload-tag="item.id"
        :is-inherited="isMediaFieldInherited(item)"
        :disabled="isInlineEdit ? isMediaFieldInherited(item) : true"
        :parent-product="productEntity"
    />
    {% endblock %}
    {% endblock %}
</template>
{% endblock %}

{% block sw_product_variant_modal_body_grid_actions %}
<template #actions="{item}">

```

#### Example 3
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-product-variants-media-upload
        :source="item"
        :upload-tag="item.id"
        :is-inherited="isMediaFieldInherited(item)"
        :disabled="isInlineEdit ? isMediaFieldInherited(item) : true"
        :parent-product="product"
    />
    {% endblock %}
    {% endblock %}
</template>
{% endblock %}

<template #column-downloads="{item, isInlineEdit, compact}">
    <sw-upload-listener
        :upload-tag="item.productNumber"
```

#### Example 4
Source: `sw-product/component/sw-product-variants/sw-product-variants-overview/sw-product-variants-overview.html.twig`
```twig
    <sw-product-variants-media-upload
        :source="item"
        :upload-tag="item.id"
        :is-inherited="isMediaFieldInherited(item)"
        :parent-product="product"
        disabled
    />
</template>
{% endblock %}

<template #column-downloads="{item, isInlineEdit, compact}">
    <sw-upload-listener
        :upload-tag="item.productNumber"
        auto-upload
        @media-upload-finish="(event) => successfulUpload(event, item)"
```

## sw-product-variants-overview

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productEntity | `any` | — | yes |  |
| selectedGroups | `any` | — | yes |  |
| productStates | `any` | — | no |  |
| productType | `any` | `'all'` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| generator-open | — | |
| delivery-open | — | |
| variants-finish-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `removeFile` | |
| `mediaExists` | |
| `successfulUpload` | |
| `getDownloadsSource` | |
| `getList` | |
| `buildSearchQuery` | |
| `getFilterOptions` | |
| `resetFilterOptions` | |
| `filterOptionChecked` | |
| `getFilterCriteria` | |
| `getOptionsForGroup` | |
| `isPriceFieldInherited` | |
| `isActiveFieldInherited` | |
| `isMediaFieldInherited` | |
| `onInheritanceRestore` | |
| `onActiveInheritanceRestore` | |
| `onActiveInheritanceRemove` | |
| `onInheritanceRemove` | |
| `onMediaInheritanceRestore` | |
| `onMediaInheritanceRemove` | |
| `getDefaultPriceForVariant` | |
| `onVariationDelete` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `canVariantBeDeleted` | |
| `onOptionEdit` | |
| `isPriceEditing` | |
| `toggleBulkEditModal` | |
| `onEditItems` | |
| `onClickBulkDelete` | |
| `variantIsDigital` | |
| `updateVariantListingConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `currencies` | |
| `taxes` | |
| `variants` | |
| `isLoading` | |
| `defaultPrice` | |
| `defaultCurrency` | |
| `productTaxRate` | |
| `productRepository` | |
| `productMediaRepository` | |
| `mediaRepository` | |
| `productDownloadRepository` | |
| `variantColumns` | |
| `currencyColumns` | |
| `canBeDeletedCriteria` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-variants/sw-product-detail-variants.html.twig`
```twig
<sw-product-variants-overview
    v-if="product.id"
    v-show="variantListHasContent && !isLoading"
    ref="generatedVariants"
    :product-states="currentProductStates"
    :product-type="currentProductType"
    :groups="groups"
    :selected-groups="configSettingGroups"
    :product-entity="productEntity"
    @variants-finish-update="updateVariantListHasContent"
    @generator-open="openModal('variantGeneration')"
    @delivery-open="openModal('deliveryModal')"
/>
{% endblock %}

```

## sw-product-variants-price-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| price | `any` | — | yes |  |
| taxRate | `any` | `null` | no |  |
| currency | `any` | — | yes |  |
| readonly | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| price-lock-change | — | |
| change | — | |
| price-calculate | — | |
| price-gross-change | — | |
| price-net-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onLockSwitch` | |
| `onPriceGrossChange` | |
| `onPriceGrossChangeDebounce` | |
| `onPriceNetChange` | |
| `onPriceNetChangeDebounce` | |
| `convertNetToGross` | |
| `convertGrossToNet` | |
| `requestTaxValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `calculatePriceApiService` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-variants/sw-product-variants-configurator/sw-product-variants-configurator-prices/sw-product-variants-configurator-prices.html.twig`
```twig
                    <sw-product-variants-price-field
                        :price="getCurrencyOfOption(item, currency.id)"
                        :tax-rate="product.taxId"
                        :currency="currency"
                        compact
                    />
                </template>
                {% endblock %}

                {% block sw_product_variants_configurator_prices_actions %}
                <template
                    #actions="{ item }"
                >
                    {% block sw_product_variants_configurator_prices_actions_items %}
                    <sw-context-menu-item
```

## sw-product-visibility-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onPageChange` | |
| `changeVisibilityValue` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `product` | |
| `truncateFilter` | |
| `filteredItems` | |
| `names` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-visibility/sw-bulk-edit-product-visibility.html.twig`
```twig
<sw-product-visibility-detail />
```

#### Example 2
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
<sw-product-visibility-detail :disabled="!allowEdit" />
```

## sw-product-visibility-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| criteria | `any` | — | no |  |

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
| `product` | |
| `repository` | |
| `associationRepository` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/component/product/sw-bulk-edit-product-visibility/sw-bulk-edit-product-visibility.html.twig`
```twig
        <sw-product-visibility-select
            ref="productVisibility"
            :key="isInherited"
            class="sw-product-detail__select-visibility"
            :entity-collection="currentValue"
            :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
            :disabled="disabled || undefined"
            @update:entity-collection="updateCurrentValue"
        />
    </template>
</sw-inherit-wrapper>
{% endblock %}

{% block sw_bulk_edit_product_visibility_advanced %}
<sw-container
```

#### Example 2
Source: `sw-product/component/sw-product-category-form/sw-product-category-form.html.twig`
```twig
            <sw-product-visibility-select
                v-if="!loading.product && !loading.parentProduct && multiSelectVisible"
                ref="productVisibility"
                :key="isInherited"
                class="sw-product-detail__select-visibility"
                :entity-collection="currentValue"
                :placeholder="$tc('sw-product.visibility.placeholderVisibility')"
                :disabled="isInherited || !allowEdit"
                @update:entity-collection="updateCurrentValue"
            />
        </template>
    </sw-inherit-wrapper>
    {% endblock %}
</sw-container>

```

## sw-profile-index-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| user | `any` | — | yes |  |
| languages | `any` | — | yes |  |
| newPassword | `any` | `null` | no |  |
| newPasswordConfirm | `any` | `null` | no |  |
| avatarMediaItem | `any` | `null` | no |  |
| isUserLoading | `any` | — | yes |  |
| languageId | `any` | `null` | no |  |
| isDisabled | `any` | — | yes |  |
| userRepository | `any` | — | yes |  |
| timezoneOptions | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| new-password-change | — | |
| new-password-confirm-change | — | |
| media-upload | — | |
| media-remove | — | |
| media-open | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onUploadMedia` | |
| `onDropMedia` | |
| `onRemoveMedia` | |
| `onOpenMedia` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `userPasswordError` | |
| `computedNewPassword` | |
| `computedNewPasswordConfirm` | |
| `localeOptions` | |

### Examples

#### Basic Usage
```twig
<sw-profile-index-general
    user="..."
    languages="..."
>
    <!-- content -->
</sw-profile-index-general>
```

## sw-profile-index-privacy-preferences

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-profile-index-privacy-preferences>
    <!-- content -->
</sw-profile-index-privacy-preferences>
```

## sw-profile-index-search-preferences

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `getMinSearchTermLength` | |
| `getDataSource` | |
| `addEventListeners` | |
| `removeEventListeners` | |
| `updateDataSource` | |
| `getModuleTitle` | |
| `onChangeSearchPreference` | |
| `onSelect` | |
| `onReset` | |
| `resetSearchPreference` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `minSearchTermLength` | |
| `searchPreferences` | |
| `userSearchPreferences` | |
| `defaultSearchPreferences` | |
| `adminEsEnable` | |

### Examples

#### Basic Usage
```twig
<sw-profile-index-search-preferences>
    <!-- content -->
</sw-profile-index-search-preferences>
```

## sw-profile-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeMountComponent` | |
| `loadLanguages` | |
| `getUserData` | |
| `resetGeneralData` | |
| `saveFinish` | |
| `onSave` | |
| `checkEmail` | |
| `checkPassword` | |
| `createErrorMessage` | |
| `saveUser` | |
| `updateCurrentUser` | |
| `loadMediaItem` | |
| `setMediaItem` | |
| `onDropMedia` | |
| `onCloseConfirmPasswordModal` | |
| `onUnlinkAvatar` | |
| `openMediaModal` | |
| `handleUserSaveError` | |
| `onChangeNewPassword` | |
| `onChangeNewPasswordConfirm` | |
| `onMediaSelectionChange` | |
| `getMediaDefaultFolderId` | |
| `saveMinSearchTermLength` | |
| `saveUserSearchPreferences` | |
| `onVerifyPasswordFinished` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `minSearchTermLength` | |
| `searchPreferences` | |
| `userEmailError` | |
| `userTimeZoneError` | |
| `userSearchPreferences` | |
| `isDisabled` | |
| `userRepository` | |
| `languageRepository` | |
| `localeRepository` | |
| `mediaRepository` | |
| `languageId` | |

### Examples

#### Basic Usage
```twig
<sw-profile-index>
    <!-- content -->
</sw-profile-index>
```

## sw-progress-bar

> **Migration wrapper** — Delegates to `mt-progress-bar` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-progress-bar for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `0` | no |  |
| maxValue | `any` | `100` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `styleWidth` | |
| `progressClasses` | |

### Examples

#### Basic Usage
```twig
<sw-progress-bar>
    <!-- content -->
</sw-progress-bar>
```

## sw-promotion-detail-discounts

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onAddDiscount` | |
| `deleteDiscount` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `promotion` | |
| `isLoading` | |
| `discounts` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-detail-discounts>
    <!-- content -->
</sw-promotion-detail-discounts>
```

## sw-promotion-discount-component

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | yes |  |
| discount | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| discount-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onDiscountScopeChanged` | |
| `onDiscountTypeChanged` | |
| `onDiscountValueChanged` | |
| `onMaxValueChanged` | |
| `onClickAdvancedPrices` | |
| `recalculatePrices` | |
| `calculatePrice` | |
| `clearAdvancedPrices` | |
| `isMemberOfCollection` | |
| `onCloseAdvancedPricesModal` | |
| `onShowDeleteModal` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `loadSetGroups` | |
| `loadSorters` | |
| `loadPickers` | |
| `loadRestrictedRules` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `advancedPricesRepo` | |
| `repositoryGroups` | |
| `currencyRepository` | |
| `ruleFilter` | |
| `currencyPriceColumns` | |
| `scopes` | |
| `types` | |
| `valueSuffix` | |
| `maxValueSuffix` | |
| `showMaxValueSettings` | |
| `showAbsoluteAdvancedPricesSettings` | |
| `showMaxValueAdvancedPrices` | |
| `maxValueAdvancedPricesTooltip` | |
| `isEditingDisabled` | |
| `displayAdvancedRuleOption` | |
| `graduationSorters` | |
| `graduationPickers` | |
| `isSetGroup` | |
| `isSet` | |
| `graduationAppliers` | |
| `graduationCounts` | |
| `isPickingModeVisible` | |
| `isMaxUsageVisible` | |
| `promotionDiscountSnippet` | |
| `fieldScopeOptions` | |
| `applyCountOptions` | |
| `maxCountOptions` | |
| `sorterOptions` | |
| `pickerOptions` | |
| `discountTypeOptions` | |

### Examples

#### Example 1
Source: `sw-promotion-v2/view/sw-promotion-detail-discounts/sw-promotion-detail-discounts.html.twig`
```twig
        <sw-promotion-discount-component
            v-for="discount in discounts"
            :key="discount.id"
            :promotion="promotion"
            :discount="discount"
            @discount-delete="deleteDiscount"
        />
        {% endblock %}
    </ul>
    {% endblock %}
</div>
{% endblock %}

```

## sw-promotion-v2-cart-condition-form

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | `null` | no |  |
| restrictedRules | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `addSetGroup` | |
| `duplicateSetGroup` | |
| `deleteSetGroup` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `promotionGroupRepository` | |
| `ruleFilter` | |
| `packagers` | |
| `sorters` | |
| `isEditingDisabled` | |
| `packagerOptions` | |
| `sorterOptions` | |
| `setGroupCriteria` | |

### Examples

#### Example 1
Source: `sw-promotion-v2/view/sw-promotion-v2-conditions/sw-promotion-v2-conditions.html.twig`
```twig
        <sw-promotion-v2-cart-condition-form
            :promotion="promotion"
            :restricted-rules="cartRestrictedRules"
        />
        {% endblock %}

        {% block sw_promotion_v2_rule_conditions_rule_select_order_conditions %}
        <sw-select-rule-create
            v-if="promotion"
            v-model:rules="promotion.orderRules"
            class="sw-promotion-v2-conditions__rule-select-order-conditions"
            :local-mode="promotion.isNew()"
            :label="$tc('sw-promotion-v2.detail.conditions.preConditions.labelOrderConditionSelect')"
            :placeholder="$tc('sw-promotion-v2.detail.conditions.preConditions.placeholderOrderConditionSelect')"
            :rule-filter="orderConditionsFilter"
```

## sw-promotion-v2-conditions

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadExclusions` | |
| `onChangeExclusions` | |
| `createPromotionCollection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `exclusionCriteria` | |
| `personaRuleFilter` | |
| `cartConditionsRuleFilter` | |
| `orderConditionsFilter` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-conditions>
    <!-- content -->
</sw-promotion-v2-conditions>
```

## sw-promotion-v2-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |
| isCreateMode | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| generate-individual-codes-finish | — | |
| delete-individual-codes-finish | — | |
| clean-up-codes | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initialSort` | |
| `onChangeCodeType` | |
| `setNewCodeType` | |
| `loadCustomFieldSets` | |
| `onGenerateCodeFixed` | |
| `generateFinish` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `codeTypeOptions` | |
| `promotionNameError` | |
| `promotionValidUntilError` | |
| `showCustomFields` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-detail-base
    isCreateMode="..."
>
    <!-- content -->
</sw-promotion-v2-detail-base>
```

## sw-promotion-v2-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotionId | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `onChangeLanguage` | |
| `onSave` | |
| `onConfirmSave` | |
| `onCloseCodeTypeChangeModal` | |
| `savePromotion` | |
| `savePromotionSetGroups` | |
| `saveFinish` | |
| `onCancel` | |
| `onCleanUpCodes` | |
| `cleanUpCodes` | |
| `onGenerateIndividualCodesFinish` | |
| `onDeleteIndividualCodesFinish` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `promotionRepository` | |
| `isCreateMode` | |
| `promotionCriteria` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `promotionGroupRepository` | |
| `swPromotionV2DetailBaseError` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-detail>
    <!-- content -->
</sw-promotion-v2-detail>
```

## sw-promotion-v2-empty-state-hero

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| assetPath | `any` | `''` | no |  |
| description | `any` | `''` | no |  |
| hideDescription | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| actions | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `imagePath` | |
| `showDescription` | |
| `assetFilter` | |
| `actionSlotsAvailable` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-empty-state-hero
    title="..."
>
    <!-- content -->
</sw-promotion-v2-empty-state-hero>
```

## sw-promotion-v2-generate-codes-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| generate-finish | — | |
| close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updatePattern` | |
| `updatePreview` | |
| `onGenerate` | |
| `onClose` | |

### Examples

#### Example 1
Source: `sw-promotion-v2/component/promotion-codes/sw-promotion-v2-individual-codes-behavior/sw-promotion-v2-individual-codes-behavior.html.twig`
```twig
<sw-promotion-v2-generate-codes-modal
    v-if="generateCodesModal"
    :promotion="promotion"
    @generate-finish="onGenerateFinish"
    @close="onCloseGenerateCodesModal"
/>
{% endblock %}

{% block sw_promotion_v2_individual_codes_behavior_add_codes_modal %}
<sw-modal
    v-if="addCodesModal"
    class="sw-promotion-v2-individual-codes-behavior__add-codes-modal"
    variant="small"
    :title="$tc('sw-promotion-v2.detail.base.codes.individual.addCodesModal.title')"
    @modal-close="onCloseAddCodesModal"
```

## sw-promotion-v2-individual-codes-behavior

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| delete-finish | — | |
| generate-finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `onSearchTermChange` | |
| `loadIndividualCodesGrid` | |
| `onSelectionChange` | |
| `onCodeSelectionChange` | |
| `onShowCodeDeleteModal` | |
| `onShowCodeBulkDeleteModal` | |
| `onConfirmCodeDelete` | |
| `onConfirmCodeBulkDelete` | |
| `onCloseDeleteModal` | |
| `onCloseBulkDeleteModal` | |
| `onOpenGenerateCodesModal` | |
| `onGenerateFinish` | |
| `onCloseGenerateCodesModal` | |
| `onOpenAddCodesModal` | |
| `onAddCodes` | |
| `onCloseAddCodesModal` | |
| `routeToCustomer` | |
| `createRoutingErrorNotification` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `promotionRepository` | |
| `customerRepository` | |
| `deleteConfirmText` | |
| `codeColumns` | |
| `assetFilter` | |
| `dateFilter` | |

### Examples

#### Example 1
Source: `sw-promotion-v2/view/sw-promotion-v2-detail-base/sw-promotion-v2-detail-base.html.twig`
```twig
            <sw-promotion-v2-individual-codes-behavior
                :promotion="promotion"
                @generate-finish="$emit('generate-individual-codes-finish')"
                @delete-finish="$emit('delete-individual-codes-finish')"
            />
            {% endblock %}

        </template>
        {% endblock %}

    </mt-card>
    {% endblock %}

    {% block sw_promotion_detail_custom_field_sets %}
    <mt-card
```

## sw-promotion-v2-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `onChangeLanguage` | |
| `getPromotionColumns` | |
| `updateTotal` | |
| `onDuplicatePromotion` | |
| `deleteDisabledTooltip` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `promotionRepository` | |
| `promotionCriteria` | |
| `promotionColumns` | |
| `addButtonTooltip` | |
| `dateFilter` | |
| `allowBulkDelete` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-list>
    <!-- content -->
</sw-promotion-v2-list>
```

## sw-promotion-v2-sales-channel-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| promotion | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getChangeset` | |
| `getAssociationBySalesChannelId` | |
| `handleLocalMode` | |
| `handleWithRepository` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `promotionSalesChannelRepository` | |
| `salesChannelIds` | |
| `salesChannelCriteria` | |

### Examples

#### Example 1
Source: `sw-promotion-v2/view/sw-promotion-v2-conditions/sw-promotion-v2-conditions.html.twig`
```twig
<sw-promotion-v2-sales-channel-select
    class="sw-promotion-v2-conditions__sales-channel-selection"
    :promotion="promotion"
    :entity-collection="promotion.salesChannels"
    :disabled="!acl.can('promotion.editor')"
    :label="$tc('sw-promotion-v2.detail.conditions.preConditions.labelPromotionSalesChannel')"
    :placeholder="$tc('sw-promotion-v2.detail.conditions.preConditions.labelPromotionSalesChannel')"
/>
{% endblock %}

{% block sw_promotion_v2_conditions_pre_conditions_prevent_combination %}

<mt-switch
    v-model="promotion.preventCombination"
    class="sw-promotion-v2-conditions__prevent-combination"
```

## sw-promotion-v2-settings-discount-type

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| discount | `any` | — | yes |  |
| discountScope | `any` | — | yes |  |
| preselectedDiscountType | `any` | — | no |  |
| preselectedApplyDiscountTo | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getDiscountTypeSelection` | |
| `getApplyDiscountToSelection` | |
| `onClickAdvancedPrices` | |
| `clearAdvancedPrices` | |
| `setCurrencyForDiscountPrices` | |
| `prepareAdvancedPrices` | |
| `onMaxValueChanged` | |
| `onCloseAdvancedPricesModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isPercentageType` | |
| `labelValue` | |
| `showAdvancedPricesLink` | |
| `currencyPriceColumns` | |
| `currencyRepository` | |
| `advancedPricesRepo` | |
| `currencyCriteria` | |
| `showMaxValueAdvancedPrices` | |
| `discountTypeOptions` | |
| `applierOptions` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-settings-discount-type
    discount="..."
    discountScope="..."
>
    <!-- content -->
</sw-promotion-v2-settings-discount-type>
```

## sw-promotion-v2-settings-rule-selection

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| discount | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `ruleCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-settings-rule-selection
    discount="..."
>
    <!-- content -->
</sw-promotion-v2-settings-rule-selection>
```

## sw-promotion-v2-settings-trigger

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| discount | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `getTriggerSelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `ruleCriteria` | |
| `triggerOptions` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-settings-trigger
    discount="..."
>
    <!-- content -->
</sw-promotion-v2-settings-trigger>
```

## sw-promotion-v2-wizard-description

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Examples

#### Example 1
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-wizard-shipping-discount-trigger/sw-promotion-v2-wizard-shipping-discount-trigger.html.twig`
```twig
<sw-promotion-v2-wizard-description>
    {{ $tc('sw-promotion-v2.detail.shipping-discount-trigger.description') }}
</sw-promotion-v2-wizard-description>
```

#### Example 2
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-rule-selection/sw-promotion-v2-settings-rule-selection.html.twig`
```twig
<sw-promotion-v2-wizard-description class="sw-promotion-v2-settings-rule-selection__description">
    {{ $tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.description') }}
</sw-promotion-v2-wizard-description>
```

#### Example 3
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-wizard-discount-selection/sw-promotion-v2-wizard-discount-selection.html.twig`
```twig
<sw-promotion-v2-wizard-description>
    {{ $tc('sw-promotion-v2.detail.discount-selection.description') }}
</sw-promotion-v2-wizard-description>
```

#### Example 4
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-trigger/sw-promotion-v2-settings-trigger.html.twig`
```twig
<sw-promotion-v2-wizard-description
    class="sw-promotion-v2-settings-trigger-settings__description"
>
    {{ $tc('sw-promotion-v2.detail.discounts.wizard.shipping-discount.description') }}
</sw-promotion-v2-wizard-description>
```

## sw-promotion-v2-wizard-discount-selection

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-selection | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getSelectionOptions` | |
| `onChangeSelection` | |

### Examples

#### Basic Usage
```twig
<sw-promotion-v2-wizard-discount-selection>
    <!-- content -->
</sw-promotion-v2-wizard-discount-selection>
```

## sw-property-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-property-create>
    <!-- content -->
</sw-property-create>
```

## sw-property-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| propertyGroup | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| allowEdit | `any` | `true` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `propertyGroupNameError` | |
| `propertyGroupDisplayTypeError` | |
| `propertyGroupSortingTypeError` | |
| `displayTypeOptions` | |
| `sortingTypeOptions` | |

### Examples

#### Example 1
Source: `sw-property/page/sw-property-detail/sw-property-detail.html.twig`
```twig
<sw-property-detail-base
    v-if="propertyGroup"
    :property-group="propertyGroup"
    :allow-edit="acl.can('property.editor')"
/>
{% endblock %}

{% block sw_property_detail_content_option_list %}
<sw-property-option-list
    v-if="propertyGroup"
    ref="optionListing"
    :is-loading="isLoading || undefined"
    :option-repository="optionRepository"
    :property-group="propertyGroup"
/>
```

## sw-property-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| groupId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `saveFinish` | |
| `saveOnLanguageChange` | |
| `abortOnLanguageChange` | |
| `onChangeLanguage` | |
| `onSave` | |
| `onCancel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `optionRepository` | |
| `propertyRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `defaultCriteria` | |
| `useNaturalSorting` | |
| `showCustomFields` | |

### Examples

#### Example 1
Source: `sw-property/page/sw-property-detail/sw-property-detail.html.twig`
```twig
<sw-property-detail-base
    v-if="propertyGroup"
    :property-group="propertyGroup"
    :allow-edit="acl.can('property.editor')"
/>
{% endblock %}

{% block sw_property_detail_content_option_list %}
<sw-property-option-list
    v-if="propertyGroup"
    ref="optionListing"
    :is-loading="isLoading || undefined"
    :option-repository="optionRepository"
    :property-group="propertyGroup"
/>
```

## sw-property-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onDelete` | |
| `onCloseDeleteModal` | |
| `usePropertyCriteria` | |
| `onConfirmDelete` | |
| `onChangeLanguage` | |
| `getList` | |
| `getPropertyColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `propertyRepository` | |
| `defaultCriteria` | |
| `useNaturalSorting` | |
| `productRepository` | |

### Examples

#### Basic Usage
```twig
<sw-property-list>
    <!-- content -->
</sw-property-list>
```

## sw-property-option-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentOption | `any` | — | no |  |
| allowEdit | `any` | `true` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| cancel-option-edit | — | |
| save-option-edit | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `onCancel` | |
| `onSave` | |
| `successfulUpload` | |
| `removeMedia` | |
| `setMedia` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `colorHexCode` | |
| `modalTitle` | |
| `currentOptionNameError` | |
| `showCustomFields` | |

### Examples

#### Example 1
Source: `sw-property/component/sw-property-option-list/sw-property-option-list.html.twig`
```twig
    <sw-property-option-detail
        v-if="currentOption"
        :current-option="currentOption"
        :allow-edit="acl.can('property.editor')"
        @save-option-edit="onSaveOption"
        @cancel-option-edit="onCancelOption"
    />
    {% endblock %}

    {% block sw_property_option_list_loader %}
    <sw-loader v-if="isLoading" />
    {% endblock %}
</mt-card>
{% endblock %}

```

## sw-property-option-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| propertyGroup | `any` | — | yes |  |
| optionRepository | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `onSearch` | |
| `onGridSelectionChanged` | |
| `onOptionDelete` | |
| `onSingleOptionDelete` | |
| `onDeleteOptions` | |
| `onAddOption` | |
| `onCancelOption` | |
| `onSaveOption` | |
| `saveGroupLocal` | |
| `saveGroupRemote` | |
| `refreshOptionList` | |
| `onOptionEdit` | |
| `getGroupColumns` | |
| `checkEmptyState` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isSystemLanguage` | |
| `currentLanguage` | |
| `allowInlineEdit` | |
| `tooltipAdd` | |
| `disableAddButton` | |
| `useNaturalNameSorting` | |
| `dataSource` | |

### Examples

#### Example 1
Source: `sw-property/page/sw-property-detail/sw-property-detail.html.twig`
```twig
                <sw-property-option-list
                    v-if="propertyGroup"
                    ref="optionListing"
                    :is-loading="isLoading || undefined"
                    :option-repository="optionRepository"
                    :property-group="propertyGroup"
                />
                {% endblock %}

                {% block sw_property_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-property-detail"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                >
```

## sw-property-search

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| collapsible | `any` | `true` | no |  |
| overlay | `any` | `true` | no |  |
| options | `any` | — | yes |  |
| isAddOnly | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| toolbar | focus: onFocusSearch, input: onSearchOptions | |
| toolbar-search-field | — | |
| toolbar-items | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| option-select | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `selectGroup` | |
| `onOptionSelect` | |
| `onGroupPageChange` | |
| `onOptionPageChange` | |
| `onOptionSearchPageChange` | |
| `onFocusSearch` | |
| `onSearchOptions` | |
| `closeOnClickOutside` | |
| `selectOptions` | |
| `showSearch` | |
| `showTree` | |
| `loadGroups` | |
| `loadOptions` | |
| `sortOptions` | |
| `refreshSelection` | |
| `addOptionCount` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `swPropertySearchClasses` | |
| `propertyGroupRepository` | |
| `propertyGroupCriteria` | |
| `propertyGroupOptionRepository` | |
| `propertyGroupOptionCriteria` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-product/component/sw-product-add-properties-modal/sw-product-add-properties-modal.html.twig`
```twig
<sw-property-search
    ref="propertySearch"
    class="sw-product-add-properties-modal__search"
    :options="newProperties"
    :overlay="false"
    :collapsible="false"
    @option-select="onSelectOption"
>
    <template
        #toolbar="{ focus, input, searchTerm }"
    >
        {% block sw_property_search_field %}
        <div class="sw-property-search__toolbar sw-product-add-properties-modal__toolbar">
            <slot name="toolbar">
                <div class="sw-property-search__search-field-container">
```

## sw-provide

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-provide>
    <!-- content -->
</sw-provide>
```

## sw-purchase-price-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| price | `any` | — | yes |  |
| compact | `any` | `false` | no |  |
| taxRate | `any` | — | yes |  |
| error | `any` | `null` | no |  |
| label | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| currency | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `purchasePriceChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `purchasePrice` | |

### Examples

#### Basic Usage
```twig
<sw-purchase-price-field
    price="..."
    taxRate="..."
>
    <!-- content -->
</sw-purchase-price-field>
```

## sw-radio-field

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| bordered | `any` | `false` | no |  |
| block | `any` | `false` | no |  |
| description | `any` | `null` | no |  |
| options | `any` | — | no |  |
| value | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| `custom-field-${option.value}` | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |
| `currentIndex` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
        <sw-radio-field
            :value="checkBox"
            :name="radioButtonName"
            :options="[{ value: item.enabled }]"
            :disabled="!acl.can('country.editor') || undefined"
            @update:value="onChangeBaseCurrency(item)"
        />
    </template>
    {% endblock %}

    {% block sw_settings_country_currency_dependent_column_actions %}
    <template #actions="{ item }">

        {% block sw_settings_country_currency_dependent_grid_column_action_delete %}
        <sw-context-menu-item
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-search-behaviour/sw-settings-search-search-behaviour.html.twig`
```twig
<sw-radio-field
    v-model:value="searchBehaviourConfigs.andLogic"
    v-tooltip="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('product_search_config.editor'),
        showOnDisabledElements: true
    }"
    name="sw-field--searchBehaviourConfigs-andLogic"
    class="sw-settings-search__search-behaviour-condition"
    block
    :disabled="!acl.can('product_search_config.editor')"
    :options="conditionsOptions"
/>
{% endblock %}

```

#### Example 3
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
    <sw-radio-field
        v-model:value="selectedFeatureType"
        :label="$tc('sw-settings-product-feature-sets.modal.labelTitlePageOne')"
        block
        class="sw-settings-product-feature-sets-modal__options"
        identification="fieldType"
        :options="settingOptions"
        @update:value="onChangeOption"
    />
</template>
{% endblock %}

{% block sw_settings_product_feature_sets_modal_custom_field_list %}
<template v-if="showCustomField">

```

#### Example 4
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
    <sw-radio-field
        :disabled="disabled"
        :value="item.visibility"
        :name="'visibility' + item.id"
        :options="[{ value: 30 }]"
        @update:value="changeVisibilityValue($event, item)"
    />
</sw-grid-column>
{% endblock %}

{% block sw_settings_listing_visibility_detail_columns_search_only %}
<sw-grid-column
    :label="$tc('sw-product.visibility.columnSearchOnly')"
    flex="0.7fr"
    align="left"
```

#### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-visibility-detail/sw-settings-listing-visibility-detail.html.twig`
```twig
            <sw-radio-field
                type="radio"
                :disabled="disabled"
                :value="item.visibility"
                :name="'visibility' + item.id"
                :options="[{ value: 10 }]"
                @update:value="changeVisibilityValue($event, item)"
            />
        </sw-grid-column>
        {% endblock %}
    </template>
    {% endblock %}

    {% block sw_settings_listing_visibility_detail_pagination %}
    <template #pagination>
```

## sw-radio-panel

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| modelValue | `any` | — | no |  |
| title | `any` | `''` | no |  |
| description | `any` | `''` | no |  |
| icon | `any` | `''` | no |  |
| id | `any` | — | no |  |
| name | `any` | `null` | no |  |
| required | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| truncate | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:modelValue | — | |

### Methods

| Method | Description |
|--------|-------------|
| `toggle` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `checked` | |

### Examples

#### Basic Usage
```twig
<sw-radio-panel>
    <!-- content -->
</sw-radio-panel>
```

## sw-range-filter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| property | `any` | — | yes |  |
| isShowDivider | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| from-field | — | |
| divider | — | |
| to-field | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| filter-update | — | |

### Methods

| Method | Description |
|--------|-------------|
| `updateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-range-filter
    value="..."
    property="..."
>
    <!-- content -->
</sw-range-filter>
```

## sw-rating-stars

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | yes |  |
| maxStars | `any` | `5` | no |  |
| iconSize | `any` | `16` | no |  |
| displayFractions | `any` | `4` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `ratingTooltip` | |
| `cappedValue` | |
| `partialStarCutStyle` | |
| `dynamicWidthStyle` | |

### Examples

#### Example 1
Source: `sw-review/page/sw-review-detail/sw-review-detail.html.twig`
```twig
                    <sw-rating-stars
                        :value="review.points"
                        class="star-count-display"
                    />

                    <div class="star-count-description">
                        {{ $tc(`sw-review.detail.review${Math.round(stars)}PointRatingText`) }}
                    </div>
                </div>
            </div>

            {% endblock %}
            {% endblock %}
        </div>
        {% endblock %}
```

#### Example 2
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
<sw-rating-stars :value="item.points" />
```

#### Example 3
Source: `sw-product/view/sw-product-detail-reviews/sw-product-detail-reviews.html.twig`
```twig
<sw-rating-stars :value="item.points" />
```

## sw-review-detail

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `onSave` | |
| `onSaveFinish` | |
| `onCancel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `repository` | |
| `stars` | |
| `languageCriteria` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `showCustomFields` | |
| `dateFilter` | |
| `emailIdnFilter` | |

### Examples

#### Basic Usage
```twig
<sw-review-detail>
    <!-- content -->
</sw-review-detail>
```

## sw-review-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `updateCriteria` | |
| `onDelete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `listFilterOptions` | |
| `listFilters` | |
| `salesChannelCriteria` | |
| `languageCriteria` | |
| `customerCriteria` | |
| `productCriteria` | |
| `columns` | |
| `repository` | |
| `criteria` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-review-list>
    <!-- content -->
</sw-review-list>
```

## sw-rule-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| allowedRuleScopes | `any` | `null` | no |  |
| ruleAwareGroupKey | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save | — | |
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadConditionData` | |
| `conditionsChanged` | |
| `getChildrenConditions` | |
| `validateRuleAwareness` | |
| `saveAndClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `ruleRepository` | |
| `ruleConditionRepository` | |
| `appScriptConditionRepository` | |
| `modalTitle` | |
| `ruleNameError` | |
| `rulePriorityError` | |

### Examples

#### Basic Usage
```twig
<sw-rule-modal>
    <!-- content -->
</sw-rule-modal>
```

## sw-sales-channel-config

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| domain | `any` | `''` | no |  |
| value | `any` | — | no |  |
| criteria | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| select | — | |
| content | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| salesChannelChanged | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `readAll` | |
| `onInput` | |
| `save` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `actualConfigData` | |
| `salesChannelRepository` | |

### Examples

#### Basic Usage
```twig
<sw-sales-channel-config>
    <!-- content -->
</sw-sales-channel-config>
```

## sw-sales-channel-create-base

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-sales-channel-create-base>
    <!-- content -->
</sw-sales-channel-create-base>
```

## sw-sales-channel-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setMeasurementUnits` | |
| `saveFinish` | |
| `onSave` | |
| `getMeasurementUnits` | |
| `ensureDefaultLanguageInCollection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `allowSaving` | |

### Examples

#### Basic Usage
```twig
<sw-sales-channel-create>
    <!-- content -->
</sw-sales-channel-create>
```

## sw-sales-channel-defaults-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | `null` | no |  |
| propertyName | `any` | — | yes |  |
| propertyLabel | `any` | — | yes |  |
| defaultPropertyName | `any` | — | yes |  |
| defaultPropertyLabel | `any` | — | yes |  |
| propertyNameInDomain | `any` | `null` | no |  |
| helpText | `any` | `null` | no |  |
| disabled | `any` | `false` | no |  |
| criteria | `any` | — | no |  |
| disabledTooltipMessage | `any` | `''` | no |  |
| shouldShowActiveState | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `updateCollection` | |
| `getNotInCollection` | |
| `addItem` | |
| `removeItem` | |
| `getDomainUsingValue` | |
| `updateDefault` | |
| `isDisabledItem` | |
| `getActiveIconColor` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `propertyCollection` | |
| `defaultId` | |
| `propertyEntityName` | |
| `propertyNameKebabCase` | |
| `multiSelectClass` | |
| `singleSelectClass` | |
| `defaultsValueError` | |
| `labelProperty` | |
| `showClearableButtonForDefault` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-defaults-select
    v-if="!isProductComparison"
    :sales-channel="salesChannel"
    property-name="countries"
    :property-label="$tc('sw-sales-channel.detail.labelInputCountries')"
    :help-text="$tc('sw-sales-channel.detail.countryMultiSelectHelpText')"
    default-property-name="countryId"
    :criteria="countryCriteria"
    :disabled="!acl.can('sales_channel.editor') || undefined"
    :default-property-label="$tc('sw-sales-channel.detail.labelInputDefaultCountry')"
    :disabled-tooltip-message="$tc('sw-sales-channel.detail.tooltipDisabledCountry')"
    should-show-active-state
/>
{% endblock %}

```

#### Example 2
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-defaults-select
    v-if="!isProductComparison"
    :sales-channel="salesChannel"
    property-name="paymentMethods"
    :criteria="paymentMethodCriteria"
    :property-label="$tc('sw-sales-channel.detail.labelInputPaymentMethods')"
    default-property-name="paymentMethodId"
    :disabled="!acl.can('sales_channel.editor') || undefined"
    :default-property-label="$tc('sw-sales-channel.detail.labelInputDefaultPaymentMethod')"
    :disabled-tooltip-message="$tc('sw-sales-channel.detail.tooltipDisabledPaymentMethod')"
    should-show-active-state
/>
{% endblock %}

{% block sw_sales_channel_detail_base_disabled_shipping_methods_warning %}
```

## sw-sales-channel-detail-analytics

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| salesChannel | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createAnalyticsData` | |

### Examples

#### Basic Usage
```twig
<sw-sales-channel-detail-analytics
    salesChannel="..."
>
    <!-- content -->
</sw-sales-channel-detail-analytics>
```

## sw-sales-channel-detail-base

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| productExport | `any` | — | yes |  |
| storefrontSalesChannelCriteria | `any` | — | no |  |
| customFieldSets | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| productComparisonAccessUrl | `any` | `''` | no |  |
| templateOptions | `any` | — | no |  |
| showTemplateModal | `any` | `false` | no |  |
| templateName | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| template-selected | — | |
| template-modal-close | — | |
| template-modal-confirm | — | |
| invalid-file-name | — | |
| valid-file-name | — | |
| access-key-changed | — | |
| domain-changed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onGenerateKeys` | |
| `onGenerateProductExportKey` | |
| `onToggleActive` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `deleteSalesChannel` | |
| `extractFkInfo` | |
| `copyToClipboard` | |
| `onStorefrontSelectionChange` | |
| `onStorefrontDomainSelectionChange` | |
| `loadStorefrontDomains` | |
| `onChangeFileName` | |
| `onChangeFileNameDebounce` | |
| `changeInterval` | |
| `createCategoryCollections` | |
| `createCategoriesCollection` | |
| `onMainSelectionAdd` | |
| `onMainSelectionRemove` | |
| `onFooterSelectionAdd` | |
| `onFooterSelectionRemove` | |
| `onServiceSelectionAdd` | |
| `onServiceSelectionRemove` | |
| `buildDisabledPaymentAlert` | |
| `buildDisabledShippingAlert` | |
| `buildUnservedLanguagesAlert` | |
| `isFavorite` | |
| `validateMaintenanceIpCidr` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `secretAccessKeyFieldType` | |
| `isStorefront` | |
| `isDomainAware` | |
| `salesChannelRepository` | |
| `isProductComparison` | |
| `isHeadlessSalesChannel` | |
| `storefrontSalesChannelDomainCriteria` | |
| `storefrontSalesChannelCurrencyCriteria` | |
| `paymentMethodCriteria` | |
| `countryCriteria` | |
| `languageCriteria` | |
| `disabledCountries` | |
| `disabledCountryVariant` | |
| `disabledPaymentMethods` | |
| `disabledPaymentMethodVariant` | |
| `disabledShippingMethods` | |
| `disabledShippingMethodVariant` | |
| `unservedLanguages` | |
| `unservedLanguageVariant` | |
| `storefrontDomainsLoaded` | |
| `domainRepository` | |
| `globalDomainRepository` | |
| `productExportRepository` | |
| `mainNavigationCriteria` | |
| `getIntervalOptions` | |
| `getFileFormatOptions` | |
| `getEncodingOptions` | |
| `invalidFileNameError` | |
| `helpTextTaxCalculation` | |
| `taxCalculationTypeOptions` | |
| `maintenanceIpAllowlist` | |
| `salesChannelNameError` | |
| `salesChannelCustomerGroupIdError` | |
| `salesChannelNavigationCategoryIdError` | |
| `productExportProductStreamIdError` | |
| `productExportEncodingError` | |
| `productExportFileNameError` | |
| `productExportFileFormatError` | |
| `productExportStorefrontSalesChannelIdError` | |
| `productExportSalesChannelDomainIdError` | |
| `productExportCurrencyIdError` | |
| `categoryRepository` | |
| `mainCategoryCriteria` | |
| `footerCategoryCriteria` | |
| `serviceCategoryCriteria` | |
| `mainCategories` | |
| `footerCategories` | |
| `serviceCategories` | |
| `navigationCategoryPlaceholder` | |
| `footerCategoryPlaceholder` | |
| `serviceCategoryPlaceholder` | |
| `salesChannelFavoritesService` | |
| `currencyCriteria` | |
| `shippingMethodCriteria` | |
| `productStreamCriteria` | |
| `dateFilter` | |
| `cliCommand` | |
| `templateSelectOptions` | |

### Examples

#### Basic Usage
```twig
<sw-sales-channel-detail-base
    salesChannel="..."
    productExport="..."
>
    <!-- content -->
</sw-sales-channel-detail-base>
```

## sw-sales-channel-detail-domains

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| disableEdit | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `sortColumns` | |
| `unicodeUriFilter` | |
| `localSortDomains` | |
| `getSortValue` | |
| `onInput` | |
| `verifyUrl` | |
| `domainExistsLocal` | |
| `isOriginalUrl` | |
| `domainExistsInDatabase` | |
| `setCurrentDomainBackup` | |
| `resetCurrentDomainToBackup` | |
| `setInitialCurrency` | |
| `setInitialLanguage` | |
| `setInitialMeasurementUnits` | |
| `onClickOpenCreateDomainModal` | |
| `onClickAddNewDomain` | |
| `onClickEditDomain` | |
| `onCloseCreateDomainModal` | |
| `onClickDeleteDomain` | |
| `onConfirmDeleteDomain` | |
| `onCloseDeleteDomainModal` | |
| `onLanguageSelect` | |
| `onCurrencySelect` | |
| `onOptionSelect` | |
| `getDomainColumns` | |
| `getMeasurementName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `domainRepository` | |
| `currentDomainModalTitle` | |
| `currentDomainModalButtonText` | |
| `snippetSetCriteria` | |
| `salesChannelFilterCriteria` | |
| `currencyCriteria` | |
| `hreflangLocalisationOptions` | |
| `disabled` | |
| `sortedDomains` | |
| `measurementSystemRepository` | |
| `measurementSystemCriteria` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-detail-domains
    v-if="salesChannel && isDomainAware"
    :sales-channel="salesChannel"
    :disable-edit="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
{% endblock %}

{% block sw_sales_channel_detail_base_general_input_product_comparison_storefront %}
<mt-card
    v-if="salesChannel && isProductComparison"
    position-identifier="sw-sales-channel-detail-base-general-input-product-comparison-storefront"
    :is-loading="isLoading"
    :title="$tc('sw-sales-channel.detail.productComparison.storefront')"
>
```

## sw-sales-channel-detail-hreflang

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `domainCriteria` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-detail-hreflang
    v-if="salesChannel && isStorefront"
    :sales-channel="salesChannel"
    :disabled="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
{% endblock %}

{% block sw_sales_channel_detail_base_options_domains %}
<sw-sales-channel-detail-domains
    v-if="salesChannel && isDomainAware"
    :sales-channel="salesChannel"
    :disable-edit="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
```

## sw-sales-channel-detail-product-comparison-preview

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| content | `any` | `null` | no |  |
| errors | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onModalClose` | |
| `navigateToLine` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `editorConfig` | |
| `displayErrors` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-product-comparison/sw-sales-channel-detail-product-comparison.html.twig`
```twig
            <sw-sales-channel-detail-product-comparison-preview
                :content="previewContent"
                :errors="previewErrors"
                @close="onPreviewClose"
            />
            {% endblock %}
        </div>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```

## sw-sales-channel-detail-product-comparison

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| productExport | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `validateTemplate` | |
| `preview` | |
| `outerCompleterFunction` | |
| `onPreviewClose` | |
| `resetValid` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `editorConfig` | |
| `productExportRepository` | |
| `domainRepository` | |
| `salesChannelRepository` | |
| `mainNavigationCriteria` | |
| `outerCompleterFunctionHeader` | |
| `outerCompleterFunctionBody` | |
| `outerCompleterFunctionFooter` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-product-comparison/sw-sales-channel-detail-product-comparison.html.twig`
```twig
            <sw-sales-channel-detail-product-comparison-preview
                :content="previewContent"
                :errors="previewErrors"
                @close="onPreviewClose"
            />
            {% endblock %}
        </div>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```

## sw-sales-channel-detail-products

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getProducts` | |
| `onDeleteProduct` | |
| `onDeleteProducts` | |
| `getDeleteId` | |
| `showNotificationError` | |
| `onChangePage` | |
| `onChangeSearchTerm` | |
| `openAddProductsModal` | |
| `onAddProducts` | |
| `saveProductVisibilities` | |
| `isProductRemovable` | |
| `onProductSelectionChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productVisibilityRepository` | |
| `productCriteria` | |
| `productColumns` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-sales-channel-detail-products>
    <!-- content -->
</sw-sales-channel-detail-products>
```

## sw-sales-channel-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadSalesChannel` | |
| `getLoadSalesChannelCriteria` | |
| `onTemplateSelected` | |
| `onTemplateModalClose` | |
| `onTemplateModalConfirm` | |
| `loadCustomFieldSets` | |
| `generateAccessUrl` | |
| `loadProductExportTemplates` | |
| `saveFinish` | |
| `setInvalidFileName` | |
| `onSave` | |
| `updateAnalytics` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `productExport` | |
| `isStorefront` | |
| `isProductComparison` | |
| `isHeadless` | |
| `salesChannelRepository` | |
| `salesChannelAnalyticsRepository` | |
| `customFieldRepository` | |
| `productExportRepository` | |
| `storefrontSalesChannelCriteria` | |
| `tooltipSave` | |
| `allowSaving` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
<sw-sales-channel-detail-hreflang
    v-if="salesChannel && isStorefront"
    :sales-channel="salesChannel"
    :disabled="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
{% endblock %}

{% block sw_sales_channel_detail_base_options_domains %}
<sw-sales-channel-detail-domains
    v-if="salesChannel && isDomainAware"
    :sales-channel="salesChannel"
    :disable-edit="!acl.can('sales_channel.editor') || undefined"
    :is-loading="isLoading"
/>
```

#### Example 2
Source: `sw-sales-channel/view/sw-sales-channel-detail-product-comparison/sw-sales-channel-detail-product-comparison.html.twig`
```twig
            <sw-sales-channel-detail-product-comparison-preview
                :content="previewContent"
                :errors="previewErrors"
                @close="onPreviewClose"
            />
            {% endblock %}
        </div>
        {% endblock %}
    </mt-card>
    {% endblock %}
</div>
{% endblock %}

```

## sw-sales-channel-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onAddSalesChannel` | |
| `getList` | |
| `checkForDomainLink` | |
| `openStorefrontLink` | |
| `isFavorite` | |
| `isStorefrontSalesChannel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelColumns` | |
| `salesChannelRepository` | |
| `salesChannelCriteria` | |
| `salesChannelFavoritesService` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-sales-channel-list>
    <!-- content -->
</sw-sales-channel-list>
```

## sw-sales-channel-measurement

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| labelUnitSystem | `any` | — | no |  |
| labelLengthUnit | `any` | — | no |  |
| labelWeightUnit | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| measurement-system-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onMeasurementSystemChange` | |
| `formatUnitLabel` | |
| `getDefaultMeasurementSystems` | |
| `getUnitOptionsByType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `measurementSystemRepository` | |
| `measurementSystemCriteria` | |
| `unitSystemLabel` | |
| `dimensionUnitLabel` | |
| `weightUnitLabel` | |
| `measurementUnits` | |
| `measurementSystemOptions` | |
| `lengthUnitOptions` | |
| `weightUnitOptions` | |
| `defaultLengthUnit` | |
| `defaultWeightUnit` | |
| `measurementUnitSystemError` | |
| `measurementLengthUnitError` | |
| `measurementWeightUnitError` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-detail-domains/sw-sales-channel-detail-domains.html.twig`
```twig
<sw-sales-channel-measurement
    :sales-channel="currentDomain"
    :label-unit-system="$tc('sw-sales-channel.detail.measurementSystem.labelUnitSystem')"
    :label-length-unit="$tc('sw-sales-channel.detail.measurementSystem.labelLengthUnit')"
    :label-weight-unit="$tc('sw-sales-channel.detail.measurementSystem.labelWeightUnit')"
/>

{% block sw_sales_channel_detail_domains_hreflang %}
<sw-radio-field
    v-model:value="currentDomain.hreflangUseOnlyLocale"
    :label="$tc('sw-sales-channel.detail.hreflang.domainSettings.label')"
    identification="hreflang"
    :options="hreflangLocalisationOptions"
/>
{% endblock %}
```

#### Example 2
Source: `sw-sales-channel/view/sw-sales-channel-detail-base/sw-sales-channel-detail-base.html.twig`
```twig
    <sw-sales-channel-measurement
        v-if="!isProductComparison"
        :sales-channel="salesChannel"
        :label-unit-system="$tc('sw-sales-channel.detail.measurementSystem.labelDefaultUnitSystem')"
        :label-length-unit="$tc('sw-sales-channel.detail.measurementSystem.labelDefaultLengthUnit')"
        :label-weight-unit="$tc('sw-sales-channel.detail.measurementSystem.labelDefaultWeightUnit')"
    />
</mt-card>
{% endblock %}

{% block sw_sales_channel_shipping_payment %}
<mt-card
    v-if="salesChannel"
    position-identifier="sw-sales-channel-detail-base-shipping-payment"
    :is-loading="isLoading"
```

## sw-sales-channel-menu

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerListener` | |
| `destroyedComponent` | |
| `getDomainLink` | |
| `loadEntityData` | |
| `openSalesChannelModal` | |
| `openStorefrontLink` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `canCreateSalesChannels` | |
| `salesChannelCriteria` | |
| `moreSalesChannelAvailable` | |
| `buildMenuTree` | |
| `moreItemsEntry` | |
| `salesChannelFavoritesService` | |
| `salesChannelFavorites` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/structure/sw-admin-menu-extension/sw-admin-menu-extension.html.twig`
```twig
<sw-sales-channel-menu v-if="canViewSalesChannels" />
```

## sw-sales-channel-modal-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| detailType | `any` | `null` | no |  |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal/sw-sales-channel-modal.html.twig`
```twig
<sw-sales-channel-modal-detail
    v-else
    :detail-type="detailType"
/>
{% endblock %}

{% block sw_sales_channel_modal_footer %}
<template #modal-footer>
    <a
        href="#"
        class="sw-sales-channel-modal__footer_left"
        @click.prevent="openRoute({ name: 'sw.sales.channel.list' })"
    >
        {{ $tc('sw-sales-channel.general.manageSalesChannels') }}
    </a>
```

## sw-sales-channel-modal-grid

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productStreamsExist | `any` | `true` | no |  |
| productStreamsLoading | `any` | `false` | no |  |
| addChannelAction | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| grid-channel-add | — | |
| grid-detail-open | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddChannel` | |
| `onOpenDetail` | |
| `isProductComparisonSalesChannelType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelTypeRepository` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal/sw-sales-channel-modal.html.twig`
```twig
<sw-sales-channel-modal-grid
    v-if="!detailType"
    :product-streams-exist="productStreamsExist"
    :product-streams-loading="productStreamsLoading"
    :add-channel-action="addChannelAction"
    @grid-detail-open="onGridOpenDetails"
    @grid-channel-add="onAddChannel"
/>
{% endblock %}

{% block sw_sales_channel_modal_detail %}
<sw-sales-channel-modal-detail
    v-else
    :detail-type="detailType"
/>
```

## sw-sales-channel-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onGridOpenDetails` | |
| `onCloseModal` | |
| `onAddChannel` | |
| `openRoute` | |
| `isProductComparisonSalesChannelType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `productStreamRepository` | |
| `addChannelAction` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-modal/sw-sales-channel-modal.html.twig`
```twig
<sw-sales-channel-modal-grid
    v-if="!detailType"
    :product-streams-exist="productStreamsExist"
    :product-streams-loading="productStreamsLoading"
    :add-channel-action="addChannelAction"
    @grid-detail-open="onGridOpenDetails"
    @grid-channel-add="onAddChannel"
/>
{% endblock %}

{% block sw_sales_channel_modal_detail %}
<sw-sales-channel-modal-detail
    v-else
    :detail-type="detailType"
/>
```

#### Example 2
Source: `sw-sales-channel/component/structure/sw-sales-channel-menu/sw-sales-channel-menu.html.twig`
```twig
<sw-sales-channel-modal
    v-if="showModal"
    @modal-close="showModal=false"
/>
{% endblock %}

{% block sw_sales_channel_menu_headline %}
<div class="sw-admin-menu__headline">
    {% block sw_sales_channel_menu_headline_text %}
    <div class="collapsible-text sw-admin-menu__headline_text">
        <router-link
            :to="{ name: 'sw.sales.channel.list' }"
        >{{ $tc('sw-sales-channel.general.titleMenuItems') }}</router-link>
    </div>
    {% endblock %}
```

## sw-sales-channel-product-assignment-categories

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| containerStyle | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |
| product-loading | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSearchTermChange` | |
| `createdComponent` | |
| `categoryCriteria` | |
| `categorySearchCriteria` | |
| `getTreeItems` | |
| `onChangeSearchTerm` | |
| `onCheckItem` | |
| `removeItem` | |
| `searchCategories` | |
| `isSearchItemChecked` | |
| `onCheckSearchItem` | |
| `getBreadcrumb` | |
| `productCriteria` | |
| `getProductFromCategories` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `categoryRepository` | |
| `productRepository` | |
| `selectedCategoriesItemsIds` | |
| `selectedCategoriesPathIds` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-products-assignment-modal/sw-sales-channel-products-assignment-modal.html.twig`
```twig
                <sw-sales-channel-product-assignment-categories
                    ref="category"
                    v-hide="active === 'categories'"
                    :sales-channel="salesChannel"
                    :container-style="categoryContainerStyle"
                    @selection-change="onChangeSelection"
                    @product-loading="setProductLoading"
                />
                {% endblock %}

                {% block sw_sales_channel_products_assignment_modal_tab_content_dynamic_product_groups %}
                <sw-sales-channel-products-assignment-dynamic-product-groups
                    ref="productGroup"
                    v-hide="active === 'dynamicProductGroups'"
                    :sales-channel="salesChannel"
```

## sw-sales-channel-products-assignment-dynamic-product-groups

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| containerStyle | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |
| product-loading | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getProductStreams` | |
| `onSearch` | |
| `onPaginate` | |
| `onOpen` | |
| `onSelect` | |
| `getProductsFromProductStreams` | |
| `getProductStreamFilter` | |
| `getProducts` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productStreamRepository` | |
| `productCriteria` | |
| `productStreamCriteria` | |
| `productStreamColumns` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-products-assignment-modal/sw-sales-channel-products-assignment-modal.html.twig`
```twig
                <sw-sales-channel-products-assignment-dynamic-product-groups
                    ref="productGroup"
                    v-hide="active === 'dynamicProductGroups'"
                    :sales-channel="salesChannel"
                    :container-style="productGroupContainerStyle"
                    @selection-change="onChangeSelection"
                    @product-loading="setProductLoading"
                />
                {% endblock %}
            </div>
        </template>
    </sw-tabs>
    {% endblock %}
</template>

```

## sw-sales-channel-products-assignment-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| isAssignProductLoading | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| products-add | — | |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getProductContainerStyle` | |
| `getCategoryContainerStyle` | |
| `getProductGroupContainerStyle` | |
| `onChangeSelection` | |
| `onCloseModal` | |
| `onAddProducts` | |
| `setProductLoading` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productCount` | |
| `products` | |

### Examples

#### Example 1
Source: `sw-sales-channel/view/sw-sales-channel-detail-products/sw-sales-channel-detail-products.html.twig`
```twig
    <sw-sales-channel-products-assignment-modal
        v-if="showProductsModal"
        :sales-channel="salesChannel"
        :is-assign-product-loading="isAssignProductLoading"
        @modal-close="showProductsModal = false"
        @products-add="onAddProducts"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```

## sw-sales-channel-products-assignment-single-products

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannel | `any` | — | yes |  |
| containerStyle | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| selection-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getProducts` | |
| `onChangeSearchTerm` | |
| `onSelectionChange` | |
| `onChangePage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productCriteria` | |
| `productColumns` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-sales-channel/component/sw-sales-channel-products-assignment-modal/sw-sales-channel-products-assignment-modal.html.twig`
```twig
<sw-sales-channel-products-assignment-single-products
    ref="product"
    v-hide="active === 'singleProducts'"
    :sales-channel="salesChannel"
    :container-style="productContainerStyle"
    @selection-change="onChangeSelection"
/>
{% endblock %}

{% block sw_sales_channel_products_assignment_modal_tab_content_categories %}
<sw-sales-channel-product-assignment-categories
    ref="category"
    v-hide="active === 'categories'"
    :sales-channel="salesChannel"
    :container-style="categoryContainerStyle"
```

## sw-sales-channel-switch

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| abortChangeFunction | `any` | — | no |  |
| saveChangesFunction | `any` | — | no |  |
| label | `any` | `''` | no |  |
| salesChannelCriteria | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-sales-channel-id | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |
| `checkAbort` | |
| `emitChange` | |
| `onCloseChangesModal` | |
| `onClickSaveChanges` | |
| `onClickRevertUnsavedChanges` | |
| `changeToNewSalesChannel` | |

### Examples

#### Example 1
Source: `sw-settings/component/sw-system-config/sw-system-config.html.twig`
```twig
    <sw-sales-channel-switch
        :label="$tc('sw-settings.system-config.labelSalesChannelSelect')"
        @change-sales-channel-id="onSalesChannelChanged"
    />
</div>

{% block sw_system_config_content_card %}
<mt-card
    v-for="card, index in config"
    :key="index"
    position-identifier="sw-system-config-content"
    :class="`sw-system-config__card--${index}`"
    :is-loading="isLoading"
    :title="getInlineSnippet(card.title)"
>
```

#### Example 2
Source: `sw-settings-seo/component/sw-seo-url-template-card/sw-seo-url-template-card.html.twig`
```twig
    <sw-sales-channel-switch
        :label="$tc('sw-seo-url-template-card.general.labelSalesChannelSelect')"
        @change-sales-channel-id="onSalesChannelChanged"
    />
</template>

{% block sw_seo_url_template_card_info_box %}
<mt-banner
    variant="info"
    :title="$tc('sw-seo-url-template-card.general.headlineInfoMessageBoxEmptyProperties')"
>
    <span>{{ $tc('sw-seo-url-template-card.general.textInfoMessageBoxEmptyProperties') }}</span>
</mt-banner>
{% endblock %}

```

#### Example 3
Source: `sw-settings-seo/component/sw-seo-url/sw-seo-url.html.twig`
```twig
            <sw-sales-channel-switch
                ref="salesChannelSwitch"
                :disabled="disabled || undefined"
                :label="$tc('sw-seo-url.labelSalesChannelSelect')"
                @change-sales-channel-id="onSalesChannelChanged"
            />
        </template>
        {% endblock %}

        <div
            v-if="hasAdditionalSeoSlot"
            class="sw-seo-url__card-seo-additional"
        >
            <slot
                name="seo-additional"
```

## sw-search-bar-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| item | `any` | — | no |  |
| type | `any` | — | yes |  |
| index | `any` | — | yes |  |
| column | `any` | — | yes |  |
| searchTerm | `any` | `null` | no |  |
| entityIconColor | `any` | — | yes |  |
| entityIconName | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `registerEvents` | |
| `removeEvents` | |
| `checkActiveState` | |
| `onEnter` | |
| `onMouseEnter` | |
| `onClickSearchResult` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `searchTypes` | |
| `moduleManifest` | |
| `detailRoute` | |
| `displayValue` | |
| `componentClasses` | |
| `moduleName` | |
| `routeName` | |
| `iconName` | |
| `iconColor` | |
| `shortcut` | |
| `productDisplayName` | |
| `currentUser` | |
| `mediaNameFilter` | |

### Examples

#### Basic Usage
```twig
<sw-search-bar-item
    type="..."
    index="..."
>
    <!-- content -->
</sw-search-bar-item>
```

## sw-search-bar

> Global search bar component with auto-complete and module filtering.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialSearchType | `any` | `''` | no |  |
| typeSearchAlwaysInContainer | `any` | `false` | no |  |
| placeholder | `any` | `''` | no |  |
| initialSearch | `any` | `''` | no |  |
| entitySearchColor | `any` | `''` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| search-input | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| search | — | |
| active-item-index-select | — | |
| keyup-enter | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `registerListener` | |
| `onMouseOver` | |
| `registerActiveItemIndexSelectHandler` | |
| `unregisterActiveItemIndexSelectHandler` | |
| `registerKeyupEnterHandler` | |
| `unregisterKeyupEnterHandler` | |
| `getLabelSearchType` | |
| `setFocus` | |
| `closeOnClickOutside` | |
| `clearSearchTerm` | |
| `onFocusInput` | |
| `onBlur` | |
| `showSearchBar` | |
| `hideSearchBar` | |
| `showSearchFieldOnLargerViewports` | |
| `onSearchTermChange` | |
| `showTypeContainer` | |
| `filterTypeSelectResults` | |
| `onClickType` | |
| `setSearchType` | |
| `toggleOffCanvas` | |
| `resetSearchType` | |
| `doListSearch` | |
| `doListSearchWithContainer` | |
| `doGlobalSearch` | |
| `loadResults` | |
| `loadTypeSearchResults` | |
| `loadTypeSearchResultsByService` | |
| `setActiveResultPosition` | |
| `emitActiveResultPosition` | |
| `navigateUpResults` | |
| `navigateDownResults` | |
| `checkScrollPosition` | |
| `onKeyUpEnter` | |
| `getSearchTypeProperty` | |
| `getEntityIconName` | |
| `getEntityIconColor` | |
| `getEntityIcon` | |
| `isResultEmpty` | |
| `onMouseEnterSearchType` | |
| `onOpenModuleFiltersDropDown` | |
| `loadSalesChannelType` | |
| `getModuleEntities` | |
| `getDefaultMatchSearchableModules` | |
| `getSalesChannelTypesBySearchTerm` | |
| `toggleSearchPreferencesModal` | |
| `loadSearchTrends` | |
| `getFrequentlyUsedModules` | |
| `getRecentlySearch` | |
| `getInfoModuleFrequentlyUsed` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `searchBarFieldClasses` | |
| `placeholderSearchInput` | |
| `salesChannelRepository` | |
| `salesChannelTypeRepository` | |
| `salesChannelCriteria` | |
| `canCreateSalesChannels` | |
| `moduleRegistry` | |
| `searchableModules` | |
| `criteriaCollection` | |
| `currentUser` | |
| `showSearchTipForEsSearch` | |
| `adminEsEnable` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-list/sw-settings-country-list.html.twig`
```twig
    <sw-search-bar
        initial-search-type="country"
        :placeholder="$tc('sw-settings-country.general.placeholderSearchBar')"
        :initial-search="term"
        @search="onSearch"
    />
</template>
{% endblock %}

{% block sw_settings_country_list_smart_bar_header %}
<template #smart-bar-header>
    {% block sw_settings_country_list_smart_bar_header_title %}
    <h2>
        {% block sw_settings_country_list_smart_bar_header_title_text %}
        {{ $tc('sw-settings.index.title') }}
```

#### Example 2
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
    <sw-search-bar
        initial-search-type="Logs"
        :placeholder="$tc('sw-settings-logging.general.placeholderSearchBar')"
        :initial-search="term"
        @search="onSearch"
    />
</template>
{% endblock %}

{% block sw_settings_logging_list_smart_bar_header %}
<template #smart-bar-header>
    {% block sw_settings_logging_list_smart_bar_header_title %}
    <h2>
        {% block sw_settings_logging_list_smart_bar_header_title_text %}
        {{ $tc('sw-settings.index.title') }}
```

#### Example 3
Source: `sw-settings-salutation/page/sw-settings-salutation-list/sw-settings-salutation-list.html.twig`
```twig
    <sw-search-bar
        initial-search-type="salutation"
        :placeholder="$tc('sw-settings-salutation.general.placeholderSearchBar')"
        :initial-search="term"
        @search="onSearch"
    />
</template>
{% endblock %}

{% block sw_settings_salutation_list_smart_bar_header %}
<template #smart-bar-header>
    {% block sw_settings_salutation_list_smart_bar_header_title %}
    <h2>
        {% block sw_settings_salutation_list_smart_bar_header_title_text %}
        {{ $tc('sw-settings.index.title') }}
```

#### Example 4
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-search-bar />
```

#### Example 5
Source: `sw-bulk-edit/page/sw-bulk-edit-order/sw-bulk-edit-order.html.twig`
```twig
<sw-search-bar />
```

## sw-search-more-results

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| entity | `any` | `''` | yes |  |
| term | `any` | `null` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| content | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `moduleFactory` | |
| `searchTypeRoute` | |
| `searchTypes` | |
| `searchContent` | |

### Examples

#### Basic Usage
```twig
<sw-search-more-results
    entity="..."
>
    <!-- content -->
</sw-search-more-results>
```

## sw-search-preferences-modal

> Shopware Administration component.

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
| `getDataSource` | |
| `addEventListeners` | |
| `removeEventListeners` | |
| `getModuleName` | |
| `onChangeSearchPreference` | |
| `onClose` | |
| `onOpenSearchSettings` | |
| `onCancel` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `defaultSearchPreferences` | |
| `searchPreferencesColumns` | |

### Examples

#### Basic Usage
```twig
<sw-search-preferences-modal>
    <!-- content -->
</sw-search-preferences-modal>
```

## sw-select-base

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| showClearableButton | `any` | — | no |  |
| size | `any` | `'default'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-select-selection | — | |
| results-list | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| select-expanded | — | |
| select-collapsed | — | |
| clear | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onMounted` | |
| `onBeforeUnmount` | |
| `handleKeydown` | |
| `toggleExpand` | |
| `expand` | |
| `collapse` | |
| `focusPreviousFormElement` | |
| `listenToClickOutside` | |
| `computePath` | |
| `emitClear` | |
| `focusParentSelect` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `swFieldClasses` | |
| `isClearable` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-multi-snippet-drag-and-drop/sw-multi-snippet-drag-and-drop.html.twig`
```twig
<sw-select-base
    class="sw-multi-snippet-select"
    :is-loading="isLoading"
    :error="errorObject"
    v-bind="$attrs"
>
    <template #sw-select-selection="{ identification, error, disabled, size, expand, collapse }">
        <ul
            ref="selectionList"
            class="sw-select-selection-list"
        >
            <!-- eslint-disable vue/no-use-v-if-with-v-for -->
            <li
                v-for="(snippet, index) in value"
                :key="index"
```

#### Example 2
Source: `sw-settings-country/component/sw-settings-country-new-snippet-modal/sw-settings-country-new-snippet-modal.html.twig`
```twig
<sw-select-base
    class="sw-multi-snippet-select"
    :is-loading="isLoading"
    :error="null"
    v-bind="$attrs"
>
    <template #sw-select-selection="{ identification, error, disabled, size, expand, collapse }">
        <ul
            ref="selectionList"
            class="sw-select-selection-list"
        >
            <!-- eslint-disable vue/no-use-v-if-with-v-for -->
            <li
                v-for="(snippet, index) in selection"
                :key="index"
```

#### Example 3
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
<sw-select-base
    ref="selectBase"
    class="sw-import-export-entity-path-select"
    :is-loading="isLoading"
    v-bind="$attrs"
    @select-expanded="onSelectExpanded"
    @select-collapsed="onSelectCollapsed"
>
    {% block sw_import_export_entity_path_select_base %}
    {% block sw_import_export_entity_path_select_base_selection %}
    <template #sw-select-selection="{ identification, error, disabled, size, setFocusClass, removeFocusClass }">
        {% block sw_import_export_entity_path_select_base_selection_slot %}
        <div class="sw-import-export-entity-path-select__selection">
            {% block sw_import_export_entity_path_select_single_selection_inner %}
            {% block sw_import_export_entity_path_select_single_selection_inner_label %}
```

#### Example 4
Source: `sw-cms/component/sw-cms-product-assignment/sw-cms-product-assignment.html.twig`
```twig
<sw-select-base
    v-bind="$attrs"
    ref="selectBase"
    class="sw-cms-product-assignment-select"
    :disabled="disabled"
    :label="selectLabel"
    :is-loading="isLoadingResults"
    @select-expanded="onSelectExpanded"
    @select-collapsed="onSelectCollapsed"
>

    <template #sw-select-selection="{ identification, error, disabled, size, expand, collapse }">
        {% block sw_cms_product_assignment_search_field %}
        <input
            ref="searchInput"
```

#### Example 5
Source: `sw-settings-cache/page/sw-settings-cache-index/sw-settings-cache-index.html.twig`
```twig
<sw-select-base
    class="sw-settings-cache__indexers-select"
    :label="indexingMethod === 'skip' ? $tc('sw-settings-cache.section.indexesSkipSelectLabel') : $tc('sw-settings-cache.section.indexesOnlySelectLabel')"
    :disabled="processes.updateIndexes"
>
    <template #sw-select-selection>
        <sw-label
            v-for="(selection, index) in indexerSelection"
            :key="index"
            @dismiss="changeSelection(false, selection)"
        >
            {{ selection }}
        </sw-label>
        <sw-label
            ghost
```

## sw-select-field-deprecated

> **Deprecated in 6.7** — Use `mt-select` instead. Will be removed in 6.8.
> See mt-select for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-select-field>` | `<mt-select>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |
| placeholder | `any` | `null` | no |  |
| options | `any` | `null` | no |  |
| aside | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getOptionName` | |
| `onChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `locale` | |
| `fallbackLocale` | |
| `swFieldSelectClasses` | |
| `hasOptions` | |

### Examples

#### Basic Usage
```twig
<sw-select-field-deprecated>
    <!-- content -->
</sw-select-field-deprecated>
```

## sw-select-field

> **Migration wrapper** — Delegates to `mt-select` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-select for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `any` | — | no |  |
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

#### Basic Usage
```twig
<sw-select-field>
    <!-- content -->
</sw-select-field>
```

## sw-select-number-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

### Examples

#### Basic Usage
```twig
<sw-select-number-field>
    <!-- content -->
</sw-select-number-field>
```

## sw-select-option

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| index | `any` | — | yes |  |
| item | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| selected | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `registerEvents` | |
| `removeEvents` | |
| `emitActiveResultPosition` | |
| `onClicked` | |
| `checkActiveState` | |
| `selectOptionOnEnter` | |
| `isInSelections` | |
| `onMouseEnter` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `componentClasses` | |

### Examples

#### Basic Usage
```twig
<sw-select-option
    index="..."
    item="..."
>
    <!-- content -->
</sw-select-option>
```

## sw-select-result-list

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| options | `any` | — | no |  |
| emptyMessage | `any` | `null` | no |  |
| focusEl | `null \| null` | — | no |  |
| isLoading | `any` | `false` | no |  |
| popoverClasses | `any` | — | no |  |
| popoverResizeWidth | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| before-item-list | — | |
| result-item | — | |
| after-item-list | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-select | — | |
| active-item-change | — | |
| outside-click | — | |
| paginate | — | |
| item-select-by-keyboard | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyedComponent` | |
| `setActiveItemIndex` | |
| `addEventListeners` | |
| `removeEventListeners` | |
| `onItemSelect` | |
| `emitActiveItemIndex` | |
| `checkOutsideClick` | |
| `navigate` | |
| `navigateNext` | |
| `navigatePrevious` | |
| `updateScrollPosition` | |
| `emitClicked` | |
| `onScroll` | |
| `getBottomDistance` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `emptyMessageText` | |
| `popoverClass` | |

### Examples

#### Example 1
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
<sw-select-result-list
    ref="resultsList"
    :options="visibleResults"
    :is-loading="isLoading"
    :empty-message="$tc('global.sw-single-select.messageNoResults', { term: searchInput }, 0)"
    :focus-el="$refs.swSelectInput"
    :popover-classes="resultListClasses"
    @paginate="$emit('paginate')"
    @item-select="setValue"
>
    {% block sw_import_export_entity_path_select_base_results_list %}
    {% block sw_import_export_entity_path_select_base_results_list_before %}
    <template #before-item-list>
        <slot name="before-item-list">
            <sw-select-result
```

#### Example 2
Source: `sw-cms/component/sw-cms-product-assignment/sw-cms-product-assignment.html.twig`
```twig
<sw-select-result-list
    ref="swSelectResultList"
    :options="resultCollection"
    :is-loading="isLoadingResults"
    :empty-message="$tc('global.sw-entity-many-to-many-select.messageNoResults', { term: searchTerm }, 0)"
    :focus-el="$refs.searchInput"
    @paginate="paginateResult"
    @item-select="onItemSelect"
>

    {% block sw_cms_product_assignment_results_list_before %}
    <template #before-item-list>
        {% block sw_cms_product_assignment_results_list_before_content %}
        <slot name="before-item-list"></slot>
    {% endblock %}
```

#### Example 3
Source: `sw-settings-cache/page/sw-settings-cache-index/sw-settings-cache-index.html.twig`
```twig
<sw-select-result-list :options="[indexers]">
    <template #result-item="{ item, index }">
        <ul
            class="sw-settings-cache__indexers-list"
            @click.stop
        >
            <li
                v-for="(updaters, indexer) in item"
                :key="indexer"
            >
                <mt-checkbox
                    class="sw-settings-cache__indexers-entry"
                    :checked="indexerSelection.includes(indexer)"
                    :label="indexer"
                    :name="indexer"
```

## sw-select-result

> Shopware Administration component.

- [Slots](#slots)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| index | `any` | — | yes |  |
| item | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| selected | `any` | `false` | no |  |
| descriptionPosition | `any` | `'right'` | no | Valid: `bottom`, `right`, `left` |
| ariaLabel | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| preview | — | |
| description | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |
| `checkIfSelected` | |
| `checkIfActive` | |
| `onClickResult` | |
| `onMouseEnter` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `resultClasses` | |
| `hasDescriptionSlot` | |

### Examples

#### Example 1
Source: `sw-bulk-edit/page/sw-bulk-edit-product/sw-bulk-edit-product.html.twig`
```twig
<sw-select-result
    :selected="isSelected(item)"
    :disabled="!!priceRuleGroups[item.id] || undefined"
    v-bind="{ item, index }"
    @item-select="addItem"
>
    {{ getKey(item,labelProperty) || getKey(item, `translated.${labelProperty}`) }}
</sw-select-result>
```

#### Example 2
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
<sw-select-result
    v-tooltip="{
        showDelay: 300,
        message: $tc('sw-import-export.profile.objectTypeDisabledText'),
        disabled: !shouldDisableObjectType(item)
    }"
    :disabled="item.disabled || shouldDisableObjectType(item)"
    :class="'sw-select-option--' + item.value"
    :selected="isSelected(item)"
    v-bind="{ item, index }"
    @item-select="setValue"
>
    {% block sw_import_export_edit_profile_general_container_object_type_select_result_highlight %}
    <sw-highlight-text
        v-if="highlightSearchTerm && !isSelected(item)"
```

#### Example 3
Source: `sw-import-export/component/sw-import-export-edit-profile-general/sw-import-export-edit-profile-general.html.twig`
```twig
<sw-select-result
    v-tooltip="{
        showDelay: 300,
        message: $tc('sw-import-export.profile.profileTypeDisabledText'),
        disabled: !shouldDisableProfileType(item)
    }"
    :disabled="item.disabled || shouldDisableProfileType(item)"
    :class="'sw-select-option--' + item.value"
    :selected="isSelected(item)"
    v-bind="{ item, index }"
    @item-select="setValue"
>
    {% block sw_import_export_edit_profile_general_container_type_result_highlight %}
    <sw-highlight-text
        v-if="highlightSearchTerm && !isSelected(item)"
```

#### Example 4
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
<sw-select-result-list
    ref="resultsList"
    :options="visibleResults"
    :is-loading="isLoading"
    :empty-message="$tc('global.sw-single-select.messageNoResults', { term: searchInput }, 0)"
    :focus-el="$refs.swSelectInput"
    :popover-classes="resultListClasses"
    @paginate="$emit('paginate')"
    @item-select="setValue"
>
    {% block sw_import_export_entity_path_select_base_results_list %}
    {% block sw_import_export_entity_path_select_base_results_list_before %}
    <template #before-item-list>
        <slot name="before-item-list">
            <sw-select-result
```

#### Example 5
Source: `sw-import-export/component/sw-import-export-entity-path-select/sw-import-export-entity-path-select.html.twig`
```twig
<sw-select-result
    :selected="isSelected(item)"
    v-bind="{ item, index }"
    @item-select="setValue"
>
    {% block sw_import_export_entity_path_select_base_results_list_result_label %}
    <slot
        name="result-label-property"
        v-bind="{ item, index, labelProperty, valueProperty, searchTerm, highlightSearchTerm, getKey }"
    >
        <sw-highlight-text
            v-if="highlightSearchTerm"
            :text="getKey(item, labelProperty)"
            :search-term="searchTerm"
        />
```

## sw-select-rule-create

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | `null` | no |  |
| rules | `any` | `null` | no |  |
| ruleFilter | `any` | — | no |  |
| ruleAwareGroupKey | `any` | `null` | no |  |
| restrictedRuleIds | `any` | — | no |  |
| restrictedRuleIdsTooltipLabel | `any` | — | no |  |
| size | `any` | `'default'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-item | — | |
| result-label-property | — | |
| rule-modal | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| save-rule | — | |
| dismiss-rule | — | |
| update:rules | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSaveRule` | |
| `onSelectRule` | |
| `onUpdateCollection` | |
| `openCreateRuleModal` | |
| `onCloseRuleModal` | |
| `onRuleSelectInput` | |
| `isRuleRestricted` | |
| `getAdvancedSelectionParameters` | |
| `tooltipConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `collection` | |

### Examples

#### Example 1
Source: `sw-settings-tax/page/sw-settings-tax-provider-detail/sw-settings-tax-provider-detail.html.twig`
```twig
                    <sw-select-rule-create
                        v-if="!isLoading"
                        class="sw-settings-tax-tax-provider-detail__field-availability-rule"
                        :disabled="!acl.can('tax.editor') || undefined"
                        :rule-id="taxProvider.availabilityRuleId"
                        :rule-filter="ruleFilter"
                        :placeholder="$tc('sw-settings-tax.taxProviderDetail.placeholderAvailabilityRule')"
                        rule-aware-group-key="taxProvider"
                        @save-rule="onSaveRule"
                        @dismiss-rule="onDismissRule"
                    />
                </mt-card>

                <sw-extension-component-section
                    v-if="hasIdentifier"
```

#### Example 2
Source: `sw-promotion-v2/component/sw-promotion-v2-cart-condition-form/sw-promotion-v2-cart-condition-form.html.twig`
```twig
<sw-select-rule-create
    v-if="promotion"
    v-model:rules="promotion.cartRules"
    class="sw-promotion-v2-cart-condition-form__rule-select-cart"
    :local-mode="promotion.isNew()"
    :rule-filter="ruleFilter"
    :label="$tc('sw-promotion-v2.detail.conditions.preConditions.labelCartConditionSelect')"
    :placeholder="$tc('sw-promotion-v2.detail.conditions.preConditions.placeholderCartConditionSelect')"
    :rule-scope="['checkout', 'global', 'lineItem']"
    rule-aware-group-key="cartPromotions"
    :disabled="isEditingDisabled"
/>
{% endblock %}

{% block sw_promotion_v2_cart_condition_form_use_setgroups_field %}
```

#### Example 3
Source: `sw-promotion-v2/component/sw-promotion-v2-cart-condition-form/sw-promotion-v2-cart-condition-form.html.twig`
```twig
        <sw-select-rule-create
            v-model:rules="group.setGroupRules"
            class="sw-promotion-v2-cart-condition-form__setgroup-rules"
            :label="$tc('sw-promotion-v2.detail.conditions.setgroups.labelRules')"
            :placeholder="$tc('sw-promotion-v2.detail.conditions.setgroups.placeholder')"
            :rule-filter="ruleFilter"
            :rule-scope="['checkout', 'global', 'lineItem']"
            :disabled="isEditingDisabled"
            rule-aware-group-key="promotionSetGroups"
        />
        {% endblock %}

    </sw-container>
</mt-card>
{% endblock %}
```

#### Example 4
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-rule-selection/sw-promotion-v2-settings-rule-selection.html.twig`
```twig
    <sw-select-rule-create
        v-model:rules="discount.discountRules"
        :rule-filter="ruleCriteria"
        :rule-scope="['cart']"
        local-mode
        :label="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.labelSelection')"
        :placeholder="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.placeholderSelection')"
        :disabled="!acl.can('promotion.editor')"
    />
    {% endblock %}

</div>
{% endblock %}

```

#### Example 5
Source: `sw-promotion-v2/component/discount/sw-promotion-v2-settings-trigger/sw-promotion-v2-settings-trigger.html.twig`
```twig
        <sw-select-rule-create
            v-model:rules="discount.discountRules"
            local-mode
            class="sw-promotion-v2-settings-trigger-settings__rule-selection"
            :rule-filter="ruleCriteria"
            :rule-scope="['cart']"
            :label="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.labelSelection')"
            :placeholder="$tc('sw-promotion-v2.detail.discounts.settings.ruleSelection.placeholderSelection')"
            :disabled="!acl.can('promotion.editor')"
        />
        {% endblock %}

    </sw-container>
    {% endblock %}

```

## sw-select-selection-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selections | `any` | — | no |  |
| labelProperty | `any` | `'label'` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| enableSearch | `any` | `true` | no |  |
| invisibleCount | `any` | `0` | no |  |
| size | `any` | `null` | no |  |
| alwaysShowPlaceholder | `any` | `false` | no |  |
| placeholder | `any` | `''` | no |  |
| isLoading | `any` | `false` | no |  |
| searchTerm | `any` | `''` | no |  |
| disabled | `any` | `false` | no |  |
| selectionDisablingMethod | `any` | — | no |  |
| hideLabels | `any` | `false` | no |  |
| inputLabel | `any` | — | no |  |
| autocomplete | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| selected-option | — | |
| label-property | — | |
| invisible-count | — | |
| input | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| total-count-click | — | |
| search-term-change | — | |
| last-item-delete | — | |
| key-down-enter | — | |
| item-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `isSelectionDisabled` | |
| `onClickInvisibleCount` | |
| `onSearchTermChange` | |
| `onKeyDownDelete` | |
| `onKeyDownEnter` | |
| `onClickDismiss` | |
| `focus` | |
| `blur` | |
| `select` | |
| `getFocusEl` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showPlaceholder` | |

### Examples

#### Basic Usage
```twig
<sw-select-selection-list>
    <!-- content -->
</sw-select-selection-list>
```

## sw-self-maintained-extension-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| extension | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `changeExtensionStatus` | |
| `installAndActivateExtension` | |
| `installExtension` | |
| `activateExtension` | |
| `deactivateExtension` | |
| `removeExtension` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `extensionCardClasses` | |
| `permissions` | |
| `isInstalled` | |

### Examples

#### Basic Usage
```twig
<sw-self-maintained-extension-card
    extension="..."
>
    <!-- content -->
</sw-self-maintained-extension-card>
```

## sw-seo-main-category

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentSalesChannelId | `any` | `null` | no |  |
| categories | `any` | — | yes |  |
| mainCategories | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| allowEdit | `any` | `true` | no |  |
| overwriteLabel | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| main-category-add | — | |
| main-category-remove | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onMainCategorySelected` | |
| `refreshMainCategoryForSalesChannel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mainCategoryRepository` | |
| `isHeadlessSalesChannel` | |
| `selectedCategory` | |

### Examples

#### Example 1
Source: `sw-product/view/sw-product-detail-seo/sw-product-detail-seo.html.twig`
```twig
                    <sw-seo-main-category
                        :current-sales-channel-id="props.currentSalesChannelId"
                        :categories="categories"
                        :main-categories="isInherited ? parentProduct.mainCategories : product.mainCategories"
                        :overwrite-label="true"
                        :allow-edit="acl.can('product.editor') && !isInherited"
                        @main-category-add="onAddMainCategory"
                        @main-category-remove="onRemoveMainCategory"
                    />
                    {% endblock %}
                </template>

            </sw-inherit-wrapper>
            {% endblock %}
        </template>
```

## sw-seo-url-template-card

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchSeoUrlTemplates` | |
| `createSeoUrlTemplatesFromDefaultRoutes` | |
| `createVariableOptions` | |
| `getVariableOptions` | |
| `getLabel` | |
| `getPlaceholder` | |
| `onClickSave` | |
| `createSaveErrorNotification` | |
| `createSaveSuccessNotification` | |
| `onSelectInput` | |
| `onInput` | |
| `debouncedPreviewSeoUrlTemplate` | |
| `setErrorMessagesForEntity` | |
| `fetchSeoUrlPreview` | |
| `fetchSalesChannels` | |
| `onSalesChannelChanged` | |
| `getTemplatesForSalesChannel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `seoUrlTemplatesTemplateError` | |
| `salesChannelRepository` | |
| `salesChannelIsHeadless` | |

### Examples

#### Example 1
Source: `sw-settings-seo/page/sw-settings-seo/sw-settings-seo.html.twig`
```twig
<sw-seo-url-template-card ref="seoUrlTemplateCard" />
```

## sw-seo-url

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salesChannelId | `any` | `null` | no |  |
| urls | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |
| hasDefaultTemplate | `any` | `true` | no |  |
| disabled | `any` | `false` | no |  |
| resultLimit | `any` | `25` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| seo-additional | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-change-sales-channel | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `initSalesChannelCollection` | |
| `initSeoUrlCollection` | |
| `clearDefaultSeoUrls` | |
| `refreshCurrentSeoUrl` | |
| `onSalesChannelChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `seoUrlCollection` | |
| `currentSeoUrl` | |
| `defaultSeoUrl` | |
| `seoUrlRepository` | |
| `salesChannelRepository` | |
| `isHeadlessSalesChannel` | |
| `seoUrlHelptext` | |
| `hasAdditionalSeoSlot` | |
| `allowInput` | |

### Examples

#### Example 1
Source: `sw-category/view/sw-category-detail-seo/sw-category-detail-seo.html.twig`
```twig
    <sw-seo-url
        v-if="category.seoUrls"
        :is-loading="isLoading"
        :has-default-template="false"
        :disabled="!acl.can('category.editor')"
        :urls="category.seoUrls"
    />
    {% endblock %}

</div>
{% endblock %}

```

#### Example 2
Source: `sw-product/view/sw-product-detail-seo/sw-product-detail-seo.html.twig`
```twig
<sw-seo-url
    v-if="product.seoUrls"
    :has-default-template="false"
    :disabled="!acl.can('product.editor')"
    :urls="product.seoUrls"
    @on-change-sales-channel="onChangeSalesChannel"
>
    {% block sw_product_detail_seo_urls_content %}
    <template #seo-additional="props">
        {% block sw_product_detail_seo_urls_content_seo_additional %}
        <sw-inherit-wrapper
            v-if="product.mainCategories"
            v-model:value="productMainCategory"
            :has-parent="!!parentProduct.id && !!props.currentSalesChannelId && product.categories.length === 0"
            :label="$tc('sw-seo-url.labelMainCategory')"
```

#### Example 3
Source: `sw-settings-seo/page/sw-settings-seo/sw-settings-seo.html.twig`
```twig
<sw-seo-url-template-card ref="seoUrlTemplateCard" />
```

## sw-settings-basic-information

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `onSave` | |
| `onLoadingChanged` | |

### Examples

#### Basic Usage
```twig
<sw-settings-basic-information>
    <!-- content -->
</sw-settings-basic-information>
```

## sw-settings-cache-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `resetButtons` | |
| `decreaseWorkerPoll` | |
| `clearDataCache` | |
| `clearCache` | |
| `updateIndexes` | |
| `changeSelection` | |
| `createOnlySelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `httpCacheValue` | |
| `environmentValue` | |
| `cacheAdapterValue` | |
| `indexingMethodOptions` | |

### Examples

#### Basic Usage
```twig
<sw-settings-cache-index>
    <!-- content -->
</sw-settings-cache-index>
```

## sw-settings-cache-modal

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUnmountComponent` | |
| `keydownEventListener` | |
| `openModal` | |
| `closeModal` | |
| `clearCache` | |

### Examples

#### Basic Usage
```twig
<sw-settings-cache-modal>
    <!-- content -->
</sw-settings-cache-modal>
```

## sw-settings-captcha-select-v2

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `setCaptchaOptions` | |
| `renderCaptchaOption` | |
| `getTranslations` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `attributes` | |
| `currentValue` | |
| `activeCaptchaSelect` | |

### Examples

#### Basic Usage
```twig
<sw-settings-captcha-select-v2>
    <!-- content -->
</sw-settings-captcha-select-v2>
```

## sw-settings-cart

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `onSave` | |
| `onLoadingChanged` | |

### Examples

#### Basic Usage
```twig
<sw-settings-cart>
    <!-- content -->
</sw-settings-cart>
```

## sw-settings-country-address-handling

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| country | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onDragStart` | |
| `onDragEnter` | |
| `onDrop` | |
| `onDropEnd` | |
| `moveToNewPosition` | |
| `addNewLineAt` | |
| `swapPosition` | |
| `change` | |
| `customerLabel` | |
| `onChangeCustomer` | |
| `resetMarkup` | |
| `openSnippetModal` | |
| `onCloseModal` | |
| `getSnippets` | |
| `renderFormattingAddress` | |
| `getLabelProperty` | |
| `updateCountry` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customerCriteria` | |
| `dragConf` | |
| `addressFormat` | |
| `hasDefaultPostalCodePattern` | |
| `disabledAdvancedPostalCodePattern` | |

### Examples

#### Basic Usage
```twig
<sw-settings-country-address-handling
    country="..."
    isLoading="..."
>
    <!-- content -->
</sw-settings-country-address-handling>
```

## sw-settings-country-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |

### Examples

#### Basic Usage
```twig
<sw-settings-country-create>
    <!-- content -->
</sw-settings-country-create>
```

## sw-settings-country-currency-dependent-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencyDependsValue | `any` | — | yes |  |
| countryId | `any` | — | yes |  |
| userConfig | `any` | — | yes |  |
| userConfigValues | `any` | — | yes |  |
| menuOptions | `any` | — | yes |  |
| taxFreeType | `any` | `''` | no |  |
| isLoading | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| modal-save | — | |
| base-item-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `saveModal` | |
| `changeCurrencyDependentRow` | |
| `addCurrencyDependentRow` | |
| `removeCurrencyDependentRow` | |
| `updateCheckBoxHamburgerMenu` | |
| `onChangeBaseCurrency` | |
| `calculateInheritedPrice` | |
| `reCalculatorInherited` | |
| `getPriceByCurrency` | |
| `createUserConfigValue` | |
| `createNewUserConfig` | |
| `updateExistedValue` | |
| `getCurrencyNameById` | |
| `getCurrencyById` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentUserId` | |
| `currencyTaxFreeDependentRepository` | |
| `radioButtonName` | |
| `countryCurrencyColumns` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-general/sw-settings-country-general.html.twig`
```twig
<sw-settings-country-currency-dependent-modal
    v-if="showCurrencyModal"
    :currency-depends-value="currencyDependsValue"
    :country-id="countryId"
    :is-loading="isLoading"
    :menu-options="menuOptions"
    :user-config="userConfig"
    :user-config-values="userConfigValues"
    :tax-free-type="taxFreeType"
    @modal-close="onToggleCurrencyModal"
    @modal-save="saveCountryCurrencyDependent"
    @base-item-change="changeBaseItem"
/>
{% endblock %}

```

## sw-settings-country-currency-hamburger-menu

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | `false` | no |  |
| options | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| currency-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onCheckCurrency` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-currency-dependent-modal/sw-settings-country-currency-dependent-modal.html.twig`
```twig
    <sw-settings-country-currency-hamburger-menu
        :options="menuOptions"
        @currency-change="changeCurrencyDependentRow"
    />
</template>
{% endblock %}

{% block  sw_settings_country_currency_dependent_modal_content_currency_name %}
<template #column-currencyId="{ item }">
    <div class="sw-settings-country-currency-dependent-modal__inheritance-wrapper">
        <!-- eslint-disable-next-line vuejs-accessibility/label-has-for -->
        <label>{{ getCurrencyNameById(item.currencyId) }}</label>
    </div>
</template>
{% endblock %}
```

## sw-settings-country-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `loadUserConfig` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `getStateColumns` | |
| `onSaveModal` | |
| `onUpdateCountry` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentUserId` | |
| `countryRepository` | |
| `userConfigRepository` | |
| `identifier` | |
| `stateColumns` | |
| `isNewCountry` | |
| `allowSave` | |
| `tooltipSave` | |
| `userConfigCriteria` | |
| `countryNameError` | |
| `showCustomFields` | |

### Examples

#### Basic Usage
```twig
<sw-settings-country-detail>
    <!-- content -->
</sw-settings-country-detail>
```

## sw-settings-country-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| country | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| userConfig | `any` | — | yes |  |
| userConfigValues | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCurrencies` | |
| `openCustomerTaxModal` | |
| `openCompanyTaxModal` | |
| `onToggleCurrencyModal` | |
| `changeBaseItem` | |
| `createDataModal` | |
| `clearMenuOptions` | |
| `addCheckedHamburgerMenu` | |
| `addDisabledBaseCurrencyCheckBox` | |
| `sortCurrencyCheckBox` | |
| `pushDataFromUserConfig` | |
| `calculateInheritedPrice` | |
| `getPriceByCurrency` | |
| `getCurrencyById` | |
| `saveCountryCurrencyDependent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `countryRepository` | |
| `currencyRepository` | |
| `countryNameError` | |

### Examples

#### Basic Usage
```twig
<sw-settings-country-general
    country="..."
    isLoading="..."
    userConfig="..."
>
    <!-- content -->
</sw-settings-country-general>
```

## sw-settings-country-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `onInlineEditSave` | |
| `onChangeLanguage` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `getCountryColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `countryRepository` | |
| `detailPageLinkText` | |

### Examples

#### Basic Usage
```twig
<sw-settings-country-list>
    <!-- content -->
</sw-settings-country-list>
```

## sw-settings-country-new-snippet-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| selections | `any` | — | no |  |
| currentPosition | `any` | — | yes |  |
| addressFormat | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
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
| `createdComponent` | |
| `onCloseModal` | |
| `addElement` | |
| `debouncedSearch` | |
| `search` | |
| `getSnippetsTree` | |
| `onClickDismiss` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `selection` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
    <sw-settings-country-new-snippet-modal
        v-if="isOpenModal"
        :selections="snippets"
        :current-position="currentPosition"
        :address-format="addressFormat"
        :get-label-property="getLabelProperty"
        @change="change"
        @modal-close="onCloseModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-settings-country-preview-template

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| formattingAddress | `any` | — | yes |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `displayFormattingAddress` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-address-handling/sw-settings-country-address-handling.html.twig`
```twig
<sw-settings-country-preview-template :formatting-address="formattingAddress" />
```

## sw-settings-country-state

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| country | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |
| countryStateRepository | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `getStateColumns` | |
| `countryStateSelectionChanged` | |
| `onSearchCountryState` | |
| `onDeleteCountryStates` | |
| `onAddCountryState` | |
| `onSaveCountryState` | |
| `onCancelCountryState` | |
| `onClickCountryState` | |
| `refreshCountryStateList` | |
| `getCountryStateName` | |
| `checkEmptyState` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateColumns` | |
| `countryStates` | |

### Examples

#### Basic Usage
```twig
<sw-settings-country-state
    country="..."
>
    <!-- content -->
</sw-settings-country-state>
```

## sw-settings-currency-country-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencyCountryRounding | `any` | — | yes |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| result-label-property | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-cancel | — | |
| save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCancel` | |
| `onSave` | |
| `shouldDisableCountry` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `countryCriteria` | |
| `countryRepository` | |
| `assignedCountriesCriteria` | |
| `currencyCountryRoundingCountryIdError` | |

### Examples

#### Example 1
Source: `sw-settings-currency/page/sw-settings-currency-detail/sw-settings-currency-detail.html.twig`
```twig
                <sw-settings-currency-country-modal
                    v-if="currentCurrencyCountry"
                    :currency-country-rounding="currentCurrencyCountry"
                    @save="onSaveCurrencyCountry"
                    @edit-cancel="onCancelEditCountry"
                />
                {% endblock %}
                {% endblock %}

                {% block sw_settings_currency_detail_custom_field_sets %}
                <mt-card
                    v-if="showCustomFields"
                    position-identifier="sw-settings-currency-detail-custom-field-sets"
                    :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                    :is-loading="isLoading"
```

## sw-settings-currency-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currencyId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCurrencyCountryRoundings` | |
| `loadCustomFieldSets` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `onChangeCountrySearch` | |
| `onAddCountry` | |
| `onCancelEditCountry` | |
| `onClickEdit` | |
| `onSaveCurrencyCountry` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `currencyRepository` | |
| `currencyCountryRoundingRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `currencyNameError` | |
| `currencyIsoCodeError` | |
| `currencyShortNameError` | |
| `currencySymbolError` | |
| `currencyIsDefaultError` | |
| `currencyDecimalPrecisionError` | |
| `currencyFactorError` | |
| `currencyCountryColumns` | |
| `currencyCountryRoundingCriteria` | |
| `emptyStateText` | |
| `showCustomFields` | |

### Examples

#### Basic Usage
```twig
<sw-settings-currency-detail>
    <!-- content -->
</sw-settings-currency-detail>
```

## sw-settings-currency-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `metaInfo` | |
| `getList` | |
| `onChangeLanguage` | |
| `onInlineEditSave` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `getCurrencyColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currencyRepository` | |

### Examples

#### Basic Usage
```twig
<sw-settings-currency-list>
    <!-- content -->
</sw-settings-currency-list>
```

## sw-settings-custom-field-set-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |
| `onSave` | |
| `createNameNotUniqueNotification` | |

### Examples

#### Basic Usage
```twig
<sw-settings-custom-field-set-create>
    <!-- content -->
</sw-settings-custom-field-set-create>
```

## sw-settings-custom-field-set-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `onLoadingChanged` | |
| `onResetErrors` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `customFieldSetRepository` | |
| `customFieldRepository` | |
| `customFieldCriteria` | |
| `customFieldSetCriteria` | |
| `tooltipSave` | |
| `tooltipCancel` | |

### Examples

#### Basic Usage
```twig
<sw-settings-custom-field-set-detail>
    <!-- content -->
</sw-settings-custom-field-set-detail>
```

## sw-settings-custom-field-set-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getLocaleCriterias` | |
| `getTermCriteria` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `titleSaveSuccess` | |
| `messageSaveSuccess` | |
| `listingCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-settings-custom-field-set-list>
    <!-- content -->
</sw-settings-custom-field-set-list>
```

## sw-settings-customer-group-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |

### Examples

#### Basic Usage
```twig
<sw-settings-customer-group-create>
    <!-- content -->
</sw-settings-customer-group-create>
```

## sw-settings-customer-group-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| customerGroupId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomerGroup` | |
| `loadSeoUrls` | |
| `loadCustomFieldSets` | |
| `onChangeLanguage` | |
| `onCancel` | |
| `getSeoUrl` | |
| `validateSaveRequest` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `customerGroupRepository` | |
| `seoUrlRepository` | |
| `customerGroupCriteria` | |
| `registrationSalesChannelCriteria` | |
| `seoUrlCriteria` | |
| `entityDescription` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `hasRegistration` | |
| `technicalUrl` | |
| `customerGroupNameError` | |
| `allowSave` | |
| `showCustomFields` | |

### Examples

#### Basic Usage
```twig
<sw-settings-customer-group-detail>
    <!-- content -->
</sw-settings-customer-group-detail>
```

## sw-settings-customer-group-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `getColumns` | |
| `customerGroupCriteriaWithFilter` | |
| `createErrorNotification` | |
| `customerGroupCanBeDeleted` | |
| `deleteCustomerGroup` | |
| `deleteCustomerGroups` | |
| `onContextMenuDelete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `columns` | |
| `customerGroupRepository` | |
| `allCustomerGroupsCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-settings-customer-group-list>
    <!-- content -->
</sw-settings-customer-group-list>
```

## sw-settings-delivery-time-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-settings-delivery-time-create>
    <!-- content -->
</sw-settings-delivery-time-create>
```

## sw-settings-delivery-time-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `onSave` | |
| `onChangeLanguage` | |
| `saveFinish` | |
| `onCancel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `deliveryTimeNameError` | |
| `deliveryTimeMinError` | |
| `deliveryTimeMaxError` | |
| `deliveryTimeUnitError` | |
| `deliveryTimeRepository` | |
| `deliveryTimeUnits` | |
| `displayName` | |
| `isInvalidMinField` | |
| `invalidMinError` | |
| `allowSave` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `showCustomFields` | |

### Examples

#### Basic Usage
```twig
<sw-settings-delivery-time-detail>
    <!-- content -->
</sw-settings-delivery-time-detail>
```

## sw-settings-delivery-time-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `onChangeLanguage` | |
| `deliveryTimeColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `deliveryTimeRepository` | |

### Examples

#### Basic Usage
```twig
<sw-settings-delivery-time-list>
    <!-- content -->
</sw-settings-delivery-time-list>
```

## sw-settings-document-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| documentConfigId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `loadAvailableSalesChannel` | |
| `showOption` | |
| `onChangeType` | |
| `onChangeSalesChannel` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `createSalesChannelSelectOptions` | |
| `onRemoveDocumentType` | |
| `onAddDocumentType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `countryRepository` | |
| `documentBaseConfigCriteria` | |
| `documentBaseConfigRepository` | |
| `documentTypeRepository` | |
| `salesChannelRepository` | |
| `documentBaseConfigSalesChannelRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `documentBaseConfig` | |
| `documentBaseConfigNameError` | |
| `documentBaseConfigDocumentTypeIdError` | |
| `showCustomFields` | |
| `fileTypesSelected` | |
| `documentCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-settings-document-detail>
    <!-- content -->
</sw-settings-document-detail>
```

## sw-settings-document-list

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `filters` | |
| `expandButtonClass` | |
| `collapseButtonClass` | |
| `listingCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-settings-document-list>
    <!-- content -->
</sw-settings-document-list>
```

## sw-settings-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getUserConfig` | |
| `onCloseSettingRenameBanner` | |
| `hasPluginConfig` | |
| `getRouteConfig` | |
| `getLabel` | |
| `getGroupLabel` | |
| `itemIsQueried` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `settingsGroups` | |

### Examples

#### Basic Usage
```twig
<sw-settings-index>
    <!-- content -->
</sw-settings-index>
```

## sw-settings-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `any` | — | yes |  |
| to | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| icon | — | |
| label | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `classes` | |

### Examples

#### Example 1
Source: `sw-settings/page/sw-settings-index/sw-settings-index.html.twig`
```twig
<sw-settings-item
    v-for="settingsItem in settingsItems"
    :id="settingsItem.id"
    :key="settingsItem.name"
    :label="getLabel(settingsItem)"
    :to="getRouteConfig(settingsItem)"
>
    <template #icon>
        <component
            :is="settingsItem.iconComponent"
            v-if="settingsItem.iconComponent"
        />

        <mt-icon
            v-else
```

## sw-settings-language-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| languageId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `checkTranslationCodeInheritance` | |
| `setParentTranslationCodeId` | |
| `onInputLanguage` | |
| `isLocaleAlreadyUsed` | |
| `onSave` | |
| `onCancel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `languageRepository` | |
| `isIsoCodeRequired` | |
| `languageHasName` | |
| `isNewLanguage` | |
| `usedLocaleCriteria` | |
| `allowSave` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `parentLanguageCriteria` | |
| `isSystemDefaultLanguageId` | |
| `inheritanceTooltipText` | |
| `showCustomFields` | |
| `languageLocaleIdError` | |
| `languageNameError` | |

### Examples

#### Basic Usage
```twig
<sw-settings-language-detail>
    <!-- content -->
</sw-settings-language-detail>
```

## sw-settings-language-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `getParentName` | |
| `isDefault` | |
| `tooltipDelete` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `listingCriteria` | |
| `languageRepository` | |
| `getColumns` | |
| `allowCreate` | |
| `allowView` | |
| `allowEdit` | |
| `allowInlineEdit` | |
| `allowDelete` | |

### Examples

#### Basic Usage
```twig
<sw-settings-language-list>
    <!-- content -->
</sw-settings-language-list>
```

## sw-settings-listing-default-sales-channel

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchSalesChannelsSystemConfig` | |
| `displayAdvancedVisibility` | |
| `closeAdvancedVisibility` | |
| `saveSalesChannelVisibilityConfig` | |
| `updateSalesChannel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `salesChannel` | |

### Examples

#### Example 1
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
    <sw-settings-listing-default-sales-channel
        ref="defaultSalesChannelCard"
        :is-loading="isLoading"
    />
</mt-card>
{% endblock %}

{% block sw_settings_listing_content_card_view_system_config %}
<sw-system-config
    ref="systemConfig"
    sales-channel-switchable
    domain="core.listing"
    @loading-changed="onLoadingChanged"
>

```

#### Example 2
Source: `sw-first-run-wizard/view/sw-first-run-wizard-defaults/sw-first-run-wizard-defaults.html.twig`
```twig
    <sw-settings-listing-default-sales-channel
        ref="defaultSalesChannelCard"
        :is-loading="isLoading"
        @vue:mounted="() => defaultSalesChannelCardLoaded = true"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-settings-listing-delete-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| description | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| cancel | — | |
| delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `emitCancel` | |
| `emitDelete` | |

### Examples

#### Example 1
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
        <sw-settings-listing-delete-modal
            v-if="toBeDeletedProductSortingOption"
            :title="$tc('sw-settings-listing.index.deleteModal.title')"
            :description="$t('sw-settings-listing.index.deleteModal.description', {
                'sortingOptionName': toBeDeletedProductSortingOption.label
            })"
            @cancel="toBeDeletedProductSortingOption = null"
            @delete="onDeleteProductSorting(toBeDeletedProductSortingOption)"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 2
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
        <sw-settings-listing-delete-modal
            v-if="toBeDeletedCriteria"
            :title="$tc('sw-settings-listing.base.delete.modalTitle')"
            :description="$tc('sw-settings-listing.base.delete.modalDescription')"
            @cancel="toBeDeletedCriteria = null"
            @delete="onConfirmDeleteCriteria"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-settings-listing-option-base

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchProductSortingEntity` | |
| `fetchCustomFields` | |
| `fetchDefaultSorting` | |
| `getProductSortingEntityId` | |
| `isValidSortingOption` | |
| `searchForAlreadyExistingKey` | |
| `saveProductSorting` | |
| `onSave` | |
| `getCriteriaTemplate` | |
| `onDeleteCriteria` | |
| `onConfirmDeleteCriteria` | |
| `onAddCriteria` | |
| `onCancelEditCriteria` | |
| `isCriteriaACustomField` | |
| `transformCustomFieldCriterias` | |
| `onChangeLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productSortingRepository` | |
| `customFieldRepository` | |
| `smartBarHeading` | |
| `isGeneralCardLoading` | |
| `customFieldCriteria` | |
| `productSortingEntityCriteria` | |
| `isSaveButtonDisabled` | |
| `isDefaultSorting` | |

### Examples

#### Basic Usage
```twig
<sw-settings-listing-option-base>
    <!-- content -->
</sw-settings-listing-option-base>
```

## sw-settings-listing-option-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `createProductSortingEntity` | |
| `onSave` | |
| `onAddCriteria` | |
| `onConfirmDeleteCriteria` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `smartBarHeading` | |
| `isNewProductSorting` | |
| `urlKeyCriteria` | |

### Examples

#### Basic Usage
```twig
<sw-settings-listing-option-create>
    <!-- content -->
</sw-settings-listing-option-create>
```

## sw-settings-listing-option-criteria-grid

> Shopware Administration component.

- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productSortingEntity | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| criteria-add | — | |
| criteria-delete | — | |
| inline-edit-save | — | |
| inline-edit-cancel | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `fetchCustomFieldSetIds` | |
| `fetchCustomFields` | |
| `isItemACustomField` | |
| `getCustomFieldByName` | |
| `onAddCriteria` | |
| `getOrderSnippet` | |
| `onRemoveCriteria` | |
| `getCriteriaTemplate` | |
| `onSaveInlineEdit` | |
| `onCancelInlineEdit` | |
| `filterEmptyCustomFields` | |
| `stripCustomFieldPath` | |
| `getCriteriaSnippetByFieldName` | |
| `criteriaIsAlreadyUsed` | |
| `getCustomFieldLabelByCriteriaName` | |
| `getCustomFieldName` | |
| `customFieldCriteriaSingleSelect` | |
| `changeCustomField` | |
| `getProductSortingFieldsByName` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `customFieldSetRepository` | |
| `customFieldSetRelationsRepository` | |
| `customFieldCriteria` | |
| `customFieldsRelationsCriteria` | |
| `sortedProductSortingFields` | |
| `productSortingEntityColumns` | |
| `criteriaOptions` | |
| `orderOptions` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-settings-listing/page/sw-settings-listing-option-create/sw-settings-listing-option-create.html.twig`
```twig
<sw-settings-listing-option-criteria-grid
    v-if="productSortingEntity"
    :product-sorting-entity="productSortingEntity"
    @criteria-delete="onDeleteCriteria"
    @criteria-add="onAddCriteria"
/>
{% endblock %}

{% block sw_settings_listing_option_base_language_switch %}
<!-- eslint-disable vue/valid-v-slot -->
<template #language-switch>
    <sw-language-switch
        :disabled="isNewProductSorting"
        @on-change="onChangeLanguage"
    />
```

#### Example 2
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
        <sw-settings-listing-option-criteria-grid
            v-if="productSortingEntity"
            :product-sorting-entity="productSortingEntity"
            @criteria-delete="onDeleteCriteria"
            @criteria-add="onAddCriteria"
            @inline-edit-save="onSave"
            @inline-edit-cancel="onCancelEditCriteria"
        />
        {% endblock %}

        {% block sw_settings_listing_option_base_smart_bar_actions_grid_delete_modal %}
        <sw-settings-listing-delete-modal
            v-if="toBeDeletedCriteria"
            :title="$tc('sw-settings-listing.base.delete.modalTitle')"
            :description="$tc('sw-settings-listing.base.delete.modalDescription')"
```

## sw-settings-listing-option-general-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sortingOption | `any` | — | yes |  |
| isDefaultSorting | `any` | — | yes |  |
| technicalNameError | `any` | `{}` | no |  |
| labelError | `any` | `{}` | no |  |

### Examples

#### Example 1
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
    <sw-settings-listing-option-general-info
        v-if="productSortingEntity"
        :sorting-option="productSortingEntity"
        :is-default-sorting="isDefaultSorting"
        :label-error="sortingOptionLabelError"
        :technical-name-error="sortingOptionTechnicalNameError"
    />
    {% endblock %}

    {% block sw_settings_listing_option_base_smart_bar_actions_grid %}
    <sw-settings-listing-option-criteria-grid
        v-if="productSortingEntity"
        :product-sorting-entity="productSortingEntity"
        @criteria-delete="onDeleteCriteria"
        @criteria-add="onAddCriteria"
```

## sw-settings-listing-visibility-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |
| config | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onPageChange` | |
| `changeVisibilityValue` | |
| `fetchSalesChannels` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `truncateFilter` | |

### Examples

#### Example 1
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
            <sw-settings-listing-visibility-detail
                ref="visibilityConfig"
                :config="visibilityConfig"
            />

            <template #modal-footer>
                <mt-button
                    variant="primary"
                    size="small"
                    @click="closeAdvancedVisibility"
                >
                    {{ $tc('global.default.apply') }}
                </mt-button>
            </template>
        </sw-modal>
```

## sw-settings-listing

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `createdComponent` | |
| `fetchProductSortingOptions` | |
| `fetchSearchResultSortingOptions` | |
| `fetchCustomFields` | |
| `onSave` | |
| `saveProductSortingOptions` | |
| `saveSearchResultSortingOptions` | |
| `onDeleteProductSorting` | |
| `checkForPagination` | |
| `onPageChange` | |
| `onEditProductSortingOption` | |
| `formatProductSortingOptionField` | |
| `getCustomFieldLabelByCriteriaName` | |
| `getCustomFieldByName` | |
| `onAddNewProductSortingOption` | |
| `onSearchProductSortingOptions` | |
| `onSaveProductSortingOptionInlineEdit` | |
| `isItemACustomField` | |
| `getCustomFieldById` | |
| `stripCustomFieldPath` | |
| `isProductSortingEditable` | |
| `onChangeLanguage` | |
| `setDefaultSortingActive` | |
| `isItemDefaultSorting` | |
| `onLoadingChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productSortingOptionRepository` | |
| `customFieldRepository` | |
| `salesChannelRepository` | |
| `systemConfigRepository` | |
| `productSortingsOptionsCriteria` | |
| `searchResultSortingOptionCriteria` | |
| `productSortingOptionsSearchCriteria` | |
| `sortingOptionsGridTotal` | |
| `customFieldCriteria` | |
| `productSortingOptionColumns` | |
| `assetFilter` | |
| `salesChannelDefaultSortingError` | |

### Examples

#### Example 1
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
    <sw-settings-listing-default-sales-channel
        ref="defaultSalesChannelCard"
        :is-loading="isLoading"
    />
</mt-card>
{% endblock %}

{% block sw_settings_listing_content_card_view_system_config %}
<sw-system-config
    ref="systemConfig"
    sales-channel-switchable
    domain="core.listing"
    @loading-changed="onLoadingChanged"
>

```

#### Example 2
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
        <sw-settings-listing-delete-modal
            v-if="toBeDeletedProductSortingOption"
            :title="$tc('sw-settings-listing.index.deleteModal.title')"
            :description="$t('sw-settings-listing.index.deleteModal.description', {
                'sortingOptionName': toBeDeletedProductSortingOption.label
            })"
            @cancel="toBeDeletedProductSortingOption = null"
            @delete="onDeleteProductSorting(toBeDeletedProductSortingOption)"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 3
Source: `sw-settings-listing/page/sw-settings-listing-option-create/sw-settings-listing-option-create.html.twig`
```twig
<sw-settings-listing-option-criteria-grid
    v-if="productSortingEntity"
    :product-sorting-entity="productSortingEntity"
    @criteria-delete="onDeleteCriteria"
    @criteria-add="onAddCriteria"
/>
{% endblock %}

{% block sw_settings_listing_option_base_language_switch %}
<!-- eslint-disable vue/valid-v-slot -->
<template #language-switch>
    <sw-language-switch
        :disabled="isNewProductSorting"
        @on-change="onChangeLanguage"
    />
```

#### Example 4
Source: `sw-settings-listing/page/sw-settings-listing-option-base/sw-settings-listing-option-base.html.twig`
```twig
    <sw-settings-listing-option-general-info
        v-if="productSortingEntity"
        :sorting-option="productSortingEntity"
        :is-default-sorting="isDefaultSorting"
        :label-error="sortingOptionLabelError"
        :technical-name-error="sortingOptionTechnicalNameError"
    />
    {% endblock %}

    {% block sw_settings_listing_option_base_smart_bar_actions_grid %}
    <sw-settings-listing-option-criteria-grid
        v-if="productSortingEntity"
        :product-sorting-entity="productSortingEntity"
        @criteria-delete="onDeleteCriteria"
        @criteria-add="onAddCriteria"
```

#### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-default-sales-channel/sw-settings-listing-default-sales-channel.html.twig`
```twig
            <sw-settings-listing-visibility-detail
                ref="visibilityConfig"
                :config="visibilityConfig"
            />

            <template #modal-footer>
                <mt-button
                    variant="primary"
                    size="small"
                    @click="closeAdvancedVisibility"
                >
                    {{ $tc('global.default.apply') }}
                </mt-button>
            </template>
        </sw-modal>
```

## sw-settings-logging-entry-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| logEntry | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `displayString` | |

### Examples

#### Basic Usage
```twig
<sw-settings-logging-entry-info
    logEntry="..."
>
    <!-- content -->
</sw-settings-logging-entry-info>
```

## sw-settings-logging-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `showInfoModal` | |
| `closeInfoModal` | |
| `getList` | |
| `logLevelToString` | |
| `getLogColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `logEntryRepository` | |
| `logColumns` | |
| `modalNameFromLogEntry` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-settings-logging-list>
    <!-- content -->
</sw-settings-logging-list>
```

## sw-settings-logging-mail-sent-info

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `recipientString` | |

### Examples

#### Basic Usage
```twig
<sw-settings-logging-mail-sent-info>
    <!-- content -->
</sw-settings-logging-mail-sent-info>
```

## sw-settings-login-registration

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `onSave` | |
| `onLoginRegistrationLoadingChanged` | |
| `onSystemWideLoadingChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `systemConfigLoading` | |

### Examples

#### Basic Usage
```twig
<sw-settings-login-registration>
    <!-- content -->
</sw-settings-login-registration>
```

## sw-settings-mailer-smtp

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mailerSettings | `any` | — | yes |  |
| hostError | `any` | `null` | no |  |
| portError | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| host-changed | — | |
| port-changed | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isOauth` | |
| `encryptionOptions` | |

### Examples

#### Example 1
Source: `sw-first-run-wizard/view/sw-first-run-wizard-mailer-smtp/sw-first-run-wizard-mailer-smtp.html.twig`
```twig
<sw-settings-mailer-smtp :mailer-settings="mailerSettings" />
```

#### Example 2
Source: `sw-settings-mailer/page/sw-settings-mailer/sw-settings-mailer.html.twig`
```twig
                <sw-settings-mailer-smtp
                    :mailer-settings="mailerSettings"
                    :host-error="smtpHostError"
                    :port-error="smtpPortError"
                    @host-changed="resetSmtpHostError"
                    @port-changed="resetSmtpPortError"
                />
                {% endblock %}

            </mt-card>
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
```

## sw-settings-mailer

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadPageContent` | |
| `loadMailerSettings` | |
| `saveMailerSettings` | |
| `onSaveFinish` | |
| `checkFirstConfiguration` | |
| `validateSmtpConfiguration` | |
| `resetSmtpHostError` | |
| `resetSmtpPortError` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `emailSendmailOptions` | |
| `isSmtpMode` | |
| `emailAgentOptions` | |

### Examples

#### Example 1
Source: `sw-first-run-wizard/view/sw-first-run-wizard-mailer-smtp/sw-first-run-wizard-mailer-smtp.html.twig`
```twig
<sw-settings-mailer-smtp :mailer-settings="mailerSettings" />
```

#### Example 2
Source: `sw-settings-mailer/page/sw-settings-mailer/sw-settings-mailer.html.twig`
```twig
                <sw-settings-mailer-smtp
                    :mailer-settings="mailerSettings"
                    :host-error="smtpHostError"
                    :port-error="smtpPortError"
                    @host-changed="resetSmtpHostError"
                    @port-changed="resetSmtpPortError"
                />
                {% endblock %}

            </mt-card>
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
```

## sw-settings-measurement-default-units

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| measurementSystems | `any` | — | yes |  |
| measurementSystem | `any` | — | yes |  |
| measurementUnits | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| measurement-system-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeMeasurementSystem` | |
| `labelUnitCallback` | |
| `getUnitOptionsByType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `lengthUnitOptions` | |
| `weightUnitOptions` | |
| `measurementSystemOptions` | |
| `measurementUnitSystemError` | |
| `measurementLengthUnitError` | |
| `measurementWeightUnitError` | |

### Examples

#### Example 1
Source: `sw-settings-measurement/page/sw-settings-measurement/sw-settings-measurement.html.twig`
```twig
            <sw-settings-measurement-default-units
                :measurement-systems="measurementSystems"
                :measurement-system="measurementSystem"
                :measurement-units="measurementUnits"
                @measurement-system-change="onChangeMeasurementSystem"
            />
        </sw-card-view>
    </template>
</sw-page>

```

## sw-settings-measurement

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getMeasurementUnits` | |
| `getDefaultMeasurementSystems` | |
| `onSave` | |
| `onChangeLanguage` | |
| `onChangeMeasurementSystem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `measurementSystemRepository` | |
| `measurementSystemCriteria` | |
| `defaultLengthUnit` | |
| `defaultWeightUnit` | |
| `requiredFields` | |

### Examples

#### Example 1
Source: `sw-settings-measurement/page/sw-settings-measurement/sw-settings-measurement.html.twig`
```twig
            <sw-settings-measurement-default-units
                :measurement-systems="measurementSystems"
                :measurement-system="measurementSystem"
                :measurement-units="measurementUnits"
                @measurement-system-change="onChangeMeasurementSystem"
            />
        </sw-card-view>
    </template>
</sw-page>

```

## sw-settings-media

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |
| `onSave` | |
| `onLoadingChanged` | |

### Examples

#### Basic Usage
```twig
<sw-settings-media>
    <!-- content -->
</sw-settings-media>
```

## sw-settings-message-stats

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadStats` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `statsData` | |
| `hasStats` | |
| `isStatsDisabled` | |
| `formattedProcessedSince` | |
| `formattedAverageTime` | |
| `statBlocks` | |
| `sortedMessageTypeStats` | |

### Examples

#### Basic Usage
```twig
<sw-settings-message-stats>
    <!-- content -->
</sw-settings-message-stats>
```

## sw-settings-newsletter

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `onSave` | |
| `onLoadingChanged` | |

### Examples

#### Basic Usage
```twig
<sw-settings-newsletter>
    <!-- content -->
</sw-settings-newsletter>
```

## sw-settings-number-range-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `saveFinish` | |
| `onSave` | |
| `getProductNumberRanges` | |
| `onChangeType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productNumberRangeCriteria` | |
| `numberRangeTypeCriteria` | |
| `disableNumberRangeTypeSelect` | |

### Examples

#### Basic Usage
```twig
<sw-settings-number-range-create>
    <!-- content -->
</sw-settings-number-range-create>
```

## sw-settings-number-range-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `splitPattern` | |
| `getPreview` | |
| `getState` | |
| `loadSalesChannels` | |
| `onSave` | |
| `saveFinish` | |
| `onCancel` | |
| `onChangeLanguage` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangePattern` | |
| `onChangeType` | |
| `addSalesChannel` | |
| `removeSalesChannel` | |
| `noSalesChannelSelected` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `disableNumberRangeTypeSelect` | |
| `numberRangeRepository` | |
| `numberRangeCriteria` | |
| `numberRangeTypeRepository` | |
| `numberRangeTypeCriteria` | |
| `numberRangeTypeCriteriaGlobal` | |
| `salesChannelCriteria` | |
| `salesChannelRepository` | |
| `numberRangeSalesChannelsRepository` | |
| `selectedNumberRangeSalesChannels` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `showCustomFields` | |
| `numberRangeNameError` | |
| `numberRangeTypeIdError` | |
| `stateInput` | |
| `previewInput` | |

### Examples

#### Basic Usage
```twig
<sw-settings-number-range-detail>
    <!-- content -->
</sw-settings-number-range-detail>
```

## sw-settings-number-range-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `getNumberRangeColumns` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `onChangeLanguage` | |
| `onInlineEditSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `filters` | |
| `expandButtonClass` | |
| `collapseButtonClass` | |
| `numberRangeRepository` | |

### Examples

#### Basic Usage
```twig
<sw-settings-number-range-list>
    <!-- content -->
</sw-settings-number-range-list>
```

## sw-settings-payment-create

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |

### Examples

#### Basic Usage
```twig
<sw-settings-payment-create>
    <!-- content -->
</sw-settings-payment-create>
```

## sw-settings-payment-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSaveRule` | |
| `onDismissRule` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `saveFinish` | |
| `onSave` | |
| `onError` | |
| `onCancel` | |
| `setMediaItem` | |
| `setMediaFromSidebar` | |
| `onUnlinkLogo` | |
| `onDropMedia` | |
| `openMediaSidebar` | |
| `deletePaymentMethod` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isNewPaymentMethod` | |
| `identifier` | |
| `paymentMethodRepository` | |
| `ruleRepository` | |
| `mediaRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `ruleFilter` | |
| `showCustomFields` | |
| `paymentMethodCriteria` | |
| `forbidDelete` | |
| `technicalNameIsProvided` | |
| `paymentMethodNameError` | |
| `paymentMethodTechnicalNameError` | |

### Examples

#### Basic Usage
```twig
<sw-settings-payment-detail>
    <!-- content -->
</sw-settings-payment-detail>
```

## sw-settings-payment-overview

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadPaymentMethods` | |
| `onChangeLanguage` | |
| `togglePaymentMethodActive` | |
| `showActivationSuccessNotification` | |
| `showActivationErrorNotification` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customCards` | |
| `paymentMethodRepository` | |
| `paymentMethodCriteria` | |
| `isEmpty` | |
| `paymentMethodCards` | |

### Examples

#### Basic Usage
```twig
<sw-settings-payment-overview>
    <!-- content -->
</sw-settings-payment-overview>
```

## sw-settings-payment-sorting-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| paymentMethods | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| modal-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `applyChanges` | |
| `onSort` | |
| `isShopwareDefaultPaymentMethod` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `paymentMethodRepository` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-settings-payment/page/sw-settings-payment-overview/sw-settings-payment-overview.html.twig`
```twig
        <sw-settings-payment-sorting-modal
            v-if="showSortingModal"
            :payment-methods="paymentMethods"
            @modal-close="showSortingModal = false"
            @modal-save="loadPaymentMethods"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-settings-price-rounding

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemRounding | `any` | — | no |  |
| totalRounding | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeDecimals` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `itemIntervalDisabled` | |
| `totalIntervalDisabled` | |
| `showHeaderInfo` | |
| `showHeaderWarning` | |

### Examples

#### Example 1
Source: `sw-settings-currency/page/sw-settings-currency-detail/sw-settings-currency-detail.html.twig`
```twig
    <sw-settings-price-rounding
        :item-rounding="currency.itemRounding"
        :total-rounding="currency.totalRounding"
    />
</mt-card>
{% endblock %}

{% block sw_settings_currency_detail_content_card_country_price_rounding %}
<mt-card
    position-identifier="sw-settings-currency-detail-country-price-rounding"
    :title="$tc('sw-settings-currency.detail.titleCountryRoundingCard')"
    :is-loading="currencyCountryLoading"
>
    <template
        v-if="currency.id && !currency.isNew()"
```

#### Example 2
Source: `sw-settings-currency/component/sw-settings-currency-country-modal/sw-settings-currency-country-modal.html.twig`
```twig
<sw-settings-price-rounding
    :item-rounding="currencyCountryRounding.itemRounding"
    :total-rounding="currencyCountryRounding.totalRounding"
/>
{% endblock %}

{% block sw_settings_currency_country_modal_footer %}
<template #modal-footer>
    {% block sw_settings_currency_country_modal_footer_cancel %}
    <mt-button
        size="small"
        variant="secondary"
        @click="onCancel"
    >
        {{ $tc('global.default.cancel') }}
```

## sw-settings-product-feature-sets-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productFeatureSetId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntityData` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `productFeatureSetsRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `productFeatureSetNameError` | |
| `productFeatureSetDescriptionError` | |
| `productFeatureSetFeaturesIdError` | |

### Examples

#### Basic Usage
```twig
<sw-settings-product-feature-sets-detail>
    <!-- content -->
</sw-settings-product-feature-sets-detail>
```

## sw-settings-product-feature-sets-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `metaInfo` | |
| `getList` | |
| `onChangeLanguage` | |
| `onInlineEditSave` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `getProductFeatureSetsColumns` | |
| `renderFeaturePreview` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productFeatureSetsRepository` | |
| `propertyGroupRepository` | |
| `customFieldRepository` | |
| `featureGridTranslationService` | |

### Examples

#### Basic Usage
```twig
<sw-settings-product-feature-sets-list>
    <!-- content -->
</sw-settings-product-feature-sets-list>
```

## sw-settings-product-feature-sets-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productFeatureSet | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchCustomFields` | |
| `onSearchPropertyGroups` | |
| `onClickNext` | |
| `getProductInformationList` | |
| `getCustomFieldList` | |
| `getPropertyList` | |
| `getList` | |
| `getFeaturesIds` | |
| `onChangeOption` | |
| `checkIfReferencePriceIsSelected` | |
| `onConfirm` | |
| `setFeatures` | |
| `setFeatureSelection` | |
| `applySelectionsToActiveGrid` | |
| `getPropertyGroupColumns` | |
| `getCustomFieldColumns` | |
| `getProductInformationColumns` | |
| `paginateCustomFieldGrid` | |
| `paginatePropertyGroupGrid` | |
| `readCustomFieldLabel` | |
| `getCurrentSelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productFeatureSetRepository` | |
| `customFieldsRepository` | |
| `propertyGroupsRepository` | |
| `productFeatureSetCriteria` | |
| `customFieldCriteria` | |
| `propertyGroupCriteria` | |
| `referencePriceSelected` | |
| `propertyGroupColumns` | |
| `customFieldColumns` | |
| `productInformationColumns` | |
| `checkIfReferencePriceSelected` | |
| `settingOptions` | |
| `customFieldTotal` | |
| `propertyGroupTotal` | |
| `addButtonDisabled` | |

### Examples

#### Example 1
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-values-card/sw-settings-product-feature-sets-values-card.html.twig`
```twig
    <sw-settings-product-feature-sets-modal
        v-if="showModal"
        :product-feature-set="productFeatureSet"
        @modal-close="onModalClose"
    />
    {% endblock %}

</mt-card>
{% endblock %}

```

## sw-settings-product-feature-sets-values-card

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productFeatureSet | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| allowEdit | `any` | `true` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddField` | |
| `onGridSelectionChanged` | |
| `onSearch` | |
| `doSearch` | |
| `getList` | |
| `onModalClose` | |
| `onShowFeatureModal` | |
| `onDeleteFields` | |
| `onPositionChange` | |
| `resetPositions` | |
| `getColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productFeatureSetRepository` | |
| `propertyGroupRepository` | |
| `customFieldRepository` | |
| `valuesEmpty` | |
| `valuesCardClasses` | |
| `productFeatureSetCriteria` | |
| `featureGridTranslationService` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-settings-product-feature-sets/page/sw-settings-product-feature-sets-detail/sw-settings-product-feature-sets-detail.html.twig`
```twig
                <sw-settings-product-feature-sets-values-card
                    v-if="productFeatureSet.id"
                    :disabled="!productFeatureSetId || undefined"
                    :allow-edit="acl.can('product_feature_sets.editor') || undefined"
                    class="sw-settings-product-feature-sets-detail__tax-rule-grid"
                    :product-feature-set="productFeatureSet"
                    :is-loading="isLoading"
                    @product-feature-set-rule-save="onSave"
                />
                {% endblock %}
            </template>
        </sw-card-view>
    </template>
    {% endblock %}

```

## sw-settings-rule-add-assignment-listing

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | — | yes |  |
| entityContext | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| select-item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSelectItem` | |
| `isNotAssigned` | |
| `paginate` | |
| `doSearch` | |
| `shippingTaxTypeLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `criteria` | |
| `shippingCostTaxOptions` | |

### Examples

#### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-add-assignment-modal/sw-settings-rule-add-assignment-modal.html.twig`
```twig
<sw-settings-rule-add-assignment-listing
    v-else
    class="sw-settings-rule-detail-assignments__entity-listing"
    :entity-context="entityContext"
    :rule-id="rule.id"
    @select-item="onSelect"
/>
{% endblock %}

{% block sw_settings_rule_add_assignment_modal_footer %}
<template #modal-footer>

    {% block sw_settings_rule_add_assignment_modal_cancel %}
    <mt-button
        class="sw-settings-rule-add-assignment-modal__cancel-button"
```

## sw-settings-rule-add-assignment-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| entityContext | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close-add-modal | — | |
| entities-saved | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadEntities` | |
| `onCloseAddModal` | |
| `onAdd` | |
| `updateEntities` | |
| `insertEntities` | |
| `onSelect` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalSize` | |

### Examples

#### Example 1
Source: `sw-settings-rule/view/sw-settings-rule-detail-assignments/sw-settings-rule-detail-assignments.html.twig`
```twig
    <sw-settings-rule-add-assignment-modal
        v-if="addModal"
        :rule="rule"
        :entity-context="addEntityContext"
        @entities-saved="onEntitiesSaved"
        @close-add-modal="onCloseAddModal"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-settings-rule-assignment-listing

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| link-column | item: item, column: column | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| delete-items | — | |

### Methods

| Method | Description |
|--------|-------------|
| `deleteItems` | |

### Examples

#### Example 1
Source: `sw-settings-rule/view/sw-settings-rule-detail-assignments/sw-settings-rule-detail-assignments.html.twig`
```twig
<sw-settings-rule-assignment-listing
    v-if="entity.loadedData && entity.loadedData.length > 0"
    class="sw-settings-rule-detail-assignments__entity-listing"
    :class="`sw-settings-rule-detail-assignments__entity-listing-${entity.id}`"
    :is-loading="isLoading"
    :detail-route="entity.detailRoute"
    :data-source="entity.loadedData"
    :repository="entity.repository"
    :local-mode="false"
    :criteria-limit="5"
    :allow-delete="allowDeletion(entity) && acl.can('rule.editor')"
    :allow-inline-edit="false"
    :show-settings="false"
    :show-selection="allowDeletion(entity) && acl.can('rule.editor')"
    :allow-column-edit="false"
```

## sw-settings-rule-category-tree

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| association | `any` | — | yes |  |
| categoriesCollection | `any` | — | yes |  |
| hideHeadline | `any` | `false` | no |  |
| hideSearch | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| on-selection | — | |

### Methods

| Method | Description |
|--------|-------------|
| `searchTreeItems` | |
| `onCheckItem` | |
| `getTreeItems` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `categoryRepository` | |
| `treeCriteria` | |

### Examples

#### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-add-assignment-modal/sw-settings-rule-add-assignment-modal.html.twig`
```twig
<sw-settings-rule-category-tree
    v-if="entityContext.entityName === 'category'"
    :rule="rule"
    :association="entityContext.addContext.association"
    :categories-collection="entities"
    :hide-headline="true"
    :hide-search="true"
    placeholder="Add categories"
    @on-selection="onSelect"
/>
{% endblock %}

{% block sw_settings_rule_add_assignment_modal_listing %}
<sw-settings-rule-add-assignment-listing
    v-else
```

## sw-settings-rule-detail-assignments

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| conditions | `any` | `null` | no |  |
| detailPageLoading | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `disableAdd` | |
| `getTooltipConfig` | |
| `allowDeletion` | |
| `prepareAssociationEntitiesList` | |
| `onOpenDeleteModal` | |
| `onCloseDeleteModal` | |
| `onOpenAddModal` | |
| `onCloseAddModal` | |
| `onEntitiesSaved` | |
| `onDeleteItems` | |
| `onDelete` | |
| `doDeleteItem` | |
| `refreshAssignmentData` | |
| `onFilterEntity` | |
| `loadNotAssignedDataTotals` | |
| `getRouterLink` | |
| `loadAssociationData` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `getRuleAssignmentConfiguration` | |
| `associationEntitiesConfig` | |
| `assetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-settings-rule-detail-assignments
    rule="..."
>
    <!-- content -->
</sw-settings-rule-detail-assignments>
```

## sw-settings-rule-detail-base

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| rule | `any` | — | yes |  |
| conditions | `any` | `null` | no |  |
| conditionRepository | `any` | — | yes |  |
| isLoading | `any` | — | yes |  |
| ruleNameError | `any` | `null` | no |  |
| rulePriorityError | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| conditions-changed | — | |
| tree-finished-loading | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `hasProductStreamConditions` | |
| `hasConditionType` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `availableModuleTypes` | |
| `moduleTypes` | |
| `showCustomFields` | |
| `productStreamIndexingEnabled` | |
| `showProductStreamIndexingWarning` | |
| `showProductStateConditionWarning` | |

### Examples

#### Basic Usage
```twig
<sw-settings-rule-detail-base
    rule="..."
    conditionRepository="..."
>
    <!-- content -->
</sw-settings-rule-detail-base>
```

## sw-settings-rule-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| ruleId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `loadConditionData` | |
| `createRule` | |
| `loadEntityData` | |
| `extractEntityCount` | |
| `unsavedDataLeaveHandler` | |
| `checkUnsavedData` | |
| `setTreeFinishedLoading` | |
| `onLeaveModalClose` | |
| `onLeaveModalConfirm` | |
| `loadConditions` | |
| `conditionsChanged` | |
| `validateRuleAwareness` | |
| `getChildrenConditions` | |
| `validateDateRange` | |
| `onSave` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `saveRule` | |
| `syncConditions` | |
| `showErrorNotification` | |
| `tabHasError` | |
| `onCancel` | |
| `onDuplicate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `ruleRepository` | |
| `ruleCriteria` | |
| `appScriptConditionRepository` | |
| `conditionRepository` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `tabItems` | |
| `conditionTreeFlat` | |
| `ruleNameError` | |
| `rulePriorityError` | |

### Examples

#### Basic Usage
```twig
<sw-settings-rule-detail>
    <!-- content -->
</sw-settings-rule-detail>
```

## sw-settings-rule-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `onChangeLanguage` | |
| `onDuplicate` | |
| `onInlineEditSave` | |
| `updateCriteria` | |
| `getRuleColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `getRuleDefinition` | |
| `ruleRepository` | |
| `conditionFilterOptions` | |
| `groupFilterOptions` | |
| `associationFilterOptions` | |
| `listFilters` | |
| `listCriteria` | |
| `assignmentProperties` | |
| `dateFilter` | |

### Examples

#### Basic Usage
```twig
<sw-settings-rule-list>
    <!-- content -->
</sw-settings-rule-list>
```

## sw-settings-rule-tree-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| association | `any` | — | yes |  |
| hideActions | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `hasItemAssociation` | |

### Examples

#### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-category-tree/sw-settings-rule-category-tree.html.twig`
```twig
            <sw-settings-rule-tree-item
                v-for="item in treeItems"
                :key="item.id"
                :association="association"
                :item="item"
                :sortable="false"
                should-focus
                :mark-inactive="true"
                :hide-action="true"
                @check-item="checkItem"
            />
            {% endblock %}
        </template>
        <template
            v-if="hideHeadline"
```

#### Example 2
Source: `sw-settings-rule/component/sw-settings-rule-tree-item/sw-settings-rule-tree-item.html.twig`
```twig
<sw-settings-rule-tree-item
    v-for="child in item.children"
    :key="child.id"
    :association="association"
    :item="child"
    :dragged-item="draggedItem"
    :parent-scope="parentScope"
    :new-element-id="newElementId"
    :translation-context="translationContext"
    :on-change-route="onChangeRoute"
    :active-parent-ids="activeParentIds"
    :active-item-ids="activeItemIds"
    :mark-inactive="markInactive"
    :sortable="sortable"
    :should-focus="shouldFocus"
```

## sw-settings-rule-tree

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| check-item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `checkItem` | |
| `getTreeItems` | |

### Examples

#### Example 1
Source: `sw-settings-rule/component/sw-settings-rule-category-tree/sw-settings-rule-category-tree.html.twig`
```twig
<sw-settings-rule-tree
    ref="swTree"
    :allow-create-categories="false"
    :allow-delete-categories="false"
    :items="categories"
    after-id-property="afterCategoryId"
    :sortable="false"
    @get-tree-items="getTreeItems"
    @search-tree-items="searchTreeItems"
    @check-item="onCheckItem"
>
    {% block sw_settings_rule_category_tree_items %}
    <template
        #items="{
            treeItems,
```

#### Example 2
Source: `sw-settings-rule/component/sw-settings-rule-tree-item/sw-settings-rule-tree-item.html.twig`
```twig
<sw-settings-rule-tree-item
    v-for="child in item.children"
    :key="child.id"
    :association="association"
    :item="child"
    :dragged-item="draggedItem"
    :parent-scope="parentScope"
    :new-element-id="newElementId"
    :translation-context="translationContext"
    :on-change-route="onChangeRoute"
    :active-parent-ids="activeParentIds"
    :active-item-ids="activeItemIds"
    :mark-inactive="markInactive"
    :sortable="sortable"
    :should-focus="shouldFocus"
```

## sw-settings-salutation-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| salutationId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `onChangeLanguage` | |
| `saveFinish` | |
| `onSave` | |
| `onCancel` | |
| `onChange` | |
| `onChangeDebounce` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `salutationRepository` | |
| `entityDescription` | |
| `invalidKeyError` | |
| `allowSave` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `salutationDisplayNameError` | |
| `salutationLetterNameError` | |
| `salutationSalutationKeyError` | |
| `showCustomFields` | |

### Examples

#### Basic Usage
```twig
<sw-settings-salutation-detail>
    <!-- content -->
</sw-settings-salutation-detail>
```

## sw-settings-salutation-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getList` | |
| `getColumns` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `columns` | |
| `salutationRepository` | |
| `tooltipAdd` | |

### Examples

#### Basic Usage
```twig
<sw-settings-salutation-list>
    <!-- content -->
</sw-settings-salutation-list>
```

## sw-settings-search-example-modal

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
    <sw-settings-search-example-modal
        v-if="showExampleModal"
        @modal-close="onCloseExampleModal"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_settings_search_view_live_search_sales_channel %}
<sw-single-select
    class="sw-settings-search-live-search__sales-channel-select"
    value-property="id"
    label-property="translated.name"
    :placeholder="$tc('sw-settings-search.liveSearchTab.textPlaceholderSalesChannel')"
    :label="$tc('sw-settings-search.liveSearchTab.labelSalesChannelSelect')"
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
    <sw-settings-search-example-modal
        v-if="showExampleModal"
        @modal-close="onCloseExampleModal"
    />
    {% endblock %}
    {% endblock %}
</sw-container>
{% endblock %}

{% block sw_settings_search_searchable_content_tabs %}
<sw-tabs
    :default-item="defaultTab"
    position-identifier="sw-settings-search-searchable-content"
>
    <template #default="{ active }">
```

## sw-settings-search-excluded-search-terms

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchConfigs | `any` | `null` | no |  |
| isExcludedTermsLoading | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-change | — | |
| data-load | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `resetData` | |
| `addExcludedSearchTerms` | |
| `onInsertTerm` | |
| `renderComponent` | |
| `filterItems` | |
| `sliceItems` | |
| `onPagePagination` | |
| `onDeleteExcludedTerm` | |
| `onSearchTermChange` | |
| `selectionChanged` | |
| `onSaveEdit` | |
| `getOriginItem` | |
| `onCancelEdit` | |
| `onBulkDeleteExcludedTerm` | |
| `saveConfig` | |
| `onResetExcludedSearchTermDefault` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `searchRepository` | |
| `getSearchableGeneralColumns` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-settings-search/view/sw-settings-search-view-general/sw-settings-search-view-general.html.twig`
```twig
    <sw-settings-search-excluded-search-terms
        :search-configs="productSearchConfigs"
        :is-excluded-terms-loading="isLoading"
        @data-load="loadData"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-settings-search-live-search-keyword

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| text | `any` | `null` | yes |  |
| searchTerm | `any` | `null` | yes |  |
| highlightClass | `any` | `'sw-settings-search-live-search-keyword__highlight'` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getClass` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `textIsHighlighted` | |
| `parsedSearch` | |
| `parsedMsg` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
                    <sw-settings-search-live-search-keyword
                        :text="(item.name || item.translated.name)"
                        :search-term="liveSearchTerm"
                    />
                </sw-product-variant-info>
            </template>
            {% endblock %}

            {% block sw_settings_search_view_live_search_results_search_grid_score %}
            <template #column-score="{ item }">
                <span class="sw-settings-search-live-search__grid-result__score">
                    {{ Math.round(parseFloat(item.extensions.search._score)) }}
                </span>
            </template>
            {% endblock %}
```

## sw-settings-search-live-search

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentSalesChannelId | `any` | `null` | no |  |
| searchTerms | `any` | `null` | no |  |
| searchResults | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| live-search-results-change | — | |
| sales-channel-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `searchOnStorefront` | |
| `fetchSalesChannels` | |
| `fetchProductSortings` | |
| `changeSalesChannel` | |
| `onShowExampleModal` | |
| `onCloseExampleModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `salesChannelRepository` | |
| `productSortingRepository` | |
| `isSearchEnable` | |
| `searchColumns` | |
| `products` | |
| `productSortingCriteria` | |
| `searchParams` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
                    <sw-settings-search-live-search-keyword
                        :text="(item.name || item.translated.name)"
                        :search-term="liveSearchTerm"
                    />
                </sw-product-variant-info>
            </template>
            {% endblock %}

            {% block sw_settings_search_view_live_search_results_search_grid_score %}
            <template #column-score="{ item }">
                <span class="sw-settings-search-live-search__grid-result__score">
                    {{ Math.round(parseFloat(item.extensions.search._score)) }}
                </span>
            </template>
            {% endblock %}
```

#### Example 2
Source: `sw-settings-search/view/sw-settings-search-view-live-search/sw-settings-search-view-live-search.html.twig`
```twig
    <sw-settings-search-live-search
        v-bind="$props"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-settings-search-search-behaviour

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchBehaviourConfigs | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `conditionsOptions` | |

### Examples

#### Example 1
Source: `sw-settings-search/view/sw-settings-search-view-general/sw-settings-search-view-general.html.twig`
```twig
    <sw-settings-search-search-behaviour
        :is-loading="isLoading"
        :search-behaviour-configs="productSearchConfigs"
    />
    {% endblock %}

    {% block sw_settings_search_searchable_content_card %}
    <sw-settings-search-searchable-content
        :product-search-configs="productSearchConfigs"
        :search-config-id="searchConfigId"
    />
    {% endblock %}

    {% block sw_settings_search_excluded_search_terms_card %}
    <sw-settings-search-excluded-search-terms
```

## sw-settings-search-search-index

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `getLatestProductKeywordIndexed` | |
| `getTotalProduct` | |
| `updateProgress` | |
| `pollData` | |
| `clearPolling` | |
| `rebuildSearchIndex` | |
| `buildFinish` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productRepository` | |
| `productSearchKeywordRepository` | |
| `productCriteria` | |
| `productSearchKeywordsCriteria` | |

### Examples

#### Example 1
Source: `sw-settings-search/view/sw-settings-search-view-live-search/sw-settings-search-view-live-search.html.twig`
```twig
    <sw-settings-search-search-index
        v-if="!storefrontEsEnable"
        :is-loading="isLoading"
    />

    {% block sw_settings_search_view_live_search_content_card %}
    <sw-settings-search-live-search
        v-bind="$props"
    />
    {% endblock %}
</div>
{% endblock %}

```

## sw-settings-search-searchable-content-customfields

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isEmpty | `any` | — | yes |  |
| columns | `any` | — | yes |  |
| repository | `any` | — | yes |  |
| searchConfigs | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| config-add | — | |
| data-load | — | |
| config-save | — | |
| config-delete | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `showCustomFieldWithSet` | |
| `getMatchingCustomFields` | |
| `onSelectCustomField` | |
| `onAddField` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onResetRanking` | |
| `onRemove` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `customFieldRepository` | |
| `customFieldFilteredCriteria` | |
| `customFieldCriteria` | |
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
            <sw-settings-search-searchable-content-customfields
                v-if="active === tabNames.customTab"
                :is-empty="isListEmpty"
                :is-loading="isLoading"
                :columns="getProductSearchFieldColumns"
                :repository="productSearchFieldRepository"
                :search-configs="searchConfigFields"
                @data-load="loadData"
                @config-add="onAddNewConfig"
                @config-save="saveConfig"
                @config-delete="deleteConfig"
            />
        </template>
    </sw-tabs>
    {% endblock %}
```

## sw-settings-search-searchable-content-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isEmpty | `any` | — | yes |  |
| columns | `any` | — | yes |  |
| repository | `any` | — | yes |  |
| searchConfigs | `any` | — | no |  |
| fieldConfigs | `any` | — | yes |  |
| isLoading | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| data-load | — | |
| config-save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `getMatchingFields` | |
| `onSelectField` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onInlineEditItem` | |
| `onResetRanking` | |
| `getConfigRankingDefault` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
            <sw-settings-search-searchable-content-general
                v-if="active === tabNames.generalTab"
                :is-empty="isListEmpty"
                :is-loading="isLoading"
                :columns="getProductSearchFieldColumns"
                :repository="productSearchFieldRepository"
                :search-configs="searchConfigFields"
                :field-configs="fieldConfigs"
                @data-load="loadData"
                @config-save="saveConfig"
            />
            {% endblock %}

            <sw-settings-search-searchable-content-customfields
                v-if="active === tabNames.customTab"
```

## sw-settings-search-searchable-content

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| searchConfigId | `any` | — | yes |  |
| productSearchConfigs | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| edit-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onShowExampleModal` | |
| `onCloseExampleModal` | |
| `onAddNewConfig` | |
| `createNewConfigItem` | |
| `getConfigFieldDefault` | |
| `onResetToDefault` | |
| `onChangeTab` | |
| `loadData` | |
| `getProductSearchFieldsList` | |
| `saveConfig` | |
| `deleteConfig` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productSearchFieldRepository` | |
| `productSearchFieldCriteria` | |
| `isListEmpty` | |
| `getProductSearchFieldColumns` | |
| `storefrontEsEnable` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
            <sw-settings-search-searchable-content-general
                v-if="active === tabNames.generalTab"
                :is-empty="isListEmpty"
                :is-loading="isLoading"
                :columns="getProductSearchFieldColumns"
                :repository="productSearchFieldRepository"
                :search-configs="searchConfigFields"
                :field-configs="fieldConfigs"
                @data-load="loadData"
                @config-save="saveConfig"
            />
            {% endblock %}

            <sw-settings-search-searchable-content-customfields
                v-if="active === tabNames.customTab"
```

#### Example 2
Source: `sw-settings-search/view/sw-settings-search-view-general/sw-settings-search-view-general.html.twig`
```twig
    <sw-settings-search-searchable-content
        :product-search-configs="productSearchConfigs"
        :search-config-id="searchConfigId"
    />
    {% endblock %}

    {% block sw_settings_search_excluded_search_terms_card %}
    <sw-settings-search-excluded-search-terms
        :search-configs="productSearchConfigs"
        :is-excluded-terms-loading="isLoading"
        @data-load="loadData"
    />
    {% endblock %}
</div>
{% endblock %}
```

## sw-settings-search-view-general

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| productSearchConfigs | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| excluded-search-terms-load | — | |

### Methods

| Method | Description |
|--------|-------------|
| `loadData` | |

### Examples

#### Basic Usage
```twig
<sw-settings-search-view-general>
    <!-- content -->
</sw-settings-search-view-general>
```

## sw-settings-search-view-live-search

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentSalesChannelId | `any` | `null` | no |  |
| searchTerms | `any` | `null` | no |  |
| searchResults | `any` | — | no |  |
| isLoading | `any` | `false` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `storefrontEsEnable` | |

### Examples

#### Basic Usage
```twig
<sw-settings-search-view-live-search>
    <!-- content -->
</sw-settings-search-view-live-search>
```

## sw-settings-search

> Shopware Administration component.

- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `getProductSearchConfigs` | |
| `getDefaultSearchConfig` | |
| `createDefaultSearchConfig` | |
| `createConfigFields` | |
| `onSaveDefaultSearchConfig` | |
| `onChangeLanguage` | |
| `onTabChange` | |
| `onSaveSearchSettings` | |
| `saveFinish` | |
| `fetchSalesChannels` | |
| `unsavedDataLeaveHandler` | |
| `onSalesChannelChanged` | |
| `onLiveSearchResultsChanged` | |
| `onEditChanged` | |
| `onConfirmLeave` | |
| `onCloseLeaveModal` | |
| `onCancelLeaveModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `productSearchRepository` | |
| `productSearchFieldRepository` | |
| `productSearchConfigsCriteria` | |
| `productDefaultConfigsCriteria` | |
| `allowSave` | |
| `tooltipSave` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
    <sw-settings-search-example-modal
        v-if="showExampleModal"
        @modal-close="onCloseExampleModal"
    />
    {% endblock %}
</div>
{% endblock %}

{% block sw_settings_search_view_live_search_sales_channel %}
<sw-single-select
    class="sw-settings-search-live-search__sales-channel-select"
    value-property="id"
    label-property="translated.name"
    :placeholder="$tc('sw-settings-search.liveSearchTab.textPlaceholderSalesChannel')"
    :label="$tc('sw-settings-search.liveSearchTab.labelSalesChannelSelect')"
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
                    <sw-settings-search-live-search-keyword
                        :text="(item.name || item.translated.name)"
                        :search-term="liveSearchTerm"
                    />
                </sw-product-variant-info>
            </template>
            {% endblock %}

            {% block sw_settings_search_view_live_search_results_search_grid_score %}
            <template #column-score="{ item }">
                <span class="sw-settings-search-live-search__grid-result__score">
                    {{ Math.round(parseFloat(item.extensions.search._score)) }}
                </span>
            </template>
            {% endblock %}
```

#### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
    <sw-settings-search-example-modal
        v-if="showExampleModal"
        @modal-close="onCloseExampleModal"
    />
    {% endblock %}
    {% endblock %}
</sw-container>
{% endblock %}

{% block sw_settings_search_searchable_content_tabs %}
<sw-tabs
    :default-item="defaultTab"
    position-identifier="sw-settings-search-searchable-content"
>
    <template #default="{ active }">
```

#### Example 4
Source: `sw-settings-search/component/sw-settings-search-searchable-content/sw-settings-search-searchable-content.html.twig`
```twig
            <sw-settings-search-searchable-content-general
                v-if="active === tabNames.generalTab"
                :is-empty="isListEmpty"
                :is-loading="isLoading"
                :columns="getProductSearchFieldColumns"
                :repository="productSearchFieldRepository"
                :search-configs="searchConfigFields"
                :field-configs="fieldConfigs"
                @data-load="loadData"
                @config-save="saveConfig"
            />
            {% endblock %}

            <sw-settings-search-searchable-content-customfields
                v-if="active === tabNames.customTab"
```

#### Example 5
Source: `sw-settings-search/view/sw-settings-search-view-general/sw-settings-search-view-general.html.twig`
```twig
    <sw-settings-search-search-behaviour
        :is-loading="isLoading"
        :search-behaviour-configs="productSearchConfigs"
    />
    {% endblock %}

    {% block sw_settings_search_searchable_content_card %}
    <sw-settings-search-searchable-content
        :product-search-configs="productSearchConfigs"
        :search-config-id="searchConfigId"
    />
    {% endblock %}

    {% block sw_settings_search_excluded_search_terms_card %}
    <sw-settings-search-excluded-search-terms
```

## sw-settings-seo

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `onClickSave` | |
| `onLoadingChanged` | |

### Examples

#### Basic Usage
```twig
<sw-settings-seo>
    <!-- content -->
</sw-settings-seo>
```

## sw-settings-services-dashboard-banner

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `hideBanner` | |

### Examples

#### Example 1
Source: `sw-dashboard/page/sw-dashboard-index/sw-dashboard-index.html.twig`
```twig
<sw-settings-services-dashboard-banner />
```

## sw-settings-services-grant-permissions-modal

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `prepareRevisions` | |
| `grantPermissions` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `feedbackLink` | |
| `showGrantPermissionsModal` | |

### Examples

#### Basic Usage
```twig
<sw-settings-services-grant-permissions-modal>
    <!-- content -->
</sw-settings-services-grant-permissions-modal>
```

## sw-settings-services-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `activateServices` | |
| `reloadServices` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `config` | |
| `currentRevision` | |
| `consentGiven` | |

### Examples

#### Basic Usage
```twig
<sw-settings-services-index>
    <!-- content -->
</sw-settings-services-index>
```

## sw-settings-shipping-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| shippingMethodId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSaveRule` | |
| `loadCurrencies` | |
| `loadEntityData` | |
| `loadCustomFieldSets` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `onSave` | |
| `onError` | |
| `filterIncompletePrices` | |
| `getIncompletePrices` | |
| `onCancel` | |
| `setMediaItem` | |
| `onDropMedia` | |
| `setMediaFromSidebar` | |
| `onUnlinkLogo` | |
| `openMediaSidebar` | |
| `sortCurrencies` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `currencies` | |
| `restrictedRuleIds` | |
| `shippingMethodNameError` | |
| `shippingMethodTechnicalNameError` | |
| `shippingMethodDeliveryTimeIdError` | |
| `shippingMethodAvailabilityRuleIdError` | |
| `identifier` | |
| `shippingMethodRepository` | |
| `shippingMethodPricesRepository` | |
| `currencyRepository` | |
| `isNewShippingMethod` | |
| `mediaRepository` | |
| `deliveryTimeRepository` | |
| `deliveryTimeCriteria` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `ruleFilter` | |
| `shippingMethodCriteria` | |
| `showCustomFields` | |

### Examples

#### Basic Usage
```twig
<sw-settings-shipping-detail>
    <!-- content -->
</sw-settings-shipping-detail>
```

## sw-settings-shipping-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `onInlineEditSave` | |
| `onDelete` | |
| `onConfirmDelete` | |
| `onCloseDeleteModal` | |
| `onChangeLanguage` | |
| `shippingTaxTypeLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shippingRepository` | |
| `columns` | |
| `listingCriteria` | |
| `shippingCostTaxOptions` | |

### Examples

#### Basic Usage
```twig
<sw-settings-shipping-list>
    <!-- content -->
</sw-settings-shipping-list>
```

## sw-settings-shipping-price-matrices

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `onAddNewPriceGroup` | |
| `onDeletePriceMatrix` | |
| `onDuplicatePriceMatrix` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `shippingPriceGroups` | |
| `usedRules` | |
| `unrestrictedPriceMatrixExists` | |
| `newPriceMatrixExists` | |
| `ruleRepository` | |
| `ruleFilter` | |
| `shippingPriceRepository` | |
| `isLoaded` | |

### Examples

#### Example 1
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
            <sw-settings-shipping-price-matrices
                v-if="!isLoading"
                ref="priceMatrices"
                :disabled="!acl.can('shipping.editor') || undefined"
            />
            {% endblock %}
            <sw-skeleton v-else />

            {% block sw_settings_shipping_detail_custom_field_sets %}
            <mt-card
                v-if="showCustomFields"
                position-identifier="sw-settings-shipping-detail-custom-fields"
                :title="$tc('sw-settings-custom-field.general.mainMenuItemGeneral')"
                :is-loading="isLoading"
            >
```

## sw-settings-shipping-price-matrix

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| priceGroup | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| duplicate-price-matrix | — | |
| delete-price-matrix | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onAddNewShippingPrice` | |
| `onSaveMainRule` | |
| `onSaveCustomShippingRule` | |
| `onCalculationChange` | |
| `onDeletePriceMatrix` | |
| `onConfirmDeleteShippingPrice` | |
| `onCloseDeleteModal` | |
| `onDeleteShippingPrice` | |
| `convertDefaultPriceToCurrencyPrice` | |
| `initCurrencyPrice` | |
| `getPrice` | |
| `setPrice` | |
| `getPriceOfCurrency` | |
| `convertPrice` | |
| `onQuantityEndChange` | |
| `updateShowAllPrices` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `currencies` | |
| `restrictedRuleIds` | |
| `unrestrictedPriceMatrixExists` | |
| `newPriceMatrixExists` | |
| `defaultCurrency` | |
| `ruleRepository` | |
| `shippingPriceRepository` | |
| `labelQuantityStart` | |
| `labelQuantityEnd` | |
| `numberFieldType` | |
| `confirmDeleteText` | |
| `currencyColumns` | |
| `showDataGrid` | |
| `disableDeleteButton` | |
| `ruleFilterCriteria` | |
| `shippingRuleFilterCriteria` | |
| `isRuleMatrix` | |
| `usedCalculationRules` | |
| `mainRulePlaceholder` | |
| `cardTitle` | |
| `prices` | |

### Examples

#### Example 1
Source: `sw-settings-shipping/component/sw-settings-shipping-price-matrices/sw-settings-shipping-price-matrices.html.twig`
```twig
<sw-settings-shipping-price-matrix
    v-for="priceGroup in shippingPriceGroups"
    :key="priceGroup.ruleId"
    :price-group="priceGroup"
    :disabled="disabled || undefined"
    @duplicate-price-matrix="onDuplicatePriceMatrix"
    @delete-price-matrix="onDeletePriceMatrix"
/>
{% endblock %}

{% block sw_settings_shipping_detail_advanced_prices_actions %}
<div class="sw-settings-shipping-price-matrices__actions">
    {% block sw_settings_shipping_detail_advanced_prices_actions_add_button %}
    <mt-button
        v-tooltip="{
```

## sw-settings-shipping-tax-cost

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabled | `any` | `false` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `getTaxLabel` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shippingMethod` | |
| `currencies` | |
| `defaultCurrency` | |
| `usedRules` | |
| `unrestrictedPriceMatrixExists` | |
| `newPriceMatrixExists` | |
| `shippingMethodTaxTypeError` | |
| `shippingMethodTaxIdError` | |
| `shippingCostTaxOptions` | |
| `taxCriteria` | |
| `taxType` | |

### Examples

#### Example 1
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
<sw-settings-shipping-tax-cost
    v-if="!isLoading"
    :disabled="!acl.can('shipping.editor') || undefined"
/>
{% endblock %}
<sw-skeleton v-else />

{% block sw_settings_shipping_detail_price_matrices %}
<sw-settings-shipping-price-matrices
    v-if="!isLoading"
    ref="priceMatrices"
    :disabled="!acl.can('shipping.editor') || undefined"
/>
{% endblock %}
<sw-skeleton v-else />
```

## sw-settings-shopware-updates-index

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `searchForUpdates` | |
| `openUpdateWizard` | |
| `saveFinish` | |
| `onSave` | |
| `onLoadingChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `shopwareVersion` | |

### Examples

#### Basic Usage
```twig
<sw-settings-shopware-updates-index>
    <!-- content -->
</sw-settings-shopware-updates-index>
```

## sw-settings-shopware-updates-info

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| changelog | `any` | — | yes |  |
| isLoading | `any` | — | no |  |

### Examples

#### Example 1
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
    <sw-settings-shopware-updates-info
        v-if="updateInfo"
        :is-loading="isLoading"
        :changelog="updateInfo.body"
    />
    <sw-settings-shopware-updates-requirements
        :is-loading="isLoading"
        :update-info="updateInfo"
        :requirements="requirements"
    />
    <sw-settings-shopware-updates-plugins
        :plugins="plugins"
        :is-loading="isLoading"
    />
</sw-card-view>
```

## sw-settings-shopware-updates-plugins

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isLoading | `any` | — | no |  |
| plugins | `any` | — | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `openMyExtensions` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `columns` | |

### Examples

#### Example 1
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
    <sw-settings-shopware-updates-plugins
        :plugins="plugins"
        :is-loading="isLoading"
    />
</sw-card-view>

<mt-empty-state
    v-if="!isLoading && !updateInfo.version"
    :centered="true"
    :icon="$route.meta.$module.icon"
    :headline="$tc('sw-settings-shopware-updates.general.emptyState')"
/>

<sw-modal
    v-if="updaterIsRunning"
```

## sw-settings-shopware-updates-requirements

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| updateInfo | `any` | — | yes |  |
| requirements | `any` | — | yes |  |
| isLoading | `any` | — | no |  |

### Examples

#### Example 1
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
    <sw-settings-shopware-updates-requirements
        :is-loading="isLoading"
        :update-info="updateInfo"
        :requirements="requirements"
    />
    <sw-settings-shopware-updates-plugins
        :plugins="plugins"
        :is-loading="isLoading"
    />
</sw-card-view>

<mt-empty-state
    v-if="!isLoading && !updateInfo.version"
    :centered="true"
    :icon="$route.meta.$module.icon"
```

## sw-settings-shopware-updates-wizard

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update-started | — | |
| update-stopped | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onRequirementsResponse` | |
| `startUpdateProcess` | |
| `stopUpdateProcess` | |
| `downloadRecovery` | |
| `deactivatePlugins` | |
| `redirectToPage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `updatePossible` | |
| `updateButtonTooltip` | |
| `displayIncompatiblePluginsWarning` | |
| `displayUnknownPluginsWarning` | |
| `displayAllPluginsOkayInfo` | |
| `optionDeactivateIncompatibleTranslation` | |
| `optionDeactivateAllTranslation` | |

### Examples

#### Basic Usage
```twig
<sw-settings-shopware-updates-wizard>
    <!-- content -->
</sw-settings-shopware-updates-wizard>
```

## sw-settings-sitemap

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `onSave` | |
| `onLoadingChanged` | |

### Examples

#### Basic Usage
```twig
<sw-settings-sitemap>
    <!-- content -->
</sw-settings-sitemap>
```

## sw-settings-snippet-create

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-settings-snippet-create>
    <!-- content -->
</sw-settings-snippet-create>
```

## sw-settings-snippet-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `prepareContent` | |
| `initializeSnippet` | |
| `applySnippetsToDummies` | |
| `createSnippetDummy` | |
| `saveFinish` | |
| `onSave` | |
| `onChange` | |
| `doChange` | |
| `onNewKeyRedirect` | |
| `getCustomList` | |
| `checkIsSaveable` | |
| `getNoPermissionsTooltip` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `snippetRepository` | |
| `snippetSetRepository` | |
| `snippetSetCriteria` | |
| `backPath` | |
| `invalidKeyError` | |
| `currentAuthor` | |

### Examples

#### Basic Usage
```twig
<sw-settings-snippet-detail>
    <!-- content -->
</sw-settings-snippet-detail>
```

## sw-settings-snippet-filter-switch

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `any` | `''` | no |  |
| name | `any` | — | yes |  |
| group | `any` | `null` | no |  |
| borderTop | `any` | `false` | no |  |
| borderBottom | `any` | `false` | no |  |
| type | `any` | `'small'` | no |  |
| value | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| template | — | |
| field | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `fieldClasses` | |

### Examples

#### Example 1
Source: `sw-settings-snippet/component/sidebar/sw-settings-snippet-sidebar/sw-settings-snippet-sidebar.html.twig`
```twig
<sw-settings-snippet-filter-switch
    name="emptySnippets"
    group="emptySnippets"
    type="small"
    :value="filterSettings?.emptySnippets"
    :label="$tc('sw-settings-snippet.filter.showOnlyEmpty')"
    @update:value="onChange"
/>
{% endblock %}

{% block sw_settings_snippet_grid_sidebar_filter_custom %}
<sw-settings-snippet-filter-switch
    name="editedSnippets"
    group="editedSnippets"
    type="small"
```

#### Example 2
Source: `sw-settings-snippet/component/sidebar/sw-settings-snippet-sidebar/sw-settings-snippet-sidebar.html.twig`
```twig
            <sw-settings-snippet-filter-switch
                group="authorFilter"
                :name="item"
                :value="filterSettings?.[item]"
                :label="item"
                @update:value="onChange"
            />
        </div>
    </template>
</sw-sidebar-collapse>
{% endblock %}

{% block sw_settings_snippet_grid_sidebar_filter_more %}
<sw-sidebar-collapse :expand-on-loading="isExpandedMoreFilters">
    <template #header>
```

## sw-settings-snippet-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeDestroyComponent` | |
| `addEventListeners` | |
| `removeEventListeners` | |
| `beforeUnloadListener` | |
| `getFilterSettings` | |
| `getUserConfig` | |
| `saveUserConfig` | |
| `createFilterSettings` | |
| `getList` | |
| `getColumns` | |
| `initializeSnippetSet` | |
| `prepareGrid` | |
| `onEdit` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onEmptyClick` | |
| `onSearch` | |
| `backRoutingError` | |
| `inlineSaveSuccessMessage` | |
| `inlineSaveErrorMessage` | |
| `onReset` | |
| `getName` | |
| `onSelectionChanged` | |
| `onCloseDeleteModal` | |
| `onConfirmReset` | |
| `createSuccessMessage` | |
| `createResetErrorNote` | |
| `onChange` | |
| `onSidebarClose` | |
| `onSortColumn` | |
| `onPageChange` | |
| `getNoPermissionsTooltip` | |
| `onResetAll` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `columns` | |
| `snippetRepository` | |
| `snippetSetRepository` | |
| `queryIds` | |
| `snippetSetCriteria` | |
| `queryIdCount` | |
| `metaName` | |
| `filter` | |
| `contextMenuEditSnippet` | |
| `hasActiveFilters` | |
| `activeFilters` | |

### Examples

#### Basic Usage
```twig
<sw-settings-snippet-list>
    <!-- content -->
</sw-settings-snippet-list>
```

## sw-settings-snippet-set-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `loadBaseFiles` | |
| `onAddSnippetSet` | |
| `toggleInlineEdit` | |
| `onInlineEditSave` | |
| `onEditSnippetSets` | |
| `onSelectionChanged` | |
| `onInlineEditCancel` | |
| `onDeleteSet` | |
| `onConfirmDelete` | |
| `closeDeleteModal` | |
| `onClone` | |
| `closeCloneModal` | |
| `onConfirmClone` | |
| `createDeleteSuccessNote` | |
| `createDeleteErrorNote` | |
| `createInlineSuccessNote` | |
| `createInlineErrorNote` | |
| `createCloneSuccessNote` | |
| `createCloneErrorNote` | |
| `createNotEditableErrorNote` | |
| `getNoPermissionsTooltip` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `snippetSetRepository` | |
| `snippetSetCriteria` | |
| `contextMenuEditSnippet` | |
| `dateFilter` | |
| `baseFileOptions` | |
| `snippetSetColumns` | |

### Examples

#### Basic Usage
```twig
<sw-settings-snippet-set-list>
    <!-- content -->
</sw-settings-snippet-set-list>
```

## sw-settings-snippet-sidebar

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filterItems | `any` | — | yes |  |
| authorFilters | `any` | — | yes |  |
| filterSettings | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sw-sidebar-close | — | |
| sw-sidebar-open | — | |
| change | — | |
| sw-sidebar-collaps-refresh-grid | — | |
| sidebar-reset-all | — | |

### Methods

| Method | Description |
|--------|-------------|
| `closeContent` | |
| `onChange` | |
| `onRefresh` | |
| `resetAll` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `activeFilterNumber` | |
| `isExpandedAuthorFilters` | |
| `isExpandedMoreFilters` | |

### Examples

#### Example 1
Source: `sw-settings-snippet/page/sw-settings-snippet-list/sw-settings-snippet-list.html.twig`
```twig
        <sw-settings-snippet-sidebar
            class="sw-settings-snippet-list__grid-sidebar"
            :filter-items="filterItems"
            :author-filters="authorFilters"
            :filter-settings="filterSettings"
            @sidebar-reset-all="onResetAll"
            @change="onChange"
            @sw-sidebar-collaps-refresh-grid="getList"
            @sw-sidebar-close="onSidebarClose"
        />
        {% endblock %}
    </template>

    {% endblock %}

```

## sw-settings-state-machine-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| stateMachineId | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadStateMachine` | |
| `onChangeLanguage` | |
| `onCancel` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `stateMachineRepository` | |
| `allowSave` | |
| `tooltipSave` | |
| `tooltipCancel` | |
| `stateMachineNameError` | |

### Examples

#### Basic Usage
```twig
<sw-settings-state-machine-detail
    stateMachineId="..."
>
    <!-- content -->
</sw-settings-state-machine-detail>
```

## sw-settings-state-machine-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadStateMachines` | |
| `onChangeLanguage` | |
| `onInlineEditCancel` | |
| `onInlineEditSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineRepository` | |
| `stateMachineColumns` | |

### Examples

#### Basic Usage
```twig
<sw-settings-state-machine-list>
    <!-- content -->
</sw-settings-state-machine-list>
```

## sw-settings-state-machine-state-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| currentStateMachineState | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onCancel` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineStateNameError` | |

### Examples

#### Example 1
Source: `sw-settings-state-machine/component/sw-settings-state-machine-state-list/sw-settings-state-machine-state-list.html.twig`
```twig
    <sw-settings-state-machine-state-detail
        v-if="currentStateMachineState !== null"
        :current-state-machine-state="currentStateMachineState"
        @modal-close="onModalClose"
    />
    {% endblock %}
</mt-card>
{% endblock %}

```

## sw-settings-state-machine-state-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| stateMachineId | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadStateMachineStates` | |
| `onInlineEditCancel` | |
| `onInlineEditSave` | |
| `showModal` | |
| `onModalClose` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateMachineStateRepository` | |
| `stateMachineStateCriteria` | |
| `stateMachineStateColumns` | |

### Examples

#### Example 1
Source: `sw-settings-state-machine/page/sw-settings-state-machine-detail/sw-settings-state-machine-detail.html.twig`
```twig
            <sw-settings-state-machine-state-list
                ref="stateMachineStateList"
                :state-machine-id="stateMachineId"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

## sw-settings-store

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `saveFinish` | |
| `onSave` | |
| `trimHost` | |
| `onLoadingChanged` | |

### Examples

#### Basic Usage
```twig
<sw-settings-store>
    <!-- content -->
</sw-settings-store>
```

## sw-settings-tag-detail-assignments

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| tag | `any` | — | yes |  |
| toBeAdded | `any` | — | yes |  |
| toBeDeleted | `any` | — | yes |  |
| initialCounts | `any` | — | no |  |
| property | `any` | `null` | no |  |
| entity | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| remove-assignment | — | |
| add-assignment | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `search` | |
| `addTagAggregations` | |
| `searchInheritedEntities` | |
| `onTermChange` | |
| `onAssignmentChange` | |
| `onSelectionChange` | |
| `getCount` | |
| `countIncrease` | |
| `countDecrease` | |
| `isInherited` | |
| `parentHasTags` | |
| `hasInheritedTag` | |
| `onPageChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `tagDefinition` | |
| `isInheritable` | |
| `assignmentAssociations` | |
| `assignmentAssociationsColumns` | |
| `entityRepository` | |
| `entityCriteria` | |
| `entitiesColumns` | |
| `selectedAssignments` | |
| `totalAssignments` | |

### Examples

#### Example 1
Source: `sw-settings-tag/component/sw-settings-tag-detail-modal/sw-settings-tag-detail-modal.html.twig`
```twig
            <sw-settings-tag-detail-assignments
                :tag="tag"
                :initial-counts="computedCounts"
                :to-be-added="assignmentsToBeAdded"
                :to-be-deleted="assignmentsToBeDeleted"
                :property="property"
                :entity="entity"
                @add-assignment="addAssignment"
                @remove-assignment="removeAssignment"
            />
            {% endblock %}
        </template>
    </template>
</sw-tabs>
{% endblock %}
```

## sw-settings-tag-detail-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| editedTag | `any` | `null` | no |  |
| counts | `any` | — | no |  |
| property | `any` | `null` | no |  |
| entity | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| close | — | |
| finish | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSave` | |
| `onCancel` | |
| `addAssignment` | |
| `removeAssignment` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `tagRepository` | |
| `tagDefinition` | |
| `tagNameError` | |
| `title` | |
| `allowSave` | |
| `tooltipSave` | |
| `computedCounts` | |

### Examples

#### Example 1
Source: `sw-settings-tag/page/sw-settings-tag-list/sw-settings-tag-list.html.twig`
```twig
        <sw-settings-tag-detail-modal
            v-if="showDetailModal === item.id"
            :edited-tag="item"
            :counts="getCounts(item.id)"
            :property="detailProperty"
            :entity="detailEntity"
            @finish="onSaveFinish"
            @close="onCloseDetailModal"
        />
        {% endblock %}
    </template>
    {% endblock %}
</sw-entity-listing>
{% endblock %}

```

## sw-settings-tag-list

> Shopware Administration component.

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| bulk-modal-merge-confirm-text | — | |
| bulk-modal-merge-confirm-name-input | — | |
| bulk-modal-merge-progress | — | |
| bulk-modal-merge-footer | — | |

### Methods

| Method | Description |
|--------|-------------|
| `setAggregations` | |
| `getList` | |
| `sortByIdsOrder` | |
| `getCounts` | |
| `getPropertyCounting` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `onDuplicate` | |
| `onCloseDuplicateModal` | |
| `onConfirmDuplicate` | |
| `onDetail` | |
| `onCloseDetailModal` | |
| `onCloseBulkMergeModal` | |
| `onMergeTags` | |
| `getBulkMergeMessageGlue` | |
| `onSaveFinish` | |
| `onFilter` | |
| `resetFilters` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `tagRepository` | |
| `tagDefinition` | |
| `assignmentProperties` | |
| `tagCriteria` | |
| `tagColumns` | |
| `assignmentFilterOptions` | |
| `hasAssignmentFilter` | |
| `filterCount` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tag-list>
    <!-- content -->
</sw-settings-tag-list>
```

## sw-settings-tax-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadCustomFieldSets` | |
| `onSave` | |
| `onCancel` | |
| `abortOnLanguageChange` | |
| `saveOnLanguageChange` | |
| `onChangeLanguage` | |
| `changeName` | |
| `reloadDefaultTaxRate` | |
| `onChangeDefaultTaxRate` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `identifier` | |
| `taxRepository` | |
| `taxNameError` | |
| `taxTaxRateError` | |
| `isNewTax` | |
| `allowSave` | |
| `tooltipSave` | |
| `isShopwareDefaultTax` | |
| `label` | |
| `showCustomFields` | |
| `isDefaultTaxRate` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-detail>
    <!-- content -->
</sw-settings-tax-detail>
```

## sw-settings-tax-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `getList` | |
| `editLink` | |
| `onChangeLanguage` | |
| `onInlineEditSave` | |
| `onInlineEditCancel` | |
| `onDelete` | |
| `onCloseDeleteModal` | |
| `onConfirmDelete` | |
| `getTaxColumns` | |
| `isShopwareDefaultTax` | |
| `getLabel` | |
| `isSelectedDefaultRate` | |
| `setSelectedDefaultRate` | |
| `getDefaultTaxRate` | |
| `loadTaxProviders` | |
| `onChangeTaxProviderActive` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `taxRepository` | |
| `taxProviderRepository` | |
| `taxProviderCriteria` | |
| `showChangePriority` | |
| `noTaxProvidersFound` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-list>
    <!-- content -->
</sw-settings-tax-list>
```

## sw-settings-tax-provider-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxProviderId | `any` | `''` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadTaxProvider` | |
| `onSave` | |
| `onCancel` | |
| `onSaveRule` | |
| `onDismissRule` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `label` | |
| `taxProviderRepository` | |
| `allowSave` | |
| `ruleFilter` | |
| `hasIdentifier` | |
| `positionIdentifier` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-provider-detail>
    <!-- content -->
</sw-settings-tax-provider-detail>
```

## sw-settings-tax-provider-sorting-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxProviders | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `closeModal` | |
| `applyChanges` | |
| `onSort` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `taxProviderRepository` | |

### Examples

#### Example 1
Source: `sw-settings-tax/page/sw-settings-tax-list/sw-settings-tax-list.html.twig`
```twig
            <sw-settings-tax-provider-sorting-modal
                v-if="showSortingModal"
                :tax-providers="taxProviders"
                @modal-close="showSortingModal = false"
                @modal-save="loadTaxProviders"
            />
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
    {% endblock %}
{% endblock %}

```

## sw-settings-tax-rule-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| tax | `any` | — | yes |  |
| currentRule | `any` | `null` | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `changeRuleType` | |
| `createdComponent` | |
| `onConfirm` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `taxRuleRepository` | |
| `taxRuleTypeRepository` | |
| `additionalComponent` | |
| `taxRuleTypeCriteria` | |
| `countryCriteria` | |
| `taxRuleTaxRuleTypeIdError` | |
| `taxRuleCountryIdError` | |
| `taxRuleTaxRateError` | |
| `taxRuleActiveFromError` | |

### Examples

#### Example 1
Source: `sw-settings-tax/component/sw-tax-rule-card/sw-tax-rule-card.html.twig`
```twig
<sw-settings-tax-rule-modal
    v-if="showModal"
    :tax="tax"
    :current-rule="currentRule"
    @modal-close="onModalClose"
/>
{% endblock %}

{% block sw_tax_rule_card_empty_state %}
<template v-if="taxRulesEmpty || disabled">
    <div class="sw-settings-tax-rule-card__empty-state">
        {% block sw_tax_rule_card_empty_state_image %}
        <img
            :src="assetFilter('administration/administration/static/img/empty-states/settings-empty-state.svg')"
            alt=""
```

## sw-settings-tax-rule-type-individual-states-cell

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxRule | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadStates` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `stateRepository` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-rule-type-individual-states-cell
    taxRule="..."
>
    <!-- content -->
</sw-settings-tax-rule-type-individual-states-cell>
```

## sw-settings-tax-rule-type-individual-states

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxRule | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onChange` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `exclusionCriteria` | |
| `stateRepository` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-rule-type-individual-states
    taxRule="..."
>
    <!-- content -->
</sw-settings-tax-rule-type-individual-states>
```

## sw-settings-tax-rule-type-zip-code-cell

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxRule | `any` | — | yes |  |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-rule-type-zip-code-cell
    taxRule="..."
>
    <!-- content -->
</sw-settings-tax-rule-type-zip-code-cell>
```

## sw-settings-tax-rule-type-zip-code-range-cell

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxRule | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-rule-type-zip-code-range-cell
    taxRule="..."
>
    <!-- content -->
</sw-settings-tax-rule-type-zip-code-range-cell>
```

## sw-settings-tax-rule-type-zip-code-range

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxRule | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-rule-type-zip-code-range
    taxRule="..."
>
    <!-- content -->
</sw-settings-tax-rule-type-zip-code-range>
```

## sw-settings-tax-rule-type-zip-code

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| taxRule | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-settings-tax-rule-type-zip-code
    taxRule="..."
>
    <!-- content -->
</sw-settings-tax-rule-type-zip-code>
```

## sw-settings-units-detail

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| unitId | `any` | `null` | no |  |

### Methods

| Method | Description |
|--------|-------------|
| `loadUnit` | |
| `onSave` | |
| `onChangeLanguage` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `unitRepository` | |
| `customFieldSetRepository` | |
| `customFieldSetCriteria` | |
| `unitNameError` | |
| `unitShortCodeError` | |

### Examples

#### Basic Usage
```twig
<sw-settings-units-detail>
    <!-- content -->
</sw-settings-units-detail>
```

## sw-settings-units-list

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `createUnitsCriteria` | |
| `loadUnits` | |
| `createNewUnit` | |
| `saveUnit` | |
| `cancelUnit` | |
| `deleteUnit` | |
| `activateInlineEdit` | |
| `unitColumns` | |
| `onChangeLanguage` | |
| `editUnit` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `unitRepository` | |
| `unitList` | |
| `isEmpty` | |
| `tooltipCreate` | |
| `isAddingUnitsDisabled` | |

### Examples

#### Basic Usage
```twig
<sw-settings-units-list>
    <!-- content -->
</sw-settings-units-list>
```

## sw-settings-usage-data-consent-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialStoreDataConsent | `any` | — | yes |  |
| initialUserDataConsent | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `savePreferences` | |
| `shareAll` | |
| `shareNothing` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `showConsentModal` | |
| `showStoreDataConsent` | |
| `showSavePreferences` | |

### Examples

#### Basic Usage
```twig
<sw-settings-usage-data-consent-modal
    initialStoreDataConsent="..."
    initialUserDataConsent="..."
>
    <!-- content -->
</sw-settings-usage-data-consent-modal>
```

## sw-settings-usage-data-general

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |

### Examples

#### Basic Usage
```twig
<sw-settings-usage-data-general>
    <!-- content -->
</sw-settings-usage-data-general>
```

## sw-settings-usage-data-profile-consent

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `updateConsent` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `unionPath` | |

### Examples

#### Example 1
Source: `sw-profile/view/sw-profile-index-privacy-preferences/sw-profile-index-privacy-preferences.html.twig`
```twig
<sw-settings-usage-data-profile-consent />
```

## sw-settings-usage-data

> Shopware Administration component.

### Examples

#### Example 1
Source: `sw-profile/view/sw-profile-index-privacy-preferences/sw-profile-index-privacy-preferences.html.twig`
```twig
<sw-settings-usage-data-profile-consent />
```

#### Example 2
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<sw-settings-usage-data-consent-check-list />
```

#### Example 3
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<sw-settings-usage-data-store-data-consent-card
    v-if="showStoreDataConsent"
    v-model:consent="storeDataConsent"
/>
<sw-settings-usage-data-user-data-consent-card v-model:consent="userDataConsent" />

<div class="sw-setting-usage-data-consent-modal__legal">
    <p>{{ $tc('sw-settings-usage-data.consent-modal.opt-out-info') }}</p>

    <i18n-t
        tag="p"
        keypath="sw-settings-usage-data.consent-modal.external-links.label"
    >
        <template #data-use-details>
            <mt-link
```

#### Example 4
Source: `sw-settings-usage-data/component/sw-settings-usage-data-store-data-consent/sw-settings-usage-data-store-data-consent.html.twig`
```twig
<sw-settings-usage-data-store-data-consent-card
    :is-loading="isLoading"
    :consent="storeDataConsent"
    @update:consent="updateConsent"
/>

<div>
    <sw-settings-usage-data-consent-check-list />

    <i18n-t
        tag="p"
        keypath="sw-settings-usage-data.consent-modal.external-links.label"
        class="sw-settings-usage-data-store-data-consent__legal-links"
    >
        <template #data-use-details>
```

#### Example 5
Source: `sw-settings-usage-data/component/sw-settings-usage-data-profile-consent/sw-settings-usage-data-profile-consent.html.twig`
```twig
<sw-settings-usage-data-user-data-consent-card
    :is-loading="isLoading"
    :consent="userDataConsent"
    @update:consent="updateConsent"
/>

<div>
    <sw-settings-usage-data-consent-check-list />

    <i18n-t
        class="sw-settings-usage-data-profile-consent__legal-link"
        tag="p"
        keypath="sw-settings-usage-data.consent-modal.external-links.label"
    >
        <template #data-use-details>
```

## sw-shortcut-overview-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| content | `any` | — | yes |  |
| privilege | `any` | `null` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `showItem` | |
| `keys` | |

### Examples

#### Basic Usage
```twig
<sw-shortcut-overview-item
    title="..."
    content="..."
>
    <!-- content -->
</sw-shortcut-overview-item>
```

## sw-shortcut-overview

> Shopware Administration component.

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| shortcut-open | — | |
| shortcut-close | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onOpenShortcutOverviewModal` | |
| `onCloseShortcutOverviewModal` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sections` | |

### Examples

#### Basic Usage
```twig
<sw-shortcut-overview>
    <!-- content -->
</sw-shortcut-overview>
```

## sw-sidebar-collapse

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| expandChevronDirection | `any` | `'right'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header | expanded: expanded | |
| actions | — | |
| content | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change-expanded | — | |

### Methods

| Method | Description |
|--------|-------------|
| `collapseItem` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `expandButtonClass` | |
| `collapseButtonClass` | |

### Examples

#### Example 1
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-sidebar-collapse
    class="sw-category-detail__category-collapse"
    :expand-on-loading="landingPageId === null"
>
    <template #header>

        {% block sw_category_collapse_header %}
        <div
            v-if="categoryCheckedItem > 0"
            class="sw-category-detail__collapse-selected-count"
        >
            {{ $tc(`sw-category.general.treeHeadSelected`, { count: categoryCheckedItem }) }}:
        </div>
        <div
            v-else
```

#### Example 2
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-sidebar-collapse
    class="sw-category-detail__landing-page-collapse"
    :expand-on-loading="landingPageId !== null"
>
    <template #header>

        {% block sw_landing_page_collapse_header %}
        <div
            v-if="landingPageCheckedItem > 0"
            class="sw-category-detail__collapse-selected-count"
        >
            {{ $tc(`sw-landing-page.general.treeHeadSelected`, { count: landingPageCheckedItem }) }}:
        </div>
        <div
            v-else
```

#### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-collapse :expand-on-loading="true">

    {% block sw_cms_sidebar_page_settings_header %}
    <template #header>
        <span>{{ $tc('sw-cms.detail.sidebar.headerPageSettings') }}</span>
    </template>
    {% endblock %}

    {% block sw_cms_sidebar_page_settings_form %}
    <template #content>
        <div class="sw-cms-sidebar__settings">
            {% block sw_cms_sidebar_page_settings_name_field %}

            <mt-text-field
                v-model="page.name"
```

#### Example 4
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-collapse :expand-on-loading="true">

    {% block sw_cms_sidebar_block_settings_header %}
    <template #header>
        <span>
            {{ $tc('sw-cms.sidebar.contentMenu.generalSettings') }}
        </span>
    </template>
    {% endblock %}

    {% block sw_cms_sidebar_block_settings_form %}
    <template #content>
        <sw-cms-block-config
            :block="selectedBlock"
            @block-delete="onBlockDelete"
```

#### Example 5
Source: `sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig`
```twig
<sw-sidebar-collapse
    v-for="cmsElementGroup in groupedCmsElements"
    :key="cmsElementGroup.title"
    expand-on-loading
    expand-chevron-direction="up"
>
    <template #header>
        {{ $tc(cmsElementGroup.title) }}
    </template>

    <template #content>
        <div class="sw-cms-slot__element-selection">
            {% block sw_cms_slot_content_element_modal_selection_element %}
            <template
                v-for="element in cmsElementGroup.items"
```

## sw-sidebar-filter-panel

> Shopware Administration component.

- [Methods](#methods)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| activeFilterNumber | `any` | — | yes |  |

### Methods

| Method | Description |
|--------|-------------|
| `resetAll` | |

### Examples

#### Example 1
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="product_review"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 2
Source: `sw-settings-rule/page/sw-settings-rule-list/sw-settings-rule-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="rule"
                :store-key="storeKey"
                :active-filter-number="activeFilterNumber"
                :filters="listFilters"
                :defaults="defaultFilters"
                @criteria-changed="updateCriteria"
            />
        {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
    {% endblock %}
</sw-page>
    {% endblock %}
```

#### Example 3
Source: `sw-product/page/sw-product-list/sw-product-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="product"
                :store-key="storeKey"
                :active-filter-number="activeFilterNumber"
                :filters="listFilters"
                :defaults="defaultFilters"
                @criteria-changed="updateCriteria"
            />
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 4
Source: `sw-customer/page/sw-customer-list/sw-customer-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="customer"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 5
Source: `sw-order/page/sw-order-list/sw-order-list.html.twig`
```twig
            <sw-sidebar-filter-panel
                entity="order"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
    {% endblock %}
</sw-page>
{% endblock %}
```

## sw-sidebar-item

> Individual item within a sw-sidebar component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| title | `any` | — | yes |  |
| icon | `any` | — | yes |  |
| disabled | `any` | `false` | no |  |
| position | `any` | `'top'` | no |  |
| badge | `any` | `0` | no |  |
| hasSimpleBadge | `any` | `false` | no |  |
| badgeType | `any` | `'info'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |
| headline-content | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| toggle-active | — | |
| close-content | — | |
| click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `registerToggleActiveListener` | |
| `registerCloseContentListener` | |
| `openContent` | |
| `closeContent` | |
| `sidebarButtonClick` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sidebarItemClasses` | |
| `hasDefaultSlot` | |
| `showContent` | |

### Examples

#### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-settings-logging.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 2
Source: `sw-property/page/sw-property-list/sw-property-list.html.twig`
```twig
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-property.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 3
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-item
    ref="pageConfigSidebar"
    icon="regular-cog"
    :title="$tc('sw-cms.detail.sidebar.titlePageSettings')"
    :has-simple-badge="hasPageConfigErrors"
    badge-type="error"
    :disabled="page.locked || disabled"
>

    {% block sw_cms_sidebar_page_settings_content %}
    <sw-sidebar-collapse :expand-on-loading="true">

        {% block sw_cms_sidebar_page_settings_header %}
        <template #header>
            <span>{{ $tc('sw-cms.detail.sidebar.headerPageSettings') }}</span>
```

#### Example 4
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar-item
    ref="blockSelectionSidebar"
    icon="regular-plus-circle"
    :title="addBlockTitle"
    :disabled="currentDeviceView === 'form' || !isSystemDefaultLanguage || page.locked || disabled"
>
    {% block sw_cms_sidebar_block_overview_content %}
    <div class="sw-cms-sidebar__block-overview">

        {% block sw_cms_sidebar_block_overview_category %}
        <div class="sw-cms-sidebar__block-category">
            <mt-select
                v-model="currentBlockCategory"
                :label="$tc('sw-cms.detail.label.blockCategorySelection')"
                :options="cmsBlockCategoriesOptions"
```

#### Example 5
Source: `sw-review/page/sw-review-list/sw-review-list.html.twig`
```twig
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-review.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}

            {% block sw_review_list_sidebar_filter %}
            <sw-sidebar-filter-panel
                entity="product_review"
                :store-key="storeKey"
                :filters="listFilters"
                :defaults="defaultFilters"
                :active-filter-number="activeFilterNumber"
                @criteria-changed="updateCriteria"
```

## sw-sidebar-media-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| initialFolderId | `any` | `null` | no |  |
| isParentLoading | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| context-menu-items | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `onSearchTermChange` | |
| `initializeContent` | |
| `getSubFolders` | |
| `handleFolderGridItemDelete` | |
| `handleMediaGridItemDelete` | |
| `onLoadMore` | |
| `extendList` | |
| `getList` | |
| `getListingCriteria` | |
| `openContent` | |
| `onNavigateToFolder` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `mediaRepository` | |
| `mediaFolderRepository` | |
| `showMore` | |
| `itemsLoaded` | |

### Examples

#### Example 1
Source: `sw-settings-shipping/page/sw-settings-shipping-detail/sw-settings-shipping-detail.html.twig`
```twig
<sw-sidebar-media-item ref="mediaSidebarItem">
    <template
        #context-menu-items="media"
    >
        <sw-context-menu-item @click="setMediaFromSidebar(media.mediaItem)">
            {{ $tc('sw-settings-shipping.sidebar.labelUseAsLogo') }}
        </sw-context-menu-item>
    </template>
</sw-sidebar-media-item>
```

#### Example 2
Source: `sw-settings-payment/page/sw-settings-payment-detail/sw-settings-payment-detail.html.twig`
```twig
<sw-sidebar-media-item ref="mediaSidebarItem">
    <template
        #context-menu-items="media"
    >
        <sw-context-menu-item @click="setMediaFromSidebar(media.mediaItem)">
            {{ $tc('sw-settings-payment.detail.sidebar.labelUseAsLogo') }}
        </sw-context-menu-item>
    </template>
</sw-sidebar-media-item>
```

#### Example 3
Source: `sw-mail-template/page/sw-mail-template-detail/sw-mail-template-detail.html.twig`
```twig
<sw-sidebar-media-item ref="mediaSidebarItem">
    <template
        #context-menu-items="media"
    >
        {% block sw_mail_template_detail_sidebar_add_attachment %}
        <sw-context-menu-item
            :disabled="!acl.can('mail_templates.editor') || undefined"
            @click="onAddItemToAttachment(media.mediaItem)"
        >
            {{ $tc('sw-mail-template.detail.sidebar.labelContextMenuAddToMailTemplate') }}
        </sw-context-menu-item>
        {% endblock %}
    </template>
</sw-sidebar-media-item>
```

## sw-sidebar-navigation-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sidebarItem | `any` | — | yes |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `emitButtonClicked` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `badgeTypeClasses` | |

### Examples

#### Basic Usage
```twig
<sw-sidebar-navigation-item
    sidebarItem="..."
>
    <!-- content -->
</sw-sidebar-navigation-item>
```

## sw-sidebar-renderer

> Shopware Administration component.

### Examples

#### Basic Usage
```twig
<sw-sidebar-renderer>
    <!-- content -->
</sw-sidebar-renderer>
```

## sw-sidebar

> Side panel container for filters, navigation, or auxiliary content.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| propagateWidth | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| item-click | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `mountedComponent` | |
| `destroyedComponent` | |
| `_isItemRegistered` | |
| `_isAnyItemActive` | |
| `closeSidebar` | |
| `registerSidebarItem` | |
| `setItemActive` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sections` | |
| `sidebarClasses` | |

### Examples

#### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
        <sw-sidebar class="sw-settings-logging-list__sidebar">
            {% block sw_settings_logging_list_sidebar_refresh %}
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-settings-logging.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 2
Source: `sw-property/page/sw-property-list/sw-property-list.html.twig`
```twig
        <sw-sidebar>
            {% block sw_property_list_sidebar_refresh_item %}
            <sw-sidebar-item
                icon="regular-undo"
                :title="$tc('sw-property.list.titleSidebarItemRefresh')"
                @click="onRefresh"
            />
            {% endblock %}
        </sw-sidebar>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 3
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-sidebar-collapse
    class="sw-category-detail__category-collapse"
    :expand-on-loading="landingPageId === null"
>
    <template #header>

        {% block sw_category_collapse_header %}
        <div
            v-if="categoryCheckedItem > 0"
            class="sw-category-detail__collapse-selected-count"
        >
            {{ $tc(`sw-category.general.treeHeadSelected`, { count: categoryCheckedItem }) }}:
        </div>
        <div
            v-else
```

#### Example 4
Source: `sw-category/page/sw-category-detail/sw-category-detail.html.twig`
```twig
<sw-sidebar-collapse
    class="sw-category-detail__landing-page-collapse"
    :expand-on-loading="landingPageId !== null"
>
    <template #header>

        {% block sw_landing_page_collapse_header %}
        <div
            v-if="landingPageCheckedItem > 0"
            class="sw-category-detail__collapse-selected-count"
        >
            {{ $tc(`sw-landing-page.general.treeHeadSelected`, { count: landingPageCheckedItem }) }}:
        </div>
        <div
            v-else
```

#### Example 5
Source: `sw-cms/component/sw-cms-sidebar/sw-cms-sidebar.html.twig`
```twig
<sw-sidebar class="sw-cms-sidebar">

    {% block sw_cms_sidebar_page_settings %}
    <sw-sidebar-item
        ref="pageConfigSidebar"
        icon="regular-cog"
        :title="$tc('sw-cms.detail.sidebar.titlePageSettings')"
        :has-simple-badge="hasPageConfigErrors"
        badge-type="error"
        :disabled="page.locked || disabled"
    >

        {% block sw_cms_sidebar_page_settings_content %}
        <sw-sidebar-collapse :expand-on-loading="true">

```

## sw-simple-search-field

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'default'` | no | Valid: `default`, `inverted`, `form` |
| value | `any` | `null` | no |  |
| size | `any` | `'default'` | no |  |
| delay | `any` | `400` | no |  |
| icon | `any` | `'regular-search-s'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| sw-simple-search-field-icon | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |
| search-term-change | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onInput` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `fieldClasses` | |
| `placeholder` | |

### Examples

#### Example 1
Source: `sw-settings-country/component/sw-settings-country-state/sw-settings-country-state.html.twig`
```twig
<sw-simple-search-field
    v-model:value="term"
    size="small"
    variant="form"
    @search-term-change="onSearchCountryState"
/>
{% endblock %}

{% block sw_settings_country_state_list_toolbar_delete %}
<mt-button
    v-tooltip.bottom="{
        message: $tc('sw-privileges.tooltip.warning'),
        disabled: acl.can('country.editor'),
        showOnDisabledElements: true
    }"
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-simple-search-field
    v-model:value="liveSearchTerm"
    class="sw-settings-search-live-search__search_box"
    variant="form"
    :delay="1000"
    :disabled="!isSearchEnable || undefined"
    @search-term-change="searchOnStorefront"
>

    {% block sw_settings_search_view_live_search_search_icon_wrapper %}
    <template #sw-simple-search-field-icon>
        {% block sw_settings_search_view_live_search_search_icon %}
        <mt-icon
            class="sw-settings-search-live-search__search-icon"
            name="regular-search-s"
```

#### Example 3
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
    <sw-simple-search-field
        v-model:value="term"
        size="small"
        variant="form"
        @search-term-change="onSearchCustomFields"
    />
    {% endblock %}

</div>
{% endblock %}

<sw-data-grid
    ref="customFieldGrid"
    :data-source="customFields"
    :columns="customFieldColumns"
```

#### Example 4
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
    <sw-simple-search-field
        v-model:value="term"
        size="small"
        variant="form"
        @search-term-change="onSearchPropertyGroups"
    />
    {% endblock %}

</div>
{% endblock %}

<sw-data-grid
    ref="propertyGroupGrid"
    :data-source="propertyGroups"
    :columns="propertyGroupColumns"
```

#### Example 5
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-values-card/sw-settings-product-feature-sets-values-card.html.twig`
```twig
<sw-simple-search-field
    v-model:value="term"
    size="small"
    variant="form"
    :disabled="!allowEdit || undefined"
    @search-term-change="onSearch"
/>
{% endblock %}

{% block sw_product_feature_set_toolbar_delete %}
<mt-button
    :disabled="deleteButtonDisabled || !allowEdit || undefined"
    square
    size="small"
    class="sw-product-feature-set__delete-button"
```

## sw-single-select

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
| isLoading | `any` | `false` | no |  |
| highlightSearchTerm | `any` | `true` | no |  |
| placeholder | `any` | `''` | no |  |
| labelProperty | `any` | `'label'` | no |  |
| valueProperty | `any` | `'value'` | no |  |
| popoverClasses | `any` | — | no |  |
| searchFunction | `any` | — | no |  |
| disableSearchFunction | `any` | `false` | no |  |
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
| item-selected | — | |
| on-open-change | — | |
| before-selection-clear | — | |
| search | — | |
| paginate | — | |

### Methods

| Method | Description |
|--------|-------------|
| `isSelected` | |
| `onSelectExpanded` | |
| `tryGetSearchText` | |
| `onSelectCollapsed` | |
| `closeResultList` | |
| `setValue` | |
| `resetActiveItem` | |
| `onInputSearchTerm` | |
| `debouncedSearch` | |
| `search` | |
| `getKey` | |
| `clearSelection` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `currentValue` | |
| `inputClasses` | |
| `selectionTextClasses` | |
| `singleSelection` | |
| `visibleResults` | |

### Examples

#### Example 1
Source: `sw-settings-search/component/sw-settings-search-live-search/sw-settings-search-live-search.html.twig`
```twig
<sw-single-select
    class="sw-settings-search-live-search__sales-channel-select"
    value-property="id"
    label-property="translated.name"
    :placeholder="$tc('sw-settings-search.liveSearchTab.textPlaceholderSalesChannel')"
    :label="$tc('sw-settings-search.liveSearchTab.labelSalesChannelSelect')"
    :value="salesChannelId"
    :options="salesChannels"
    show-clearable-button
    @update:value="changeSalesChannel"
/>
{% endblock %}

{% block sw_settings_search_view_live_search_input %}
<sw-container
```

#### Example 2
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
        <sw-single-select
            v-model:value="item.field"
            class="sw-settings-search-field-select"
            size="small"
            show-clearable-button
            :options="fieldConfigs"
            @update:value="onSelectField(item)"
        />
        {% endblock %}
    </template>
    <template v-else>
        {% block sw_settings_search_searchable_content_general_field_label %}
        {{ getMatchingFields(item.field) }}
        {% endblock %}
    </template>
```

#### Example 3
Source: `sw-bulk-edit/component/sw-bulk-edit-change-type/sw-bulk-edit-change-type.html.twig`
```twig
    <sw-single-select
        v-model:value="currentValue"
        class="sw-bulk-edit-change-type__selection"
        :options="options"
        @update:value="onChangeType"
    />
    {% endblock %}

    {% block sw_bulk_edit_change_type_value_field %}
    <slot
        name="value-field"
        v-bind="{ isDisplayingValue }"
    >
    </slot>
    {% endblock %}
```

#### Example 4
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
        <sw-single-select
            class="sw-settings-listing-index__default-sorting-select"
            :placeholder="$tc('sw-settings-listing.general.placeholderDefaultSorting')"
            :disabled="isInherited"
            :value="currentValue"
            :options="productSortingOptions"
            :error="hasDefaultSortingError ? salesChannelDefaultSortingError : null"
            label-property="label"
            value-property="id"
            @update:value="updateCurrentValue"
        />
    </template>
</sw-inherit-wrapper>
{% endblock %}

```

#### Example 5
Source: `sw-settings-listing/component/sw-settings-listing-option-criteria-grid/sw-settings-listing-option-criteria-grid.html.twig`
```twig
    <sw-single-select
        :value="selectedCriteria"
        :options="criteriaOptions"
        :placeholder="$tc('sw-settings-listing.base.criteria.selectPlaceholder')"
        value-property="value"
        label-property="label"
        show-clearable-button
        @update:value="onAddCriteria"
    />
    {% endblock %}
</template>
{% endblock %}

{% block sw_settings_listing_option_criteria_card_grid %}
<sw-data-grid
```

## sw-skeleton-bar-deprecated

> **Deprecated in 6.7** — Use `mt-skeleton-bar` instead. Will be removed in 6.8.
> See mt-skeleton-bar for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-skeleton-bar>` | `<mt-skeleton-bar>` |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig`
```twig
<sw-skeleton-bar style="width: 100%; min-height: 250px;" />
```

## sw-skeleton-bar

> **Migration wrapper** — Delegates to `mt-skeleton-bar` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-skeleton-bar for the new component.

### Computed Properties

| Name | Description |
|------|-------------|
| `useMeteorComponent` | |

### Examples

#### Example 1
Source: `sw-cms/component/sw-cms-slot/sw-cms-slot.html.twig`
```twig
<sw-skeleton-bar style="width: 100%; min-height: 250px;" />
```

## sw-skeleton

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| variant | `any` | `'detail'` | no |  |

### Computed Properties

| Name | Description |
|------|-------------|
| `classList` | |

### Examples

#### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-skeleton />
```

#### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-skeleton />
```

#### Example 3
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-skeleton />
```

#### Example 4
Source: `sw-settings-search/page/sw-settings-search/sw-settings-search.html.twig`
```twig
<sw-skeleton />
```

#### Example 5
Source: `sw-settings-salutation/page/sw-settings-salutation-detail/sw-settings-salutation-detail.html.twig`
```twig
<sw-skeleton v-if="isLoading" />
```

## sw-skip-link

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `setFocus` | |
| `focusElement` | |

### Examples

#### Basic Usage
```twig
<sw-skip-link>
    <!-- content -->
</sw-skip-link>
```

## sw-snippet-field-edit-modal

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| snippets | `any` | — | yes |  |
| snippetSets | `any` | — | yes |  |
| translationKey | `any` | — | yes |  |
| fieldType | `any` | — | yes | Valid: `text`, `textarea` |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| modal-close | — | |
| save | — | |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `closeModal` | |
| `getNoPermissionsTooltip` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modalTitle` | |
| `currentAuthor` | |
| `snippetRepository` | |
| `textField` | |
| `textArea` | |

### Examples

#### Basic Usage
```twig
<sw-snippet-field-edit-modal
    snippets="..."
    snippetSets="..."
    translationKey="..."
>
    <!-- content -->
</sw-snippet-field-edit-modal>
```

## sw-snippet-field

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| snippet | `any` | — | yes |  |
| fieldType | `any` | `'text'` | no | Valid: `text`, `textarea` |

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `updatePlaceholderValueToSnippetTranslation` | |
| `getTranslationByLocale` | |
| `getSystemDefaultLocale` | |
| `openEditModal` | |
| `closeEditModal` | |
| `onSave` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `snippetSetRepository` | |
| `languageRepository` | |
| `languageCriteria` | |
| `textField` | |
| `textareaField` | |

### Examples

#### Basic Usage
```twig
<sw-snippet-field
    snippet="..."
>
    <!-- content -->
</sw-snippet-field>
```

## sw-sortable-list

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| items | `any` | — | yes |  |
| sortable | `any` | — | no |  |
| dragConf | `any` | — | no |  |
| scrollOnDrag | `any` | — | no |  |
| scrollOnDragConf | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| item | — | |

### Methods

| Method | Description |
|--------|-------------|
| `findScrollableParent` | |
| `hasOrderChanged` | |
| `onDragEnter` | |
| `onDragStart` | |
| `onScroll` | |
| `scroll` | |
| `onDrop` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `hasItems` | |
| `isSortable` | |
| `mergedDragConfig` | |
| `mergedScrollOnDragConfig` | |
| `scrollableParent` | |

### Examples

#### Example 1
Source: `sw-settings-tax/component/sw-settings-tax-provider-sorting-modal/sw-settings-tax-provider-sorting-modal.html.twig`
```twig
<sw-sortable-list
    class="sw-settings-tax-provider-sorting-modal__tax-provider-list"
    :items="sortedTaxProviders"
    @items-sorted="onSort"
>
    <template #item="{ item: taxProvider }">
        <div
            class="sw-settings-tax-provider-sorting-modal__tax-provider-list-item"
            :class="!taxProvider.active ? 'is--disabled' : ''"
        >
            <mt-icon
                class="sw-settings-tax-provider-sorting-modal__tax-provider-list-item__action"
                name="regular-grip-vertical"
            />

```

#### Example 2
Source: `sw-settings-payment/component/sw-settings-payment-sorting-modal/sw-settings-payment-sorting-modal.html.twig`
```twig
<sw-sortable-list
    class="sw-settings-payment-sorting-modal__payment-method-list"
    :items="sortedPaymentMethods"
    :scroll-on-drag="true"
    :scroll-on-drag-conf="scrollOnDragConf"
    @items-sorted="onSort"
>
    {% block sw_settings_payment_sorting_modal_content_payment_method %}
    <template #item="{ item: paymentMethod }">
        <div
            class="sw-settings-payment-sorting-modal__payment-method-list-item"
            :class="!paymentMethod.active ? 'is--disabled' : ''"
        >
            {% block sw_settings_payment_sorting_modal_content_payment_method_action %}
            <mt-icon
```

## sw-sorting-select

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| sortBy | `any` | `'createdAt'` | no |  |
| sortDirection | `any` | `'DESC'` | no |  |
| additionalSortOptions | `any` | — | no |  |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| sorting-changed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onSortingChanged` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `sortOptions` | |
| `sortingConditionConcatenation` | |
| `sortingConditionOptions` | |

### Examples

#### Example 1
Source: `sw-cms/page/sw-cms-list/sw-cms-list.html.twig`
```twig
    <sw-sorting-select
        :sort-by="sortBy"
        :sort-direction="sortDirection"
        @sorting-changed="onSort"
    />
    {% endblock %}

</div>
{% endblock %}

{% block sw_cms_list_listing_actions_mode %}
<div
    class="sw-cms-list__actions-mode"
    role="button"
    tabindex="0"
```

#### Example 2
Source: `sw-cms/component/sw-cms-layout-modal/sw-cms-layout-modal.html.twig`
```twig
<sw-sorting-select
    class="sw-cms-layout-modal__header-sorting-select"
    :sort-by="sortBy"
    :sort-direction="sortDirection"
    @sorting-changed="onSort"
/>
{% endblock %}

{% block sw_cms_layout_modal_header_view_toggle %}
<div
    class="sw-cms-layout-modal__actions-mode"
    role="button"
    tabindex="0"
    @click="toggleListMode"
    @keydown.enter="toggleListMode"
```

## sw-sso-error-index

> Shopware Administration component.

### Computed Properties

| Name | Description |
|------|-------------|
| `assetFilter` | |
| `isLoading` | |
| `url` | |
| `email` | |

### Examples

#### Basic Usage
```twig
<sw-sso-error-index>
    <!-- content -->
</sw-sso-error-index>
```

## sw-sso-users-permission-user-detail

> Shopware Administration component.

### Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `loadUser` | |
| `loadCurrentUser` | |
| `loadLanguages` | |
| `onCancel` | |
| `onSave` | |
| `setMediaItem` | |
| `onRemoveMedia` | |
| `onDropMedia` | |
| `onCreateAccessKey` | |
| `generateKey` | |
| `onAccessKeyCreateCancel` | |
| `onSaveAccessKey` | |
| `onEditAccessKey` | |
| `onGenerateNewKey` | |
| `onDeleteAccessKey` | |
| `onCloseAccessKeyDeleteModal` | |
| `onConfirmDeleteAccessKey` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `fullName` | |
| `tooltipCancel` | |
| `tooltipSave` | |
| `integrationColumns` | |
| `aclRoleCriteria` | |
| `isInvited` | |
| `isCurrentUser` | |
| `userRepository` | |
| `languageRepository` | |
| `keyRepository` | |

### Examples

#### Basic Usage
```twig
<sw-sso-users-permission-user-detail>
    <!-- content -->
</sw-sso-users-permission-user-detail>
```

## sw-status

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| color | `any` | `'green'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Computed Properties

| Name | Description |
|------|-------------|
| `statusClass` | |

### Examples

#### Example 1
Source: `sw-sales-channel/page/sw-sales-channel-list/sw-sales-channel-list.html.twig`
```twig
<sw-status color="orange">
    {{ $tc('sw-sales-channel.list.status.maintenance') }}
</sw-status>
```

#### Example 2
Source: `sw-sales-channel/page/sw-sales-channel-list/sw-sales-channel-list.html.twig`
```twig
<sw-status color="green">
    {{ $tc('sw-sales-channel.list.status.online') }}
</sw-status>
```

#### Example 3
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<sw-status
    :color="serviceStatus"
>
    {{ $t(statusText) }}
</sw-status>
```

## sw-step-display

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| itemIndex | `any` | — | yes |  |
| itemVariant | `any` | — | yes |  |
| initialItemVariants | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `addStep` | |
| `setItemVariants` | |
| `setItemVariant` | |
| `setVariantForCurrentItem` | |
| `setItemActive` | |

### Examples

#### Example 1
Source: `sw-first-run-wizard/component/sw-first-run-wizard-modal/sw-first-run-wizard-modal.html.twig`
```twig
<sw-step-display
    :item-index="stepIndex"
    :item-variant="stepVariant"
    :initial-item-variants="stepInitialItemVariants"
>
    <sw-step-item v-if="!extensionManagementDisabled">
        {{ $tc('sw-first-run-wizard.stepItemTitle.dataImport') }}
    </sw-step-item>

    <sw-step-item>
        {{ $tc('sw-first-run-wizard.stepItemTitle.defaults') }}
    </sw-step-item>

    <sw-step-item>
        {{ $tc('sw-first-run-wizard.stepItemTitle.mailer') }}
```

## sw-step-item

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| disabledIcon | `any` | `'regular-circle-xs'` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Methods

| Method | Description |
|--------|-------------|
| `registerStep` | |
| `setActive` | |
| `setVariant` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `modifierClasses` | |
| `icon` | |
| `stepDisplay` | |

### Examples

#### Example 1
Source: `sw-first-run-wizard/component/sw-first-run-wizard-modal/sw-first-run-wizard-modal.html.twig`
```twig
<sw-step-item v-if="!extensionManagementDisabled">
    {{ $tc('sw-first-run-wizard.stepItemTitle.dataImport') }}
</sw-step-item>
```

#### Example 2
Source: `sw-first-run-wizard/component/sw-first-run-wizard-modal/sw-first-run-wizard-modal.html.twig`
```twig
<sw-step-item>
    {{ $tc('sw-first-run-wizard.stepItemTitle.defaults') }}
</sw-step-item>
```

## sw-string-filter

> Shopware Administration component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| filter | `any` | — | yes |  |
| active | `any` | — | yes |  |
| criteriaFilterType | `any` | `'contains'` | no | Valid: `contains`, `equals`, `equalsAny`, `prefix`, `suffix` |

### Methods

| Method | Description |
|--------|-------------|
| `updateFilter` | |
| `resetFilter` | |

### Examples

#### Basic Usage
```twig
<sw-string-filter
    filter="..."
    active="..."
>
    <!-- content -->
</sw-string-filter>
```

## sw-switch-field-deprecated

> **Deprecated in 6.7** — Use `mt-switch` instead. Will be removed in 6.8.
> See mt-switch for the replacement.

### Migration

| Old (sw-*) | New (mt-*) |
|-----------|-----------|
| `<sw-switch-field>` | `<mt-switch>` |

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| noMarginTop | `any` | `false` | no |  |
| size | `any` | `'default'` | no | Valid: `small`, `medium`, `default` |
| ariaLabel | `any` | — | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| label | — | |
| hint | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| inheritance-remove | — | |
| inheritance-restore | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onInheritanceRestore` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `swSwitchFieldClasses` | |

### Examples

#### Basic Usage
```twig
<sw-switch-field-deprecated>
    <!-- content -->
</sw-switch-field-deprecated>
```

## sw-switch-field

> **Migration wrapper** — Delegates to `mt-switch` by default. The deprecated implementation is available via the `deprecated` prop.
> See mt-switch for the new component.

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | — | no |  |
| checked | `any` | — | no |  |
| deprecated | `any` | `false` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| update:value | — | |

### Methods

| Method | Description |
|--------|-------------|
| `onChangeHandler` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `checkedValue` | |

### Examples

#### Basic Usage
```twig
<sw-switch-field>
    <!-- content -->
</sw-switch-field>
```

## sw-system-config

> Shopware Administration component.

- [Slots](#slots)
- [Events / Emits](#events-emits)
- [Methods](#methods)
- [Computed Properties](#computed-properties)
- [Examples](#examples)

### Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| domain | `any` | — | yes |  |
| salesChannelId | `any` | `null` | no |  |
| salesChannelSwitchable | `any` | `false` | no |  |
| inherit | `any` | `true` | no |  |

### Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| title | — | |
| beforeElements | — | |
| card-element | — | |
| card-element-last | — | |
| afterElements | — | |

### Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| loading-changed | — | |
| config-changed | — | |

### Methods

| Method | Description |
|--------|-------------|
| `getFieldError` | |
| `createdComponent` | |
| `readConfig` | |
| `readAll` | |
| `loadCurrentSalesChannelConfig` | |
| `saveAll` | |
| `createErrorNotification` | |
| `onSalesChannelChanged` | |
| `hasMapInheritanceSupport` | |
| `getElementBind` | |
| `getInheritWrapperBind` | |
| `getInheritedValue` | |
| `emitConfig` | |
| `kebabCase` | |
| `isMeteorComponent` | |
| `getMeteorElementBind` | |
| `getMeteorElementEventsHandler` | |

### Computed Properties

| Name | Description |
|------|-------------|
| `isNotDefaultSalesChannel` | |
| `typesWithMapInheritanceSupport` | |

### Examples

#### Example 1
Source: `sw-extension/page/sw-extension-config/sw-extension-config.html.twig`
```twig
        <sw-system-config
            ref="systemConfig"
            :domain="domain"
            sales-channel-switchable
            :sales-channel-id="salesChannelId"
        />
    </template>
</sw-meteor-page>
{% endblock %}

```

#### Example 2
Source: `sw-settings-newsletter/page/sw-settings-newsletter/sw-settings-newsletter.html.twig`
```twig
            <sw-system-config
                ref="systemConfig"
                sales-channel-switchable
                domain="core.newsletter"
                @loading-changed="onLoadingChanged"
            />
            {% endblock %}
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 3
Source: `sw-settings-listing/page/sw-settings-listing/sw-settings-listing.html.twig`
```twig
<sw-system-config
    ref="systemConfig"
    sales-channel-switchable
    domain="core.listing"
    @loading-changed="onLoadingChanged"
>

    <template #afterElements="{ config, index, isNotDefaultSalesChannel, inheritance }">
        {% block sw_settings_listing_content_card_view_system_config_default_sorting_select %}
        <sw-inherit-wrapper
            v-if="config && index === 0"
            v-model:value="config['core.listing.defaultSorting']"
            :label="$tc('sw-settings-listing.general.labelDefaultSorting')"
            :has-parent="isNotDefaultSalesChannel"
            :inherited-value="inheritance['core.listing.defaultSorting']"
```

#### Example 4
Source: `sw-settings-basic-information/page/sw-settings-basic-information/sw-settings-basic-information.html.twig`
```twig
            <sw-system-config
                v-show="!isLoading"
                ref="systemConfig"
                sales-channel-switchable
                domain="core.basicInformation"
                @loading-changed="onLoadingChanged"
            />
        </sw-card-view>
    </template>
    {% endblock %}
</sw-page>
{% endblock %}

```

#### Example 5
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-index/sw-settings-shopware-updates-index.html.twig`
```twig
<sw-system-config
    v-show="!isLoading"
    ref="systemConfig"
    domain="core.update"
    @loading-changed="onLoadingChanged"
>
    <template #card-element-last>
        <div class="sw-settings-shopware-updates-index__check-for-updates-btn">
            <mt-button
                ghost
                :is-loading="isSearchingForUpdates"
                variant="secondary"
                @click="searchForUpdates"
            >
                {{ $t('sw-settings-shopware-updates.general.checkForUpdates') }}
```
