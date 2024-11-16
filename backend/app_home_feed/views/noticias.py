from rest_framework.views import APIView
from app_home_feed.models.noticia import Noticia
from app_home_feed.models.categoria import Categoria
from app_home_feed.serializers.noticia import NoticiaSerializer
from app_home_feed.serializers.categoria import CategoriaSerializer
from app_home_feed.pagination import PageNumberPagination

class NoticiasListView(APIView):
    def get(self, request):
        # Obter todas as categorias para exibir no front-end
        categorias = Categoria.objects.all()
        categorias_serialized = CategoriaSerializer(categorias, many=True).data

        # Filtro por categoria, se fornecido
        categoria_id = request.GET.get('categoria_id')
        noticias = Noticia.objects.all()
        if categoria_id:
            # Filtra as notícias pela categoria, se o ID for fornecido
            noticias = noticias.filter(categoria_id=categoria_id)

        # Paginar as notícias
        paginator = PageNumberPagination()
        paginated_noticias = paginator.paginate_queryset(noticias, request)
        noticias_serialized = NoticiaSerializer(paginated_noticias, many=True).data

        # Retorna as categorias e as notícias paginadas
        return paginator.get_paginated_response({
            "categorias": categorias_serialized,
            "noticias": noticias_serialized
        })
