# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(null=True, blank=True)),
                ('idAdoptante', models.AutoField(serialize=False, primary_key=True)),
                ('direccion', models.CharField(max_length=30, blank=True)),
                ('cedula', models.IntegerField(null=True, blank=True)),
                ('departamento', models.CharField(max_length=30, blank=True)),
                ('cuidad', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('informacion', models.TextField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Adoptar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('voluntario', models.CharField(max_length=30, blank=True)),
                ('estado_adopcion', models.CharField(default=1, max_length=30, choices=[(b'Perfecto', b'Perfecto'), (b'Decomisado', b'Decomisado')])),
                ('Adoptante_idAdoptante', models.ForeignKey(to='animalitos.Adoptante')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('idAnimal', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('tipo_de_animal', models.CharField(max_length=30, choices=[(b'Gato', b'Gato'), (b'Perro', b'Perro')])),
                ('edad', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=30, choices=[(b'Macho', b'Macho'), (b'Hembra', b'Hembra')])),
                ('raza', models.CharField(max_length=30, blank=True)),
                ('color', models.CharField(max_length=30, blank=True)),
                ('salud', models.CharField(max_length=30, choices=[(b'Excelente', b'Excelente'), (b'Bueno', b'Bueno'), (b'Regular', b'Regular'), (b'Pesimo', b'Pesimo')])),
                ('informacion', models.TextField(max_length=30, blank=True)),
                ('es_esterilizado', models.CharField(max_length=30, choices=[(b'Si', b'Si'), (b'No', b'No')])),
            ],
        ),
        migrations.AddField(
            model_name='adoptar',
            name='Animal_idAnimal',
            field=models.ForeignKey(to='animalitos.Animal'),
        ),
    ]
