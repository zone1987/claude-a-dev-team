<?php declare(strict_types=1);

// src/Resources/config/services/subscribers.php
//
// Explicit registration, no autowiring and no autoconfigure: every dependency is
// written out, and every tag Symfony would otherwise infer is set by hand.

namespace {PluginNamespace}\Resources\config\services;

use {PluginNamespace}\Subscriber\MySubscriber;
use {PluginNamespace}\Service\MyCachingService;
use Symfony\Component\DependencyInjection\Loader\Configurator\ContainerConfigurator;

use function Symfony\Component\DependencyInjection\Loader\Configurator\service;

return static function (ContainerConfigurator $containerConfigurator): void {
    $services = $containerConfigurator->services();

    $services->set(MySubscriber::class)
        ->args([
            service('product.repository'),
            service('{log-channel}.logger'),
        ])
        // Without autoconfigure this tag is not inferred. Omit it and the subscriber
        // is registered as a service that nothing ever calls.
        ->tag('kernel.event_subscriber');

    $services->set(MyCachingService::class)
        ->args([service('category.repository')])
        // Symfony wires ResetInterface through registerForAutoconfiguration, which this
        // plugin does not use: services are registered explicitly, so the tag is too.
        ->tag('kernel.reset', ['method' => 'reset']);
};
