# TypeScript in the Shopware Storefront plugin — reference

## Full tsconfig.json (modelled on the core)
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

## Global types for PluginManager/PluginBaseClass
If the Storefront types are not provided by a package, declare them in a `.d.ts`:
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

## Typed JS plugin
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

## Typing AJAX/HttpClient
```ts
import HttpClient from 'src/service/http-client.service';
const client = new HttpClient();
client.get(this.options.url, (response: string) => {
  const data = JSON.parse(response) as { items: Array<{ id: string }> };
});
```

## Build & Lint
- The Storefront build (Vite/webpack) transpiles `.ts` automatically; the entry point stays `main.js`/`main.ts`.
- Typecheck: `tsc --noEmit`. Lint: `composer eslint:storefront`.
- Register `.ts` plugins in `main.(js|ts)` via `PluginManager.register(...)` exactly like JS plugins.
