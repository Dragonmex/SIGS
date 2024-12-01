from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from app_optimus.models.usuarios_models import Usuario, Cidadao, Servidor
from app_optimus.serializers.usuario_serializers import CadastroUsuarioSerializer, CidadaoSerializer, ServidorSerializer


class LoginAPI(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')  # Alterado para 'password'

        if not email or not password:
            return Response({'error': 'E-mail e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(password, usuario.password):  # Alterado para 'password'
                # Gerar tokens JWT
                refresh = RefreshToken.for_user(usuario)
                refresh['user_id'] = str(usuario.id_usuario)  # Adiciona manualmente o campo `user_id` no payload do token

                return Response({
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                    'perfil': usuario.perfil,
                    'id_usuario': str(usuario.id_usuario),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Senha inválida.'}, status=status.HTTP_401_UNAUTHORIZED)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)


class LogoutAPI(APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'Refresh token é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Adiciona o token à lista negra, invalidando-o
            return Response({'success': 'Logout realizado com sucesso.'}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'Token inválido.'}, status=status.HTTP_400_BAD_REQUEST)
        
class CadastroUsuarioAPI(APIView):
    def post(self, request, *args, **kwargs):
        # Usando o serializer para validar os dados
        serializer = CadastroUsuarioSerializer(data=request.data)
        
        if serializer.is_valid():
            try:
                # Salvando o novo usuário
                serializer.save()
                return Response(
                    {"message": "Cadastro realizado com sucesso!"},
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                # Exceção para erros ao salvar
                return Response(
                    {"error": f"Erro interno ao salvar o usuário: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            # Caso os dados não sejam válidos, retornamos o erro
            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
            
            
class AlterarSenhaAPI(APIView):
    """
    Permite ao usuário autenticado alterar sua senha atual.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        senha_atual = request.data.get('senha_atual')
        nova_senha = request.data.get('nova_senha')

        if not senha_atual or not nova_senha:
            return Response({'error': 'Os campos senha_atual e nova_senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

        usuario = request.user

        # Verifica a senha atual
        if not check_password(senha_atual, usuario.password):
            return Response({'error': 'Senha atual incorreta.'}, status=status.HTTP_400_BAD_REQUEST)

        # Define a nova senha
        if len(nova_senha) < 8:
            return Response({'error': 'A nova senha deve ter pelo menos 8 caracteres.'}, status=status.HTTP_400_BAD_REQUEST)

        usuario.set_password(nova_senha)
        usuario.save()

        return Response({'message': 'Senha alterada com sucesso!'}, status=status.HTTP_200_OK)
    
class RedefinirSenhaAPI(APIView):
    """
    Permite ao usuário iniciar o processo de redefinição de senha.
    """
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'O campo email é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Usuario.objects.get(email=email)
            refresh = RefreshToken.for_user(usuario)
            reset_token = str(refresh.access_token)

            # Envia um e-mail para redefinir a senha
            send_mail(
                subject='Redefinição de Senha',
                message=f'Use o token abaixo para redefinir sua senha:\n\n{reset_token}',
                from_email='no-reply@app.com',
                recipient_list=[email],
                fail_silently=False,
            )

            return Response({'message': 'Instruções de redefinição enviadas para o e-mail fornecido.'}, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:
            return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
class ConfirmarRedefinicaoSenhaAPI(APIView):
    """
    API para confirmar a redefinição de senha do usuário.
    """
    def post(self, request):
        token = request.data.get("token")
        nova_senha = request.data.get("nova_senha")

        if not token or not nova_senha:
            return Response(
                {"error": "Token e nova senha são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Valida o token
            access_token = AccessToken(token)
            usuario_id = access_token["user_id"]

            # Recupera o usuário
            usuario = Usuario.objects.get(id_usuario=usuario_id)

            # Verifica os requisitos da nova senha
            if len(nova_senha) < 8:
                return Response({'error': 'A nova senha deve ter pelo menos 8 caracteres.'}, status=status.HTTP_400_BAD_REQUEST)

            # Define a nova senha
            usuario.set_password(nova_senha)
            usuario.save()

            return Response(
                {"message": "Senha redefinida com sucesso!"},
                status=status.HTTP_200_OK,
            )

        except Usuario.DoesNotExist:
            return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response(
                {"error": f"Erro ao redefinir senha: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )