from django.urls import path, include
from app_optimus.routers import api_router
from app_optimus.views.usuarios import LoginAPI, LogoutAPI, CadastroUsuarioAPI, AlterarSenhaAPI, RedefinirSenhaAPI, ConfirmarRedefinicaoSenhaAPI
from app_optimus.views.Home import HomeAPI
from app_optimus.views.perfil import PerfilAPI
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import OuvidoriaViewSet

router = DefaultRouter()
router.register(r'ouvidorias', OuvidoriaViewSet, basename='ouvidoria')

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
    #path('admin/', admin.site.urls),
    path('api/ouvidoria/', include(router.urls)),


    # Página Inicial
    path('api/home/', HomeAPI.as_view(), name='api-home'),

    # Funcionalidades Dinâmicas
    path('api/', include(api_router)),
]
