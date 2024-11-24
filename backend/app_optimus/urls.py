from django.urls import path
from .views import FeedView, NoticiasListView, NoticiaDetailView, BannerDetailView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),  # URL raiz da API
    path('banners/<int:pk>/', BannerDetailView.as_view(), name='banner-detail'),  # Inclua <int:pk>
    path('noticias/', NoticiasListView.as_view(), name='noticias-list'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia-detail'),
    

]
