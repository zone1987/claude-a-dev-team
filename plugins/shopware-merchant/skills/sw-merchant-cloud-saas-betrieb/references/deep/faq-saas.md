# Shopware SaaS — Häufige Fragen & Probleme

**Quelle**: https://docs.shopware.com/de/shopware-6-de/saas/haeufige-fragen

---

## Shop gesperrt — Erkennung

Drei Sperrtypen:

| Typ | Storefront | Admin | Erkennbar |
|---|---|---|---|
| **Typ 1: Storefront gesperrt** | Gesperrt | Zugänglich | Im Account + Admin sichtbar |
| **Typ 2: Vollständige Sperre** | Aufrufbar, nicht bearbeitbar | Aufrufbar, nicht bearbeitbar | Im Account + Admin |
| **Typ 3: PayPal-Problem** | Normal | Nicht bearbeitbar | Im Admin angezeigt |

---

## Shop gesperrt — Gründe

### 1. Verstoß gegen geltendes Recht
- Beispiele: Rassistische Inhalte, Waffenverkauf ohne Prüfung
- Shop wird durch Shopware gesperrt

### 2. Rechnung nicht bezahlt
- Admin wird gesperrt, Abbuchung per PayPal fehlgeschlagen
- **7 Tage Zeit** zur Anpassung der Zahlungsart
- Storefront bleibt aufrufbar (außer bei aktivem Wartungsmodus)

> ⚠️ Nach der Entsperrung: **Wartungsmodus manuell im Admin deaktivieren!**

### 3. PayPal-Verbindung getrennt
- Keine Abbuchung der Nutzungskosten möglich
- Admin wird gesperrt
- **7 Tage Zeit** zur Wiederverbindung eines neuen PayPal-Kontos
- Storefront bleibt funktionstüchtig (außer bei Wartungsmodus)

> ⚠️ Nach der Entsperrung: **Wartungsmodus manuell im Admin deaktivieren!**

---

## Testbestellung durchführen

**Voraussetzungen:**
- Gleichzeitig im Admin und im Shop mit **demselben Browser** angemeldet
- Keine In-Private/Inkognito-Session verwenden

**Erkennungszeichen:** Graue Infomeldung oben auf der Storefront-Seite sichtbar.

---

## Technische Probleme lösen

1. Alle aktivierten Erweiterungen **deaktivieren**
2. Prüfen ob Problem weiterhin besteht
3. Falls ja: Support-Ticket im Shopware Account unter „Support" erstellen (je nach Plan)

---

## Storefront wird nicht angezeigt (Error)

**Prüfschritte:**

1. **Domain prüfen:** Einstellungen > System > Domains
   - Welche Domains sind verbunden?

2. **Verkaufskanal prüfen:** Verkaufskanäle > Storefront
   - Im Bereich **Domains**: Ist die gewünschte Domain eingetragen?

---

## Wartungsmodus aktivieren

1. Verkaufskanal auswählen
2. Unter **Status** → Wartungsmodus aktivieren
3. **Whitelist für IP-Adressen** nutzen (eigene IP eintragen, um Shop anzusehen)

> **Voraussetzung:** Wartungsmodus kann nur aktiviert werden, wenn bereits ein **Plan gebucht** wurde.

---

## System Updates

- SaaS-Shop wird von Shopware **automatisch aktualisiert**
- Inkompatible Erweiterungen können **automatisch deaktiviert** werden
- Betreiber muss Erweiterungen **manuell aktualisieren und reaktivieren**
- Status: `https://status.shopware.com/`

---

## System Backup

- Nightly-Backups werden **automatisch** erstellt
- Wiederherstellung technisch möglich
- **Wird nur in speziellen Fällen durchgeführt** (Support vorher kontaktieren)

---

## Support-Link generieren

1. Im Admin oben rechts auf **„?"** klicken
2. **„Generate access link"** auswählen
3. Link an Support weitergeben

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/saas/haeufige-fragen*
