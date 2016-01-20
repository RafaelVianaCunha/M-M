# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_auto_20160117_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='dataAdicionado',
            field=models.DateField(default=datetime.datetime(2016, 1, 17, 22, 47, 9, 180000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
