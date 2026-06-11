# sw-wizard-page

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| isActive | `any` | — | no |  |
| title | `any` | — | no |  |
| position | `any` | — | no |  |

## Slots

| Name | Slot Props | Description |
|------|-----------|-------------|
| default | — | |

## Methods

| Method | Description |
|--------|-------------|
| `createdComponent` | |
| `destroyedComponent` | |

## Examples

### Example 1
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard-page
    :position="0"
    :title="pageTitleSnippet('sw-import-export.profile.generalTab')"
>
    <sw-import-export-new-profile-wizard-general-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
```

### Example 2
Source: `sw-import-export/component/profile-wizard/sw-import-export-new-profile-wizard/sw-import-export-new-profile-wizard.html.twig`
```twig
<sw-wizard-page
    :position="csvUploadPagePosition"
    :title="pageTitleSnippet('sw-import-export.profile.csvUploadTab')"
>
    <sw-import-export-new-profile-wizard-csv-page
        :profile="profile"
        @next-disable="onNextDisable"
        @next-allow="onNextAllow"
    />
</sw-wizard-page>
```
