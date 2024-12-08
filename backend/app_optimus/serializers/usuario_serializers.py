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
    """
    Serializer para criar novos usuários, com validação de senha.
    Inclui a criação do perfil de cidadão automaticamente.
    """
    nome_completo = serializers.CharField(write_only=True)
    cpf = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['email', 'password', 'nome_completo', 'cpf']
        extra_kwargs = {
            'password': {'write_only': True},  # Oculta o campo de senha na resposta
        }

    def validate_password(self, value):
        """
        Valida a força da senha, garantindo segurança.
        """
        if len(value) < 8:
            raise ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return value

    def validate_cpf(self, value):
        """
        Valida o CPF para garantir que não está duplicado.
        """
        if Cidadao.objects.filter(cpf=value).exists():
            raise ValidationError("O CPF informado já está cadastrado.")
        return value

    def create(self, validated_data):
        """
        Cria um novo usuário e o associa a um Cidadão.
        """
        nome_completo = validated_data.pop('nome_completo')
        cpf = validated_data.pop('cpf')

        # Cria o usuário
        validated_data['password'] = make_password(validated_data['password'])
        usuario = Usuario.objects.create(perfil='cidadao', **validated_data)

        # Cria o perfil de cidadão
        Cidadao.objects.create(usuario=usuario, nome_completo=nome_completo, cpf=cpf)

        return usuario

    def validate_email(self, value):
        """
        Verifica se o e-mail já está cadastrado.
        """
        if Usuario.objects.filter(email=value).exists():
            raise ValidationError("O e-mail informado já está cadastrado.")
        return value

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
