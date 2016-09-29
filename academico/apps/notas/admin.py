from django.contrib import admin

from .models import Evento, Category, Asistentes, Comentarios
# Register your models here.

admin.site.register(Evento)
admin.site.register(Category)
admin.site.register(Asistentes)
admin.site.register(Comentarios)
