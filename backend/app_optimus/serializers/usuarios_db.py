from rest_framework import serializers
from app_optimus.models.usuarios_db import Usuario, Cidadao, Endereco, Saude, Educacao, Servidor

class CadastroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'senha_hash', 'perfil']
        extra_kwargs = {
            'senha_hash': {'write_only': True},
        }

    def create(self, validated_data):
        # Criar o usuário e criptografar a senha
        usuario = Usuario(
            email=validated_data['email'],
            perfil=validated_data['perfil']
        )
        # Simulação de hash da senha (substituir por um método real como o `make_password` do Django)
        usuario.senha_hash = validated_data['senha_hash']
        usuario.save()
        return usuario

# Serializer para o modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id_usuario', 'email', 'senha_hash', 'perfil', 
            'ativo', 'data_cadastro'
        ]
        extra_kwargs = {
            'senha_hash': {'write_only': True},  # Esconde o hash da senha na resposta
        }


# Serializer para o modelo Cidadao
class CidadaoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Cidadao
        fields = [
            'id_cidadao', 'usuario', 'nome_completo', 'cpf', 
            'data_nascimento', 'sexo', 'telefone'
        ]


# Serializer para o modelo Endereco
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = [
            'id_endereco', 'cidadao', 'logradouro', 
            'numero', 'bairro', 'cidade', 'estado', 'cep'
        ]


# Serializer para o modelo Saude
class SaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saude
        fields = [
            'id_saude', 'cidadao', 'num_cartao_sus', 
            'necessidades_especiais'
        ]


# Serializer para o modelo Educacao
class EducacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educacao
        fields = [
            'id_educacao', 'cidadao', 'nivel_educacional', 
            'instituicao'
        ]


# Serializer para o modelo Servidor
class ServidorSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Servidor
        fields = [
            'id_servidor', 'usuario', 'nome_completo', 
            'cargo', 'departamento'
        ]
