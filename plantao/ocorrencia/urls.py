from django.urls import path
from .views import cadastrar_ocorrencia

urlpatterns = [
    path('', cadastrar_ocorrencia, name='cadastrar_ocorrencia'),  
]