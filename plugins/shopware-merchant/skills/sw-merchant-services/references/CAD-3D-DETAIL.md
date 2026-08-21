# Shopware CAD to 3D File Conversion — Vollständige Referenz

Quelle: https://docs.shopware.com/de/shopware-6-de/commercial-features/cad-to-3d-file-conversion

---

## Was ist CAD to 3D File Conversion?

Dieser Shopware-Service konvertiert **CAD-Dateien** in webfähige **3D-Modelle im GLB-Format**
direkt innerhalb der Plattform. Die Konvertierung erfolgt im Hintergrund über den Media Manager.

## Voraussetzungen

- Shopware **6.7.6.0** oder neuer
- Freikontingent: **1 Konvertierung/Monat**
- Über Freikontingent hinaus: **Shopware Intelligence+**-Abonnement

## Einschränkungen & Limitierungen

| Aspekt | Limit / Hinweis |
|---|---|
| Unterstütztes Format | Nur **.STEP-Dateien** |
| Maximale Dateigröße | **2 GB** |
| Nicht unterstützt | Materialien, Texturen, Beleuchtung, Animationen, Rigs, nicht-geometrische Daten |

**Wichtig:** Farben, Oberflächen-Materialien und sonstige Nicht-Geometrie-Daten werden bei
der Konvertierung **nicht übernommen**.

## Anwendung (Schritt für Schritt)

1. **Inhalte > Medien** in der Administration öffnen
2. STEP-Datei hochladen oder vorhandene STEP-Datei auswählen
3. Auf **„In 3D-Modell konvertieren"** klicken
   - Zugang über: Sidebar oder Kontextmenü der Datei
4. Fortschritt im Informationsbereich überwachen
5. Bei Fertigstellung: Benachrichtigung erhalten
6. Konvertiertes GLB aus dem **neu erstellten Ordner** abrufen

### Hintergrundverarbeitung
Das Fenster kann während der Konvertierung geschlossen werden.
Die Konvertierung läuft weiter.

### Automatische Organisation
Konvertierte Dateien werden automatisch in einem **neu erstellten Ordner** gespeichert.

## Technische Infrastruktur

Die Konvertierung und Optimierung nutzt die **RapidPipeline API** für die Verarbeitung
von CAD-Geometrie.

## Workflow: CAD → 3D → Vorschau → Produkt

1. STEP-Datei konvertieren → GLB erhalten (dieser Service)
2. GLB-Datei hochladen → Vorschaubild automatisch generieren (3D Preview Generator)
3. GLB-Datei dem Produkt zuweisen → 3D-Viewer in Storefront

## Freikontingente & Abonnement

| Status | Kontingent |
|---|---|
| Ohne Intelligence+ | 1 Konvertierung/Monat |
| Mit Intelligence+ | Erhöhte Nutzung |

## Verwandte Services

- **3D Preview Generator** — Erstellt Vorschaubilder für fertige .glb-Dateien
  → Skill: `sw-merchant-services-3d-preview`
- **Shopware Intelligence+** — Für mehr als 1 Konvertierung/Monat
  → Skill: `sw-merchant-services-intelligence-plus`

---

Quelle: https://docs.shopware.com/de/shopware-6-de/commercial-features/cad-to-3d-file-conversion
(abgerufen 2025-06-11)
