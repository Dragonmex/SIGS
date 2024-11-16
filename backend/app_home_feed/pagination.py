from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Número padrão de itens por página
    page_size_query_param = 'page_size'  # Permite que o front-end especifique o tamanho da página
    max_page_size = 100  # Limita o número máximo de itens por página
