from rest_framework import serializers
from app_optimus.models.conteudos_db import Noticia, Servico

class NoticiaSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nome')

    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'resumo', 'data_publicacao', 'autor', 'categoria']

class ServicoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nome')

    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'categoria']