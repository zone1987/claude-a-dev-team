<?php declare(strict_types=1);

// src/Resources/config/services.php
//
// Imports only. One file per area under services/ — a single file holding every
// service becomes unreadable, and every merge conflict lands in the same place.

namespace {PluginNamespace}\Resources\config;

use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

return static function (ContainerConfigurator $containerConfigurator): void {
    $containerConfigurator->import('services/definitions.php');
    $containerConfigurator->import('services/logging.php');
    $containerConfigurator->import('services/subscribers.php');
    $containerConfigurator->import('services/commands.php');
};
