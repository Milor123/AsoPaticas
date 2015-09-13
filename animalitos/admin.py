from __future__ import unicode_literals
#!/usr/bin/python 2.7
# -*- encoding: utf-8 -*-
from django.contrib import admin
from animalitos.models import Animal, Adoptante, Adoptar
from django.db import models#test
from django.utils.safestring import mark_safe




#@admin.register(Animal)
#class Animal(admin.ModelAdmin):
#    pass

#StackedInline ?? TabularInline
class AdoptarInLine(admin.StackedInline):

    model = Adoptar
    #fields=('fecha',)
    #readonly_fields = ('fecha',)
    #raw_id_fields = ("Animal_idAnimal","Adoptante_idAdoptante")
    extra = 0
    #ordering = ('-fecha',)
    fk_name = ('Animal_idAnimal')


    #fix bug auto add extra
    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra

#@admin.register(Adoptar)
#class Adoptar(admin.ModelAdmin):
    #pass
    #list_display = ('fecha','voluntario')




@admin.register(Animal)
class AnimalInline(admin.ModelAdmin):

    list_display = ('nombre','tipo_de_animal','estado_de_salud', 'numero_telefono','sexo','edad', 'color','adoptantes','fecha_de_adopcion', 'esterilizado',)
    search_fields = ('nombre', 'adoptar__Adoptante_idAdoptante__idAdoptante','adoptar__Adoptante_idAdoptante__telefono')
    inlines = [AdoptarInLine,]


    def adoptantes(self,Animal):
        adoptante = Adoptar.objects.filter(Animal_idAnimal = Animal.idAnimal).order_by('-fecha').first()
        try:
            return mark_safe("<a href='/animalitos/adoptante/%s'>%s</a> " %(adoptante.Adoptante_idAdoptante.idAdoptante,adoptante.Adoptante_idAdoptante))
        except:
            return 0

    def numero_telefono(self,Animal):
        adoptante = Adoptar.objects.filter(Animal_idAnimal = Animal.idAnimal).order_by('-fecha').first()
        try:
            return  adoptante.Adoptante_idAdoptante.telefono
        except:
            return 0

    def esterilizado(self, Animal):
        if Animal.es_esterilizado=='Si':
            return mark_safe( "<font color='green'><b>%s</b></font>" %Animal.es_esterilizado)
        elif Animal.es_esterilizado=='No':
            return mark_safe( "<font color='red'><b>%s</b></font>" %Animal.es_esterilizado)

    def estado_de_salud(self, Animal):
        if Animal.salud == 'Excelente':
            return mark_safe( "<font color='green'><b>%s</b></font>" %Animal.salud)
        elif Animal.salud == 'Bueno':
            return mark_safe( "<font color='blue'><b>%s</b></font>" %Animal.salud)
        elif Animal.salud == 'Regular':
            return mark_safe( "<font color=#F29C2A><b>%s</b></font>" %Animal.salud)
        elif Animal.salud == 'Pesimo':
            return mark_safe( "<font color='red'><b>%s</b></font>" %Animal.salud)
        else:
            return ''

    def fecha_de_adopcion(self,Animal):
        #import pdb
        #pdb.set_trace() # dir(string)
        try:
            adoptante = Adoptar.objects.filter(Animal_idAnimal = Animal.idAnimal).order_by('-fecha').first()
            return adoptante.fecha
        except:
            return 0
    esterilizado.admin_order_field='es_esterilizado'
    estado_de_salud.admin_order_field='salud'
    fecha_de_adopcion.admin_order_field='adoptar__fecha'
    adoptantes.admin_order_field = 'adoptar__Adoptante_idAdoptante'
    numero_telefono.admin_order_field= 'adoptar__Adoptante_idAdoptante__telefono'
@admin.register(Adoptante)
class Adoptante(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','direccion','cedula','departamento','cuidad','email','informacion')
    search_fields = ('nombre','apellido','informacion','direccion','email')

