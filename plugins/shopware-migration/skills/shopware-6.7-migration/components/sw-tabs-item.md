# sw-tabs-item

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| route | `null \| null` | `''` | no |  |
| active | `any` | `false` | no |  |
| activeTab | `any` | `''` | no |  |
| name | `any` | `''` | no |  |
| hasError | `any` | `false` | no |  |
| hasWarning | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| errorTooltip | `any` | — | no |  |
| warningTooltip | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| click | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `beforeUpdateComponent` | |
| `mountedComponent` | |
| `updateActiveState` | |
| `clickEvent` | |
| `checkIfActive` | |
| `checkIfRouteMatchesLink` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isNative` | |
| `tabsItemClasses` | |

## Examples

### Example 1
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-tabs-item
    v-bind="$props"
    class="sw-settings-country__setting-tab"
    :route="{ name: isNewCountry ? 'sw.settings.country.create.general' : 'sw.settings.country.detail.general' }"
>
    {{ $tc('sw-settings-country.page.generalTab') }}
</sw-tabs-item>
```

### Example 2
Source: `sw-settings-country/page/sw-settings-country-detail/sw-settings-country-detail.html.twig`
```twig
<sw-tabs-item
    v-bind="$props"
    class="sw-settings-country__state-tab"
    :route="{ name: isNewCountry ? 'sw.settings.country.create.state' : 'sw.settings.country.detail.state' }"
>
    {{ $tc('sw-settings-country.page.stateTab') }}
</sw-tabs-item>
```

### Example 3
Source: `sw-settings-logging/component/sw-settings-logging-mail-sent-info/sw-settings-logging-mail-sent-info.html.twig`
```twig
<sw-tabs-item
    class="sw-settings-logging-mail-sent-info__tab-item"
    :active="activeTab === 'html'"
    @click="activeTab = 'html'"
>
    {{ $tc('sw-settings-logging.mailInfo.tabHTML') }}
</sw-tabs-item>
```

### Example 4
Source: `sw-settings-logging/component/sw-settings-logging-mail-sent-info/sw-settings-logging-mail-sent-info.html.twig`
```twig
<sw-tabs-item
    class="sw-settings-logging-mail-sent-info__tab-item"
    :active="activeTab === 'plain'"
    @click="activeTab = 'plain'"
>
    {{ $tc('sw-settings-logging.mailInfo.tabPlain') }}
</sw-tabs-item>
```

### Example 5
Source: `sw-settings-logging/component/sw-settings-logging-entry-info/sw-settings-logging-entry-info.html.twig`
```twig
<sw-tabs-item
    :active="activeTab === 'raw'"
    @click="activeTab = 'raw'"
>
    {{ $tc('sw-settings-logging.entryInfo.tabRaw') }}
</sw-tabs-item>
```
