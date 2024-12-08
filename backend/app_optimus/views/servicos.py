from django.utils import timezone
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from app_optimus.permissions.servidor import IsServidor
from app_optimus.models.funcionalidades_models import Servico, ServicoEtapa, SolicitacaoServico, SolicitacaoEtapa
from app_optimus.serializers.cidadao_serializers import (
    ServicoSerializer, ServicoDetalhadoSerializer, CriarSolicitacaoServicoSerializer, SolicitacaoServicoSerializer
)
from app_optimus.serializers.servidor_serializers import (
    ServicoAdminSerializer, ServicoAdminDetalhadoSerializer, ServicoEtapaAdminSerializer, SolicitacaoServidorSerializer, SolicitacaoCompactaSerializer
)

class ServicoViewSetCidadao(ViewSet):
    """
    ViewSet para acesso de cidadãos aos serviços.
    """
    permission_classes = []

    def list(self, request):
        """
        Lista serviços ativos e visíveis para cidadãos.
        """
        queryset = Servico.objects.filter(status=True).order_by('-data_criacao')
        serializer = ServicoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalha informações de um serviço.
        """
        try:
            servico = Servico.objects.get(pk=pk, status=True)
        except Servico.DoesNotExist:
            raise Http404("Serviço não encontrado.")

        serializer = ServicoDetalhadoSerializer(servico)
        return Response(serializer.data)

# ViewSet para Servidores
class ServicoViewSetServidor(ViewSet):
    """
    ViewSet para gerenciamento de serviços por servidores.
    """
    permission_classes = [IsAuthenticated, IsServidor]

    def get_servico(self, pk):
        """
        Auxiliar para buscar um serviço ou retornar 404.
        """
        try:
            return Servico.objects.get(pk=pk)
        except Servico.DoesNotExist:
            raise Http404("Serviço não encontrado.")

    def list(self, request):
        """
        Lista todos os serviços para servidores.
        """
        queryset = Servico.objects.all().order_by('-data_criacao')
        serializer = ServicoAdminSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalha informações de um serviço específico.
        """
        servico = self.get_servico(pk)
        serializer = ServicoAdminDetalhadoSerializer(servico)
        return Response(serializer.data)

    def create(self, request):
        """
        Cria um novo serviço.
        """
        serializer = ServicoAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': f"Serviço '{serializer.data['nome']}' criado com sucesso.",
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        Atualiza um serviço.
        """
        servico = self.get_servico(pk)
        serializer = ServicoAdminSerializer(servico, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': f"Serviço '{serializer.data['nome']}' atualizado com sucesso.",
            'data': serializer.data
        })

    def destroy(self, request, pk=None):
        """
        Remove um serviço.
        """
        servico = self.get_servico(pk)
        servico_nome = servico.nome
        servico.delete()
        return Response({
            'message': f"Serviço '{servico_nome}' excluído com sucesso."
        }, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['get', 'post'], url_path='etapas')
    def gerenciar_etapas(self, request, pk=None):
        """
        Listar ou criar etapas para um serviço.
        """
        servico = self.get_servico(pk)

        if request.method == 'GET':
            serializer = ServicoEtapaAdminSerializer(servico.etapas.all(), many=True)
            return Response(serializer.data)

        # Criação de etapa
        data = {**request.data, 'servico': servico.id}
        serializer = ServicoEtapaAdminSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': f"Etapa '{serializer.data['nome']}' criada.",
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['delete'], url_path='etapas/(?P<etapa_pk>[^/.]+)')
    def deletar_etapa(self, request, pk=None, etapa_pk=None):
        """
        Remove uma etapa específica.
        """
        try:
            etapa = ServicoEtapa.objects.get(pk=etapa_pk, servico_id=pk)
        except ServicoEtapa.DoesNotExist:
            raise Http404("Etapa não encontrada.")

        etapa_nome = etapa.nome
        etapa.delete()
        return Response({
            'message': f"Etapa '{etapa_nome}' removida com sucesso."
        }, status=status.HTTP_204_NO_CONTENT)


class SolicitacaoServicoViewSet(ModelViewSet):
    """
    ViewSet para gerenciamento de solicitações.
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Define quais solicitações o usuário pode visualizar.
        """
        usuario = self.request.user
        if usuario.perfil == 'servidor':
            return SolicitacaoServico.objects.all()
        return SolicitacaoServico.objects.filter(id_usuario=usuario)

    def get_serializer_class(self):
        """
        Seleciona o serializer com base na ação.
        """
        if self.action == 'list':
            return SolicitacaoCompactaSerializer
        if self.action == 'create':
            return CriarSolicitacaoServicoSerializer
        if self.request.user.perfil == 'servidor':
            return SolicitacaoServidorSerializer
        return SolicitacaoServicoSerializer

    def destroy(self, request, pk=None):
        """
        Remove uma solicitação.
        """
        try:
            solicitacao = SolicitacaoServico.objects.get(pk=pk)
            solicitacao.delete()
            return Response({'message': 'Solicitação removida com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
        except SolicitacaoServico.DoesNotExist:
            raise Http404("Solicitação não encontrada.")
    
class SolicitacaoServidorViewSet(ViewSet):
    """
    ViewSet para gerenciamento de solicitações pelos servidores.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Lista solicitações pendentes ou em andamento.
        """
        status_filter = request.query_params.get('status', None)
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))
        offset = (page - 1) * limit

        # Filtro pelo status
        queryset = SolicitacaoServico.objects.all()
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        total = queryset.count()
        queryset = queryset[offset:offset + limit]

        serializer = SolicitacaoServidorSerializer(queryset, many=True)
        return Response({
            "total": total,
            "page": page,
            "limit": limit,
            "solicitacoes": serializer.data
        })
        
    def update(self, request, pk=None):
        """
        Atualiza o status geral e os comentários de uma solicitação.
        """
        try:
            solicitacao = SolicitacaoServico.objects.get(pk=pk)
        except SolicitacaoServico.DoesNotExist:
            return Response({'error': 'Solicitação não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        solicitacao.status = request.data.get('status', solicitacao.status)
        solicitacao.comentario_servidor = request.data.get('comentario_servidor', solicitacao.comentario_servidor)
        solicitacao.save()

        return Response({'mensagem': 'Solicitação atualizada com sucesso.'})

    @action(detail=True, methods=['put'], url_path='etapas/(?P<etapa_pk>[^/.]+)')
    def concluir_etapa(self, request, pk=None, etapa_pk=None):
        """
        Marca uma etapa como concluída.
        """
        try:
            etapa = SolicitacaoEtapa.objects.get(pk=etapa_pk, id_solicitacao=pk)
        except SolicitacaoEtapa.DoesNotExist:
            return Response({'error': 'Etapa não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        etapa.concluida = request.data.get('concluida', False)
        etapa.data_conclusao = timezone.now() if etapa.concluida else None
        etapa.save()

        return Response({'mensagem': 'Etapa marcada como concluída.'})