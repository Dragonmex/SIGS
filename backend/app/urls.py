from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_home_feed.urls')),  # Inclua as rotas da API principal
    path('', RedirectView.as_view(url='/api/', permanent=True)),  # Redireciona para /api
]
