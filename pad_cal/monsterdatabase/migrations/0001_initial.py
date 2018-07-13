# Generated by Django 2.0.7 on 2018-07-13 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('skillID', models.IntegerField(blank=True, default=0)),
                ('skillType', models.IntegerField(blank=True, default=0)),
                ('levels', models.IntegerField(default=0)),
                ('maxTurns', models.IntegerField(blank=True, default=0)),
                ('minTurns', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CardNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activeSkill', models.ManyToManyField(to='monsterdatabase.ActiveSkill')),
            ],
        ),
        migrations.CreateModel(
            name='LeaderSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('skillID', models.IntegerField(blank=True, default=0)),
                ('skillType', models.IntegerField(blank=True, default=0)),
                ('doesNothing', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonsterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activeSkillID', models.IntegerField(blank=True)),
                ('ancestorID', models.IntegerField()),
                ('attributeID', models.IntegerField()),
                ('baseID', models.IntegerField()),
                ('cardID', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('inheritable', models.BooleanField()),
                ('isCollab', models.BooleanField()),
                ('isReleased', models.BooleanField()),
                ('isUlt', models.BooleanField()),
                ('leaderSkillID', models.IntegerField(blank=True)),
                ('maxATK', models.IntegerField()),
                ('maxHP', models.IntegerField()),
                ('maxLevel', models.IntegerField()),
                ('maxRCV', models.IntegerField()),
                ('minATK', models.IntegerField()),
                ('minHP', models.IntegerField()),
                ('minRCV', models.IntegerField()),
                ('maxXP', models.IntegerField()),
                ('name', models.CharField(default='', max_length=200)),
                ('rarity', models.IntegerField()),
                ('subAttributeID', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cardna',
            name='leaderSkill',
            field=models.ManyToManyField(to='monsterdatabase.LeaderSkill'),
        ),
        migrations.AddField(
            model_name='cardna',
            name='monster',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster', to='monsterdatabase.MonsterData'),
        ),
    ]