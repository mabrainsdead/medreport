from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from mrApp.models import Paciente


from .forms import PacienteForm, ProcurarPacienteForm

def adicionar_paciente(request):
    '''Adiciona um paciente novo a partir de dados submetidos ou mostra a template vazia para ser preenchida '''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PacienteForm(request.POST)
        query_set = Paciente(
            nome = request.POST['nome'],
            sobrenome = request.POST['sobrenome'],
            data_nascimento = request.POST['data_nascimento'],
            profissao = request.POST['profissao'])
        
        query_set.save()
        
        
        return HttpResponse("Thanks")
    else:
        form = PacienteForm()
    
    return render(request, 'adicionar_paciente.html', {'form': form})

def home(request):
    form_procurar_paciente = ProcurarPacienteForm()
    return render (request, 'home.html', {'form_procurar_paciente': form_procurar_paciente})

def procurar_paciente(request):
    
    return HttpResponse(request.POST['procurar_paciente_post'])