from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from app_optimus.models.funcionalidades_models import CategoriaServico, CategoriaNoticia
from app_optimus.serializers.servidor_serializers import CategoriaServicoSerializer, CategoriaNoticiaSerializer

class CategoriaServicoViewSet(ViewSet):
    """
    ViewSet completo para gerenciamento de Categorias de Serviços.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Listagem de todas as Categorias de Serviços.
        """
        queryset = CategoriaServico.objects.all().order_by('nome')
        serializer = CategoriaServicoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhamento de uma Categoria de Serviço.
        """
        try:
            categoria = CategoriaServico.objects.get(pk=pk)
        except CategoriaServico.DoesNotExist:
            return Response({'error': 'Categoria de Serviço não encontrada.'}, status=404)

        serializer = CategoriaServicoSerializer(categoria)
        return Response(serializer.data)

    def create(self, request):
        """
        Criação de uma nova Categoria de Serviço.
        """
        serializer = CategoriaServicoSerializer(data=request.data)
        if serializer.is_valid():
            categoria = serializer.save()
            return Response({
                'message': f'Categoria de Serviço "{categoria.nome}" criada com sucesso.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Atualização de uma Categoria de Serviço existente.
        """
        try:
            categoria = CategoriaServico.objects.get(pk=pk)
        except CategoriaServico.DoesNotExist:
            return Response({'error': 'Categoria de Serviço não encontrada.'}, status=404)

        serializer = CategoriaServicoSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            categoria = serializer.save()
            return Response({
                'message': f'Categoria de Serviço "{categoria.nome}" atualizada com sucesso.',
                'data': serializer.data
            })
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Exclusão de uma Categoria de Serviço.
        """
        try:
            categoria = CategoriaServico.objects.get(pk=pk)
        except CategoriaServico.DoesNotExist:
            return Response({'error': 'Categoria de Serviço não encontrada.'}, status=404)

        categoria_nome = categoria.nome
        categoria.delete()
        return Response({'message': f'Categoria de Serviço "{categoria_nome}" excluída com sucesso.'}, status=status.HTTP_204_NO_CONTENT)


class CategoriaNoticiaViewSet(ViewSet):
    """
    ViewSet completo para gerenciamento de Categorias de Notícias.
    """
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        Listagem de todas as Categorias de Notícias.
        """
        queryset = CategoriaNoticia.objects.all().order_by('nome')
        serializer = CategoriaNoticiaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Detalhamento de uma Categoria de Notícia.
        """
        try:
            categoria = CategoriaNoticia.objects.get(pk=pk)
        except CategoriaNoticia.DoesNotExist:
            return Response({'error': 'Categoria de Notícia não encontrada.'}, status=404)

        serializer = CategoriaNoticiaSerializer(categoria)
        return Response(serializer.data)

    def create(self, request):
        """
        Criação de uma nova Categoria de Notícia.
        """
        serializer = CategoriaNoticiaSerializer(data=request.data)
        if serializer.is_valid():
            categoria = serializer.save()
            return Response({
                'message': f'Categoria de Notícia "{categoria.nome}" criada com sucesso.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Atualização de uma Categoria de Notícia existente.
        """
        try:
            categoria = CategoriaNoticia.objects.get(pk=pk)
        except CategoriaNoticia.DoesNotExist:
            return Response({'error': 'Categoria de Notícia não encontrada.'}, status=404)

        serializer = CategoriaNoticiaSerializer(categoria, data=request.data, partial=True)
        if serializer.is_valid():
            categoria = serializer.save()
            return Response({
                'message': f'Categoria de Notícia "{categoria.nome}" atualizada com sucesso.',
                'data': serializer.data
            })
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Exclusão de uma Categoria de Notícia.
        """
        try:
            categoria = CategoriaNoticia.objects.get(pk=pk)
        except CategoriaNoticia.DoesNotExist:
            return Response({'error': 'Categoria de Notícia não encontrada.'}, status=404)

        categoria_nome = categoria.nome
        categoria.delete()
        return Response({'message': f'Categoria de Notícia "{categoria_nome}" excluída com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
