from django.urls import path
from .views import FeedView, NoticiasListView, NoticiaDetailView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),  # URL raiz da API
    path('noticias/', NoticiasListView.as_view(), name='noticias-list'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia-detail'),  # URL para a notícia detalhada

]
