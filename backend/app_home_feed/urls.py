from django.urls import path
from .views import FeedView, NoticiasListView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),  # URL raiz da API
    path('noticias/', NoticiasListView.as_view(), name='noticias-list'),
]
