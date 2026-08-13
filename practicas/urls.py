from django.urls import path

from . import views

urlpatterns = [
    # Portada
    path('', views.frontpage, name='frontpage'),

    # Vistas HTML
    path('empresas/lista/', views.list_empresas, name='list_empresas'),
    path('alumnos/lista/', views.AlumnoListView.as_view(), name='listado_alumnos'),
]