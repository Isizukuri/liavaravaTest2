# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20151116_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpRequestLogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Request date/time', db_index=True)),
                ('request_method', models.CharField(max_length=6, verbose_name=b'Method', db_index=True)),
                ('path', models.CharField(max_length=256)),
            ],
        ),
    ]
