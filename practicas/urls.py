from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    
    path('empresas/<int:id>/', views.empresa_detalle, name='empresa_detalle'),  
    path('alumnos/<int:pk>/', views.AlumnoDetailView.as_view(), name='alumno_detalle'),
]
