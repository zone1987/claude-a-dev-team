# Contao Profiler (5.x)

## Overview

Contao ships the `symfony/profiler-pack`, which provides a **Web Developer Toolbar** and the **profiler view** as a development tool.

---

## Components

### Contao data collector

Contao extends the standard Symfony profiler with its own data collector that gathers Contao-specific request data and displays it in the profiler.

### Web Developer Toolbar

Toolbar extension for visual development feedback.

---

## Access

The profiler interface is available at: `/_profiler/`

---

## Availability

> **`dev` mode only:** data collectors, the profiler and the Web Developer Toolbar are disabled in `prod` mode for performance and security reasons.

---

## Symfony profiler documentation

For complete implementation details of the profiler framework:
→ https://symfony.com/doc/current/profiler.html

---

*Source: https://docs.contao.org/5.x/dev/framework/profiler/*
