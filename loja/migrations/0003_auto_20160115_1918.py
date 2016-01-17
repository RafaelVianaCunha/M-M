# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20160114_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nomeSubCat', models.CharField(max_length=255, null=True)),
                ('cat', models.ForeignKey(related_name='subCategoria', to='loja.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='produto',
            name='fabricante',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='tamanho',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='tecido',
        ),
        migrations.AddField(
            model_name='categoria',
            name='produtos',
            field=models.ManyToManyField(related_name='categorias', to='loja.Produto'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imagem',
            name='img',
            field=models.FileField(default=1, upload_to=b'img/%Y'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagem',
            name='produto',
            field=models.ForeignKey(related_name='imagens', default=1, to='loja.Produto'),
            preserve_default=False,
        ),
    ]
