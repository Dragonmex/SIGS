from rest_framework import serializers
from app_optimus.models import Servico, Noticia, CategoriaServico, CategoriaNoticia

class CategoriaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServico
        fields = ['id', 'nome', 'descricao', 'slug']


class CategoriaNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNoticia
        fields = ['id', 'nome', 'descricao', 'slug']
        
class ServicoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()  # Mostra o nome da categoria no lugar do ID

    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'status', 'data_criacao', 'categoria']

class NoticiaSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()  # Mostra o nome da categoria no lugar do ID

    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'resumo', 'conteudo', 'imagem', 'data_publicacao', 'autor', 'categoria']


