# Shopware PaaS Native — Ressourcen & Skalierung

## Default-Ressourcen-Profil

| Komponente   | Replicas | CPU req | Memory req | Memory limit |
|--------------|----------|---------|------------|--------------|
| `storefront` | 2        | 50m     | 256Mi      | 2Gi          |
| `admin`      | 1        | 25m     | 128Mi      | 2Gi          |
| `worker`     | 1        | 50m     | 256Mi      | 1Gi          |

Skalierung: primär **horizontal** (mehr Replicas).
Limits abhängig vom gebuchten Plan.

## Snapshots (Backups)

```bash
# Snapshot erstellen (vor Updates/Cloning empfohlen)
sw-paas snapshot create
```

Snapshots enthalten: Datenbank + Shopware-Filesystem.
Werden für Cloning als Quell-Snapshot genutzt.

## Deployment-Typen

```bash
# Neuester Build
sw-paas application deploy create

# Spezifischen Build deployen (Rollback auf älteren Stand)
sw-paas application deploy create
# → Interaktive Build-Auswahl

# Deployments anzeigen
sw-paas application deploy list
sw-paas application deploy get
```

## Wichtige Limits

- **Anzahl Projekte/Applications**: Abhängig vom Plan
- **Zusätzliche Queues**: Nicht konfigurierbar
- **Nur Shopware**: Keine anderen Anwendungstypen (kein Node.js etc.)
- **AWS only**: Kein Azure oder GCP

## Vertiefung

[RESOURCES-SCALING-DETAIL.md](RESOURCES-SCALING-DETAIL.md)
