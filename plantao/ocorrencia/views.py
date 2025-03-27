from django.shortcuts import get_object_or_404, render, redirect
from .models import Ocorrencia 
from .forms import OcorrenciaForm, ComentarioForm


# Create your views here.

#class IndexView(TemplateView):
    #template_name = "index.html"  

def lista_ocorrencia(request):
    ocorrencias = Ocorrencia.objects.all()
    return render(request, "ocorrencia/lista_ocorrencia.html", {"ocorrencias": ocorrencias})

def cadastrar_ocorrencia(request):
    form = OcorrenciaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("lista_ocorrencia")
        
    return render(request, "ocorrencia/cadastrar_ocorrencia.html", {"form": form})


def editar_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, instance=ocorrencia)
        if form.is_valid():
            form.save()
            return redirect('lista_ocorrencia')
    else:
        form = OcorrenciaForm(instance=ocorrencia)
    return render(request, 'ocorrencia/editar_ocorrencia.html', {'form': form})

def excluir_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    ocorrencia.delete()
    return redirect('lista_ocorrencia')

def comentario_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    comentarios = ocorrencia.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.ocorrencia = ocorrencia
            comentario.save()
            return redirect('comentario_ocorrencia', id=ocorrencia.id)  # Redireciona para a mesma página, mostrando o novo comentário
    else:
        form = ComentarioForm()

    return render(request, 'ocorrencia/comentario_ocorrencia.html', {
        'ocorrencia': ocorrencia,
        'comentarios': comentarios,
        'form': form
    })