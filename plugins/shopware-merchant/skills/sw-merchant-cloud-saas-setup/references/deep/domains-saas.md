# Shopware SaaS — Eigene Domain verbinden

**Quelle**: https://docs.shopware.com/de/shopware-6-de/saas/domains

---

## Übersicht

- **Pfad:** Einstellungen > System > Domains
- System-Domain vorhanden (nicht entfernbar)
- Button **„Domain verbinden"** zum Hinzufügen eigener Domains
- Community Edition: nur eine Domain möglich

---

## Domain verbinden — Schritt für Schritt

### Schritt 1: Domain eingeben

Unterscheidung zwischen zwei Typen:
- **Second-Level-Domain** (z.B. `meinshop.de`)
- **Subdomain** (z.B. `shop.meine-webseite.de`)

---

### Für Second-Level-Domains: A-Records setzen

Bis zu 4 IPv4-Adressen bei Shopware SaaS:
- `151.101.2.196`
- `151.101.66.196`
- `151.101.130.196`
- `151.101.194.196`

**Alternativ CNAME auf:** `shops.shopware.store`

Im Hoster-Control-Panel A-Record-Einträge anlegen, dann im Shopware-Admin verifizieren.

---

### Für Subdomains: CNAME-Record setzen

Beispiel: `shop.meine-webseite.de`

CNAME-Eintrag für den Subdomain-Teil anlegen (beim Domain-Anbieter konfigurieren).

---

### Schritt 2: Domain verifizieren

Nach DNS-Konfiguration im Shopware-Admin bestätigen.

> **Hinweis:** DNS-Propagation benötigt etwas Zeit (kann Minuten bis Stunden dauern).

---

### Schritt 3: Domain im Verkaufskanal verwenden

Ohne Verkaufskanal-Zuordnung erscheint Fehlermeldung „Die Shop-Domain ist zur Zeit nicht verfügbar".

**Lösung:**
1. Verkaufskanäle öffnen
2. Verkaufskanal-Detailseite aufrufen
3. Bereich **Domains** → „Domain hinzufügen"
4. Domain aus Dropdown wählen
5. Sprache, Währung, Textbausteinset konfigurieren
6. Speichern

---

## Weiterleitungen konfigurieren

Über das Kontextmenü bei der Domain:
- **Weiterleitung konfigurieren** — Ziel-URL und Weiterleitungstyp wählen
- **Entfernen** — Domain löschen

### 301 vs. 302 Redirects

| Typ | Bedeutung | SEO |
|---|---|---|
| **301 (Permanent)** | Dauerhaft unter neuer URL | SEO-Wert wird übertragen |
| **302 (Temporär)** | Nur vorübergehend umgeleitet | Ursprüngliche URL bleibt im Index |

---

## DNS-Konfiguration bei häufigen Hostern

### Profihost
- **Ort:** Meine Produkte > Webhosting & Domains
- A-Record: Typ „A", mehrere Einträge je eigene Zeile
- CNAME-Record: Typ „CNAME"
- Doku: `wissen.profihost.com`

### Mittwald
- **Ort:** Domains > DNS-Editor > Tab „Host Adresse / Alias"
- Doku: `mittwald.de/faq/domains-ssl/dns`

### Strato
- **Ort:** Paketübersicht > „..."-Menü > Domains verwalten
- Alternativ: Domains > Domainverwaltung
- Doku: `strato.de/faq/domains`

### All-inkl
- **Ort:** KAS > Tools > DNS-Einstellungen
- Doku: `all-inkl.com/wichtig/anleitungen/kas/tools/dns-werkzeuge`

### 1&1 / IONOS
- **Ort:** Control-Center
- Doku: `ionos.de/hilfe/domains/domain-verwenden`

### Hostpoint
- **Ort:** Control Panel > Domains > DNS Zone bearbeiten
- Doku: `support.hostpoint.ch/de/technisches/dns`

---

## Fehlerbehebung

### Fehler: NET::ERR_CERT_COMMON_NAME_INVALID / SSL_ERROR_BAD_CERT_DOMAIN
**Ursache:** Domain nicht im Shopware-Admin hinterlegt
**Lösung:** Einstellungen > System > Domains > Domain hinzufügen

### Fehler: „Die Shop-Domain ist zur Zeit nicht verfügbar"
**Ursache:** Domain verbunden, aber nicht dem Verkaufskanal zugewiesen
**Lösung:** Verkaufskanal > Domains > Domain hinzufügen (s. Schritt 3)

### Diagnose via Google Dig Toolbox

**A-Record prüfen:**
- Tool: `https://toolbox.googleapps.com/apps/dig/#A/`
- Eingabe: nur Domain (z.B. `shopware.com`)
- Muss enthalten: `151.101.2.196`, `151.101.66.196`, `151.101.130.196`, `151.101.194.196` ODER `shops.shopware.store`
- Darf keine andere IP/CNAME enthalten

**AAAA-Record prüfen:**
- Tool: `https://toolbox.googleapps.com/apps/dig/#AAAA/`
- Kann enthalten: `2a04:4e42::708`, `2a04:4e42:200::708`, `2a04:4e42:400::708`, `2a04:4e42:600::708` ODER `shops.shopware.store`
- Darf keine andere IP/CNAME enthalten

---

*Quelle: https://docs.shopware.com/de/shopware-6-de/saas/domains*
