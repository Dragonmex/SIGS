from rest_framework import serializers
from ..models.banner import Banner

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'titulo', 'imagem', 'descricao', 'link']