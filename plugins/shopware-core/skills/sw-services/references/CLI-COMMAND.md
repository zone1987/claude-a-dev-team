# Shopware 6 — CLI Command

A plugin command is a plain Symfony command, registered via `#[AsCommand]` (or the `console.command` tag).
Naming convention `vendor:domain:action`, e.g. `ff:content:import`.

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

Inject dependencies (repositories/services) through the constructor. Move long-running imports into the message queue (`sw-message-queue`)
or a scheduled task (`sw-scheduled-task`, in `shopware-framework`) where appropriate.

→ Arguments/options, progress, examples: [CLI-COMMAND-COMMANDS.md](CLI-COMMAND-COMMANDS.md)
→ Skeleton: [examples/CustomCommand.php](examples/CustomCommand.php)
