# Meteor Icon Kit — reference

Package: `@shopware-ag/meteor-icon-kit`

## Icon naming scheme

### Format

Icons follow the scheme: `{mode}-{basename}[-{size}]`

| Part | Values | Description |
|---|---|---|
| `mode` | `regular`, `solid` | Line style or filled |
| `basename` | e.g. `home`, `save`, `shopping-cart` | Icon name (kebab case) |
| `size` | `s`, `xs` (optional) | Smaller variant |

**Examples:**
- `regular-home` — home icon, line style
- `solid-save` — save icon, filled
- `solid-filter-s` — filter icon filled, small variant
- `regular-search-xs` — search icon, extra small

### Inventory

- **regular**: 471 icons
- **solid**: 435 icons

### Usage in `mt-icon`

```html
<mt-icon name="solid-save" size="24px" />
<mt-icon name="regular-shopping-cart" size="16" />
```

The prefix `solid-` or `regular-` in the name overrides the `mode` prop.

### Usage as CSS class / font

The icon kit ships a CSS file:

```css
/* Include */
@import '@shopware-ag/meteor-icon-kit/icons/meteor-icon-kit.scss';
/* or */
@import '@shopware-ag/meteor-icon-kit/icons/meteor-icon-kit-aa7f6c2f67a2943b68c63f61fb088f50.css';
```

### Frequently used icons (selection)

| Name | Description |
|---|---|
| `solid-home` / `regular-home` | Home page |
| `solid-save` / `regular-save` | Save |
| `solid-search` / `regular-search` | Search |
| `solid-filter-s` | Filter |
| `solid-plus-s` | Add |
| `solid-trash` | Delete |
| `solid-pencil-s` | Edit |
| `solid-times` | Close |
| `solid-check` | Confirm |
| `solid-info-circle` | Info |
| `solid-exclamation-triangle` | Warning |
| `solid-exclamation-circle` | Error |
| `solid-chevron-right-xs` | Arrow right |
| `solid-chevron-down-xs` | Arrow down |
| `solid-ellipsis-h-s` | More menu (3 dots) |
| `solid-eye` | Visible |
| `solid-eye-slash` | Hidden |
| `solid-download` | Download |
| `solid-upload` | Upload |
| `solid-shopping-cart` | Shopping cart |
| `solid-tag` | Tag/label |
| `solid-user` | User |
| `solid-users` | User group |
| `solid-cog` | Settings |
| `regular-analytics` | Statistics |
| `solid-bell` | Notification |
| `regular-calendar` | Calendar |
| `solid-image` | Image |
| `solid-list` | List |
| `regular-table` | Table |

### Meta file

The complete icon metadata file is located at:
`icons/meta.json` — contains for every icon: `name`, `basename`, `mode`, `size`, `tags`, `sizes`, `modes`, `related`.
