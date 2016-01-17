# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_auto_20160115_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='fabricante',
            field=models.CharField(default=b'N\xc3\xa3o informado', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='produto',
            name='origem',
            field=models.CharField(default=b'N\xc3\xa3o informado', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='produto',
            name='tamanho',
            field=models.CharField(default=b'N\xc3\xa3o informado', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='produto',
            name='tecido',
            field=models.CharField(default=b'N\xc3\xa3o informado', max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='dataAdicionado',
            field=models.DateField(default=datetime.datetime(2016, 1, 17, 20, 22, 41, 600000, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(default=b'N\xc3\xa3o informado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtdVendido',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor',
            field=models.CharField(default=100, max_length=255),
            preserve_default=False,
        ),
    ]
