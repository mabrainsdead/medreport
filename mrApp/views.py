from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from mrApp.models import Paciente, Atendimento
import json
import datetime


from .forms import PacienteForm, ProcurarPacienteForm

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
        
        
        return HttpResponse("Thanks")
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
    
    contexts = []
    
    for obj in Paciente.objects.filter(nome = request.POST['procurar_paciente_post']):
        context = {
            'nome':  obj.nome, 
            'data_nascimento' : obj.data_nascimento,
            'profissao' : obj.profissao,
            'id':obj.id
            }
        
        contexts.append(context)
        
    
    return render(request, 'resultado_pesquisa_paciente.html', {'contexts': contexts})

def conversor_data(date_provided):
    ''' Converte datas para entrada no banco de dados '''
    
    date_converted = datetime.datetime.strptime(date_provided, "%d-%m-%Y").strftime('%Y-%m-%d')
    return date_converted




def pesquisar_datas_atendimento(request):
    ''' Elabora rotina para pesquisa lista de data de atendimentos ''' 
    contexts = []
    
    for datas_atendimento in Atendimento.objects.filter(paciente__id=request.POST['paciente_id']):
        context = {
            'id_atendimento': datas_atendimento.id,
            'data_atendimento': datas_atendimento.data_atendimento,
        }
        
        contexts.append(context)
    
    return render (request, 'resultado_pesquisa_datas_atendimento.html', {'contexts':contexts})

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

        
    

