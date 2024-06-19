from django.db import models

# Create your models here.

"""
Esto crea una tabla con nombre Prueba y sus campos
titulo y subtitulo se le asigna un típo de dato
"""


class Prueba(models.Model):
    titulo = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=50)
    cantidad  = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.titulo + "-" + self.subtitulo
