# Shopware 6 — TypeScript im Admin-Plugin

Die Administration ist TypeScript-fähig (Vite). Eigener Plugin-Admin-Code kann schrittweise `.ts`/`.vue<script lang="ts">` nutzen.

## tsconfig.json (Plugin)
Im Admin-Source-Root (`src/Resources/app/administration/`) eine `tsconfig.json` mit `strict: true`,
`baseUrl`, `paths` (`"src": ["src"]`), `types: ["vite/client", "jest"]`, `noEmit: true`, `allowJs: true`
(JS+TS mischbar). Am Core-tsconfig orientieren.

## Globale Shopware-Typen
Das `Shopware`-Objekt und viele Bausteine sind getypt. Eigene globale Ergänzungen/Module-Augmentation per `.d.ts`:

```ts
// types/shopware.d.ts
import 'src/core/shopware';
declare global {
  interface CustomEntityTypes { ff_example: FfExampleEntity; } // Entity-Typ registrieren
}
export interface FfExampleEntity { id: string; name: string; active: boolean; }
```

## Komponenten/Services typisieren
- Components: `Shopware.Component.register('ff-x', { /* defineComponent-ähnlich, props mit PropType<T> */ })`.
- Services/Composables: Parameter & Rückgaben typisieren; `repositoryFactory.create<FfExampleEntity>('ff_example')`.
- Meteor-Admin-SDK ist vollständig getypt (`sw-meteor-admin-sdk`).

→ tsconfig-Vollvorlage, Entity-/Repository-Typing, Module-Augmentation, Vue-PropType-Muster: [ADMIN-TYPESCRIPT-TYPESCRIPT.md](ADMIN-TYPESCRIPT-TYPESCRIPT.md)
