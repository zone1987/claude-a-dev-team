# Shopware 6 — TypeScript in the Storefront plugin

The Storefront supports TypeScript (ADR "add typescript support for storefront js"); JS plugins can be written as
`.ts` (core example: `plugin/spatial/*.plugin.ts`).

## tsconfig.json (plugin)
In the Storefront source root (`src/Resources/app/storefront/`):

```json
{
  "compilerOptions": {
    "module": "ESNext", "moduleResolution": "Bundler", "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"], "strict": true, "noEmit": true,
    "skipLibCheck": true, "forceConsistentCasingInFileNames": true,
    "baseUrl": "./", "paths": { "src/*": ["./src/*"] }
  },
  "include": ["src/**/*"], "exclude": ["node_modules"]
}
```

## Typing a JS plugin
Extend `window.PluginBaseClass`, declare an `Options` interface, fetch DOM elements typed:

```ts
interface FfExampleOptions { url: string; }
export default class FfExamplePlugin extends window.PluginBaseClass<FfExampleOptions> {
  static options: FfExampleOptions = { url: '' };
  init(): void {
    const btn = this.el.querySelector<HTMLButtonElement>('[data-ff-trigger]');
    btn?.addEventListener('click', () => this._run());
  }
  private _run(): void { /* ... */ }
}
```

Declare global types (`window.PluginManager`, `window.PluginBaseClass`) via `.d.ts` if not present.
Build via Storefront Vite/webpack (transpiles `.ts`). Lint: `composer eslint:storefront`.

→ tsconfig details, global window types, AJAX/HttpClient typing, examples: [STOREFRONT-TYPESCRIPT-TYPESCRIPT.md](STOREFRONT-TYPESCRIPT-TYPESCRIPT.md)
