# sw-settings-usage-data

> Shopware Administration component.

## Examples

### Example 1
Source: `sw-profile/view/sw-profile-index-privacy-preferences/sw-profile-index-privacy-preferences.html.twig`
```twig
<sw-settings-usage-data-profile-consent />
```

### Example 2
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<sw-settings-usage-data-consent-check-list />
```

### Example 3
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

### Example 4
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

### Example 5
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
