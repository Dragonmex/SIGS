from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from app_optimus.models.usuarios_models import Usuario
from app_optimus.serializers.usuario_serializers import CadastroUsuarioSerializer

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