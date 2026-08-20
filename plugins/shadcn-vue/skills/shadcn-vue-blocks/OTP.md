# shadcn-vue OTP Blocks

These 5 prebuilt blocks provide complete one-time-password / verification code pages for Vue 3 applications. Each block uses the shadcn-vue `InputOTP` component for a 6-digit PIN input field, combined with a verify button and a resend link. The blocks differ in layout (card, split screen with image, muted background, minimalist form) and can be installed directly via `npx shadcn-vue@latest add <block>`.

Complete source code of all blocks: `OTP-01-03.md` (otp-01 through otp-03) and `OTP-04-05.md` (otp-04, otp-05).

---

## otp-01: simple OTP form in a card

**Installation:**
```bash
npx shadcn-vue@latest add otp-01
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Centered layout with a `Card` wrapper. The 6-digit OTP input is rendered as one contiguous group (`InputOTPGroup`) with one slot per digit. Below it a verify button and a resend link.

---

## otp-02: OTP form with split screen and image

**Installation:**
```bash
npx shadcn-vue@latest add otp-02
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Two-column layout: the OTP form on the left (full width < lg, half width >= lg), a placeholder image on the right. The OTP input is split into three groups of two with `InputOTPSeparator` (2-2-2). Heading and description centered above the input.

---

## otp-03: OTP form with muted background and logo

**Installation:**
```bash
npx shadcn-vue@latest add otp-03
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Muted background with a logo link at the top (GalleryVerticalEnd icon + "Acme Inc."). OTP form inside a `Card` with a centered header. 6-digit input as a single group without separators. Verify button and resend link below.

---

## otp-04: OTP form with image panel and privacy note

**Installation:**
```bash
npx shadcn-vue@latest add otp-04
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Two-column card layout (form on the left, image on the right, visible from md upwards). OTP input with `InputOTPSeparator` as a 3-3 group split. Below it a privacy/ToS note. Maximum container width 3xl.

---

## otp-05: minimalist OTP form with logo and large slots

**Installation:**
```bash
npx shadcn-vue@latest add otp-05
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Card-less, minimalist structure with a logo link at the top (GalleryVerticalEnd). The OTP input uses extra-large slots (h-16 w-12, text-xl) in a 3-3 group split with `InputOTPSeparator`. Resend link directly under the input, verify button separately below. Privacy/ToS note at the end.
