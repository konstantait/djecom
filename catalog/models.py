from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from core.mixins.models import (
    BaseUUID,
    BaseName,
    BaseSlug,
    BaseDescription,
    BaseImage,
    BaseQuantityPrice,
    BaseStatus,
    BaseSortOrder,
    BaseDateAddedModified
)

from core.constants import (
    CSV_IN_FIELD_ATTR_DELIMITER
)

User = get_user_model()


class AttributeGroup(
    BaseUUID,
    BaseName,
    BaseSortOrder
):
    def __str__(self):
        return self.name


class Attribute(
    BaseUUID,
    BaseName,
    BaseSortOrder
):
    attribute_group = models.ForeignKey(
        AttributeGroup,
        on_delete=models.CASCADE,
        related_name='attributes',
        verbose_name='Group'
    )

    def __str__(self):
        return self.name


class Category(
    BaseUUID,
    BaseName,
    BaseSlug,
    BaseDescription,
    BaseStatus,
    BaseSortOrder,
    BaseDateAddedModified
):
    def __str__(self):
        return self.name


class Product(
    BaseUUID,
    BaseName,
    BaseSlug,
    BaseDescription,
    BaseImage,
    BaseQuantityPrice,
    BaseStatus,
    BaseSortOrder,
    BaseDateAddedModified
):
    model = models.CharField(
        max_length=64,
        default='',
        blank=True
    )
    sku = models.CharField(
        max_length=64,
        unique=True
    )

    bookmarked_by = models.ManyToManyField(
        User,
        related_name='favorites',
        blank=True
    )

    bookmarks_count = models.PositiveIntegerField(default=0)

    categories = models.ManyToManyField(
        Category,
        related_name='products',
        blank=True
    )

    attributes = models.ManyToManyField(
        Attribute,
        related_name='products',
        blank=True
    )

    def __str__(self):
        return self.name

    def get_main_category(self):
        return self.categories.order_by('sort_order').first()

    def get_absolute_url(self):
        categories = self.get_main_category()
        kwargs = {
            'category_slug': categories.slug,
            'slug': self.slug
        }
        url = reverse('catalog:detail', kwargs=kwargs)
        return url

    def get_categories(self):
        return [
            category['name'] for category in (
                self.categories
                .all()
                .order_by('sort_order')
                .values('name')
            )
        ]

    def get_attributes(self):
        return [
            attribute['attribute_group__name'] +
            CSV_IN_FIELD_ATTR_DELIMITER +
            attribute['name'] for attribute in (
                self.attributes
                .select_related('attribute_group')
                .order_by('attribute_group__sort_order')
                .values('attribute_group__name', 'name')
            )
        ]
