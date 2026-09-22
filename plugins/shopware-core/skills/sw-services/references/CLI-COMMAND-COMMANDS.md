# Custom Console Commands

## Contents

- [Overview](#overview)
- [Command Class](#command-class)
- [Service Registration](#service-registration)
- [Command Naming Convention](#command-naming-convention)
- [Running Commands](#running-commands)
- [Progress Bar for Long-Running Commands](#progress-bar-for-long-running-commands)

## Overview

Plugins can register custom CLI commands using Symfony's command system. Without
`autoconfigure` — the standard for new plugins — the command is registered explicitly in
`services/commands.php` and carries its own `console.command` tag:

```php
$services->set(MyCommand::class)
    ->args([service('product.repository')])
    ->tag('console.command');
```

Older plugins rely on `autoconfigure="true"` in `services.xml` to discover them; see
[DEPENDENCY-INJECTION.md](DEPENDENCY-INJECTION.md).

## Command Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Command;

use {PluginNamespace}\Framework\Log\Package;   // the plugin's OWN attribute
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Style\SymfonyStyle;

/**
 * @class ImportDataCommand
 * @package FfContentPlus\Command
 */
#[AsCommand(
    name: 'ff:content-plus:import',
    description: 'Import content data from external source',
)]
#[Package('{PluginName}.{Area}')]
class ImportDataCommand extends Command
{
    /**
     * @param MyImportService $importService
     */
    public function __construct(
        private readonly MyImportService $importService,
    ) {
        parent::__construct();
    }

    /**
     * @return void
     */
    protected function configure(): void
    {
        $this->addArgument('source', InputArgument::REQUIRED, 'Source file path');
        $this->addOption('dry-run', 'd', InputOption::VALUE_NONE, 'Run without writing changes');
        $this->addOption('limit', 'l', InputOption::VALUE_REQUIRED, 'Limit number of items', '0');
    }

    /**
     * @param InputInterface $input
     * @param OutputInterface $output
     * @return int
     */
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $io = new SymfonyStyle($input, $output);
        $source = $input->getArgument('source');
        $dryRun = $input->getOption('dry-run');
        $limit = (int) $input->getOption('limit');

        $io->title('Importing data from: ' . $source);

        try {
            $count = $this->importService->import($source, $dryRun, $limit);
            $io->success(\sprintf('Successfully imported %d items.', $count));

            return Command::SUCCESS;
        } catch (\Exception $e) {
            $io->error($e->getMessage());

            return Command::FAILURE;
        }
    }
}
```

## Service Registration

Older plugins with `autoconfigure="true"` had the command registered for them:

**New plugins do not use `autoconfigure`** (→ [DEPENDENCY-INJECTION.md](DEPENDENCY-INJECTION.md)),
so the tag is set by hand. Forgetting it is silent: the class exists, the service is
registered, and nothing ever calls it.

```xml
<service id="FfContentPlus\Command\ImportDataCommand"/>
```

Without autoconfigure, add the tag explicitly:

```xml
<service id="FfContentPlus\Command\ImportDataCommand">
    <tag name="console.command"/>
</service>
```

## Command Naming Convention

Plugin commands follow the pattern: `{vendor}:{plugin-kebab}:{action}`

Examples:
- `ff:content-plus:import`
- `ff:content-plus:cleanup`
- `adt:product-export:sync`

## Running Commands

```bash
# Via DDEV
ddev exec bin/console ff:content-plus:import /path/to/file.csv

# With options
ddev exec bin/console ff:content-plus:import /path/to/file.csv --dry-run --limit=100
```

## Progress Bar for Long-Running Commands

```php
use Symfony\Component\Console\Helper\ProgressBar;

protected function execute(InputInterface $input, OutputInterface $output): int
{
    $items = $this->getItems();
    $progressBar = new ProgressBar($output, \count($items));
    $progressBar->start();

    foreach ($items as $item) {
        $this->process($item);
        $progressBar->advance();
    }

    $progressBar->finish();
    $output->writeln('');

    return Command::SUCCESS;
}
```
