---
name: sw-code-structure
description: >
  Shopware-6 Bundle- und Plugin-Code-Struktur: welcher Extension-Typ für welchen Use Case (Plugin,
  App, Bundle, Theme), Verzeichnis-Layout, Namespace-Konventionen, Domänen-Schnitt, Upgrade-orientierte
  Struktur, Isolierung von Integration-Points. Trigger: "plugin struktur", "bundle layout",
  "app struktur shopware", "namespace konventionen shopware", "verzeichnisstruktur plugin",
  "welchen extension typ", "plugin vs app", "code struktur shopware", "upgrade friction shopware".
  Shopware 6.7.
---

# Shopware 6 — Code-Struktur und Extension-Typen

Vollständige Referenz: `references/deep/code-structure.md`

## Extension-Typ wählen

| Typ | Wann | Besonderheit |
|-----|------|-------------|
| **Custom Bundle** | Projekt-eigene Installation, volle Kontrolle | Kein Plugin-Lifecycle, nur Symfony Bundle |
| **Static Plugin** | Projektspezifisch, wenige Projekte | Standard-Skeleton, Overrides dünn halten |
| **Managed Plugin** | Shopware Store-Veröffentlichung | Strenge Metadaten, BC-Garantien, keine Projekt-Hacks |
| **App** | Kein PHP im Shop / SaaS / Cloud | Manifest + App-Server, multi-tenant |
| **Theme** | Nur Storefront-Optik anpassen | Stripped-down Plugin; in Cloud via App |

## Kern-Konventionen

- PSR-4 Autoloading: Namespaces exakt zu Ordnernamen mappen
- `composer.json` type: `shopware-platform-plugin` oder `shopware-bundle`
- DB-Änderungen: immer via Migrations (idempotent, non-destructive in `update()`)
- Integration-Points (Events, DAL Extensions, Decorators) hinter Service-Klassen kapseln

## Upgrade-Orientierung

- Wenige Cross-Plugin-Abhängigkeiten
- Zusammengehörige Logik NICHT auf mehrere Plugins aufteilen
- Ein Repository mit konsistentem Tooling bevorzugen
- Je mehr Surface Area dem Platform-Core ausgesetzt ist, desto mehr Upgrade-Aufwand entsteht

Abgrenzung: Dieser Skill behandelt Struktur und Layout. Erweiterungs-Patterns (Events/Decorator)
→ `sw-extendability`. Coding-Style und Static Analysis → `sw-coding-guidelines`.
