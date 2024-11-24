from rest_framework import serializers
from app_optimus.models.noticia import Noticia

class NoticiaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'imagem']

class NoticiaRelacionadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'imagem']

class NoticiaSerializer(serializers.ModelSerializer):
    noticias_relacionadas = NoticiaRelacionadaSerializer(many=True, read_only=True)

    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'conteudo', 'imagem', 'noticias_relacionadas', 'data_publicacao']
