---
name: sw-admin-catalog
description: >
  Den projektspezifischen Admin-Katalog von Shopware nutzen — welche Admin-Module, Komponenten, Services, Mixins,
  Direktiven, Filter und ApiServices es im KONKRETEN Projekt (Core + custom) gibt, wo sie liegen und was sie tun.
  Trigger: "welche Admin-Module/Services/Mixins gibt es", "Admin-Katalog", "welcher Service heißt", "Komponente finden admin",
  "welche Slots/Props/Events hat Komponente X", "welche Filter admin", "admin map", "Shopware Admin Inventar". Shopware 6.7.
  Erzeuger: /sw-admin-map.
---

# Shopware 6 — Admin-Katalog (Projekt-Introspektion)

Beantwortet: **„welche Admin-Bausteine existieren in DIESEM Projekt?"** — Module, Komponenten, Services, Mixins,
Direktiven, Filter, ApiServices (Core + custom) — aus einem gecachten Katalog.

Pro **Komponente** enthält der Katalog zusätzlich die Anatomie: **Props, Events, Slots und Twig-Blocks** (Override-Punkte)
sowie Zweck/Aufbau — so weiß man vor dem Bauen/Überschreiben genau, welche Slots/Props eine Komponente bietet.

## Nutzung
1. Katalog liegt unter `.shopware-catalog/admin.md` im Projekt-Root.
2. **Fehlt/veraltet** → mit `/sw-admin-map` (Agent `shopware-admin-mapper`, haiku) neu erzeugen.
3. Nachschlagen vor dem Bauen: existiert schon ein Service/Mixin/Component? Wie heißt das Modul/der Selector?
   → wiederverwenden statt neu erfinden; bestehende Komponente überschreiben (`sw-admin-component-override`).

## Wann neu erzeugen
- Nach `git pull` / Plugin-Install/-Update, nach Anlegen/Ändern eigener Module/Components/Services/Mixins.

Zum **Bauen** die Referenz-Skills (`sw-admin-module`, `sw-admin-component`, `sw-admin-services`, `sw-admin-mixins`,
`sw-admin-utils-filters`); der Katalog ist die Quelle der Wahrheit über vorhandene Admin-Bausteine.
