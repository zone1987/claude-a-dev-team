# Shopware 6 Storefront SCSS — Vollständige Datei-Karte

Basis: `src/Storefront/Resources/app/storefront/src/scss/`  
Trunk-Quelle: Shopware 6 Core (Stand 2026).

---

## Einstiegspunkte (via theme.json)

| Datei | Zweck |
|---|---|
| `base.scss` | Haupt-Einstiegspunkt: Lädt Variablen, Vendor (Bootstrap/TinySlider/Flatpickr), Base, alle Component/Layout/Page-Partials |
| `variables.scss` | Variablen-Aggregator: lädt Bootstrap-Overrides, Skin-Variablen, Bootstrap-Core, Custom-Vars, CSS-Properties |
| `skin/shopware/_base.scss` | Shopware-Default-Skin-Einstieg: lädt Inter-Font, Base, Typography, alle Skin-Component/Layout/Page-Partials |

---

## abstract/ — Funktionen, Mixins, Variablen (Framework-Ebene)

| Datei | Zweck |
|---|---|
| `abstract/functions/feature.scss` | SCSS-Funktion `feature($flag)` — prüft Feature-Flags aus `$sw-features`-Map (injiziert von ThemeCompiler/webpack) |
| `abstract/mixins/truncate-multiline.scss` | Mixin `truncate-multiline($line-height, $line-count, $bg-color)` — mehrzeiliges Text-Truncate mit `-webkit-line-clamp` |
| `abstract/variables/_bootstrap.scss` | Bootstrap-Overrides **ohne** Skin/Theme (nur strukturelle Änderungen): Container, Modal-Transition, Z-Index-Levels, `$enable-important-utilities: false` |
| `abstract/variables/_custom.scss` | Eigene Non-Bootstrap-Variablen: Z-Index-Werte, Icon-Basis, Spacer-XS…XL, Asset-Pfad-Vars (`$sw-asset-theme-url`, `$theme-id`) |
| `abstract/variables/_css-properties.scss` | Exponiert SCSS-Variablen als CSS Custom Properties in `:root` (vollständige Liste → `css-custom-properties.md`) |

---

## base/ — Globale Basis-Styles

| Datei | Zweck |
|---|---|
| `base/_base.scss` | HTML-Basis: `no-scroll`-Klasse, `sw-text-editor-table`-Styles (Tabellen aus Rich-Text-Editor), `col-selector` ausblenden |
| `base/_reboot.scss` | Storefront-Reboot: kleines Zusatz-Reset über Bootstrap-Reboot hinaus |

---

## component/ — UI-Komponenten (strukturell, skin-neutral)

