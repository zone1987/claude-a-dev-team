# Shopware PaaS Native — Monitoring (Deep Reference)

Sources: `products/paas/shopware/monitoring/index.md`,
`products/paas/shopware/monitoring/logs.md`,
`products/paas/shopware/monitoring/traces.md`,
`products/paas/shopware/monitoring/watch.md`

Images: `assets/paas-monitoring-log-search.png`, `assets/paas-monitoring-log-filter.png`

---

## Contents

- [Monitoring overview](#monitoring-overview)
- [Logs — CLI](#logs-cli)
- [Logs — Grafana](#logs-grafana)
- [Traces — Grafana](#traces-grafana)
- [Events — real-time monitoring](#events-real-time-monitoring)

## Monitoring overview

Shopware PaaS Native provides three monitoring components:

1. **Logs** (Loki) — application logs, deployment logs, cron logs
2. **Traces** (Tempo) — request tracing via OpenTelemetry
3. **Events** — real-time event stream via `sw-paas watch`

**Grafana access:** via CLI credentials (no SSO available):
```bash
sw-paas open grafana
```

**Not available:** Tideways, Blackfire, managed load testing.

---

## Logs — CLI

### Standard log query

```bash
# Last 15 minutes (default)
sw-paas application logs

# With explicit IDs
sw-paas application logs \
  --organization-id <org-id> \
  --project-id <project-id> \
  --application-id <app-id>
```

At the end of each output: a Grafana Explore URL for the same query.

### Live streaming

```bash
# New lines only
sw-paas application logs --follow

# With history + live stream
sw-paas application logs --follow --since 30m
```

### Filtering by component

```bash
sw-paas application logs --component storefront
```

Available components:

| Component | Description |
|------------|-------------|
| `admin` | Shopware admin backend |
| `command` | Commands run via `sw-paas command create` |
| `cronjob` | Cron job executions |
| `migration` | DB migration logs |
| `scheduled-task` | Shopware scheduled tasks |
| `setup` | Deployment setup phase |
| `storefront` | Shopware storefront |
| `worker` | Message queue worker |

### Time window

```bash
# Today's time window (HH:MM-HH:MM)
sw-paas application logs --time-range 09:00-10:00
```

### Number of lines

```bash
sw-paas application logs --limit 500
```

### Output formats

```bash
sw-paas application logs --raw           # messages only, no metadata
sw-paas application logs --output json   # machine-readable
```

### LogQL (advanced)

```bash
sw-paas application logs --query '{job="vector",component="storefront"} |= "error"'
```

### Specialized log commands

#### Deployment logs

```bash
sw-paas application deploy logs
sw-paas application deploy logs --deployment-id <id>
sw-paas application deploy logs --follow
```

Alias: `sw-paas application logs` → runtime logs (without `deploy`)

#### Cron job logs

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

#### Command logs

```bash
sw-paas command logs
sw-paas command logs --command-id <id>
sw-paas command logs --follow
```

---

## Logs — Grafana

```bash
sw-paas open grafana
# Prints URL, username, password
```

### Logs in Grafana

1. **Explore** → data source: **Loki**
2. Set the `component` label to the desired value
3. Run the query

### Search operators (Explore view)

- **Line contains**: exact string match
- **Line contains case-insensitive**: recommended (case-independent)

### Dashboard

Predefined dashboard: **`Logs Dashboard`**
- Log ingestion volume
- Built-in case-insensitive search box

### Log retention

Logs are kept for **45 days**, then deleted automatically.

---

## Traces — Grafana

Traces via OpenTelemetry (configured by k8s-meta → `opentelemetry.yaml`).

```bash
sw-paas open grafana
```

### Traces in Grafana

1. **Explore** → data source: **Tempo**
2. Query type: **Search**
3. Service name: `shopware`
4. Run the query

### Trace retention

Traces are kept for **14 days**.

---

## Events — real-time monitoring

```bash
# All events in the project
sw-paas watch

# Specific applications
sw-paas watch --application-ids app1,app2

# Filter by event type
sw-paas watch --event-types "EVENT_TYPE_DEPLOYMENT_STARTED,EVENT_TYPE_DEPLOYMENT_FINISHED"
```

Quit with: `Ctrl+C`

### Event types

| Event | Description |
|-------|-------------|
| `UNSPECIFIED` | Default/unspecified status |
| `PENDING` | Deployment is waiting |
| `BASE` | Base infrastructure is being deployed |
| `BASE_FAILED` | Base infrastructure failed |
| `BASE_SUCCESS` | Base infrastructure succeeded |
| `SHOP` | Shop infrastructure is being deployed |
| `SHOP_FAILED` | Shop infrastructure failed |
| `SHOP_SUCCESS` | Shop infrastructure succeeded |
| `DEPLOYING_STORE` | Shopware store is being deployed |
| `DEPLOYING_STORE_FAILED` | Store deployment failed |
| `DEPLOYING_STORE_SUCCESS` | Store deployment succeeded |
| `DEPLOYMENT_SUCCESS` | Fully successful |
| `DEPLOYMENT_FAILED` | Complete failure |

### Deployment event history

```bash
sw-paas application deploy get
# → shows DEPLOYMENT STATUS HISTORY with all events
```
