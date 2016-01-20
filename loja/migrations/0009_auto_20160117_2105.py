# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0008_auto_20160117_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='dataAdicionado',
            field=models.DateField(default=datetime.datetime(2016, 1, 17, 23, 5, 9, 770000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtdVendido',
            field=models.CharField(default=0, max_length=255),
            preserve_default=True,
        ),
    ]
