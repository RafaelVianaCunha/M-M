# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20160115_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
