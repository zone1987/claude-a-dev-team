#!/usr/bin/env python3
"""
Shopware 6.7 Component Reference Documentation Generator

Generates markdown reference files for sw-* and mt-* components.

Usage:
  python3 generate-docs.py --batch mt          # Generate all mt-* docs
  python3 generate-docs.py --batch sw-core     # sw-button*, sw-card*, sw-alert*, sw-modal*, sw-icon*, sw-loader*, sw-avatar*, sw-badge*, sw-label, sw-status, etc.
  python3 generate-docs.py --batch sw-form     # sw-field*, sw-text-field*, sw-select*, sw-checkbox*, etc.
  python3 generate-docs.py --batch sw-data     # sw-data-grid*, sw-entity-*, sw-page, sw-tabs*, sw-sidebar*, sw-context-*, etc.
  python3 generate-docs.py --batch sw-cms      # sw-cms-*
  python3 generate-docs.py --batch sw-bulk     # sw-bulk-edit-*, sw-customer-*, sw-product-*, sw-order-*
  python3 generate-docs.py --batch sw-catset   # sw-category-*, sw-settings-*, sw-flow-*
  python3 generate-docs.py --batch sw-ext      # sw-extension-*, sw-import-export-*, sw-media-*, sw-mail-*
  python3 generate-docs.py --batch sw-cond     # sw-condition-*, sw-custom-field-*, sw-first-run-wizard-*
  python3 generate-docs.py --batch sw-rest     # All remaining sw-*
  python3 generate-docs.py --component sw-button  # Single component
"""

import json
import os
import re
import sys
import glob as globmod
import argparse
from pathlib import Path

# Paths
BASE = "/Users/andreasgerhardt/Projekte/Shopware/6/6.7/shopware/vendor/shopware/administration/Resources/app/administration"
SW_COMP = f"{BASE}/src/app/component"
MT_COMP = f"{BASE}/node_modules/@shopware-ag/meteor-component-library/src/components"
MODULES = f"{BASE}/src/module"
JSON_FILE = "/Users/andreasgerhardt/.claude/skills/shopware-6.7-migration/shopware-components.json"
OUTPUT_DIR = "/Users/andreasgerhardt/.claude/skills/shopware-6.7-migration/components"

# Deprecated sw-* -> mt-* mappings
DEPRECATED_MAPPINGS = {
    "sw-button-deprecated": "mt-button",
    "sw-button": "mt-button",
    "sw-card-deprecated": "mt-card",
    "sw-card": "mt-card",
    "sw-alert-deprecated": "mt-banner",
    "sw-alert": "mt-banner",
    "sw-icon-deprecated": "mt-icon",
    "sw-icon": "mt-icon",
    "sw-loader-deprecated": "mt-loader",
    "sw-loader": "mt-loader",
    "sw-checkbox-field-deprecated": "mt-checkbox",
    "sw-checkbox-field": "mt-checkbox",
    "sw-colorpicker-deprecated": "mt-colorpicker",
    "sw-colorpicker": "mt-colorpicker",
    "sw-datepicker-deprecated": "mt-datepicker",
    "sw-datepicker": "mt-datepicker",
    "sw-email-field-deprecated": "mt-email-field",
    "sw-email-field": "mt-email-field",
    "sw-text-field-deprecated": "mt-text-field",
    "sw-text-field": "mt-text-field",
    "sw-number-field-deprecated": "mt-number-field",
    "sw-number-field": "mt-number-field",
    "sw-password-field-deprecated": "mt-password-field",
    "sw-password-field": "mt-password-field",
    "sw-textarea-deprecated": "mt-textarea",
    "sw-textarea": "mt-textarea",
    "sw-switch-field-deprecated": "mt-switch",
    "sw-switch-field": "mt-switch",
    "sw-url-field-deprecated": "mt-url-field",
    "sw-url-field": "mt-url-field",
    "sw-select-field-deprecated": "mt-select",
    "sw-select-field": "mt-select",
    "sw-external-link-deprecated": "mt-link",
    "sw-external-link": "mt-link",
    "sw-skeleton-bar-deprecated": "mt-skeleton-bar",
    "sw-skeleton-bar": "mt-skeleton-bar",
    "sw-progress-bar-deprecated": "mt-progress-bar",
    "sw-progress-bar": "mt-progress-bar",
    "sw-tabs-deprecated": "mt-tabs",
    "sw-tabs": "mt-tabs",
    "sw-modal-deprecated": "mt-modal",
}

