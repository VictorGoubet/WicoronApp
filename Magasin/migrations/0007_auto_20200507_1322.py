# Generated by Django 3.0.3 on 2020-05-07 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Magasin', '0006_commande_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='Date',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 11, 22, 36, 720769, tzinfo=utc)),
        ),
    ]
