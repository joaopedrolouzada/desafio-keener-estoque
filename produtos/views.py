from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, MovimentacaoEstoque

def lista_produtos(request):
    busca = request.GET.get('busca')
    if busca:
        produtos = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos = Produto.objects.all()
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        Produto.objects.create(
            nome=request.POST.get('nome'),
            descricao=request.POST.get('descricao'),
            quantidade=int(request.POST.get('quantidade')),
            preco=request.POST.get('preco').replace(',', '.')
        )
        return redirect('lista_produtos')
    return render(request, 'produtos/cadastrar_produto.html')

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.quantidade = int(request.POST.get('quantidade'))
        produto.preco = request.POST.get('preco').replace(',', '.')
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'produtos/editar_produto.html', {'produto': produto})

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/detalhe.html', {'produto': produto})

def cadastrar_movimentacao(request):
    if request.method == 'POST':
        produto = get_object_or_404(Produto, id=request.POST.get('produto'))
        MovimentacaoEstoque.objects.create(
            produto=produto,
            tipo=request.POST.get('tipo'),
            quantidade=int(request.POST.get('quantidade'))
        )
        return redirect('lista_produtos')
    produtos = Produto.objects.all()
    return render(request, 'produtos/cadastrar_movimentacao.html', {'produtos': produtos})

def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirmar_exclusao.html', {'produto': produto})
