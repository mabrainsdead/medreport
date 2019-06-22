from django.urls import path, include
from django.views.generic import TemplateView


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar_paciente', views.adicionar_paciente, name = 'adicionar_paciente'),
    path('procurar_paciente', views.procurar_paciente, name= 'procurar_paciente'),
    path('search', views.search, name = 'search'),
    path('ajax', views.ajax, name  = 'ajax'),
    path('pesquisar_datas_atendimento', views.pesquisar_datas_atendimento, name = 'pesquisar_datas_atendimento'),
    path('pesquisar_conteudo_atendimento', views.pesquisar_conteudo_atendimento, name = 'pesquisar_conteudo_atendimento'),
    path('cadastrar_atendimento', views.cadastrar_atendimento, name = 'cadastrar_atendimento'),
    path('inserir_texto_ajax', views.inserir_texto_ajax, name = 'inserir_texto_ajax'),
    path('ajax', views.ajax, name = 'ajax'),
    path('adicionar_prescricao', views.adicionar_prescricao, name = 'adicionar_prescricao'),
  
    
    
    ]