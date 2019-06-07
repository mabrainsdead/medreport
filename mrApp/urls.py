from django.urls import path, include
from django.views.generic import TemplateView


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar_paciente', views.adicionar_paciente, name = 'adicionar_paciente'),
    path('procurar_paciente', views.procurar_paciente, name= 'procurar_paciente'),
    path('search', views.search, name = 'search'),
    path('ajax', TemplateView.as_view(template_name='ajax_test.html')),
    path('pesquisar_datas_atendimento', views.pesquisar_datas_atendimento, name = 'pesquisar_datas_atendimento'),
    path('pesquisar_conteudo_atendimento', views.pesquisar_conteudo_atendimento, name = 'pesquisar_conteudo_atendimento'),
    
    
    ]