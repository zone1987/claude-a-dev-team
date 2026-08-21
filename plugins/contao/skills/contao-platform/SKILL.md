---
name: contao-platform
description: Contao 5 platform services: hooks and the hook reference, security, CSP, filesystem, caching, cron, translations. Use when the request names a Contao hook or Contao caching.
---

# Contao platform services

Cross-cutting services. Hooks are Contao's main extension point and have their own complete reference here.

## Reference map

- **[HOOKS-HOW-TO.md](references/HOOKS-HOW-TO.md)**: what a hook is, both registration methods, invokable services, priority, and the typical listener patterns.
- **[HOOKS-REFERENCE-00-INDEX.md](references/HOOKS-REFERENCE-00-INDEX.md)**: all 69 hooks in one alphabetical table with their group and return type. Start here to find the group.

The 69 hooks, grouped as the documentation groups them. Each entry gives the hook's signature, its arguments, its return value and a worked listener:

- **[HOOKS-REFERENCE-01-MEMBER-ACCOUNT.md](references/HOOKS-REFERENCE-01-MEMBER-ACCOUNT.md)**: `activateAccount`, `closeAccount`, `createNewUser`, `setNewPassword`, `updatePersonalData`.
- **[HOOKS-REFERENCE-02-NEWSLETTER.md](references/HOOKS-REFERENCE-02-NEWSLETTER.md)**: `activateRecipient`, `removeRecipient`.
- **[HOOKS-REFERENCE-03-COMMENTS.md](references/HOOKS-REFERENCE-03-COMMENTS.md)**: `addComment`, `isAllowedToEditComment`, `listComments`.
- **[HOOKS-REFERENCE-04-FORMS.md](references/HOOKS-REFERENCE-04-FORMS.md)**: the six form-generator hooks from `compileFormFields` to `validateFormField`.
- **[HOOKS-REFERENCE-05-PAGE-LAYOUT.md](references/HOOKS-REFERENCE-05-PAGE-LAYOUT.md)**: `generatePage`, `getPageLayout`, `loadPageDetails`, `modifyFrontendPage`, `replaceDynamicScriptTags` and three more.
- **[HOOKS-REFERENCE-06-TEMPLATES.md](references/HOOKS-REFERENCE-06-TEMPLATES.md)**: `parseTemplate`, `parseFrontendTemplate`, `parseBackendTemplate`, `parseWidget`, `outputBackendTemplate`.
- **[HOOKS-REFERENCE-07-CONTENT-MODULES.md](references/HOOKS-REFERENCE-07-CONTENT-MODULES.md)**: `getContentElement`, `getFrontendModule`, `getForm`, `compileArticle`, `isVisibleElement` and two more.
- **[HOOKS-REFERENCE-08-DCA-BACKEND.md](references/HOOKS-REFERENCE-08-DCA-BACKEND.md)**: `loadDataContainer`, `executePreActions`, `executePostActions`, `getAttributesFromDca`, `reviseTable` and two more.
- **[HOOKS-REFERENCE-09-CALENDAR-NEWS.md](references/HOOKS-REFERENCE-09-CALENDAR-NEWS.md)**: `getAllEvents`, `findCalendarBoundaries`, `newsListFetchItems`, `newsListCountItems`, `parseArticles`.
- **[HOOKS-REFERENCE-10-SEARCH.md](references/HOOKS-REFERENCE-10-SEARCH.md)**: `customizeSearch`, `indexPage`.
- **[HOOKS-REFERENCE-11-INSERT-TAGS.md](references/HOOKS-REFERENCE-11-INSERT-TAGS.md)**: `replaceInsertTags`, `insertTagFlags`.
- **[HOOKS-REFERENCE-12-THEME-FILES.md](references/HOOKS-REFERENCE-12-THEME-FILES.md)**: `exportTheme`, `extractThemeFiles`, `compareThemeFiles`, `getCombinedFile`, `postUpload`, `postDownload` and two more.
- **[HOOKS-REFERENCE-13-SYSTEM.md](references/HOOKS-REFERENCE-13-SYSTEM.md)**: `initializeSystem`, `loadLanguageFile`, `addCustomRegexp`, `parseDate`, `setCookie`, the `sql*` hooks and two more.

Platform services:

- **[SECURITY.md](references/SECURITY.md)**: checking permissions, DCA CRUD permissions (Contao 5.0 and later), and custom voters.
- **[CACHING.md](references/CACHING.md)**: the three caching methods, the cache-tag system, fragment rendering, and a complete example.
- **[CRON.md](references/CRON.md)**: configuring cron execution, registering a cron job, scope-aware jobs, and asynchronous execution.
- **[FILESYSTEM.md](references/FILESYSTEM.md)**: `VirtualFilesystem`, filesystem configuration, and the DBAFS.
- **[MESSAGING-JOBS.md](references/MESSAGING-JOBS.md)**: Symfony Messenger in Contao (5.1 and later) and the Jobs framework.
- **[TRANSLATIONS.md](references/TRANSLATIONS.md)**: the supported languages, translation structure, both implementation methods, and the Symfony integration.
- **[CSP.md](references/CSP.md)**: the `CspHandler`, `addSource`, and retrieving nonces.

## Source

Distilled from [docs.contao.org/5.x](https://docs.contao.org/5.x) : the developer documentation and the German end-user manual : plus the [contao/contao](https://github.com/contao/contao) source, retrieved 2026-08-20.
