from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo