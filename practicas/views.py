import logging
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from auditlog.context import set_actor

from .models import Curso, Empresa, Horario, Alumno
from .serializers import CursoSerializer, EmpresaSerializer, HorarioSerializer, AlumnoSerializer

from auditlog.context import set_actor

from django.shortcuts import render, get_object_or_404
from .models import Alumno, Curso
from .models import Empresa, Alumno
from django.views.generic import DetailView, ListView
from practicas.models import Alumno

logger = logging.getLogger('principal')


# --- VISTAS WEB (HTML) ---

def frontpage(request):
    return render(request, 'practica/frontpage.html')


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

class CursoListView(ListView):
    model = Curso
    template_name = 'practicas/curso_list.html'
    context_object_name = 'cursos'
    paginate_by = 10
# Create your views here.
def lista_alumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'practicas/listado_alumnos.html', {
        'alumnos': alumnos,
    })

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nombre__icontains=q)
        return queryset


class AlumnoListView(ListView):
    model = Alumno
    template_name = "alumnos/listado.html"
    context_object_name = "alumnos"

    def get_queryset(self):
        queryset = Alumno.objects.all()
        curso_id = self.request.GET.get("curso")

        if curso_id:
            queryset = queryset.filter(curso_id=curso_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curso_id = self.request.GET.get("curso")

        context["cursos"] = Curso.objects.all()
        context["curso_seleccionado"] = curso_id

        return context


# --- MIXINS ---

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


# --- VIEWSETS (API REST) ---

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




class AlumnoDetailView(DetailView):
    model = Alumno
    # template_name = "alumnos/detalle.html"  # Ajusta al nombre de tu plantilla
    context_object_name = "alumno"

    # def get_queryset(self):
    #     alumno_id = self.kwargs.get("id")
    #     return Alumno.objects.filter(id=alumno_id)
