from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_optimus.urls')),  # Inclui todas as rotas do app com o prefixo 'api/'
    path('', include('dados.urls')),
    path('', RedirectView.as_view(url='/api/home/', permanent=False)),  # Redireciona para o login
]
