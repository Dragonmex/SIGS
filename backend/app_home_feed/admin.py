from django.contrib import admin
from .models import Banner, Categoria, Funcionalidade, LinkRapido, Noticia, Video

# Registrando cada modelo para aparecer na interface do admin
admin.site.register(Banner)
admin.site.register(Categoria)
admin.site.register(Funcionalidade)
admin.site.register(LinkRapido)
admin.site.register(Noticia)
admin.site.register(Video)
