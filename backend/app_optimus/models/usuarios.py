from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid

class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, perfil=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um endereço de email.")
        if not perfil:
            raise ValueError("O campo 'perfil' é obrigatório para criar um usuário.")

        email = self.normalize_email(email)
        extra_fields.setdefault('ativo', True)  # Garante que o campo 'ativo' tenha um valor padrão
        user = self.model(email=email, perfil=perfil, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Configurações específicas para superusuário
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("O superusuário deve ter is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("O superusuário deve ter is_superuser=True.")

        # Define o perfil automaticamente para superusuário
        return self.create_user(email, password, perfil='admin', **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    PERFIL_CHOICES = [
        ('servidor', 'Servidor'),
        ('cidadao', 'Cidadão'),
        ('admin', 'Administrador'),
    ]

    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    perfil = models.CharField(max_length=50, choices=PERFIL_CHOICES)  # Dropdown para o perfil
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # Criar o registro correspondente com base no perfil, sem CPF
        if self.perfil == 'servidor' and not hasattr(self, 'servidor'):
            Servidor.objects.create(usuario=self)
        elif self.perfil == 'cidadao' and not hasattr(self, 'cidadao'):
            Cidadao.objects.create(usuario=self)  # Sem necessidade de CPF


    def get_user_id(self):
        return str(self.id_usuario)
    
class Cidadao(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, primary_key=True, related_name='cidadao'
    )
    nome_completo = models.CharField(max_length=255, null=True, blank=True)  # Pode ser preenchido depois
    cpf = models.CharField(max_length=11, unique=False, null=True, blank=True)  # Não obrigatório
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome_completo if self.nome_completo else f"Cidadão {self.usuario.email}"


class Servidor(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='servidor'
    )
    nome_completo = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome_completo} - {self.cargo}"

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"