# Component descriptions (curated for common ones)
COMP_DESCRIPTIONS = {
    "sw-button": "Wrapper component that auto-switches between sw-button-deprecated and mt-button.",
    "sw-button-deprecated": "Button component with variants, sizes, loading states, and router link support.",
    "sw-button-group": "Groups multiple buttons together with consistent spacing.",
    "sw-button-process": "Button with integrated progress/loading state visualization.",
    "sw-card": "Wrapper component that auto-switches between sw-card-deprecated and mt-card.",
    "sw-card-deprecated": "Card container for grouping related content with optional title, toolbar, and hero section.",
    "sw-card-filter": "Filter card with integrated search functionality.",
    "sw-card-section": "Section divider within a sw-card with configurable appearance.",
    "sw-card-view": "Container for organizing multiple sw-card components in a scrollable view.",
    "sw-alert": "Wrapper component that auto-switches between sw-alert-deprecated and mt-banner.",
    "sw-alert-deprecated": "Alert/notification banner with variants (info, warning, error, success) and optional close button.",
    "sw-modal": "Modal dialog overlay with title, subtitle, body content, and footer actions.",
    "sw-icon": "Wrapper component that auto-switches between sw-icon-deprecated and mt-icon.",
    "sw-icon-deprecated": "SVG icon component with configurable size, color, and decorative mode.",
    "sw-loader": "Wrapper that auto-switches between sw-loader-deprecated and mt-loader.",
    "sw-loader-deprecated": "Loading spinner indicator with configurable size.",
    "sw-avatar": "Avatar component displaying user initials, images, or placeholder icons.",
    "sw-data-grid": "Advanced data grid with sorting, filtering, inline editing, column resizing, and selection.",
    "sw-entity-listing": "Extended data grid for entity listing with pagination, search, and CRUD operations.",
    "sw-entity-single-select": "Single-select dropdown for Shopware entities with search and API integration.",
    "sw-entity-multi-select": "Multi-select dropdown for Shopware entities with tag display.",
    "sw-entity-tag-select": "Tag-based multi-select for entity associations.",
    "sw-page": "Base page layout component with smart bar, header, content area, and sidebar.",
    "sw-tabs": "Wrapper that auto-switches between sw-tabs-deprecated and mt-tabs.",
    "sw-tabs-deprecated": "Tab navigation with support for router-based and event-based tab switching.",
    "sw-text-field": "Wrapper that auto-switches between sw-text-field-deprecated and mt-text-field.",
    "sw-text-field-deprecated": "Text input field with label, placeholder, help text, error state, and suffix/prefix.",
    "sw-number-field": "Wrapper that auto-switches between sw-number-field-deprecated and mt-number-field.",
    "sw-number-field-deprecated": "Number input with min/max, step, digits after decimal, and unit display.",
    "sw-select-field": "Wrapper that auto-switches between sw-select-field-deprecated and mt-select.",
    "sw-select-field-deprecated": "Native HTML select dropdown with label, placeholder, and error support.",
    "sw-checkbox-field": "Wrapper that auto-switches between sw-checkbox-field-deprecated and mt-checkbox.",
    "sw-checkbox-field-deprecated": "Checkbox field with label, help text, and error state.",
    "sw-switch-field": "Wrapper that auto-switches between sw-switch-field-deprecated and mt-switch.",
    "sw-switch-field-deprecated": "Toggle switch with optional label and bordered appearance.",
    "sw-datepicker": "Wrapper that auto-switches between sw-datepicker-deprecated and mt-datepicker.",
    "sw-datepicker-deprecated": "Date/time picker with calendar, time selection, and various date formats.",
    "sw-colorpicker": "Wrapper that auto-switches between sw-colorpicker-deprecated and mt-colorpicker.",
    "sw-colorpicker-deprecated": "Color picker with hex/rgb input, alpha channel, and preset colors.",
    "sw-textarea": "Wrapper that auto-switches between sw-textarea-deprecated and mt-textarea.",
    "sw-textarea-deprecated": "Multi-line text input with auto-grow and character count.",
    "sw-password-field": "Wrapper that auto-switches between sw-password-field-deprecated and mt-password-field.",
    "sw-password-field-deprecated": "Password input with show/hide toggle and strength indicator.",
    "sw-email-field": "Wrapper that auto-switches between sw-email-field-deprecated and mt-email-field.",
    "sw-email-field-deprecated": "Email input with built-in email validation.",
    "sw-url-field": "Wrapper that auto-switches between sw-url-field-deprecated and mt-url-field.",
    "sw-url-field-deprecated": "URL input with protocol prefix and optional SSL switch.",
    "sw-context-button": "Trigger button that opens a context menu dropdown.",
    "sw-context-menu": "Context menu container with menu items and dividers.",
    "sw-context-menu-item": "Individual menu item within a context menu.",
    "sw-context-menu-divider": "Visual divider between context menu item groups.",
    "sw-sidebar": "Side panel container for filters, navigation, or auxiliary content.",
    "sw-sidebar-item": "Individual item within a sw-sidebar component.",
    "sw-collapse": "Collapsible content panel with animated expand/collapse.",
    "sw-container": "Flexible layout container with configurable columns and gap.",
    "sw-search-bar": "Global search bar component with auto-complete and module filtering.",
    "sw-confirm-modal": "Confirmation modal dialog with confirm and cancel actions.",
    "sw-media-field": "Media selection field for picking images/files from the media library.",
    "sw-media-upload-v2": "Media upload component supporting drag & drop, URL upload, and multi-file upload.",
    "sw-media-compact-upload-v2": "Compact variant of the media upload component.",
    "sw-code-editor": "Code editor component with syntax highlighting (based on Ace editor).",
    "sw-form-field-renderer": "Dynamic form field renderer that generates form inputs from custom field definitions.",
    "sw-custom-field-set-renderer": "Renders a complete set of custom fields with their configured field types.",
    "sw-condition-tree": "Visual rule/condition tree builder with AND/OR grouping.",
    "sw-filter-panel": "Filter panel with multiple configurable filter types.",
    "sw-inherit-wrapper": "Wrapper component that handles value inheritance from parent entities.",
    "sw-inheritance-switch": "Toggle switch for enabling/disabling value inheritance.",
    "sw-language-switch": "Language selector for switching the admin editing language.",
    "sw-many-to-many-assignment-card": "Card component for managing many-to-many entity relationships.",
    "sw-tree": "Tree view component with drag & drop reordering.",
    "sw-tree-item": "Individual tree node within sw-tree.",
    "sw-tag-field": "Tag input field for adding and removing tags.",
}

