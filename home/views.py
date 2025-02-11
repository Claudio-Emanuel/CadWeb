
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.apps import apps
from .models import *
from .forms import *


#--------------------------------------------------------    
def index(request):
    return render(request,'index.html')



#---------------------------------------------------------------------Categoria---------------------------------------------------------------------
def categoria(request):
    contexto = {
        'lista' : Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria/categoria.html',contexto)
#--------------------------------------------------------    
def form_categoria(request):

    if request.method == 'POST': 
        form=CategoriaForm(request.POST)
#--------------------------------------------------------    
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso!!')
            return redirect('categoria')
    else:
        form=CategoriaForm()
#--------------------------------------------------------    
    contexto = {
        'form' : form,
    }
    return render(request, 'categoria/formulario.html', contexto )
#--------------------------------------------------------    

#------------Funcao de Editar Categoria de Produto------------ 
def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar a categoria solicitada')
        return redirect('categoria/categoria')
        
    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save() # save retorna o objeto salvo
            lista = []
            lista.append(categoria) 
            return render(request, 'categoria/categoria.html', {'lista': lista})
    else:
         form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/formulario.html', {'form': form,})

#------------Funcao de Deletar Categoria de Produto------------ 
def delet_categoria(request,id):
    try:
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        messages.info(request, 'Item deletado com sucesso!!!')

    except Categoria.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar a categoria solicitada')
        return redirect('categoria')
    return redirect('categoria')

#------------Funcao de Detalhar Categoria de Produto------------ 
def detail_categoria(request,id):
    try:
        categoria = get_object_or_404(Categoria, pk=id)
    except Categoria.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar a categoria solicitada')
        return redirect('categoria')
    return render(request, 'categoria/detail.html', {'categoria': categoria})
#---------------------------------------------------------------------Categoria---------------------------------------------------------------------


#---------------------------------------------------------------------Cliente---------------------------------------------------------------------
def cliente(request):
    contexto = {
        'lista' : Cliente.objects.all().order_by('id'),
    }
    return render(request, 'cliente/cliente.html',contexto)


def form_cliente(request):

    if request.method == 'POST': 
        form=ClienteForm(request.POST)


        if form.is_valid():
            form.save()
            messages.success(request, 'Registro realizado com sucesso!!')
            return redirect('cliente')
    else:
        form=ClienteForm()


    contexto = {
        'form' : form,
    }
    return render(request, 'cliente/clienteFormulario.html', contexto )


def delet_cliente(request,id):
    try:
        categoria = Cliente.objects.get(pk=id)
        categoria.delete()
        messages.info(request, 'Item deletado com sucesso!!!')

    except Cliente.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar o cliente solicitado')
        return redirect('cliente')
    return redirect('cliente')


def detail_cliente(request,id):
    try:
        cliente = get_object_or_404(Cliente, pk=id)
    except Cliente.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar o cliente solicitad')
        return redirect('cliente')
        
    return render(request, 'cliente/detailClient.html', {'cliente': cliente})


def editar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar o cliente solicitad')
        return redirect('cliente')
        
    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save() # save retorna o objeto salvo
            lista = []
            lista.append(cliente) 
            return render(request, 'cliente.html', {'lista': lista})
    else:
         form = ClienteForm(instance=cliente)
    return render(request, 'cliente/clienteFormulario.html', {'form': form,})

#---------------------------------------------------------------------Cliente---------------------------------------------------------------------

#---------------------------------------------------------------------Produto---------------------------------------------------------------------

def produto(request):
        contexto = {
            'lista' : Produto.objects.all().order_by('id'),
        }
        return render(request, 'produto/produto.html',contexto)
    
def form_produto(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto')
    else:
        form = ProdutoForm()
    return render(request, 'produto/form_produto.html', {'form': form, 'categorias': categorias})

def delet_produto(request,produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('produto')
    
    return redirect('produto')

def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso.')
            return redirect('produto')  # Redireciona para a lista de produtos após salvar
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto/form_produto.html', {'form': form})



def detail_produto(request,id):
    try:
        produto = get_object_or_404(Produto, pk=id)
    except Produto.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar o cliente solicitad')
        return redirect('produto')
    return render(request, 'produto/detail_produto.html', {'produto': produto})
#---------------------------------------------------------------------Produto---------------------------------------------------------------------

#---------------------------------------------------------------------Estoque---------------------------------------------------------------------
def ajustar_estoque(request,id):
    produto = get_object_or_404(Produto, id=id)
    try:
        estoque = produto.estoque
    except Estoque.DoesNotExist:
        estoque = Estoque(produto=produto)
    
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estoque atualizado com sucesso.')
            return redirect('produto')
    else:
        form = EstoqueForm(instance=estoque)
    
    return render(request, 'produto/estoque.html', {'form': form, 'produto': produto})
#---------------------------------------------------------------------Estoque---------------------------------------------------------------------
def teste_1(request):
    return render(request, 'teste/teste1.html')

def teste_2(request):
    return render(request, 'teste/teste2.html')

def teste_3(request):
    return render(request, 'teste/teste3.html')


def buscar_dados(request, app_modelo):
    termo = request.GET.get('q', '') # pega o termo digitado
    try:
        # Divida o app e o modelo
        app, modelo = app_modelo.split('.')
        modelo = apps.get_model(app, modelo)
    except LookupError:
        return JsonResponse({'error': 'Modelo não encontrado'}, status=404)
    
    # Verifica se o modelo possui os campos 'nome' e 'id'
    if not hasattr(modelo, 'nome') or not hasattr(modelo, 'id'):
        return JsonResponse({'error': 'Modelo deve ter campos "id" e "nome"'}, status=400)
    
    resultados = modelo.objects.filter(nome__icontains=termo)
    dados = [{'id': obj.id, 'nome': obj.nome} for obj in resultados]
    return JsonResponse(dados, safe=False)




#---------------------------------------------------------------------Pedido---------------------------------------------------------------------
def pedido(request):
    listaP = Pedido.objects.all().order_by('-id')
    return render(request, 'pedido/pedido.html', {'listaP': listaP})

def novo_pedido(request,id):
    if request.method == 'GET':
        try:
            item_pedido = ItemPedido.objects.get(pk=id)
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            messages.error(request, 'Registro não encontrado')
            return redirect('cliente')  
        pedido = Pedido(cliente=cliente)
        form = PedidoForm(instance=pedido)# cria um formulario com o novo pedido
        return render(request, 'pedido/form.html',{'form': form})
    
    else: # se for metodo post, salva o pedido.
        form = PedidoForm(request.POST,instance=item_pedido)
        
    return redirect('pedido')

def detalhes_pedido(request,id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar o pedido solicitado')
        return redirect('pedido')

    if request.method == 'GET':
        itemPedido = ItemPedido(pedido=pedido)
        form = ItemPedidoForm(instance=itemPedido)
    else:
        form = ItemPedidoForm(request.POST)
        if form.is_valid():
            item_pedido = form.save(commit=False)  # Inicializa item_pedido antes de acessar

            # Obtém o estoque do produto de forma segura
            try:
                estoque = Estoque.objects.get(produto=item_pedido.produto)
            except Estoque.DoesNotExist:
                messages.error(request, 'Erro: Estoque não encontrado para o produto.')
                return redirect('detalhes_pedido', id=pedido.id)

            # Verifica se há quantidade suficiente no estoque
            if estoque.qtde < item_pedido.qtde:
                messages.error(request, 'Quantidade em estoque insuficiente para o produto.')
                return redirect('detalhes_pedido', id=pedido.id)

            # Atualiza o estoque
            estoque.qtde -= item_pedido.qtde
            estoque.save()  # Salva a alteração no banco de dados

            # Associa o item ao pedido e salva
            item_pedido.pedido = pedido
            item_pedido.preco = item_pedido.produto.preco
            item_pedido.save()

            messages.success(request, 'Item adicionado ao pedido com sucesso.')

    # Recria um novo itemPedido para ser renderizado no formulário
    itemPedido = ItemPedido(pedido=pedido)
    form = ItemPedidoForm(instance=itemPedido)
    contexto = {
        'pedido': pedido,
        'form': form,
    }
    return render(request, 'pedido/detalhes.html', contexto)

def editar_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)

    else:
        form = ItemPedidoForm(instance=item_pedido)
        
    contexto = {
        'pedido': pedido,
        'form': form,
        'item_pedido': item_pedido,
    }
    return render(request, 'pedido/detalhes.html', contexto)

def remover_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)
    
    pedido_id = item_pedido.pedido.id  # Armazena o ID do pedido antes de remover o item
    estoque = item_pedido.produto.estoque  # Obtém o estoque do produto
    estoque.qtde += item_pedido.qtde  # Devolve a quantidade do item ao estoque
    estoque.save()  # Salva as alterações no estoque
    # Remove o item do pedido
    item_pedido.delete()
    messages.success(request, 'Operação realizada com Sucesso')


    # Redireciona de volta para a página de detalhes do pedido
    return redirect('detalhes_pedido', id=pedido_id)
#---------------------------------------------------------------------Pedido---------------------------------------------------------------------

#---------------------------------------------------------------------Pagamento---------------------------------------------------------------------
def form_pagamento(request,id):

    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar o pedido solicitado')
        return redirect('pedido')
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pagamento realizado com sucesso')

    pagamento = Pagamento(pedido=pedido)
    form =  PagamentoForm(instance=pagamento)
    contexto = {
        'pedido': pedido,
        'form': form,

    }
    return render(request, 'pedido/pagamento.html', contexto)