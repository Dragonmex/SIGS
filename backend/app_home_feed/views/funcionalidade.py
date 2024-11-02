from rest_framework import generics
from ..models.funcionalidade import Funcionalidade
from ..serializers.funcionalidade import FuncionalidadeSerializer

class FuncionalidadeListCreateView(generics.ListCreateAPIView):
    queryset = Funcionalidade.objects.all()
    serializer_class = FuncionalidadeSerializer
    
class FuncionalidadeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionalidade.objects.all()
    serializer_class = FuncionalidadeSerializer