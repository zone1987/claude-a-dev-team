# Administration (Admin-Panel)

## Übersicht

Das Plugin erweitert das Shopware-Admin-Panel um eine OCTO-Produktzuweisung in der Produktdetailansicht.

---

## Registrierung

**Datei:** `src/Resources/app/administration/src/main.js`

```javascript
import './core/service/api';        // 5 API-Services
import './module/sw-product';       // Komponenten + Overrides
```

**Datei:** `src/module/sw-product/index.js`

```javascript
Shopware.Component.register('sw-product-api-product-form', ...);
Shopware.Component.override('sw-product-detail', ...);
Shopware.Component.override('sw-product-detail-base', ...);
```

---

## API-Services

**Datei:** `src/core/service/api/index.js`

5 Services registriert auf `Shopware.Service()`:

| Service | Klasse | Route-Prefix | Methoden |
|---------|--------|-------------|----------|
| `octoProductApiService` | OctoProductApiService | `/octo/` | getProducts(), getProduct(uuid, identifier) |
| `propertyApiService` | PropertyApiService | `/property-group/` | createPropertyGroup(apiProduct) |
| `variantApiService` | VariantApiService | `/product-variants/` | createProductVariants(apiProduct, propertyGroup, product) |
| `productMediaApiService` | ProductMediaApiService | `/product-media/` | assignProductMedia(apiProduct, product) |
| `productPriceApiService` | ProductPriceApiService | `/product-price/` | updateProductPrices(apiProduct, productId, identifier) |

Alle Services erweitern `Shopware.Classes.ApiService` und nutzen `httpClient` + `loginService`.

---

## sw-product-detail Override

**Datei:** `src/module/sw-product/page/sw-product-detail/index.js`

### Computed: getModeSettingGeneralTab
Fügt `api_product` Tab zu den Mode-Settings hinzu.

### Computed: productCriteria
Erweitert Product-Criteria um `ffOctoProduct` Association.

### Lifecycle
- `createdComponent()` — Registriert `reload-product-detail` Event auf EventBus
- `beforeDestroy()` — Deregistriert Event-Listener

---

## sw-product-detail-base Override

**Datei:** `src/module/sw-product/view/sw-product-detail-base/`

### Template

```twig
{% block sw_product_detail_base_basic_info_card %}
    {{ $super }}

    {% if showProductCard('api_product') and !product.parentId %}
        <sw-product-api-product-form
            :show-settings-api-product="showModeSetting"
            :allow-edit="acl.can('product.editor')"
            @reload-product="onReloadProduct()" />
    {% endif %}
{% endblock %}
```

Zeigt die OCTO-Produktzuweisung nur für **Hauptprodukte** (nicht für Varianten).

---

## sw-product-api-product-form Komponente

**Datei:** `src/module/sw-product/component/sw-product-api-product-form/`

### Injected Services

```javascript
inject: [
    'octoProductApiService',
    'propertyApiService',
    'variantApiService',
    'productMediaApiService',
    'productPriceApiService'
]
```

### Props

```javascript
props: {
    allowEdit: { type: Boolean, required: true },
    showSettingsApiProduct: { type: Boolean, required: true }
}
```

### Data

```javascript
data() {
    return {
        octoProduct: null,              // Aktuell zugewiesenes OctoProduct
        apiProducts: [],                // Alle verfügbaren API-Produkte
        apiSuppliers: [],               // Supplier-Liste (aus apiProducts extrahiert)
        selectedApiProduct: null,       // Gewähltes Produkt
        selectedApiSuppliers: [],       // Filter: Gewählte Supplier
        isApiProductLoading: false,     // Loading-State
    };
}
```

### Computed

```javascript
filteredApiProducts   // Nach selectedApiSuppliers gefiltert
isApplyButtonDisabled // true wenn kein Produkt gewählt
octoProductRepository // Shopware Repository für ff_octo_product
productRepository     // Shopware Repository für product
```

### Haupt-Workflow: applyApiProductSettings()

