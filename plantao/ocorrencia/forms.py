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
            "data_solicitacao": forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            "situacao_agua_cliente": forms.Select(attrs={'class': 'form-control'}),
            "status_regiao": forms.Select(attrs={'class': 'form-control'}),
            "plantonista": forms.HiddenInput,
        }


class OcorrenciaFilterForm(forms.ModelForm):
    class Meta: 
        model = Ocorrencia
        fields = ['bairro', 'parecer', 'data_solicitacao', 'situacao_agua_cliente', 'status_regiao', 'status']
        widgets = {
            "bairro": forms.Select(attrs={'class': 'form-control'}),
            "parecer": forms.Select(attrs={'class': 'form-control'}),
            "data_solicitacao": forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            "situacao_agua_cliente": forms.Select(attrs={'class': 'form-control'}),
            "status_regiao": forms.Select(attrs={'class': 'form-control'}),
            "status": forms.Select(attrs={'class': 'form-control'}),
            # "plantonista": forms.HiddenInput,
        }
    
    def __init__(self, *args, **kwargs):
        super(OcorrenciaFilterForm, self).__init__(*args, **kwargs)
        self.fields['data_solicitacao'].required = False
        self.fields['bairro'].empty_label = 'Bairro'
        self.fields['bairro'].required = False
        self.fields['parecer'].empty_label = 'Parecer'
        self.fields['parecer'].required = False
        self.fields['status_regiao'].empty_label = 'Status da Região'
        self.fields['status_regiao'].required = False
        self.fields['status'].empty_label = 'Status da Ocorência'
        self.fields['status'].required = False
        self.fields['status'].initial = Ocorrencia.StatusOcorrencia.EM_ABERTO
        self.fields['situacao_agua_cliente'].empty_label = 'Situação da Água do Cliente'
        self.fields['situacao_agua_cliente'].required = False


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
        fields = ['texto', 'user', 'ocorrencia']