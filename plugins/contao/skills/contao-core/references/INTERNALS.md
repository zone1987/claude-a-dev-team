# Internals: what an extension may rely on

The four policies that decide whether an extension survives an update, plus the Contao Manager API
and the issue workflow. Read `bc-promise` before depending on any core class.

## Contents

- [Backward compatibility promise](#backward-compatibility-promise)
- [Experimental features](#experimental-features)
- [Release procedure](#release-procedure)
- [Contao Manager API](#contao-manager-api)
- [Issue and PR workflow](#issue-and-pr-workflow)
- [Source](#source)

## Backward compatibility promise

Contao makes **the same promise as Symfony**, and follows Semantic Versioning: expect a breaking
change only on a new major version. It deviates from Symfony in one direction, because Contao is not
only a framework: it also ships tools of its own.

### What the promise does not cover

Nine exclusions, each a place where code may change under you in a minor release:

- **`@internal` classes and methods.** Mostly the constructors of services Contao provides. To change
  a service's behaviour, **decorate** it rather than replacing it with your own instance of the class.
- **`@experimental` classes and methods.** See the next section.
- **Templates.** They change often and have to be compared on every update. Contao tries to confine
  template changes to major and minor versions, but a bugfix may carry one.
- **Translation keys.** Added and removed in any minor version. Check core labels after an update, or
  ship your own and be unaffected.
- **Symfony application integration**, because Contao is a bundle like any other. Specifically:
  **commands**, **data collectors**, **dependency injection compiler passes**, **event listeners**.
- **The `ContaoManager/Plugin` class**, which integrates a bundle into the Managed Edition.
- **Tests in any bundle.** What is meant to be usable for testing your own extension is extracted
  into `contao/test-case`, which does follow Semantic Versioning.
- **Named parameters** (PHP 8.0). Currently outside the promise; the discussion is
  [contao/contao#2624](https://github.com/contao/contao/issues/2624).

### The practical consequence

Prefer **composition over inheritance**, and decorate services rather than extending them. Contao's
own rule of thumb is to break as little as possible and as much as required. A problematic break
belongs in an issue on the monorepository.

## Experimental features

An `@experimental` annotation puts an API **outside** the backward compatibility promise on purpose,
so real-world feedback can shape it before it is fixed. When it is mature, the annotation is removed
and the feature counts as stable. How a feature is *removed* rather than graduated is not stated
upstream.

Currently experimental, with the version each entered that state:

| Feature | Namespace | Since |
|---|---|---|
| Virtual filesystem | `Contao\CoreBundle\Filesystem\*` | 4.13 |
| Backend search | `Contao\CoreBundle\Search\*` | 5.5 |
| Job framework | `Contao\CoreBundle\Job\*` | 5.6 |
| Twig and Slots page layout | the modern page layout logic | 5.6 |

**Use them anyway.** The documentation is explicit: without real usage no feedback arrives, and the
core itself uses these features. The only difference from a stable API is that core development needs
watching more closely, and your own code has to be ready to follow sooner.

## Release procedure

Three stages before a version is stable, and **no beta phase**: experience showed hardly anyone
installs a beta, so it added no value.

| Stage | Length | What is accepted |
|---|---|---|
| Dev | about six months | feature PRs at any time |
| Review | about two weeks | complete feature PRs are reviewed and merged; incomplete ones move on |
| RC | about four weeks | bug fixes only; feature PRs move to the next milestone |

A feature PR counts as **complete** when it is no longer a draft, every function is implemented, the
unit tests are in place, and CI passes.

Two releases a year, so two deadlines:

- **Winter release**, around 15 February: a feature PR has to be complete by 31 December.
- **Summer release**, around 15 August: complete by 30 June. (The page writes "June 31".)

Support windows are not stated upstream.

## Contao Manager API

The Contao Manager ships as a Phar and exposes a REST API beside its interface. It lives at `/api`
below wherever the Phar sits: with `contao-manager.phar.php` at the document root of
`https://example.com`, the API is `https://example.com/contao-manager.phar.php/api/`. The full
endpoint list is the [OpenAPI documentation](https://contao.github.io/contao-manager/api/index.html).

### Two ways to authenticate

- **HTTP-only cookie**, through `/api/session`. Preferred where a browser is involved, because it
  stores no credentials and expires by itself. Suitable only where the user logs in before the API is
  used.
- **API token**, bound to a user account, for long-term access or where no browser is involved.

### Getting a token

The Manager implements OAuth Implicit Grant (RFC 6749 section 4.2). The documentation acknowledges
that Implicit Grant is not recommended on security grounds, but the alternatives require registering
an application ID up front, and since the Manager is distributed to every user there can be no
predefined list of permitted applications.

```
https://example.com/contao-manager.phar.php/#oauth?response_type=token&scope=admin
  &client_id=XXX&redirect_uri=https://your-website.com/your-script.php&state=XXX
```

- **response_type** (required): `token`, for Implicit Grant.
- **scope** (required): the access level. Scopes are **hierarchical**, so `admin` includes the rest.
  Several may be passed space-separated, and the user then chooses what to grant.
- **client_id** (required): a representative name for the application. It is stored with the token,
  and each `client_id` gets its own. **Reusing an existing `client_id` issues a new token and
  overwrites the old one.**
- **redirect_uri** (required): where the user returns after allowing or denying.
- **state** (optional): guards against CSRF, per RFC 6749 section 10.12.

The four scopes:

| Scope | May |
|---|---|
| `read` | see installed packages and read log files; change nothing |
| `update` | update existing packages, run maintenance such as clearing the cache |
| `install` | update and install packages, change system settings |
| `admin` | everything |

On **allow**, the token is appended to the `redirect_uri` per RFC 6749 section 4.2.2 and can be read
from the URL fragment. On **deny**, the redirect carries `error=access_denied`.

### Sending the token

Two headers, and the choice is about Apache rather than preference:

- **`Authentication: Bearer <token>`**: the standardised form the Manager fully supports. Note that
  the upstream page writes the header name as `Authentication`, while RFC 6750 defines
  `Authorization`; it is reproduced here as stated rather than silently corrected.
- **`Contao-Manager-Auth: <token>`**: the alternative, because some Apache versions strip
  `Authentication: Bearer` before it reaches the Manager.

Use the standard header where you control the webserver and have ruled that out; use
`Contao-Manager-Auth` to support any Manager on any unknown host.

### One-time passwordless login

Manager **1.7 and later**. A tool with API access can generate a URL that logs a user into the
Manager front end without a password. Created with `grant_type=one-time` on
`POST /api/users/{username}/tokens`; the response carries a `url`. **Valid for 30 seconds, usable
once.**

## Issue and PR workflow

### A new issue

No assignee by default. If a reported bug reproduces, **remove `unconfirmed`** and assign the
milestone of the version that should carry the fix, `4.9` for instance. Otherwise leave `unconfirmed`
and add a short comment. **Feature requests get no milestone.**

### A new PR

Assign it to its creator, label it `bug` or `feature` after reading it, and where it targets an active
version branch such as `5.7`, assign the matching milestone.

### The labels

| Label | Meaning |
|---|---|
| `unconfirmed` | the bug has not been reproduced yet |
| `bug` / `feature` | what the PR is |
| `up for discussion` | it is unclear how to fix or implement it |
| `help wanted` | nobody has self-assigned; volunteers sought |
| `BC break` | it cannot be done without breaking backward compatibility |

### Branch names

A prefix that says what the change is, so a reviewer knows before opening it:

- **`fix/`**: a bug fix, `fix/disable-turbo-navigation-on-hover`.
- **`feature/`**: a new feature, `feature/datacontainer_edit_twig_templates`.
- **`ci/`**: CI or build-chain, `ci/update-rector-tools`.

The page's own bad examples are instructive: `feat/`, `bugfix/`, `bug/`, `chore/` and a bare
`remove-legacy-stuff` or `rector` are all wrong.

## Source

Distilled from the Contao 5 developer documentation, retrieved 2026-08-21:

- https://docs.contao.org/5.x/dev/internals/bc-promise/
- https://docs.contao.org/5.x/dev/internals/experimental-features/
- https://docs.contao.org/5.x/dev/internals/release-procedure/
- https://docs.contao.org/5.x/dev/internals/contao-manager-api/
- https://docs.contao.org/5.x/dev/internals/issue-workflow/

Two facts the pages do not state, recorded as absent rather than guessed: the support window per
release, and how an experimental feature is removed rather than graduated.
