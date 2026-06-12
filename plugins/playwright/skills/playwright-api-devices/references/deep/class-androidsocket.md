# Playwright API: AndroidSocket

> **EXPERIMENTAL** — AndroidSocket is part of Playwright's experimental Android (ADB) support.

`AndroidSocket` represents an open bidirectional communication channel with a process
launched on an Android device via `androidDevice.open(command)`. It is conceptually similar
to a Node.js `net.Socket` and exposes the same pattern of `data` / `close` events plus
`write()` / `close()` methods.

```js
const socket = await device.open('logcat -T 1');
socket.on('data', (buf) => process.stdout.write(buf.toString()));
// … later …
await socket.close();
```

---

## Events

### androidSocket.on('close')

Emitted when the socket is closed — either by calling `socket.close()` or because
the remote process has exited.

**Event data:** none

**Signature:**
```js
androidSocket.on('close', () => { /* ... */ });
```

**Example:**
```js
socket.on('close', () => console.log('Socket closed'));
```

---

### androidSocket.on('data')

Emitted each time data arrives from the remote process.

**Event data:** `Buffer` — the raw bytes received

**Signature:**
```js
androidSocket.on('data', (data: Buffer) => { /* ... */ });
```

**Example:**
```js
socket.on('data', (chunk) => {
  console.log('Received:', chunk.toString('utf8'));
});
```

---

## Methods

### androidSocket.close()

Closes the socket and terminates the associated remote process.
After calling this method the socket must not be used.

**Signature:**
```js
await androidSocket.close();
```

**Parameters:** none

**Returns:** `Promise<void>`

**Example:**
```js
await socket.close();
```

---

### androidSocket.write(data)

Sends raw bytes to the remote process over the socket.

**Signature:**
```js
await androidSocket.write(data);
```

**Parameters:**

| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| `data` | Buffer | yes | — | Raw bytes to write to the socket |

**Returns:** `Promise<void>`

**Example:**
```js
const { Buffer } = require('buffer');
await socket.write(Buffer.from('GET / HTTP/1.0\r\n\r\n', 'utf8'));
```

---

## Full Usage Example

```js
const { android } = require('playwright');

(async () => {
  const [device] = await android.devices();

  // Open an interactive shell process
  const socket = await device.open('cat /proc/version');

  const chunks = [];
  socket.on('data', (buf) => chunks.push(buf));
  await new Promise((resolve) => socket.on('close', resolve));

  console.log(Buffer.concat(chunks).toString('utf8'));
})();
```

---

## Notes

- `AndroidSocket` has **no properties**.
- Instances are created exclusively via `androidDevice.open(command)` — there is no constructor.
- The `data` event may fire multiple times for a single logical message; callers must buffer if needed.
- The socket is half-duplex at the protocol level: write is fire-and-forget; the response is received
  through the `data` event.

---

## Manifest

| Attribute | Value |
|---|---|
| Methods | 2 (`close`, `write`) |
| Properties | 0 |
| Events | 2 (`close`, `data`) |

**Fazit:** `AndroidSocket` ist ein schlankes Wrapper-Objekt um eine ADB-Shell-Verbindung.
Es ermoeglicht bidirektionale Kommunikation mit beliebigen Geraetp rozessen via `write()` und
dem `data`-Event. Typische Anwendungsfaelle sind: Logcat-Streaming, Custom-Shell-Protokolle
und direktes ADB-Forwarding.

---

Source: https://playwright.dev/docs/api/class-androidsocket
