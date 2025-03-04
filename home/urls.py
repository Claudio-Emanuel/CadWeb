from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('categoria', views.categoria, name='categoria'),
    path('formularioCategoria' , views.form_categoria, name='formulario'),
    path('editar_categoria/<int:id>',views.editar_categoria, name='editar_categoria'),
    path('delet_categoria/<int:id>',views.delet_categoria, name='delet_categoria'),
    path('detail_categoria/<int:id>',views.detail_categoria, name='detail_categoria'),
    path('client', views.cliente, name='cliente'),
    path('clienteFormulario', views.form_cliente, name='clienteFormulario'),
    path('delet_cliente/<int:id>',views.delet_cliente, name='delet_cliente'),
    path('detail_cliente/<int:id>',views.detail_cliente, name='detailClient'),
    path('editar_cliente/<int:id>',views.editar_cliente, name='editar_cliente'),
    path('produto', views.produto, name='produto'),
    path('produtoFormulario', views.form_produto, name='produtoFormulario'),
    path('delet_produto/<int:produto_id>',views.delet_produto, name='delet_produto'),
    path('editar_produto/<int:produto_id>', views.editar_produto, name='editar_produto'),
    path('detail_produto/<int:id>',views.detail_produto, name='detailproduto'),
    path('ajustar_estoque/<int:id>',views.ajustar_estoque, name='ajustar_estoque'),
    path('teste', views.teste_1, name='teste1'),
    path('teste2', views.teste_2, name='teste2'),
    path('teste3', views.teste_3, name='teste3'),
    path('buscar_dados/<str:app_modelo>', views.buscar_dados, name='buscar_dados'),
    path('pedido', views.pedido, name='pedido'),
    path('novo_pedido/<int:id>', views.novo_pedido, name='novo_pedido'),
    path('detail_pedido/<int:id>', views.detalhes_pedido, name='detalhes_pedido'),
    path('remover_item_pedido/<int:id>', views.remover_item_pedido, name='remover_item_pedido'),
    path('pagamentos_pedido/<int:id>', views.form_pagamento, name='pagamentos_pedido'),
    path('nota_fiscal/<int:id>', views.nota_fiscal, name='nota_fiscal'),

]