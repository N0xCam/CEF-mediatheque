# Generated by Django 5.1.7 on 2025-04-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0014_emprunt'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprunt',
            name='retourne',
            field=models.BooleanField(default=False),
        ),
    ]
