from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from app_optimus.models.usuarios_db import Usuario
from app_optimus.serializers.usuarios_db import CadastroUsuarioSerializer

def cadastro_view(request):
    if request.method == 'POST':
        serializer = CadastroUsuarioSerializer(data=request.POST)
        if serializer.is_valid():
            usuario = Usuario(
                email=serializer.validated_data['email'],
                perfil=serializer.validated_data['perfil']
            )
            usuario.senha_hash = make_password(serializer.validated_data['senha_hash'])
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para acessar.')
            return redirect('login')  # Redireciona para a página de login
        else:
            messages.error(request, 'Erro ao realizar o cadastro. Verifique os dados.')
    return render(request, 'cadastro.html')
