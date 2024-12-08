from rest_framework import serializers
from app_optimus.models.funcionalidades_models import (
    Servico,
    Noticia,
    CategoriaServico,
    CategoriaNoticia,
    ServicoEtapa,
    SolicitacaoServico,
    SolicitacaoEtapa,
)

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


class ServicoEtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicoEtapa
        fields = ['id', 'nome', 'descricao', 'ordem']


class ServicoDetalhadoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    etapas = ServicoEtapaSerializer(many=True, read_only=True)
    servicos_relacionados = serializers.SerializerMethodField()

    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'status', 'data_criacao', 'categoria', 'etapas', 'servicos_relacionados']

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
                'imagem': noticia.imagem,  # Retorna diretamente o valor do campo
                'data_publicacao': noticia.data_publicacao,
            }
            for noticia in relacionadas
        ]


class SolicitacaoEtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoEtapa
        fields = ['id', 'nome_etapa', 'descricao_etapa', 'ordem', 'concluida']


class SolicitacaoServicoSerializer(serializers.ModelSerializer):
    etapas = SolicitacaoEtapaSerializer(many=True, read_only=True)
    usuario = serializers.SerializerMethodField()  # Campo personalizado
    servico_nome = serializers.CharField(source='id_servico.nome', read_only=True)

    class Meta:
        model = SolicitacaoServico
        fields = ['id', 'usuario', 'servico_nome', 'data_solicitacao', 'status', 'comentario_servidor', 'etapas']

    def get_usuario(self, obj):
        """
        Retorna os detalhes do usuário associado à solicitação.
        """
        usuario = obj.id_usuario
        if hasattr(usuario, 'cidadao'):
            nome = usuario.cidadao.nome_completo
        elif hasattr(usuario, 'servidor'):
            nome = usuario.servidor.nome_completo
        else:
            nome = usuario.email  # Fallback se nenhum nome estiver definido
        return {
            "nome": nome,
            "email": usuario.email
        }


class CriarSolicitacaoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoServico
        fields = ['id_servico']

    def validate(self, attrs):
        usuario = self.context['request'].user
        servico = attrs.get('id_servico')

        if SolicitacaoServico.objects.filter(id_usuario=usuario, id_servico=servico).exists():
            raise serializers.ValidationError("Você já fez uma solicitação para este serviço.")

        return attrs

    def create(self, validated_data):
        usuario = self.context['request'].user
        servico = validated_data['id_servico']

        # Criar a solicitação
        solicitacao = SolicitacaoServico.objects.create(id_usuario=usuario, id_servico=servico)

        # Vincular as etapas existentes do serviço à solicitação
        etapas_servico = servico.etapas.all()
        for etapa in etapas_servico:
            SolicitacaoEtapa.objects.create(
                solicitacao=solicitacao,
                nome_etapa=etapa.nome,
                descricao_etapa=etapa.descricao,
                ordem=etapa.ordem,
                concluida=False
            )

        # Mensagem personalizada
        self.context['response_message'] = f"Solicitação criada com sucesso! Serviço: '{servico.nome}'. Você pode acompanhar as etapas na sua área de usuário."

        return solicitacao
