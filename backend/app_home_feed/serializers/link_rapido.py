# serializers/link_rapido.py
from rest_framework import serializers
from ..models.link_rapido import LinkRapido

class LinkRapidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkRapido
        fields = ['id', 'titulo', 'url', 'descricao']  # Campos corretos do modelo