| Datei | Zweck |
|---|---|
| `component/_address-manager.scss` | Adressverwaltungs-Modal (Account-Bereich) |
| `component/_alert.scss` | Bootstrap-Alert-Basisstyles |
| `component/_ar-overlay.scss` | AR (Augmented Reality) Overlay-Layer |
| `component/_ar-qr-modal.scss` | AR QR-Code-Modal |
| `component/_ar-splash-screen.scss` | AR Splash/Loading-Screen |
| `component/_backdrop.scss` | Element-Backdrop (halbtransparente Überlagerung, z.B. beim Laden) |
| `component/_base-slider.scss` | Basis-Slider-Styles (TinySlider-Basis) |
| `component/_basic-captcha.scss` | Basic-Captcha-Formfeld |
| `component/_card.scss` | Bootstrap-Card-Erweiterungen |
| `component/_category-navigation.scss` | Kategorie-Navigation (Desktop-Dropdown) |
| `component/_cms-block.scss` | CMS-Block-Layout (Shopping-Erlebnisse) |
| `component/_cms-element.scss` | CMS-Element-Basisstyles (Text, Bild, Video, etc.) |
| `component/_cms-form-confirmation.scss` | Bestätigungsseite CMS-Formular |
| `component/_cms-sections.scss` | CMS-Sektionen-Layout (Full-Width, Sidebar, etc.) |
| `component/_delivery-status.scss` | Lieferstatus-Anzeige |
| `component/_filter-boolean.scss` | Filter-Panel: Boolean/Ja-Nein-Filter |
| `component/_filter-multi-select.scss` | Filter-Panel: Multi-Select |
| `component/_filter-panel.scss` | Filter-Panel Wrapper/Container |
| `component/_filter-property-select.scss` | Filter-Panel: Eigenschafts-Filter |
| `component/_filter-range.scss` | Filter-Panel: Bereichs-Filter (Preis) |
| `component/_filter-rating-select.scss` | Filter-Panel: Bewertungs-Filter |
| `component/_flags.scss` | Länderflaggen-Icons |
| `component/_forms.scss` | Formular-Basisstyles (Input, Select, Checkbox) |
| `component/_gallery-slider.scss` | Produkt-Galerie-Slider (Detailseite) |
| `component/_icon.scss` | Icon-Basisstyles (SVG-Icons) |
| `component/_image-slider.scss` | Allgemeiner Bild-Slider |
| `component/_line-item.scss` | Warenkorb-/Bestellpositionen |
| `component/_loader.scss` | Lade-Spinner/Overlay |
| `component/_magnifier.scss` | Produktbild-Lupe/Zoom-Hover |
| `component/_modal.scss` | Bootstrap-Modal-Basisstyles |
| `component/_notification-dot.scss` | Notification-Badge (Warenkorb-Zähler) |
| `component/_offcanvas.scss` | Bootstrap-Offcanvas-Basisstyles |
| `component/_pagination.scss` | Paginierung |
| `component/_payment-method.scss` | Zahlungsart-Auswahl |
| `component/_product-box.scss` | Produkt-Kachel (Listing) |
| `component/_product-feature.scss` | Produkt-Eigenschaften-Anzeige |
| `component/_product-slider.scss` | Produkt-Slider (CMS-Element) |
| `component/_product-wishlist.scss` | Wunschliste-Button/Icon |
| `component/_quantity-selector.scss` | Mengenauswahl-Stepper |
| `component/_quickview-modal.scss` | Quickview-Modal (Schnellansicht) |
| `component/_shipping-method.scss` | Versandart-Auswahl |
| `component/_sorting.scss` | Listing-Sortierung (Dropdown) |
| `component/_visibility.scss` | Sichtbarkeits-Utility-Klassen |
| `component/_zoom-modal.scss` | Produkt-Zoom-Modal |

---

## layout/ — Seitenlayout-Bereiche

| Datei | Zweck |
|---|---|
| `layout/_account-menu.scss` | Account-Dropdown-Menü (Header) |
| `layout/_container.scss` | Container-Overrides (max-width-Anpassungen) |
| `layout/_cookie-configuration.scss` | Cookie-Einstellungen-Modal |
| `layout/_cookie-permission.scss` | Cookie-Banner |
| `layout/_footer.scss` | Footer-Struktur |
| `layout/_header.scss` | Header-Struktur (Logo, Search, Actions) |
| `layout/_header-minimal.scss` | Minimaler Header (z.B. Checkout) |
| `layout/_navigation-offcanvas.scss` | Mobile-Navigation-Offcanvas (Struktur) |
| `layout/_offcanvas-cart.scss` | Warenkorb-Offcanvas (Struktur) |
| `layout/_recaptcha.scss` | reCAPTCHA-Einbindung |
| `layout/_scroll-up.scss` | Scroll-to-Top-Button |
| `layout/_search-suggest.scss` | Suchvorschläge-Dropdown |

---

## page/ — Seitenspezifische Styles

### page/account/
| Datei | Zweck |
|---|---|
| `page/account/_account.scss` | Account-Seiten-Wrapper |
| `page/account/_address.scss` | Adressverwaltung |
| `page/account/_edit-order.scss` | Bestellung nachbearbeiten |
| `page/account/_order.scss` | Bestellübersicht |
| `page/account/_order-detail.scss` | Bestelldetail |
| `page/account/_overview.scss` | Account-Übersicht |
| `page/account/_register.scss` | Registrierungsseite |

