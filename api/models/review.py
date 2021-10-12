from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.models.title import Title
from api.models.user import YaUser


class Review(models.Model):
    """
    Model to represent reviews.
    """
    title = models.ForeignKey(Title,
                              verbose_name='Произведение',
                              on_delete=models.CASCADE,
                              related_name='reviews')
    text = models.TextField(verbose_name='Текст отзыва')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(YaUser,
                               verbose_name='Автор отзыва',
                               on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=[
            MinValueValidator(limit_value=1,
                              message='Оценка не может быть меньше 1'),
            MaxValueValidator(limit_value=10,
                              message='Оценка не может быть больше 10')
        ]
    )

    class Meta:
        ordering = ('-pub_date',)
        models.UniqueConstraint(
            fields=['author', 'title'],
            name='unique_review'
        )
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return (f'Отзыв на {self.title} пользователя'
                f'{self.author}, создана {self.pub_date}')
