// Vite configuration for plugin administration (Shopware 6.7)
// src/Resources/app/administration/vite.config.js
//
// Most plugins do NOT need a custom vite.config.js — Shopware's build system
// handles plugin integration automatically. Only create this file if you need
// custom build behavior (aliases, plugins, etc.).

import { defineConfig } from 'vite';

export default defineConfig({
    build: {
        // Custom build options if needed
    },
    resolve: {
        alias: {
            // Add custom aliases if needed
            // '@my-plugin': '/src',
        },
    },
});
