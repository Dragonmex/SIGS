from django.db import models

class Banner(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='banners/')
    descricao = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo