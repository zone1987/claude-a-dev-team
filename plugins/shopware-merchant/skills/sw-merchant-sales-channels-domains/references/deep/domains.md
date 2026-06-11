# Shopware 6 – Verkaufskanal: Domains, Sprachen, Währungen (vollständig)

> Quelle: https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
> Version: 6.7.7.0+

---

## 1. Domain-Konzept in Shopware 6

Jeder Verkaufskanal kann **mehrere Domains** besitzen. Über Domains werden folgende Parameter sprachspezifisch konfiguriert:

- URL (Protokoll + Domain + Subdomain)
- Sprache
- Währung
- Textbaustein-Set (Übersetzungen für Shop-Texte)
- Hreflang-Lokalisierung

Dieses Konzept ermöglicht es, **mehrere Sprachshops** über einen einzigen Verkaufskanal zu betreiben:
- `https://www.shop.de` → Deutsch, EUR
- `https://www.shop.at` → Deutsch (AT), EUR
- `https://www.shop.com` → Englisch, USD

---

## 2. Domain-Konfiguration: Selbst gehostete Instanz

![Domains – Selbst gehostete Instanz](../../sw-merchant-sales-channels/assets/domains-self-hosted.png)

**Zugang:** Verkaufskanal > Reiter "Allgemein" > Abschnitt "Domains"

**Button:** "Domain hinzufügen"

### Konfigurationsfelder

![Domain-Konfiguration Detail](../../sw-merchant-sales-channels/assets/domains-detail.png)

| Nr. | Feld | Beschreibung |
|---|---|---|
| 1 | **URL** | Vollständige Domain mit Subdomain; Protokoll (https/http) über Dropdown wählbar |
| 2 | **Sprache** | Aus den dem Kanal zugewiesenen Sprachen wählen |
| 3 | **Währung** | Aus den unter Einstellungen > Regional > Währungen verfügbaren Währungen |
| 4 | **Textbaustein-Set** | Aus den unter Einstellungen > Regional > Textbausteine vorhandenen Sets |
| 5 | **Hreflang-Lokalisierung** | ISO-Norm oder Browsersprache; ISO empfohlen bei landestypischen Sprachvarianten (z.B. de-AT vs. de-DE) |

### Best Practices

- **Duplicate Content vermeiden:** Domain nur mit `https://` oder `http://` hinterlegen, ohne `www.`-Suffix als zusätzliche Domain
- Wenn sowohl `www.shop.de` als auch `shop.de` erreichbar sein sollen → serverseitige Weiterleitung auf eine kanonische URL einrichten, nicht beide als Shopware-Domain eintragen

---

## 3. Domain-Konfiguration: Cloud-Instanz

![Domains – Cloud Instanz](../../sw-merchant-sales-channels/assets/domains-cloud.png)

**Standard:** Eine automatisch generierte URL wird beim Erstellen des Kanals angelegt.

**Individuelle Domain hinzufügen:**

1. Domain zuerst unter **Einstellungen > System > Domains** anlegen
2. Dann im Verkaufskanal > "Domain hinzufügen" auswählen
3. Alternativ: Link "Individuelle Domain einrichten" im Domain-Bereich nutzen

**Besonderheit Cloud:**
- Serverseitige Weiterleitung stellt https:// Verbindung automatisch sicher
- DNS-Konfiguration auf Shopware-Cloud-Server muss beim Domain-Anbieter gesetzt werden

---

## 4. Hreflang

Hreflang-Metatags sind wichtig bei mehrsprachigen Shops:

- Ordnen Seiten-Inhalte eindeutig einer Sprache und Region zu
- Verhindern, dass Google mehrsprachige Versionen als Duplicate Content einstuft
- Ermöglichen korrektes Ranking je nach Nutzersprache

**Aktivierung:** Im Grundeinstellungen-Abschnitt "Hreflang" aktivieren

Nach Aktivierung:
- Alle konfigurierten Domains erscheinen im Dropdown
- Eine Standard-Domain als Fallback für alle Sprachen auswählen

**Hreflang-Lokalisierung je Domain:**
- **ISO-Norm** (z.B. `de-DE`, `de-AT`, `en-US`) – empfohlen für länderspezifische Sprachvarianten
- **Browsersprache** (z.B. `de`, `en`) – einfacher, aber weniger präzise

![Hreflang Einstellung](../../sw-merchant-sales-channels/assets/hreflang.png)

---

## 5. Sprachen zuweisen

Sprachen werden im Grundeinstellungen-Bereich "Sprachen" (Feld 9) dem Kanal zugewiesen:

- Mehrfachauswahl möglich
- Eine Sprache als Standard-Sprache festlegen (für Besucher ohne erkannte Präferenz)
- Sprachen müssen zuvor unter **Einstellungen > System > Sprachen** angelegt werden

**Verknüpfung zu Domains:**
Jede Domain kann nur einer der dem Kanal zugewiesenen Sprachen zugeordnet werden.

---

## 6. Währungen zuweisen

Währungen werden im Grundeinstellungen-Bereich "Zahlungsarten" (Feld 3 im Zahlungs/Versand-Abschnitt):

- Mehrfachauswahl möglich
- Standard-Währung erforderlich
- Währungen müssen unter **Einstellungen > Regional > Währungen** angelegt sein

**Verknüpfung zu Domains:**
Jede Domain erhält eine Standardwährung; Besucher können andere verfügbare Währungen im Shop wählen.

---

## Quelle

https://docs.shopware.com/de/shopware-6-de/einstellungen/Verkaufskanaele
https://docs.shopware.com/de/shopware-6-de/einstellungen/domaenen
