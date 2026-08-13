from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    
    path('empresas/<int:id>/', views.empresa_detalle, name='empresa_detalle'),  
    path('alumnos/<int:id>/', views.alumnos_detalle, name='alumnos_detalle'),     
]
