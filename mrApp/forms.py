from django import forms
from django.conf import settings
from mrApp.models import Paciente



class PacienteForm(forms.Form):
    
    nome = forms.CharField(label='Nome', max_length=100)    
    data_nascimento = forms.DateField(label = 'Data de Nascimento', widget = forms.DateInput(attrs={'id':'data'}))
    profissao = forms.CharField(label='Profissao', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=20)
    email = forms.EmailField(label = 'Email', max_length=50)
    endereco = forms.CharField(label = 'Endereço', max_length = 200)
    cidade = forms.CharField(label = 'Cidade', max_length=20)
    estado = forms.CharField(label = 'Estado', max_length=20)
    
    class Meta:
        model = Paciente
    
class ProcurarPacienteForm(forms.Form):
    procurar_paciente_post = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Procurar..', 'id':'procurar_paciente'}), max_length=100)
    