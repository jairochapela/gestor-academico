from django.urls import path, include
from rest_framework import routers

from . import views
from practicas.views import (
    AlumnoListView,
    CursoViewSet,
    EmpresaViewSet,
    HorarioViewSet,
    AlumnoViewSet,
    list_empresas,
)

router = routers.DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('empresas/', list_empresas, name='list_empresas'),
    path('', include(router.urls)),
    path('alumnos/', AlumnoListView.as_view(), name='listado_alumnos'),


    path('', views.frontpage, name='frontpage'),
    path('api/v1/', include(router.urls)),
]
