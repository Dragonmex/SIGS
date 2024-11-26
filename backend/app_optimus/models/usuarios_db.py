from django.db import models
import uuid

# Usuário
class Usuario(models.Model):
    PERFIL_CHOICES = [
        ('cidadao', 'Cidadão'),
        ('servidor', 'Servidor'),
    ]

    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    senha_hash = models.CharField(max_length=255)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Perfil Cidadão
class Cidadao(models.Model):
    id_cidadao = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='cidadao')
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('Outro', 'Outro')], null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nome_completo


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    cidadao = models.ForeignKey(Cidadao, on_delete=models.CASCADE, related_name='enderecos')
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"


class Saude(models.Model):
    id_saude = models.AutoField(primary_key=True)
    cidadao = models.OneToOneField(Cidadao, on_delete=models.CASCADE, related_name='saude')
    num_cartao_sus = models.CharField(max_length=15, unique=True, null=True, blank=True)
    necessidades_especiais = models.BooleanField(default=False)

    def __str__(self):
        return f"SUS: {self.num_cartao_sus}" if self.num_cartao_sus else "Sem cartão SUS"


class Educacao(models.Model):
    NIVEL_EDUCACIONAL_CHOICES = [
        ('Fundamental', 'Fundamental'),
        ('Medio', 'Médio'),
        ('Superior', 'Superior'),
        ('Outro', 'Outro'),
    ]

    id_educacao = models.AutoField(primary_key=True)
    cidadao = models.OneToOneField(Cidadao, on_delete=models.CASCADE, related_name='educacao')
    nivel_educacional = models.CharField(max_length=20, choices=NIVEL_EDUCACIONAL_CHOICES)
    instituicao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.nivel_educacional} - {self.instituicao}" if self.instituicao else self.nivel_educacional


# Perfil Servidor
class Servidor(models.Model):
    id_servidor = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='servidor')
    nome_completo = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_completo} ({self.cargo})"
