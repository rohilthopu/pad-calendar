# Generated by Django 2.0.4 on 2018-06-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jpnTitle', models.CharField(default='', max_length=50)),
                ('altTitle', models.CharField(default='', max_length=50)),
                ('altTitle2', models.CharField(default='', max_length=50)),
                ('stamina', models.CharField(default='', max_length=10)),
                ('battles', models.CharField(default='', max_length=10)),
                ('dungeonType', models.CharField(default='', max_length=30)),
            ],
        ),
    ]