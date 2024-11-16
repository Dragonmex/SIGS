from rest_framework import serializers
from app_home_feed.models import Noticia

class NoticiaSerializer(serializers.ModelSerializer):
    noticias_relacionadas = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Noticia.objects.all(), required=False
    )

    class Meta:
        model = Noticia
        fields = [
            'id',
            'titulo',
            'conteudo',
            'imagem',
            'categoria',
            'noticias_relacionadas',
            'data_publicacao'
        ]
