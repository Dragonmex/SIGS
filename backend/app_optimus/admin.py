from django.contrib import admin
from .models import CategoriaNoticia, Noticia, CategoriaServico, Servico

admin.site.register(CategoriaNoticia)
admin.site.register(Noticia)
admin.site.register(CategoriaServico)
admin.site.register(Servico)