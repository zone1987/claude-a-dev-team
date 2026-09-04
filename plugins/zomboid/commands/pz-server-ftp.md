---
name: pz-server-ftp
description: Inspect or update a live Project Zomboid dedicated server over FTP - fetch logs and saves, upload config, without ever printing the credentials.
argument-hint: <what to do> (e.g. "fetch today's logs", "upload servertest.ini")
allowed-tools: Read, Glob, Grep, Bash, Write
model: sonnet
---

# /pz-server-ftp

Reach a hosted dedicated server over plain FTP to do what $ARGUMENTS asks: pull logs for diagnosis,
download a save for analysis, or push a config file back up.

Use `scripts/pz_ftp.sh` rather than hand-rolled `curl` calls. It keeps the credentials in one place,
verifies every upload, and prints nothing that identifies the server or the account.

## Credentials — never printed, never committed

Four environment variables, values supplied by the operator from a gitignored location (a DDEV
`config.local.yaml`, a shell profile, a secret store):

| Variable | Holds | Fallback |
|---|---|---|
| `PZ_FTP_HOST` | hostname or IP | `FTP_HOST` |
| `PZ_FTP_PORT` | port, usually 21 | `FTP_PORT` |
| `PZ_FTP_USER` | username | `FTP_USER` |
| `PZ_FTP_PASS` | password | `FTP_PASS` |

**Absolute rules, no exceptions:**

- **Never print a value.** Not with `echo`, `printf`, `env`, `printenv` or `set`; not as a length, a
  prefix, a masked form or a character count; not inside an error message, a commit message or a
  report. Report only whether a variable is *set*.
- **Never pass a value as a command argument.** An argument is world-readable through `ps` and lands
  in shell history. The script feeds them to curl through `--config` on a process substitution for
  exactly this reason — keep it that way.
- **Never write a value to a file**, including a scratch file, a generated script or a `.netrc`.
- **Never commit them**, and never move them into a tracked config file. If a task seems to need
  that, stop and say so.

## Establish first

1. **Read or write?** Reading is safe at any time. Writing needs the game server **stopped** — a
   running server keeps state in memory and overwrites files on its next save, discarding the upload
   silently. Confirm it is stopped before any `put`.
2. **Which paths?** The install root holds `server-console.txt`, `Logs/`, `Server/` (the INI and
   sandbox vars) and `Saves/Multiplayer/<world>/`. Confirm the world name rather than assuming
   `servertest`.
3. **Is there a backup?** Before overwriting anything, `get` the current remote file to a local
   backup directory and say where it is.

## Commands

```bash
scripts/pz_ftp.sh check                    # connection test, prints "connection ok" only
scripts/pz_ftp.sh ls   /Server             # long-format listing
scripts/pz_ftp.sh get  <remote> <local>    # download one file
scripts/pz_ftp.sh put  <local> <remote>    # upload, then verify byte-for-byte
scripts/pz_ftp.sh tail /server-console.txt 8192   # last N bytes, no full download
scripts/pz_ftp.sh logs <local-dir>         # server-console.txt plus every Logs/*.txt
```

Run it wherever the variables live. With DDEV that means inside the container, from the project root:
`ddev exec 'bash <path>/pz_ftp.sh check'`.

`tail` matters for diagnosis: a `server-console.txt` can be hundreds of KB, and the interesting part
is the end. Pull the tail before pulling the whole file.

## Writing safely

1. `get` the remote file into a timestamped local backup directory.
2. `diff` it against the local version so the change set is known and stated — never upload a file
   whose differences you have not read.
3. `put` it. The script re-downloads and compares; a mismatch is a hard failure and means **do not
   start the server**.
4. Re-read the changed keys from the remote file and quote the values back.

## What not to do

- Do not upload a whole save folder over a live one. A local copy is a snapshot; the server has
  written since, and a bulk upload silently reverts progress. Upload the specific files that changed.
- Do not delete remote files unless the operator asked for that file by name.
- Do not fetch a whole `map/` tree over FTP — hundreds of thousands of small files is hours of
  round-trips. Ask the operator for an archive instead.

## Close by reporting

What was read or written, the remote paths, the backup location, the verification result, and — for a
write — the changed keys with their new values read back **from the server**. Say explicitly that the
server may be started again, or why it may not.

Print no host, port, username or password at any point.
