# Shopware Services — Vollständige Referenz

Quelle: https://docs.shopware.com/de/shopware-6-de/shopware-services

---

## Was sind Shopware Services?

Shopware Services sind cloudbasierte Erweiterungen, die **exklusiv von Shopware** entwickelt werden.
Sie stellen spezifische Funktionen über **APIs und Webhooks** bereit und integrieren sich nativ
in die Administrationsoberfläche.

**Kernmerkmale:**
- Schnelle Bereitstellung ohne Core-Updates
- Automatische Updates ohne manuelle Eingriffe
- Anbindung über APIs/Webhooks
- Native Integration in die Shopware-Administration

## Verfügbare Services (Stand: 2025)

### Shopware Intelligence+
Abonnement-Service, der erweiterte KI-Funktionen und erhöhte Nutzungskontingente freischaltet.
→ Skill: `sw-merchant-services-intelligence-plus`

### Shopware Nexus
Visuelles Automatisierungstool — verbindet Shopware-Shops mit externen Systemen per Drag-and-Drop.
Status: Early Access
→ Skill: `sw-merchant-services-nexus`

### Shopware Payments
Integriertes Zahlungssystem auf Basis der PayPal-Infrastruktur.
→ Skill: `sw-merchant-services-payments`

### Copilot
Chat-basierter KI-Assistent für Shop-Betrieb und Administration.
→ Skill: `sw-merchant-services-copilot`

### Bild-Editor
KI-gestützte Produktbild-Bearbeitung (Freistellen, Hintergrund, Schatten, Neufärbung).
→ Skill: `sw-merchant-services-image-editor`

### 3D Preview Generator
Erstellt automatisch Vorschaubilder für .glb-3D-Dateien.
→ Skill: `sw-merchant-services-3d-preview`

### CAD to 3D File Conversion
Wandelt CAD-Dateien (.STEP) in webfähige GLB-3D-Modelle um.
→ Skill: `sw-merchant-services-cad-3d`

### Empfehlungs-Vorschau
Zeigt kontextbezogene Empfehlungen für Features und Erweiterungen in der Administration.
→ Skill: `sw-merchant-services-recommendation-preview`

## Kostenlose Kontingente (monatlich)

| Service | Freikontingent |
|---|---|
| Copilot (Basis-Nutzung) | 10 Anfragen |
| Bild-Editor | 20 Anfragen |
| CAD to 3D Conversion | 1 Konvertierung |
| 3D Preview Generator | — (nur mit Abo) |

Für erhöhte Nutzung: **Shopware Intelligence+**-Abonnement erforderlich.

## Aktivierung der Services

1. Shopware-Administration öffnen
2. **Einstellungen > System > Shopware Services** aufrufen
3. Gewünschten Service per Toggle aktivieren
4. Für Intelligence+: Schaltfläche „Abonnieren" klicken

## Verfügbarkeit nach Plan

Alle Services stehen grundsätzlich allen Händlern zur Verfügung — unabhängig vom Shopware-Plan
(Community Edition, Rise, Evolve, Beyond). Die Nutzung ist optional.

## Daten & Datenschutz

Für bestimmte Services (z.B. 3D Preview Generator) müssen Händler die Datenverarbeitung
über die Service-Registry explizit genehmigen.

Weitere Informationen: https://docs.shopware.com/de/shopware-6-de/einstellungen/system/daten-teilen

---

Quelle: https://docs.shopware.com/de/shopware-6-de/shopware-services (abgerufen 2025-06-11)
