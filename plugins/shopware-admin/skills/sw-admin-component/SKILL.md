---
name: sw-admin-component
description: >
  Eine eigene Admin-Komponente in Shopware 6 registrieren (Vue 3): Shopware.Component.register, .twig-Template,
  index.js, Composition/Options API, Meteor-Komponenten nutzen. Trigger: "Admin Component", "Component.register",
  "eigene Komponente Administration", "vue component shopware admin", "component twig template". Shopware 6.7.
  Scaffolder: /sw-admin-component.
---

# Shopware 6 — Admin-Komponente

Komponenten werden über `Shopware.Component.register(name, config)` registriert. Template als `.html.twig`
(Twig-basiertes Vue-Templating der Admin).

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

UI mit **Meteor-Komponenten** (`mt-*`, `sw-meteor-components`) aufbauen. Bestehende Komponente anpassen statt neu:
`sw-admin-component-override`. Daten via Repository (`sw-admin-repository-js`).
