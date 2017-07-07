from django.contrib import admin
from cuentas.models import Usuarios, Dispositivos, Alarma
admin.site.register([Usuarios])
admin.site.register([Dispositivos])
admin.site.register([Alarma])
# Register your models here.
