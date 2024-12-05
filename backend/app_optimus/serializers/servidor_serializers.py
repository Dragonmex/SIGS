from rest_framework import serializers
from app_optimus.models.funcionalidades_models import Servico, Noticia, CategoriaServico, CategoriaNoticia, ServicoEtapa, SolicitacaoEtapa, SolicitacaoServico


# Serializers Genéricos (reutilizáveis para ambos os perfis)
class CategoriaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaServico
        fields = ['id', 'nome', 'descricao', 'slug']


class CategoriaNoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNoticia
        fields = ['id', 'nome', 'descricao', 'slug']


# Serializers para CRUD de Serviços (Servidor)
class ServicoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'status', 'data_criacao', 'categoria']

class ServicoEtapaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoEtapa
        fields = ['id', 'servico', 'nome', 'descricao', 'ordem']

# Serializer Detalhado para Serviços (Servidor)
class ServicoAdminDetalhadoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    etapas = ServicoEtapaAdminSerializer(many=True)

    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'status', 'data_criacao', 'categoria', 'etapas']

    def get_etapas(self, obj):
        """
        Retorna as etapas do serviço ou uma lista vazia se não houver etapas.
        """
        etapas = obj.etapas.all()
        if not etapas.exists():
            return []  # Retorna uma lista vazia se não houver etapas
        return ServicoEtapaAdminSerializer(etapas, many=True).data

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


# Serializers para CRUD de Notícias (Servidor)
class NoticiaAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'resumo', 'conteudo', 'imagem', 'data_publicacao', 'autor', 'categoria']


# Serializer Detalhado para Notícias (Servidor)
class NoticiaAdminDetalhadaSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    noticias_relacionadas = serializers.SerializerMethodField()

    class Meta:
        model = Noticia
        fields = [
            'id', 'titulo', 'resumo', 'conteudo', 'imagem', 
            'data_publicacao', 'autor', 'categoria', 'noticias_relacionadas'
        ]

    def get_noticias_relacionadas(self, obj):
        """
        Busca até 4 notícias na mesma categoria, excluindo a notícia atual.
        """
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

class SolicitacaoEtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoEtapa
        fields = ['id', 'nome_etapa', 'descricao_etapa', 'ordem', 'concluida']

class SolicitacaoServidorSerializer(serializers.ModelSerializer):
    etapas = serializers.SerializerMethodField()
    usuario = serializers.SerializerMethodField()
    servico = serializers.CharField(source='id_servico.nome')

    class Meta:
        model = SolicitacaoServico
        fields = ['id', 'usuario', 'servico', 'data_solicitacao', 'status', 'comentario_servidor', 'etapas']

    def get_usuario(self, obj):
        usuario = obj.id_usuario  # Corrigido para usar id_usuario
        if hasattr(usuario, 'cidadao'):
            nome = usuario.cidadao.nome_completo
        elif hasattr(usuario, 'servidor'):
            nome = usuario.servidor.nome_completo
        else:
            nome = usuario.email  # Fallback se não houver um nome definido
        return {
            "nome": nome,
            "email": usuario.email
        }

    def get_etapas(self, obj):
        etapas = obj.etapas.all()  # Acessa pelo related_name configurado no modelo
        return [
            {
                "id": etapa.id,
                "nome_etapa": etapa.nome_etapa,
                "descricao_etapa": etapa.descricao_etapa,
                "ordem": etapa.ordem,
                "concluida": etapa.concluida,
            }
            for etapa in etapas
        ]