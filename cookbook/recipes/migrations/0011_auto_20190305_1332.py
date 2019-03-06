# Generated by Django 2.1.5 on 2019-03-05 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20190304_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 13, 32, 51, 519784)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 13, 32, 51, 518787)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_reviewed',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 13, 32, 51, 518787)),
        ),
        migrations.AlterField(
            model_name='step',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 13, 32, 51, 518787)),
        ),
    ]