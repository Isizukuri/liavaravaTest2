# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1000, verbose_name='T\u0435\u043a\u0441\u0442\u043e\u0432\u0456 \u043f\u043e\u043b\u044f')),
            ],
        ),
    ]
