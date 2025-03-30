from django.contrib import admin
from .models import Unidade, Bairro, Ocorrencia, DataSolicitacao,\
    Parecer, SituacaoAguaCliente, StatusRegiao, Plantao


admin.site.register(Unidade)
admin.site.register(Bairro)
admin.site.register(Ocorrencia)
admin.site.register(DataSolicitacao)
admin.site.register(Parecer)
admin.site.register(SituacaoAguaCliente)
admin.site.register(StatusRegiao)
admin.site.register(Plantao)
