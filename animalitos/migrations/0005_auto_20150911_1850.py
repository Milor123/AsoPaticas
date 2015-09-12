# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalitos', '0004_animal_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptante',
            name='direccion',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='informacion',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='adoptar',
            name='estado_adopcion',
            field=models.CharField(default=1, max_length=1000, choices=[(b'Perfecto', b'Perfecto'), (b'Decomisado', b'Decomisado'), (b'Devuelto', b'Devuelto')]),
        ),
    ]
