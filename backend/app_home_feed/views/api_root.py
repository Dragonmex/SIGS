from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'banners': reverse('banner-list', request=request, format=format),
        'categorias': reverse('categoria-list', request=request, format=format),
        'links-rapidos': reverse('linkrapido-list', request=request, format=format),
        'noticias': reverse('noticia-list', request=request, format=format),
        'funcionalidades': reverse('funcionalidade-list', request=request, format=format),
        'videos': reverse('video-list', request=request, format=format),
    })
