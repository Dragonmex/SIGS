from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from app_optimus.models.usuarios_models import Usuario, Cidadao, Servidor
from app_optimus.models.funcionalidades_models import CategoriaNoticia, CategoriaServico, Noticia, Servico
from django.contrib.auth.forms import UserChangeForm

# Registro de categorias e serviços
admin.site.register(CategoriaNoticia)
admin.site.register(Noticia)
admin.site.register(CategoriaServico)
admin.site.register(Servico)

# Formulário para edição de usuários no admin
class UsuarioChangeForm(UserChangeForm):
    password = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = Usuario
        fields = ('email', 'perfil', 'is_staff', 'is_active', 'ativo')

    def save(self, commit=True):
        # Salva apenas os campos relacionados ao usuário
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Atualiza apenas a senha
        if commit:
            user.save()  # Salva o usuário sem alterar os dados do Cidadao
        return user

# Configuração do modelo Usuario no admin
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    form = UsuarioChangeForm
    list_display = ('email', 'perfil', 'is_staff', 'ativo')
    search_fields = ('email',)

# Formulário customizado para validação do CPF no admin
class CidadaoAdminForm(forms.ModelForm):
    class Meta:
        model = Cidadao
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and Cidadao.objects.filter(cpf=cpf).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Este CPF já está em uso por outro cidadão.")
        return cpf

# Configuração do modelo Cidadao no admin
@admin.register(Cidadao)
class CidadaoAdmin(admin.ModelAdmin):
    form = CidadaoAdminForm
    list_display = ('usuario', 'nome_completo', 'cpf')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.message_user(request, "CPF atualizado com sucesso!")

# Configuração do modelo Servidor no admin
@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nome_completo', 'cargo', 'departamento')
