from django.db import models

class CategoriaNoticia(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome