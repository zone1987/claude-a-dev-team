---
name: sw-cli-command
description: >
  Eigene CLI-Commands (bin/console) in einem Shopware-6-Plugin: Symfony-Command registrieren, Argumente/Optionen,
  SymfonyStyle-Output, Naming-Konvention. Trigger: "bin/console command", "CLI command", "Konsolenbefehl",
  "console.command", "eigener Command", "AsCommand", "command argument option". Shopware 6.7. Scaffolder: /sw-command-create.
---

# Shopware 6 — CLI-Command

Ein Plugin-Command ist ein normaler Symfony-Command, registriert via `#[AsCommand]` (oder `console.command`-Tag).
Namens-Konvention `vendor:domain:action`, z.B. `ff:content:import`.

```php
#[AsCommand(name: 'ff:content:import', description: 'Importiert Inhalte')]
class ImportCommand extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $io = new SymfonyStyle($input, $output);
        $io->success('Fertig');
        return Command::SUCCESS;
    }
}
```

Dependencies (Repositories/Services) per Constructor-Injection. Lang laufende Imports ggf. in MessageQueue (`sw-message-queue`)
oder als ScheduledTask (`sw-scheduled-task`, in `shopware-framework`).

→ Argumente/Optionen, Progress, Beispiele: [references/commands.md](references/commands.md)
→ Gerüst: [examples/CustomCommand.php](examples/CustomCommand.php)
