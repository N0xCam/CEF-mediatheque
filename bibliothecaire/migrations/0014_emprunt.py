# Generated by Django 5.1.7 on 2025-04-10 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0013_remove_media_est_empruntable_media_emprunte'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateTimeField(auto_now_add=True)),
                ('date_retour', models.DateTimeField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliothecaire.media')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
