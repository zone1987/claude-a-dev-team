<?php declare(strict_types=1);

namespace FfContentPlus\Extension\Content\Product;

use FfContentPlus\Core\Content\FfContentPlusItemDefinition;
use Shopware\Core\Content\Product\ProductDefinition;
use Shopware\Core\Framework\DataAbstractionLayer\EntityExtension;
use Shopware\Core\Framework\DataAbstractionLayer\Field\ManyToManyAssociationField;
use Shopware\Core\Framework\DataAbstractionLayer\FieldCollection;
use Shopware\Core\Framework\Log\Package;

/**
 * @class ProductExtension
 * @package FfContentPlus\Extension\Content\Product
 */
#[Package('custom-plugins')]
class ProductExtension extends EntityExtension
{
    /**
     * @param FieldCollection $collection
     * @return void
     */
    public function extendFields(FieldCollection $collection): void
    {
        $collection->add(
            new ManyToManyAssociationField(
                'ffContentPlusItems',
                FfContentPlusItemDefinition::class,
                'ff_content_plus_item_product',
                'product_id',
                'ff_content_plus_item_id',
            ),
        );
    }

    /**
     * @return string
     */
    public function getDefinitionClass(): string
    {
        return ProductDefinition::class;
    }
}
