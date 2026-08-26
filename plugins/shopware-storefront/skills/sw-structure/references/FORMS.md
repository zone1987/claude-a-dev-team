<!-- distilled from shopware/storefront and shopware/core v6.7.13.1 — component/form/, element/cms-element-form/, Controller/FormController, Content/ContactForm/, plugin/forms/ -->

# Shopware Storefront — forms, from field to mail

Every form in the Storefront is built from the same seven components, validated twice, and posted to
a route that hands the data to a Store API route. Knowing that one shape covers the contact form,
the revocation form, registration, address editing and the profile forms alike.

## Contents

- [The seven field components](#the-seven-field-components)
- [form-input in detail](#form-input-in-detail)
- [The other components](#the-other-components)
- [Client-side validation](#client-side-validation)
- [FormHandler and the older plugins](#formhandler-and-the-older-plugins)
- [Submitting: normal and AJAX](#submitting-normal-and-ajax)
- [Server-side validation](#server-side-validation)
- [Showing server errors: formViolations](#showing-server-errors-formviolations)
- [The CMS form element](#the-cms-form-element)
- [The contact form end to end](#the-contact-form-end-to-end)
- [The revocation form](#the-revocation-form)
- [The newsletter form](#the-newsletter-form)
- [Where the mail is actually sent](#where-the-mail-is-actually-sent)
- [Captcha](#captcha)
- [Building your own form](#building-your-own-form)
- [Accessibility requirements](#accessibility-requirements)

## The seven field components

`storefront/component/form/`:

| Component | Renders |
|---|---|
| `form-input.html.twig` | any `<input>` — text, email, password, number, hidden |
| `form-textarea.html.twig` | a `<textarea>` |
| `form-select.html.twig` | a `<select>` |
| `form-checkbox.html.twig` | a single checkbox |
| `form-radio.html.twig` | one radio button |
| `form-radio-group.html.twig` | a group of radios with a shared legend |
| `form-select-birthday.html.twig` | the three-part day / month / year selects |

**Use these rather than writing an `<input>`.** They carry the label association, the required
marker, the `aria-describedby` wiring, the invalid state and the violation output — all of which
BFSG requires and all of which are easy to omit by hand.

## form-input in detail

```twig
{% sw_include '@Storefront/storefront/component/form/form-input.html.twig' with {
    id: 'personalMail',
    name: 'email',
    type: 'email',
    label: 'account.personalMailLabel'|trans,
    value: data.get('email'),
    validationRules: 'required,email',
    violationPath: '/email',
    autocomplete: 'email',
    placeholder: 'account.personalMailPlaceholder'|trans|striptags,
    additionalClass: 'col-md-6',
} %}
```

| Property | Required | Purpose |
|---|---|---|
| `id` | yes | the input's id; the label's `for` and the feedback ids derive from it |
| `name` | yes | the request key |
| `type` | no | defaults to `text` |
| `label` | no | label text; omitted means no visible label — then supply an `aria-label` |
| `value` | no | the initial value |
| `placeholder` | no | never a substitute for a label |
| `minlength`, `maxlength` | no | native constraints |
| `disabled` | no | renders the attribute |
| `validationRules` | no | comma-separated client rules |
| `violationPath` | no | the key server errors arrive under |
| `additionalClass` | no | classes on the `.form-group` wrapper |
| `additionalInputClass` | no | classes on the input itself |
| `attributes` | no | a hash of extra attributes |
| `description` | no | help text, linked by `aria-describedby` |

What it renders, and why each part matters:

- **`<label class="form-label" for="{{ id }}">`** — the association a screen reader needs.
- **`<span class="form-required-label" aria-hidden="true">`** when `required` is among the rules —
  the visual asterisk, hidden from screen readers because `aria-required` already says it.
- **`aria-describedby="{id}-feedback"`**, extended with `{id}-description` when `description` is
  set — so the error and help text are announced with the field.
- **`aria-required="true"`** when required.
- **`data-validation="{{ validationRules }}"`** — what the client validator reads.
- **`.is-invalid`** on the input when a violation exists for `violationPath`.
- **`<div id="{id}-feedback" class="form-field-feedback">`** — where the violation is rendered by
  `utilities/form-violation.html.twig`.

Blocks: `component_form_input`, `component_form_input_label`, `component_form_input_input`,
`component_form_input_description`, `component_form_input_feedback`,
`component_form_input_feedback_violations`.

## The other components

They take the same core properties. Differences worth knowing:

- **`form-select`** takes `options` as a list of `{ id, name }` hashes, plus `placeholder` for the
  empty first entry.
- **`form-checkbox`** puts the label after the control and supports `checked`.
- **`form-radio-group`** wraps its radios in a `<fieldset>` with a `<legend>` — required for a
  screen reader to announce what the group is asking.
- **`form-select-birthday`** posts three fields: `birthdayDay`, `birthdayMonth`, `birthdayYear`.

## Client-side validation

`src/helper/form-validation.helper.js` registers **four validators**:

| Rule | Checks |
|---|---|
| `required` | non-empty; for radios, that one of the group is checked |
| `email` | the value looks like an email address |
| `confirmation` | matches another field, e.g. password confirmation |
| `minLength` | at least `defaultMinLength` (8) or the field's `minlength` |

Written as `validationRules: 'required,email'`. A field carrying the native `required` attribute has
`required` added automatically.

On failure the helper sets `.is-invalid` on the field and `.invalid-feedback` on the message; on
success `.is-valid` and `.valid-feedback`. It also wires `aria-describedby` to the feedback element
so the message is announced.

**Client validation is convenience, never a guarantee.** The server validates independently, and it
is what actually protects the data.

## FormHandler and the older plugins

`[data-form-handler]` (`form-handler.plugin.js`) is the current plugin and the one to use. Options:

| Option | Default | Purpose |
|---|---|---|
| `validation` | `true` | validate at all |
| `validateOnSubmit` | `true` | validate before submitting |
| `focusInvalidField` | `true` | move focus to the first invalid field |
| `debounceTime` | `200` | delay before validating while typing |

It publishes `validSubmit` and `validationFailed`.

`[data-form-validation]` and `[data-form-submit-loader]` are **deprecated in 6.8**. Existing markup
still works; new forms use `[data-form-handler]`.

Related plugins that compose with it:

| Attribute | Plugin | Does |
|---|---|---|
| `[data-form-ajax-submit]` | `FormAjaxSubmit` | submits over AJAX and replaces markup |
| `[data-form-auto-submit]` | `FormAutoSubmit` | submits on change, e.g. the cart quantity |
| `[data-form-field-toggle]` | `FormFieldToggle` | shows or hides fields based on another field |
| `[data-form-preserver]` | `FormPreserver` | keeps values across a reload |
| `[data-form-add-history]` | `FormAddHistory` | writes the submission into browser history |
| `[data-form-ajax-pagination]` | `FormAjaxPagination` | paginates without a reload |
| `[data-form-add-dynamic-redirect]` | `FormAddDynamicRedirect` | sets the redirect target at submit time |

## Submitting: normal and AJAX

**Normal** — the browser posts, the controller redirects, the page reloads. Errors come back through
`formViolations`.

**AJAX** — `[data-form-ajax-submit]`:

```
submit
  -> publishes 'beforeSubmit'                  (tracking hooks here)
  -> fetch to the form's action
  -> response.text()
  -> ElementReplaceHelper.replaceFromMarkup(response, replaceSelectors)
  -> publishes 'onAfterAjaxSubmit' with { response }
  -> PluginManager re-initialises the replaced markup
```

`data-form-ajax-submit-options` carries `replaceSelectors` — the elements to swap. The route must
return **markup for those selectors**, not JSON.

Because markup is replaced, anything bound to the form must be a registered plugin.

## Server-side validation

The pattern is the same everywhere:

```php
$definition = $this->contactFormValidationFactory->create($context);
$this->validator->validate($data->all(), $definition);
```

A `DataValidationFactory` builds a `DataValidationDefinition` of Symfony constraints; `DataValidator`
throws a `ConstraintViolationException` on failure. The controller catches it and renders the form
again with the violations attached.

`ContactFormValidationFactory` for example:

| Field | Constraints |
|---|---|
| `salutationId` | `NotBlank`, `EntityExists(salutation)` |
| `email` | `NotBlank`, `Email` |
| `subject` | `NotBlank` |
| `comment` | `NotBlank` |
| `firstName` | `Regex` rejecting domain-like input; `NotBlank` when configured required |
| `lastName` | same |
| `phone` | `NotBlank` when configured required |

The `Regex` on the names is a spam guard: it rejects values that look like a domain.

Which fields are required is **configurable per sales channel**, so the factory reads the system
config — the same form has different rules in different channels.

**Extend validation** by decorating the validation factory, or by subscribing to the
`BuildValidationEvent` that fires for the definition.

## Showing server errors: formViolations

`formViolations` is one of the eight global Twig variables, populated from the request attributes
after a failed submission.

```twig
{% if formViolations.getViolations('/email') is not empty %}
```

`form-input` does this automatically when given a `violationPath`. The path is the field name with a
leading slash — `/email`, `/firstName`. Getting it wrong means the field never shows its error, and
nothing fails loudly.

`utilities/form-violation.html.twig` renders the messages.

## The CMS form element

A form placed by an editor in Shopping Experiences. `element/cms-element-form.html.twig` dispatches
on the configured type:

| Type | Template |
|---|---|
| Contact | `form-types/contact-form.html.twig` |
| Newsletter | `form-types/newsletter-form.html.twig` |
| Revocation | `form-types/online-revocation-request-form.html.twig` |

Shared field components in `form-components/`: `cms-element-form-input`,
`cms-element-form-textarea`, `cms-element-form-select-salutation`, `cms-element-form-privacy`,
`cms-element-form-info-required`, `cms-element-form-submit`, `cms-element-form-forward`.

Every CMS form posts three hidden fields, and they are load-bearing:

```twig
<input type="hidden" name="navigationId" value="{{ page.navigationId }}">
<input type="hidden" name="entityName"  value="{{ page.entityName }}">
<input type="hidden" name="slotId"      value="{{ element.id }}">
```

`slotId` identifies which form on the page submitted, `navigationId` and `entityName` give the
confirmation mail its context. Dropping them breaks multi-form pages and the mail content.

## The contact form end to end

```
element/cms-element-form/form-types/contact-form.html.twig
  fields: salutationId, firstName, lastName, email, phone, subject, comment
          + captcha + privacy notice + required-fields note + submit
          + hidden navigationId, entityName, slotId
  -> POST frontend.form.contact.send   (/form/contact)
  -> FormController::sendContactForm(RequestDataBag $data, SalesChannelContext $context)
  -> AbstractContactFormRoute::load
       EmailIdnConverter::encodeDataBag($data)      punycode for international domains
       validate against ContactFormValidationFactory
       on failure: ConstraintViolationException -> violations back to the form
  -> dispatches ContactFormEvent (EVENT_NAME 'contact_form.send')
  -> the Flow Builder reacts and sends the mail
  -> JsonResponse with the rendered success or error markup
```

The controller returns **JSON containing markup**, because the form submits over AJAX and the
response replaces the form area.

## The revocation form

Same shape, posting to `frontend.form.revocation.request` (`/form/revocation/request`). It exists
because the EU right of withdrawal requires shops to offer a revocation form; the fields are the
customer's identity, the order reference and the revocation statement.

Treat it as legally required content: do not remove the form, its privacy notice or its required
fields marker when restyling.

## The newsletter form

`frontend.form.newsletter.register.handle` (`/form/newsletter`), and inside the account
`frontend.account.newsletter` (`/widgets/account/newsletter`).

Newsletter uses **double opt-in** where configured: subscribing sends a confirmation mail, and the
subscription is only active after the link is followed. The form's `option` field carries
`subscribe` or `unsubscribe`.

## Where the mail is actually sent

**Not in the controller, and not in the route.** Each form dispatches an event —
`ContactFormEvent`, the newsletter equivalent — and the **Flow Builder** decides what happens.

```
form submitted -> route validates -> event dispatched
  -> Flow Builder flow triggered by that event
       action: send mail
       -> the mail template chosen in the flow
       -> MailService renders it with the event's data
       -> the configured mail transport sends it
```

Three consequences:

- **Changing the mail means changing the mail template**, in the administration under Settings →
  Mail templates, not in the Storefront.
- **Changing who receives it, or adding a second action**, means editing the flow.
- **No mail arriving** is usually a disabled flow or a mail transport problem, not a form defect.
  Check the flow first.

A plugin can subscribe to the same event to do something additional — write a ticket, call a CRM —
without touching the form.

## Captcha

`component/captcha/base.html.twig` renders whichever captcha the sales channel has configured:
honeypot, basic captcha (`[data-basic-captcha]`) or Google reCAPTCHA v2/v3.

reCAPTCHA is **consent-gated**: its plugins only activate when the corresponding cookie is accepted,
which is why the captcha declares cookies through `CookieGroupCollectEvent`.

Keep the include when restyling a form. Removing it removes the spam protection silently.

## Building your own form

1. **Compose the fields** from `component/form/*` — never hand-written inputs.
2. **Give each field an `id`, a `name`, a `label` and a `violationPath`.**
3. **Add `[data-form-handler]`** to the `<form>`, and `[data-form-ajax-submit]` if it should submit
   without a reload.
4. **Add a route and controller**, or a Store API route for reuse.
5. **Write a validation factory** and validate server-side; never rely on the client rules.
6. **Dispatch an event** instead of sending mail yourself, so the shop owner controls the mail
   through the Flow Builder.
7. **Include the captcha** and the privacy notice.
8. **Return markup for the replace selectors** if the form submits over AJAX.

## Accessibility requirements

BFSG makes these obligations rather than suggestions:

- **Every field has a visible label.** A placeholder is not a label — it disappears on focus.
- **Required fields are marked** both visually and with `aria-required`, and the form states what
  the marker means (`cms-element-form-info-required.html.twig`).
- **Errors are announced**: linked with `aria-describedby`, and describing what to do rather than
  only that something is wrong.
- **Focus moves to the first invalid field** on a failed submit — `focusInvalidField` does this.
- **Radio groups sit in a `<fieldset>` with a `<legend>`.**
- **`autocomplete` is set** on personal data fields; WCAG 1.3.5 requires it, and it helps everyone.
- **The form is completable by keyboard alone**, including the captcha.

The field components already do all of this. Replacing them with hand-written markup is how it gets
lost.
