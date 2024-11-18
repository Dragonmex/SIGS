from django.db import models

class AcessoInformacao(models.Model):
    nome_documento = models.CharField(max_length=255)
    descricao = models.TextField()
    documento = models.FileField(upload_to='documentos/')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome_documento

    class Meta:
        verbose_name = "Acesso à Informação"
        verbose_name_plural = "Acessos à Informação"
