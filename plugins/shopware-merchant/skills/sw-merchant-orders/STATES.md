# Shopware 6 – Status-Management (Bestell-/Zahlungs-/Lieferstatus)

Vollständige Referenz aller Status, Übergänge und der Zahlungslogik nach der Bestellung.

Ausführliche Dokumentation: [STATES-DETAIL.md](STATES-DETAIL.md)

## Drei Status-Dimensionen

| Status | Kontrolliert |
|---|---|
| Bestellstatus | Gesamtzustand der Bestellung; Stornierung setzt Lagerbestand frei |
| Zahlungsstatus | Zahlungsvorgang (Offen → Bezahlt / Fehlgeschlagen / Erstattet) |
| Lieferstatus | Versandprozess (Offen → Geliefert → Retoure) |

## Quelle
https://docs.shopware.com/de/shopware-6-de/bestellungen/uebersicht
https://docs.shopware.com/de/shopware-6-de/bestellungen/zahlungsvorgang-nach-bestellung
