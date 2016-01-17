# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_categoria_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategoria',
            old_name='cat',
            new_name='categoria',
        ),
    ]
