from django.urls import path
from app_optimus.views import LoginAPI, LogoutAPI, HomeAPI, CadastroUsuarioAPI, NoticiaDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # AUTENTICAÇÃO DE USUARIOS
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/logout/', LogoutAPI.as_view(), name='api-logout'),
    path('api/home/', HomeAPI.as_view(), name='api-home'),
    path('api/register/', CadastroUsuarioAPI.as_view(), name='api-cadastro'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # VISUALIZAÇÃO EM DETALHES - NOTICIAS
    path('api/noticia/<int:noticia_id>/', NoticiaDetailView.as_view(), name='api-noticia-detail'),

]
