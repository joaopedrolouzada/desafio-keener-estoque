from django.db import models

# Create your models here.
from django.db import models

# Certifique-se que o P é maiúsculo!
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class MovimentacaoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    quantidade = models.IntegerField(default=0)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.produto.nome} - {self.tipo} - {self.quantidade}'