### page/checkout/
| Datei | Zweck |
|---|---|
| `page/checkout/_aside.scss` | Checkout-Sidebar (Zusammenfassung) |
| `page/checkout/_cart.scss` | Warenkorb-Seite |
| `page/checkout/_checkout.scss` | Checkout-Wrapper |
| `page/checkout/_confirm.scss` | Checkout-Bestätigungsschritt |
| `page/checkout/_finish.scss` | Checkout-Abschlussseite |
| `page/checkout/_register.scss` | Checkout-Gastbestellung/Registrierung |

### page/product-detail/
| Datei | Zweck |
|---|---|
| `page/product-detail/_configurator.scss` | Varianten-Konfigurator (Swatches, Dropdowns) |
| `page/product-detail/_product-detail.scss` | Produktdetailseite Wrapper |
| `page/product-detail/_review.scss` | Produktbewertungen |
| `page/product-detail/_tabs.scss` | Tab-Navigation (Beschreibung, Eigenschaften) |

### page/search/
| Datei | Zweck |
|---|---|
| `page/search/_search.scss` | Suchergebnisseite |

### page/wishlist/
| Datei | Zweck |
|---|---|
| `page/wishlist/_wishlist.scss` | Wunschlisten-Seite |

---

## vendor/ — Externe Abhängigkeiten

| Datei | Zweck |
|---|---|
| `vendor/_bootstrap.scss` | Bootstrap 5.x vollständiger Import (`~vendor/bootstrap/scss/bootstrap`) |
| `vendor/_datepicker.scss` | Flatpickr-Datepicker-Styles |
| `vendor/_tiny-slider.scss` | TinySlider-Slider-Styles |

---

## skin/shopware/ — Shopware Default Visual Skin

Überschreibt/ergänzt die strukturellen Styles mit visuellen Styles.
Alle Dateien liegen unter `skin/shopware/`.

### skin/shopware/abstract/

| Datei | Zweck |
|---|---|
| `abstract/_variables.scss` | Import-Aggregator: lädt `_theme.scss`, `_bootstrap.scss`, `_custom.scss` |
| `abstract/variables/_theme.scss` | **Theme-Variablen** (alle `$sw-*`-Variablen — Farben, Fonts, Logos) |
| `abstract/variables/_bootstrap.scss` | Bootstrap-Overrides MIT Theme-Farben (Colors, Typography, Buttons, Forms, etc.) |
| `abstract/variables/_custom.scss` | Custom Non-Bootstrap-Vars mit Theme-Farb-Referenzen (`$buy-btn-bg`, `$price-color`, etc.) |
| `abstract/mixins/` | (leer, `.gitkeep`) |

### skin/shopware/base/

| Datei | Zweck |
|---|---|
| `base/_base.scss` | `body` global: font-smoothing, min-height 100vh, flex-column |
| `base/_typography.scss` | Heading-Zeilenhöhen, Blockquote-Styling, Listen-Margin |

### skin/shopware/component/

| Datei | Zweck |
|---|---|
| `component/_alert.scss` | Alert-Farben via `$theme-colors`-Loop, Icon-Spacing |
| `component/_badge.scss` | Badge-Höhe (20px/28px), Box-Sizing |
| `component/_breadcrumb.scss` | Breadcrumb-Links (Farbe, Hover → Primary), Active-Gewicht |
| `component/_button.scss` | `.btn-buy` (Bootstrap-Variant mit `$buy-btn-bg`), `.btn-link-inline`, Focus-Box-Shadow-Loop |
| `component/_card.scss` | Card-Background via `$body-bg` |
| `component/_cms-block.scss` | CMS-Block visuelle Anpassungen |
| `component/_cms-element.scss` | CMS-Element visuelle Anpassungen |
| `component/_custom-select.scss` | Custom-Select Styling |
| `component/_form.scss` | Formular: `.form-group` Abstand, Validierungs-Box-Shadow, `.form-required-label` (danger-Farbe) |
| `component/_modal.scss` | Modal-Box-Shadow, Titel-Zeilenhöhe, Back-Button-Icon |
| `component/_pagination.scss` | Page-Link Höhe/Mindestbreite |
| `component/_product-box.scss` | `.product-box` Border, `.product-name` Gewicht, `.product-price` Farbe |
| `component/_quickview-modal.scss` | Quickview-Modal visuelles Styling |
| `component/_tab-menu.scss` | `.card-tabs` Tab-Navigation: Farben, Border-Bottom-Indikator |

