# Shopware 6 — Admin-Assets

Statische Plugin-Assets liegen unter `src/Resources/app/administration/src/assets/` und werden vom Vite-Build
gebündelt; Import direkt im JS/SCSS.

```js
import logoUrl from '../../assets/ff-logo.svg';
```

Icons über die Icon-Komponente (`<mt-icon name="regular-cog"/>` bzw. Legacy `<sw-icon>`); eigene SVGs als Asset
importieren. Medien aus dem DAL (Media-Entity) über `sw-media-field`/Media-Upload-Komponenten, nicht als statisches
Asset. Build-Details: `sw-admin-vite`.
