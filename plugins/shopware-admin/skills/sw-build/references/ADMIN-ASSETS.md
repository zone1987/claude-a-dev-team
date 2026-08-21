# Shopware 6 — Admin assets

Static plugin assets live under `src/Resources/app/administration/src/assets/` and are bundled by the Vite
build; import them directly in JS/SCSS.

```js
import logoUrl from '../../assets/ff-logo.svg';
```

Icons via the icon component (`<mt-icon name="regular-cog"/>` or legacy `<sw-icon>`); import your own SVGs as an
asset. Media from the DAL (media entity) via `sw-media-field`/media upload components, not as a static
asset. Build details: `sw-admin-vite`.
