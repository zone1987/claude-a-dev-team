# sw-pagination

> Shopware Administration component.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| total | `any` | — | yes |  |
| limit | `any` | — | yes |  |
| page | `any` | — | yes |  |
| totalVisible | `any` | `7` | no |  |
| steps | `any` | — | no |  |
| autoHide | `any` | `true` | no |  |

## Events / Emits

| Event | Payload | Description |
|-------|---------|-------------|
| page-change | — | |

## Methods

| Method | Description |
|--------|-------------|
| `range` | |
| `pageChange` | |
| `onPageSizeChange` | |
| `firstPage` | |
| `prevPage` | |
| `nextPage` | |
| `lastPage` | |
| `changePageByPageNumber` | |
| `refresh` | |

## Computed Properties

| Name | Description |
|------|-------------|
| `maxPage` | |
| `displayedPages` | |
| `shouldBeVisible` | |
| `possibleSteps` | |
| `possibleStepsOptions` | |

## Examples

### Example 1
Source: `sw-settings-logging/page/sw-settings-logging-list/sw-settings-logging-list.html.twig`
```twig
        <sw-pagination
            :page="page"
            :limit="limit"
            :total="total"
            :total-visible="7"
            @page-change="onPageChange"
        />
        {% endblock %}
    </template>

    <template
        #actions="{ item }"
    >
        {% block sw_settings_logging_list_content_listing_actions %}
        <sw-context-menu-item @click="showInfoModal(item)">
```

### Example 2
Source: `sw-settings-search/component/sw-settings-search-excluded-search-terms/sw-settings-search-excluded-search-terms.html.twig`
```twig
                        <sw-pagination
                            :page="page"
                            :limit="limit"
                            :total="total"
                            :total-visible="7"
                            @page-change="onPagePagination"
                        />
                        {% endblock %}
                    </template>
                </sw-data-grid>
                {% block sw_search_excliuded_terms_no_results %}
                <div v-if="items.length === 0">
                    <p class="sw-settings-search__no-data-results">
                        {{ $tc('sw-settings-search.generalTab.labelExcludedSearchTermsNoResults') }}
                    </p>
```

### Example 3
Source: `sw-settings-search/component/sw-settings-search-searchable-content-general/sw-settings-search-searchable-content-general.html.twig`
```twig
            <sw-pagination
                :page="page"
                :limit="limit"
                :total="total"
                auto-hide
            />
        </template>
        {% endblock %}
    </sw-entity-listing>
    {% endblock %}
</div>
{% endblock %}

```

### Example 4
Source: `sw-extension/page/sw-extension-my-extensions-listing/sw-extension-my-extensions-listing.html.twig`
```twig
                    <sw-pagination
                        :total="total"
                        :limit="limit"
                        :page="page"
                        @page-change="changePage"
                    />
                </template>
            </div>
        </template>
    </div>
</div>

```

### Example 5
Source: `sw-settings-product-feature-sets/component/sw-settings-product-feature-sets-modal/sw-settings-product-feature-sets-modal.html.twig`
```twig
            <sw-pagination
                v-if="customFieldTotal > customFieldCriteria.limit"
                :total="customFieldTotal"
                :limit="customFieldCriteria.limit"
                :page="customFieldCriteria.page"
                :auto-hide="false"
                @page-change="paginateCustomFieldGrid"
            />
        </template>
        {% endblock %}

    </sw-data-grid>

</template>
{% endblock %}
```
