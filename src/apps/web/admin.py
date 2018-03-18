from django.contrib import admin
from .models import ModelExample
# Register your models here.


@admin.register(ModelExample)
class ModelExampleAdmin(admin.ModelAdmin):
	pass