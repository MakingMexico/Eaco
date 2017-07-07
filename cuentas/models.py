from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

# Create your models here.


class Usuarios(models.Model):
    """docstring for telefono."""

    id_persona = models.OneToOneField(User, related_name='id_persona')
    tel = models.IntegerField(null=True, blank=True)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to="img/img_usr", null=True, blank=True)
    city = models.CharField(max_length=255, default="Mexico")
    location = PlainLocationField(based_fields=['city'], zoom=7, default=(1.0, 1.0))

    def get_image(self):

        try:
            return '<img src="%s" style="display: block; width: 60px;"/>' % self.image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True


class Dispositivos(models.Model):
    """docstring for telefono."""

    owner = models.ForeignKey(Usuarios, null=True, blank=True)
    Nombre = models.CharField(max_length=30)


class Alarma(models.Model):
    """docstring for Alarma"""
    owner = models.ForeignKey(Dispositivos, null=True, blank=True)
    hora = models.CharField(max_length=30)
    image = models.ImageField(upload_to="img/img_usr", null=True, blank=True)
    def get_image(self):

        try:
            return '<img src="%s" style="display: block; width: 60px;"/>' % self.image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True
        