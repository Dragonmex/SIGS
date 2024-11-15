# views/feed.py

from rest_framework.views import APIView
from rest_framework.response import Response
from app_home_feed.models.banner import Banner
from app_home_feed.models.categoria import Categoria
from app_home_feed.models.link_rapido import LinkRapido
from app_home_feed.models.noticia import Noticia
from app_home_feed.models.video import Video
from app_home_feed.serializers.banner import BannerSerializer
from app_home_feed.serializers.categoria import CategoriaSerializer
from app_home_feed.serializers.link_rapido import LinkRapidoSerializer
from app_home_feed.serializers.noticia import NoticiaSerializer
from app_home_feed.serializers.video import VideoSerializer

class FeedView(APIView):
    def get(self, request):
        # Parâmetros para decidir o que mostrar
        show_banners = request.GET.get('show_banners', 'true').lower() == 'true'
        show_categorias = request.GET.get('show_categorias', 'true').lower() == 'true'
        show_links = request.GET.get('show_links', 'true').lower() == 'true'
        show_noticias = request.GET.get('show_noticias', 'true').lower() == 'true'
        show_videos = request.GET.get('show_videos', 'true').lower() == 'true'

        # Inicializando os dados
        banners_serialized = categorias_serialized = links_serialized = noticias_serialized = videos_serialized = []

        # Buscando e serializando apenas os itens que devem ser exibidos
        if show_banners:
            banners = Banner.objects.all()
            banners_serialized = BannerSerializer(banners, many=True).data

        if show_categorias:
            categorias = Categoria.objects.all()
            categorias_serialized = CategoriaSerializer(categorias, many=True).data

        if show_links:
            links_rapidos = LinkRapido.objects.all()
            links_serialized = LinkRapidoSerializer(links_rapidos, many=True).data

        if show_noticias:
            noticias = Noticia.objects.all()
            noticias_serialized = NoticiaSerializer(noticias, many=True).data

        if show_videos:
            videos = Video.objects.all()
            videos_serialized = VideoSerializer(videos, many=True).data

        # Retornando os itens selecionados organizados por seção
        return Response({
            "banners": banners_serialized,
            "categorias": categorias_serialized,
            "links_rapidos": links_serialized,
            "noticias": noticias_serialized,
            "videos": videos_serialized
        })
