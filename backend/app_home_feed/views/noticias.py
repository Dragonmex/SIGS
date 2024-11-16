from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from app_home_feed.models.noticia import Noticia
from app_home_feed.models.categoria import Categoria
from app_home_feed.serializers.noticia import NoticiaSimpleSerializer, NoticiaSerializer
from app_home_feed.serializers.categoria import CategoriaSerializer
from app_home_feed.pagination import CustomPageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404



class NoticiasListView(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSimpleSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categoria', 'data_publicacao']
    search_fields = ['titulo', 'conteudo']
    ordering_fields = ['data_publicacao', 'titulo']

    def get(self, request, *args, **kwargs):
        # Obter todas as categorias para exibir no front-end
        categorias = Categoria.objects.all()
        categorias_serialized = CategoriaSerializer(categorias, many=True).data

        # Obter os dados paginados e filtrados das notícias
        response = super().get(request, *args, **kwargs)

        # Reorganizar a resposta para ter a ordem desejada
        response.data = {
            "count": response.data["count"],
            "next": response.data["next"],
            "previous": response.data["previous"],
            "categorias": categorias_serialized,
            "results": response.data["results"],
        }

        return response

class NoticiaDetailView(APIView):
    def get(self, request, pk):
        # Obtém a notícia específica ou retorna 404 se não existir
        noticia = get_object_or_404(Noticia, pk=pk)
        
        # Serializa a notícia usando o serializer completo
        noticia_serialized = NoticiaSerializer(noticia).data

        # Retorna a notícia detalhada
        return Response(noticia_serialized, status=status.HTTP_200_OK)