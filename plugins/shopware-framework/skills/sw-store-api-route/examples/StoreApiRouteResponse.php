<?php declare(strict_types=1);

namespace FfContentPlus\Core\Content\Route;

use Shopware\Core\Framework\DataAbstractionLayer\Search\EntitySearchResult;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\System\SalesChannel\StoreApiResponse;

/**
 * @class FfContentPlusRouteResponse
 * @package FfContentPlus\Core\Content\Route
 */
#[Package('custom-plugins')]
class FfContentPlusRouteResponse extends StoreApiResponse
{
    /**
     * @param EntitySearchResult $object
     */
    public function __construct(EntitySearchResult $object)
    {
        parent::__construct($object);
    }

    /**
     * @return EntitySearchResult
     */
    public function getResult(): EntitySearchResult
    {
        return $this->object;
    }
}
