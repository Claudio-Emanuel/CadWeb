from django.shortcuts import render, redirect

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
            return redirect('categoria')
    else:
        form=CategoriaForm()
#--------------------------------------------------------    
    contexto = {
        'form' : form,
    }
    return render(request, 'formulario.html', contexto )
#--------------------------------------------------------    