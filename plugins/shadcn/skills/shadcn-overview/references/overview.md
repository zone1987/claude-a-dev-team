# shadcn/ui — Detailed Overview

## What it is

shadcn/ui is a set of beautifully-designed, accessible components **and** a code
distribution platform. It works with your favourite frameworks and AI models.
It is Open Source and uses Open Code.

## Open Code

- Full Transparency: see exactly how each component is built.
- Easy Customisation: modify any part to fit your design and functionality
  requirements.
- AI Integration: LLMs can read, understand, and even improve your components.

FAQ: _How do I pull upstream updates?_
shadcn/ui follows a headless component architecture. The core can receive fixes
by updating dependencies (radix-ui, input-otp, etc.). The topmost layer —
closest to your design system — is not coupled to the library implementation.
It stays open for modification.

## Composition

All components share a common composable interface. If a needed component does
not exist, shadcn brings it in, makes it composable, and adjusts its style to
match the rest of the design system.

## Distribution

- **Schema:** flat-file structure defining components, their dependencies, and
  properties.
- **CLI:** command-line tool to distribute and install components across projects
  with cross-framework support.

The schema can be used to distribute your own components to other projects or
have AI generate completely new ones based on the existing schema.

## Beautiful Defaults

Good out-of-the-box, unified design, easily customisable.

## AI-Ready

An AI model can learn how your components work and suggest improvements or
create new components that integrate with your existing design.

## Base UI vs Radix UI toggle

When running `npx shadcn@latest init`, select a base:

```bash
npx shadcn@latest init -b radix   # default, @radix-ui/* / radix-ui package
npx shadcn@latest init -b base    # @base-ui-components/react
```

Key difference:
- Radix: `asChild` prop pattern, forwardRef removed in v4 (use React 19 ref prop)
- Base: `ButtonPrimitive` from `@base-ui/react/button`; always applies
  `role="button"` — do NOT use for links; use `buttonVariants` + `<a>` instead

Source: `/tmp/shadcn-repo/apps/v4/content/docs/(root)/index.mdx`
