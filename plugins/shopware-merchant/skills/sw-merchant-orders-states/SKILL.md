---
name: sw-merchant-orders-states
description: >
  Bestellstatus Shopware, Zahlungsstatus Bestellung, Lieferstatus Bestellung, Status ändern
  Bestellung, Statusübergänge Shopware, Bestellstatus Workflow, Zahlungsstatus offen bezahlt
  erstattet, Lieferstatus geliefert Retoure, After-Order-Payment, Zahlung nach Bestellung,
  Bestellung stornieren Lagerbestand, E-Mail bei Statusänderung
---

# Shopware 6 – Status-Management (Bestell-/Zahlungs-/Lieferstatus)

Vollständige Referenz aller Status, Übergänge und der Zahlungslogik nach der Bestellung.

Ausführliche Dokumentation: [`references/deep/states.md`](references/deep/states.md)

## Drei Status-Dimensionen

| Status | Kontrolliert |
|---|---|
| Bestellstatus | Gesamtzustand der Bestellung; Stornierung setzt Lagerbestand frei |
| Zahlungsstatus | Zahlungsvorgang (Offen → Bezahlt / Fehlgeschlagen / Erstattet) |
| Lieferstatus | Versandprozess (Offen → Geliefert → Retoure) |

## Quelle
https://docs.shopware.com/de/shopware-6-de/bestellungen/uebersicht
https://docs.shopware.com/de/shopware-6-de/bestellungen/zahlungsvorgang-nach-bestellung
