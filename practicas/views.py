import logging
from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from django.db.models import Count
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.rest_framework import DjangoFilterBackend
from auditlog.context import set_actor

from .models import Curso, Empresa, Horario, Alumno
from .serializers import CursoSerializer, EmpresaSerializer, HorarioSerializer, AlumnoSerializer

from auditlog.context import set_actor

from django.shortcuts import render


logger = logging.getLogger('principal')

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

# --- VIEWSETS (API) ---

class CursoViewSet(AuditlogActorMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'descripcion']
    filterset_fields = ['fecha_inicio', 'fecha_fin']
    ordering_fields = ['nombre', 'fecha_inicio', 'fecha_fin']
    ordering = ['-fecha_inicio']

    def get_queryset(self):
        return Curso.objects.annotate(total_alumnos=Count('alumno'))

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

# --- VISTA HTML ---

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'practica/curso_list.html'
    context_object_name = 'cursos'
    paginate_by = 10
    ordering = ['-fecha_inicio']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nombre__icontains=query)
        return queryset
    

def frontpage(request):
    return render(request, 'practica/frontpage.html')
