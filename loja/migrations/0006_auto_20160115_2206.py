# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_auto_20160115_2205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategoria',
            old_name='nomeSubCat',
            new_name='nome',
        ),
    ]
