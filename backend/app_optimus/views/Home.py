from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from app_optimus.models import Servico, Noticia, CategoriaNoticia
from django.shortcuts import get_object_or_404
from app_optimus.serializers import NoticiaDetalhadaSerializer, NoticiaSerializer
from app_optimus.pagination import CustomPageNumberPagination


class HomeAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            # Buscar serviços ativos e últimas notícias
            servicos = Servico.objects.filter(status=True).order_by('-data_criacao')[:6]
            noticias = Noticia.objects.order_by('-data_publicacao')[:6]
            categorias_noticias = CategoriaNoticia.objects.all()

            # Preparar a resposta JSON
            data = {
                'servicos': [
                    {
                        'id': servico.id,
                        'nome': servico.nome,
                        'descricao': servico.descricao,
                        'data_criacao': servico.data_criacao,
                    }
                    for servico in servicos
                ],
                'noticias': [
                    {
                        'id': noticia.id,
                        'titulo': noticia.titulo,
                        'resumo': noticia.resumo,
                        'data_publicacao': noticia.data_publicacao,
                        'categoria': noticia.categoria.nome,
                        'imagem': noticia.imagem.url if noticia.imagem else None,
                    }
                    for noticia in noticias
                ],
                'categorias_noticias': [
                    {'id': categoria.id, 'nome': categoria.nome}
                    for categoria in categorias_noticias
                ],
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class NoticiaDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, noticia_id, *args, **kwargs):
        # Busca a notícia pelo ID
        noticia = get_object_or_404(Noticia, id=noticia_id)
        serializer = NoticiaDetalhadaSerializer(noticia)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NoticiaListView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Noticia.objects.all().order_by('-data_publicacao')
    serializer_class = NoticiaSerializer
    pagination_class = CustomPageNumberPagination