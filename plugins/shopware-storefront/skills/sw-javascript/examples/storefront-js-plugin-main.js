// Storefront main.js entry point
// src/Resources/app/storefront/src/main.js

import FfContentPlusPlugin from './ff-content-plus-plugin/ff-content-plus-plugin.plugin';

const PluginManager = window.PluginManager;

PluginManager.register('FfContentPlusPlugin', FfContentPlusPlugin, '[data-ff-content-plus]');
