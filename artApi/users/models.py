from artwork.models import Artist
from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ['User']


class User(AbstractUser):
    biography = models.TextField(null=True)
    favorite_artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username
