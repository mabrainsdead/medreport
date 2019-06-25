from django.db import models




# Create your models here.
class Paciente(models.Model):
    
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField(null=False)
    telefone = models.CharField(max_length=20)
    profissao = models.CharField(max_length=100)
    email = models.EmailField(blank=True, unique=True)
    endereco = models.CharField(max_length=200, default = '')
    cidade = models.CharField(max_length=20, default = '')
    estado = models.CharField(max_length=20, default = '')
    
class Atendimento(models.Model):
    data_atendimento = models.DateField(null=False)
    evolucao = models.TextField()
    solicitacao_exame_lab = models.TextField(null = True)
    solicitacao_exame_imagem = models.TextField(null = True)
    atestado = models.TextField(null = True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
class Receituario(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome_droga = models.CharField(max_length=200, default = '')
    apresentacao_droga = models.CharField(max_length=200, default = '')
    quantidade_droga = models.CharField(max_length=200, default = '')
    forma_uso_droga = models.CharField(max_length=200, default = '')
    duracao_uso_droga = models.CharField(max_length=200, default = '')
       
class Post(models.Model):
    text = models.CharField(max_length=200, default = '')
    