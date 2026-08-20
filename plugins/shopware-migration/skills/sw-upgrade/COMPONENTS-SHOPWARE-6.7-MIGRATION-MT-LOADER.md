# mt-loader

> Loading spinner indicator for async operations.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| size | ``${string}px`` | — | no | |

## Examples

### Example 1
Source: `sw-sso-error/page/index/sw-sso-error-index.html.twig`
```twig
<mt-loader />
```

### Example 2
Source: `sw-login/page/index/sw-login.html.twig`
```twig
<mt-loader v-if="isLoading" />
```

### Example 3
Source: `sw-login/view/sw-login-recovery-recovery/sw-login-recovery-recovery.html.twig`
```twig
<mt-loader />
```

### Example 4
Source: `sw-login/view/sw-login-login/sw-login-login.html.twig`
```twig
<mt-loader />
```

### Example 5
Source: `sw-settings-usage-data/component/sw-settings-usage-data-consent-modal/subcomponents/sw-settings-usage-data-store-data-consent-card/sw-settings-usage-data-store-data-consent-card.html.twig`
```twig
<mt-loader v-if="isLoading" />
```
