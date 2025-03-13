from django.db import models


# Create your models here.


class Unidade(models.Model):
    nome = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.nome
    
class Matricula(models.Model):
    codigo = models.IntegerField(unique=True)  

    def __str__(self):
        return str(self.codigo)  
    
class Bairro(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="bairros")

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"

class OrdemDeServico(models.Model):
    codigo = models.IntegerField(unique=True)
    
    def __str__(self):
        return str(self.codigo)

class DataSolicitacao(models.Model):
    data = models.DateField()

    def __str__(self):
        return self.data.strftime("%d/%m/%Y")

class Parecer(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class StatusRegiao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class SituacaoAguaCliente(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    

class Ocorrencia(models.Model):
    ordem_de_servico = models.IntegerField()
    matricula = models.IntegerField()
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, related_name="ocorrencias")
    data_solicitacao = models.DateField()
    parecer = models.ForeignKey(Parecer, on_delete=models.SET_NULL, null=True, related_name="ocorrencias")
    situacao_agua_cliente = models.ForeignKey(SituacaoAguaCliente, on_delete=models.SET_NULL,null=True, related_name="ocorrencias")
    status_regiao = models.ForeignKey(StatusRegiao, on_delete=models.SET_NULL, null=True, related_name="ocorrencias")
    descricao = models.TextField()

    def __str__(self):
        ordem_codigo = self.ordem_de_servico if self.ordem_de_servico else "Sem OS"
        return f"Ocorrência {self.id} - {ordem_codigo}"
