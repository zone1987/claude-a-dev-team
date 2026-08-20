#!/usr/bin/env python3
"""Resolve the Ventrata OpenAPI specification URL.

The specification lives in a GitBook file blob whose URL is content-addressed: the hash
changes whenever Ventrata publishes an update. Never hardcode it. Every documentation page
that transcludes the spec carries the full URL, so resolve it from a page instead.

Usage:
    resolve_blob.py --print-url          print the resolved URL
    resolve_blob.py --download PATH      download the spec to PATH, print URL + sha256
"""
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import ssl
import subprocess
import sys
import urllib.request

DOC_PAGES = (
    "https://docs.ventrata.com/octo-core/products.md",
    "https://docs.ventrata.com/octo-core/bookings.md",
    "https://docs.ventrata.com/capabilities/pricing.md",
)
BLOB_RE = re.compile(
    r"https://\d+-files\.gitbook\.io/[^)\"'\s]*openapi\.yaml\?alt=media"
)
TIMEOUT = 30


def _ssl_context() -> ssl.SSLContext | None:
    """Prefer certifi's bundle: a stock macOS python3 often has no usable CA store."""
    try:
        import certifi

        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return None


def fetch(url: str) -> bytes:
    """Fetch over HTTPS, falling back to curl when the CA store is unusable."""
    req = urllib.request.Request(url, headers={"User-Agent": "octo-api-plugin/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=_ssl_context()) as r:
            return r.read()
    except ssl.SSLError:
        pass
    except urllib.error.URLError as exc:
        if not isinstance(exc.reason, ssl.SSLError):
            raise
    curl = shutil.which("curl")
    if not curl:
        raise RuntimeError("TLS verification failed and curl is unavailable")
    return subprocess.run(
        [curl, "-sSL", "--max-time", str(TIMEOUT), url],
        check=True,
        capture_output=True,
    ).stdout


def resolve() -> str:
    """Return the spec URL, trying several pages so one page edit cannot break us."""
    errors = []
    for page in DOC_PAGES:
        try:
            m = BLOB_RE.search(fetch(page).decode("utf-8", "replace"))
        except Exception as exc:  # network, DNS, HTTP
            errors.append(f"{page}: {exc}")
            continue
        if m:
            return m.group(0)
        errors.append(f"{page}: no blob URL found")
    raise SystemExit("could not resolve the spec URL:\n  " + "\n  ".join(errors))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--print-url", action="store_true")
    ap.add_argument("--download", metavar="PATH")
    args = ap.parse_args()

    url = resolve()
    if args.download:
        data = fetch(url)
        with open(args.download, "wb") as fh:
            fh.write(data)
        print(url)
        print(hashlib.sha256(data).hexdigest())
    else:
        print(url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
