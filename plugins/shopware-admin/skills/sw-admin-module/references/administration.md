# Administration (Admin Panel)

## Overview

The Administration is a Vue.js-based SPA. Plugins extend it by registering custom modules, components, and routes.

## Directory Structure

```
src/Resources/app/administration/
├── src/
│   ├── main.js                        # Entry point
│   ├── module/
│   │   └── ff-content-plus/
│   │       ├── index.js               # Module registration
│   │       ├── page/
│   │       │   ├── ff-content-plus-list/
│   │       │   │   ├── index.js
│   │       │   │   └── ff-content-plus-list.html.twig
│   │       │   └── ff-content-plus-detail/
│   │       │       ├── index.js
│   │       │       └── ff-content-plus-detail.html.twig
│   │       └── snippet/
│   │           ├── de-DE.json
│   │           └── en-GB.json
│   └── component/
│       └── ff-content-plus-badge/
│           ├── index.js
│           └── ff-content-plus-badge.html.twig
└── build/
```

## Module Registration (main.js)

```javascript
// src/Resources/app/administration/src/main.js
import './module/ff-content-plus';
```

## Module Definition (index.js)

```javascript
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
```

## List Page Component

```javascript
// src/module/ff-content-plus/page/ff-content-plus-list/index.js
const { Component, Mixin } = Shopware;
const { Criteria } = Shopware.Data;

Component.register('ff-content-plus-list', {
    template,

    inject: ['repositoryFactory'],

    mixins: [
        Mixin.getByName('listing'),
    ],

    data() {
        return {
            items: null,
            isLoading: false,
        };
    },

    computed: {
        repository() {
            return this.repositoryFactory.create('ff_content_plus_item');
        },

        columns() {
            return [
                { property: 'name', label: 'Name', sortable: true },
                { property: 'active', label: 'Active', sortable: true },
            ];
        },
    },

    methods: {
        async getList() {
            this.isLoading = true;
            const criteria = new Criteria(this.page, this.limit);
            criteria.setTerm(this.term);
            criteria.addSorting(Criteria.sort('createdAt', 'DESC'));

            const result = await this.repository.search(criteria);
            this.items = result;
            this.total = result.total;
            this.isLoading = false;
        },
    },
});
```

## Admin Snippets

```json
// snippet/en-GB.json
{
    "ff-content-plus": {
        "general": {
            "mainMenuItemGeneral": "Content Plus",
            "description": "Manage Content Plus items"
        },
        "list": {
            "title": "Items",
            "columnName": "Name",
            "columnActive": "Active"
        },
        "detail": {
            "title": "Item Detail"
        }
    }
}
```

## ACL (Access Control)

Register custom privileges:

```php
// In the plugin class
public function enrichPrivileges(): array
{
    return [
        'ff_content_plus.viewer' => [
            'ff_content_plus_item:read',
        ],
        'ff_content_plus.editor' => [
            'ff_content_plus_item:read',
            'ff_content_plus_item:write',
        ],
        'ff_content_plus.creator' => [
            'ff_content_plus_item:read',
            'ff_content_plus_item:write',
            'ff_content_plus_item:create',
            'ff_content_plus_item:delete',
        ],
    ];
}
```

## Component Override

Override existing Administration components:

```javascript
Component.override('sw-product-detail-base', {
    template,

    computed: {
        // Add computed properties
    },

    methods: {
        // Override or add methods
    },
});
```

## Building Assets

```bash
# With Shopware CLI
ddev exec shopware-cli project admin-build --only-extensions FfContentPlus
ddev exec shopware-cli project admin-watch --only-extensions FfContentPlus

# Without Shopware CLI
ddev exec bin/build-administration.sh
ddev exec bin/watch-administration.sh
```
