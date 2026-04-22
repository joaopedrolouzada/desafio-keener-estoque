from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    # Pega o que o usuário digitou no campo chamado 'busca'
    nome_a_buscar = request.GET.get('busca')
    
    if nome_a_buscar:
        
        produtos = Produto.objects.filter(nome__icontains=nome_a_buscar)
    else:

        produtos = Produto.objects.all()
        
    return render(request, 'produtos/lista.html', {'produtos': produtos})

from django.shortcuts import render, get_object_or_404 
from .models import Produto, MovimentacaoEstoque

def lista_movimentacoes(request):
    movimentacoes = MovimentacaoEstoque.objects.all()
    return render(request, 'produtos/lista_movimentacoes.html', {'movimentacoes': movimentacoes})

def cadastrar_movimentacao(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto')
        tipo = request.POST.get('tipo')
        quantidade = request.POST.get('quantidade')
        produto = Produto.objects.get(id=produto_id)
        movimentacao = MovimentacaoEstoque(produto=produto, tipo=tipo, quantidade=quantidade)
        movimentacao.save()
        return redirect('lista_movimentacoes')
    produtos = Produto.objects.all()
    return render(request, 'produtos/cadastrar_movimentacao.html', {'produtos': produtos})
from django.shortcuts import render, get_object_or_404 
from .models import Produto

# ... (mantem a função lista_produtos aqui)

def detalhe_produto(request, pk):
    # Busca o produto pela Chave Primária (ID). Se não existir, mostra erro 404.
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/detalhe.html', {'produto': produto})
from django.shortcuts import render, get_object_or_404, redirect 

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        #  dados novos do formulário
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.quantidade = request.POST.get('quantidade')
        produto.preco = request.POST.get('preco').replace(',', '.') # Garante que salve com ponto
        produto.save()
        return redirect('detalhe_produto', pk=produto.pk)
    return render(request, 'produtos/editar_produto.html', {'produto': produto})
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class CadastroView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/cadastro.html'
