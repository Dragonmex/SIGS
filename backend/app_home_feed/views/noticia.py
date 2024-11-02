from rest_framework import generics
from ..models.noticia import Noticia
from ..serializers.noticia import NoticiaSerializer

class NoticiaListCreateView(generics.ListCreateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    
class NoticiaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer