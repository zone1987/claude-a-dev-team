<?php declare(strict_types=1);

namespace {PluginName};

use {PluginName}\Core\Framework\Config\PluginLoggerTrait;
use Exception;
use Shopware\Core\Framework\Plugin;
use Symfony\Component\DependencyInjection\ContainerBuilder;

/**
 * @class {PluginName}
 * @package {PluginName}
 */
class {PluginName} extends Plugin
{

    use PluginLoggerTrait;

    /**
     * @param ContainerBuilder $container
     * @return void
     * @throws Exception
     */
    public function build(ContainerBuilder $container): void
    {
        parent::build($container);

        $this->registerPluginLogger($container, $this->getPath());
    }
}
