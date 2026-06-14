# InputOTP — Installation

## CLI

```bash
npx shadcn-vue@latest add input-otp
```

## Manuell

### Abhaengigkeiten

```bash
npm install vue-input-otp
```

### Schritte

1. Quellcode kopieren (siehe `references/source.md`) nach `components/ui/input-otp/`
2. Importpfade anpassen

### Import

```vue
<script setup lang="ts">
import {
  InputOTP,
  InputOTPGroup,
  InputOTPSeparator,
  InputOTPSlot,
} from '@/components/ui/input-otp'
</script>
```

Quellen:
- https://vue-input-otp.vercel.app/
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/input-otp
