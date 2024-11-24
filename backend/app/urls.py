from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração
    path('home/', include('app_optimus.urls')),  # Inclua as rotas da API principal
    path('', RedirectView.as_view(url='/home/', permanent=True)),  # Redireciona para /home
]
