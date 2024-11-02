from rest_framework import generics
from ..models.link_rapido import LinkRapido
from ..serializers.link_rapido import LinkRapidoSerializer

class LinkRapidoListCreateView(generics.ListCreateAPIView):
    queryset = LinkRapido.objects.all()
    serializer_class = LinkRapidoSerializer
    
class LinkRapidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkRapido.objects.all()
    serializer_class = LinkRapidoSerializer