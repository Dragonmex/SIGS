from rest_framework import serializers
from app_optimus.models.funcionalidades_models import Servico, Noticia, CategoriaServico, CategoriaNoticia



# Serializers Genéricos para Categorias
class CategoriaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServico
        fields = ['id', 'nome', 'descricao', 'slug']


class CategoriaNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNoticia
        fields = ['id', 'nome', 'descricao', 'slug']


# Serializers para Cidadão
class ServicoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()

    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'status', 'data_criacao', 'categoria']


class ServicoDetalhadoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    servicos_relacionados = serializers.SerializerMethodField()

    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'status', 'data_criacao', 'categoria', 'servicos_relacionados']

    def get_servicos_relacionados(self, obj):
        relacionados = Servico.objects.filter(categoria=obj.categoria).exclude(id=obj.id)[:4]
        return [
            {
                'id': servico.id,
                'nome': servico.nome,
                'descricao': servico.descricao,
                'data_criacao': servico.data_criacao,
            }
            for servico in relacionados
        ]


class NoticiaSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()

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
