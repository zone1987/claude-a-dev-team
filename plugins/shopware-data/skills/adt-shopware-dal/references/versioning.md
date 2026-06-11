# Versioning System

## Overview

Implements a Git-like model: entities can have versions, each version contains commits, each commit contains data entries. Creating a version clones the entity. Merging replays all commits against the live version.

## Entities

### VersionDefinition

Entity name: `version`. Fields: `id`, `name`, `commits` (OneToMany). Not version-aware itself.

### VersionCommitDefinition

Entity name: `version_commit`. Parent: Version. Fields: `id`, `versionId`, `userId`, `integrationId`, `autoIncrement`, `isMerge`, `message`, `data` (OneToMany, CascadeDelete).

### VersionCommitDataDefinition

Entity name: `version_commit_data`. Parent: VersionCommit. Fields: `id`, `versionCommitId`, `entityName`, `entityId` (JSON), `action`, `payload` (VersionDataPayloadField).

## VersionManager

Core engine for versioned CRUD operations.

### Key Operations

**createVersion(EntityDefinition, string $id, WriteContext, ?string $name, ?string $versionId): string**
1. Creates a Version entity
2. Clones source entity into the new version
3. Dispatches EntityWrittenContainerEvent
4. Writes audit log

**merge(string $versionId, WriteContext): void**
1. Acquires lock (`sw-merge-version-{id}`)
2. Loads all commits with data, sorted by autoIncrement
3. Dispatches `BeforeVersionMergeEvent`
4. Builds write operations (insert/update/delete) via `buildWrites()`
5. Executes against live version via SyncOperations
6. Creates merge commit
7. Deletes version entity and cloned records

**clone(EntityDefinition, string $id, string $newId, string $versionId, WriteContext, CloneBehavior): array**
1. Loads entity with all CascadeDelete associations
2. Filters properties: removes version fields, handles extensions, respects WriteProtected
3. Recursively processes OneToMany/OneToOne/ManyToMany with `CascadeDelete(cloneRelevant: true)`
4. For ManyToMany: only copies `{id: ...}` references
5. Applies CloneBehavior overwrites
6. Writes in SYSTEM_SCOPE

### CloneBehavior

Controls clone operation: `$overwrites` (field values to override), `$cloneChildren` (whether to clone child entities, default true).

### Audit Log

Written for non-live versions only. Creates version_commit and version_commit_data records tracking all changes.

### Cleanup

`CleanupVersionTask`: Daily scheduled task that deletes old version and version_commit records in batches of 1000.
