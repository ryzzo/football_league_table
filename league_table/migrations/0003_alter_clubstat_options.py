# Generated by Django 4.1.4 on 2023-01-29 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league_table', '0002_alter_club_options_alter_clubstat_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubstat',
            options={'ordering': ('-points', 'goal_dif', 'club')},
        ),
    ]
