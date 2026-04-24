from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('detalhe/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
    path('excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
    path('movimentar/', views.cadastrar_movimentacao, name='cadastrar_movimentacao'),
    path('movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
]