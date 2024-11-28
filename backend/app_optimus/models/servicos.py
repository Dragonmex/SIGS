from django.db import models

# Categorias de Serviços
class CategoriaServico(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


# Categorias de Notícias
class CategoriaNoticia(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome
    
# Serviços
class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(CategoriaServico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


# Notícias
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=255, blank=True)
    categoria = models.ForeignKey(CategoriaNoticia, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
