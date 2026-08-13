from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('empresas/', views.list_empresas, name='list_empresas'),    
    path('empresas/<int:id>/', views.empresa_detalle, name='empresa_detalle'),  
    path('alumnos/', views.lista_alumno, name='lista_alumno'),
    path('alumnos/<int:pk>/', views.AlumnoDetailView.as_view(), name='alumno_detalle'),
    # TODO path('cursos/', views.lista_curso, name='lista_curso'),
    # TODO path('cursos/<int:pk>/', views.CursoDetailView.as_view(), name='curso_detalle'),
]
