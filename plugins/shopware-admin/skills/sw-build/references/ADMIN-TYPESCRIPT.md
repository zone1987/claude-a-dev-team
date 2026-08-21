# Shopware 6 — TypeScript in the admin plugin

The administration is TypeScript-capable (Vite). Your own plugin admin code can adopt `.ts`/`.vue<script lang="ts">` step by step.

## tsconfig.json (plugin)
In the admin source root (`src/Resources/app/administration/`) a `tsconfig.json` with `strict: true`,
`baseUrl`, `paths` (`"src": ["src"]`), `types: ["vite/client", "jest"]`, `noEmit: true`, `allowJs: true`
(JS+TS can be mixed). Take the core tsconfig as your reference.

## Global Shopware types
The `Shopware` object and many building blocks are typed. Add your own global additions/module augmentation via `.d.ts`:

```ts
// types/shopware.d.ts
import 'src/core/shopware';
declare global {
  interface CustomEntityTypes { ff_example: FfExampleEntity; } // register entity type
}
export interface FfExampleEntity { id: string; name: string; active: boolean; }
```

## Typing components/services
- Components: `Shopware.Component.register('ff-x', { /* defineComponent-like, props with PropType<T> */ })`.
- Services/composables: type parameters and return values; `repositoryFactory.create<FfExampleEntity>('ff_example')`.
- The Meteor Admin SDK is fully typed (`sw-meteor-admin-sdk`).

→ Full tsconfig template, entity/repository typing, module augmentation, Vue PropType patterns: [ADMIN-TYPESCRIPT-TYPESCRIPT.md](ADMIN-TYPESCRIPT-TYPESCRIPT.md)
