# Generated by Django 3.0.5 on 2020-05-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connexion', '0002_profil_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='coordonneeGeoX',
            field=models.IntegerField(default=1, help_text='Coordonnée en X'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='coordonneeGeoY',
            field=models.IntegerField(default=1, help_text='Coordonnée en X'),
            preserve_default=False,
        ),
    ]
