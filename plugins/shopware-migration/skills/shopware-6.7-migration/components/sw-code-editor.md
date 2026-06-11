# sw-code-editor

> Code editor component with syntax highlighting (based on Ace editor).

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| value | `any` | `''` | no |  |
| label | `any` | `''` | no |  |
| completerFunction | `any` | `null` | no |  |
| editorConfig | `any` | — | no |  |
| completionMode | `any` | `'text'` | no | Valid: `entity`, `text` |
| mode | `any` | `'twig'` | no | Valid: `twig`, `text` |
| softWraps | `any` | `true` | no |  |
| setFocus | `any` | `false` | no |  |
| disabled | `any` | `false` | no |  |
| required | `any` | `false` | no |  |
| sanitizeInfoWarn | `any` | `false` | no |  |
| sanitizeInput | `any` | `false` | no |  |
| sanitizeFieldName | `any` | `null` | no |  |
| error | `any` | `null` | no |  |
| placeholder | `any` | `''` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| mounted | — | |
| update:value | — | |
| blur | — | |

## Methods

| Method | Description |
|--------|-------------|
| `mountedComponent` | |
| `beforeUnmountedComponent` | |
| `destroyedComponent` | |
| `onInput` | |
| `onBlur` | |
| `sanitizeEditorInput` | |
| `defineAutocompletion` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `aceConfig` | |
| `classes` | |
| `enableHtmlSanitizer` | |
| `attrsWithoutClass` | |

## Examples

### Example 1
Source: `sw-cms/blocks/html/html/preview/sw-cms-preview-html.html.twig`
```twig
    <sw-code-editor
        v-model:value="demoValue"
        :disabled="true"
        :editor-config="editorConfig"
    />
</div>
{% endblock %}

```

### Example 2
Source: `sw-cms/elements/html/config/sw-cms-el-config-html.html.twig`
```twig
            <sw-code-editor
                v-model:value="element.config.content.value"
                :disabled="isInherited"
                :set-focus="true"
                @update:value="onInput"
                @blur="onBlur"
            />
        </template>
    </sw-cms-inherit-wrapper>

    <mt-banner variant="attention">
        {{ $t('sw-cms.elements.html.config.warning') }}
    </mt-banner>
</div>
{% endblock %}
```

### Example 3
Source: `sw-cms/elements/html/component/sw-cms-el-html.html.twig`
```twig
    <sw-code-editor
        v-model:value="element.config.content.value"
        :disabled="true"
        :editor-config="editorConfig"
    />
</div>
{% endblock %}

```

### Example 4
Source: `sw-cms/elements/html/preview/sw-cms-el-preview-html.html.twig`
```twig
    <sw-code-editor
        v-model:value="demoValue"
        :disabled="true"
        :editor-config="editorConfig"
    />
</div>
{% endblock %}

```

### Example 5
Source: `sw-flow/component/modals/sw-flow-create-mail-template-modal/sw-flow-create-mail-template-modal.html.twig`
```twig
<sw-code-editor
    ref="plainEditor"
    :key="`${mailTemplate.mailTemplateTypeId}plain`"
    v-model:value="mailTemplate.contentPlain"
    class="sw-flow-create-mail-template-modal__content-plain"
    name="content_plain"
    completion-mode="entity"
    :label="$tc('sw-flow.modals.mail.labelContentPlain')"
    :placeholder="placeholder(mailTemplate, 'contentPlain', $tc('sw-flow.modals.mail.placeholderPlain'))"
    :completer-function="outerCompleterFunction"
    :editor-config="editorConfig"
    :error="mailTemplateContentPlainError"
    required
/>
{% endblock %}
```