# mt-* component descriptions
MT_DESCRIPTIONS = {
    "mt-button": "Primary interactive button component with variants, sizes, loading states, and icon slots.",
    "mt-card": "Card container for grouping related content with optional title, subtitle, hero, and toolbar.",
    "mt-banner": "Notification banner for displaying info, success, warning, error, or attention messages.",
    "mt-icon": "SVG icon component rendering icons from the Shopware icon set.",
    "mt-loader": "Loading spinner indicator for async operations.",
    "mt-badge": "Small status badge for labeling and categorizing items.",
    "mt-color-badge": "Color swatch badge displaying a specific color value.",
    "mt-progress-bar": "Progress bar indicator for showing completion status.",
    "mt-promo-badge": "Promotional badge for highlighting features or status.",
    "mt-skeleton-bar": "Skeleton loading placeholder for content that is being loaded.",
    "mt-snackbar": "Temporary notification snackbar appearing at the bottom of the screen.",
    "mt-toast": "Toast notification manager for stacking multiple toast messages.",
    "mt-toast-notification": "Individual toast notification with auto-dismiss and action support.",
    "mt-text-field": "Text input field with label, placeholder, help text, prefix, suffix, and error state.",
    "mt-number-field": "Number input with step, min/max, digits control, and increase/decrease buttons.",
    "mt-text-editor": "Rich text editor with formatting toolbar (bold, italic, lists, links, etc.).",
    "mt-textarea": "Multi-line text input with label and error handling.",
    "mt-checkbox": "Checkbox input with label, indeterminate state, and inheritance support.",
    "mt-switch": "Toggle switch input with label and optional bordered appearance.",
    "mt-select": "Dropdown select with single/multi selection, search, and custom rendering.",
    "mt-datepicker": "Date/time picker with calendar and various date format support.",
    "mt-colorpicker": "Color picker with hex input, alpha channel, and visual color selection.",
    "mt-email-field": "Email input field with built-in validation.",
    "mt-password-field": "Password input with show/hide toggle.",
    "mt-url-field": "URL input field with protocol prefix.",
    "mt-slider": "Slider input for selecting a value within a range.",
    "mt-unit-field": "Number input with a unit selector dropdown (e.g., px, em, %).",
    "mt-help-text": "Help icon with tooltip popover showing explanatory text.",
    "mt-modal": "Modal dialog with title, content area, actions, and close functionality.",
    "mt-popover": "Popover overlay positioned relative to a trigger element.",
    "mt-popover-item": "Menu item within a popover menu.",
    "mt-popover-item-result": "Result item within a popover search results list.",
    "mt-tooltip": "Tooltip overlay showing help text on hover.",
    "mt-tabs": "Tab navigation with support for items array and content slot.",
    "mt-link": "Styled link component for navigation with external/internal variants.",
    "mt-search": "Search input field with debounced search event.",
    "mt-segmented-control": "Segmented toggle control for switching between options.",
    "mt-data-table": "Advanced data table with sorting, filtering, pagination, and column configuration.",
    "mt-pagination": "Pagination control with page navigation and items-per-page selector.",
    "mt-context-button": "Button that triggers a context menu dropdown.",
    "mt-context-menu-item": "Individual item in a context menu.",
    "mt-context-menu-divider": "Visual separator between context menu groups.",
    "mt-avatar": "Avatar component displaying user initials or images.",
    "mt-entity-data-table": "Data table with integrated Shopware entity data source.",
    "mt-entity-select": "Entity select dropdown with Shopware API data source.",
    "mt-chart": "Chart component for data visualization (bar, line, pie charts).",
    "mt-text": "Typography component for consistent text rendering.",
    "mt-theme-provider": "Theme provider component that wraps children with CSS custom properties.",
    "mt-inset": "Layout component providing consistent inset padding.",
    "mt-empty-state": "Empty state display with icon, title, and description for zero-data scenarios.",
}


def load_json_data():
    with open(JSON_FILE) as f:
        return json.load(f)


def find_sw_source_files(comp_name):
    """Find index.js/ts and .html.twig for a sw-* component."""
    # Search in app/component directory tree
    for root, dirs, files in os.walk(SW_COMP):
        dirname = os.path.basename(root)
        if dirname == comp_name:
            index_file = None
            twig_file = None
            for f in files:
                if f in ("index.js", "index.ts"):
                    index_file = os.path.join(root, f)
                if f.endswith(".html.twig"):
                    twig_file = os.path.join(root, f)
            return index_file, twig_file

    # Also search in module directories
    for root, dirs, files in os.walk(MODULES):
        dirname = os.path.basename(root)
        if dirname == comp_name:
            index_file = None
            twig_file = None
            for f in files:
                if f in ("index.js", "index.ts"):
                    index_file = os.path.join(root, f)
                if f.endswith(".html.twig"):
                    twig_file = os.path.join(root, f)
            return index_file, twig_file

    return None, None


