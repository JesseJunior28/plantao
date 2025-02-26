from django import forms
from .models import Ocorrencia, DataSolicitacao, Parecer, SituacaoAguaCliente
from django.contrib.admin.widgets import AdminDateWidget

class OcorrenciaForm(forms.ModelForm):
    class Meta: 
        model = Ocorrencia
        fields = '__all__'

class DataSolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = '__all__'
        widgets = {
            'data_de_solicitacao': AdminDateWidget()
        }

class Parecer(forms.ModelForm):
    class Meta:
        model = Parecer
        fields = '__all__'

class SituacaoAguaCliente(forms.ModelForm):
    class Meta:
        model = SituacaoAguaCliente
        fields = '__all__'
