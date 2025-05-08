from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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


class Comentario(models.Model):
    ocorrencia = models.ForeignKey('Ocorrencia', on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField('Texto')
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comentarios", verbose_name="Plantonista")
    def __str__(self):
        return f"Comentário de {self.autor} em {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"



class Plantao(models.Model):
    class TurnoPlantao(models.TextChoices):
        DIURNO = 'DIURNO', 'Diurno'
        NOTURNO = 'NOTURNO', 'Noturno'
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    inicio = models.DateTimeField(default=timezone.now)
    turno = models.CharField(max_length=10, choices=TurnoPlantao.choices)

    class Meta:
        verbose_name_plural = 'Plantões'
        verbose_name = 'Plantão'

    def __str__(self):
        return f"{self.usuario.username} - {self.inicio.strftime('%d/%m/%Y %H:%M') } - {self.turno}"


class Ocorrencia(models.Model):
    class StatusOcorrencia(models.TextChoices):
        EM_ABERTO = 'EM_ABERTO', 'Em Aberto'
        CONCLUIDA = 'CONCLUIDA', 'Concluida'
    ordem_de_servico = models.IntegerField('OS')
    matricula = models.IntegerField('Matricula')
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, related_name="ocorrencias")
    data_solicitacao = models.DateTimeField('Data da Solicitação')
    parecer = models.ForeignKey(Parecer, on_delete=models.SET_NULL, null=True, related_name="ocorrencias", verbose_name="Parecer")
    situacao_agua_cliente = models.ForeignKey(SituacaoAguaCliente, on_delete=models.SET_NULL,null=True, related_name="ocorrencias", verbose_name="Situação da Água do Cliente")
    status_regiao = models.ForeignKey(StatusRegiao, on_delete=models.SET_NULL, null=True, related_name="ocorrencias", verbose_name="Status da Região")
    plantonista = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="ocorrencias", verbose_name="Plantonista")
    plantao = models.ForeignKey(Plantao, on_delete=models.SET_NULL, null=True, related_name="ocorrencias", verbose_name="Plantao")
    status = models.CharField(
        'Status',
        max_length=10,
        choices=StatusOcorrencia.choices,
        default=StatusOcorrencia.EM_ABERTO,
    )
    descricao = models.TextField('Descrição',blank=True, null=True)

    @property
    def em_aberto(self):
        return self.status == self.StatusOcorrencia.EM_ABERTO
    
    @property
    def conluida(self):
        return self.status == self.StatusOcorrencia.CONCLUIDA
        

    def __str__(self):
        ordem_codigo = self.ordem_de_servico if self.ordem_de_servico else "Sem OS"
        return f"Ocorrência {self.id} - {ordem_codigo}"
