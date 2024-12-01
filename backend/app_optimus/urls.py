from django.urls import path, include
from app_optimus.routers import api_router
from app_optimus.views.usuarios import LoginAPI, LogoutAPI, CadastroUsuarioAPI, AlterarSenhaAPI, RedefinirSenhaAPI, ConfirmarRedefinicaoSenhaAPI
from app_optimus.views.home import HomeAPI
from app_optimus.views.perfil import PerfilAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# URLs Globais
urlpatterns = [
    # Usuários
    path('api/register/', CadastroUsuarioAPI.as_view(), name='api-cadastro'),
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/logout/', LogoutAPI.as_view(), name='api-logout'),
    path('api/perfil/', PerfilAPI.as_view(), name='perfil'),
    path('api/alterar-senha/', AlterarSenhaAPI.as_view(), name='alterar-senha'),
    path('api/redefinir-senha/', RedefinirSenhaAPI.as_view(), name='redefinir-senha'),
    path('api/confirmar-redefinicao-senha/', ConfirmarRedefinicaoSenhaAPI.as_view(), name='confirmar-redefinicao-senha'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Página Inicial
    path('api/home/', HomeAPI.as_view(), name='api-home'),

    # Funcionalidades Dinâmicas
    path('api/', include(api_router)),
]
