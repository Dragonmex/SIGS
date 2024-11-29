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


class NoticiaDetalhadaSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    noticias_relacionadas = serializers.SerializerMethodField()

    class Meta:
        model = Noticia
        fields = [
            'id', 'titulo', 'conteudo', 'imagem', 
            'data_publicacao', 'autor', 'categoria', 'noticias_relacionadas'
        ]

    def get_noticias_relacionadas(self, obj):
        # Busca as notícias relacionadas pela mesma categoria, excluindo a atual
        relacionadas = Noticia.objects.filter(categoria=obj.categoria).exclude(id=obj.id)[:4]
        return [
            {
                'id': noticia.id,
                'titulo': noticia.titulo,
                'resumo': noticia.resumo,
                'imagem': noticia.imagem.url if noticia.imagem else None,
                'data_publicacao': noticia.data_publicacao,
            }
            for noticia in relacionadas
        ]
