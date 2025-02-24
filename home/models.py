import hashlib
from django.db import models
from decimal import Decimal
class Categoria(models.Model):
    nome= models.CharField(max_length=100)
    ordem= models.IntegerField()

    def _str_(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15,verbose_name="C.P.F")
    datanasc = models.DateField(verbose_name="Data de Nascimento")

        
    def __str__(self):
        return self.nome
    

    @property
    def datanascimento(self):

        if self.datanasc:
            return self.datanasc.strftime('%d/%m/%Y')
        return None

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2,blank=False)
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    img_base64 = models.TextField(blank=True)

    def _str_(self):
        return self.nome
    
    @property
    def estoque(self):
        estoque_item,flag_created = Estoque.objects.get_or_create(produto=self,defaults={'qtde':0})
        return estoque_item

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde = models.IntegerField()


    def _str_(self):
        return f'{self.produto.nome} - Quantidade: {self.qtde}'
    
class Pedido(models.Model):


    NOVO = 1
    EM_ANDAMENTO = 2
    CONCLUIDO = 3
    CANCELADO = 4


    STATUS_CHOICES = [
        (NOVO, 'Novo'),
        (EM_ANDAMENTO, 'Em Andamento'),
        (CONCLUIDO, 'Concluído'),
        (CANCELADO, 'Cancelado'),
    ]


    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=NOVO)


    def __str__(self):
            return f"Pedido {self.id} - Cliente: {self.cliente.nome} - Status: {self.get_status_display()}"
    
    @property
    def data_pedidof(self):
        if self.data_pedido:
            return self.data_pedido.strftime('%d/%m/%Y %H:%M:%S')
        return None
    
    @property
    def total(self):
        """Calcula o total de todos os itens no pedido, formatado como moeda local"""
        total = sum(item.qtde * item.preco for item in self.itempedido_set.all())
        return total


    
    @property
    def qtdeItens(self):
        """Conta a qtde de itens no pedido, """
        return self.itempedido_set.count()  


    # lista dos pagamentos
    @property
    def pagamentos(self):
        return Pagamento.objects.filter(pedido=self)

    @property
    def total_pago(self):
        total = sum(pagamento.valor for pagamento in self.pagamentos.all())
        return total

    @property
    def debito(self):
        deb = self.total - self.total_pago
        return deb
    
    @property
    def icms(self):
        return self.total * Decimal(0.18)
    
    @property
    def ipi(self):
        return self.total * Decimal('0.05')

    @property
    def pis(self):
        return self.total * Decimal('0.0165')

    @property
    def cofins(self):
        return self.total * Decimal('0.076')

    @property
    def total_tributos(self):
        return self.total + self.icms + self.ipi + self.pis + self.cofins
    
    @property
    def total_completo(self):
        return self.total + self.total_tributos
    
    @property
    def data_pedido_key(self):
        if self.data_pedido:
            return self.data_pedido.strftime('%Y%m%d')
        return None
    
    @property
    def chave_acesso(self):
        # Combina o ID do pedido e a data formatada
        if self.id and self.data_pedido_key:
            dados_comb = f"{self.id}{self.data_pedido_key}"
        
            # Cria o hash com sha256
            sha256 = hashlib.sha256()
            sha256.update(dados_comb.encode('utf-8'))  # Codificando a string para bytes
            key_final = f"{self.data_pedido_key}{self.id}{sha256.hexdigest()}"
            
            # Remove caracteres não numéricos
            key_final_numerico = ''.join(filter(str.isdigit, key_final))
            return key_final_numerico  # Retorna a chave de acesso contendo apenas números
        return None
    

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.produto.nome} (Qtd: {self.qtde}) - Preço Unitário: {self.preco}"      
    
    @property
    def Total_parcial(self):
        total = self.qtde * self.preco
        return total
    
class Pagamento(models.Model):
    
    DINHEIRO  = 1
    CARTAO    = 2
    PIX       = 3
    BOLETO    = 4
    ESPECIE   = 5
    OUTRO     = 6

    FORMAS_CHOICES = [
        (DINHEIRO, 'Dinheiro'),
        (CARTAO, 'Cartão'),
        (PIX, 'Pix'),
        (BOLETO, 'Boleto'),
        (ESPECIE, 'Espécie'),
        (OUTRO, 'Outro'),
    ]

    pedido      = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    forma       = models.IntegerField(choices=FORMAS_CHOICES)
    valor       = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    data_pagnto = models.DateTimeField(auto_now_add=True)

    @property
    def data_pagntof(self):
        # Retorna a data no formato DD/MM/AAAA HH:MM
        if self.data_pagnto:
            return self.data_pagnto.strftime('%d/%m/%Y %H:%M')
        return None
