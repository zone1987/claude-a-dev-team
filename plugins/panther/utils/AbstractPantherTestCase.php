<?php

declare(strict_types=1);

namespace App\Tests\E2E;

use Symfony\Component\Panther\Client;
use Symfony\Component\Panther\PantherTestCase;

/**
 * Base test case for Symfony Panther E2E tests.
 *
 * Provides convenient helpers around the WebDriver client. Method signatures are verified against the
 * Panther-Quellcode verifiziert (Skill: panther-client). Passe Namespace/Pfade an dein Projekt an.
 */
abstract class AbstractPantherTestCase extends PantherTestCase
{
    protected Client $client;

    protected function setUp(): void
    {
        parent::setUp();

        // Real browser (Chrome/Firefox) via WebDriver — for JS/AJAX/real-time.
        // Optionen: $options (Webserver), $kernelOptions, $managerOptions (Browser-Args). Siehe panther-testcase.
        $this->client = static::createPantherClient(
            options: [
                // 'browser' => static::FIREFOX, // Default: static::CHROME
            ],
            managerOptions: [
                // 'capabilities' => [...],
            ],
        );
    }

    /**
     * Navigates to a path and returns the fresh crawler.
     */
    protected function visit(string $path): \Symfony\Component\Panther\DomCrawler\Crawler
    {
        return $this->client->request('GET', $path);
    }

    /**
     * Waits until the element is visible (instead of sleep()) — default timeout from Panther.
     */
    protected function waitVisible(string $cssSelector, int $timeoutInSecond = 30): void
    {
        $this->client->waitForVisibility($cssSelector, $timeoutInSecond);
    }

    /**
     * Takes a screenshot (e.g. for diagnostics) at the given path.
     */
    protected function screenshot(string $file): void
    {
        $this->client->takeScreenshot($file);
    }
}
