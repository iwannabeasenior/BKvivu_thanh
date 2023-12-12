# Generated by Django 4.2.7 on 2023-12-11 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_manager_name_stripped_alter_bill_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name_stripped',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_stripped',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 19, 45, 0, 268207)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 19, 45, 0, 268207)),
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 19, 45, 0, 268207)),
        ),
    ]