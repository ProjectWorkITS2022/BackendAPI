# Generated by Django 4.1.7 on 2023-02-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0019_artwork_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(db_column='artist', max_length=50, unique=True),
        ),
    ]