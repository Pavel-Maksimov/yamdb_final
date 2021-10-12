from django.contrib.auth.models import AbstractUser
from django.db import models


class YaUser(AbstractUser):
    """ Defines YaUser model and its database fields."""

    class Role(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    username = models.CharField(
        'Username', max_length=255, unique=True
    )
    bio = models.TextField('О себе', blank=True)
    email = models.EmailField(
        'Адрес электронной почты', max_length=255, unique=True
    )
    role = models.CharField(
        max_length=20, choices=Role.choices, default=Role.USER
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.email)

    @property
    def is_moderator(self):
        """
        Return True if user.role is 'moderator'.
        """
        return self.role == 'moderator'

    @property
    def is_admin(self):
        """
        Return True if user.role is 'admin'
        or user is superuser.
        """
        return self.is_superuser or self.role == 'admin'
