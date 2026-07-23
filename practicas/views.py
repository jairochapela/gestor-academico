from django.shortcuts import render
import logging
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated

from .models import Curso, Empresa, Horario, Alumno
from .serializers import CursoSerializer, EmpresaSerializer, HorarioSerializer, AlumnoSerializer

logger = logging.getLogger('principal')


# Create your views here.



class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def list(self, request, *args, **kwargs):
        # Logging the request data for debugging purposes using Django logging facilities
        logger.info(f"Request data for listing Cursos: {request.data}")
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # Logging the request data for debugging purposes using Django logging facilities
        logger.info(f"Request data for creating Curso: {request.data}")
        return super().create(request, *args, **kwargs)

class EmpresaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer