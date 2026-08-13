from django.urls import path, include
from rest_framework import routers

from . import views
from practicas.views import (
    CursoViewSet,
    EmpresaViewSet,
    HorarioViewSet,
    AlumnoViewSet,
)

router = routers.DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('api/v1/', include(router.urls)),
]