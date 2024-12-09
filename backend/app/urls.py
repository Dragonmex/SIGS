from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Rotas para APIs de diferentes apps
    path('api/', include('app_optimus.urls')),  # Rotas do app_optimus
    path('api/dados/', include('dados.urls')),  # Rotas do app dados

    # Redirecionamento para página inicial
    path('', RedirectView.as_view(url='/api/home/', permanent=False)),
]
