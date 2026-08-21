# Contao 5.x – Hook-Referenz: Index

Vollständige Referenz aller 69 dokumentierten Hooks, gruppiert nach Domäne.

## Dateien in diesem Verzeichnis

| Datei                          | Gruppe                    | Hooks                                      |
|-------------------------------|---------------------------|--------------------------------------------|
| `01-member-account.md`        | Member / Account          | activateAccount, closeAccount, createNewUser, setNewPassword, updatePersonalData |
| `02-newsletter.md`            | Newsletter                | activateRecipient, removeRecipient         |
| `03-comments.md`              | Kommentare                | addComment, isAllowedToEditComment, listComments |
| `04-forms.md`                 | Formulare                 | compileFormFields, loadFormField, prepareFormData, processFormData, storeFormData, validateFormField |
| `05-page-layout.md`           | Seite / Layout            | generatePage, generateBreadcrumb, getPageLayout, getPageStatusIcon, loadPageDetails, modifyFrontendPage, outputFrontendTemplate, replaceDynamicScriptTags |
| `06-templates.md`             | Templates                 | outputBackendTemplate, parseBackendTemplate, parseFrontendTemplate, parseTemplate, parseWidget |
| `07-content-modules.md`       | Content-Elemente / Module | compileArticle, getArticle, getArticles, getContentElement, getFrontendModule, getForm, isVisibleElement |
| `08-dca-backend.md`           | DCA / Backend             | executePostActions, executePreActions, getAttributesFromDca, getUserNavigation, getSystemMessages, loadDataContainer, reviseTable |
| `09-calendar-news.md`         | Kalender / News           | findCalendarBoundaries, getAllEvents, newsListCountItems, newsListFetchItems, parseArticles |
| `10-search.md`                | Suche                     | customizeSearch, indexPage                 |
| `11-insert-tags.md`           | Insert-Tags               | insertTagFlags, replaceInsertTags          |
| `12-theme-files.md`           | Theme / Dateien           | compareThemeFiles, exportTheme, extractThemeFiles, generateXmlFiles, getCombinedFile, postDownload, postUpload, removeOldFeeds |
| `13-system.md`                | System / Sonstiges        | addCustomRegexp, colorizeLogEntries, initializeSystem, loadLanguageFile, parseDate, removeRecipient, setCookie, sqlCompileCommands, sqlGetFromDB, sqlGetFromDca |

## Schnellreferenz: Alle Hooks alphabetisch

| Hook-Name                  | Gruppe              | Rückgabe       |
|---------------------------|---------------------|----------------|
| activateAccount           | Member              | void           |
| activateRecipient         | Newsletter          | void           |
| addComment                | Kommentare          | void           |
| addCustomRegexp           | System              | bool           |
| closeAccount              | Member              | void           |
| colorizeLogEntries        | System              | string         |
| compareThemeFiles         | Theme               | string         |
| compileArticle            | Content/Module      | void           |
| compileFormFields         | Formulare           | array          |
| createNewUser             | Member              | void           |
| customizeSearch           | Suche               | void           |
| executePostActions        | DCA/Backend         | void           |
| executePreActions         | DCA/Backend         | void           |
| exportTheme               | Theme               | void           |
| extractThemeFiles         | Theme               | void           |
| findCalendarBoundaries    | Kalender/News       | void           |
| generateBreadcrumb        | Seite/Layout        | array          |
| generatePage              | Seite/Layout        | void           |
| generateXmlFiles          | Theme               | void           |
| getAllEvents               | Kalender/News       | array          |
| getArticle                | Content/Module      | void           |
| getArticles               | Content/Module      | string\|null   |
| getAttributesFromDca      | DCA/Backend         | array          |
| getCombinedFile           | Theme               | string         |
| getContentElement         | Content/Module      | string         |
| getForm                   | Content/Module      | string         |
| getFrontendModule         | Content/Module      | string         |
| getPageLayout             | Seite/Layout        | void           |
| getPageStatusIcon         | Seite/Layout        | string         |
| getSystemMessages         | DCA/Backend         | string         |
| getUserNavigation         | DCA/Backend         | array          |
| indexPage                 | Suche               | void           |
| initializeSystem          | System              | void           |
| insertTagFlags            | Insert-Tags         | string\|false  |
| isAllowedToEditComment    | Kommentare          | bool           |
| isVisibleElement          | Content/Module      | bool           |
| listComments              | Kommentare          | string         |
| loadDataContainer         | DCA/Backend         | void           |
| loadFormField             | Formulare           | Widget         |
| loadLanguageFile          | System              | void           |
| loadPageDetails           | Seite/Layout        | void           |
| modifyFrontendPage        | Seite/Layout        | string         |
| newsListCountItems        | Kalender/News       | int\|false     |
| newsListFetchItems        | Kalender/News       | Collection\|false\|null |
| outputBackendTemplate     | Templates           | string         |
| outputFrontendTemplate    | Seite/Layout        | string         |
| parseArticles             | Kalender/News       | void           |
| parseBackendTemplate      | Templates           | string         |
| parseDate                 | System              | string         |
| parseFrontendTemplate     | Templates           | string         |
| parseTemplate             | Templates           | void           |
| parseWidget               | Templates           | string         |
| postDownload              | Theme               | void           |
| postUpload                | Theme               | void           |
| prepareFormData           | Formulare           | void           |
| processFormData           | Formulare           | void           |
| removeOldFeeds            | Theme               | array          |
| removeRecipient           | Newsletter          | void           |
| replaceDynamicScriptTags  | Seite/Layout        | string         |
| replaceInsertTags         | Insert-Tags         | string\|false  |
| reviseTable               | DCA/Backend         | bool\|null     |
| setCookie                 | System              | stdClass       |
| setNewPassword            | Member              | void           |
| sqlCompileCommands        | System              | array          |
| sqlGetFromDB              | System              | array          |
| sqlGetFromDca             | System              | array          |
| storeFormData             | Formulare           | array          |
| updatePersonalData        | Member              | void           |
| validateFormField         | Formulare           | Widget         |

_Quelle: https://docs.contao.org/5.x/dev/reference/hooks/ (Stand 2025-06)_
