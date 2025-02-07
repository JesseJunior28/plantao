from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ocorrencia
from .forms import OcorrenciaForm


# Create your views here.

def inserir_ocorrencia(request):
    form = OcorrenciaForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("Listar_ocorrencias")
        
    return render(request, "ocorrencias/inserir_ocorrencia.html", {"form": form}
)