# Generated by Django 3.2.4 on 2021-06-04 06:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('limit', models.DateField(blank=True, default=datetime.datetime(2021, 6, 5, 6, 21, 13, 785500, tzinfo=utc))),
            ],
        ),
    ]
