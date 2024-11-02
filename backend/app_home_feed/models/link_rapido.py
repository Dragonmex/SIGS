# models/link_rapido.py
from django.db import models

class LinkRapido(models.Model):
    titulo = models.CharField(max_length=255)  # Campo para o título do link
    url = models.URLField()  # Campo para a URL
    descricao = models.TextField()  # Campo para uma descrição adicional

    def __str__(self):
        return self.titulo
