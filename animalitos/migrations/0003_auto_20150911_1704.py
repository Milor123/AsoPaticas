# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalitos', '0002_animal_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='members',
        ),
        migrations.AlterField(
            model_name='adoptar',
            name='estado_adopcion',
            field=models.CharField(default=1, max_length=30, choices=[(b'Perfecto', b'Perfecto'), (b'Decomisado', b'Decomisado'), (b'Devuelto', b'Devuelto')]),
        ),
    ]
