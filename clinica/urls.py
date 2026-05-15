from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medicos/', views.listar_medicos, name= 'listar_medicos'),
    path('agenda/', views.agenda_clinica, name= 'agenda'),
    path('novo/', views.novo_agendamento, name= 'novo_agendamento'),
    path('editar/<int:pk>/', views.editar_consulta, name='editar_consulta'),
    path('excluir/<int:pk>/', views.excluir_consulta, name='excluir_consulta'),
]