# Playwright Component Testing — Vollstaendige Referenz

**Status:** Experimentell (`@playwright/experimental-ct-react`, `@playwright/experimental-ct-vue`)

---

## Setup

### Installation

```bash
# Interaktiv (empfohlen)
npm init playwright@latest -- --ct
yarn create playwright --ct
pnpm create playwright --ct

# Manuell fuer React
npm install -D @playwright/experimental-ct-react
```

Erzeugte Dateien:

**`playwright/index.html`** — HTML-Geruest fuer Component-Rendering:

```html
<!DOCTYPE html>
<html lang="en">
  <body>
    <div id="root"></div>
    <script type="module" src="./index.ts"></script>
  </body>
</html>
```

**`playwright/index.ts`** — Initialisierung (Themes, globale Styles):

```typescript
// React
import { beforeMount, afterMount } from '@playwright/experimental-ct-react/hooks';
import '../src/theme.css';

beforeMount(async ({ App, hooksConfig }) => {
  // Optional: App in Provider wrappen
});

afterMount(async ({ component }) => {
  // Optional: nach dem Mount
});
```

**`playwright-ct.config.ts`** — Separate Config fuer Component Tests:

```typescript
import { defineConfig, devices } from '@playwright/experimental-ct-react';

export default defineConfig({
  testDir: './src',
  use: {
    ctPort: 3100,
    ctViteConfig: {
      // Vite-Konfiguration (Plugins, Aliase etc.)
    },
  },
});
```

---

## mount()-API

### React

```typescript
import { test, expect } from '@playwright/experimental-ct-react';
import { MyComponent } from './MyComponent';

test('renders', async ({ mount }) => {
  const component = await mount(<MyComponent msg="Hello" />);
  await expect(component).toContainText('Hello');
});
```

### Vue

```typescript
import { test, expect } from '@playwright/experimental-ct-vue';
import MyComponent from './MyComponent.vue';

test('renders', async ({ mount }) => {
  const component = await mount(MyComponent, {
    props: { msg: 'Hello' },
  });
  await expect(component).toContainText('Hello');
});
```

### Rueckgabe

`mount()` gibt einen `Locator` zurueck, der auf den gemounteten Component-Root zeigt.
Alle Locator-Methoden und Assertions sind verfuegbar.

---

## Props weitergeben

### React (JSX-Attribute)

```typescript
const component = await mount(
  <TodoItem
    item={{ title: 'Buy milk', completed: false }}
    isEditing={false}
    onSave={async () => {}}
  />
);
```

### Vue (props-Objekt)

```typescript
const component = await mount(MyComponent, {
  props: {
    title: 'Hello',
    count: 42,
    items: ['a', 'b'],
  },
});
```

**Einschraenkung:** Nur serialisierbare Plain-JavaScript-Objekte (Strings, Numbers, Dates, Arrays, einfache Objekte). Keine Browser-Objekte, Promises, Funktionen als Daten.

Fuer komplexe Objekte: Story-Wrapper-Komponente erstellen.

---

## Children / Slots

### React (JSX-Children)

```typescript
const component = await mount(
  <Button>
    <span>Click me</span>
  </Button>
);
```

### Vue (slots)

```typescript
const component = await mount(MyComponent, {
  slots: {
    default: 'Default slot content',
    header: '<h1>Custom Header</h1>',
  },
});
```

---

## Events / Callbacks

### React (Callback-Props)

```typescript
let clicked = false;
const component = await mount(
  <Button onClick={() => { clicked = true; }}>Click</Button>
);
await component.getByRole('button').click();
expect(clicked).toBe(true);
```

### Vue (on-Optionen)

```typescript
const messages: string[] = [];
const component = await mount(MyInput, {
  on: {
    input(text: string) { messages.push(text); },
    change(value: string) { messages.push(value); },
  },
});
await component.locator('input').fill('Hello');
expect(messages).toContain('Hello');
```

---

## update() — Props/Slots/Events aendern

```typescript
const component = await mount(<MyComponent step={1} />);
await expect(component).toContainText('Step 1');

await component.update(<MyComponent step={2} />);
await expect(component).toContainText('Step 2');
```

```typescript
// Vue
await component.update(MyComponent, {
  props: { step: 2 },
  on: { change: newHandler },
});
```

---

## unmount() — Component entfernen

```typescript
const component = await mount(<MyComponent />);
await component.unmount();
// Component ist jetzt aus dem DOM entfernt
```

