from django.urls import path
from app_optimus.views import login_view, cadastro_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),  # Página de login
    path('cadastro/', cadastro_view, name='cadastro_usuario'),  # Página de cadastro
    path('home/', home_view, name='home'),  # Página inicial após login
]
