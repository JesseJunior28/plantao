from django import forms
from .models import Ocorrencia, DataSolicitacao, Parecer, SituacaoAguaCliente, Comentario
from django.contrib.admin.widgets import AdminDateWidget

class OcorrenciaForm(forms.ModelForm):
    class Meta: 
        model = Ocorrencia
        fields = '__all__'
        widgets = {
            "bairro": forms.Select(attrs={'class': 'form-control'}),
            "parecer": forms.Select(attrs={'class': 'form-control'}),
            "situacao_agua_cliente": forms.Select(attrs={'class': 'form-control'}),
            "status_regiao": forms.Select(attrs={'class': 'form-control'}),
        }

class DataSolicitacaoForm(forms.ModelForm):
    class Meta:
        model = DataSolicitacao
        fields = '__all__'
        widgets = {
            'data_de_solicitacao': AdminDateWidget()
        }

class ParecerForm(forms.ModelForm):
    class Meta:
        model = Parecer
        fields = '__all__'

class SituacaoAguaClienteForm(forms.ModelForm):
    class Meta:
        model = SituacaoAguaCliente
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']