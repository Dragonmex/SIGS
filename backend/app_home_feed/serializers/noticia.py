from rest_framework import serializers
from ..models.noticia import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'conteudo', 'data_publicacao']