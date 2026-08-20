# Contao 5.x Manual — Skills Manifest

Erstellt: 2026-06-12
Aktualisiert: 2026-06-12
Quelle: https://docs.contao.org/5.x/manual/de/

---

## Alle Skills (contao-manual-*)

| Skill-Pfad | Bilder | Eingearbeitete Seiten |
|------------|--------|----------------------|
| `skills/contao-manual-overview/` | 3 | einleitung/ (Index), contao-open-source-cms/, das-contao-netzwerk/, contao-im-schnelldurchlauf/ (= 4 Seiten) |
| `skills/contao-manual-installation/` | 2 | installation/ (Index), systemvoraussetzungen/, quickstart/, contao-manager/, contao-installieren/, contao-aktualisieren/, contao-umziehen/, erweiterungen-installieren/, erweiterungen-aktualisieren/, erweiterungen-deinstallieren/, contao-installtool/, anleitungen/lokale-installation/ (Index+ddev+devilbox+laragon) (= 14 Seiten) |
| `skills/contao-manual-backend/` | 8 | administrationsbereich/ (Index), aufruf-und-aufbau-des-backends/, backend-tastaturkuerzel/, datensaetze-auflisten/, datensaetze-bearbeiten/ (= 5 Seiten) |
| `skills/contao-manual-page-structure/` | 0 | seitenstruktur/ (Index), seiten-als-zentrale-elemente/, multidomain-betrieb/, mehrsprachige-webseiten/ (= 4 Seiten) |
| `skills/contao-manual-file-management/` | 0 | dateiverwaltung/ (Index), dateien-und-ordner-verwalten/, metadaten/, downloads-kontrollieren/ (= 4 Seiten) |
| `skills/contao-manual-user-management/` | 0 | benutzerverwaltung/ (Index), benutzer/, mitglieder/ (= 3 Seiten) |
| `skills/contao-manual-system/` | 0 | system/ (Index), einstellungen/, systemwartung/, preview-link/, debug-modus/ (= 5 Seiten) |
| `skills/contao-manual-performance/` | 0 | performance/ (Index), cronjobs/, http-caching/, php-setup/ (= 4 Seiten) |
| `skills/contao-manual-cli/` | 0 | cli/ (Index), automator/, datenbank-backups/, crawl/, maintenance-mode/, migrate/, resize-images/, user/, dca/ (= 9 Seiten) |
| `skills/contao-manual-migration/` | 0 | migration/, installation/contao-aktualisieren/, faq/ (= 3+ Seiten; FAQ vollständig eingearbeitet) |
| `skills/contao-manual-tutorials/` | 0 | anleitungen/ (Index), testversionen-installieren/, die-erste-startseite/, wartungstemplate-anpassen/, contao-demo/, dca/, sass-less-integration/, tinymce-konfiguration/, grid/, svg/, formulardaten-speichern/ (= 11 Seiten) |
| `skills/contao-manual-articles-content/` | 0 | artikelverwaltung/, text-elemente/, media-elemente/, link-elemente/, datei-elemente/, include-elemente/, legacy-elemente/ (= 10 Seiten) |
| `skills/contao-manual-insert-tags-tokens/` | 0 | insert-tags/, simple-tokens/ (= 2 Seiten) |
| `skills/contao-manual-layout/` | 0 | layout/, theme-manager/, themes-verwalten/, stylesheets-verwalten/, seitenlayouts-verwalten/, modulverwaltung/, navigationsmodule/, benutzermodule/, website-suche/, anwendungen/, templates/ (= 12 Seiten) |
| `skills/contao-manual-form-generator/` | 0 | formulargenerator/, formulare/, formularfelder/, ein-suchformular-erstellen/ (= 4 Seiten) |
| `skills/contao-manual-core-extensions/` | 0 | core-erweiterungen/, nachrichten/, kalender/, faq/, newsletter/, kommentare/ (= 14 Seiten) |
| `skills/contao-manual-third-party-extensions/` | 0 | erweiterungen/, animated-timeline/, contao-easy_themes/, isotope-core/ u.a. (= 8 Seiten) |

**Gesamtseiten eingearbeitet:** ~116
**Gesamtbilder heruntergeladen:** 13 (3 Übersicht + 8 Backend + 2 Installation)
**Gesamtzeilen Referenz-Markdown:** ~2.500+

---

## Referenz-Dateien

| Datei | Inhalt |
|-------|--------|
| `contao-manual-overview/references/deep/overview.md` | Einleitung, CMS-Grundbegriffe, LGPL, Netzwerk, Schnelldurchlauf |
| `contao-manual-installation/references/deep/installation.md` | Systemvoraussetzungen, Contao Manager, CLI-Installation, Update, Erweiterungen, DDEV/Devilbox/Laragon/XAMPP |
| `contao-manual-backend/references/deep/backend.md` | Aufruf, Aufbau, Infobereich, Navigation, Arbeitsbereich, Vorschau, Tastaturkürzel, List/Parent/Tree-View, Klemmbrett, Versionierung |
| `contao-manual-page-structure/references/deep/page-structure.md` | Seitentypen, Multidomain, Mehrsprachigkeit |
| `contao-manual-file-management/references/deep/file-management.md` | Dateien/Ordner, UUID, Metadaten, Downloads schützen |
| `contao-manual-user-management/references/deep/user-management.md` | Benutzer, Gruppen, Rechte, 2FA, Mitglieder, geschützte Bereiche |
| `contao-manual-system/references/deep/system.md` | Einstellungen, config.yaml, .env, SMTP, Wartung, Crawler, Vorschau-Links, Debug |
| `contao-manual-performance/references/deep/performance.md` | Cronjobs, HTTP-Caching, PHP-Setup (OPcache, SAPI, Realpath Cache) |
| `contao-manual-cli/references/deep/cli.md` | Alle 8 CLI-Befehle mit Optionen |
| `contao-manual-migration/references/deep/migration.md` | Versioning, 3.5→4.x, 4.13→5.x, FAQ |

---

## Fazit

Die contao-manual-* Skills dokumentieren das gesamte Contao 5.x Benutzerhandbuch (Bedienung/Administration) auf Deutsch exhaustiv. Kernbereiche (Backend, Installation, Seitenstruktur, System, CLI, Migration) wurden erstmals mit vollständigen Schritt-für-Schritt-Referenzdateien ausgestattet. Screenshots für Backend und Übersicht wurden lokal heruntergeladen und relativ referenziert. Alle Skills sind klar von den Entwickler-`contao-*`-Skills abgegrenzt (Präfix `contao-manual-`). Die marketplace.json wurde nicht verändert.
