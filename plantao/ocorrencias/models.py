from django.db import models

# Create your models here.

class Unidades(models.Model):
    nome = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.nome
    
class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"

class Ocorrencia(models.model):
    codigo = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.codigo)

class DataSolicitacao(models.Model):
    data = models.DateField()

    def __str__(self):
        return self.data.strftime("%d/%m/%y")

class Parecer(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class SituacaoAguaCliente(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
    