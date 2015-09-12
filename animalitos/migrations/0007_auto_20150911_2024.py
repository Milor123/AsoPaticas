# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalitos', '0006_auto_20150911_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='tipo_de_animal',
            field=models.CharField(max_length=30, choices=[('Gato', 'Gato'), ('Perro', 'Perro'), ('Desconocido', 'Desconocido')]),
        ),
    ]
