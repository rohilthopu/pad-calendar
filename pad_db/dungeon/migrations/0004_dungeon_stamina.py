# Generated by Django 2.0.7 on 2018-12-11 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0003_dungeon_floorname'),
    ]

    operations = [
        migrations.AddField(
            model_name='dungeon',
            name='stamina',
            field=models.IntegerField(default=0),
        ),
    ]
