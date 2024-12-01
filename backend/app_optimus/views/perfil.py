from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from app_optimus.models.usuarios_models import Cidadao, Servidor
from app_optimus.serializers.usuario_serializers import (
    UsuarioSerializer,
    CidadaoSerializer,
    ServidorSerializer
)


class PerfilAPI(APIView):
    """
    API para gerenciar o perfil do usuário autenticado.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retorna os dados do perfil do usuário autenticado.
        """
        usuario = request.user

        if usuario.perfil == 'cidadao':
            serializer = CidadaoSerializer(usuario.cidadao)
        elif usuario.perfil == 'servidor':
            serializer = ServidorSerializer(usuario.servidor)
        else:
            serializer = UsuarioSerializer(usuario)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        """
        Atualiza os dados do perfil do usuário autenticado.
        """
        usuario = request.user

        if usuario.perfil == 'cidadao':
            try:
                perfil = usuario.cidadao
            except Cidadao.DoesNotExist:
                return Response({'error': 'Perfil de cidadão não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CidadaoSerializer(perfil, data=request.data, partial=True)
        elif usuario.perfil == 'servidor':
            try:
                perfil = usuario.servidor
            except Servidor.DoesNotExist:
                return Response({'error': 'Perfil de servidor não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

            serializer = ServidorSerializer(perfil, data=request.data, partial=True)
        else:
            serializer = UsuarioSerializer(usuario, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Perfil atualizado com sucesso!', 'data': serializer.data}, status=status.HTTP_200_OK)

        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        Exclui o perfil do usuário autenticado.
        """
        usuario = request.user

        try:
            usuario.delete()
            return Response({'message': 'Perfil excluído com sucesso!'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': f'Erro ao excluir o perfil: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
