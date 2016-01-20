# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0010_auto_20160117_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='img',
            field=models.FileField(upload_to=b'imgp/%Y'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='dataAdicionado',
            field=models.DateField(default=datetime.datetime(2016, 1, 18, 0, 28, 31, 402000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
