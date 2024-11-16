from django.db import models

class LinkRapido(models.Model):
    titulo = models.CharField(max_length=255)  # Campo para o título do link
    url = models.URLField()  # Campo para a URL

    def __str__(self):
        return self.titulo
