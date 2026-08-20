<?php

declare(strict_types=1);

// Domain Exception Factory Pattern (Shopware 6.7)
// Each domain gets one exception class acting as a factory for all error cases.
// See: references/php-migration.md, shopware-plugins/adr/2022-02-24-domain-exceptions.md

namespace FfContentPlus\Core\Exception;

use Shopware\Core\Framework\HttpException;
use Shopware\Core\Framework\Log\Package;
use Symfony\Component\HttpFoundation\Response;

/**
 * @class ContentException
 * @package FfContentPlus\Core\Exception
 */
#[Package('custom-plugins')]
class ContentException extends HttpException
{
    /**
     * @var string
     */
    public const CONTENT_NOT_FOUND = 'FF_CONTENT_PLUS__CONTENT_NOT_FOUND';

    /**
     * @var string
     */
    public const IMPORT_FAILED = 'FF_CONTENT_PLUS__IMPORT_FAILED';

    /**
     * @var string
     */
    public const INVALID_CONFIGURATION = 'FF_CONTENT_PLUS__INVALID_CONFIGURATION';

    /**
     * @param string $contentId
     * @return self
     */
    public static function contentNotFound(string $contentId): self
    {
        return new self(
            Response::HTTP_NOT_FOUND,
            self::CONTENT_NOT_FOUND,
            'Content item with id "{{ contentId }}" not found.',
            ['contentId' => $contentId]
        );
    }

    /**
     * @param string $reason
     * @param \Throwable|null $previous
     * @return self
     */
    public static function importFailed(string $reason, ?\Throwable $previous = null): self
    {
        return new self(
            Response::HTTP_INTERNAL_SERVER_ERROR,
            self::IMPORT_FAILED,
            'Content import failed: {{ reason }}',
            ['reason' => $reason],
            $previous
        );
    }

    /**
     * @param string $key
     * @return self
     */
    public static function invalidConfiguration(string $key): self
    {
        return new self(
            Response::HTTP_BAD_REQUEST,
            self::INVALID_CONFIGURATION,
            'Plugin configuration key "{{ key }}" is invalid or missing.',
            ['key' => $key]
        );
    }
}

// Usage:
// throw ContentException::contentNotFound($id);
// throw ContentException::importFailed('API timeout', $previousException);
// throw ContentException::invalidConfiguration('FfContentPlus.config.apiKey');
