from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Curso, Empresa, Horario, Alumno
from .serializers import CursoSerializer, EmpresaSerializer, HorarioSerializer, AlumnoSerializer

# Create your views here.


class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer