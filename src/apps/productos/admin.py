from django.contrib import admin
from .models import Categoria, Producto, Subcategoria
# Register your models here.

class SubcategoriaInline(admin.StackedInline):
    model = Subcategoria
    extra = 0
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    inlines = SubcategoriaInline,


class ProductoInline(admin.StackedInline):
    model = Producto
    extra = 0

@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    inlines = ProductoInline,
    extra = 0

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass