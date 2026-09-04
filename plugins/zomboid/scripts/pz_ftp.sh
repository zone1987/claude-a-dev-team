#!/usr/bin/env bash
# Read and write a Project Zomboid dedicated-server filesystem over plain FTP.
#
# Credentials come from four environment variables and are never printed, logged,
# echoed, or written to a file by this script:
#
#   PZ_FTP_HOST   hostname or IP        (fallback: FTP_HOST)
#   PZ_FTP_PORT   port, usually 21      (fallback: FTP_PORT)
#   PZ_FTP_USER   username              (fallback: FTP_USER)
#   PZ_FTP_PASS   password              (fallback: FTP_PASS)
#
# The fallbacks exist because a host panel often provisions the unprefixed names.
# Provide them from a gitignored place — a DDEV `config.local.yaml`, a shell
# profile, a secret store. Never commit them and never pass them as arguments:
# an argument shows up in `ps`, an environment variable does not.
#
# Usage:
#   pz_ftp.sh check                       verify the connection, print nothing secret
#   pz_ftp.sh ls   <remote-dir>           list a directory (long format)
#   pz_ftp.sh get  <remote> <local>       download one file
#   pz_ftp.sh put  <local> <remote>       upload one file, verifying afterwards
#   pz_ftp.sh tail <remote> [bytes]       print the last N bytes (default 8192)
#   pz_ftp.sh logs <local-dir>            fetch server-console.txt and Logs/*
#
# `put` re-downloads the file and compares it byte-for-byte; it fails loudly if
# the upload did not land intact. Stop the game server before writing anything
# under Saves/ or Server/ — a running server holds state in memory and will
# overwrite the file on its next save.
set -euo pipefail

HOST="${PZ_FTP_HOST:-${FTP_HOST:-}}"
PORT="${PZ_FTP_PORT:-${FTP_PORT:-21}}"
USER="${PZ_FTP_USER:-${FTP_USER:-}}"
PASS="${PZ_FTP_PASS:-${FTP_PASS:-}}"

die() { printf 'pz_ftp: %s\n' "$1" >&2; exit 1; }

for v in HOST PORT USER PASS; do
    [ -n "${!v}" ] || die "environment variable PZ_FTP_$v (or FTP_$v) is not set"
done
command -v curl >/dev/null || die "curl is required"

# All credential handling stays inside this function. Callers pass only paths.
#
# The password goes in through a config file on stdin, not through --user: an
# argument is visible to every process on the box via `ps`, and it lands in shell
# history. The file descriptor is created per call and closed with the process.
# --ftp-pasv is explicit because many game hosts refuse active mode.
# -sS keeps curl quiet but still reports errors.
_curl() {
    curl -sS --ftp-pasv --connect-timeout 20 --max-time 300 \
         --config <(printf 'user = "%s:%s"\n' "$USER" "$PASS") "$@"
}
_url() { printf 'ftp://%s:%s%s' "$HOST" "$PORT" "$1"; }

cmd="${1:-}"; shift || true

case "$cmd" in
check)
    # A plain directory listing, not --list-only: some hosts answer NLST with 502
    # while LIST works fine. Output is discarded; only reachability matters here.
    _curl "$(_url /)" >/dev/null
    # Deliberately prints no host, port or username: those identify the server and
    # the account, and this output ends up in transcripts and CI logs.
    printf 'connection ok\n'
    ;;
ls)
    [ $# -ge 1 ] || die "usage: pz_ftp.sh ls <remote-dir>"
    d="$1"; [ "${d: -1}" = "/" ] || d="$d/"
    _curl "$(_url "$d")"
    ;;
get)
    [ $# -ge 2 ] || die "usage: pz_ftp.sh get <remote> <local>"
    mkdir -p "$(dirname "$2")"
    _curl "$(_url "$1")" -o "$2"
    printf 'got %s -> %s (%s bytes)\n' "$1" "$2" "$(wc -c <"$2" | tr -d ' ')"
    ;;
put)
    [ $# -ge 2 ] || die "usage: pz_ftp.sh put <local> <remote>"
    [ -f "$1" ] || die "local file not found: $1"
    _curl -T "$1" "$(_url "$2")"
    # Verify rather than trust: a silent partial write is the failure that hurts.
    tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT
    _curl "$(_url "$2")" -o "$tmp"
    if cmp -s "$1" "$tmp"; then
        printf 'put %s -> %s (%s bytes, verified byte-identical)\n' \
               "$1" "$2" "$(wc -c <"$1" | tr -d ' ')"
    else
        die "upload of $2 does NOT match the local file - do not start the server"
    fi
    ;;
tail)
    [ $# -ge 1 ] || die "usage: pz_ftp.sh tail <remote> [bytes]"
    n="${2:-8192}"
    _curl -r "-$n" "$(_url "$1")"
    ;;
logs)
    [ $# -ge 1 ] || die "usage: pz_ftp.sh logs <local-dir>"
    out="$1"; mkdir -p "$out/Logs"
    _curl "$(_url /server-console.txt)" -o "$out/server-console.txt" || true
    # The Logs listing is long format; the filename is the last field.
    _curl "$(_url /Logs/)" | awk '{print $NF}' | grep -v '^$' | while read -r f; do
        case "$f" in
            *.txt) _curl "$(_url "/Logs/$f")" -o "$out/Logs/$f" && printf '  %s\n' "$f" ;;
        esac
    done
    printf 'logs written to %s\n' "$out"
    ;;
*)
    sed -n '3,30p' "$0" | sed 's/^# \{0,1\}//'
    exit 1
    ;;
esac
