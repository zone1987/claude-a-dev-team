---
name: sw-sorting
description: >
  Sortierung in der Shopware-6 Criteria-API: FieldSorting (ASC/DESC), CountSorting, natural sorting,
  Sortierung über Associations. Trigger: "Sorting criteria", "FieldSorting", "sortieren DAL", "addSorting",
  "nach Feld sortieren", "CountSorting". Shopware 6.7.
---

# Shopware 6 — Criteria-Sorting

```php
$criteria->addSorting(new FieldSorting('createdAt', FieldSorting::DESCENDING));
$criteria->addSorting(new FieldSorting('name', FieldSorting::ASCENDING, true)); // naturalSorting
// nach Aggregat/Count sortieren:
$criteria->addSorting(new CountSorting('lines.id', CountSorting::DESCENDING));
```

Mehrere Sortierungen werden in Reihenfolge angewendet. Felder über Associations per Punktnotation. Für die
Sortierung innerhalb einer nachgeladenen Association `$criteria->getAssociation('lines')->addSorting(...)`.

→ Sorting-Referenz: [references/search-criteria.md](references/search-criteria.md)
