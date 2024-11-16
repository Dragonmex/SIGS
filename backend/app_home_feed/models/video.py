from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.titulo
