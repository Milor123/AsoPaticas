from __future__ import unicode_literals
# -*- coding: iso-8859-15 -*-


from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your models here.



class Adoptante(models.Model):
    def __unicode__(self):
        return u"%s %s" %(self.nombre, self.apellido.decode("utf-8"))

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField(blank=True, null=True)

    idAdoptante = models.AutoField(primary_key=True)

    direccion = models.CharField(max_length=120, blank=True)
    cedula = models.IntegerField(blank=True, null=True)
    departamento = models.CharField(max_length=30, blank=True)
    cuidad = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    informacion = models.TextField(max_length=1000, blank=True)

class Animal(models.Model):

    def __unicode__(self):
        return "%s" %(self.nombre)

    idAnimal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    animales = (
        ('Gato','Gato'),
        ('Perro','Perro'),
        ('Desconocido', 'Desconocido')
    )
    tipo_de_animal = models.CharField(max_length=30, choices=animales)
    edad = models.CharField(max_length=30)
    estadosexo = (
        ('Macho', 'Macho'),
        ('Hembra','Hembra'),
    )
    sexo = models.CharField(max_length=30, choices=estadosexo)
    raza = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=30, blank=True)

    estadosalud= (
        ('Excelente','Excelente'),
        ('Bueno','Bueno'),
        ('Regular','Regular'),
        ('Pesimo','Pesimo'),
    )
    salud = models.CharField(max_length=30, choices=estadosalud)
    informacion = models.TextField(max_length=1000, blank=True)

    estadoesterilizado = (
        ('Si', 'Si'),
        ('No', 'No'),
    )
    es_esterilizado = models.CharField(max_length=30, choices=estadoesterilizado)

    members = models.ManyToManyField(Adoptante, through='Adoptar', through_fields=('Animal_idAnimal', 'Adoptante_idAdoptante'))

    # para vetificar antes de iniciar
    def clean(self):
        import re
        RE= re.compile(r'^\s')
        if RE.search(self.nombre):
            raise ValidationError('El campo %s No puede contener espacios al inicio del mismo' % ('Nombre'))


class Adoptar(models.Model):

    #def __unicode__(self):
     #   return "Animal:%s ---- Encargado:%s" %(self.Animal_idAnimal, self.Adoptante_idAdoptante)



    def save(self, *args, **kwargs):
        #Instanciamos el objeto adoptar, y vamos a ver si existe un animal con la que vamos a relacionar,
        #es decir self.mi id y comparamos.... si existe entonces ya fue adoptado,
        #asi que debemos proceder a ver si existe uno adoptado y que aya sido decomisado
        #usamos filter para varios NO GET...
        test=False
        adoptar= Adoptar.objects.filter(Animal_idAnimal= self.Animal_idAnimal, estado_adopcion='Perfecto') # Instancia Adoptante y pasa lo que encuentr en id_Adoptante
        if len(adoptar)>0 and (self.estado_adopcion=='Perfecto'):
            for x in adoptar:
                if x.Adoptante_idAdoptante==self.Adoptante_idAdoptante and x.Animal_idAnimal!=self.Animal_idAnimal:
                    super(Adoptar, self).save(*args, **kwargs)
                else:
                    raise ValidationError('El animal ya ha sido adoptado esto es test %s **** **** %s'%(test, 'xD'))

        #elif len(adoptar)<0 and self.estado_adopcion=='Decomisado':
            #raise ValidationError('No puedes poner en adopcion un animal y decir que ha sido decomidado, revisa lo que dices')
        else:
            super(Adoptar, self).save(*args, **kwargs)


    Animal_idAnimal = models.ForeignKey('Animal')
    Adoptante_idAdoptante = models.ForeignKey('Adoptante')
    #Adoptante_idAdoptante= models.ForeignKey(Adoptante, on_delete=models.CASCADE) # test2
    #Adoptante_idAdoptante = models.ManyToManyField('Adoptante') # test

    fecha = models.DateField()
    voluntario= models.CharField(max_length=30, blank=True)

    estadoanimal = (
        ('Perfecto', 'Perfecto'),
        ('Decomisado', 'Decomisado'),
        ('Devuelto','Devuelto')
    )
    estado_adopcion = models.CharField(max_length=30, choices=estadoanimal, default=1)
#xD














