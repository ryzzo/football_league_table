# Generated by Django 4.1.4 on 2023-01-29 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league_table', '0003_alter_clubstat_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubstat',
            options={'ordering': ('-points', '-goal_dif', 'club')},
        ),
    ]
