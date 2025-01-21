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

]