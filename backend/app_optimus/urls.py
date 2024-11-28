from django.urls import path
from app_optimus.views import LoginAPI, LogoutAPI, HomeAPI, CadastroUsuarioAPI

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/logout/', LogoutAPI.as_view(), name='api-logout'),
    path('api/home/', HomeAPI.as_view(), name='api-home'),
    path('api/register/', CadastroUsuarioAPI.as_view(), name='api-cadastro'),
]
