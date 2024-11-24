from django.db import models
from app_optimus.models import CategoriaNoticia

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=255, blank=True)
    categoria = models.ForeignKey(CategoriaNoticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
