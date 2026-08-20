# Shopware 6 — JS-Plugin-Katalog (Projekt-Introspektion)

Beantwortet: **„welche JS-Storefront-Plugins existieren in DIESEM Projekt?"** — aus einem gecachten Katalog.

## Nutzung
1. Katalog liegt unter `.shopware-catalog/js-plugins.md` im Projekt-Root.
2. **Fehlt/veraltet** → mit `/sw-js-plugin-map` (Agent `shopware-js-plugin-mapper`, haiku) neu erzeugen.
3. Nachschlagen: Plugin-Name → Datei, Aufgabe, Selector, Optionen, Override-Punkte — bevor man ein Core-Plugin
   überschreibt (`sw-js-plugin-override`) oder erweitert (`sw-js-plugin-extend`).

## Wann neu erzeugen
- Nach `git pull` / Plugin-Install/-Update, nach Anlegen/Ändern eigener JS-Plugins oder der `main.js`-Registry.

Zum **Bauen** neuer JS-Plugins die Referenz-Skills (`sw-storefront-js-plugin`, `sw-js-plugin-override`,
`sw-js-plugin-extend`) nutzen; der Katalog ist die Quelle der Wahrheit über vorhandene Plugins.
