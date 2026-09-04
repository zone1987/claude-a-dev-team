# File Upload

Custom Shadcn File Upload for React and Tailwind CSS. Enables users to upload files to a server or
application. Ships as a hook (`useFileUpload`), not a compound component.

Free component — no licence key required.

## Contents

- [Installation](#installation)
- [Import](#import)
- [Usage](#usage)
- [Examples (7 total)](#examples-7-total)
- [API Reference](#api-reference)
- [Base UI vs Radix UI](#base-ui-vs-radix-ui)
- [Source](#source)

## Installation

```
pnpm dlx shadcn@latest add @reui/use-file-upload
```

## Import

```tsx
import { useFileUpload } from "@/hooks/use-file-upload"
```

## Usage

```tsx
const [{ files }, { openFileDialog, getInputProps }] = useFileUpload({
  accept: "image/*",
  multiple: false,
})

return (
  <div>
    <Button onClick={openFileDialog}>Upload Image</Button>
    <input {...getInputProps()} className="sr-only" />
    {files.map((file) => (
      <div key={file.id}>{file.file.name}</div>
    ))}
  </div>
)
```

## Examples (7 total)

Titles enumerated upstream: Avatar Upload, Compact Upload, Gallery Upload, Progress Upload, Table
Upload, Image Upload, Sortable Upload.

### Avatar Upload

```tsx
"use client"

import { useFileUpload } from "@/hooks/use-file-upload"
import { Button } from "@/components/ui/button"
import { CircleUserRoundIcon } from "lucide-react"

export function Pattern() {
  const [{ files }, { removeFile, openFileDialog, getInputProps }] = useFileUpload({
    accept: "image/*",
  })
  const previewUrl = files[0]?.preview || null
  const fileName = files[0]?.file.name || null

  return (
    <div className="flex flex-col items-center gap-2">
      <div className="inline-flex items-center gap-2 align-top">
        <div
          className="border-input rounded-md relative flex size-9 shrink-0 items-center justify-center overflow-hidden border"
          aria-label={previewUrl ? "Preview of uploaded image" : "Default user avatar"}
        >
          {previewUrl ? (
            <img className="size-full object-cover" src={previewUrl} alt="Preview of uploaded image" width={32} height={32} />
          ) : (
            <CircleUserRoundIcon className="opacity-60" width="16" height="16" aria-hidden="true" />
          )}
        </div>
        <div className="relative inline-block">
          <Button onClick={openFileDialog} aria-haspopup="dialog">
            {fileName ? "Change image" : "Upload image"}
          </Button>
          <input {...getInputProps()} className="sr-only" aria-label="Upload image file" tabIndex={-1} />
        </div>
      </div>
      {fileName ? (
        <div className="inline-flex gap-2 text-xs">
          <p className="text-muted-foreground truncate" aria-live="polite">{fileName}</p>{" "}
          <button
            onClick={() => removeFile(files[0]?.id)}
            className="text-destructive cursor-pointer font-medium hover:underline"
            aria-label={`Remove ${fileName}`}
          >
            Remove
          </button>
        </div>
      ) : (
        <div className="inline-flex gap-2 text-xs">
          <p className="text-muted-foreground truncate" aria-live="polite">No image attached</p>
        </div>
      )}
    </div>
  )
}
```

### Compact Upload

```tsx
"use client"

import { formatBytes, useFileUpload, type FileWithPreview } from "@/hooks/use-file-upload"
import { Alert, AlertDescription, AlertTitle } from "@/components/reui/alert"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { CircleAlertIcon, FileIcon, PlusIcon, XIcon } from "lucide-react"

interface FileUploadCompactProps {
  maxFiles?: number
  maxSize?: number
  accept?: string
  multiple?: boolean
  className?: string
  onFilesChange?: (files: FileWithPreview[]) => void
}

export function Pattern({
  maxFiles = 3,
  maxSize = 2 * 1024 * 1024, // 2MB
  accept = "image/*",
  multiple = true,
  className,
  onFilesChange,
}: FileUploadCompactProps) {
  const [
    { files, isDragging, errors },
    { removeFile, handleDragEnter, handleDragLeave, handleDragOver, handleDrop, openFileDialog, getInputProps },
  ] = useFileUpload({ maxFiles, maxSize, accept, multiple, onFilesChange })

  // isImage(file) checks file.type.startsWith("image/")
  // Renders a dashed drop zone with an "Add files" button, inline thumbnails
  // (image preview or FileIcon fallback) each with a hover remove button, a
  // "{count}/{maxFiles}" counter, and an Alert (variant="destructive") listing
  // `errors` when non-empty.
}
```

### Gallery Upload

Uses `useFileUpload({ maxFiles: 10, maxSize: 5MB, accept: "image/*", multiple: true, initialFiles })`
seeded with `FileMetadata[]` default images. Renders a large dashed drop zone with an `ImageIcon`,
heading, `formatBytes(maxSize)` hint, and a "Select images" button; below it a stats row
(`Gallery ({files.length}/{maxFiles})`, total size via `formatBytes`, a "Clear all" button calling
`clearFiles()`); then a responsive image grid where each thumbnail shows a loading `Spinner` until
`onLoad`, a hover overlay with a zoom button that opens a `Dialog` image preview and a remove button
calling `removeFile(fileItem.id)`; file name and `formatBytes(fileItem.file.size)` shown per tile; an
`Alert` for `errors`.

### Progress Upload

Wraps `useFileUpload` state in a local `FileUploadItem[]` (`FileWithPreview & { progress: number;
status: "uploading" | "completed" | "error"; error?: string }`) so it can simulate per-file progress
with `setInterval`, occasionally flipping a file to `"error"` (10% chance past 50% progress) with a
`RefreshCwIcon` retry button rendered via `AlertAction`. Uses `Badge` (`success-light`,
`destructive`, `secondary` variants) to summarize completed/failed/uploading counts, and a shadcn
`Progress` bar per uploading file.

### Table Upload

Same `FileUploadItem` pattern as Progress Upload, rendered as rows in a shadcn `Table` (`Name`,
`Type`, `Size`, `Actions` columns). The Name cell draws a circular SVG progress ring around the file
icon while `status === "uploading"`, and a `Badge variant="destructive-light"` next to the name on
error. Actions column offers a download icon button (when `preview` is set), plus a retry
(`RefreshCwIcon`) or remove (`Trash2Icon`) icon button depending on status.

### Image Upload

Manages its own local `ImageFile[]` state (`{ id, file, preview, progress, status, error? }`) rather
than reading `useFileUpload`'s `files` directly — it builds images through a `validateFile` check
(rejects non-image types, files over `maxSize`, or once `images.length >= maxFiles`) and a
`simulateUpload` interval per file. Renders: a top image grid mixing `visibleDefaultImages`
(dismissible seed images) and uploaded `images`, each in a `Card` with a hover remove button; a dashed
`Card` drop zone below the grid with a "Browse File" button and a local `formatBytes` helper (not the
hook's exported one — this example defines its own); then a stacked list of upload-progress `Card`s
showing name, size, `"Uploading... {progress}%"` and a `Progress` bar per in-flight image; and an
`Alert` for `errors`. Props interface: `ImageUploadProps { maxFiles?, maxSize?, accept?, className?,
onImagesChange?, onUploadComplete? }`, with defaults `maxFiles = 10`, `maxSize = 2 * 1024 * 1024`
(2MB), `accept = "image/*"`.

### Sortable Upload

Composes file upload with the **Sortable** component (`@/components/reui/sortable`): imports
`Sortable`, `SortableItem`, `SortableItemHandle` from `@/components/reui/sortable` alongside
`useFileUpload`. Local state types: `ImageFile { id, file, preview, progress, status, error? }` and
`SortableImage { id, src, alt, type: "default" | "uploaded" }`, used to let the user drag-reorder both
seeded default images and freshly uploaded ones in one unified sortable list, each item exposing a
`SortableItemHandle` with a `GripVerticalIcon` and a remove button, plus the same upload-progress
`Card`/`Progress` treatment as Image Upload. Confirms the file-upload and sortable primitives are
meant to be composed directly, with no adapter layer beyond passing the combined item list to
`<Sortable value={...} onValueChange={...} getItemValue={...}>`.

## API Reference

### useFileUpload

A custom hook for managing file upload state and interactions.

```tsx
const [state, actions] = useFileUpload(options)
```

#### Options

| Prop | Type | Default | Description |
|---|---|---|---|
| `maxFiles` | `number` | `Infinity` | Maximum number of files allowed (only when `multiple` is true). |
| `maxSize` | `number` | `Infinity` | Maximum size for each file in bytes. |
| `accept` | `string` | `"*"` | Accepted file types (e.g., `"image/*"`, `".pdf,.docx"`). |
| `multiple` | `boolean` | `false` | Whether to allow multiple file selection. |
| `initialFiles` | `FileMetadata[]` | `[]` | Initial set of files to populate the state. |
| `onFilesChange` | `(files: FileWithPreview[]) => void` | `-` | Callback fired whenever the files list changes. |
| `onFilesAdded` | `(files: FileWithPreview[]) => void` | `-` | Callback fired when new valid files are added. |
| `onError` | `(errors: string[]) => void` | `-` | Callback fired when validation errors occur. |

#### State

| Property | Type | Description |
|---|---|---|
| `files` | `FileWithPreview[]` | The list of currently selected/uploaded files. |
| `isDragging` | `boolean` | Whether a file is currently being dragged over the target area. |
| `errors` | `string[]` | Any current validation error messages. |

#### Actions

| Method | Type | Description |
|---|---|---|
| `addFiles` | `(files: FileList \| File[]) => void` | Manually add files to the state. |
| `removeFile` | `(id: string) => void` | Remove a file by its unique ID. |
| `clearFiles` | `() => void` | Remove all files from the state. |
| `clearErrors` | `() => void` | Clear all current error messages. |
| `openFileDialog` | `() => void` | Programmatically open the browser's file selection dialog. |
| `getInputProps` | `(props?) => InputProps` | Returns props for a hidden `<input>` element. |
| `handleDragEnter` | `(e) => void` | Event handler for the `onDragEnter` event. |
| `handleDragLeave` | `(e) => void` | Event handler for the `onDragLeave` event. |
| `handleDragOver` | `(e) => void` | Event handler for the `onDragOver` event. |
| `handleDrop` | `(e) => void` | Event handler for the `onDrop` event. |

### Types

#### FileMetadata

```ts
type FileMetadata = {
  name: string
  size: number
  type: string
  url: string
  id: string
}
```

#### FileWithPreview

```ts
type FileWithPreview = {
  file: File | FileMetadata
  id: string
  preview?: string
}
```

#### formatBytes

A utility function to format a byte count into a human-readable string (e.g., `1.5 MB`).

```ts
function formatBytes(bytes: number, decimals?: number): string
```

## Base UI vs Radix UI

The Base UI and Radix UI pages are textually identical apart from the "Free Components" marketing
sentence (confirmed by full-file diff). Import path (`@/hooks/use-file-upload`), installation command,
and the full API Reference (Options, State, Actions, Types, `formatBytes`) are unchanged between
builds — this component is a plain hook with no Base UI or Radix UI primitive dependency.

To tell which build a project is on, check `components.json`: `style: "base-nova"` means Base UI,
`style: "radix-nova"` means Radix UI. For this specific component the distinction is immaterial since
it has no underlying primitive-library dependency.

## Source

- Base UI: `docs/components/base/file-upload` — mirror captured 2026-09-04.
- Radix UI: `docs/components/radix/file-upload` — mirror captured 2026-09-04 (marketing-line diff only,
  confirmed by full-file diff; example bodies not independently re-read).
