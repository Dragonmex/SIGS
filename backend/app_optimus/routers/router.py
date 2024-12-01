from rest_framework.routers import DefaultRouter
from app_optimus.views.servicos import ServicoViewSetCidadao, ServicoViewSetServidor
from app_optimus.views.noticias import NoticiaViewSetCidadao, NoticiaViewSetServidor
from app_optimus.views.categorias import CategoriaServicoViewSet, CategoriaNoticiaViewSet

# Instância do roteador
router = DefaultRouter()

# Rotas em Comum
router.register(r'servicos', ServicoViewSetCidadao, basename='servico-cidadao')
router.register(r'noticias', NoticiaViewSetCidadao, basename='noticia-cidadao')
router.register(r'categorias-servicos', CategoriaServicoViewSet, basename='categoria-servico')
router.register(r'categorias-noticias', CategoriaNoticiaViewSet, basename='categoria-noticia')

# Rotas Exclusivas para servidores
router.register(r'servicos-admin', ServicoViewSetServidor, basename='servico-servidor')
router.register(r'noticias-admin', NoticiaViewSetServidor, basename='noticia-servidor')

# Isso permite acessar as URLs registradas pelo roteador
urlpatterns = router.urls
