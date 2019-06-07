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
    queixa =  models.TextField()
    evolucao = models.TextField()
    conduta = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)