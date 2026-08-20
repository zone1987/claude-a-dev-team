# TypeScript im Shopware-Storefront-Plugin — Referenz

## Vollständige tsconfig.json (am Core orientiert)
```json
{
  "compilerOptions": {
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "noEmit": true,
    "allowImportingTsExtensions": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noUncheckedIndexedAccess": true,
    "baseUrl": "./",
    "paths": { "src/*": ["./src/*"] }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

## Globale Typen für PluginManager/PluginBaseClass
Falls die Storefront-Typen nicht über ein Paket bereitstehen, in einer `.d.ts` deklarieren:
```ts
// src/types/storefront.d.ts
declare global {
  class PluginBaseClass<TOptions = Record<string, unknown>> {
    el: HTMLElement;
    options: TOptions;
    $emitter: { publish(name: string, detail?: unknown): void; subscribe(name: string, cb: (e: CustomEvent) => void): void };
    init(): void;
    update?(): void;
  }
  interface Window {
    PluginBaseClass: typeof PluginBaseClass;
    PluginManager: {
      register(name: string, plugin: unknown, selector?: string, options?: unknown): void;
      override(name: string, plugin: unknown, selector?: string): void;
      extend(name: string, newName: string, plugin: unknown, selector?: string): void;
      initializePlugins(): void;
    };
  }
}
export {};
```

## Typisiertes JS-Plugin
```ts
interface FfExampleOptions { url: string; threshold: number; }

export default class FfExamplePlugin extends window.PluginBaseClass<FfExampleOptions> {
  static options: FfExampleOptions = { url: '', threshold: 0 };

  private _button: HTMLButtonElement | null = null;

  init(): void {
    this._button = this.el.querySelector<HTMLButtonElement>('[data-ff-trigger]');
    this._registerEvents();
  }

  private _registerEvents(): void {
    this._button?.addEventListener('click', this._onClick.bind(this));
  }

  private _onClick(): void {
    this.$emitter.publish('FfExample/clicked', { url: this.options.url });
  }
}
```

## AJAX/HttpClient typisieren
```ts
import HttpClient from 'src/service/http-client.service';
const client = new HttpClient();
client.get(this.options.url, (response: string) => {
  const data = JSON.parse(response) as { items: Array<{ id: string }> };
});
```

## Build & Lint
- Storefront-Build (Vite/Webpack) transpiliert `.ts` automatisch; Einstieg bleibt `main.js`/`main.ts`.
- Typecheck: `tsc --noEmit`. Lint: `composer eslint:storefront`.
- `.ts`-Plugins genauso in `main.(js|ts)` via `PluginManager.register(...)` registrieren wie JS-Plugins.
