# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0012_auto_20160117_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='img',
            field=models.ImageField(upload_to=b'img/%Y'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='dataAdicionado',
            field=models.DateField(default=datetime.datetime(2016, 1, 18, 13, 14, 51, 295000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
