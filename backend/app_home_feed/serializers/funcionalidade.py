from rest_framework import serializers
from app_home_feed.models.funcionalidade import Funcionalidade

class FuncionalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionalidade
        fields = ['id', 'nome', 'descricao', 'icone', 'rota']