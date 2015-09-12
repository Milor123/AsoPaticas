# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalitos', '0005_auto_20150911_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptar',
            name='estado_adopcion',
            field=models.CharField(default=1, max_length=30, choices=[('Perfecto', 'Perfecto'), ('Decomisado', 'Decomisado'), ('Devuelto', 'Devuelto')]),
        ),
        migrations.AlterField(
            model_name='animal',
            name='informacion',
            field=models.TextField(max_length=1000, blank=True),
        ),
    ]
