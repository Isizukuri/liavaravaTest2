# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textnote',
            name='text',
            field=models.TextField(verbose_name='T\u0435\u043a\u0441\u0442\u043e\u0432\u0456 \u043f\u043e\u043b\u044f'),
        ),
    ]
