from django.db import models
from .categoria import Categoria

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias_imagens/', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, related_name='noticias', on_delete=models.CASCADE)
    noticias_relacionadas = models.ManyToManyField('self', blank=True, related_name='relacionadas')
    data_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
