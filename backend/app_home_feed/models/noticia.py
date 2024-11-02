from django.db import models
from .categoria import Categoria  # Importa o modelo Categoria para criar a relação

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    categoria = models.ForeignKey(Categoria, related_name='noticias', on_delete=models.CASCADE)
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
