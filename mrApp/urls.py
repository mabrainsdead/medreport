from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar_paciente', views.adicionar_paciente, name = 'adicionar_paciente'),
    path('procurar_paciente', views.procurar_paciente, name= 'procurar_paciente'),
    
    
    ]