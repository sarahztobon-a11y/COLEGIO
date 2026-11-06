from rest_framework import serializers
from .models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']

class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source='autor.nombre', read_only=True)

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'autor_nombre', 'precio', 'disponible', 'fecha_publicacion']

def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que cero.")
        return value

def validate(self, data):
        # Validación que involucra más de un campo a la vez
        if not data.get('disponible', True) and data.get('precio', 0) == 0:
            raise serializers.ValidationError("Un libro no disponible no puede tener precio 0.")
        return data