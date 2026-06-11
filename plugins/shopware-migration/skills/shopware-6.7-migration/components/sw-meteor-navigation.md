# sw-meteor-navigation

> A back-navigation component used within `sw-meteor-page`. Displays a "Back" link that navigates to the parent route. Automatically determines the parent route from the current route's meta data or from an explicit `fromLink` prop.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| fromLink | `RouteLocationNamedRaw \| null` | `null` | no | Explicit parent route to navigate back to. If not provided, falls back to `$route.meta.parentPath`. |

## Slots

This component does not provide slots.

## Events / Emits

This component does not emit custom events.

## Methods

This component does not define public methods.

## Computed Properties

| Name | Type | Description |
|------|------|-------------|
| hasParentRoute | `Boolean` | Whether a parent route is available (determines visibility) |
| parentRoute | `RouteLocationNamedRaw \| null` | Resolved parent route — uses `fromLink` if provided, otherwise derives from `$route.meta.parentPath` |

## Examples

### Example 1: Default Usage (inside sw-meteor-page)
The component is primarily used internally by `sw-meteor-page`:
```html
<sw-meteor-navigation :from-link="fromLink" />
```

### Example 2: With Explicit fromLink
```html
<sw-meteor-navigation
    :from-link="{ name: 'sw.extension.my-extensions.listing' }"
/>
```

### Example 3: Automatic Parent Route
When no `fromLink` is provided, the component reads `$route.meta.parentPath` to determine the back link:
```html
<!-- In a route with meta: { parentPath: 'sw.settings.index' } -->
<sw-meteor-navigation />
<!-- Renders a back link to sw.settings.index -->
```
