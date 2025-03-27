from django.urls import path
from . views import lista_ocorrencia, cadastrar_ocorrencia, editar_ocorrencia, excluir_ocorrencia, comentario_ocorrencia

urlpatterns = [
    path('lista/', lista_ocorrencia, name='lista_ocorrencia'),
    path('cadastrar/', cadastrar_ocorrencia, name='cadastrar_ocorrencia'),
    path('editar/<int:id>/', editar_ocorrencia, name='editar_ocorrencia'),
    path('excluir/<int:id>/', excluir_ocorrencia, name='excluir_ocorrencia'),
    path('comentario/<int:id>/', comentario_ocorrencia, name='comentario_ocorrencia')
]