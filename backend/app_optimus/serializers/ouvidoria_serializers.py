from rest_framework import serializers
from app_optimus.models.funcionalidades_models import Ouvidoria  

class ouvidoria_serializers(serializers.ModelSerializer): 
    class Meta:
        model = Ouvidoria
        fields = ['id', 'tipo', 'descricao', 'data_criacao', 'status', 'cidadao', 'servidor']
