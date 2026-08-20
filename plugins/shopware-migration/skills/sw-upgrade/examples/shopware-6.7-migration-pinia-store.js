// Pinia store registration (Shopware 6.7)
// src/Resources/app/administration/src/store/my-plugin.store.js
//
// Replaces Vuex module: Shopware.State.registerModule('myPlugin', { ... })
// Access via: Shopware.Store.get('myPlugin')

const myPluginStore = Shopware.Store.register({
    id: 'myPlugin',

    state: () => ({
        items: [],
        loading: false,
        currentItem: null,
    }),

    actions: {
        async fetchItems() {
            this.loading = true;
            try {
                const response = await Shopware.Service('repositoryFactory')
                    .create('my_plugin_item')
                    .search(new Shopware.Data.Criteria(), Shopware.Context.api);
                this.items = response;
            } finally {
                this.loading = false;
            }
        },

        async deleteItem(itemId) {
            await Shopware.Service('repositoryFactory')
                .create('my_plugin_item')
                .delete(itemId, Shopware.Context.api);
            this.items = this.items.filter(i => i.id !== itemId);
        },

        setCurrentItem(item) {
            this.currentItem = item;
        },
    },

    getters: {
        totalItems(state) {
            return state.items.length;
        },

        activeItems(state) {
            return state.items.filter(i => i.active);
        },
    },
});

export default myPluginStore;
