from django.db import models
# Create your models here.
class Produto(models.Model):
    id = models.IntegerField("id", primary_key=True)
    nome = models.CharField("nome", max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    def __str__(self) -> str:
        return self.nome

class Estoque(models.Model):
    id = models.IntegerField("id_estoque", primary_key=True)
    id_produto = models.IntegerField("id_produto")
    quantidade = models.IntegerField("quantidade")
    def __str__(self) -> str:
        return f"{self.id} - {self.quantidade}"
        
class Pedido(models.Model):
    id = models.IntegerField('id_pedido', primary_key=True)
    nome = models.CharField('nome', max_length=100)
    status = models.CharField('status', max_length=100)
    def __str__(self):
        return self.nome