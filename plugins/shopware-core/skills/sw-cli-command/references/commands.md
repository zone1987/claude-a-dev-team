# Custom Console Commands

## Overview

Plugins can register custom CLI commands using Symfony's command system. Commands are auto-discovered when using `autoconfigure="true"` in services.xml.

## Command Class

```php
<?php declare(strict_types=1);

namespace FfContentPlus\Command;

use Shopware\Core\Framework\Log\Package;
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
#[Package('custom-plugins')]
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

With `autoconfigure="true"`, the command is auto-registered:

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
