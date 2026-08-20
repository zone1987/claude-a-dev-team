# TypeScript im Shopware-Admin-Plugin — Referenz

## Vollständige tsconfig.json (am Core orientiert)
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
`allowJs: true` erlaubt schrittweise Migration (JS + TS gemischt). `noEmit: true` — Vite transpiliert.

## Entity-Typen & Repository
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

## Komponente (Options-API mit Typen)
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

## Module-Augmentation / globale Typen
Eigene `.d.ts` (z.B. `src/types/ff.d.ts`), via tsconfig `include` erfasst:
```ts
declare global {
  interface Window { ffExampleConfig?: { apiKey: string }; }
}
export {};
```

## Services / Composables typisieren
- Konstruktor-Argumente und Rückgaben annotieren.
- Für injizierte Services Interfaces definieren und im Service-Provider zurückgeben.
- Meteor-Admin-SDK-Aufrufe sind bereits typisiert (siehe Skill `sw-meteor-admin-sdk`).

## Hinweise
- Vue 3 Composition API: `defineComponent`-Muster bzw. `<script setup lang="ts">` in SFCs (sofern Build unterstützt).
- Lint/Typecheck: `composer eslint:admin` + projektweiter `tsc --noEmit` (über die tsconfig).
- `strict` aktiv halten; `noUncheckedIndexedAccess` optional für mehr Sicherheit.
