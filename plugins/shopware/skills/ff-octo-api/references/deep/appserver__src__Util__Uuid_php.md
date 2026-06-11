# Uuid (AppServer) (`ResubmissionAppServer/src/Util/Uuid.php`)

## Zweck
UUID-Hilfsklasse des AppServers. Stellt insbesondere `fromStringToHex` bereit — **identische deterministische ID-Logik wie Shopware** (md5-Hash → Hex), damit AppServer-generierte IDs zu den Plugin-IDs passen.

## Typ & Vererbung
- Namespace `App\Util`, `class Uuid extends Symfony\Component\Uid\Uuid`, `declare(strict_types=1)`.

## Konstanten
- `VALID_PATTERN` = `^[0-9a-f]{32}$`.

## Methoden
- `static hashBinary(data, algo='xxh128'): string` — binärer Hash (nicht kryptografisch).
- `static fromBytesToHex(bytes): string` — 16-Byte → 32-Hex (validiert Länge + Pattern).
- `static fromStringToHex(string): string` — **md5**-Hash des Strings → Hex (entspricht Shopware `Uuid::fromStringToHex`).
- `static isValidUuid(id): bool`.
- `static transformToRfc4122(uuid): string` — Hex → RFC-4122-Format.

## Besonderheiten / Fallstricke
- **`fromStringToHex` nutzt md5** (nicht den Default-Algo `xxh128`) — kritisch für die Übereinstimmung der deterministischen Produkt-/Option-IDs mit dem Plugin. Bei Änderung würde die Cross-Repo-ID-Konsistenz brechen.

## Bezüge
`Service/AdminApiClient.php` (`addProduct` ID-Berechnung), FfOctoApi `Shopware\Core\Framework\Uuid\Uuid`, `../appserver-integration.md`.
