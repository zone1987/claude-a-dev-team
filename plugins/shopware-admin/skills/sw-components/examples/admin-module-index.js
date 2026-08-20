// Administration module registration
// src/Resources/app/administration/src/module/ff-content-plus/index.js

import './page/ff-content-plus-list';
import './page/ff-content-plus-detail';

import deDE from './snippet/de-DE.json';
import enGB from './snippet/en-GB.json';

Shopware.Module.register('ff-content-plus', {
    type: 'plugin',
    name: 'ff-content-plus',
    title: 'ff-content-plus.general.mainMenuItemGeneral',
    description: 'ff-content-plus.general.description',
    color: '#ff3d58',
    icon: 'default-shopping-paper-bag',

    snippets: {
        'de-DE': deDE,
        'en-GB': enGB,
    },

    routes: {
        list: {
            component: 'ff-content-plus-list',
            path: 'list',
        },
        detail: {
            component: 'ff-content-plus-detail',
            path: 'detail/:id',
            meta: {
                parentPath: 'ff.content.plus.list',
            },
        },
    },

    navigation: [
        {
            label: 'ff-content-plus.general.mainMenuItemGeneral',
            color: '#ff3d58',
            path: 'ff.content.plus.list',
            icon: 'default-shopping-paper-bag',
            parent: 'sw-content',
            position: 100,
        },
    ],
});
