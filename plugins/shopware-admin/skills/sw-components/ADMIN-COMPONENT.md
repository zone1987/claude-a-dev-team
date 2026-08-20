# Shopware 6 — Admin component

Components are registered via `Shopware.Component.register(name, config)`. The template is a `.html.twig`
(the admin's Twig-based Vue templating).

```js
import template from './ff-example-card.html.twig';
Shopware.Component.register('ff-example-card', {
    template,
    props: { item: { type: Object, required: true } },
    computed: { title() { return this.item.name; } },
});
```
```twig
{% block ff_example_card %}
<mt-card :title="title">
    <mt-text-field v-model="item.name" :label="$tc('ff-example.detail.name')"/>
</mt-card>
{% endblock %}
```

Build the UI with **Meteor components** (`mt-*`, `sw-meteor-components`). Adapt an existing component instead of writing a new one:
`sw-admin-component-override`. Data via repository (`sw-admin-repository-js`).
