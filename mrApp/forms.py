from django import forms



class PacienteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    sobrenome = forms.CharField(label='Sobrenome', max_length=100)
    data_nascimento = forms.DateField(label = 'Data de Nascimento')
    profissao = forms.CharField(label='Profissao', max_length=100)
    
class ProcurarPacienteForm(forms.Form):
    procurar_paciente_post = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Procurar..', 'id':'procurar_paciente'}), max_length=100)
    