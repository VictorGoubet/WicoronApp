# Generated by Django 3.0.5 on 2020-05-06 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connexion', '0005_auto_20200505_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='numero',
            field=models.CharField(default='0123456789', help_text='Numere de téléphone', max_length=10),
            preserve_default=False,
        ),
    ]
