from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import AnonymousUser
from app_optimus.models.funcionalidades_models import Servico, Noticia, CategoriaNoticia
from app_optimus.serializers.cidadao_serializers import ServicoSerializer as ServicoCidadaoSerializer, NoticiaSerializer as NoticiaCidadaoSerializer
from app_optimus.serializers.servidor_serializers import ServicoAdminSerializer as ServicoServidorSerializer, NoticiaAdminSerializer as NoticiaServidorSerializer

class HomeAPI(APIView):
    """
    HomeAPI adaptada para exibir dados personalizados com base no perfil do usuário.
    """

    def get(self, request, *args, **kwargs):
        try:
            # Dados comuns
            categorias_noticias = CategoriaNoticia.objects.all()

            # Simular perfil padrão para usuários não autenticados
            if isinstance(request.user, AnonymousUser):
                perfil = 'cidadao'  # Perfil padrão para usuários anônimos
            else:
                perfil = request.user.perfil

            # Lógica baseada no perfil do usuário
            if perfil == 'cidadao':
                servicos = Servico.objects.filter(status=True).order_by('-data_criacao')[:6]
                noticias = Noticia.objects.order_by('-data_publicacao')[:6]

                servico_serializer = ServicoCidadaoSerializer(servicos, many=True)
                noticia_serializer = NoticiaCidadaoSerializer(noticias, many=True)

            elif perfil == 'servidor':
                servicos = Servico.objects.all().order_by('-data_criacao')[:6]
                noticias = Noticia.objects.order_by('-data_publicacao')[:6]

                servico_serializer = ServicoServidorSerializer(servicos, many=True)
                noticia_serializer = NoticiaServidorSerializer(noticias, many=True)

            else:
                return Response({'error': 'Perfil de usuário não suportado.'}, status=status.HTTP_403_FORBIDDEN)

            # Dados finais para resposta
            data = {
                'servicos': servico_serializer.data,
                'noticias': noticia_serializer.data,
                'categorias_noticias': [{'id': categoria.id, 'nome': categoria.nome} for categoria in categorias_noticias],
            }

            return Response(data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Erro ao buscar dados: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
