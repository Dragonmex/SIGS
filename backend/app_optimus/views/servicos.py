from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from app_optimus.permissions.servidor import IsServidor
from app_optimus.models.funcionalidades_models import Servico
from app_optimus.serializers.cidadao_serializers import ServicoSerializer, ServicoDetalhadoSerializer
from app_optimus.serializers.servidor_serializers import ServicoAdminSerializer

class ServicoViewSetCidadao(ViewSet):
    """
    ViewSet específico para Serviços acessados por Cidadãos.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Listagem de Serviços visíveis para Cidadãos.
        """
        queryset = Servico.objects.filter(status=True).order_by('-data_criacao')
        serializer = ServicoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhamento de um Serviço para Cidadãos.
        """
        try:
            servico = Servico.objects.get(pk=pk, status=True)  # Apenas serviços ativos
        except Servico.DoesNotExist:
            return Response({'error': 'Serviço não encontrado.'}, status=404)

        serializer = ServicoDetalhadoSerializer(servico)
        return Response(serializer.data)


class ServicoViewSetCidadao(ViewSet):
    """
    ViewSet específico para Serviços acessados por Cidadãos.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Listagem de Serviços visíveis para Cidadãos.
        """
        queryset = Servico.objects.filter(status=True).order_by('-data_criacao')
        serializer = ServicoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhamento de um Serviço para Cidadãos.
        """
        try:
            servico = Servico.objects.get(pk=pk, status=True)  # Apenas serviços ativos
        except Servico.DoesNotExist:
            return Response({'error': 'Serviço não encontrado.'}, status=404)

        serializer = ServicoDetalhadoSerializer(servico)
        return Response(serializer.data)


class ServicoViewSetServidor(ViewSet):
    """
    ViewSet completo para gerenciamento de Serviços pelos Servidores.
    """
    permission_classes = [IsAuthenticated, IsServidor]

    def list(self, request):
        """
        Listagem de todos os Serviços para Servidores.
        """
        queryset = Servico.objects.all().order_by('-data_criacao')
        serializer = ServicoAdminSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhamento de um Serviço para Servidores.
        """
        try:
            servico = Servico.objects.get(pk=pk)
        except Servico.DoesNotExist:
            return Response({'error': 'Serviço não encontrado.'}, status=404)

        serializer = ServicoAdminSerializer(servico)
        return Response(serializer.data)

    def create(self, request):
        """
        Criação de um novo Serviço.
        """
        serializer = ServicoAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Serviço criado com sucesso.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        # Adiciona mensagens de validação detalhadas
        validation_errors = {field: msg[0] for field, msg in serializer.errors.items()}
        return Response(
            {
                'error': 'Erro de validação. Verifique os campos obrigatórios.',
                'fields': validation_errors,
                'required_fields': ['nome', 'descricao', 'categoria', 'status']
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, pk=None):
        """
        Atualização de um Serviço existente.
        """
        try:
            servico = Servico.objects.get(pk=pk)
        except Servico.DoesNotExist:
            return Response({'error': 'Serviço não encontrado.'}, status=404)

        serializer = ServicoAdminSerializer(servico, data=request.data, partial=True)
        if serializer.is_valid():
            servico_atualizado = serializer.save()
            return Response({
                'message': f'Serviço "{servico_atualizado.nome}" atualizado com sucesso.',
                'data': serializer.data
            })
        validation_errors = {field: msg[0] for field, msg in serializer.errors.items()}
        return Response(
            {
                'error': 'Erro de validação. Verifique os campos obrigatórios.',
                'fields': validation_errors,
                'required_fields': ['nome', 'descricao', 'categoria', 'status']
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None):
        """
        Exclusão de um Serviço.
        """
        try:
            servico = Servico.objects.get(pk=pk)
        except Servico.DoesNotExist:
            return Response({'error': 'Serviço não encontrado.'}, status=404)

        servico.delete()
        return Response({'message': 'Serviço excluído com sucesso.'}, status=status.HTTP_204_NO_CONTENT)