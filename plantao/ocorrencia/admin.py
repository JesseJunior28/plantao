from django.contrib import admin


# Importar as classes

from .models import Unidade, Bairro, Ocorrencia, DataSolicitacao, Parecer, SituacaoAguaCliente

# Register your models here.
admin.site.register(Unidade)
admin.site.register(Bairro)
admin.site.register(Ocorrencia)
admin.site.register(DataSolicitacao)
admin.site.register(Parecer)
admin.site.register(SituacaoAguaCliente)