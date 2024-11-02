# app_home_feed/urls.py
from django.urls import path
from .views import (
    BannerListCreateView, BannerDetailView,
    CategoriaListCreateView, CategoriaDetailView,
    LinkRapidoListCreateView, LinkRapidoDetailView,
    NoticiaListCreateView, NoticiaDetailView,
    FuncionalidadeListCreateView, FuncionalidadeDetailView,
    VideoListCreateView, VideoDetailView,
    api_root
)

urlpatterns = [
    path('', api_root, name='api-root'),  # URL raiz da API
    
    path('banners/', BannerListCreateView.as_view(), name='banner-list'),
    path('banners/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),
    
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    
    path('links-rapidos/', LinkRapidoListCreateView.as_view(), name='linkrapido-list'),
    path('links-rapidos/<int:pk>/', LinkRapidoDetailView.as_view(), name='linkrapido-detail'),
    
    path('noticias/', NoticiaListCreateView.as_view(), name='noticia-list'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia-detail'),
    
    path('funcionalidades/', FuncionalidadeListCreateView.as_view(), name='funcionalidade-list'),
    path('funcionalidades/<int:pk>/', FuncionalidadeDetailView.as_view(), name='funcionalidade-detail'),
    
    path('videos/', VideoListCreateView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
]