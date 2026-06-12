# Shopware PaaS Native — CDN & Custom Domains (Deep Reference)

Quellen: `products/paas/shopware/cdn/index.md`,
`products/paas/shopware/cdn/fastly-snippets.md`,
`products/paas/shopware/cdn/security-features.md`,
`products/paas/shopware-paas/fastly.md`

---

## Fastly CDN — Überblick

Fastly ist das primäre CDN für Shopware PaaS Native. Vorteile:

- **Globale Performance**: Responses aus weltweiten Edge-Locations
- **Ressourcen-Optimierung**: Weniger Last auf Application-Servern
- **Redis-Entlastung**: HTTP Cache am Edge statt Redis
- **Auto-Scaling**: Traffic-Spitzen ohne App-Auswirkung

### Zwei Fastly-Services

| Service | Zweck |
|---------|-------|
| `storefront` | Proxy für Storefront und Admin |
| `cdn` | Proxy für alle S3-CDN-Assets (Public Bucket) |

### Konfiguration

Vollständig automatisch — kein zusätzliches Setup nötig.
Konfiguriert durch `config/packages/prod/fastly.yaml` (via k8s-meta).

---

## Web Application Firewall (WAF)

Standardmäßig aktiviert via Fastly NGWAF — kein User-Action erforderlich.

- Feature Set: NGWAF `Core`
- Schutz gegen: OWASP Top 10 Kategorien
- Weitere Add-ons in Roadmap (kein konkreter Zeitplan)

---

## Custom Domains

### Voraussetzungen

- `sw-paas` CLI installiert und konfiguriert
- Organization-ID bekannt: `sw-paas org list`
- Domain registriert mit DNS-Verwaltungszugang
- Deployment-Berechtigungen vorhanden

### Wichtig: DNS vor Domain-Anlage konfigurieren!

Die Plattform validiert DNS in Echtzeit bei `sw-paas domain create`.
Bei Fehler: Domain-Anlage schlägt fehl.

---

### DNS-Konfiguration: Subdomain (nicht-Apex)

Beispiel: `shop.example.com`, `www.example.com`

```dns
shop.example.com.  IN  CNAME  cdn.shopware.shop.
```

### DNS-Konfiguration: Apex Domain

Beispiel: `example.com`

#### A Records (IPv4, alle 4 anlegen!)

```dns
example.com.  IN  A  151.101.3.52
example.com.  IN  A  151.101.67.52
example.com.  IN  A  151.101.131.52
example.com.  IN  A  151.101.195.52
```

#### AAAA Records (IPv6, alle 4 anlegen!)

```dns
example.com.  IN  AAAA  2a04:4e42::820
example.com.  IN  AAAA  2a04:4e42:200::820
example.com.  IN  AAAA  2a04:4e42:400::820
example.com.  IN  AAAA  2a04:4e42:600::820
```

#### TXT Record (Domain Ownership Verification)

```dns
_shopware-challenge.example.com.  IN  TXT  "shopware-challenge=<organization-id>"
```

Organization-ID ermitteln:
```bash
sw-paas org list
```

---

### DNS-Konfiguration Übersicht

| Record-Typ | Apex | Subdomain | Ziel | Anzahl | Zweck |
|------------|:----:|:---------:|------|:------:|-------|
| `CNAME` | Nein | Ja | `cdn.shopware.shop` | 1 | Traffic-Routing |
| `A` | Ja | Nein | Fastly IPv4 | 4 | IPv4-Routing |
| `AAAA` | Ja | Nein | Fastly IPv6 | 4 | IPv6-Routing |
| `TXT` | Ja | Nein | Ownership-Proof | 1 | Domain-Validierung |

---

### Schritt-für-Schritt: Domain einrichten

#### Schritt 1: DNS konfigurieren

Beim DNS-Provider/Registrar Records anlegen (siehe oben).

#### Schritt 2: DNS-Propagation prüfen

```bash
# Subdomain
dig shop.example.com CNAME

# Apex Domain
dig example.com A
dig example.com AAAA
dig _shopware-challenge.example.com TXT

# Mit öffentlichem DNS-Server testen
dig @8.8.8.8 example.com A
```

Online-Tool: https://www.whatsmydns.net

**DNS-Propagation**: Normal 15-30 Min, max. 48 Stunden.

#### Schritt 3: Domain in PaaS anlegen

```bash
sw-paas domain create
```

Mehrere Domains möglich: Befehl für jede Domain wiederholen.

#### Schritt 4: Application redeployen

```bash
sw-paas application deploy create
# Alternativ:
sw-paas application update  # (gleicher Commit nutzbar)
```

#### Schritt 5: Shopware konfigurieren

1. Shopware Admin → Sales Channel
2. Domain konfigurieren
3. Storefront zuweisen

---

### Troubleshooting: DNS-Validierung schlägt fehl

**Symptome:** Fehler bei `sw-paas domain create`

**Lösungen:**

1. **DNS-Records prüfen:**
   - Apex: Alle 4 A-Records, alle 4 AAAA-Records, TXT-Record vorhanden?
   - Subdomain: CNAME auf `cdn.shopware.shop`?

2. **Propagation abwarten:**
   - `dig` Befehle ausführen
   - Online-Tool für globale Propagation nutzen

3. **Organization-ID prüfen:**
   - `sw-paas org list`
   - TXT-Record: `shopware-challenge=<exakte-org-id>`

4. **Tippfehler ausschließen:**
   - Domain-Name korrekt?
   - Keine Leerzeichen in DNS-Records?

### Troubleshooting: Domain erstellt, keine Traffic-Antwort

**Symptome:** Domain erstellt, aber Site nicht erreichbar

**Lösungen:**

1. Deployment erfolgreich? → `sw-paas application deploy get`
2. Domain in Shopware-Admin Sales Channel eingetragen?
3. Cache leeren (Browser Incognito-Test)
4. DNS-Propagation noch im Gange? Weitere Zeit abwarten

---

## Fastly Snippets (PaaS Native)

### Storefront-Service Snippets

```bash
composer require shopware/fastly-meta
```

- `FASTLY_API_KEY` und `FASTLY_SERVICE_ID`: Automatisch bereitgestellt
- Snippets werden automatisch beim Deployment installiert/aktualisiert
- Kein weiterer Handlungsbedarf

### Einschränkungen

Aktuell nur Snippets für `storefront`-Service konfigurierbar.
Support für `cdn`-Service in Entwicklung.

---

## Fastly (klassisches Shopware PaaS / Platform.sh)

Shopware 6.4.11+ erforderlich.

### Setup

1. `FASTLY_API_TOKEN` und `FASTLY_SERVICE_ID` in Environment setzen / Support kontaktieren
2. Fastly-Package installieren:
   ```bash
   composer require fastly
   ```
3. Caching in `.platform/routes.yaml` deaktivieren
4. Pushen → Fastly wird aktiviert

### Soft Purge empfohlen

Verhindert Auswirkungen bei großen Cache-Invalidierungen.
[Fastly Soft Purge Docs](https://developer.shopware.com/docs/guides/hosting/infrastructure/reverse-http-cache.html#fastly-soft-purge)
