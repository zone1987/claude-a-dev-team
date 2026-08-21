# mt-modal

> Modal dialog with title, content area, actions, and close functionality.

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| header-left | — | |
| title-after | — | |
| header-right | — | |
| default | — | |
| footer | — | |

## Examples

### Example 1
Source: `sw-media/component/sw-media-modal-v2/sw-media-modal-v2.html.twig`
```twig
<mt-modal-root
    :is-open="isOpen"
    @change="onModalRootChange"
>
    <mt-modal
        ref="swMediaModal"
        class="sw-media-modal-v2"
        width="full"
        :title="$tc('sw-media.sw-media-modal-v2.titleModal')"
    >

        {% block sw_media_modal_v2_content %}
        <div class="sw-media-modal-v2__content">

            {% block sw_media_modal_v2_tabs %}
```

### Example 2
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
<mt-modal-root
    :is-open="showConsentModal"
    :closable="false"
>
    <mt-modal
        width="s"
        :title="$t('sw-settings-usage-data.consent-modal.title')"
        :closable="false"
        hide-header
    >
        <template #default>
            <div class="sw-settings-usage-data-consent-modal__content">
                <img
                    class="sw-setting-usage-data-consent-modal__icon-union"
                    :src="unionPath"
```

### Example 3
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/sw-settings-usage-data-consent-modal.html.twig`
```twig
    <mt-modal-action
        as="mt-button"
        variant="primary"
        @click="savePreferences"
    >
        {{ $t('sw-settings-usage-data.consent-modal.actions.save-preferences') }}
    </mt-modal-action>
</template>
<template v-else>
    <mt-modal-action
        as="mt-button"
        variant="primary"
        @click="shareNothing"
    >
        <template #iconFront="{ size }">
```

### Example 4
Source: `sw-settings-services/component/sw-settings-services-revoke-permissions-modal/sw-settings-services-revoke-permissions-modal.html.twig`
```twig
<mt-modal-root>
    <mt-modal :title="$t('sw-settings-services.revoke-permissions-modal.title')">
        <div class="sw-settings-services-revoke-permissions-modal__content">
            <p>{{ $t('sw-settings-services.revoke-permissions-modal.p-1') }}</p>

            <p>{{ $t('sw-settings-services.revoke-permissions-modal.p-2') }}</p>
        </div>

        <template #footer>
            <div class="sw-settings-services-revoke-permissions-modal__footer">
                <mt-modal-close
                    as="mt-button"
                    variant="secondary"
                >
                    {{ $t('global.default.cancel') }}
```

### Example 5
Source: `sw-settings-services/component/sw-settings-services-service-card/sw-settings-services-service-card.html.twig`
```twig
<mt-modal-root
    :is-open="showDeactivateModal"
    @change="showDeactivateModal = $event"
>
    <mt-modal :title="$t('sw-settings-services.general.deactivate')">
        <div class="sw-settings-services-service-card__deactivate-modal-content">
            <p>{{ $t('sw-settings-services.service-card.deactivate-modal.warning', { serviceName: service.label }) }}</p>

            <p>{{ $t('sw-settings-services.service-card.deactivate-modal.consequences') }}</p>
        </div>

        <template #footer>
            <div class="sw-settings-services-service-card__deactivate-modal-footer">
                <mt-modal-action
                    as="mt-button"
```
