from rest_framework.routers import DefaultRouter
from app_optimus.views.servicos import ServicoViewSetCidadao, ServicoViewSetServidor
from app_optimus.views.noticias import NoticiaViewSetCidadao, NoticiaViewSetServidor
from app_optimus.views.categorias import CategoriaServicoViewSet, CategoriaNoticiaViewSet
from app_optimus.views.servicos import SolicitacaoServicoViewSet, SolicitacaoServidorViewSet
from .views import OuvidoriaViewSet

# Instância do roteador
router = DefaultRouter()

# Rotas em Comum
router.register(r'ouvidorias', OuvidoriaViewSet, basename='ouvidoria')
router.register(r'servicos', ServicoViewSetCidadao, basename='servico-cidadao')
router.register(r'noticias', NoticiaViewSetCidadao, basename='noticia-cidadao')
router.register(r'solicitacoes', SolicitacaoServicoViewSet, basename='solicitacoes')
router.register(r'categorias-servicos', CategoriaServicoViewSet, basename='categoria-servico')
router.register(r'categorias-noticias', CategoriaNoticiaViewSet, basename='categoria-noticia')

# Rotas Exclusivas para servidores
router.register(r'servicos-admin', ServicoViewSetServidor, basename='servico-servidor')
router.register(r'noticias-admin', NoticiaViewSetServidor, basename='noticia-servidor')
router.register(r'solicitacoes-admin', SolicitacaoServidorViewSet, basename='solicitacoes-servidor')


# Inclui todas as rotas do roteador
api_router = router.urls

