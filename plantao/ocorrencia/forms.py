from django import forms
from .models import Ocorrencia, DataSolicitacao, Parecer, SituacaoAguaCliente

class OcorrenciaForm(forms.ModelForm):
    class Meta: 
        model = Ocorrencia
        fields = '__all__'

class DataSolicitacaoForm(forms.ModelForm):
    class Meta:
        model = DataSolicitacao
        fields = '__all__'

class Parecer(forms.Modelform):
    class Meta:
        model = Parecer
        fields = '__all__'

class SituacaoAguaCliente(forms.ModeForm):
    class Meta:
        model = SituacaoAguaCliente
        fields = '__all__'
