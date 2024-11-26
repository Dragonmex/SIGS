from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from app_optimus.models.usuarios_db import Usuario

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(senha, usuario.senha_hash):
                # Armazena o ID do usuário na sessão
                request.session['usuario_id'] = str(usuario.id_usuario)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('home')  # Redireciona para a home
            else:
                messages.error(request, 'Senha inválida.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
    return render(request, 'login.html')
