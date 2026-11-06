from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets  

from .models import Libro, Autor  
from .serializers import AutorSerializer, LibroSerializer

def resumen(request):
    total = Libro.objects.count()
    return HttpResponse(f"Actualmente hay {total} libros registrados en la biblioteca.")

@api_view(['GET'])
def listado_libros(request):
    libros = Libro.objects.all()
    datos = [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor.nombre,
            "precio": libro.precio,
            "disponible": libro.disponible,
        }
        for libro in libros
    ]
    return Response(datos)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('titulo')
    serializer_class = LibroSerializer