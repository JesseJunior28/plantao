from django.urls import path
from .views import IndexView, cadastrar_ocorrencia

urlpatterns = [
    path('inicio/', IndexView.as_view(), name='inserir_ocorrencia'),
    path("cadastrar/", cadastrar_ocorrencia, name="cadastrar_ocorrencia"),
]