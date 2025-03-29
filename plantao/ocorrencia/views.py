from django.shortcuts import get_object_or_404, render, redirect
from .models import Ocorrencia 
from .forms import OcorrenciaForm, ComentarioForm, OcorrenciaFilterForm, Comentario
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def lista_ocorrencia(request):
    ocorrencias = Ocorrencia.objects.all()
    em_aberto = ocorrencias.filter(status=Ocorrencia.StatusOcorrencia.EM_ABERTO).count()
    form = OcorrenciaFilterForm(request.GET, initial={'status': Ocorrencia.StatusOcorrencia.EM_ABERTO})

    if request.GET.get('bairro'):
        ocorrencias = ocorrencias.filter(bairro=request.GET.get('bairro'))
    if request.GET.get('parecer'):
        ocorrencias = ocorrencias.filter(parecer=request.GET.get('parecer'))
    if request.GET.get('data_solicitacao'):
        ocorrencias = ocorrencias.filter(data_solicitacao=request.GET.get('data_solicitacao'))
    if request.GET.get('situacao_agua_cliente'):
        ocorrencias = ocorrencias.filter(situacao_agua_cliente=request.GET.get('situacao_agua_cliente'))
    if request.GET.get('status_regiao'):
        ocorrencias = ocorrencias.filter(status_regiao=request.GET.get('status_regiao'))
    if request.GET.get('status', Ocorrencia.StatusOcorrencia.EM_ABERTO):
        status = request.GET.get('status', Ocorrencia.StatusOcorrencia.EM_ABERTO)
        ocorrencias = ocorrencias.filter(status=status)

    return render(request, "ocorrencia/lista_ocorrencia.html", {"ocorrencias": ocorrencias, 'form': form, 'em_aberto': em_aberto})

@login_required
def cadastrar_ocorrencia(request):
    

    if request.method == "POST":
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            ocorrencia = form.save()
            messages.success(request, f'Ocorrência {ocorrencia.ordem_de_servico} cadastrada com sucesso!')
            return redirect("lista_ocorrencia")
    else:
        form = OcorrenciaForm(initial={'plantonista': request.user})
        
    return render(request, "ocorrencia/cadastrar_ocorrencia.html", {"form": form})


def editar_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ocorrência {ocorrencia.ordem_de_servico} editada com sucesso!')
            return redirect('lista_ocorrencia')
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    return render(request, 'ocorrencia/editar_ocorrencia.html', {'form': form})


def excluir_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, id=ocorrencia_id)
    ocorrencia.delete()
    messages.warning(request, f'Ocorrência excluída com sucesso!')
    return redirect('lista_ocorrencia')


def adicionar_comentario(request):
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ocorrencia')
        return redirect('lista_ocorrencia')
    return redirect('lista_ocorrencia')


def concluir_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

    ocorrencia.status = Ocorrencia.StatusOcorrencia.CONCLUIDA
    ocorrencia.save()
    messages.success(request, f'Ocorrência {ocorrencia.ordem_de_servico} concluída com sucesso!')
    
    return redirect('lista_ocorrencia')