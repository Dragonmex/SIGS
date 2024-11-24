from rest_framework import serializers
from app_optimus.models.Noticia import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nome')

    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'resumo', 'data_publicacao', 'autor', 'categoria']
