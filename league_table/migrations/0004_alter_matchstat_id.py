# Generated by Django 4.1.4 on 2022-12-20 19:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('league_table', '0003_alter_matchstat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchstat',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]