# Shopware 6 – Integrationen & API-Zugänge (vollständige Referenz)

Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/system/integrationen

---

## Überblick

**Pfad:** Einstellungen > System > Integrationen  
**Verfügbar ab:** 6.3.3.0

Ermöglicht die Verbindung externer Anwendungen und Systeme über die Shopware API.

---

## Integration anlegen

1. „Integration anlegen" klicken
2. **Name** eingeben (Identifikation der Integration)
3. **Berechtigungen** wählen: Administrator oder benutzerdefinierte Rollen
4. **Zugangsdaten generieren**: Zugangs-ID + Sicherheitsschlüssel werden erstellt

> **Wichtig:** Der Sicherheitsschlüssel wird **nur einmalig angezeigt**. Sofort sicher speichern!

---

## Integrationen verwalten

Die Übersichtsseite zeigt:
- Alle angelegten Integrationen mit Name und Berechtigungen
- Bearbeitungsmöglichkeit durch Namensklick
- Kontextmenü für Bearbeitung oder Löschung

---

## Integration bearbeiten

Bei nachträglicher Bearbeitung:
- Sicherheitsschlüssel wird aus Sicherheitsgründen nicht angezeigt
- Funktion **„API-Zugangsschlüssel neu generieren"** erneuert beide Credentials (ID und Schlüssel)

---

## API-Berechtigungen

| Option | Beschreibung |
|---|---|
| Administrator | Vollständige Rechte (alle API-Endpunkte) |
| Benutzerdefinierte Rollen | Granulare Rechtevergabe wie bei Benutzerrollen |

---

## Verwendung der Credentials

Die generierten Zugangsdaten (Access Key + Secret Key) werden für:
- OAuth 2.0 Client Credentials Flow
- API-Anfragen mit Bearer-Token-Authentifizierung

Vollständige API-Dokumentation: https://developer.shopware.com

---

## API-Zugänge für einzelne Benutzer

Alternativ können API-Zugänge direkt an Benutzer geknüpft werden:
**Pfad:** Einstellungen > System > Benutzer & Rechte > [Benutzer] > Integrationen (Reiter)

- „Neuer Zugangsschlüssel"-Button generiert API-ID + Sicherheitsschlüssel
- Sicherheitsschlüssel sofort notieren (nur einmalig sichtbar)
- Bearbeitung/Löschung via Kontextmenü
