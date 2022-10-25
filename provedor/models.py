from django.db import models

# Create your models here.
class Provedor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    preco = models.DecimalField(max_digits=9, decimal_places=2, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.URLField(max_length=255, null=False, blank=False)

class Servico(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    provedor = models.ForeignKey(to=Provedor,on_delete=models.CASCADE,related_name="servicos",null=False,blank=False) # serve para quando for fazer uma busca ele puxar todos os relate names, ou seja pelo nome puxar as aula.