---

## Lifecycle-Hooks (playwright/index.ts)

```typescript
import { beforeMount, afterMount } from '@playwright/experimental-ct-react/hooks';
import { ThemeProvider } from './ThemeProvider';

beforeMount<HooksConfig>(async ({ App, hooksConfig }) => {
  // hooksConfig wird aus dem Test uebergeben
  if (hooksConfig?.theme) {
    return (
      <ThemeProvider theme={hooksConfig.theme}>
        <App />
      </ThemeProvider>
    );
  }
});

afterMount<HooksConfig>(async ({ component, hooksConfig }) => {
  // component ist der Locator nach dem Mount
});
```

```typescript
// Test nutzt hooksConfig
test('with dark theme', async ({ mount }) => {
  const component = await mount<HooksConfig>(
    <MyComponent />,
    { hooksConfig: { theme: 'dark' } }
  );
});
```

---

## Locators in Component Tests

Da `mount()` einen Locator zurueckgibt, sind alle Standard-Locator-Methoden verfuegbar:

```typescript
const component = await mount(<UserForm />);

// Elemente finden
await component.getByRole('textbox', { name: 'Email' }).fill('user@example.com');
await component.getByRole('button', { name: 'Submit' }).click();

// Assertions
await expect(component.getByText('Success')).toBeVisible();
await expect(component).toHaveText('Welcome');

// Verschachtelt
await component.locator('.error-message').getByText('Required').isVisible();
```

---

## Testing Library Migration

### Konzept-Mapping

| Testing Library | Playwright |
|---|---|
| `render(<App />)` | `await mount(<App />)` |
| `screen.getByRole(...)` | `component.getByRole(...)` |
| `screen.getByText(...)` | `component.getByText(...)` |
| `screen.getByLabel(...)` | `component.getByLabel(...)` |
| `screen.getByPlaceholder(...)` | `component.getByPlaceholder(...)` |
| `screen.getByTestId(...)` | `component.getByTestId(...)` |
| `userEvent.click(el)` | `await component.locator(el).click()` |
| `userEvent.type(el, text)` | `await component.locator(el).fill(text)` |
| `waitFor(() => ...)` | Automatisch durch Auto-Wait |
| `within(container)` | `component.locator(container).getBy...` |
| `expect(el).toBeInTheDocument()` | `await expect(locator).toBeAttached()` |
| `expect(el).toBeVisible()` | `await expect(locator).toBeVisible()` |
| `expect(el).toHaveTextContent(t)` | `await expect(locator).toHaveText(t)` |

### Vorher (Testing Library)

```typescript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('sign in', async () => {
  const user = userEvent.setup();
  render(<SignInPage />);
  await user.type(screen.getByLabelText('Username'), 'John');
  await user.click(screen.getByRole('button', { name: 'Sign in' }));
  expect(await screen.findByText('Welcome, John')).toBeInTheDocument();
});
```

### Nachher (Playwright)

```typescript
import { test, expect } from '@playwright/experimental-ct-react';

test('sign in', async ({ mount }) => {
  const component = await mount(<SignInPage />);
  await component.getByLabel('Username').fill('John');
  await component.getByRole('button', { name: 'Sign in' }).click();
  await expect(component.getByText('Welcome, John')).toBeVisible();
  // Kein waitFor noetig - auto-wait
});
```

### Async-Operationen

```typescript
// STATT: waitFor(() => expect(el).toBeInTheDocument())
await expect(component.getByText('Loaded')).toBeVisible();  // wartet automatisch

// Fuer komplexe Bedingungen:
await expect.poll(async () => {
  return component.getByRole('listitem').count();
}).toBeGreaterThan(0);
```

### within() ersetzen

```typescript
// STATT: within(screen.getByRole('dialog'))
const dialog = component.getByRole('dialog');
await expect(dialog.getByRole('heading')).toHaveText('Confirm');
await dialog.getByRole('button', { name: 'OK' }).click();
```

---

## Vorteile von Playwright Component Testing

- Cross-Browser (Chromium, Firefox, WebKit)
- TypeScript out of the box
- Parallele Ausfuehrung
- Playwright Inspector, UI Mode, Trace Viewer
- Code Generation mit Codegen
- Kein jsdom-Polyfill-Problem (echter Browser)

---

Source: https://playwright.dev/docs/test-components | https://playwright.dev/docs/testing-library
