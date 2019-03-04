# Generated by Django 2.1 on 2019-03-01 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20190301_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 12, 33, 56, 630484)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 12, 33, 56, 625674)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date_reviewed',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 12, 33, 56, 625674)),
        ),
        migrations.AlterField(
            model_name='step',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 12, 33, 56, 630484)),
        ),
    ]