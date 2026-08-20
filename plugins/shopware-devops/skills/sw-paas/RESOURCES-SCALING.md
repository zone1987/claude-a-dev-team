# Shopware PaaS Native — Resources & scaling

## Default resource profile

| Component    | Replicas | CPU req | Memory req | Memory limit |
|--------------|----------|---------|------------|--------------|
| `storefront` | 2        | 50m     | 256Mi      | 2Gi          |
| `admin`      | 1        | 25m     | 128Mi      | 2Gi          |
| `worker`     | 1        | 50m     | 256Mi      | 1Gi          |

Scaling: primarily **horizontal** (more replicas).
Limits depend on the booked plan.

## Snapshots (backups)

```bash
# Create a snapshot (recommended before updates/cloning)
sw-paas snapshot create
```

Snapshots contain: database + Shopware filesystem.
They are used as the source snapshot for cloning.

## Deployment types

```bash
# Latest build
sw-paas application deploy create

# Deploy a specific build (rollback to an older state)
sw-paas application deploy create
# → interactive build selection

# Show deployments
sw-paas application deploy list
sw-paas application deploy get
```

## Important limits

- **Number of projects/applications**: depends on the plan
- **Additional queues**: not configurable
- **Shopware only**: no other application types (no Node.js etc.)
- **AWS only**: no Azure or GCP

## Deep dive

[RESOURCES-SCALING-DETAIL.md](RESOURCES-SCALING-DETAIL.md)
