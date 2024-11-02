from rest_framework import serializers
from ..models.noticia import Noticia
from ..models.categoria import Categoria

class NoticiaSerializer(serializers.ModelSerializer):
    # Exibir o nome da categoria no output para fácil leitura
    categoria = serializers.SlugRelatedField(
        slug_field='nome', 
        queryset=Categoria.objects.all()
    )

    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'conteudo', 'categoria', 'data_publicacao']
