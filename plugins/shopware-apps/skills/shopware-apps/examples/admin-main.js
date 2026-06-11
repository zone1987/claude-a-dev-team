/**
 * Meteor Admin SDK entry point for Shopware App
 * Install: npm install @shopware-ag/meteor-admin-sdk
 *
 * This file is loaded via base-app-url in manifest.xml.
 * It is NOT placed in Resources/administration/ (that is ignored for apps).
 */

// Signal readiness to the Shopware Administration (must fire within 5 seconds)
function sendReadyState() {
  window.parent.postMessage('sw-app-loaded', '*');
}

// --- Location Management ---

import { location } from '@shopware-ag/meteor-admin-sdk';

// Check if running inside the Shopware Administration
if (location.isIframe()) {
  sendReadyState();

  // Register different behaviors based on which location this iframe is loaded in
  if (location.is('myAppDashboard')) {
    initDashboard();
  } else if (location.is('myAppSettings')) {
    initSettings();
  }
}

// --- Notification API ---

import { notification } from '@shopware-ag/meteor-admin-sdk';

async function showNotification(title, message, variant = 'success') {
  await notification.dispatch({
    title,
    message,
    variant, // 'success' | 'info' | 'warning' | 'error'
    growl: true,
  });
}

// --- Data API ---

import { data } from '@shopware-ag/meteor-admin-sdk';

async function fetchProducts(limit = 10) {
  const result = await data.repository('product').search({
    limit,
    filter: [{ type: 'equals', field: 'active', value: true }],
    associations: {
      manufacturer: {},
    },
  });

  return result;
}

async function updateProduct(productId, changes) {
  await data.repository('product').save({
    id: productId,
    ...changes,
  });

  await showNotification('Product Updated', 'Product was saved successfully.');
}

// --- Context API ---

import { context } from '@shopware-ag/meteor-admin-sdk';

async function getCurrentLanguage() {
  const languageId = await context.getLanguage();
  return languageId;
}

async function getCurrentCurrency() {
  const currency = await context.getCurrency();
  return currency;
}

// --- UI Extension Points ---

import { ui } from '@shopware-ag/meteor-admin-sdk';

// Add a menu item
ui.menu.addMenuItem({
  label: 'My App',
  locationId: 'myAppDashboard',
  displaySearchBar: false,
  parent: 'sw-marketing',
});

// Add a settings item
ui.settings.addSettingsItem({
  label: 'My App Settings',
  locationId: 'myAppSettings',
  icon: 'default-action-settings',
  tab: 'plugins',
});

// --- Action Buttons ---

import { window as sdkWindow } from '@shopware-ag/meteor-admin-sdk';

// Open a modal from action button response
async function openDetailModal(entityId) {
  await sdkWindow.open({
    title: 'Product Details',
    size: 'medium',
    locationId: 'product-detail-' + entityId,
    buttons: [
      {
        label: 'Save',
        variant: 'primary',
        method: 'save',
      },
      {
        label: 'Cancel',
        variant: 'secondary',
        method: 'close',
      },
    ],
  });
}

// --- Example Dashboard Init ---

async function initDashboard() {
  const products = await fetchProducts(5);
  const language = await getCurrentLanguage();

  // Render dashboard (use your frontend framework of choice)
  document.getElementById('app').innerHTML =
    '<h1>Dashboard</h1>' +
    '<p>Language: ' + language + '</p>' +
    '<ul>' +
    products.data.map(function(p) { return '<li>' + p.name + '</li>'; }).join('') +
    '</ul>';
}

async function initSettings() {
  await showNotification('Settings', 'Settings panel loaded.', 'info');
}
