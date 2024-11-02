from rest_framework import serializers
from ..models.video import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'titulo', 'descricao', 'embed_url']