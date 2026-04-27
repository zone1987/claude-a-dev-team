# Example: Tree Entity (CategoryDefinition)

Demonstrates: tree structure with path, level, breadcrumb, parent/children, after-sorting.

```php
class CategoryDefinition extends EntityDefinition
{
    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new IdField('id', 'id'))->addFlags(new ApiAware(), new PrimaryKey(), new Required()),
            (new VersionField())->addFlags(new ApiAware()),

            // Self-referencing parent FK
            (new ParentFkField(self::class))->addFlags(new ApiAware()),
            (new ReferenceVersionField(self::class, 'parent_version_id'))->addFlags(new ApiAware(), new Required()),

            // After-sorting (linked-list ordering within siblings)
            (new FkField('after_category_id', 'afterCategoryId', self::class))->addFlags(new ApiAware()),
            (new ReferenceVersionField(self::class, 'after_category_version_id'))->addFlags(new ApiAware(), new Required()),

            // Tree fields (auto-computed, system-write-protected)
            (new TreeLevelField('level', 'level'))->addFlags(new ApiAware()),
            (new TreePathField('path', 'path'))->addFlags(new ApiAware()),
            (new ChildCountField())->addFlags(new ApiAware()),

            // Breadcrumb in translation (write-protected)
            (new TranslatedField('breadcrumb'))->addFlags(new ApiAware(), new WriteProtected()),

            // Parent/Children associations
            (new ParentAssociationField(self::class, 'id'))->addFlags(new ApiAware()),
            (new ChildrenAssociationField(self::class))->addFlags(new ApiAware()),

            // Products in this category (with ReverseInherited)
            (new ManyToManyAssociationField('products', ProductDefinition::class,
                ProductCategoryDefinition::class, 'category_id', 'product_id'))
                ->addFlags(new CascadeDelete(), new ReverseInherited('categories')),

            (new TranslationsAssociationField(CategoryTranslationDefinition::class, 'category_id'))
                ->addFlags(new ApiAware(), new Required()),
        ]);
    }
}
```

**Tree fields behavior:**
- `TreePathField`: Stores `|uuid1|uuid2|uuid3|` (pipe-delimited ancestor trail)
- `TreeLevelField`: Depth integer (1-based, root = 1)
- `ChildCountField`: Denormalized count of direct children
- All three are `WriteProtected(Context::SYSTEM_SCOPE)` and maintained by `TreeUpdater` and `ChildCountUpdater`
