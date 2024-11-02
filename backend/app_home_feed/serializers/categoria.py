from rest_framework import serializers
from ..models.categoria import Categoria
from ..models.funcionalidade import Funcionalidade
from .funcionalidade import FuncionalidadeSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    funcionalidades = FuncionalidadeSerializer(many=True)

    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao', 'funcionalidades']