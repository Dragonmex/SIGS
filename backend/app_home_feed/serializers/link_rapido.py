from rest_framework import serializers
from ..models.link_rapido import LinkRapido

class LinkRapidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkRapido
        fields = ['id', 'nome', 'icone', 'url']