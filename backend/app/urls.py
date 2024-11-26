from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/', permanent=False)),  # Redireciona a raiz para o login
    path('', include('app_optimus.urls')),  # Inclui as rotas do app
]
