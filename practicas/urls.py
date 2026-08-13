from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CursoViewSet, 
    EmpresaViewSet, 
    HorarioViewSet, 
    AlumnoViewSet, 
    CursoListView
)

<<<<<<< HEAD
router = DefaultRouter()
=======
from . import views
from practicas.views import (
    CursoViewSet,
    EmpresaViewSet,
    HorarioViewSet,
    AlumnoViewSet,
)

router = routers.DefaultRouter()
>>>>>>> 7a14db6154e221ee24ac06aa796621a90e98c313
router.register(r'cursos', CursoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
<<<<<<< HEAD
    # Vista HTML del listado (Accesible en /api/v1/listado-cursos/)
    path('listado-cursos/', CursoListView.as_view(), name='curso-list-web'),
    
    # Endpoints de la API REST (Accesibles en /api/v1/cursos/, etc.)
    path('', include(router.urls)),
=======
    path('', views.frontpage, name='frontpage'),
    path('api/v1/', include(router.urls)),
>>>>>>> 7a14db6154e221ee24ac06aa796621a90e98c313
]