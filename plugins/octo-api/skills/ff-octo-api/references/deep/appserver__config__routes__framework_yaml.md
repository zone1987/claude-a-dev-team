# config/routes/framework.yaml (`ResubmissionAppServer/config/routes/framework.yaml`)

## Zweck
Symfony-Standard: bindet im `dev`-Env die Error-Preview-Routen ein (`/_error`).

## Inhalt
- `when@dev: _errors → @FrameworkBundle/.../errors.php, prefix /_error`.

## Bezüge
Symfony FrameworkBundle (Boilerplate).