def extract_slots_from_twig(twig_content):
    """Extract slot definitions from .html.twig template."""
    slots = []
    seen = set()
    # Match <slot name="xxx"> or <slot name="xxx" :prop="val">
    # Also match {% block sw_xxx %} patterns as pseudo-slots
    slot_pattern = re.compile(r'<slot\s+(?:[^>]*?)name=["\']([^"\']+)["\']([^>]*?)/?>', re.DOTALL)
    for m in slot_pattern.finditer(twig_content):
        name = m.group(1)
        attrs = m.group(2)
        if name not in seen:
            seen.add(name)
            # Extract slot props (v-bind, :prop patterns)
            slot_props = []
            bind_pattern = re.compile(r':(\w+)=["\']([^"\']*)["\']')
            for bp in bind_pattern.finditer(attrs):
                slot_props.append(f"{bp.group(1)}: {bp.group(2)}")
            slots.append({
                "name": name,
                "props": ", ".join(slot_props) if slot_props else "—",
            })

    # Also check for unnamed default slot
    if '<slot>' in twig_content or '<slot />' in twig_content or re.search(r'<slot\s*/?\s*>', twig_content):
        if "default" not in seen:
            slots.insert(0, {"name": "default", "props": "—"})

    # Check for block-based slots (Shopware's twig block pattern)
    block_pattern = re.compile(r'\{%\s*block\s+([\w]+)\s*%\}')
    for m in block_pattern.finditer(twig_content):
        block_name = m.group(1)
        # Only include blocks that look like slot insertion points
        if block_name not in seen:
            seen.add(block_name)

    return slots


def extract_slots_from_vue(vue_content):
    """Extract slots from Vue SFC template."""
    slots = []
    seen = set()

    # Match defineSlots<{...}>()
    define_slots = re.search(r'defineSlots<\{([^}]+)\}>\(\)', vue_content, re.DOTALL)
    if define_slots:
        slots_text = define_slots.group(1)
        # Parse typed slot definitions like: default: null; iconFront: { size: number };
        for line in slots_text.split(';'):
            line = line.strip()
            if not line:
                continue
            # Match "slotName: type" or "slotName(props): type"
            m = re.match(r'(\w+)\s*(?:\(([^)]*)\))?\s*:\s*(.+)', line)
            if m:
                name = m.group(1)
                props_type = m.group(3).strip()
                if name not in seen:
                    seen.add(name)
                    if props_type == "null" or props_type == "void":
                        slots.append({"name": name, "props": "—"})
                    else:
                        slots.append({"name": name, "props": props_type})

    # Also find <slot> tags in template
    template_match = re.search(r'<template>(.*?)</template>', vue_content, re.DOTALL)
    if template_match:
        template = template_match.group(1)
        # Named slots
        slot_pattern = re.compile(r'<slot\s+(?:[^>]*?)name=["\']([^"\']+)["\']([^>]*?)/?>')
        for m in slot_pattern.finditer(template):
            name = m.group(1)
            if name not in seen:
                seen.add(name)
                slots.append({"name": name, "props": "—"})
        # Default slot
        if re.search(r'<slot\s*/?\s*>', template) or re.search(r'<slot\s*(?!name)[^>]*/?>', template):
            if "default" not in seen:
                seen.insert(0, "default") if isinstance(seen, list) else seen.add("default")
                slots.insert(0, {"name": "default", "props": "—"})

    return slots


def extract_props_from_vue(vue_content):
    """Extract props from Vue SFC defineProps/withDefaults."""
    props = {}

    # Try withDefaults(defineProps<{...}>(), {...})
    wd_match = re.search(
        r'withDefaults\s*\(\s*defineProps<\{([^}]+(?:\{[^}]*\}[^}]*)*)\}>\(\)\s*,\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}\s*\)',
        vue_content, re.DOTALL
    )

    if wd_match:
        props_def = wd_match.group(1)
        defaults_def = wd_match.group(2)

        # Parse defaults
        defaults = {}
        for dm in re.finditer(r'(\w+)\s*:\s*(?:undefined|"[^"]*"|\'[^\']*\'|\d+|true|false|null|[^,\n]+)', defaults_def):
            key = dm.group(0).split(':')[0].strip()
            val = ':'.join(dm.group(0).split(':')[1:]).strip().rstrip(',')
            defaults[key] = val

        # Parse prop types
        for line in props_def.split('\n'):
            line = line.strip().rstrip(';').rstrip(',')
            if not line or line.startswith('//') or line.startswith('/*') or line.startswith('*'):
                continue
            # Match "propName?: Type" or "propName: Type"
            pm = re.match(r'(\w+)\s*(\?)?\s*:\s*(.+)', line)
            if pm:
                name = pm.group(1)
                optional = pm.group(2) == '?'
                ptype = pm.group(3).strip().rstrip(';').rstrip(',')
                props[name] = {
                    "type": ptype,
                    "required": not optional and name not in defaults,
                    "default": defaults.get(name, "—"),
                }
    else:
        # Try simple defineProps<{...}>()
        dp_match = re.search(r'defineProps<\{([^}]+(?:\{[^}]*\}[^}]*)*)\}>\(\)', vue_content, re.DOTALL)
        if dp_match:
            props_def = dp_match.group(1)
            for line in props_def.split('\n'):
                line = line.strip().rstrip(';').rstrip(',')
                if not line or line.startswith('//') or line.startswith('/*') or line.startswith('*'):
                    continue
                pm = re.match(r'(\w+)\s*(\?)?\s*:\s*(.+)', line)
                if pm:
                    name = pm.group(1)
                    optional = pm.group(2) == '?'
                    ptype = pm.group(3).strip().rstrip(';').rstrip(',')
                    props[name] = {
                        "type": ptype,
                        "required": not optional,
                        "default": "—",
                    }

    return props


