# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animalitos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='members',
            field=models.ManyToManyField(to='animalitos.Adoptante', through='animalitos.Adoptar'),
        ),
    ]
