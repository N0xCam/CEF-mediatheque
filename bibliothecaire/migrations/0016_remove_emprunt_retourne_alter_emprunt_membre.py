# Generated by Django 5.1.7 on 2025-04-10 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0015_emprunt_retourne'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprunt',
            name='retourne',
        ),
        migrations.AlterField(
            model_name='emprunt',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.membre'),
        ),
    ]
