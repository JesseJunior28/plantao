from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import Ocorrencia, Plantao
from .forms import OcorrenciaForm, ComentarioForm, OcorrenciaFilterForm, PlantaoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from urllib.parse import urlencode
from datetime import date, time, datetime


@login_required
def lista_ocorrencia(request):

    agora = datetime.now().time()
    hoje = datetime.now().date()
    
    if time(6, 0) <= agora < time(18, 0):

        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.DIURNO).first()
    else:
        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.NOTURNO).first()

    print(plantao)
    if not plantao:
        messages.warning(request, f'Nenhum plantão iniciado, favor iniciar o plantão!')
        return redirect('iniciar_plantao')

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
    
    context = {
        "ocorrencias": ocorrencias,
        "plantao": plantao,
        'form': form,
        'em_aberto': em_aberto,
        'ocorrencia_id': int(request.GET.get('ocorrencia_id', '0'))
    }
    
    return render(request, "ocorrencia/lista_ocorrencia.html", context)

@login_required
def cadastrar_ocorrencia(request):

    agora = datetime.now().time()
    hoje = datetime.now().date()
    
    if time(6, 0) <= agora < time(18, 0):
        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.DIURNO).first()
    else:
        plantao = Plantao.objects.filter(inicio__date=hoje, turno=Plantao.TurnoPlantao.NOTURNO).first()

    if not plantao:
        messages.warning(request, f'Nenhum plantão iniciado, favor iniciar o plantão!')
        return redirect('iniciar_plantao')
    

    if request.method == "POST":
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            ocorrencia = form.save()
            messages.success(request, f'Ocorrência {ocorrencia.ordem_de_servico} cadastrada com sucesso!')
            return redirect("lista_ocorrencia")
    else:
        form = OcorrenciaForm(initial={'plantonista': request.user, 'plantao': plantao})
        
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
            comentario = form.save()
            base_url = reverse('lista_ocorrencia') # Obtém a URL base
            query_string = urlencode({'ocorrencia_id': comentario.ocorrencia.id }) # Cria a query string
            url = f'{base_url}?{query_string}'
            messages.success(request, f'Comentário adicionado com sucesso!')
            return redirect(url)
        return redirect('lista_ocorrencia')
    return redirect('lista_ocorrencia')


def concluir_ocorrencia(request, ocorrencia_id):
    ocorrencia = get_object_or_404(Ocorrencia, pk=ocorrencia_id)

    ocorrencia.status = Ocorrencia.StatusOcorrencia.CONCLUIDA
    ocorrencia.save()
    messages.success(request, f'Ocorrência {ocorrencia.ordem_de_servico} concluída com sucesso!')
    
    return redirect('lista_ocorrencia')


@login_required
def iniciar_plantao(request):
    if request.method == 'POST':
        form = PlantaoForm(request.POST)
        if form.is_valid():
            plantao = form.save(commit=False)
            plantao.usuario = request.user
            plantao.save()
            messages.success(request,"Plantao iniciado com sucesso!")

            # turno = request.POST.get('turno')
            # inicio = request.POST.get('inicio')
            # Plantao.objects.create(usuario=request.user, turno=turno, inicio=inicio)
        return redirect('lista_ocorrencia')
    return render(request, 'ocorrencia/plantao.html')