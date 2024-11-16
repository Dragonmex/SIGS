from rest_framework import serializers
from app_home_feed.models import LinkRapido

class LinkRapidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkRapido
        fields = ['id', 'titulo', 'url']
