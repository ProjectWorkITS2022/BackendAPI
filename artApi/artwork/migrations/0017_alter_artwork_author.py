# Generated by Django 4.1.7 on 2023-02-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0016_alter_artwork_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='author',
            field=models.CharField(max_length=64),
        ),
    ]
