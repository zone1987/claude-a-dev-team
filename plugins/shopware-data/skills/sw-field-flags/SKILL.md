---
name: sw-field-flags
description: >
  Shopware-6 DAL-Field-Flags: PrimaryKey, Required, ApiAware, Inherited, Runtime, Computed, ReadProtected,
  WriteProtected, SearchRanking, AllowHtml, CascadeDelete, RestrictDelete, SetNullOnDelete.
  Trigger: "Field flag", "addFlags", "ApiAware", "Required flag", "Inherited flag", "CascadeDelete",
  "Runtime field", "SearchRanking". Shopware 6.7.
---

# Shopware 6 — Field-Flags

Flags steuern Verhalten/Sichtbarkeit eines Feldes: `->addFlags(new Required(), new ApiAware())`.

| Flag | Wirkung |
|---|---|
| `PrimaryKey` | Teil des Primärschlüssels |
| `Required` | Pflichtfeld beim Schreiben |
| `ApiAware` | über API les-/schreibbar (sonst intern) |
| `Inherited` | Vererbung Parent→Child (→ `sw-field-inheritance`) |
| `Runtime` | nicht persistiert, zur Laufzeit befüllt (Subscriber/Resolver) |
| `Computed` | berechnet, nicht schreibbar |
| `CascadeDelete` / `RestrictDelete` / `SetNullOnDelete` | Lösch-Verhalten von Associations |
| `SearchRanking` | Gewicht in der Volltextsuche |
| `ReadProtected` / `WriteProtected` | Zugriffsschutz je Scope (→ `sw-entity-protection`) |
| `AllowHtml` | HTML im Wert erlaubt |

Faustregel: API-Felder explizit `ApiAware` machen; interne Felder ohne. Association-Lösch-Flags bewusst wählen.

→ Alle Flags mit Details: [references/flags.md](references/flags.md)
