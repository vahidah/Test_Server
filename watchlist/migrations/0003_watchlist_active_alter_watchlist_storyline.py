# Generated by Django 4.2 on 2023-05-03 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0002_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='storyline',
            field=models.CharField(max_length=200),
        ),
    ]
