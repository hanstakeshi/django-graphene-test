from django.contrib import admin
from .models import ModelExample, Mensaje
# Register your models here.


@admin.register(ModelExample)
class ModelExampleAdmin(admin.ModelAdmin):
    pass


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    pass

