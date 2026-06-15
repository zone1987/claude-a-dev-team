// @/lib/utils — Pflicht-Helfer für shadcn/ui (Datei: src/lib/utils.ts bzw. lib/utils.ts).
// Voraussetzung: npm i clsx tailwind-merge
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

/**
 * Führt bedingte Klassen (clsx) zusammen und löst Tailwind-Konflikte (tailwind-merge) auf.
 * Wird von praktisch jeder shadcn/ui-Komponente importiert.
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
