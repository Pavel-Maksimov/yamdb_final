from django.db import models

from api.validators.validate_year import validate_year

from .category import Category
from .genre import Genre


class Title(models.Model):
    """
    Model to represent all the titles.
    """
    name = models.CharField('Название', max_length=250)
    year = models.PositiveSmallIntegerField(
        'Год создания',
        null=True,
        validators=[validate_year],
        db_index=True)
    description = models.TextField('Описание', default='Описание не добавлено')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория произведения')
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenre')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
