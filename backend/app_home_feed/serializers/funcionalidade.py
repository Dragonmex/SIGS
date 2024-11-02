from rest_framework import serializers
from ..models.funcionalidade import Funcionalidade

class FuncionalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionalidade
        fields = ['id', 'nome', 'descricao']