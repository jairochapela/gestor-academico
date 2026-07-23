import logging
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from auditlog.mixins import LogAccessMixin

from .models import Curso, Empresa, Horario, Alumno
from .serializers import CursoSerializer, EmpresaSerializer, HorarioSerializer, AlumnoSerializer

from auditlog.context import set_actor


logger = logging.getLogger('principal')


# Create your views here.


class AuditlogActorMixin:
    def _actor_context(self):
        user = getattr(self.request, 'user', None)
        if user is not None and user.is_authenticated:
            return set_actor(user)
        return set_actor(None)

    def create(self, request, *args, **kwargs):
        with self._actor_context():
            logger.info(f"Request data for creating {self.__class__.__name__}: {request.data} with user: {request.user}")
            return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        with self._actor_context():
            logger.info(f"Request data for updating {self.__class__.__name__}: {request.data} with user: {request.user}")
            return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        with self._actor_context():
            logger.info(f"Request data for partially updating {self.__class__.__name__}: {request.data} with user: {request.user}")
            return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        with self._actor_context():
            logger.info(f"Request data for deleting {self.__class__.__name__}: {request.data} with user: {request.user}")
            return super().destroy(request, *args, **kwargs)


class CursoViewSet(AuditlogActorMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EmpresaViewSet(AuditlogActorMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class HorarioViewSet(AuditlogActorMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class AlumnoViewSet(AuditlogActorMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer