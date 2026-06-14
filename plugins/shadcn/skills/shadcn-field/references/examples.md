# Field — Examples

## Example 1 — Demo (Payment Form)

Full payment form with FieldSet, FieldGroup, horizontal checkbox, and Textarea.

```tsx
import { Button } from "@/registry/new-york-v4/ui/button"
import { Checkbox } from "@/registry/new-york-v4/ui/checkbox"
import {
  Field,
  FieldDescription,
  FieldGroup,
  FieldLabel,
  FieldLegend,
  FieldSeparator,
  FieldSet,
} from "@/registry/new-york-v4/ui/field"
import { Input } from "@/registry/new-york-v4/ui/input"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/registry/new-york-v4/ui/select"
import { Textarea } from "@/registry/new-york-v4/ui/textarea"

export default function FieldDemo() {
  return (
    <div className="w-full max-w-md">
      <form>
        <FieldGroup>
          <FieldSet>
            <FieldLegend>Payment Method</FieldLegend>
            <FieldDescription>
              All transactions are secure and encrypted
            </FieldDescription>
            <FieldGroup>
              <Field>
                <FieldLabel htmlFor="card-name">Name on Card</FieldLabel>
                <Input id="card-name" placeholder="Evil Rabbit" required />
              </Field>
              <Field>
                <FieldLabel htmlFor="card-number">Card Number</FieldLabel>
                <Input
                  id="card-number"
                  placeholder="1234 5678 9012 3456"
                  required
                />
                <FieldDescription>
                  Enter your 16-digit card number
                </FieldDescription>
              </Field>
              <div className="grid grid-cols-3 gap-4">
                <Field>
                  <FieldLabel htmlFor="exp-month">Month</FieldLabel>
                  <Select defaultValue="">
                    <SelectTrigger id="exp-month">
                      <SelectValue placeholder="MM" />
                    </SelectTrigger>
                    <SelectContent>
                      {Array.from({ length: 12 }, (_, i) => (
                        <SelectItem
                          key={i + 1}
                          value={String(i + 1).padStart(2, "0")}
                        >
                          {String(i + 1).padStart(2, "0")}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </Field>
                <Field>
                  <FieldLabel htmlFor="exp-year">Year</FieldLabel>
                  <Select defaultValue="">
                    <SelectTrigger id="exp-year">
                      <SelectValue placeholder="YYYY" />
                    </SelectTrigger>
                    <SelectContent>
                      {[2024, 2025, 2026, 2027, 2028, 2029].map((y) => (
                        <SelectItem key={y} value={String(y)}>
                          {y}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </Field>
                <Field>
                  <FieldLabel htmlFor="cvv">CVV</FieldLabel>
                  <Input id="cvv" placeholder="123" required />
                </Field>
              </div>
            </FieldGroup>
          </FieldSet>
          <FieldSeparator />
          <FieldSet>
            <FieldLegend>Billing Address</FieldLegend>
            <FieldGroup>
              <Field orientation="horizontal">
                <Checkbox id="same-as-shipping" defaultChecked />
                <FieldLabel
                  htmlFor="same-as-shipping"
                  className="font-normal"
                >
                  Same as shipping address
                </FieldLabel>
              </Field>
            </FieldGroup>
          </FieldSet>
          <FieldSet>
            <FieldGroup>
              <Field>
                <FieldLabel htmlFor="comments">Comments</FieldLabel>
                <Textarea
                  id="comments"
                  placeholder="Add any additional comments"
                  className="resize-none"
                />
              </Field>
            </FieldGroup>
          </FieldSet>
          <Field orientation="horizontal">
            <Button type="submit">Submit</Button>
            <Button variant="outline" type="button">
              Cancel
            </Button>
          </Field>
        </FieldGroup>
      </form>
    </div>
  )
}
```

## Example 2 — FieldError with Validation

```tsx
<Field data-invalid>
  <FieldLabel htmlFor="username">Username</FieldLabel>
  <Input id="username" aria-invalid defaultValue="taken@name" />
  <FieldError>This username is already taken. Choose another.</FieldError>
</Field>
```

## Example 3 — Horizontal Switch Field

```tsx
import { Switch } from "@/registry/new-york-v4/ui/switch"
import { Field, FieldContent, FieldDescription, FieldLabel } from "@/registry/new-york-v4/ui/field"

<Field orientation="horizontal">
  <Switch id="notifications" />
  <FieldContent>
    <FieldLabel htmlFor="notifications">Email Notifications</FieldLabel>
    <FieldDescription>Receive updates about your account activity.</FieldDescription>
  </FieldContent>
</Field>
```

## Example 4 — FieldSeparator with Label

```tsx
<FieldGroup>
  <Field>
    <FieldLabel htmlFor="email">Email</FieldLabel>
    <Input id="email" type="email" />
  </Field>
  <FieldSeparator>Or continue with</FieldSeparator>
  <Field>
    <FieldLabel htmlFor="phone">Phone</FieldLabel>
    <Input id="phone" type="tel" />
  </Field>
</FieldGroup>
```

---

_Source: `apps/v4/registry/new-york-v4/examples/field-demo.tsx`, `apps/v4/content/docs/components/base/field.mdx`_
