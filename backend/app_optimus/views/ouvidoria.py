from rest_framework import viewsets
from app_optimus.models.funcionalidades_models import Ouvidoria
from app_optimus.serializers.ouvidoria_serializers import ouvidoria_serializers

class OuvidoriaViewSet(viewsets.ModelViewSet):
    queryset = Ouvidoria.objects.all()
    serializer_class= ouvidoria_serializers