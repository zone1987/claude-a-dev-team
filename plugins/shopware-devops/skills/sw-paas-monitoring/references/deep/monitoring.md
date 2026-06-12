# Shopware PaaS Native — Monitoring (Deep Reference)

Quellen: `products/paas/shopware/monitoring/index.md`,
`products/paas/shopware/monitoring/logs.md`,
`products/paas/shopware/monitoring/traces.md`,
`products/paas/shopware/monitoring/watch.md`

Bilder: `assets/paas-monitoring-log-search.png`, `assets/paas-monitoring-log-filter.png`

---

## Monitoring-Übersicht

Shopware PaaS Native bietet drei Monitoring-Komponenten:

1. **Logs** (Loki) — Application-Logs, Deployment-Logs, Cron-Logs
2. **Traces** (Tempo) — Request-Tracing via OpenTelemetry
3. **Events** — Real-time Event-Stream via `sw-paas watch`

**Grafana-Zugang:** Via CLI-Credentials (kein SSO verfügbar):
```bash
sw-paas open grafana
```

**Nicht verfügbar:** Tideways, Blackfire, managed Load Testing.

---

## Logs — CLI

### Standard-Log-Abfrage

```bash
# Letzte 15 Minuten (Default)
sw-paas application logs

# Mit expliziten IDs
sw-paas application logs \
  --organization-id <org-id> \
  --project-id <project-id> \
  --application-id <app-id>
```

Am Ende jeder Ausgabe: Grafana Explore URL für denselben Query.

### Live-Streaming

```bash
# Nur neue Zeilen
sw-paas application logs --follow

# Mit Geschichte + Live-Stream
sw-paas application logs --follow --since 30m
```

### Filtering nach Komponenten

```bash
sw-paas application logs --component storefront
```

Verfügbare Komponenten:

| Komponente | Beschreibung |
|------------|-------------|
| `admin` | Shopware Admin-Backend |
| `command` | Via `sw-paas command create` ausgeführte Befehle |
| `cronjob` | Cron-Job-Ausführungen |
| `migration` | DB-Migrations-Logs |
| `scheduled-task` | Shopware Scheduled Tasks |
| `setup` | Deployment-Setup-Phase |
| `storefront` | Shopware Storefront |
| `worker` | Message Queue Worker |

### Zeitfenster

```bash
# Heutiges Zeitfenster (HH:MM-HH:MM)
sw-paas application logs --time-range 09:00-10:00
```

### Anzahl Zeilen

```bash
sw-paas application logs --limit 500
```

### Ausgabe-Formate

```bash
sw-paas application logs --raw           # Nur Nachrichten, keine Metadaten
sw-paas application logs --output json   # Maschinenlesbar
```

### LogQL (Fortgeschritten)

```bash
sw-paas application logs --query '{job="vector",component="storefront"} |= "error"'
```

### Spezialisierte Log-Befehle

#### Deployment-Logs

```bash
sw-paas application deploy logs
sw-paas application deploy logs --deployment-id <id>
sw-paas application deploy logs --follow
```

Alias: `sw-paas application logs` → Laufzeit-Logs (ohne `deploy`)

#### Cron-Job-Logs

```bash
sw-paas application cronjob logs
sw-paas application cronjob logs --run-id <run-id>
sw-paas application cronjob logs \
  --cronjob-id <cronjob-id> \
  --history-limit 100
sw-paas application cronjob logs --follow

# Alias
sw-paas application cron logs
```

#### Command-Logs

```bash
sw-paas command logs
sw-paas command logs --command-id <id>
sw-paas command logs --follow
```

---

## Logs — Grafana

```bash
sw-paas open grafana
# Gibt URL, Username, Passwort aus
```

### Logs in Grafana

1. **Explore** → Datenquelle: **Loki**
2. Label `component` auf gewünschten Wert setzen
3. Query ausführen

### Suchoperatoren (Explore-Ansicht)

- **Line contains**: Exakter String-Match
- **Line contains case-insensitive**: Empfohlen (case-unabhängig)

### Dashboard

Vordefiniertes Dashboard: **`Logs Dashboard`**
- Log-Ingestion-Volumen
- Integrierte Case-Insensitive-Suchbox

### Log-Retention

Logs werden **45 Tage** aufbewahrt, danach automatisch gelöscht.

---

## Traces — Grafana

Traces via OpenTelemetry (konfiguriert durch k8s-meta → `opentelemetry.yaml`).

```bash
sw-paas open grafana
```

### Traces in Grafana

1. **Explore** → Datenquelle: **Tempo**
2. Query-Typ: **Search**
3. Service Name: `shopware`
4. Query ausführen

### Trace-Retention

Traces werden **14 Tage** aufbewahrt.

---

## Events — Real-time Monitoring

```bash
# Alle Events im Projekt
sw-paas watch

# Spezifische Applications
sw-paas watch --application-ids app1,app2

# Nach Event-Typ filtern
sw-paas watch --event-types "EVENT_TYPE_DEPLOYMENT_STARTED,EVENT_TYPE_DEPLOYMENT_FINISHED"
```

Beenden: `Ctrl+C`

### Event-Typen

| Event | Beschreibung |
|-------|-------------|
| `UNSPECIFIED` | Standard/unspezifizierter Status |
| `PENDING` | Deployment wartet |
| `BASE` | Basis-Infrastruktur wird deployed |
| `BASE_FAILED` | Basis-Infrastruktur fehlgeschlagen |
| `BASE_SUCCESS` | Basis-Infrastruktur erfolgreich |
| `SHOP` | Shop-Infrastruktur wird deployed |
| `SHOP_FAILED` | Shop-Infrastruktur fehlgeschlagen |
| `SHOP_SUCCESS` | Shop-Infrastruktur erfolgreich |
| `DEPLOYING_STORE` | Shopware Store wird deployed |
| `DEPLOYING_STORE_FAILED` | Store-Deployment fehlgeschlagen |
| `DEPLOYING_STORE_SUCCESS` | Store-Deployment erfolgreich |
| `DEPLOYMENT_SUCCESS` | Vollständig erfolgreich |
| `DEPLOYMENT_FAILED` | Vollständiger Fehler |

### Deployment-Event-History

```bash
sw-paas application deploy get
# → Zeigt DEPLOYMENT STATUS HISTORY mit allen Events
```
