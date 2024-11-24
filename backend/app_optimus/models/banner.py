from django.db import models

class Banner(models.Model):
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class ImagemBanner(models.Model):
    banner = models.ForeignKey(Banner, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='banners/')

    def __str__(self):
        return f"Imagem para {self.banner.titulo}"
