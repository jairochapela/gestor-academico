from django.urls import path, include
from practicas.views import list_empresas, AlumnoListView, AlumnoDetailView
from practicas import views

from . import views

urlpatterns = [
    #Listado de empresas
    path('empresas/', list_empresas, name='list_empresas'),
    path('alumnos/', AlumnoListView.as_view(), name='listado_alumnos'),

    path('', views.frontpage, name='frontpage'),
    path('empresas/<int:id>/', views.empresa_detalle, name='empresa_detalle'),  
    path('alumnos/<int:pk>/', AlumnoDetailView.as_view(), name='alumnos_detalle'),
]
