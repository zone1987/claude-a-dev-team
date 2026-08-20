# TypeScript in the Shopware admin plugin — reference

## Complete tsconfig.json (modelled on the core)
```json
{
  "compilerOptions": {
    "target": "ES2023",
    "lib": ["ES2020", "DOM", "ES2023"],
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "baseUrl": "./",
    "paths": { "src": ["src"], "src/*": ["src/*"] },
    "types": ["vite/client", "jest"],
    "resolveJsonModule": true,
    "allowJs": true,
    "noEmit": true,
    "isolatedModules": true,
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true
  },
  "include": ["./src/**/*", "./test/**/*.d.ts"],
  "exclude": ["node_modules"]
}
```
`allowJs: true` allows a step-by-step migration (JS + TS mixed). `noEmit: true` — Vite does the transpiling.

## Entity types & repository
```ts
export interface FfExampleEntity {
  id: string;
  name: string;
  active: boolean;
  createdAt: string;
  customFields?: Record<string, unknown>;
}

const repo = this.repositoryFactory.create('ff_example'); // Repository<FfExampleEntity>
const criteria = new Shopware.Data.Criteria(1, 25);
const result = await repo.search(criteria, Shopware.Context.api); // EntityCollection<FfExampleEntity>
```

## Component (Options API with types)
```ts
import template from './ff-example-card.html.twig';
import type { PropType } from 'vue';

Shopware.Component.register('ff-example-card', {
  template,
  props: {
    item: { type: Object as PropType<FfExampleEntity>, required: true },
  },
  computed: {
    title(): string { return this.item.name; },
  },
});
```

## Module augmentation / global types
Your own `.d.ts` (e.g. `src/types/ff.d.ts`), picked up via the tsconfig `include`:
```ts
declare global {
  interface Window { ffExampleConfig?: { apiKey: string }; }
}
export {};
```

## Typing services / composables
- Annotate constructor arguments and return values.
- Define interfaces for injected services and return them in the service provider.
- Meteor Admin SDK calls are already typed (see skill `sw-meteor-admin-sdk`).

## Notes
- Vue 3 Composition API: `defineComponent` pattern or `<script setup lang="ts">` in SFCs (where the build supports it).
- Lint/typecheck: `composer eslint:admin` + a project-wide `tsc --noEmit` (via the tsconfig).
- Keep `strict` enabled; `noUncheckedIndexedAccess` optional for extra safety.
