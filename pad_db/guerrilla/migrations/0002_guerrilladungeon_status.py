# Generated by Django 2.0.7 on 2019-07-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guerrilla', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guerrilladungeon',
            name='status',
            field=models.CharField(default='', max_length=15),
        ),
    ]