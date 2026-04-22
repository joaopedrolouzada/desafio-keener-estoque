from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('produto/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
    path('produto/<int:pk>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('produto/<int:pk>/editar/', views.editar_produto, name='editar_produto'),
]
from .views import CadastroView 

urlpatterns = [
    #  outras urls (lista, editar, etc) ...
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('cadastrar_movimentacao/', views.cadastrar_movimentacao, name='cadastrar_movimentacao'),
]
