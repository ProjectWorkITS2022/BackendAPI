# Generated by Django 4.1.7 on 2023-02-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0015_remove_artwork_color_remove_artwork_file_dimension_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