def extract_emits_from_vue(vue_content):
    """Extract emits from Vue SFC defineEmits."""
    emits = []

    # defineEmits<{...}>()
    de_match = re.search(r'defineEmits<\{([^}]+(?:\{[^}]*\}[^}]*)*)\}>\(\)', vue_content, re.DOTALL)
    if de_match:
        emits_text = de_match.group(1)
        for line in emits_text.split('\n'):
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            # Match "(e: 'eventName', payload: Type): void"
            em = re.match(r'\(\s*e\s*:\s*["\']([^"\']+)["\'](?:\s*,\s*(.+?))?\s*\)\s*:\s*\w+', line)
            if em:
                name = em.group(1)
                payload = em.group(2)
                emits.append({
                    "name": name,
                    "payload": payload.strip() if payload else "—",
                })

    # defineEmits([...])
    de_arr = re.search(r'defineEmits\(\s*\[([^\]]+)\]\s*\)', vue_content)
    if de_arr and not emits:
        for m in re.finditer(r'["\']([^"\']+)["\']', de_arr.group(1)):
            emits.append({"name": m.group(1), "payload": "—"})

    # Also check for emit() calls in script
    for m in re.finditer(r"emit\(['\"]([^'\"]+)['\"]", vue_content):
        name = m.group(1)
        if not any(e["name"] == name for e in emits):
            emits.append({"name": name, "payload": "—"})

    return emits


def find_usage_examples(comp_name, max_examples=5):
    """Search for usage examples in src/module/**/*.html.twig."""
    examples = []
    tag_pattern = f"<{comp_name}"

    for root, dirs, files in os.walk(MODULES):
        for f in files:
            if not f.endswith('.html.twig'):
                continue
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', errors='replace') as fh:
                    content = fh.read()
                if tag_pattern in content:
                    # Extract the usage snippet
                    snippets = extract_tag_snippets(content, comp_name)
                    for snippet in snippets[:2]:  # max 2 from same file
                        # Get relative path from module dir
                        rel = os.path.relpath(filepath, MODULES)
                        examples.append({
                            "source": rel,
                            "snippet": snippet,
                        })
                        if len(examples) >= max_examples:
                            return examples
            except Exception:
                pass

    return examples


def extract_tag_snippets(content, tag_name):
    """Extract concise snippets showing component usage."""
    snippets = []
    lines = content.split('\n')
    tag_open = f"<{tag_name}"

    i = 0
    while i < len(lines):
        if tag_open in lines[i]:
            start = max(0, i)
            # Find end of tag usage (self-closing or closing tag)
            end = i
            depth = 0
            for j in range(i, min(i + 30, len(lines))):
                line = lines[j]
                if tag_open in line:
                    depth += 1
                if f"</{tag_name}>" in line:
                    depth -= 1
                    if depth <= 0:
                        end = j
                        break
                if '/>' in line and depth == 1 and f"</{tag_name}>" not in line:
                    # Self-closing on same line or next
                    if tag_open in line:
                        end = j
                        depth -= 1
                        if depth <= 0:
                            break
                end = j

            snippet_lines = lines[start:end + 1]
            # Trim excessive whitespace, limit to 15 lines
            snippet = '\n'.join(snippet_lines[:15])
            # Remove leading whitespace consistently
            min_indent = 999
            for sl in snippet_lines:
                if sl.strip():
                    min_indent = min(min_indent, len(sl) - len(sl.lstrip()))
            if min_indent < 999:
                snippet = '\n'.join(sl[min_indent:] if len(sl) >= min_indent else sl for sl in snippet_lines[:15])

            if len(snippet.strip()) > 10:
                snippets.append(snippet)
            i = end + 1
        else:
            i += 1

    return snippets


def format_type(type_info):
    """Format a prop type from JSON or Vue."""
    if isinstance(type_info, str):
        return f"`{type_info}`"
    if isinstance(type_info, list):
        types = [str(t) if t else "null" for t in type_info]
        return "`" + " \\| ".join(types) + "`"
    if isinstance(type_info, dict):
        return "`Object`"
    return "`any`"


def format_default(val):
    """Format a default value."""
    if val is None:
        return "`null`"
    if val == "—":
        return "—"
    if isinstance(val, bool):
        return f"`{str(val).lower()}`"
    if isinstance(val, (int, float)):
        return f"`{val}`"
    if isinstance(val, str):
        val = val.strip().strip(',')
        if val in ('undefined', 'null'):
            return f"`{val}`"
        if val in ('true', 'false'):
            return f"`{val}`"
        # If it's already quoted
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            return f"`{val}`"
        return f"`'{val}'`" if val else "`''`"
    return f"`{val}`"


