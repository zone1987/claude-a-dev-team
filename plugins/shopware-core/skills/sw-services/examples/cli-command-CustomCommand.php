<?php declare(strict_types=1);

namespace FfContentPlus\Command;

use Shopware\Core\Framework\Log\Package;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Input\InputOption;
use Symfony\Component\Console\Output\OutputInterface;

/**
 * @class FfContentPlusCommand
 * @package FfContentPlus\Command
 */
#[AsCommand(
    name: 'ff:content-plus:example',
    description: 'Example CLI command for Content Plus',
)]
#[Package('custom-plugins')]
class FfContentPlusCommand extends Command
{
    /**
     * @return void
     */
    protected function configure(): void
    {
        $this->addArgument('name', InputArgument::REQUIRED, 'The item name');
        $this->addOption('force', 'f', InputOption::VALUE_NONE, 'Force execution');
    }

    /**
     * @param InputInterface $input
     * @param OutputInterface $output
     * @return int
     */
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $name = $input->getArgument('name');
        $force = $input->getOption('force');

        $output->writeln(sprintf('Processing: %s', $name));

        return Command::SUCCESS;
    }
}
