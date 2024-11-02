from django.db import models

class Funcionalidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.ImageField(upload_to='icons/', blank=True, null=True)
    rota = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome