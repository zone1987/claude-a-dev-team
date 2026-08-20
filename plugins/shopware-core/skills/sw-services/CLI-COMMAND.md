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

→ Argumente/Optionen, Progress, Beispiele: [CLI-COMMAND-COMMANDS.md](CLI-COMMAND-COMMANDS.md)
→ Gerüst: [examples/CustomCommand.php](examples/CustomCommand.php)
