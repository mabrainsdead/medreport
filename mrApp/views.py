from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from mrApp.models import Paciente, Atendimento, Post, Receituario
import json
import datetime
import logging
from django.urls import reverse

from .forms import PacienteForm, ProcurarPacienteForm, AtendimentoForm, ReceituarioForm, PostForm

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

def adicionar_paciente(request):
    '''Adiciona um paciente novo a partir de dados submetidos ou mostra a template vazia para ser preenchida '''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PacienteForm(request.POST)
        query_set = Paciente(
            nome = request.POST['nome'],
            data_nascimento = conversor_data(request.POST['data_nascimento']),
            profissao = request.POST['profissao'],
            email = request.POST['email'],
            telefone = request.POST['telefone'],
            endereco = request.POST['endereco'],
            cidade = request.POST['cidade'],
            estado = request.POST['estado'])     
        
        query_set.save()        
        form = AtendimentoForm() #Instancia form de anamnese para mandar via context
        
        paciente = get_object_or_404(Paciente, email=request.POST['email'])
        
          
        
        return render(request, 'cadastrar_atendimento.html', {'form_anamnese': form, 'paciente':paciente})
    
    else:
        form = PacienteForm()
    
    return render(request, 'adicionar_paciente.html', {'form': form})

def home(request):
    form_procurar_paciente = ProcurarPacienteForm()
    return render (request, 'home.html', {'form_procurar_paciente': form_procurar_paciente})

def search(request):
    if request.is_ajax():
        q = request.GET.get('term','')
        names = Paciente.objects.filter(nome__contains=q)
        result = []
        for n in names:
            name_json = n.nome
            result.append(name_json)
        data = json.dumps(result)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def procurar_paciente(request):
    ''' Elabora rotina para pesquisar paciente  já cadastrado '''
    
    paciente = get_object_or_404(Paciente, nome = request.POST['procurar_paciente_post'])
        
    return render(request, 'resultado_pesquisa_paciente.html', {'paciente':paciente}) 

def conversor_data(date_provided):
    ''' Converte datas para entrada no banco de dados '''
    
    date_converted = datetime.datetime.strptime(date_provided, "%d-%m-%Y").strftime('%Y-%m-%d')
    return date_converted

def pesquisar_datas_atendimento(request, paciente_id):
    ''' Elabora rotina para pesquisa lista de data de atendimentos ''' 
    contexts = []
    
    for datas_atendimento in Atendimento.objects.filter(paciente__id=request.POST['paciente_id']):
        context = {
            'id_atendimento': datas_atendimento.id,
            'data_atendimento': datas_atendimento.data_atendimento,
        }
        
        contexts.append(context)
    
    return render (request, 'resultado_pesquisa_datas_atendimento.html', {'contexts':contexts, 'paciente_id':request.POST['paciente_id']})

def pesquisar_conteudo_atendimento(request):
    '''Mostra conteúdo de atendimento por data '''
    for conteudo_atendimento in Atendimento.objects.filter(id = request.POST['id_atendimento']):
        context = {
            'data_atendimento': conteudo_atendimento.data_atendimento,
            'queixa': conteudo_atendimento.queixa,
            'evolucao': conteudo_atendimento.evolucao,
            'conduta' : conteudo_atendimento.conduta
        }
    return render(request, 'conteudo_atendimento.html', {'context':context}) 
   
def cadastrar_atendimento(request, paciente_id):
    if request.method == 'POST': #se esta view for acionada pelo template cadastrar_atendimento.html
        
        if not request.POST['data_atendimento']:
            query_set = Atendimento(
                data_atendimento = datetime.date.today(),
                evolucao = request.POST['evolucao'],
                paciente_id = request.POST['paciente_id'], 
                )
        else:
            query_set = Atendimento(
                data_atendimento = conversor_data(request.POST['data_atendimento']),
                evolucao = request.POST['evolucao'],
                paciente_id = request.POST['paciente_id'], 
                )
        
        
        query_set.save()
        return HttpResponseRedirect(reverse('pesquisar_datas_atendimento', args=(request.POST['paciente_id'])))
        
    else:
        
        paciente = get_object_or_404(Paciente, pk=paciente_id)
        
        try:
            form_anamnese = AtendimentoForm()
            return render(request, 'cadastrar_atendimento.html', {'form_anamnese': form_anamnese, 'paciente':paciente})
        except (KeyError, Paciente.DoesNotExist):
            return HttpResponse("erro")
        
  
def inserir_texto_ajax(request):
    if request.method=='POST':
        
        obj = Post(text = request.POST['text'])
        obj.save()
    
        return JsonResponse({'error':'something bad'})
        
    
    else:
        return HttpResponse ("erro")

def ajax(request):
    return render(request, 'ajax_test.html')

def adicionar_prescricao(request):
    '''Rotina para acrescentar, modificar e deletar prescrição no atendimento '''
    
    if request.method == 'POST':
        if request.POST['action'] == 'Salvar e fechar':
            '''Rotina para salvar e voltar ao atendimento '''
            return HttpResponse('Salvar e Fechar')
        
        
        if request.POST['action'] == 'Salvar e adicionar outra medicação':
            '''Rotina para salvar e recarregar formulário para nova medicação'''
            
            return HttpResponse('Salvar e adicionar outra medicação')
    else :
        '''Exibir formulário vazio no redirecionamento do template'''
        form = ReceituarioForm()
    
        return render(request, 'adicionar_prescricao.html', {'form': form})
    
    
def detail(request, question_id):
    return HttpResponse(question_id)


    






        
    

