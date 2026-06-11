<?php declare(strict_types=1);

namespace FfContentPlus\Core\Content\Route;

use Shopware\Core\Framework\DataAbstractionLayer\EntityRepository;
use Shopware\Core\Framework\DataAbstractionLayer\Search\Criteria;
use Shopware\Core\Framework\Log\Package;
use Shopware\Core\Framework\Plugin\Exception\DecorationPatternException;
use Shopware\Core\System\SalesChannel\SalesChannelContext;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Attribute\Route;

/**
 * @class FfContentPlusRoute
 * @package FfContentPlus\Core\Content\Route
 */
#[Route(defaults: ['_routeScope' => ['store-api']])]
#[Package('custom-plugins')]
class FfContentPlusRoute extends AbstractFfContentPlusRoute
{
    /**
     * @param EntityRepository $repository
     */
    public function __construct(
        private readonly EntityRepository $repository,
    ) {}

    /**
     * @return AbstractFfContentPlusRoute
     * @throws DecorationPatternException
     */
    public function getDecorated(): AbstractFfContentPlusRoute
    {
        throw new DecorationPatternException(self::class);
    }

    /**
     * @param Request $request
     * @param Criteria $criteria
     * @param SalesChannelContext $context
     * @return FfContentPlusRouteResponse
     */
    #[Route(
        path: '/store-api/ff-content-plus',
        name: 'store-api.ff-content-plus.search',
        methods: ['GET', 'POST'],
        defaults: ['_entity' => 'ff_content_plus_item'],
    )]
    public function load(
        Request $request,
        Criteria $criteria,
        SalesChannelContext $context,
    ): FfContentPlusRouteResponse {
        $result = $this->repository->search($criteria, $context->getContext());

        return new FfContentPlusRouteResponse($result);
    }
}
