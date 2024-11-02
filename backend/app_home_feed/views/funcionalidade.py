from rest_framework import generics
from app_home_feed.models.funcionalidade import Funcionalidade
from app_home_feed.serializers.funcionalidade import FuncionalidadeSerializer

class FuncionalidadeListCreateView(generics.ListCreateAPIView):
    queryset = Funcionalidade.objects.all()
    serializer_class = FuncionalidadeSerializer

class FuncionalidadeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionalidade.objects.all()
    serializer_class = FuncionalidadeSerializer