### skin/shopware/layout/

| Datei | Zweck |
|---|---|
| `layout/_header.scss` | Header: Search-Input/Button-Styles, Actions-Button-Hover, Cart-Total-Farbe |
| `layout/_footer.scss` | Footer: Border-Top, Column-Headlines (Primary), Links, Bottom-Background |
| `layout/_main-navigation.scss` | Desktop-Navigation: Active-Border-Indikator (Primary), Dropdown-Overlay |
| `layout/_navigation-flyout.scss` | Navigation-Flyout: Links (Farbe, Hover-Einrückung, Bold Level-0) |
| `layout/_navigation-offcanvas.scss` | Mobile-Nav-Offcanvas: Listenelement-Border, Active-Link-Farbe (Primary) |
| `layout/_offcanvas-cart.scss` | Warenkorb-Offcanvas: Header-Count (`$text-muted`), Steuer-Hinweis |
| `layout/_top-bar.scss` | Top-Bar-Buttons: Farbe, Padding, Hover (Primary), Dropdown-Active |

### skin/shopware/page/account/

| Datei | Zweck |
|---|---|
| `page/account/_aside.scss` | Account-Sidebar: Header bold, List-Items ohne Border, Active = Primary |
| `page/account/_address.scss` | Adress-Karten-Styles |
| `page/account/_order.scss` | Bestellübersicht-Tabelle |
| `page/account/_order-detail.scss` | Bestelldetail-Ansicht |
| `page/account/_profile.scss` | Profil-Seiten-Styles |
| `page/account/_register.scss` | Registrierungs-Formular (Skin) |

### skin/shopware/page/checkout/

| Datei | Zweck |
|---|---|
| `page/checkout/_aside.scss` | Checkout-Sidebar-Zusammenfassung: `$light`-Hintergrund, Spacing |
| `page/checkout/_cart.scss` | Warenkorb-Tabelle: Mobile-Border entfernen |

### skin/shopware/page/contact/

| Datei | Zweck |
|---|---|
| `page/contact/_contact.scss` | Kontaktformular-Seite |

### skin/shopware/page/newsletter/

| Datei | Zweck |
|---|---|
| `page/newsletter/_newsletter.scss` | Newsletter-Anmelde-Seite |

### skin/shopware/page/product-detail/

| Datei | Zweck |
|---|---|
| `page/product-detail/_product-detail.scss` | Produktname (Headline-Farbe), Preise (danger bei Liste), Streichpreise, Bestellnummer |
| `page/product-detail/_tabs.scss` | Tab-Navigation: Flex-Direction Responsive, Preview-Text, Tab-Link-Styles |
| `page/product-detail/_review.scss` | Bewertungen-Bereich |
| `page/product-detail/_cross-selling.scss` | Cross-Selling-Tabs: Mobile = alle aufgeklappt, Desktop = Tab-Navigation |

### skin/shopware/vendor/

| Datei | Zweck |
|---|---|
| `vendor/_inter-fontface.scss` | Inter-Schrift @font-face-Deklarationen (Variable Font, mehrere Unicode-Ranges: Latin, Cyrillic, Greek, Vietnamese) |

---

## Admin-SCSS (Abgrenzung)

Basis: `src/Administration/Resources/app/administration/src/app/assets/scss/`

| Datei | Zweck |
|---|---|
| `all.scss` | Einstiegspunkt: lädt variables, typography, global, directives, pages |
| `variables.scss` | Alle Admin-Design-Tokens (Color-Palette, Typography, z-Index, Border-Radius) |
| `global.scss` | Globale Basis-Styles; generiert CSS Custom Properties automatisch via `@each meta.module-variables("variables")` |
| `typography.scss` | Admin-Typografie-Styles |
| `mixins.scss` | Admin-SCSS-Mixins |
| `directives/tooltip.scss` | Tooltip-Directive-Styles |
| `directives/dragdrop.scss` | Drag-and-Drop-Directive-Styles |
| `pages/error.scss` | Fehlerseiten-Styles (500, 404) |

Admin-SCSS ist **vollständig von Storefront-SCSS getrennt** — keine gemeinsamen Variablen.
