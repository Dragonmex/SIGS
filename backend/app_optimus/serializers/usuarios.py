from rest_framework import serializers
from app_optimus.models import Usuario, Cidadao, Servidor
from django.contrib.auth.hashers import make_password


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'email', 'perfil', 'ativo', 'data_cadastro']


class CidadaoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Cidadao
        fields = ['usuario', 'nome_completo', 'cpf', 'data_nascimento']


class ServidorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Servidor
        fields = ['usuario', 'nome_completo', 'cargo', 'departamento']



class CadastroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'password', 'perfil']
        extra_kwargs = {
            'password': {'write_only': True},  # Garante que a senha não será exibida
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Usuario.objects.create(**validated_data)
