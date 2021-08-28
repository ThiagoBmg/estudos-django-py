from django.contrib import admin
from .models import Produto, Estoque, Pedido

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantidade')
    list_filter = [('id')]

class PedidoAdmin(admin.ModelAdmin):
    list_display =  ('id', 'nome')

# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Pedido, PedidoAdmin)