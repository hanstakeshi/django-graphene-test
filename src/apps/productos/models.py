from django.db import models
from filebrowser.fields import FileBrowseField

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField("Nombre", blank=True,
                              null=True, max_length=440)
    posicion = models.SmallIntegerField("Posición", default=0)

    codigo = models.CharField(u"Código", blank=True, max_length=400, null=True)
    def __str__(self):
        return u'%s' % self.nombre


class Subcategoria(models.Model):
    categoria = models.ForeignKey(Categoria, blank=True, null=True, related_name="cat_sub")
    nombre = models.CharField("Nombre", 
                              max_length=400, blank=True, null=True)
    posicion = models.SmallIntegerField("Posición", default=0)

    def __str__(self):
        return u'%s' % self.nombre

class Producto(models.Model):
    subcategoria = models.ForeignKey(Subcategoria,
                                     blank=True, null=True)

    nombre = models.CharField("Nombre", blank=True, null=True, max_length=400)

    imagen = FileBrowseField('Fondo Miniatura Izquierdo', max_length=200,
                              blank=True,
                              extensions=['.jpg', '.png', '.gif'],
                              directory='producto')

    stock = models.IntegerField("Stock", default=0)

    date_creation = models.DateTimeField("Fecha", auto_now_add=True)

    def __str__(self):
        return u'%s' % self.nombre