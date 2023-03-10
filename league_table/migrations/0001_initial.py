# Generated by Django 4.1.4 on 2023-01-29 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MatchStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_goals', models.PositiveIntegerField(default=0)),
                ('away_goals', models.PositiveIntegerField(default=0)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='away_team', to='league_table.club')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='home_team', to='league_table.club')),
            ],
        ),
        migrations.CreateModel(
            name='ClubStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played', models.PositiveIntegerField(default=0)),
                ('won', models.PositiveIntegerField(default=0)),
                ('draw', models.PositiveIntegerField(default=0)),
                ('losses', models.PositiveIntegerField(default=0)),
                ('goal_dif', models.PositiveIntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league_table.club')),
            ],
            options={
                'ordering': ['-points'],
            },
        ),
    ]
