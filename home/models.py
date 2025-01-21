from django.db import models

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