# Playwright Component Testing — Complete Reference

**Status:** Experimental (`@playwright/experimental-ct-react`, `@playwright/experimental-ct-vue`)

---

## Contents

- [Setup](#setup)
- [mount() API](#mount-api)
- [Passing props](#passing-props)
- [Children / Slots](#children-slots)
- [Events / callbacks](#events-callbacks)
- [update() — changing props/slots/events](#update--changing-propsslotsevents)
- [unmount() — removing the component](#unmount--removing-the-component)
- [Lifecycle hooks (playwright/index.ts)](#lifecycle-hooks-playwrightindexts)
- [Locators in component tests](#locators-in-component-tests)
- [Testing Library migration](#testing-library-migration)
- [Advantages of Playwright component testing](#advantages-of-playwright-component-testing)

## Setup

### Installation

```bash
# Interactive (recommended)
npm init playwright@latest -- --ct
yarn create playwright --ct
pnpm create playwright --ct

# Manually for React
npm install -D @playwright/experimental-ct-react
```

Generated files:

**`playwright/index.html`** — HTML scaffold for component rendering:

```html
<!DOCTYPE html>
<html lang="en">
  <body>
    <div id="root"></div>
    <script type="module" src="./index.ts"></script>
  </body>
</html>
```

**`playwright/index.ts`** — initialization (themes, global styles):

```typescript
// React
import { beforeMount, afterMount } from '@playwright/experimental-ct-react/hooks';
import '../src/theme.css';

beforeMount(async ({ App, hooksConfig }) => {
  // Optional: wrap App in a provider
});

afterMount(async ({ component }) => {
  // Optional: after the mount
});
```

**`playwright-ct.config.ts`** — separate config for component tests:

```typescript
import { defineConfig, devices } from '@playwright/experimental-ct-react';

export default defineConfig({
  testDir: './src',
  use: {
    ctPort: 3100,
    ctViteConfig: {
      // Vite configuration (plugins, aliases etc.)
    },
  },
});
```

---

## mount() API

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

### Return value

`mount()` returns a `Locator` pointing at the mounted component root.
All locator methods and assertions are available.

---

## Passing props

### React (JSX attributes)

```typescript
const component = await mount(
  <TodoItem
    item={{ title: 'Buy milk', completed: false }}
    isEditing={false}
    onSave={async () => {}}
  />
);
```

### Vue (props object)

```typescript
const component = await mount(MyComponent, {
  props: {
    title: 'Hello',
    count: 42,
    items: ['a', 'b'],
  },
});
```

**Limitation:** only serializable plain JavaScript objects (strings, numbers, dates, arrays, simple objects). No browser objects, promises, or functions as data.

For complex objects: create a story wrapper component.

---

## Children / Slots

### React (JSX children)

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

## Events / callbacks

### React (callback props)

```typescript
let clicked = false;
const component = await mount(
  <Button onClick={() => { clicked = true; }}>Click</Button>
);
await component.getByRole('button').click();
expect(clicked).toBe(true);
```

### Vue (on options)

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

## update() — changing props/slots/events

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

## unmount() — removing the component

```typescript
const component = await mount(<MyComponent />);
await component.unmount();
// The component is now removed from the DOM
```

---

## Lifecycle hooks (playwright/index.ts)

```typescript
import { beforeMount, afterMount } from '@playwright/experimental-ct-react/hooks';
import { ThemeProvider } from './ThemeProvider';

beforeMount<HooksConfig>(async ({ App, hooksConfig }) => {
  // hooksConfig is passed in from the test
  if (hooksConfig?.theme) {
    return (
      <ThemeProvider theme={hooksConfig.theme}>
        <App />
      </ThemeProvider>
    );
  }
});

afterMount<HooksConfig>(async ({ component, hooksConfig }) => {
  // component is the locator after the mount
});
```

```typescript
// Test uses hooksConfig
test('with dark theme', async ({ mount }) => {
  const component = await mount<HooksConfig>(
    <MyComponent />,
    { hooksConfig: { theme: 'dark' } }
  );
});
```

---

## Locators in component tests

Since `mount()` returns a locator, all standard locator methods are available:

```typescript
const component = await mount(<UserForm />);

// Find elements
await component.getByRole('textbox', { name: 'Email' }).fill('user@example.com');
await component.getByRole('button', { name: 'Submit' }).click();

// Assertions
await expect(component.getByText('Success')).toBeVisible();
await expect(component).toHaveText('Welcome');

// Nested
await component.locator('.error-message').getByText('Required').isVisible();
```

---

## Testing Library migration

### Concept mapping

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
| `waitFor(() => ...)` | Automatic via auto-wait |
| `within(container)` | `component.locator(container).getBy...` |
| `expect(el).toBeInTheDocument()` | `await expect(locator).toBeAttached()` |
| `expect(el).toBeVisible()` | `await expect(locator).toBeVisible()` |
| `expect(el).toHaveTextContent(t)` | `await expect(locator).toHaveText(t)` |

### Before (Testing Library)

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

### After (Playwright)

```typescript
import { test, expect } from '@playwright/experimental-ct-react';

test('sign in', async ({ mount }) => {
  const component = await mount(<SignInPage />);
  await component.getByLabel('Username').fill('John');
  await component.getByRole('button', { name: 'Sign in' }).click();
  await expect(component.getByText('Welcome, John')).toBeVisible();
  // No waitFor needed - auto-wait
});
```

### Async operations

```typescript
// INSTEAD OF: waitFor(() => expect(el).toBeInTheDocument())
await expect(component.getByText('Loaded')).toBeVisible();  // waits automatically

// For complex conditions:
await expect.poll(async () => {
  return component.getByRole('listitem').count();
}).toBeGreaterThan(0);
```

### Replacing within()

```typescript
// INSTEAD OF: within(screen.getByRole('dialog'))
const dialog = component.getByRole('dialog');
await expect(dialog.getByRole('heading')).toHaveText('Confirm');
await dialog.getByRole('button', { name: 'OK' }).click();
```

---

## Advantages of Playwright component testing

- Cross-Browser (Chromium, Firefox, WebKit)
- TypeScript out of the box
- Parallel execution
- Playwright Inspector, UI Mode, Trace Viewer
- Code generation with codegen
- No jsdom polyfill problems (a real browser)

---

Source: https://playwright.dev/docs/test-components | https://playwright.dev/docs/testing-library
