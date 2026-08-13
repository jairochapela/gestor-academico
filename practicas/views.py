import logging
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from auditlog.mixins import LogAccessMixin

from .models import Curso, Empresa, Horario, Alumno
from .serializers import CursoSerializer, EmpresaSerializer, HorarioSerializer, AlumnoSerializer

from auditlog.context import set_actor

from django.shortcuts import render, get_object_or_404
from .models import Alumno, Curso
from .models import Empresa, Alumno
from django.views.generic import ListView
from practicas.models import Alumno

logger = logging.getLogger('principal')


def list_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'practicas/list_empresas.html', {
        'empresas': empresas,
    })

def empresa_detalle(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    alumnos = Alumno.objects.filter(empresa=empresa)

    return render(request, 'practicas/empresa_detalle.html', {
        'empresa': empresa,
        'alumnos': alumnos,
    })

# Create your views here.
def lista_alumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'practicas/listado_alumnos.html', {
        'alumnos': alumnos,
    })


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

    def get_queryset(self):
        queryset = Alumno.objects.all()
        curso_id = self.request.query_params.get("curso")

        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)

        return queryset

   
class AlumnoListView(ListView):
    model = Alumno
    template_name = "practicas/listado_alumnos.html"
    context_object_name = "alumnos"

    def get_queryset(self):
        queryset = Alumno.objects.all()
        curso_id = self.request.GET.get("curso")

        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        
        # Pasar el ID del curso seleccionado
        curso_id = self.request.GET.get("curso")
        if curso_id:
            context['selected_curso'] = int(curso_id)
        
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curso_id = self.request.GET.get("curso")

        context["cursos"] = Curso.objects.all()
        context["curso_seleccionado"] = curso_id

        return context

def frontpage(request):
    return render(request, 'practica/frontpage.html')
