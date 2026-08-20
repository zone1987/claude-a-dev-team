<?php declare(strict_types=1);

namespace FfContentPlus\Storefront\Controller;

use Shopware\Core\Framework\Log\Package;
use Shopware\Core\System\SalesChannel\SalesChannelContext;
use Shopware\Storefront\Controller\StorefrontController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

/**
 * @class FfContentPlusController
 * @package FfContentPlus\Storefront\Controller
 */
#[Route(defaults: ['_routeScope' => ['storefront']])]
#[Package('custom-plugins')]
class FfContentPlusController extends StorefrontController
{
    /**
     * @param Request $request
     * @param SalesChannelContext $context
     * @return Response
     */
    #[Route(
        path: '/ff-content-plus',
        name: 'frontend.ff-content-plus.index',
        methods: ['GET'],
    )]
    public function index(Request $request, SalesChannelContext $context): Response
    {
        return $this->renderStorefront(
            '@FfContentPlus/storefront/page/content-plus/index.html.twig',
            [
                'page' => [],
            ],
        );
    }
}
