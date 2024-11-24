from django.core.management.base import BaseCommand
from app_optimus.models import Categoria, Noticia, Video, LinkRapido, Banner, ImagemBanner
from django.utils import timezone

class Command(BaseCommand):
    help = "Popula o banco de dados com dados de exemplo para as tabelas principais"

    def handle(self, *args, **options):
        # Limpar dados antigos
        ImagemBanner.objects.all().delete()
        Banner.objects.all().delete()
        LinkRapido.objects.all().delete()
        Video.objects.all().delete()
        Noticia.objects.all().delete()
        Categoria.objects.all().delete()

        # Criando as categorias
        categorias_data = [
            {"nome": "Governo"},
            {"nome": "Educação"},
            {"nome": "Saúde"},
            {"nome": "Segurança"},
            {"nome": "Cultura"},
        ]

        for categoria_data in categorias_data:
            Categoria.objects.create(nome=categoria_data["nome"])

        # Criando os banners com 5 imagens cada
        banners_data = [
            {"titulo": "Leilão de Bens Públicos"},
            {"titulo": "Segurança Pública"},
            {"titulo": "Restituição de IPVA"},
            {"titulo": "Educação no Estado"},
            {"titulo": "Eventos Culturais"},
        ]

        for banner_data in banners_data:
            banner = Banner.objects.create(titulo=banner_data["titulo"])
            for i in range(5):  # Criar 5 imagens para cada banner
                ImagemBanner.objects.create(
                    banner=banner,
                    imagem=f"banners/exemplo_{banner.id}_{i+1}.jpg"  # Exemplo de caminho para a imagem
                )

        # Criando links rápidos
        links_rapidos_data = [
            {"titulo": "Portal da Transparência", "url": "https://www.portaltransparencia.gov.br"},
            {"titulo": "Sistema Único de Saúde (SUS)", "url": "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/sistema-unico-de-saude-sus"},
            {"titulo": "Serviços de Ouvidoria", "url": "https://www.gov.br/ouvidorias"},
            {"titulo": "Consulta de Benefícios", "url": "https://www.consultabeneficios.gov.br"},
            {"titulo": "Agendamento de Serviços", "url": "https://www.agendamentoservicos.gov.br"},
        ]

        for link_data in links_rapidos_data:
            LinkRapido.objects.create(
                titulo=link_data["titulo"],
                url=link_data["url"]
            )

        # Criando vídeos
        videos_data = [
            {"titulo": "Como Funciona o Sistema de Saúde", "url": "https://www.youtube.com/watch?v=exemplo1"},
            {"titulo": "Novo Serviço de Atendimento Rápido", "url": "https://www.youtube.com/watch?v=exemplo2"},
            {"titulo": "Programa de Educação", "url": "https://www.youtube.com/watch?v=exemplo3"},
            {"titulo": "Segurança Pública em Ação", "url": "https://www.youtube.com/watch?v=exemplo4"},
            {"titulo": "Preservação Ambiental", "url": "https://www.youtube.com/watch?v=exemplo5"},
        ]

        for video_data in videos_data:
            Video.objects.create(
                titulo=video_data["titulo"],
                url=video_data["url"]
            )

        # Criando 20 notícias realistas
        noticias_data = [
            {"titulo": "Governo Anuncia Novo Plano de Infraestrutura", "conteudo": "O governo anunciou um novo plano de infraestrutura que promete modernizar rodovias e ferrovias em todo o país."},
            {"titulo": "Escolas Públicas Recebem Investimento Recorde", "conteudo": "As escolas públicas receberam um investimento recorde para melhorias nas instalações e novos equipamentos tecnológicos."},
            {"titulo": "Campanha de Vacinação Supera Expectativas", "conteudo": "A campanha de vacinação contra a gripe superou as expectativas, com milhões de pessoas imunizadas na primeira semana."},
            {"titulo": "Polícia Lança Operação para Combater o Crime Organizado", "conteudo": "Uma grande operação policial foi lançada para desmantelar uma rede de crime organizado, com várias prisões realizadas."},
            {"titulo": "Festival Cultural Atrae Milhares de Visitantes", "conteudo": "O festival cultural deste ano atraiu milhares de visitantes, com apresentações artísticas e culinária típica."},
            {"titulo": "Novo Hospital é Inaugurado na Região Metropolitana", "conteudo": "O novo hospital conta com tecnologia de ponta e promete melhorar o atendimento na região metropolitana."},
            {"titulo": "Prefeitura Lança Programa de Reciclagem", "conteudo": "A prefeitura lançou um novo programa de reciclagem para incentivar a sustentabilidade nas comunidades."},
            {"titulo": "Concurso Público Anunciado para o Setor de Segurança", "conteudo": "O governo anunciou um novo concurso público com vagas para o setor de segurança e salários atrativos."},
            {"titulo": "Campanha de Doação de Sangue Acontece Neste Fim de Semana", "conteudo": "A campanha de doação de sangue acontecerá em diversos pontos da cidade, com expectativa de alta adesão."},
            {"titulo": "Universidades Federais Recebem Novos Equipamentos", "conteudo": "O governo federal investiu em novos equipamentos para modernizar as universidades e melhorar a pesquisa acadêmica."},
            {"titulo": "Evento Esportivo Regional Atrai Atletas de Todo o País", "conteudo": "O evento esportivo regional trouxe atletas de todo o Brasil para competir em diversas modalidades."},
            {"titulo": "Prefeitura Inicia Obras de Pavimentação em Bairros", "conteudo": "As obras de pavimentação começaram em diversos bairros e devem ser concluídas até o próximo semestre."},
            {"titulo": "Governo Anuncia Redução de Impostos para Pequenas Empresas", "conteudo": "Pequenas empresas terão uma redução de impostos, o que deve impulsionar a economia local."},
            {"titulo": "Seminário de Tecnologia Discutirá Inovações Futuras", "conteudo": "Especialistas em tecnologia se reunirão para discutir inovações e o futuro do setor no país."},
            {"titulo": "Festival Gastronômico Apresenta Pratos Típicos Regionais", "conteudo": "O festival gastronômico apresentará pratos típicos da culinária regional, com chefs renomados participando."},
            {"titulo": "Projeto de Lei para Preservação Ambiental é Aprovado", "conteudo": "O projeto de lei que visa proteger áreas ambientais foi aprovado e entrará em vigor no próximo mês."},
            {"titulo": "Comunidade Recebe Nova Área de Lazer", "conteudo": "A comunidade local agora conta com uma nova área de lazer, com parques, quadras esportivas e ciclovias."},
            {"titulo": "Alunos de Escolas Públicas Participam de Programa de Artes", "conteudo": "O programa de artes visa incluir atividades culturais no currículo das escolas públicas, incentivando a criatividade."},
            {"titulo": "Estado Investe em Novos Veículos para a Polícia", "conteudo": "O estado investiu em uma frota de novos veículos para melhorar o patrulhamento e a segurança nas ruas."},
            {"titulo": "Exposição de Arte Contemporânea Acontece no Centro Cultural", "conteudo": "A exposição de arte contemporânea contará com obras de artistas locais e internacionais, aberta ao público gratuitamente."},
        ]

        categorias = Categoria.objects.all()
        for i, noticia_data in enumerate(noticias_data):
            categoria = categorias[i % len(categorias)]  # Distribuindo as notícias pelas categorias
            noticia = Noticia.objects.create(
                titulo=noticia_data["titulo"],
                conteudo=noticia_data["conteudo"],
                categoria=categoria,
                data_publicacao=timezone.now().date()
            )

        # Associando notícias relacionadas automaticamente com base na mesma categoria
        for noticia in Noticia.objects.all():
            relacionadas = Noticia.objects.filter(categoria=noticia.categoria).exclude(id=noticia.id)
            noticia.noticias_relacionadas.set(relacionadas)

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso, com IDs reiniciados!"))
