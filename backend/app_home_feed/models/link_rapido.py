from django.db import models

class LinkRapido(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.ImageField(upload_to='links_rapidos/', blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.nome