def generate_sw_doc(comp_name, json_data):
    """Generate markdown doc for a sw-* component."""
    data = json_data.get(comp_name, {})
    is_deprecated = comp_name.endswith("-deprecated")
    is_wrapper = comp_name in DEPRECATED_MAPPINGS and not is_deprecated

    # Get description
    desc = COMP_DESCRIPTIONS.get(comp_name, "")
    if not desc:
        if is_deprecated:
            base = comp_name.replace("-deprecated", "")
            mt_name = DEPRECATED_MAPPINGS.get(comp_name, "")
            desc = f"Deprecated component. Use `{mt_name}` instead."
        elif is_wrapper:
            mt_name = DEPRECATED_MAPPINGS.get(comp_name, "")
            desc = f"Wrapper component that auto-switches between the deprecated implementation and `{mt_name}`."
        else:
            desc = f"Shopware Administration component."

    md = []

    # Header
    md.append(f"# {comp_name}\n")

    # Deprecation notice
    if is_deprecated:
        mt_name = DEPRECATED_MAPPINGS.get(comp_name, "")
        if mt_name:
            md.append(f"> **Deprecated in 6.7** — Use `{mt_name}` instead. Will be removed in 6.8.")
            md.append(f"> See [{mt_name}]({mt_name}.md) for the replacement.\n")
        else:
            md.append(f"> **Deprecated in 6.7** — Will be removed in 6.8.\n")
    elif is_wrapper:
        mt_name = DEPRECATED_MAPPINGS.get(comp_name, "")
        md.append(f"> **Migration wrapper** — Delegates to `{mt_name}` by default. The deprecated implementation is available via the `deprecated` prop.")
        md.append(f"> See [{mt_name}]({mt_name}.md) for the new component.\n")
    else:
        md.append(f"> {desc}\n")

    # Migration section for deprecated components
    if is_deprecated and comp_name in DEPRECATED_MAPPINGS:
        mt_name = DEPRECATED_MAPPINGS[comp_name]
        md.append("## Migration\n")
        md.append("| Old (sw-*) | New (mt-*) |")
        md.append("|-----------|-----------|")
        old_tag = comp_name.replace("-deprecated", "")
        md.append(f"| `<{old_tag}>` | `<{mt_name}>` |")
        md.append("")

    # Props
    props = data.get("props", {})
    if props and isinstance(props, dict):
        md.append("## Props\n")
        md.append("| Name | Type | Default | Required | Description |")
        md.append("|------|------|---------|----------|-------------|")
        for pname, pinfo in props.items():
            if isinstance(pinfo, dict):
                ptype = pinfo.get("type", "any")
                ptype_str = format_type(ptype)
                pdefault = pinfo.get("default", "—")
                pdefault_str = format_default(pdefault)
                preq = "yes" if pinfo.get("required", False) else "no"
                valid_values = pinfo.get("validValues", [])
                pdesc = ""
                if valid_values:
                    pdesc = f"Valid: `{'`, `'.join(str(v) for v in valid_values)}`"
                md.append(f"| {pname} | {ptype_str} | {pdefault_str} | {preq} | {pdesc} |")
            else:
                md.append(f"| {pname} | `any` | — | no | |")
        md.append("")
    elif props and isinstance(props, list):
        md.append("## Props\n")
        md.append("| Name | Type | Default | Required | Description |")
        md.append("|------|------|---------|----------|-------------|")
        for pname in props:
            md.append(f"| {pname} | `any` | — | no | |")
        md.append("")

    # Slots - from twig template
    _, twig_file = find_sw_source_files(comp_name)
    slots = []
    if twig_file:
        try:
            with open(twig_file, 'r', errors='replace') as f:
                twig_content = f.read()
            slots = extract_slots_from_twig(twig_content)
        except Exception:
            pass

    if slots:
        md.append("## Slots\n")
        md.append("| Name | Slot Props | Description |")
        md.append("|------|-----------|-------------|")
        for s in slots:
            md.append(f"| {s['name']} | {s['props']} | |")
        md.append("")

    # Events/Emits
    emits = data.get("emits", [])
    if emits:
        md.append("## Events / Emits\n")
        md.append("| Event | Payload | Description |")
        md.append("|-------|---------|-------------|")
        for e in emits:
            if isinstance(e, str):
                md.append(f"| {e} | — | |")
            elif isinstance(e, dict):
                md.append(f"| {e.get('name', '')} | {e.get('payload', '—')} | |")
        md.append("")

    # Methods
    methods = data.get("methods", [])
    if methods:
        md.append("## Methods\n")
        md.append("| Method | Description |")
        md.append("|--------|-------------|")
        for m in methods:
            if isinstance(m, str):
                md.append(f"| `{m}` | |")
        md.append("")

    # Data
    data_attrs = data.get("data", {})
    if isinstance(data_attrs, dict) and data_attrs:
        md.append("## Data\n")
        md.append("| Name | Type | Default | Description |")
        md.append("|------|------|---------|-------------|")
        for dname, dinfo in data_attrs.items():
            if isinstance(dinfo, dict):
                dtype = format_type(dinfo.get("type", "any"))
                ddefault = format_default(dinfo.get("default", "—"))
                md.append(f"| {dname} | {dtype} | {ddefault} | |")
            else:
                dval = format_default(dinfo)
                md.append(f"| {dname} | `any` | {dval} | |")
        md.append("")

    # Computed
    computed = data.get("computed", [])
    if computed:
        md.append("## Computed Properties\n")
        md.append("| Name | Description |")
        md.append("|------|-------------|")
        for c in computed:
            if isinstance(c, str):
                md.append(f"| `{c}` | |")
        md.append("")

    # Examples
    examples = find_usage_examples(comp_name, max_examples=5)
    # Also search by wrapper name if deprecated
    if is_deprecated:
        base_name = comp_name.replace("-deprecated", "")
        extra = find_usage_examples(base_name, max_examples=5 - len(examples))
        examples.extend(extra)

    if examples:
        md.append("## Examples\n")
        for idx, ex in enumerate(examples[:5], 1):
            md.append(f"### Example {idx}")
            md.append(f"Source: `{ex['source']}`")
            md.append("```twig")
            md.append(ex["snippet"])
            md.append("```\n")
    else:
        # Generate a synthetic example from props
        md.append("## Examples\n")
        md.append("### Basic Usage")
        md.append("```twig")
        if props and isinstance(props, dict):
            prop_attrs = []
            for pname, pinfo in list(props.items())[:3]:
                if isinstance(pinfo, dict) and pinfo.get("required"):
                    prop_attrs.append(f'    {pname}="..."')
            if prop_attrs:
                md.append(f"<{comp_name}")
                for pa in prop_attrs:
                    md.append(pa)
                md.append(f">")
                md.append(f"    <!-- content -->")
                md.append(f"</{comp_name}>")
            else:
                md.append(f"<{comp_name}>")
                md.append(f"    <!-- content -->")
                md.append(f"</{comp_name}>")
        else:
            md.append(f"<{comp_name}>")
            md.append(f"    <!-- content -->")
            md.append(f"</{comp_name}>")
        md.append("```\n")

    return "\n".join(md)


def generate_mt_doc(comp_name, vue_file):
    """Generate markdown doc for a mt-* component."""
    try:
        with open(vue_file, 'r', errors='replace') as f:
            vue_content = f.read()
    except Exception:
        vue_content = ""

    desc = MT_DESCRIPTIONS.get(comp_name, f"Meteor component from the `@shopware-ag/meteor-component-library` package.")

    md = []
    md.append(f"# {comp_name}\n")
    md.append(f"> {desc}\n")

    # Props
    props = extract_props_from_vue(vue_content)
    if props:
        md.append("## Props\n")
        md.append("| Name | Type | Default | Required | Description |")
        md.append("|------|------|---------|----------|-------------|")
        for pname, pinfo in props.items():
            ptype = f"`{pinfo['type']}`"
            pdefault = format_default(pinfo['default'])
            preq = "yes" if pinfo['required'] else "no"
            md.append(f"| {pname} | {ptype} | {pdefault} | {preq} | |")
        md.append("")

    # Slots
    slots = extract_slots_from_vue(vue_content)
    if slots:
        md.append("## Slots\n")
        md.append("| Name | Slot Props | Description |")
        md.append("|------|-----------|-------------|")
        for s in slots:
            md.append(f"| {s['name']} | {s['props']} | |")
        md.append("")

    # Events/Emits
    emits = extract_emits_from_vue(vue_content)
    if emits:
        md.append("## Events / Emits\n")
        md.append("| Event | Payload | Description |")
        md.append("|-------|---------|-------------|")
        for e in emits:
            md.append(f"| {e['name']} | {e['payload']} | |")
        md.append("")

    # Usage examples from module twig files
    examples = find_usage_examples(comp_name, max_examples=5)
    if examples:
        md.append("## Examples\n")
        for idx, ex in enumerate(examples[:5], 1):
            md.append(f"### Example {idx}")
            md.append(f"Source: `{ex['source']}`")
            md.append("```twig")
            md.append(ex["snippet"])
            md.append("```\n")
    else:
        # Generate synthetic example
        md.append("## Examples\n")
        md.append("### Basic Usage")
        md.append("```vue")
        md.append(f"<{comp_name}")
        if props:
            required = [(k, v) for k, v in props.items() if v.get("required")]
            for pname, pinfo in required[:3]:
                md.append(f'    {pname}="..."')
        md.append(f">")
        if slots and any(s["name"] == "default" for s in slots):
            md.append(f"    <!-- content -->")
        md.append(f"</{comp_name}>")
        md.append("```\n")

    return "\n".join(md)


def get_mt_components():
    """Get list of all public mt-* components."""
    components = []
    for root, dirs, files in os.walk(MT_COMP):
        # Skip _internal
        if '/_internal/' in root or root.endswith('/_internal'):
            continue
        # Skip sub-components and renderers
        if '/sub-components/' in root or '/renderer/' in root:
            continue
        for f in files:
            if f.endswith('.vue'):
                name = f.replace('.vue', '')
                vue_file = os.path.join(root, f)
                components.append((name, vue_file))
    return components


