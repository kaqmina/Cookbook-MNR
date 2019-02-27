# Generated by Django 2.1 on 2019-02-27 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20190227_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 27, 12, 56, 23, 472179)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 27, 12, 56, 23, 470184)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_reviewed',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 27, 12, 56, 23, 471181)),
        ),
        migrations.AlterField(
            model_name='step',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 27, 12, 56, 23, 472179)),
        ),
    ]
