from django.contrib import admin
from biblioteca.models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'precio', 'disponible')
    list_filter = ('disponible', 'autor')
    search_fields = ('titulo',)  