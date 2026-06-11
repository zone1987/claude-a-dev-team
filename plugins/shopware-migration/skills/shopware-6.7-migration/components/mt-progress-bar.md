# mt-progress-bar

> Progress bar indicator for showing completion status.

## Props

| Name | Type | Default | Required | Description |
|------|------|---------|----------|-------------|
| label | `string` | — | yes | |
| maxValue | `number` | — | yes | |
| error | `{ detail: string; code: number } | null` | — | no | |
| progressLabelType | `string` | — | no | |

## Examples

### Example 1
Source: `sw-settings-search/component/sw-settings-search-search-index/sw-settings-search-search-index.html.twig`
```twig
<mt-progress-bar
    :model-value="progressBarValue"
    :max-value="100"
>
    {{ $tc('sw-settings-search.generalTab.textRebuildingSearchIndex') }}
</mt-progress-bar>
```

### Example 2
Source: `sw-extension/component/sw-ratings/sw-extension-ratings-summary/sw-extension-ratings-summary.html.twig`
```twig
                    <mt-progress-bar
                        :model-value="ratingGroup.count"
                        :max-value="maxProgressValue"
                    />
                    {% endblock %}
                </template>
            </div>
            {% endblock %}
        </div>
        {% endblock %}
    </div>
    {% endblock %}
</div>
{% endblock %}

```

### Example 3
Source: `sw-settings-shopware-updates/page/sw-settings-shopware-updates-wizard/sw-settings-shopware-updates-wizard.html.twig`
```twig
        <mt-progress-bar
            :model-value="progressbarValue"
            :max-value="100"
        />
        <span class="progress-title">
            <p v-if="step === 'download'">{{ $t('sw-settings-shopware-updates.infos.progress.download') }}</p>
            <p v-if="step === 'unpack'">{{ $t('sw-settings-shopware-updates.infos.progress.unpack') }}</p>
            <p v-if="step === 'deactivate'">{{ $t('sw-settings-shopware-updates.infos.progress.deactivate') }}</p>
        </span>
    </div>
</sw-modal>

<sw-modal
    v-if="updateModalShown"
    class="sw-settings-shopware-updates-check__start-update"
```

### Example 4
Source: `sw-product/component/sw-product-clone-modal/sw-product-clone-modal.html.twig`
```twig
    <mt-progress-bar
        class="clone-variant-progress-bar"
        :max-value="cloneMaxProgress"
        :model-value="cloneProgress"
    />
    {% endblock %}

    {% block sw_product_clone_modal_progress_bar_description %}
    <div class="clone-variant-progress-bar__description">
        {{ cloneProgress }} {{ $tc('sw-product.variations.progressTypeOf') }} {{ cloneMaxProgress }} {{ $tc('sw-product.general.cloneSuffix') }}
    </div>
    {% endblock %}
</sw-modal>
{% endblock %}

```

### Example 5
Source: `sw-product/component/sw-product-variants/sw-product-modal-variant-generation/sw-product-modal-variant-generation.html.twig`
```twig
                <mt-progress-bar
                    class="generate-variant-progress-bar"
                    :model-value="actualProgress"
                    :max-value="maxProgress"
                />

                <span class="generate-variant-progress-bar__description">
                    {{ actualProgress }} {{ $tc('sw-product.variations.progressTypeOf') }} {{ maxProgress }} {{ $tc('sw-product.variations.progressTypeVariation') }} {{ progressMessage }}
                </span>
            </div>
        </transition>
    </template>
</sw-modal>
{% endblock %}

```
