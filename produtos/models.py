from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

from django.db import models
from django.core.exceptions import 

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [('entrada', 'Entrada'), ('saida', 'Saída')]
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.tipo == 'saida': # Ajustado para 'saida' minusculo como no seu TIPO_CHOICES
            if self.produto.quantidade < self.quantidade:
                raise ValidationError(f"Saldo insuficiente! Estoque atual: {self.produto.quantidade}")
            self.produto.quantidade -= self.quantidade
        else:
            self.produto.quantidade += self.quantidade
        
        self.produto.save()
        super().save(*args, **kwargs)