```javascript
async applyApiProductSettings(selectedApiProductId) {
    this.isApiProductLoading = true;

    // 1. OctoProduct-Entity erstellen/aktualisieren
    await this.preSave(selectedApiProductId);

    // 2. Shopware-Produkt-Felder setzen
    this.setName();           // product.name = apiProduct.title
    this.setDescription();    // product.description = apiProduct.description
    this.setInactive();       // product.active = false
    this.setPrice();          // product.price = [{gross: 0, net: 0, linked: true}]
    this.setStock();          // product.stock = 9999
    this.setProductNumber();  // product.productNumber = apiProduct.reference

    // 3. Produkt speichern
    await this.productRepository.save(this.product, Shopware.Context.api);

    // 4. Parallel ausführen
    await Promise.all([
        this.createProductMedia(),    // Bilder importieren
        this.createProductVariants()  // Varianten erstellen
    ]);

    // 5. Preise aktualisieren
    await this.updatePrices();

    // 6. Seite neu laden
    this.reloadProduct();
}
```

### preSave() — OctoProduct erstellen

```javascript
async preSave(selectedApiProductId) {
    const selected = this.apiProducts.find(p => p.id === selectedApiProductId);

    // OctoProduct-Entity erstellen
    const octoProduct = this.octoProductRepository.create(Shopware.Context.api);
    octoProduct.id = selected.id;          // Deterministische ID
    octoProduct.uuid = selected.product.id; // API Product UUID
    octoProduct.identifier = selected.identifier;
    octoProduct.product = selected.product;

    await this.octoProductRepository.save(octoProduct, Shopware.Context.api);

    // Shopware-Produkt verknüpfen
    this.product.ffOctoProductId = selected.id;
}
```

### createProductVariants()

```javascript
async createProductVariants() {
    // 1. Property Group erstellen
    const { data: { propertyGroup } } = await this.propertyApiService.createPropertyGroup(
        this.octoProduct.product
    );

    // 2. Varianten erstellen
    await this.variantApiService.createProductVariants(
        this.octoProduct.product,
        propertyGroup,
        { id: this.product.id, taxId: this.product.taxId }
    );
}
```

### Template

```html
<!-- Supplier-Filter (Multi-Select) -->
<sw-multi-select v-model="selectedApiSuppliers" :options="apiSuppliers" />

<!-- Produkt-Auswahl (Single-Select mit Vererbung) -->
<sw-inherit-wrapper v-model="product.ffOctoProductId">
    <sw-single-select
        :options="filteredApiProducts"
        :disabled="!allowEdit || isLoading || octoProduct"
        @change="selectedApiProduct = $event" />
</sw-inherit-wrapper>

<!-- Zuweisen-Button -->
<mt-button
    variant="primary"
    :disabled="isApplyButtonDisabled"
    @click="applyApiProductSettings(selectedApiProduct)">
    {{ $tc('sw-product.apiProductForm.applyButton') }}
</mt-button>
```

### Skeleton-Loader

Während `isApiProductLoading` werden Skeleton-Loader angezeigt (UX-Pattern).

---

## Admin-Snippets

### Deutsch (de-DE.json)

```json
{
    "sw-product": {
        "detailBase": {
            "cardTitleApiProduct": "Api-Produkt"
        },
        "apiProductForm": {
            "title": "Api-Produkt",
            "supplierLabel": "Anbieter",
            "productSelectLabel": "Produkt",
            "applyButton": "Produkt zuweisen",
            "success": "Produkt erfolgreich zugewiesen",
            "error": "Fehler beim Zuweisen",
            "supplier": {
                "gocity": "Go-City",
                "goldentours": "Goldentours",
                "demo": "Demo"
            }
        }
    }
}
```

### Englisch

Aktuell nur leerer Stub.

---

## Styling

**Datei:** `sw-product-api-product-form.scss`

```scss
@import '~scss/variables';

.product-api-product-form-supplier {
    // Supplier-Badge Styling mit Farben aus Client-Konstanten
}
```
