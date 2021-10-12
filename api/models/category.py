from autoslug import AutoSlugField
from django.db import models


class Category(models.Model):
    """
    Model to represent categories of titles.
    """
    name = models.CharField('Название категории', max_length=200, unique=True)
    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        db_index=True,
        editable=True,
        blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
