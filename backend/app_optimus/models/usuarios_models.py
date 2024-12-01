from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
import uuid


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, perfil=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um endereço de email válido.")
        if not perfil:
            raise ValueError("O campo 'perfil' é obrigatório para criar um usuário.")

        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, perfil=perfil, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superusuários devem ter is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superusuários devem ter is_superuser=True.")

        return self.create_user(email, password, perfil='admin', **extra_fields)

    def ativos(self):
        return self.filter(is_active=True)

    def por_perfil(self, perfil):
        return self.filter(perfil=perfil)


class Usuario(AbstractBaseUser, PermissionsMixin):
    PERFIL_CHOICES = [
        ('servidor', 'Servidor'),
        ('cidadao', 'Cidadão'),
        ('admin', 'Administrador'),
    ]

    id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    perfil = models.CharField(max_length=50, choices=PERFIL_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['-data_cadastro']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.perfil not in dict(self.PERFIL_CHOICES):
            raise ValueError(f"Perfil '{self.perfil}' inválido.")
        super().save(*args, **kwargs)

        if self.perfil == 'servidor' and not hasattr(self, 'servidor'):
            Servidor.objects.get_or_create(usuario=self)
        elif self.perfil == 'cidadao' and not hasattr(self, 'cidadao'):
            Cidadao.objects.get_or_create(usuario=self)


class Cidadao(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, primary_key=True, related_name='cidadao'
    )
    nome_completo = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Cidadão"
        verbose_name_plural = "Cidadãos"

    def __str__(self):
        return self.nome_completo or f"Cidadão {self.usuario.email}"


class Servidor(models.Model):
    usuario = models.OneToOneField(
        Usuario, on_delete=models.CASCADE, primary_key=True, related_name='servidor'
    )
    nome_completo = models.CharField(max_length=255)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"
        ordering = ['nome_completo']

    def __str__(self):
        return f"{self.nome_completo} - {self.cargo}"
