from django.db import models
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.utils.text import slugify
from app_optimus.models.usuarios_models import Usuario


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

class ServicoEtapa(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='etapas')
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    ordem = models.PositiveIntegerField()

    class Meta:
        ordering = ['ordem']
        verbose_name = "Etapa do Serviço"
        verbose_name_plural = "Etapas do Serviço"

    def __str__(self):
        return f"{self.ordem} - {self.nome}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    conteudo = models.TextField()
    imagem = models.URLField(max_length=500, blank=True, null=True)
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

class SolicitacaoServico(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em andamento'),
        ('concluido', 'Concluído'),
    ]

    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='solicitacoes')
    id_servico = models.ForeignKey('Servico', on_delete=models.CASCADE, related_name='solicitacoes')
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    comentario_servidor = models.TextField(blank=True, null=True)  # Adicionando o campo

    def __str__(self):
        return f"Solicitação {self.id} - {self.id_servico.nome}"
    
class SolicitacaoEtapa(models.Model):
    solicitacao = models.ForeignKey(
        SolicitacaoServico,
        on_delete=models.CASCADE,
        related_name='etapas'  # Define o nome do relacionamento reverso
    )
    nome_etapa = models.CharField(max_length=255)
    descricao_etapa = models.TextField(blank=True, null=True)
    ordem = models.PositiveIntegerField()
    concluida = models.BooleanField(default=False)
    data_conclusao = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f"{self.nome_etapa} ({'Concluída' if self.concluida else 'Pendente'})"

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

