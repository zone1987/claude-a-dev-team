# Shopware PaaS Native — Ressourcen & Skalierung (Deep Reference)

Quellen: `products/paas/shopware/fundamentals/applications.md`,
`products/paas/shopware/resources/databases.md`,
`products/paas/shopware/resources/object-storage.md`,
`products/paas/shopware/resources/index.md`,
`products/paas/shopware/faq.md`,
`products/paas/shopware/guides/update-shopware.md`

---

## Ressourcen-Profil

### Default-Zuteilung

| Komponente   | Default Replicas | CPU request | Memory request | Memory limit |
|--------------|-----------------|-------------|----------------|--------------|
| `storefront` | 2               | 50m         | 256Mi          | 2Gi          |
| `admin`      | 1               | 25m         | 128Mi          | 2Gi          |
| `worker`     | 1               | 50m         | 256Mi          | 1Gi          |

### Skalierungs-Prinzip

- **Primär horizontal**: Mehr Replicas des gleichen Pods
- Limits über dem Default-Profil: Abhängig vom gebuchten Plan
- Skalierung innerhalb des Plans mit gewisser Flexibilität möglich

### Plan-Abhängigkeiten

| Ressource | Abhängig vom Plan |
|-----------|------------------|
| Max. Projekte/Applications | Ja |
| CPU/Memory Limits | Ja |
| Anzahl Replicas | Ja |
| Disk-Größe | Ja (DB, Storage) |

Infrastruktur-Änderungsanfragen: Standard-Ticketing-Prozess oder dedizierter Slack-Channel.

---

## Managed MySQL Cluster

### Features (automatisch)

- Automatische Backups und Recovery
- High Availability (HA)
- Performance Monitoring und Metriken
- Ressourcen-Skalierung (CPU, RAM, Storage)
- Encryption at rest und in transit

### Datenbankzugriff

```bash
# CLI-Tunnel (Port-Forwarding)
sw-paas open service --service database --port 3306
```

- Kein direkter öffentlicher DB-Zugang
- mTLS-Tunnel: Inkompatibel mit NAT
- In VM/WSL: `Host` oder `Mirrored` Netzwerk-Modus

---

## S3 Object Storage

### Standard-Setup

Jede Application bekommt **2 S3-kompatible Buckets**:

| Bucket | Zweck |
|--------|-------|
| Public Bucket | Öffentlich zugängliche Medien, Assets |
| Private Bucket | Nicht-öffentliche Dateien |

Konfiguration via `operator.yaml` (k8s-meta):
- public, private, theme, sitemap Filesysteme → S3

### Filesystem-Zugriff

| Kontext | Filesystem |
|---------|-----------|
| `storefront` | Ja |
| `admin` | Ja |
| `worker` | Ja |
| `exec` | Ja |
| `migration` | Ja |
| `setup` | Ja |
| **`build`** | **Nein** |

### Externe Zugriff-Limitierungen

Kein direkter externer Zugriff auf S3.
Medien hinzufügen via:
- Shopware Admin Media Manager
- Shopware API
- PHP-Script in exec-Session

---

## Snapshots

Snapshots sichern: Datenbank + Shopware-Filesystem

```bash
sw-paas snapshot create
# Auf Fertigstellung warten
```

**Verwendung:**
- Vor Shopware-Updates (Empfehlung)
- Als Quelle für Clone-Operationen
- Disaster Recovery

---

## Deployment-Management

### Build-Auswahl

```bash
# Neuester Build deployen
sw-paas application deploy create

# Spezifischen Build auswählen (z.B. für Rollback)
sw-paas application deploy create
# → Interaktive Liste aller erfolgreichen Builds
```

### Deployment-Status prüfen

```bash
sw-paas application deploy list
sw-paas application deploy get

# Deployment-Logs
sw-paas application deploy logs
sw-paas application deploy logs --deployment-id <id>
sw-paas application deploy logs --follow
```

### Zero-Downtime

Alle Deployments: Kubernetes Rolling Updates = Zero Downtime.
DB-Migrationen laufen zuerst, danach Deployment Helper.

---

## Plattform-Grenzen

| Feature | Status |
|---------|--------|
| Zusätzliche Queues | Nicht konfigurierbar |
| Andere Anwendungstypen (Node.js) | Nicht unterstützt |
| Cloud Provider | Nur AWS |
| Blackfire / Tideways APM | Nicht unterstützt |
| Managed Load Testing | Nicht unterstützt |
| SSO für Grafana/OpenSearch | Nicht verfügbar |
| CDN-Customization | In Entwicklung |
| DB-Customization | In Entwicklung |

---

## Häufige Ressourcen-Fragen

**Q: Wie viele Projekte/Applications kann ich erstellen?**
Abhängig vom gebuchten Plan der Organisation.

**Q: Kann ich Infrastruktur anpassen (Webserver-Konfiguration)?**
Nein, Infrastruktur ist opinionated und pre-konfiguriert.

**Q: Gibt es Managed Load Testing?**
Nein, nicht als Plattform-Bestandteil.

**Q: Kann ich Application Performance Monitoring (Tideways/Blackfire) nutzen?**
Aktuell nicht unterstützt, in Planung.

**Q: Läuft PaaS auf Azure oder GCP?**
Nein, aktuell nur AWS.

**Q: Wie oft läuft der Scheduler?**
Alle 5 Minuten.
