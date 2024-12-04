from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.text import slugify


class CategoriaServico(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Categoria de Serviço"
        verbose_name_plural = "Categorias de Serviços"

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)


class CategoriaNoticia(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Categoria de Notícia"
        verbose_name_plural = "Categorias de Notícias"

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)


class ServicoManager(models.Manager):
    def ativos(self):
        return self.filter(status=True)


class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.BooleanField(default=True)  # Ativo ou Inativo
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.CASCADE)

    objects = ServicoManager()

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=255, blank=True)
    categoria = models.ForeignKey(CategoriaNoticia, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = "Notícia"
        verbose_name_plural = "Notícias"

    def __str__(self):
        return self.titulo

    def imagem_preview(self):
        if self.imagem:
            return format_html('<img src="{}" style="width: 50px; height:50px;" />', self.imagem.url)
        return "Sem Imagem"

#OUVIDORIA 

class Ouvidoria(models.Model):
    TIPOS_CHOICES = [
        ('DENUNCIA','Denúncia'),
        ('SUGESTAO', 'Sugestão'),
        ('ELOGIO', 'Elogio'),
        ('OUTRO', 'Outro'),
    ]

    tipo = models.CharField(max_length= 10, choices = TIPOS_CHOICES)
    descricao = models.TextField()
    data_criacao=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20, default='PENDENTE')
    cidadao = models.ForeignKey('Cidadao', on_delete=models.SET_NULL, null=True, blank=True)
    servidor = models.ForeignKey('Servidor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.tipo} - {self.status} - {self.data_criacao}'