from django.urls import path, include
from app_optimus.routers.router import urlpatterns as router_urls
from app_optimus.views.usuarios import LoginAPI, LogoutAPI, CadastroUsuarioAPI, AlterarSenhaAPI, RedefinirSenhaAPI, ConfirmarRedefinicaoSenhaAPI
from app_optimus.views.home import HomeAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Autenticação
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/logout/', LogoutAPI.as_view(), name='api-logout'),
    path('api/register/', CadastroUsuarioAPI.as_view(), name='api-cadastro'),
    path('api/alterar-senha/', AlterarSenhaAPI.as_view(), name='alterar-senha'),
    path('api/redefinir-senha/', RedefinirSenhaAPI.as_view(), name='redefinir-senha'),
    path('api/confirmar-redefinicao-senha/', ConfirmarRedefinicaoSenhaAPI.as_view(), name='confirmar-redefinicao-senha'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # Pagina Inicial
    path('api/home/', HomeAPI.as_view(), name='api-home'),
    
    # Funcionalidades Dinâmicas
    path('api/', include(router_urls)),
]
