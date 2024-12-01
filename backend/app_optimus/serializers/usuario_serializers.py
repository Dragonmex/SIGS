from rest_framework import serializers
from app_optimus.models.usuarios_models import Usuario
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from app_optimus.models.usuarios_models import Cidadao, Servidor


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para exibir dados básicos do usuário.
    """
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'email', 'perfil', 'ativo', 'data_cadastro']


class CadastroUsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para criar novos usuários, com validação de senha e perfil.
    """
    class Meta:
        model = Usuario
        fields = ['email', 'password', 'perfil']
        extra_kwargs = {
            'password': {'write_only': True},  # Oculta o campo de senha na resposta
        }

    def validate_password(self, value):
        """
        Valida a força da senha, garantindo segurança.
        """
        if len(value) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        # Adicionar validações adicionais conforme necessário (números, caracteres especiais, etc.)
        return value

    def validate_perfil(self, value):
        """
        Valida o perfil para garantir que seja um valor permitido.
        """
        valid_profiles = [choice[0] for choice in Usuario.PERFIL_CHOICES]
        if value not in valid_profiles:
            raise ValidationError(f"Perfil inválido. Escolha um dos seguintes: {', '.join(valid_profiles)}.")
        return value

    def create(self, validated_data):
        """
        Cria um novo usuário com senha criptografada.
        """
        validated_data['password'] = make_password(validated_data['password'])
        try:
            return Usuario.objects.create(**validated_data)
        except Exception as e:
            raise serializers.ValidationError(f"Erro ao criar usuário: {str(e)}")

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