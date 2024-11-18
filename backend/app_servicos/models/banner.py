from django.db import models

class Banner(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='banners/', blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
