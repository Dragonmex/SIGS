from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feed/', include('app_optimus.urls')),  # Inclua as rotas da API principal
    path('', RedirectView.as_view(url='feed/', permanent=True)),  # Redireciona para /feed
]
