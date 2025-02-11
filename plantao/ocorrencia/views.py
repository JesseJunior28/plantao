from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import OcorrenciaForm
from django.views.generic import TemplateView 


# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"  

def cadastrar_ocorrencia(request):
    form = OcorrenciaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("Lista_ocorrencias")
        
    return render(request, "ocorrencias/inserir_ocorrencia.html", {"form": form})
