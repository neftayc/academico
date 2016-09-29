from django.db import models
from django.template.defaultfilters import slugify

from django.conf import settings
# Create your models here.
class TimeStampModel(models.Model):

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(models.Model):

    nombre = models.CharField(max_length=50)
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Evento(TimeStampModel):

    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(editable=False)
    sumamary = models.TextField(max_length=255)
    contenido = models.TextField()
    categoria = models.ForeignKey(Category)
    lugar = models.CharField(max_length=50)
    inicio = models.DateTimeField()
    finalizado = models.DateTimeField()
    imagen = models.ImageField(upload_to = 'events')
    is_free = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    vistas = models.PositiveIntegerField(default=0)
    organizador = models.ForeignKey(settings.AUTH_USER_MODEL)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super (Evento, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Asistentes(TimeStampModel):

    asistente = models.ForeignKey(settings.AUTH_USER_MODEL)
    evento = models.ManyToManyField(Evento)

    atender = models.BooleanField(default=False)
    has_pagado = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.asistente.username , self.event.nombre)

class Comentarios(TimeStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    evento = models.ForeignKey(Evento)

    content = models.TextField()
    def __str__ (self):
        return "%s %s" % (self.user.username, self.event.name)
