---
name: contao-hook
description: Scaffolds a Contao hook listener with #[AsHook] and the exact method signature the chosen hook requires.
argument-hint: <hookName> [--bundle <Bundle>] [--priority <int>]
allowed-tools: Read, Glob, Grep, Write, Edit
model: sonnet
---

# /contao-hook

Create a listener for the hook named in $ARGUMENTS.

Call the Skill tool with "contao-platform" first. **The signature is not negotiable**: each of the 69
hooks takes specific arguments and returns a specific type, and a listener with the wrong signature
fails at runtime rather than at build time. Read the hook's entry in the grouped reference before
writing a line.

## Steps

1. **Resolve the hook name** against the reference. Where the name is unknown, list the near matches
   from the alphabetical index rather than guessing.
2. **Copy the signature exactly**: every argument, its type, and the return type.
3. **Write the listener** at `src/EventListener/<Name>Listener.php` with
   `#[AsHook('<hookName>')]`, adding `priority` where the order against other listeners matters.
4. **Register it** if the bundle does not autoconfigure listeners.

## Output

The file written, the signature used, and the reference file it came from.

Take the signature from the reference, never from memory. Invent nothing.
