from django.urls import path
from .views.categoria import CategoriaListView, CategoriaDetailView
from .views.banner import BannerListView, BannerDetailView
from .views.acesso_informacao import AcessoInformacaoListView, AcessoInformacaoDetailView

urlpatterns = [
    #Categoria
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),

    #Banner
    path('banners/', BannerListView.as_view(), name='banner-list'),
    path('banners/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),

    # Acesso a Informação
    path('acessos-informacao/', AcessoInformacaoListView.as_view(), name='acesso-informacao-list'),
    path('acessos-informacao/<int:pk>/', AcessoInformacaoDetailView.as_view(), name='acesso-informacao-detail'),
]
