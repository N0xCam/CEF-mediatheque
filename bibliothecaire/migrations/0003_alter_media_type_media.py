# Generated by Django 5.1.7 on 2025-04-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0002_boardgame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='type_media',
            field=models.CharField(choices=[('livre', 'Livre'), ('dvd', 'Dvd'), ('cd', 'Cd')], max_length=20),
        ),
    ]
