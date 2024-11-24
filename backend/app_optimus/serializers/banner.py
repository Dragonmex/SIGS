from rest_framework import serializers
from app_optimus.models.banner import Banner, ImagemBanner

class ImagemBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemBanner
        fields = ['id', 'imagem']

class BannerSerializer(serializers.ModelSerializer):
    imagens = ImagemBannerSerializer(many=True, read_only=True)

    class Meta:
        model = Banner
        fields = ['id', 'titulo', 'imagens']
