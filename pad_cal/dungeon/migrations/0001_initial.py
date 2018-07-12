# Generated by Django 2.0.7 on 2018-07-12 19:29

import datetime
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
                ('dungeonLink', models.TextField(default='')),
                ('daily', models.BooleanField(default=False)),
                ('repeat', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DungeonToday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listingDate', models.DateField(default=datetime.date(2018, 7, 12))),
                ('dungeons', models.ManyToManyField(to='dungeon.Dungeon')),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('hp', models.CharField(default='', max_length=20)),
                ('defense', models.CharField(default='', max_length=20)),
                ('atk', models.CharField(default='', max_length=20)),
                ('jpnTitle', models.CharField(default='', max_length=50)),
                ('altTitle', models.CharField(default='', max_length=50)),
                ('altTitle2', models.CharField(default='', max_length=50)),
                ('dungeonID', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('altName', models.CharField(default='', max_length=50)),
                ('effect', models.TextField(default='', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='skills',
            field=models.ManyToManyField(to='dungeon.Skill'),
        ),
        migrations.AddField(
            model_name='dungeon',
            name='monsters',
            field=models.ManyToManyField(to='dungeon.Monster'),
        ),
    ]
