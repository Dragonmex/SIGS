from rest_framework import serializers
from app_optimus.models.Servico import Servico

class ServicoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source='categoria.nome')

    class Meta:
        model = Servico
        fields = ['id', 'nome', 'descricao', 'categoria']