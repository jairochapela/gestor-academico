from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    CursoViewSet, 
    EmpresaViewSet, 
    HorarioViewSet, 
    AlumnoViewSet, 
    CursoListView
)

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    # Vista principal agregada por el equipo
    path('', views.frontpage, name='frontpage'),

    # Vista HTML del listado
    path('listado-cursos/', CursoListView.as_view(), name='curso-list-web'),
    
    # Endpoints de la API REST
    path('', include(router.urls)),
]