from django.db import models

class Funcionalidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    icone = models.ImageField(upload_to='icones/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, related_name='funcionalidades', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome