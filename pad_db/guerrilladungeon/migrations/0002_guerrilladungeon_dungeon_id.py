# Generated by Django 2.0.7 on 2018-12-20 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guerrilladungeon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guerrilladungeon',
            name='dungeon_id',
            field=models.IntegerField(default=-1),
        ),
    ]
