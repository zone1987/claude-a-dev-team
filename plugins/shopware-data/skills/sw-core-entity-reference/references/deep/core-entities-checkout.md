# Shopware 6 Core Entities — Checkout

> Auto-generated from `src/` — 49 definitions


## Checkout/Cart

### `absolute_price` [E]

**Class:** `AbsolutePriceDefinition`

### `currency_price` [E]

**Class:** `CurrencyPriceDefinition`

### `percentage_price` [E]

**Class:** `PercentagePriceDefinition`

### `quantity_price` [E]

**Class:** `QuantityPriceDefinition`

### `reference_price` [E]

**Class:** `ReferencePriceDefinition`


## Checkout/Customer

### `customer` [E]

**Class:** `CustomerDefinition` | **Entity:** `CustomerEntity` | **Collection:** `CustomerCollection`

**Defaults:** `accountType="CustomerEntity::ACCOUNT_TYPE_PRIVATE"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `groupId` | `customer_group_id` | FkField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |
| `languageId` | `language_id` | FkField | ApiAware |
| `lastPaymentMethodId` | `last_payment_method_id` | FkField | ApiAware |
| `defaultBillingAddressId` | `default_billing_address_id` | FkField | ApiAware |
| `defaultShippingAddressId` | `default_shipping_address_id` | FkField | ApiAware |
| `` | `` | AutoIncrementField |  |
| `customerNumber` | `customer_number` | NumberRangeField | ApiAware |
| `salutationId` | `salutation_id` | FkField | ApiAware |
| `firstName` | `first_name` | StringField | ApiAware |
| `lastName` | `last_name` | StringField | ApiAware |
| `company` | `company` | StringField | ApiAware |
| `password` | `password` | PasswordField |  |
| `email` | `email` | EmailField | ApiAware |
| `title` | `title` | StringField | ApiAware |
| `vatIds` | `vat_ids` | ListField | ApiAware |
| `affiliateCode` | `affiliate_code` | StringField | ApiAware |
| `campaignCode` | `campaign_code` | StringField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `doubleOptInRegistration` | `double_opt_in_registration` | BoolField | ApiAware |
| `doubleOptInEmailSentDate` | `double_opt_in_email_sent_date` | DateTimeField | ApiAware |
| `doubleOptInConfirmDate` | `double_opt_in_confirm_date` | DateTimeField | ApiAware |
| `hash` | `hash` | StringField | ApiAware |
| `guest` | `guest` | BoolField | ApiAware |
| `firstLogin` | `first_login` | DateTimeField | ApiAware |
| `lastLogin` | `last_login` | DateTimeField | ApiAware |
| `newsletterSalesChannelIds` | `newsletter_sales_channel_ids` | JsonField | WriteProtected |
| `birthday` | `birthday` | DateField | ApiAware |
| `lastOrderDate` | `last_order_date` | DateTimeField | ApiAware |
| `orderCount` | `order_count` | IntField | ApiAware |
| `orderTotalAmount` | `order_total_amount` | FloatField | ApiAware |
| `reviewCount` | `review_count` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |
| `legacyPassword` | `legacy_password` | StringField |  |
| `legacyEncoder` | `legacy_encoder` | StringField |  |
| `remoteAddress` | `remote_address` | RemoteAddressField |  |
| `tagIds` | `tag_ids` | ManyToManyIdField | ApiAware |
| `requestedGroupId` | `requested_customer_group_id` | FkField | ApiAware |
| `boundSalesChannelId` | `bound_sales_channel_id` | FkField |  |
| `accountType` | `account_type` | StringField | ApiAware |
| `Context::CRUD_API_SCOPE]` | `[Context::SYSTEM_SCOPE` | CreatedByField | ApiAware |
| `Context::CRUD_API_SCOPE]` | `[Context::SYSTEM_SCOPE` | UpdatedByField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `defaultBillingAddress` | OneToOne | `CustomerAddressDefinition` |
| `defaultBillingAddress` | ManyToOne | `CustomerAddressDefinition` |
| `defaultShippingAddress` | OneToOne | `CustomerAddressDefinition` |
| `defaultShippingAddress` | ManyToOne | `CustomerAddressDefinition` |
| `group` | ManyToOne | `CustomerGroupDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |
| `lastPaymentMethod` | ManyToOne | `PaymentMethodDefinition` |
| `activeBillingAddress` | ManyToOne | `CustomerAddressDefinition` |
| `activeShippingAddress` | ManyToOne | `CustomerAddressDefinition` |
| `salutation` | ManyToOne | `SalutationDefinition` |
| `addresses` | OneToMany | `CustomerAddressDefinition` |
| `orderCustomers` | OneToMany | `OrderCustomerDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `promotions` | ManyToMany | `PromotionDefinition` |
| `productReviews` | OneToMany | `ProductReviewDefinition` |
| `recoveryCustomer` | OneToOne | `CustomerRecoveryDefinition` |
| `requestedGroup` | ManyToOne | `CustomerGroupDefinition` |
| `boundSalesChannel` | ManyToOne | `SalesChannelDefinition` |
| `wishlists` | OneToMany | `CustomerWishlistDefinition` |
| `createdBy` | ManyToOne | `UserDefinition` |
| `updatedBy` | ManyToOne | `UserDefinition` |

### `customer_address` [E]

**Class:** `CustomerAddressDefinition` | **Entity:** `CustomerAddressEntity` | **Collection:** `CustomerAddressCollection` | **Parent:** `CustomerDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `customerId` | `customer_id` | FkField | ApiAware |
| `countryId` | `country_id` | FkField | ApiAware |
| `countryStateId` | `country_state_id` | FkField | ApiAware |
| `salutationId` | `salutation_id` | FkField | ApiAware |
| `firstName` | `first_name` | StringField | ApiAware |
| `lastName` | `last_name` | StringField | ApiAware |
| `zipcode` | `zipcode` | StringField | ApiAware |
| `city` | `city` | StringField | ApiAware |
| `company` | `company` | StringField | ApiAware |
| `street` | `street` | StringField | ApiAware |
| `department` | `department` | StringField | ApiAware |
| `title` | `title` | StringField | ApiAware |
| `phoneNumber` | `phone_number` | StringField | ApiAware |
| `additionalAddressLine1` | `additional_address_line1` | StringField | ApiAware |
| `additionalAddressLine2` | `additional_address_line2` | StringField | ApiAware |
| `hash` | `hash` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `customer` | ManyToOne | `CustomerDefinition` |
| `country` | ManyToOne | `CountryDefinition` |
| `countryState` | ManyToOne | `CountryStateDefinition` |
| `salutation` | ManyToOne | `SalutationDefinition` |
| `defaultBillingAddressCustomer` | OneToOne | `CustomerDefinition` |
| `defaultShippingAddressCustomer` | OneToOne | `CustomerDefinition` |

### `customer_group` [E]

**Class:** `CustomerGroupDefinition` | **Entity:** `CustomerGroupEntity` | **Collection:** `CustomerGroupCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `displayGross` | `display_gross` | BoolField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `registrationActive` | `registration_active` | BoolField | ApiAware |
| `registrationTitle` | `` | TranslatedField | ApiAware |
| `registrationIntroduction` | `` | TranslatedField | ApiAware |
| `registrationOnlyCompanyRegistration` | `` | TranslatedField | ApiAware |
| `registrationSeoMetaDescription` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `customers` | OneToMany | `CustomerDefinition` |
| `salesChannels` | OneToMany | `SalesChannelDefinition` |
| `CustomerGroupTranslationDefinition::class` | OneToMany | `CustomerGroupTranslationDefinition` |
| `registrationSalesChannels` | ManyToMany | `SalesChannelDefinition` |

**Translated fields:** `name`, `customFields`, `registrationTitle`, `registrationIntroduction`, `registrationOnlyCompanyRegistration`, `registrationSeoMetaDescription`

### `customer_group_registration_sales_channels` [M]

**Class:** `CustomerGroupRegistrationSalesChannelDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `customerGroupId` | `customer_group_id` | FkField | PrimaryKey |
| `salesChannelId` | `sales_channel_id` | FkField | PrimaryKey |
| `` | `` | CreatedAtField |  |

| Association | Type | Target |
|-------------|------|--------|
| `customerGroup` | ManyToOne | `CustomerGroupDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `customer_group_translation` [T]

**Class:** `CustomerGroupTranslationDefinition` | **Entity:** `CustomerGroupTranslationEntity` | **Collection:** `CustomerGroupTranslationCollection` | **Parent:** `CustomerGroupDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `registrationTitle` | `registration_title` | StringField | ApiAware |
| `registrationIntroduction` | `registration_introduction` | LongTextField | ApiAware |
| `registrationOnlyCompanyRegistration` | `registration_only_company_registration` | BoolField | ApiAware |
| `registrationSeoMetaDescription` | `registration_seo_meta_description` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `customer_recovery` [E]

**Class:** `CustomerRecoveryDefinition` | **Entity:** `CustomerRecoveryEntity` | **Collection:** `CustomerRecoveryCollection` | **Parent:** `CustomerDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `hash` | `hash` | StringField | Required |
| `customerId` | `customer_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `customer` | OneToOne | `CustomerDefinition` |

### `customer_tag` [M]

**Class:** `CustomerTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `customerId` | `customer_id` | FkField | ApiAware |
| `tagId` | `tag_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `customer` | ManyToOne | `CustomerDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `customer_wishlist` [E]

**Class:** `CustomerWishlistDefinition` | **Entity:** `CustomerWishlistEntity` | **Collection:** `CustomerWishlistCollection` | **Parent:** `CustomerDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `customerId` | `customer_id` | FkField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | Required |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `products` | OneToMany | `CustomerWishlistProductDefinition` |
| `customer` | ManyToOne | `CustomerDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `customer_wishlist_product` [E]

**Class:** `CustomerWishlistProductDefinition` | **Entity:** `CustomerWishlistProductEntity` | **Collection:** `CustomerWishlistProductCollection` | **Parent:** `CustomerWishlistDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `productId` | `product_id` | FkField | ApiAware |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | ApiAware |
| `wishlistId` | `customer_wishlist_id` | FkField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `wishlist` | ManyToOne | `CustomerWishlistDefinition` |
| `product` | ManyToOne | `ProductDefinition` |

### `sales_channel_customer_address` [E]

**Class:** `SalesChannelCustomerAddressDefinition` | **Entity:** `SalesChannelCustomerAddressEntity` | **Collection:** `SalesChannelCustomerAddressCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `isDefaultBillingAddress` | `is_default_billing_address` | BoolField | Runtime |
| `isDefaultShippingAddress` | `is_default_shipping_address` | BoolField | Runtime |


## Checkout/Order

### `order` [E]

**Class:** `OrderDefinition` | **Entity:** `OrderEntity` | **Collection:** `OrderCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `` | `` | AutoIncrementField |  |
| `orderNumber` | `order_number` | NumberRangeField | ApiAware |
| `billingAddressId` | `billing_address_id` | FkField | ApiAware |
| `billing_address_version_id` | `OrderAddressDefinition::class` | ReferenceVersionField | ApiAware |
| `primaryOrderDeliveryId` | `primary_order_delivery_id` | FkField | ApiAware |
| `primary_order_delivery_version_id` | `OrderDeliveryDefinition::class` | ReferenceVersionField | ApiAware |
| `primaryOrderTransactionId` | `primary_order_transaction_id` | FkField | ApiAware |
| `primary_order_transaction_version_id` | `OrderTransactionDefinition::class` | ReferenceVersionField | ApiAware |
| `currencyId` | `currency_id` | FkField | ApiAware |
| `languageId` | `language_id` | FkField | ApiAware |
| `salesChannelId` | `sales_channel_id` | FkField | ApiAware |
| `orderDateTime` | `order_date_time` | DateTimeField | ApiAware |
| `orderDate` | `order_date` | DateField | ApiAware |
| `price` | `price` | CartPriceField | ApiAware |
| `amountTotal` | `amount_total` | FloatField | ApiAware |
| `amountNet` | `amount_net` | FloatField | ApiAware |
| `positionPrice` | `position_price` | FloatField | ApiAware |
| `taxStatus` | `tax_status` | StringField | ApiAware |
| `shippingCosts` | `shipping_costs` | CalculatedPriceField | ApiAware |
| `shippingTotal` | `shipping_total` | FloatField | ApiAware |
| `currencyFactor` | `currency_factor` | FloatField | ApiAware |
| `deepLinkCode` | `deep_link_code` | StringField | ApiAware |
| `affiliateCode` | `affiliate_code` | StringField | ApiAware |
| `campaignCode` | `campaign_code` | StringField | ApiAware |
| `customerComment` | `customer_comment` | LongTextField | ApiAware |
| `internalComment` | `internal_comment` | LongTextField | AllowEmptyString |
| `source` | `source` | StringField | ApiAware |
| `taxCalculationType` | `tax_calculation_type` | StringField | ApiAware |
| `stateId` | `state_id` | StateMachineStateField | Required |
| `ruleIds` | `rule_ids` | ListField |  |
| `` | `` | CustomFields | ApiAware |
| `Context::CRUD_API_SCOPE]` | `[Context::SYSTEM_SCOPE` | CreatedByField | ApiAware |
| `Context::CRUD_API_SCOPE]` | `[Context::SYSTEM_SCOPE` | UpdatedByField | ApiAware |
| `itemRounding` | `item_rounding` | CashRoundingConfigField | Required |
| `totalRounding` | `total_rounding` | CashRoundingConfigField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `primaryOrderDelivery` | OneToOne | `OrderDeliveryDefinition` |
| `primaryOrderTransaction` | OneToOne | `OrderTransactionDefinition` |
| `orderCustomer` | OneToOne | `OrderCustomerDefinition` |
| `currency` | ManyToOne | `CurrencyDefinition` |
| `language` | ManyToOne | `LanguageDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |
| `addresses` | OneToMany | `OrderAddressDefinition` |
| `billingAddress` | ManyToOne | `OrderAddressDefinition` |
| `deliveries` | OneToMany | `OrderDeliveryDefinition` |
| `lineItems` | OneToMany | `OrderLineItemDefinition` |
| `transactions` | OneToMany | `OrderTransactionDefinition` |
| `documents` | OneToMany | `DocumentDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `createdBy` | ManyToOne | `UserDefinition` |
| `updatedBy` | ManyToOne | `UserDefinition` |

### `order_address` [E]

**Class:** `OrderAddressDefinition` | **Entity:** `OrderAddressEntity` | **Collection:** `OrderAddressCollection` | **Parent:** `OrderDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `countryId` | `country_id` | FkField | ApiAware |
| `countryStateId` | `country_state_id` | FkField | ApiAware |
| `orderId` | `order_id` | FkField | Required |
| `order_version_id` | `OrderDefinition::class` | ReferenceVersionField | Required |
| `salutationId` | `salutation_id` | FkField |  |
| `firstName` | `first_name` | StringField | ApiAware |
| `lastName` | `last_name` | StringField | ApiAware |
| `street` | `street` | StringField | ApiAware |
| `zipcode` | `zipcode` | StringField | ApiAware |
| `city` | `city` | StringField | ApiAware |
| `company` | `company` | StringField | ApiAware |
| `department` | `department` | StringField | ApiAware |
| `title` | `title` | StringField | ApiAware |
| `phoneNumber` | `phone_number` | StringField | ApiAware |
| `additionalAddressLine1` | `additional_address_line1` | StringField | ApiAware |
| `additionalAddressLine2` | `additional_address_line2` | StringField | ApiAware |
| `hash` | `hash` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |
| `vatId` | `vat_id` | StringField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `country` | ManyToOne | `CountryDefinition` |
| `countryState` | ManyToOne | `CountryStateDefinition` |
| `order` | ManyToOne | `OrderDefinition` |
| `orderDeliveries` | OneToMany | `OrderDeliveryDefinition` |
| `salutation` | ManyToOne | `SalutationDefinition` |

### `order_customer` [E]

**Class:** `OrderCustomerDefinition` | **Entity:** `OrderCustomerEntity` | **Collection:** `OrderCustomerCollection` | **Parent:** `OrderDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `customerId` | `customer_id` | FkField |  |
| `orderId` | `order_id` | FkField | Required |
| `OrderDefinition::class` | `OrderDefinition::class` | ReferenceVersionField | Required |
| `email` | `email` | StringField | ApiAware |
| `salutationId` | `salutation_id` | FkField | ApiAware |
| `firstName` | `first_name` | StringField | ApiAware |
| `lastName` | `last_name` | StringField | ApiAware |
| `company` | `company` | StringField | ApiAware |
| `title` | `title` | StringField | ApiAware |
| `vatIds` | `vat_ids` | ListField | ApiAware |
| `customerNumber` | `customer_number` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |
| `remoteAddress` | `remote_address` | RemoteAddressField |  |

| Association | Type | Target |
|-------------|------|--------|
| `order` | OneToOne | `OrderDefinition` |
| `customer` | ManyToOne | `CustomerDefinition` |
| `salutation` | ManyToOne | `SalutationDefinition` |

### `order_delivery` [E]

**Class:** `OrderDeliveryDefinition` | **Entity:** `OrderDeliveryEntity` | **Collection:** `OrderDeliveryCollection` | **Parent:** `OrderDefinition`

**Defaults:** `trackingCodes="["`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `orderId` | `order_id` | FkField | ApiAware |
| `OrderDefinition::class` | `OrderDefinition::class` | ReferenceVersionField | ApiAware |
| `shippingOrderAddressId` | `shipping_order_address_id` | FkField | ApiAware |
| `shipping_order_address_version_id` | `OrderAddressDefinition::class` | ReferenceVersionField | ApiAware |
| `shippingMethodId` | `shipping_method_id` | FkField | ApiAware |
| `stateId` | `state_id` | StateMachineStateField | ApiAware |
| `trackingCodes` | `tracking_codes` | ListField | ApiAware |
| `shippingDateEarliest` | `shipping_date_earliest` | DateTimeField | ApiAware |
| `shippingDateLatest` | `shipping_date_latest` | DateTimeField | ApiAware |
| `shippingCosts` | `shipping_costs` | CalculatedPriceField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `order` | ManyToOne | `OrderDefinition` |
| `shippingOrderAddress` | ManyToOne | `OrderAddressDefinition` |
| `shippingMethod` | ManyToOne | `ShippingMethodDefinition` |
| `positions` | OneToMany | `OrderDeliveryPositionDefinition` |
| `primaryOrder` | OneToOne | `OrderDefinition` |

### `order_delivery_position` [E]

**Class:** `OrderDeliveryPositionDefinition` | **Entity:** `OrderDeliveryPositionEntity` | **Collection:** `OrderDeliveryPositionCollection` | **Parent:** `OrderDeliveryDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `orderDeliveryId` | `order_delivery_id` | FkField | ApiAware |
| `OrderDeliveryDefinition::class` | `OrderDeliveryDefinition::class` | ReferenceVersionField | ApiAware |
| `orderLineItemId` | `order_line_item_id` | FkField | ApiAware |
| `OrderLineItemDefinition::class` | `OrderLineItemDefinition::class` | ReferenceVersionField | ApiAware |
| `price` | `price` | CalculatedPriceField | ApiAware |
| `unitPrice` | `unit_price` | FloatField | ApiAware |
| `totalPrice` | `total_price` | FloatField | ApiAware |
| `quantity` | `quantity` | IntField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `orderDelivery` | ManyToOne | `OrderDeliveryDefinition` |
| `orderLineItem` | ManyToOne | `OrderLineItemDefinition` |

### `order_line_item` [E]

**Class:** `OrderLineItemDefinition` | **Entity:** `OrderLineItemEntity` | **Collection:** `OrderLineItemCollection` | **Parent:** `OrderDefinition`

**Defaults:** `position=1`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `orderId` | `order_id` | FkField | ApiAware |
| `OrderDefinition::class` | `OrderDefinition::class` | ReferenceVersionField | ApiAware |
| `productId` | `product_id` | FkField | ApiAware |
| `ProductDefinition::class` | `ProductDefinition::class` | ReferenceVersionField | ApiAware |
| `promotionId` | `promotion_id` | FkField | ApiAware |
| `self::class` | `self::class` | ParentFkField | ApiAware |
| `parent_version_id` | `self::class` | ReferenceVersionField | ApiAware |
| `coverId` | `cover_id` | FkField | ApiAware |
| `identifier` | `identifier` | StringField | ApiAware |
| `referencedId` | `referenced_id` | StringField | ApiAware |
| `quantity` | `quantity` | IntField | ApiAware |
| `label` | `label` | StringField | ApiAware |
| `payload` | `payload` | JsonField | ApiAware |
| `good` | `good` | BoolField | ApiAware |
| `removable` | `removable` | BoolField | ApiAware |
| `stackable` | `stackable` | BoolField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `price` | `price` | CalculatedPriceField | Required |
| `priceDefinition` | `price_definition` | PriceDefinitionField | ApiAware |
| `unitPrice` | `unit_price` | FloatField | ApiAware |
| `totalPrice` | `total_price` | FloatField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `type` | `type` | StringField | ApiAware |
| `` | `` | CustomFields | ApiAware |
| `states` | `states` | ListField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `cover` | ManyToOne | `MediaDefinition` |
| `order` | ManyToOne | `OrderDefinition` |
| `product` | ManyToOne | `ProductDefinition` |
| `promotion` | ManyToOne | `PromotionDefinition` |
| `orderDeliveryPositions` | OneToMany | `OrderDeliveryPositionDefinition` |
| `orderTransactionCaptureRefundPositions` | OneToMany | `OrderTransactionCaptureRefundPositionDefinition` |
| `downloads` | OneToMany | `OrderLineItemDownloadDefinition` |
| `self::class` | ManyToOne | `` |
| `self::class` | OneToMany | `` |

### `order_line_item_download` [E]

**Class:** `OrderLineItemDownloadDefinition` | **Entity:** `OrderLineItemDownloadEntity` | **Collection:** `OrderLineItemDownloadCollection` | **Parent:** `OrderLineItemDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `orderLineItemId` | `order_line_item_id` | FkField | ApiAware |
| `OrderLineItemDefinition::class` | `OrderLineItemDefinition::class` | ReferenceVersionField | ApiAware |
| `mediaId` | `media_id` | FkField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `accessGranted` | `access_granted` | BoolField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `orderLineItem` | ManyToOne | `OrderLineItemDefinition` |
| `media` | ManyToOne | `MediaDefinition` |

### `order_tag` [M]

**Class:** `OrderTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `orderId` | `order_id` | FkField | ApiAware |
| `OrderDefinition::class` | `OrderDefinition::class` | ReferenceVersionField | ApiAware |
| `tagId` | `tag_id` | FkField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `order` | ManyToOne | `OrderDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `order_transaction` [E]

**Class:** `OrderTransactionDefinition` | **Entity:** `OrderTransactionEntity` | **Collection:** `OrderTransactionCollection` | **Parent:** `OrderDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `orderId` | `order_id` | FkField | ApiAware |
| `OrderDefinition::class` | `OrderDefinition::class` | ReferenceVersionField | ApiAware |
| `paymentMethodId` | `payment_method_id` | FkField | ApiAware |
| `amount` | `amount` | CalculatedPriceField | ApiAware |
| `validationData` | `validation_data` | JsonField | ApiAware |
| `stateId` | `state_id` | StateMachineStateField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `order` | ManyToOne | `OrderDefinition` |
| `paymentMethod` | ManyToOne | `PaymentMethodDefinition` |
| `captures` | OneToMany | `OrderTransactionCaptureDefinition` |
| `primaryOrder` | OneToOne | `OrderDefinition` |

### `order_transaction_capture` [E]

**Class:** `OrderTransactionCaptureDefinition` | **Entity:** `OrderTransactionCaptureEntity` | **Collection:** `OrderTransactionCaptureCollection` | **Parent:** `OrderTransactionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `orderTransactionId` | `order_transaction_id` | FkField | ApiAware |
| `OrderTransactionDefinition::class` | `OrderTransactionDefinition::class` | ReferenceVersionField | ApiAware |
| `stateId` | `state_id` | StateMachineStateField | ApiAware |
| `externalReference` | `external_reference` | StringField | ApiAware |
| `amount` | `amount` | CalculatedPriceField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `transaction` | ManyToOne | `OrderTransactionDefinition` |
| `refunds` | OneToMany | `OrderTransactionCaptureRefundDefinition` |

### `order_transaction_capture_refund` [E]

**Class:** `OrderTransactionCaptureRefundDefinition` | **Entity:** `OrderTransactionCaptureRefundEntity` | **Collection:** `OrderTransactionCaptureRefundCollection` | **Parent:** `OrderTransactionCaptureDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `captureId` | `capture_id` | FkField | ApiAware |
| `capture_version_id` | `OrderTransactionCaptureDefinition::class` | ReferenceVersionField | ApiAware |
| `stateId` | `state_id` | StateMachineStateField | ApiAware |
| `externalReference` | `external_reference` | StringField | ApiAware |
| `reason` | `reason` | StringField | ApiAware |
| `amount` | `amount` | CalculatedPriceField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `stateMachineState` | ManyToOne | `StateMachineStateDefinition` |
| `transactionCapture` | ManyToOne | `OrderTransactionCaptureDefinition` |
| `positions` | OneToMany | `OrderTransactionCaptureRefundPositionDefinition` |

### `order_transaction_capture_refund_position` [E]

**Class:** `OrderTransactionCaptureRefundPositionDefinition` | **Entity:** `OrderTransactionCaptureRefundPositionEntity` | **Collection:** `OrderTransactionCaptureRefundPositionCollection` | **Parent:** `OrderTransactionCaptureRefundDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `` | `` | VersionField | ApiAware |
| `refundId` | `refund_id` | FkField | ApiAware |
| `refund_version_id` | `OrderTransactionCaptureRefundDefinition::class` | ReferenceVersionField | ApiAware |
| `orderLineItemId` | `order_line_item_id` | FkField | ApiAware |
| `OrderLineItemDefinition::class` | `OrderLineItemDefinition::class` | ReferenceVersionField | ApiAware |
| `externalReference` | `external_reference` | StringField | ApiAware |
| `reason` | `reason` | StringField | ApiAware |
| `quantity` | `quantity` | IntField | ApiAware |
| `amount` | `amount` | CalculatedPriceField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `orderLineItem` | ManyToOne | `OrderLineItemDefinition` |
| `orderTransactionCaptureRefund` | ManyToOne | `OrderTransactionCaptureRefundDefinition` |


## Checkout/Payment

### `payment_method` [E]

**Class:** `PaymentMethodDefinition` | **Entity:** `PaymentMethodEntity` | **Collection:** `PaymentMethodCollection`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `pluginId` | `plugin_id` | FkField |  |
| `handlerIdentifier` | `handler_identifier` | StringField |  |
| `name` | `` | TranslatedField | ApiAware |
| `distinguishableName` | `` | TranslatedField | ApiAware |
| `description` | `` | TranslatedField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `afterOrderEnabled` | `after_order_enabled` | BoolField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `availabilityRuleId` | `availability_rule_id` | FkField |  |
| `mediaId` | `media_id` | FkField | ApiAware |
| `formattedHandlerIdentifier` | `formatted_handler_identifier` | StringField | WriteProtected |
| `technicalName` | `technical_name` | StringField | ApiAware |
| `shortName` | `short_name` | StringField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `PaymentMethodTranslationDefinition::class` | OneToMany | `PaymentMethodTranslationDefinition` |
| `media` | ManyToOne | `MediaDefinition` |
| `availabilityRule` | ManyToOne | `RuleDefinition` |
| `salesChannelDefaultAssignments` | OneToMany | `SalesChannelDefinition` |
| `plugin` | ManyToOne | `PluginDefinition` |
| `customers` | OneToMany | `CustomerDefinition` |
| `orderTransactions` | OneToMany | `OrderTransactionDefinition` |
| `salesChannels` | ManyToMany | `SalesChannelDefinition` |
| `appPaymentMethod` | OneToOne | `AppPaymentMethodDefinition` |

**Translated fields:** `name`, `distinguishableName`, `description`, `customFields`

### `payment_method_translation` [T]

**Class:** `PaymentMethodTranslationDefinition` | **Entity:** `PaymentMethodTranslationEntity` | **Collection:** `PaymentMethodTranslationCollection` | **Parent:** `PaymentMethodDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `distinguishableName` | `distinguishable_name` | StringField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |

### `sales_channel_payment_method` [E]

**Class:** `SalesChannelPaymentMethodDefinition`


## Checkout/Promotion

### `cart_promotions_data` [E]

**Class:** `CartPromotionsDataDefinition`

### `promotion` [E]

**Class:** `PromotionDefinition` | **Entity:** `PromotionEntity` | **Collection:** `PromotionCollection`

**Defaults:** `active=false`, `exclusive=false`, `useCodes=false`, `useIndividualCodes=false`, `individualCodePattern=""`, `useSetGroups=false`, `maxRedemptionsGlobal=null`, `maxRedemptionsPerCustomer=null`, `preventCombination=false`, `priority=1`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `name` | `` | TranslatedField |  |
| `active` | `active` | BoolField | Required |
| `validFrom` | `valid_from` | DateTimeField |  |
| `validUntil` | `valid_until` | DateTimeField |  |
| `maxRedemptionsGlobal` | `max_redemptions_global` | IntField |  |
| `maxRedemptionsPerCustomer` | `max_redemptions_per_customer` | IntField |  |
| `priority` | `priority` | IntField | Required |
| `exclusive` | `exclusive` | BoolField | Required |
| `code` | `code` | StringField |  |
| `useCodes` | `use_codes` | BoolField | Required |
| `useIndividualCodes` | `use_individual_codes` | BoolField | Required |
| `individualCodePattern` | `individual_code_pattern` | StringField |  |
| `useSetGroups` | `use_setgroups` | BoolField | Required |
| `customerRestriction` | `customer_restriction` | BoolField |  |
| `preventCombination` | `prevent_combination` | BoolField | Required |
| `orderCount` | `order_count` | IntField | WriteProtected |
| `ordersPerCustomerCount` | `orders_per_customer_count` | JsonField | WriteProtected |
| `exclusionIds` | `exclusion_ids` | ListField |  |
| `customFields` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `setgroups` | OneToMany | `PromotionSetGroupDefinition` |
| `salesChannels` | OneToMany | `PromotionSalesChannelDefinition` |
| `discounts` | OneToMany | `PromotionDiscountDefinition` |
| `individualCodes` | OneToMany | `PromotionIndividualCodeDefinition` |
| `personaRules` | ManyToMany | `RuleDefinition` |
| `personaCustomers` | ManyToMany | `CustomerDefinition` |
| `orderRules` | ManyToMany | `RuleDefinition` |
| `cartRules` | ManyToMany | `RuleDefinition` |
| `orderLineItems` | OneToMany | `OrderLineItemDefinition` |
| `PromotionTranslationDefinition::class` | OneToMany | `PromotionTranslationDefinition` |

**Translated fields:** `name`, `customFields`

### `promotion_cart_rule` [M]

**Class:** `PromotionCartRuleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `promotionId` | `promotion_id` | FkField | PrimaryKey |
| `ruleId` | `rule_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |

### `promotion_discount` [E]

**Class:** `PromotionDiscountDefinition` | **Entity:** `PromotionDiscountEntity` | **Collection:** `PromotionDiscountCollection` | **Parent:** `PromotionDefinition`

**Defaults:** `considerAdvancedRules=false`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `promotionId` | `promotion_id` | FkField | Required |
| `scope` | `scope` | StringField | Required |
| `type` | `type` | StringField | Required |
| `value` | `value` | FloatField | Required |
| `considerAdvancedRules` | `consider_advanced_rules` | BoolField | Required |
| `maxValue` | `max_value` | FloatField |  |
| `sorterKey` | `sorter_key` | StringField |  |
| `applierKey` | `applier_key` | StringField |  |
| `usageKey` | `usage_key` | StringField |  |
| `pickerKey` | `picker_key` | StringField |  |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |
| `discountRules` | ManyToMany | `RuleDefinition` |
| `promotionDiscountPrices` | OneToMany | `PromotionDiscountPriceDefinition` |

### `promotion_discount_prices` [E]

**Class:** `PromotionDiscountPriceDefinition` | **Entity:** `PromotionDiscountPriceEntity` | **Collection:** `PromotionDiscountPriceCollection` | **Parent:** `PromotionDiscountDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `discountId` | `discount_id` | FkField | Required |
| `currencyId` | `currency_id` | FkField | Required |
| `price` | `price` | FloatField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `promotionDiscount` | ManyToOne | `PromotionDiscountDefinition` |
| `currency` | ManyToOne | `CurrencyDefinition` |

### `promotion_discount_rule` [M]

**Class:** `PromotionDiscountRuleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `discountId` | `discount_id` | FkField | PrimaryKey |
| `ruleId` | `rule_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `discount` | ManyToOne | `PromotionDiscountDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |

### `promotion_individual_code` [E]

**Class:** `PromotionIndividualCodeDefinition` | **Entity:** `PromotionIndividualCodeEntity` | **Collection:** `PromotionIndividualCodeCollection` | **Parent:** `PromotionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `promotionId` | `promotion_id` | FkField | Required |
| `code` | `code` | StringField | Required |
| `payload` | `payload` | JsonField |  |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |

### `promotion_order_rule` [M]

**Class:** `PromotionOrderRuleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `promotionId` | `promotion_id` | FkField | PrimaryKey |
| `ruleId` | `rule_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |

### `promotion_persona_customer` [M]

**Class:** `PromotionPersonaCustomerDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `promotionId` | `promotion_id` | FkField | PrimaryKey |
| `customerId` | `customer_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |
| `customer` | ManyToOne | `CustomerDefinition` |

### `promotion_persona_rule` [M]

**Class:** `PromotionPersonaRuleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `promotionId` | `promotion_id` | FkField | PrimaryKey |
| `ruleId` | `rule_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |

### `promotion_sales_channel` [E]

**Class:** `PromotionSalesChannelDefinition` | **Entity:** `PromotionSalesChannelEntity` | **Collection:** `PromotionSalesChannelCollection` | **Parent:** `PromotionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `promotionId` | `promotion_id` | FkField | Required |
| `salesChannelId` | `sales_channel_id` | FkField | Required |
| `priority` | `priority` | IntField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |
| `salesChannel` | ManyToOne | `SalesChannelDefinition` |

### `promotion_setgroup` [E]

**Class:** `PromotionSetGroupDefinition` | **Entity:** `PromotionSetGroupEntity` | **Collection:** `PromotionSetGroupCollection` | **Parent:** `PromotionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | PrimaryKey |
| `promotionId` | `promotion_id` | FkField | Required |
| `packagerKey` | `packager_key` | StringField | Required |
| `sorterKey` | `sorter_key` | StringField | Required |
| `value` | `value` | FloatField | Required |

| Association | Type | Target |
|-------------|------|--------|
| `promotion` | ManyToOne | `PromotionDefinition` |
| `setGroupRules` | ManyToMany | `RuleDefinition` |

### `promotion_setgroup_rule` [M]

**Class:** `PromotionSetGroupRuleDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `setgroupId` | `setgroup_id` | FkField | PrimaryKey |
| `ruleId` | `rule_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `setgroup` | ManyToOne | `PromotionSetGroupDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |

### `promotion_translation` [T]

**Class:** `PromotionTranslationDefinition` | **Entity:** `PromotionTranslationEntity` | **Collection:** `PromotionTranslationCollection` | **Parent:** `PromotionDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | Required |
| `` | `` | CustomFields | ApiAware |


## Checkout/Shipping

### `sales_channel_shipping_method` [E]

**Class:** `SalesChannelShippingMethodDefinition`

### `shipping_method` [E]

**Class:** `ShippingMethodDefinition` | **Entity:** `ShippingMethodEntity` | **Collection:** `ShippingMethodCollection`

**Defaults:** `taxType="ShippingMethodEntity::TAX_TYPE_AUTO"`, `position="ShippingMethodEntity::POSITION_DEFAULT"`, `active="ShippingMethodEntity::ACTIVE_DEFAULT"`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `name` | `` | TranslatedField | ApiAware |
| `technicalName` | `technical_name` | StringField | ApiAware |
| `active` | `active` | BoolField | ApiAware |
| `position` | `position` | IntField | ApiAware |
| `customFields` | `` | TranslatedField | ApiAware |
| `availabilityRuleId` | `availability_rule_id` | FkField |  |
| `mediaId` | `media_id` | FkField | ApiAware |
| `deliveryTimeId` | `delivery_time_id` | FkField | ApiAware |
| `taxType` | `tax_type` | StringField | ApiAware |
| `taxId` | `tax_id` | FkField |  |
| `description` | `` | TranslatedField | ApiAware |
| `trackingUrl` | `` | TranslatedField | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `deliveryTime` | ManyToOne | `DeliveryTimeDefinition` |
| `ShippingMethodTranslationDefinition::class` | OneToMany | `ShippingMethodTranslationDefinition` |
| `availabilityRule` | ManyToOne | `RuleDefinition` |
| `prices` | OneToMany | `ShippingMethodPriceDefinition` |
| `media` | ManyToOne | `MediaDefinition` |
| `tags` | ManyToMany | `TagDefinition` |
| `orderDeliveries` | OneToMany | `OrderDeliveryDefinition` |
| `salesChannels` | ManyToMany | `SalesChannelDefinition` |
| `salesChannelDefaultAssignments` | OneToMany | `SalesChannelDefinition` |
| `tax` | ManyToOne | `TaxDefinition` |
| `appShippingMethod` | OneToOne | `AppShippingMethodDefinition` |

**Translated fields:** `name`, `customFields`, `description`, `trackingUrl`

### `shipping_method_price` [E]

**Class:** `ShippingMethodPriceDefinition` | **Entity:** `ShippingMethodPriceEntity` | **Collection:** `ShippingMethodPriceCollection` | **Parent:** `ShippingMethodDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `id` | `id` | IdField | ApiAware |
| `shippingMethodId` | `shipping_method_id` | FkField | ApiAware |
| `ruleId` | `rule_id` | FkField | ApiAware |
| `calculation` | `calculation` | IntField | ApiAware |
| `calculationRuleId` | `calculation_rule_id` | FkField | ApiAware |
| `quantityStart` | `quantity_start` | FloatField | ApiAware |
| `quantityEnd` | `quantity_end` | FloatField | ApiAware |
| `currencyPrice` | `currency_price` | PriceField | ApiAware |
| `` | `` | CustomFields | ApiAware |

| Association | Type | Target |
|-------------|------|--------|
| `shippingMethod` | ManyToOne | `ShippingMethodDefinition` |
| `rule` | ManyToOne | `RuleDefinition` |
| `calculationRule` | ManyToOne | `RuleDefinition` |

### `shipping_method_tag` [M]

**Class:** `ShippingMethodTagDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `shippingMethodId` | `shipping_method_id` | FkField | PrimaryKey |
| `tagId` | `tag_id` | FkField | PrimaryKey |

| Association | Type | Target |
|-------------|------|--------|
| `shippingMethod` | ManyToOne | `ShippingMethodDefinition` |
| `tag` | ManyToOne | `TagDefinition` |

### `shipping_method_translation` [T]

**Class:** `ShippingMethodTranslationDefinition` | **Entity:** `ShippingMethodTranslationEntity` | **Collection:** `ShippingMethodTranslationCollection` | **Parent:** `ShippingMethodDefinition`

| Field | Storage | Type | Flags |
|-------|---------|------|-------|
| `name` | `name` | StringField | ApiAware |
| `description` | `description` | LongTextField | ApiAware |
| `trackingUrl` | `tracking_url` | LongTextField | ApiAware |
| `` | `` | CustomFields | ApiAware |
