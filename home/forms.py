from .models import *
from django import forms 
from datetime import date


class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields = ['nome', 'ordem']
        widgets = {
            'nome' : forms.TextInput(attrs={'class' : 'form-control', 'place-holder': 'Nome'}),
            'ordem' : forms.NumberInput(attrs={'class' : 'inteiro form-control', 'placeholder': ''}),
        }

    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome  
    
    def clean_ordem(self):
        ordem = self.cleaned_data.get('ordem')
        if ordem <= 0:
            raise forms.ValidationError("O campo ordem deve ser maior que zero.")
        return ordem
   
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'datanasc']
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf':forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'C.P.F'}),
            'datanasc': forms.DateInput(attrs={'class': 'data form-control','max': date.today().strftime('%d-%m-%Y'),'placeholder': 'Data de Nascimento'}, format='%d/%m/%Y'),
        }
        
    def clean_datanasc(self):
        data=self.cleaned_data.get('datanasc')
        if data > date.today():
            raise forms.ValidationError('A data inserida não pode ser maior que a data atual')
        return data

class ProdutoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=True)
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria','img_base64']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'img_base64': forms.HiddenInput(), 
            'preco':forms.TextInput(attrs={
                'class': 'money form-control',
                'maxlength': 500,
                'placeholder': '0.000,00'
            }),
        }
        
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço do Produto',
        }


    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].localize = True
        self.fields['preco'].widget.is_localized = True   

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto','qtde']
        widgets = {
            'produto': forms.HiddenInput(),
            'qtde': forms.TextInput(attrs={'class': 'inteiro form-control', 'placeholder': 'Quantidade'}),
        }
        
    def clean_qtde(self):
        qtde = self.cleaned_data.get('qtde')
        if qtde <= 0:
            raise forms.ValidationError("O campo quantidade deve ser maior que zero.")
        return qtde
    
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente']
        widgets = {
            'cliente': forms.HiddenInput(),  # Campo oculto para armazenar o ID
        }

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido', 'produto', 'qtde']
        widgets = {
            'produto': forms.HiddenInput(),
            'pedido': forms.HiddenInput(),
            'qtde': forms.TextInput(attrs={'class': 'form-control',}),
        }
        
    def clean_qtde(self):
        qtde = self.cleaned_data.get('qtde')
        if qtde <= 0:
            raise forms.ValidationError("O campo quantidade deve ser maior que zero.")
        return qtde

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco <= 0:
            raise forms.ValidationError("O campo preço deve ser maior que zero.")
        return preco
    
class PagamentoForm(forms.ModelForm):
    class Meta:
        model= Pagamento
        fields = ['pedido', 'valor', 'forma']
        widgets = {
            'pedido': forms.HiddenInput(),
            'valor': forms.TextInput(attrs={
                'class': 'money form-control', 
                'placeholder': '0.000,00',
                'maxlength': 500,
                }),
            'forma': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PagamentoForm, self).__init__(*args, **kwargs)
        self.fields['valor'].localize = True
        self.fields['valor'].widget.is_localized = True
    
    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if valor <= 0:
            raise forms.ValidationError("O campo valor deve ser maior que zero.")
        return valor





