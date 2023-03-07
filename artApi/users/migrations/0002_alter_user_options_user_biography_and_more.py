# Generated by Django 4.1.7 on 2023-03-05 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0022_alter_artist_id'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='biography',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artwork.artist'),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
