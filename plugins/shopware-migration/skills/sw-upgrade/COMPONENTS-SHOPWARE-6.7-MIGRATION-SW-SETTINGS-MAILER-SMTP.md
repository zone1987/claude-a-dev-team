# sw-settings-mailer-smtp

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| mailerSettings | `any` | — | yes |  |
| hostError | `any` | `null` | no |  |
| portError | `any` | `null` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| host-changed | — | |
| port-changed | — | |

## Computed Properties

| Name | Description |
|------|-------------|
| `isOauth` | |
| `encryptionOptions` | |

## Examples

### Example 1
Source: `sw-first-run-wizard/view/sw-first-run-wizard-mailer-smtp/sw-first-run-wizard-mailer-smtp.html.twig`
```twig
<sw-settings-mailer-smtp :mailer-settings="mailerSettings" />
```

### Example 2
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
