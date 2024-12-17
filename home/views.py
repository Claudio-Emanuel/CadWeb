from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import *


#--------------------------------------------------------    
def index(request):
    return render(request,'index.html')
#--------------------------------------------------------    
def categoria(request):
    contexto = {
        'lista' : Categoria.objects.all().order_by('id'),
    }
    return render(request, 'categoria.html',contexto)
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
    return render(request, 'formulario.html', contexto )
#--------------------------------------------------------    

#------------Funcao de Editar Categoria de Produto------------ 
def editar_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar a categoria solicitada')
        return redirect('categoria')
        
    if request.method == 'POST':
        # combina os dados do formulário submetido com a instância do objeto existente, permitindo editar seus valores.
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save() # save retorna o objeto salvo
            lista = []
            lista.append(categoria) 
            return render(request, 'categoria.html', {'lista': lista})
    else:
         form = CategoriaForm(instance=categoria)
    return render(request, 'formulario.html', {'form': form,})

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
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        messages.error(request, 'Não foi possível encontrar a categoria solicitada')
        return redirect('categoria')
        
    if request.method == 'POST':
        CategoriaForm(request.POST, instance=categoria)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'detail.html', {'form': form,})
    