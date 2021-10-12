from autoslug import AutoSlugField
from django.db import models


class Genre(models.Model):
    """
    Model to represent genres of titles.
    """
    name = models.CharField('Название жанра', max_length=200, unique=True)
    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        db_index=True,
        editable=True,
        blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
