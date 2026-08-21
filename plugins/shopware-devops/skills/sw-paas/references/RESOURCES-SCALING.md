# Shopware PaaS Native — Resources & scaling

## Contents

- [Default resource profile](#default-resource-profile)
- [Snapshots (backups)](#snapshots-backups)
- [Deployment types](#deployment-types)
- [Important limits](#important-limits)
- [Deep dive](#deep-dive)
- [Shopware PaaS Native — Resources & scaling (Deep Reference)](#shopware-paas-native-resources-scaling-deep-reference)

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

## Shopware PaaS Native — Resources & scaling (Deep Reference)

Sources: `products/paas/shopware/fundamentals/applications.md`,
`products/paas/shopware/resources/databases.md`,
`products/paas/shopware/resources/object-storage.md`,
`products/paas/shopware/resources/index.md`,
`products/paas/shopware/faq.md`,
`products/paas/shopware/guides/update-shopware.md`

---

### Contents

- [Resource profile](#resource-profile)
- [Managed MySQL cluster](#managed-mysql-cluster)
- [S3 object storage](#s3-object-storage)
- [Snapshots](#snapshots)
- [Deployment management](#deployment-management)
- [Platform limits](#platform-limits)
- [Common resource questions](#common-resource-questions)

### Resource profile

#### Default allocation

| Component    | Default replicas | CPU request | Memory request | Memory limit |
|--------------|-----------------|-------------|----------------|--------------|
| `storefront` | 2               | 50m         | 256Mi          | 2Gi          |
| `admin`      | 1               | 25m         | 128Mi          | 2Gi          |
| `worker`     | 1               | 50m         | 256Mi          | 1Gi          |

#### Scaling principle

- **Primarily horizontal**: more replicas of the same pod
- Limits above the default profile: depend on the booked plan
- Scaling within the plan is possible with some flexibility

#### Plan dependencies

| Resource | Depends on the plan |
|-----------|------------------|
| Max. projects/applications | Yes |
| CPU/memory limits | Yes |
| Number of replicas | Yes |
| Disk size | Yes (DB, storage) |

Infrastructure change requests: standard ticketing process or a dedicated Slack channel.

---

### Managed MySQL cluster

#### Features (automatic)

- Automatic backups and recovery
- High availability (HA)
- Performance monitoring and metrics
- Resource scaling (CPU, RAM, storage)
- Encryption at rest and in transit

#### Database access

```bash
## CLI tunnel (port forwarding)
sw-paas open service --service database --port 3306
```

- No direct public DB access
- mTLS tunnel: incompatible with NAT
- In a VM/WSL: `Host` or `Mirrored` network mode

---

### S3 object storage

#### Standard setup

Every application gets **2 S3-compatible buckets**:

| Bucket | Purpose |
|--------|-------|
| Public bucket | Publicly accessible media, assets |
| Private bucket | Non-public files |

Configuration via `operator.yaml` (k8s-meta):
- public, private, theme, sitemap filesystems → S3

#### Filesystem access

| Context | Filesystem |
|---------|-----------|
| `storefront` | Yes |
| `admin` | Yes |
| `worker` | Yes |
| `exec` | Yes |
| `migration` | Yes |
| `setup` | Yes |
| **`build`** | **No** |

#### External access limitations

No direct external access to S3.
Add media via:
- Shopware Admin Media Manager
- Shopware API
- PHP script in an exec session

---

### Snapshots

Snapshots back up: database + Shopware filesystem

```bash
sw-paas snapshot create
## Wait for completion
```

**Usage:**
- Before Shopware updates (recommended)
- As the source for clone operations
- Disaster recovery

---

### Deployment management

#### Build selection

```bash
## Deploy the latest build
sw-paas application deploy create

## Select a specific build (e.g. for a rollback)
sw-paas application deploy create
## → interactive list of all successful builds
```

#### Check deployment status

```bash
sw-paas application deploy list
sw-paas application deploy get

## Deployment logs
sw-paas application deploy logs
sw-paas application deploy logs --deployment-id <id>
sw-paas application deploy logs --follow
```

#### Zero downtime

All deployments: Kubernetes rolling updates = zero downtime.
DB migrations run first, then the deployment helper.

---

### Platform limits

| Feature | Status |
|---------|--------|
| Additional queues | Not configurable |
| Other application types (Node.js) | Not supported |
| Cloud provider | AWS only |
| Blackfire / Tideways APM | Not supported |
| Managed load testing | Not supported |
| SSO for Grafana/OpenSearch | Not available |
| CDN customization | In development |
| DB customization | In development |

---

### Common resource questions

**Q: How many projects/applications can I create?**
Depends on the organization's booked plan.

**Q: Can I customize the infrastructure (webserver configuration)?**
No, the infrastructure is opinionated and pre-configured.

**Q: Is there managed load testing?**
No, not as part of the platform.

**Q: Can I use application performance monitoring (Tideways/Blackfire)?**
Not supported at the moment, planned.

**Q: Does PaaS run on Azure or GCP?**
No, currently AWS only.

**Q: How often does the scheduler run?**
Every 5 minutes.
