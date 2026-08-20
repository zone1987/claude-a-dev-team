# Shopware 6 — TypeScript im Storefront-Plugin

Das Storefront unterstützt TypeScript (ADR „add typescript support for storefront js"); JS-Plugins können als `.ts`
geschrieben werden (Core-Beispiel: `plugin/spatial/*.plugin.ts`).

## tsconfig.json (Plugin)
Im Storefront-Source-Root (`src/Resources/app/storefront/`):

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

## JS-Plugin typisieren
`window.PluginBaseClass` erweitern, `Options`-Interface deklarieren, DOM-Elemente typisiert holen:

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

Globale Typen (`window.PluginManager`, `window.PluginBaseClass`) per `.d.ts` deklarieren, falls nicht vorhanden.
Build via Storefront-Vite/Webpack (transpiliert `.ts`). Lint: `composer eslint:storefront`.

→ tsconfig-Details, globale window-Typen, AJAX/HttpClient-Typing, Beispiele: [STOREFRONT-TYPESCRIPT-TYPESCRIPT.md](STOREFRONT-TYPESCRIPT-TYPESCRIPT.md)
