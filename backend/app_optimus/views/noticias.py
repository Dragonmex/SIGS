from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from app_optimus.permissions.servidor import IsServidor
from app_optimus.models.funcionalidades_models import Noticia
from app_optimus.serializers.servidor_serializers import NoticiaAdminSerializer
from app_optimus.serializers.cidadao_serializers import NoticiaSerializer, NoticiaDetalhadaSerializer

class NoticiaViewSetCidadao(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Noticia.objects.order_by('-data_publicacao')
        serializer = NoticiaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            noticia = Noticia.objects.get(pk=pk)
            serializer = NoticiaDetalhadaSerializer(noticia)
            return Response(serializer.data)
        except Noticia.DoesNotExist:
            return Response({'error': 'Notícia não encontrada.'}, status=404)

class NoticiaViewSetServidor(ViewSet):
    """
    ViewSet completo para gerenciamento de Notícias pelos Servidores.
    """
    permission_classes = [IsAuthenticated, IsServidor]

    def list(self, request):
        """
        Listagem de todas as Notícias.
        """
        queryset = Noticia.objects.order_by('-data_publicacao')
        serializer = NoticiaAdminSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhamento de uma Notícia específica.
        """
        try:
            noticia = Noticia.objects.get(pk=pk)
            serializer = NoticiaAdminSerializer(noticia)
            return Response(serializer.data)
        except Noticia.DoesNotExist:
            return Response({'error': 'Notícia não encontrada.'}, status=404)

    def create(self, request):
        """
        Criação de uma nova Notícia.
        """
        serializer = NoticiaAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Atualização de uma Notícia existente.
        """
        try:
            noticia = Noticia.objects.get(pk=pk)
        except Noticia.DoesNotExist:
            return Response({'error': 'Notícia não encontrada.'}, status=404)

        serializer = NoticiaAdminSerializer(noticia, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Exclusão de uma Notícia.
        """
        try:
            noticia = Noticia.objects.get(pk=pk)
        except Noticia.DoesNotExist:
            return Response({'error': 'Notícia não encontrada.'}, status=404)

        noticia.delete()
        return Response({'message': 'Notícia excluída com sucesso.'}, status=status.HTTP_204_NO_CONTENT)