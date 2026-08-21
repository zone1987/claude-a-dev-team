# InputOTP — Installation

## CLI

```bash
npx shadcn-vue@latest add input-otp
```

## Manual

### Dependencies

```bash
npm install vue-input-otp
```

### Steps

1. Copy source code (see `references/source.md`) to `components/ui/input-otp/`
2. Adjust import paths

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

Sources:
- https://vue-input-otp.vercel.app/
- https://github.com/unovue/shadcn-vue/tree/dev/apps/v4/registry/new-york-v4/ui/input-otp
