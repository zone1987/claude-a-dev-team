<?php

declare(strict_types=1);

namespace App\Tests\E2E;

use Symfony\Component\Panther\Client;
use Symfony\Component\Panther\PantherTestCase;

/**
 * Basis-TestCase für Symfony-Panther-E2E-Tests.
 *
 * Bietet bequeme Helfer rund um den WebDriver-Client. Methoden-Signaturen sind gegen den
 * Panther-Quellcode verifiziert (Skill: panther-client). Passe Namespace/Pfade an dein Projekt an.
 */
abstract class AbstractPantherTestCase extends PantherTestCase
{
    protected Client $client;

    protected function setUp(): void
    {
        parent::setUp();

        // Echter Browser (Chrome/Firefox) via WebDriver — für JS/AJAX/Real-Time.
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
     * Navigiert zu einem Pfad und gibt den frischen Crawler zurück.
     */
    protected function visit(string $path): \Symfony\Component\Panther\DomCrawler\Crawler
    {
        return $this->client->request('GET', $path);
    }

    /**
     * Wartet, bis das Element sichtbar ist (statt sleep()) — Default-Timeout aus Panther.
     */
    protected function waitVisible(string $cssSelector, int $timeoutInSecond = 30): void
    {
        $this->client->waitForVisibility($cssSelector, $timeoutInSecond);
    }

    /**
     * Erstellt einen Screenshot (z. B. zur Diagnose) unter dem angegebenen Pfad.
     */
    protected function screenshot(string $file): void
    {
        $this->client->takeScreenshot($file);
    }
}
