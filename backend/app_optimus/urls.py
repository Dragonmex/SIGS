from django.urls import path, include
from app_optimus.routers import api_router
from app_optimus.views.usuarios import LoginAPI, LogoutAPI, CadastroUsuarioAPI, AlterarSenhaAPI, RedefinirSenhaAPI, ConfirmarRedefinicaoSenhaAPI
from app_optimus.views.home import HomeAPI
from app_optimus.views.perfil import PerfilAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from app_optimus.routers import api_router

# Instância do roteador para endpoints adicionais
router = DefaultRouter()

urlpatterns = [
    # Endpoints de autenticação
    path('register/', CadastroUsuarioAPI.as_view(), name='api-cadastro'),
    path('login/', LoginAPI.as_view(), name='api-login'),
    path('logout/', LogoutAPI.as_view(), name='api-logout'),
    path('perfil/', PerfilAPI.as_view(), name='perfil'),
    path('alterar-senha/', AlterarSenhaAPI.as_view(), name='alterar-senha'),
    path('redefinir-senha/', RedefinirSenhaAPI.as_view(), name='redefinir-senha'),
    path('redefinicao-senha/', ConfirmarRedefinicaoSenhaAPI.as_view(), name='redefinicao-senha'),
    path('home/', HomeAPI.as_view(), name='api-home'),

    # Rotas dinâmicas do roteador
    path('', include(api_router)),
]
