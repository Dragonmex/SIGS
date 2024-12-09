from rest_framework import serializers
from app_optimus.models.usuarios_models import Usuario, Cidadao, Servidor
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para exibir dados básicos do usuário.
    """
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'email', 'perfil', 'ativo', 'data_cadastro']


class CadastroUsuarioSerializer(serializers.ModelSerializer):
    nome_completo = serializers.CharField(write_only=True)
    cpf = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['email', 'password', 'nome_completo', 'cpf']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return value

    def validate_cpf(self, value):
        if Cidadao.objects.filter(cpf=value).exists():
            raise ValidationError("O CPF informado já está cadastrado.")
        return value

    def create(self, validated_data):
        nome_completo = validated_data.pop('nome_completo')
        cpf = validated_data.pop('cpf')

        validated_data['password'] = make_password(validated_data['password'])

        usuario = Usuario.objects.create(perfil='cidadao', **validated_data)
        Cidadao.objects.create(usuario=usuario, nome_completo=nome_completo, cpf=cpf)

        return usuario

class CidadaoSerializer(serializers.ModelSerializer):
    """
    Serializer para o perfil de cidadão.
    """
    class Meta:
        model = Cidadao
        fields = ['nome_completo', 'cpf', 'data_nascimento']


class ServidorSerializer(serializers.ModelSerializer):
    """
    Serializer para o perfil de servidor.
    """
    class Meta:
        model = Servidor
        fields = ['nome_completo', 'cargo', 'departamento']