def get_batch_components(batch_name, json_data):
    """Get list of component names for a given batch."""
    all_names = sorted(json_data.keys())

    if batch_name == "sw-core":
        prefixes = ["sw-button", "sw-card", "sw-alert", "sw-modal", "sw-icon",
                     "sw-loader", "sw-avatar", "sw-badge", "sw-label", "sw-status",
                     "sw-circle-icon", "sw-color-badge", "sw-description-list",
                     "sw-empty-state", "sw-error", "sw-external-link", "sw-help-text",
                     "sw-highlight-text", "sw-image", "sw-internal-link",
                     "sw-page", "sw-skeleton", "sw-progress-bar", "sw-confirm",
                     "sw-collapse", "sw-container", "sw-desktop", "sw-discard",
                     "sw-error-boundary", "sw-error-summary", "sw-gtc-checkbox",
                     "sw-help-center", "sw-help-sidebar", "sw-hidden-iframes",
                     "sw-iframe-renderer", "sw-ignore-class", "sw-inactivity-login",
                     "sw-license", "sw-notification", "sw-popover", "sw-shortcut",
                     "sw-tooltip", "sw-verify", "sw-app-action", "sw-app-topbar",
                     "sw-app-wrong", "sw-app-shop-id", "sw-in-app-purchase"]
        return [n for n in all_names if any(n.startswith(p) or n == p for p in prefixes)]

    elif batch_name == "sw-form":
        prefixes = ["sw-field", "sw-text-field", "sw-text-editor", "sw-number-field",
                     "sw-select", "sw-single-select", "sw-multi-select", "sw-grouped-single-select",
                     "sw-checkbox", "sw-switch", "sw-datepicker", "sw-colorpicker",
                     "sw-compact-colorpicker", "sw-textarea", "sw-password-field",
                     "sw-email-field", "sw-url-field", "sw-file-input", "sw-code-editor",
                     "sw-form-field-renderer", "sw-base-field", "sw-block-field",
                     "sw-contextual-field", "sw-field-copyable", "sw-field-error",
                     "sw-boolean-radio-group", "sw-confirm-field", "sw-dynamic-url",
                     "sw-inherit-wrapper", "sw-inheritance-switch", "sw-inheritance-warning",
                     "sw-maintain-currencies", "sw-list-price", "sw-price",
                     "sw-tagged-field", "sw-tag-field", "sw-text-preview",
                     "sw-upload-listener", "sw-simple-search-field", "sw-select-result",
                     "sw-select-result-list", "sw-select-selection-list", "sw-select-field",
                     "sw-select-number-field", "sw-select-base", "sw-select-deprecated"]
        return [n for n in all_names if any(n.startswith(p) or n == p for p in prefixes)]

    elif batch_name == "sw-data":
        prefixes = ["sw-data-grid", "sw-entity", "sw-grid", "sw-tabs", "sw-sidebar",
                     "sw-context-button", "sw-context-menu", "sw-search",
                     "sw-address", "sw-admin-menu", "sw-admin", "sw-arrow-field",
                     "sw-language", "sw-tree", "sw-sortable",
                     "sw-ai-copilot", "sw-advanced-selection",
                     "sw-many-to-many", "sw-one-to-many", "sw-block-parent",
                     "sw-chart", "sw-filter", "sw-base-filter", "sw-boolean-filter",
                     "sw-date-filter", "sw-existence-filter", "sw-multi-tag",
                     "sw-generic"]
        return [n for n in all_names if any(n.startswith(p) or n == p for p in prefixes)]

    elif batch_name == "sw-cms":
        return [n for n in all_names if n.startswith("sw-cms-")]

    elif batch_name == "sw-bulk":
        prefixes = ["sw-bulk-edit", "sw-customer", "sw-product", "sw-order"]
        return [n for n in all_names if any(n.startswith(p) for p in prefixes)]

    elif batch_name == "sw-catset":
        prefixes = ["sw-category", "sw-settings", "sw-flow"]
        return [n for n in all_names if any(n.startswith(p) for p in prefixes)]

    elif batch_name == "sw-ext":
        prefixes = ["sw-extension", "sw-import-export", "sw-media", "sw-mail",
                     "sw-duplicated-media"]
        return [n for n in all_names if any(n.startswith(p) for p in prefixes)]

    elif batch_name == "sw-cond":
        prefixes = ["sw-condition", "sw-custom-field", "sw-first-run-wizard"]
        return [n for n in all_names if any(n.startswith(p) for p in prefixes)]

    elif batch_name == "sw-rest":
        # All not covered by other batches
        covered = set()
        for b in ["sw-core", "sw-form", "sw-data", "sw-cms", "sw-bulk", "sw-catset", "sw-ext", "sw-cond"]:
            covered.update(get_batch_components(b, json_data))
        return [n for n in all_names if n not in covered]

    return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", help="Batch to process: mt, sw-core, sw-form, sw-data, sw-cms, sw-bulk, sw-catset, sw-ext, sw-cond, sw-rest")
    parser.add_argument("--component", help="Single component to process")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be generated")
    args = parser.parse_args()

    json_data = load_json_data()

    if args.component:
        comp = args.component
        if comp.startswith("mt-"):
            # Find vue file
            for name, vue_file in get_mt_components():
                if name == comp:
                    doc = generate_mt_doc(name, vue_file)
                    out = os.path.join(OUTPUT_DIR, f"{name}.md")
                    with open(out, 'w') as f:
                        f.write(doc)
                    print(f"Generated: {out}")
                    return
            print(f"mt-* component not found: {comp}")
        else:
            doc = generate_sw_doc(comp, json_data)
            out = os.path.join(OUTPUT_DIR, f"{comp}.md")
            with open(out, 'w') as f:
                f.write(doc)
            print(f"Generated: {out}")
        return

    if args.batch == "mt":
        components = get_mt_components()
        print(f"Processing {len(components)} mt-* components...")
        for name, vue_file in components:
            if args.dry_run:
                print(f"  Would generate: {name}")
                continue
            doc = generate_mt_doc(name, vue_file)
            out = os.path.join(OUTPUT_DIR, f"{name}.md")
            with open(out, 'w') as f:
                f.write(doc)
            print(f"  Generated: {name}")
        print(f"Done: {len(components)} mt-* docs generated.")
        return

    if args.batch and args.batch.startswith("sw-"):
        components = get_batch_components(args.batch, json_data)
        print(f"Processing {len(components)} sw-* components for batch '{args.batch}'...")
        for comp_name in components:
            if args.dry_run:
                print(f"  Would generate: {comp_name}")
                continue
            doc = generate_sw_doc(comp_name, json_data)
            out = os.path.join(OUTPUT_DIR, f"{comp_name}.md")
            with open(out, 'w') as f:
                f.write(doc)
            print(f"  Generated: {comp_name}")
        print(f"Done: {len(components)} docs generated for batch '{args.batch}'.")
        return

    if args.batch:
        print(f"Unknown batch: {args.batch}")
        sys.exit(1)

    parser.print_help()


if __name__ == "__main__":
    main()
