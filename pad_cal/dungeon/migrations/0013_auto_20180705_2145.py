# Generated by Django 2.0.4 on 2018-07-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0012_auto_20180705_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='dungeon',
            name='repeat',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='skill',
            name='altName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
