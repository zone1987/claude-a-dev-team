# Example: MediaDefinition

Demonstrates: Computed fields, RestrictDelete, SetNullOnDelete, Runtime fields, WriteProtected with scopes, BlobField.

```php
class MediaDefinition extends EntityDefinition
{
    protected function defineFields(): FieldCollection
    {
        return new FieldCollection([
            (new IdField('id', 'id'))->addFlags(new ApiAware(), new PrimaryKey(), new Required()),

            // System-scope write-protected fields (set by upload process)
            (new DateTimeField('uploaded_at', 'uploadedAt'))
                ->addFlags(new ApiAware(), new WriteProtected(Context::SYSTEM_SCOPE)),
            (new IntField('file_size', 'fileSize'))
                ->addFlags(new ApiAware(), new WriteProtected(Context::SYSTEM_SCOPE)),
            (new JsonField('meta_data', 'metaData'))
                ->addFlags(new ApiAware(), new WriteProtected(Context::SYSTEM_SCOPE)),

            // BlobField for binary data (not API-visible)
            (new BlobField('media_type', 'mediaTypeRaw'))->removeFlag(ApiAware::class)
                ->addFlags(new WriteProtected(Context::SYSTEM_SCOPE)),

            // Runtime field computed from other fields
            (new JsonField('media_type', 'mediaType'))->addFlags(new WriteProtected(), new Runtime()),
            (new StringField('url', 'url'))
                ->addFlags(new ApiAware(), new Runtime(['path', 'private', 'updatedAt'])),
            (new BoolField('has_file', 'hasFile'))->addFlags(new ApiAware(), new Runtime()),

            // Computed field (written by indexer, not writable)
            (new BlobField('thumbnails_ro', 'thumbnailsRo'))
                ->removeFlag(ApiAware::class)->addFlags(new Computed()),

            // Translated fields with SearchRanking
            (new TranslatedField('alt'))
                ->addFlags(new ApiAware(), new SearchRanking(SearchRanking::MIDDLE_SEARCH_RANKING)),
            (new TranslatedField('title'))
                ->addFlags(new ApiAware(), new SearchRanking(SearchRanking::HIGH_SEARCH_RANKING)),

            // CascadeDelete: thumbnails deleted with media
            (new OneToManyAssociationField('thumbnails', MediaThumbnailDefinition::class, 'media_id'))
                ->addFlags(new ApiAware(), new CascadeDelete()),

            // SetNullOnDelete: FK set to NULL when media deleted
            (new OneToManyAssociationField('categories', CategoryDefinition::class, 'media_id'))
                ->addFlags(new SetNullOnDelete()),

            // RestrictDelete: cannot delete media if referenced
            (new OneToManyAssociationField('cmsBlocks', CmsBlockDefinition::class, 'background_media_id'))
                ->addFlags(new RestrictDelete()),
            (new OneToManyAssociationField('productDownloads', ProductDownloadDefinition::class, 'media_id'))
                ->addFlags(new RestrictDelete()),
        ]);
    }
}
```
