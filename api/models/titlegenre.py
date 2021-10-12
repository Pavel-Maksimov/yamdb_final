from django.db import models

from .genre import Genre
from .title import Title


class TitleGenre(models.Model):
    """
    Auxiliary model for relationship Title-Genre (many-to-many).
    """
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'genre'],
                name='unique_genre')]

    def __str__(self):
        return f'{self.title}{self.genre}'
