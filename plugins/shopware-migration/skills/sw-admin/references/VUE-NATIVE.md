# Shopware — the move towards native Vue

The administration is moving off its custom layers — the Options API, Twig.js templates and Vuex —
towards single-file components with the Composition API, native blocks and Pinia.

**The Composition API extension system and the native block system (`sw-block`) are experimental.**
Their APIs can still change, and no release version is committed for when they become standard. The
article this is distilled from previously named fixed versions; those timelines were removed.

## Contents

- [Where things stand](#where-things-stand)
- [The three changes](#the-three-changes)
- [Today: the stable extension system](#today-the-stable-extension-system)
- [Experimental: the native extension system](#experimental-the-native-extension-system)

## Where things stand

Today's administration is Vue.js with custom systems layered on for extensibility:

```javascript
Shopware.Component.register('sw-component', {
    template,
    // ...
});
```

```html
{% block sw-component %}
{% endblock %}
```

The reasons for going native: developer experience and devtools, easier maintenance, alignment with
Vue 3 and whatever follows it, and the performance of Vue's own mechanisms.

## The three changes

**1. Options API to Composition API.** The Composition API is the standard in Vue's own docs and
across GitHub, and libraries like `vue-i18n` are already dropping Options API support. Together with
native blocks it is what makes single-file components possible. Removal of the Options API would be a
breaking change and can only happen in a future major version.

| System | Status today | Direction |
|---|---|---|
| Options API | standard | deprecated and removed once the migration is complete |
| Composition API extension system | experimental | becomes the standard for core components and extensions |

**2. Twig.js to native blocks.** Vue has slots, but slots do not behave like Twig blocks — Shopware
found a way to implement real blocks as native Vue components, which keeps Twig.js's extendability
while allowing SFCs. It also lowers the learning curve, since Twig.js syntax is unfamiliar to Vue
developers, and makes standard tooling (VSCode, ESLint, Prettier) work out of the box. Templates move
from external `*.html.twig` files to `.vue` files.

| System | Status today | Direction |
|---|---|---|
| Twig.js blocks | standard | deprecated and removed once the migration is complete |
| Native blocks (`sw-block`) | experimental | becomes the standard |

**3. Vuex to Pinia.** Vuex was the Vue 2 default; Pinia took its place for Vue 3. The public API
changes from `Shopware.State` to `Shopware.Store`.

| Shopware version | Vuex | Pinia |
|---|---|---|
| 6.7 | still supported for extensions\* | standard for core components |
| 6.8 | **removed completely** | standard |

\* An extension can still register Vuex states in 6.7, but **core stores are accessed through
Pinia**. See `VUEX-TO-PINIA.md`.

## Today: the stable extension system

A core component, registered with the Options API and a Twig.js template:

```javascript
Shopware.Component.register('sw-text-field', {
    template: `
        {% block sw-text-field %}
        {% endblock %}
    `,
    data() {
        return { value: null };
    },
    methods: {
        onChange() {
            this.$emit('update:value', this.value);
        },
    },
});
```

An extension overriding it, with `{% parent %}` to keep the original block content:

```javascript
Shopware.Component.override('sw-text-field', {
    template: `
        {% block sw-text-field %}
        {% parent %}
        {{ helpText }}
        {% endblock %}
    `,
    props: {
        helpText: { type: String, required: false },
    },
});
```

An extension adding a component of its own:

```javascript
Shopware.Component.register('your-crazy-ai-field', {
    template: `
        {% block your-crazy-ai-field %}
        {# ... #}
        {% endblock %}
    `,
    // Options API implementation
});
```

## Experimental: the native extension system

Once migrated, a core component is a single-file component using the Composition API, with a native
block component instead of Twig blocks. Vue is imported normally (`import { ref, defineEmits } from
'vue'`), and extensibility comes from **`Shopware.Component.createExtendableSetup`**:

```javascript
const { value, onChange, privateExample } = Shopware.Component.createExtendableSetup({
    props,
    context,
    name: 'originalComponent',
}, () => {
    const emit = defineEmits(['update:value']);

    const value = ref(null);
    const onChange = () => {
        emit('update:value', value.value);
    };

    const privateExample = ref('This is a private property');

    return {
        public: { value, onChange },
        // anything outside `public` stays private to the component
    };
});
```

The `public` block is the seam: it declares what an extension may reach, so a component can expose
part of its setup without exposing all of it.

An extension's own SFC declares its props the Vue way, with `defineProps` imported from `vue`:

```javascript
import { defineProps } from 'vue';

const props = defineProps({
    helpText: { type: String, required: false },
});
```

A file that changes the existing public API uses `Shopware.Component.overrideComponentSetup`
alongside it.

## Source

[developer.shopware.com/docs/guides/upgrades-migrations/administration/vue-native.html](https://developer.shopware.com/docs/guides/upgrades-migrations/administration/vue-native.html),
Shopware 6.7, retrieved 2026-08-21.
