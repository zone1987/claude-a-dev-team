# Shopware 6 — Field inheritance

Lets a child (a product variant, for example) inherit field values from its parent when it has no value of its own.

- Mark the field with `->addFlags(new Inherited())`.
- The definition declares inheritance (`getParentDefinitionClass()` / `isInheritanceAware()`, depending on the setup) and
  owns `parent_id` plus parent/children associations.
- On read, the DAL returns the effective (inherited) value; `translated`/`extensions` take it into account.

The classic case: `product` (main product) ↔ variants. Use inheritance only where variant semantics are
genuinely needed — otherwise use a plain field.

→ Background on flags: `sw-field-flags` · Associations: `sw-associations-manytoone`
