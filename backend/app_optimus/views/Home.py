from rest_framework.views import APIView
from rest_framework.response import Response
from app_optimus.models import Noticia, Servico
from app_optimus.serializers import NoticiaSerializer, ServicoSerializer

class Home(APIView):
    def get(self, request):
        noticias_limit = int(request.query_params.get('noticias_limit', 5))
        servicos_limit = int(request.query_params.get('servicos_limit', 3))

        noticias = Noticia.objects.order_by('-data_publicacao')[:noticias_limit]
        servicos = Servico.objects.filter(status=True).order_by('-data_criacao')[:servicos_limit]

        noticias_serializer = NoticiaSerializer(noticias, many=True)
        servicos_serializer = ServicoSerializer(servicos, many=True)

        links_uteis = [
            {"nome": "Portal da Transparência", "url": "https://www.portaltransparencia.gov.br"},
            {"nome": "Consulta de IPTU", "url": "https://www.prefeitura.gov.br/consulta-iptu"},
            {"nome": "Agendamento de Serviços Municipais", "url": "https://www.prefeitura.gov.br/agendamento-servicos"},
            {"nome": "Ouvidoria Municipal", "url": "https://www.prefeitura.gov.br/ouvidoria"},
            {"nome": "Calendário de Eventos Culturais", "url": "https://www.prefeitura.gov.br/eventos-culturais"},
]

        return Response({
            "noticias": noticias_serializer.data,
            "servicos_destaque": servicos_serializer.data,
            "links_uteis": links_uteis
        })