import os

from django.db import models

__all__ = ['Artwork', 'Artist']


# Create your models here.
def upload_to(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return 'images/artworks/{filename}'.format(filename=instance.id) + file_extension


class Artist(models.Model):
    name = models.CharField(max_length=50, db_column='artist', primary_key=True)
    years = models.CharField(max_length=50, db_column='born-died')
    period = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    base = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    sourcePage = models.CharField(max_length=64, db_column='url')

    def __str__(self):
        return self.name


class Artwork(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    # Extra picture data
    date = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=50, null=True)
    museum = models.CharField(max_length=128, null=True)
    # File information
    resolution = models.CharField(max_length=24)
    color = models.CharField(max_length=24)
    file_dimension = models.CharField(max_length=24)

    image_url = models.ImageField(upload_to=upload_to, max_length=50, db_column='jpg url')

    def __str__(self):
        return self.title
