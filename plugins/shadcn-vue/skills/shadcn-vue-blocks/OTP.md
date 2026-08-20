# shadcn-vue OTP Blocks

Diese 5 vorgefertigten Blöcke bieten vollständige One-Time-Password / Verifizierungscode-Seiten für Vue-3-Anwendungen. Jeder Block nutzt die `InputOTP`-Komponente von shadcn-vue für ein 6-stelliges PIN-Eingabefeld, kombiniert mit einem Verify-Button und einem Resend-Link. Die Blöcke unterscheiden sich im Layout (Card, Split-Screen mit Bild, Muted-Background, minimalistische Form) und können direkt via `npx shadcn-vue@latest add <block>` installiert werden.

Vollständiger Quellcode aller Blöcke: `OTP-01-03.md` (otp-01 bis otp-03) und `OTP-04-05.md` (otp-04, otp-05).

---

## otp-01: Einfaches OTP-Formular in Card

**Installation:**
```bash
npx shadcn-vue@latest add otp-01
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Zentriertes Layout mit `Card`-Wrapper. Der 6-stellige OTP-Input wird als zusammenhängende Gruppe (`InputOTPGroup`) mit je einem Slot pro Ziffer dargestellt. Darunter Verify-Button und Resend-Link.

---

## otp-02: OTP-Formular mit Split-Screen und Bild

**Installation:**
```bash
npx shadcn-vue@latest add otp-02
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Zweispaltiges Layout: links das OTP-Formular (volle Breite < lg, halbe Breite >= lg), rechts ein Platzhalterbild. Der OTP-Input ist in drei Zweier-Gruppen mit `InputOTPSeparator` aufgeteilt (2-2-2). Heading und Beschreibung zentriert über dem Input.

---

## otp-03: OTP-Formular mit gemutedtem Hintergrund und Logo

**Installation:**
```bash
npx shadcn-vue@latest add otp-03
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Muted-Hintergrund mit Logo-Link oben (GalleryVerticalEnd-Icon + "Acme Inc."). OTP-Formular in einer `Card` mit zentriertem Header. 6-stelliger Input als eine Gruppe ohne Separatoren. Verify-Button und Resend-Link unterhalb.

---

## otp-04: OTP-Formular mit Bild-Panel und Privacy-Hinweis

**Installation:**
```bash
npx shadcn-vue@latest add otp-04
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Zweispaltiges Card-Layout (links Formular, rechts Bild, nur ab md sichtbar). OTP-Input mit `InputOTPSeparator` als 3-3-Gruppen-Split. Darunter Privacy/ToS-Hinweis. Maximale Containerbreite 3xl.

---

## otp-05: Minimalistisches OTP-Formular mit Logo und großen Slots

**Installation:**
```bash
npx shadcn-vue@latest add otp-05
```

**Files:**
- `page.vue`
- `components/OTPForm.vue`

Kartenloser, minimalistischer Aufbau mit Logo-Link oben (GalleryVerticalEnd). Der OTP-Input verwendet extra-große Slots (h-16 w-12, text-xl) in 3-3-Gruppen-Split mit `InputOTPSeparator`. Resend-Link direkt unter dem Input, Verify-Button separat darunter. Privacy/ToS-Hinweis am Ende.
