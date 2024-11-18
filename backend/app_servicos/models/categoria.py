from django.db import models
from django.utils.text import slugify

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    descricao = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super(Categoria, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"