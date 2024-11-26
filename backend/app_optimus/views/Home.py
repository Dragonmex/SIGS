from django.shortcuts import render
from app_optimus.models import Servico, Noticia, CategoriaNoticia

def home_page(request):
    servicos = Servico.objects.filter(status=True).order_by('-data_criacao')[:6]
    noticias = Noticia.objects.order_by('-data_publicacao')[:6]
    categorias_noticias = CategoriaNoticia.objects.all()
    return render(request, 'home.html', {
        'servicos': servicos,
        'noticias': noticias,
        'categorias_noticias': categorias_noticias,
    })

def home_view(request):
    usuario_id = request.session.get('usuario_id')
    return render(request, 'home.html', {'usuario_id': usuario_id})
