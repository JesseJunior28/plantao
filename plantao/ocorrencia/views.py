from django.shortcuts import get_object_or_404, render, redirect
from .models import Ocorrencia 
from .forms import OcorrenciaForm


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

