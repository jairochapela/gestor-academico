from django.urls import path, include
from rest_framework.routers import DefaultRouter
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
    # Vista HTML del listado (Accesible en /api/v1/listado-cursos/)
    path('listado-cursos/', CursoListView.as_view(), name='curso-list-web'),
    
    # Endpoints de la API REST (Accesibles en /api/v1/cursos/, etc.)
    path('', include(router.urls)),
]