# mt-password-field

> Password input with show/hide toggle.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `string | null` | — | no | |
| placeholder | `string` | — | no | |
| disabled | `boolean` | — | no | |
| error | `{ code: number; detail: string } | null` | — | no | |
| hint | `string | null` | — | no | |
| toggable | `boolean` | — | no | |
| name | `string | undefined` | — | no | |
| required | `boolean` | — | no | |
| helpText | `string` | — | no | |
| size | `"small" | "default"` | — | no | |
| isInherited | `boolean` | — | no | |
| isInheritanceField | `boolean` | — | no | |
| disableInheritanceToggle | `boolean` | — | no | |
| idSuffix | `string` | — | no | |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| change | value: string | undefined | |
| submit | — | |
| inheritance-restore | value: unknown | |
| inheritance-remove | value: unknown | |
| update:modelValue | value: string | undefined | |

## Examples

### Example 1
Source: `sw-extension/page/sw-extension-my-extensions-account/sw-extension-my-extensions-account.html.twig`
```twig
            <mt-password-field
                v-model="form.password"
                class="sw-extension-my-extensions-account__password-field"
                :label="$tc('sw-extension.my-extensions.account.passwordLabel')"
                :placeholder="$tc('sw-extension.my-extensions.account.passwordPlaceholder')"
                @keyup.enter="login"
            />
        </div>

        <div class="sw-extension-my-extensions-account__wrapper-content-login-footer">
            <a
                :href="$tc('sw-extension.my-extensions.account.recoveryUrl')"
                target="_blank"
                rel="noopener"
            >
```

### Example 2
Source: `sw-integration/page/sw-integration-list/sw-integration-list.html.twig`
```twig
    <mt-password-field
        v-if="secretAccessKeyFieldTypeIsPassword"
        v-model="currentIntegration.secretAccessKey"
        name="sw-field--currentIntegration-secretAccessKey"
        :label="$tc('sw-integration.detail.secretFieldLabel')"
        :disabled="true"
        :password-toggle-able="false"
        :copyable="showSecretAccessKey"
        :copyable-tooltip="true"
    />
</template>

<mt-button
    v-if="!showSecretAccessKey"
    variant="critical"
```

### Example 3
Source: `sw-inactivity-login/page/index/sw-inactivity-login.html.twig`
```twig
<mt-password-field
    v-model="password"
    v-autofocus
    :label="$tc('sw-login.index.labelPassword')"
    :disabled="isLoading"
    :error="passwordError"
    @keydown.enter="loginUserWithPassword"
/>

<mt-checkbox
    v-model:checked="rememberMe"
    :label="$tc('sw-login.index.labelKeepLoggedIn')"
/>

<template #modal-footer>
```

### Example 4
Source: `sw-login/view/sw-login-recovery-recovery/sw-login-recovery-recovery.html.twig`
```twig
        <mt-password-field
            ref="swLoginRecoveryRecoveryNewPasswordField"
            v-model="newPassword"
            :label="$tc('sw-login.recovery.recovery.newPasswordField.label')"
            :error="userPasswordError"
        />
        {% endblock %}

        {% block sw_login_recovery_recovery_form_password_confirm_field %}
        <mt-password-field
            v-model="newPasswordConfirm"
            :label="$tc('sw-login.recovery.recovery.passwordConfirmField.label')"
        />
        {% endblock %}

```

### Example 5
Source: `sw-login/view/sw-login-login/sw-login-login.html.twig`
```twig
<mt-password-field
    v-model="password"
    name="sw-field--password"
    :label="$tc('sw-login.index.labelPassword')"
    :placeholder="$tc('sw-login.index.placeholderPassword')"
    :disabled="showLoginAlert"
    required
/>
{% endblock %}

{% block sw_login_login_submit %}
<div class="sw-login__submit">
    {% block sw_login_login_submit_button %}
    <mt-button
        :disabled="password.length <= 0 || username.length <= 0 || showLoginAlert"
```
