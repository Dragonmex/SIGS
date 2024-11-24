from django.db import models
from app_optimus.models import CategoriaServico

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
