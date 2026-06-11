---
name: sw-field-inheritance
description: >
  Field-Inheritance in Shopware 6 DAL (Parent→Child, z.B. Produkt-Varianten erben vom Hauptprodukt) mit dem
  Inherited-Flag und setParentDefinition/Inheritance-Aware-Definition. Trigger: "field inheritance", "Vererbung Felder",
  "Inherited flag", "Varianten erben", "parent child inheritance", "isInheritanceAware". Shopware 6.7.
---

# Shopware 6 — Field-Inheritance

Erlaubt, dass ein Child (z.B. Produkt-Variante) Feldwerte vom Parent erbt, wenn es selbst keinen Wert hat.

- Feld mit `->addFlags(new Inherited())` markieren.
- Die Definition macht Inheritance bekannt (`getParentDefinitionClass()` / `isInheritanceAware()` je nach Setup) und
  besitzt `parent_id` + Parent/Children-Associations.
- Beim Lesen liefert DAL den effektiven (geerbten) Wert; `translated`/`extensions` berücksichtigen das.

Klassischer Fall: `product` (Hauptprodukt) ↔ Varianten. Inheritance nur dort einsetzen, wo Varianten-Semantik
wirklich gebraucht wird — sonst normales Feld.

→ Hintergrund zu Flags: `sw-field-flags` · Associations: `sw-associations-manytoone`
