# Generated by Django 3.0.3 on 2020-05-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connexion', '0004_auto_20200504_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='coordonneeGeoY',
            field=models.FloatField(help_text='Coordonnée en Y'),
        ),
    ]