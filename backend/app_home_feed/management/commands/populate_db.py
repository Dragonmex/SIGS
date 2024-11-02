from django.core.management.base import BaseCommand
from app_home_feed.models import Categoria, Noticia, Video, LinkRapido, Funcionalidade, Banner
from django.utils import timezone

class Command(BaseCommand):
    help = "Popula o banco de dados com dados de exemplo para as tabelas principais"

    def handle(self, *args, **options):
        # Criando as categorias, se não existirem
        categorias_data = [
            {"nome": "Governo", "descricao": "Informações e atualizações sobre o governo estadual."},
            {"nome": "Educação", "descricao": "Notícias e programas educacionais."},
            {"nome": "Saúde", "descricao": "Informações sobre saúde pública e campanhas de vacinação."},
            {"nome": "Segurança", "descricao": "Notícias sobre segurança pública e ações da polícia."},
            {"nome": "Cultura", "descricao": "Eventos culturais e informações sobre patrimônio."},
            {"nome": "Esporte", "descricao": "Eventos esportivos e programas de incentivo ao esporte."},
            {"nome": "Meio Ambiente", "descricao": "Projetos de preservação e notícias ambientais."},
            {"nome": "Tecnologia", "descricao": "Inovações e desenvolvimento tecnológico."},
            {"nome": "Infraestrutura", "descricao": "Projetos de infraestrutura e urbanização."},
            {"nome": "Transporte", "descricao": "Informações sobre transporte público e infraestrutura."},
        ]
        
        for categoria_data in categorias_data:
            Categoria.objects.get_or_create(
                nome=categoria_data["nome"],
                defaults={"descricao": categoria_data["descricao"]}
            )

        # Criando os banners, se não existirem
        banners_data = [
            {
                "titulo": "Leilão de Bens Públicos",
                "imagem": "banners/leilao_bens.jpg",
                "descricao": "Governo do Estado vai leiloar bens públicos avaliados em R$ 1,8 milhão.",
                "link": "https://exemplo.com/leilao"
            },
            {
                "titulo": "Segurança Pública",
                "imagem": "banners/seguranca_publica.jpg",
                "descricao": "Estado encaminha PL para Alba buscando criação de 2.400 cargos na Polícia Civil.",
                "link": "https://exemplo.com/seguranca"
            },
            {
                "titulo": "Restituição de IPVA",
                "imagem": "banners/restituicao_ipva.jpg",
                "descricao": "Restituição de IPVA já pode ser feita pelo portal ba.gov.br.",
                "link": "https://exemplo.com/ipva"
            },
            {
                "titulo": "Educação no Estado",
                "imagem": "banners/educacao_estado.jpg",
                "descricao": "Novos programas de incentivo à educação básica e superior.",
                "link": "https://exemplo.com/educacao"
            },
            {
                "titulo": "Eventos Culturais",
                "imagem": "banners/eventos_culturais.jpg",
                "descricao": "Confira os próximos eventos culturais promovidos pelo Estado.",
                "link": "https://exemplo.com/eventos"
            },
        ]

        for banner_data in banners_data:
            Banner.objects.get_or_create(
                titulo=banner_data["titulo"],
                defaults={
                    "imagem": banner_data["imagem"],
                    "descricao": banner_data["descricao"],
                    "link": banner_data["link"]
                }
            )

        # Criando uma notícia, se não existir
        categoria_educacao = Categoria.objects.get(nome="Educação")
        categoria_saude = Categoria.objects.get(nome="Saúde")
        
        Noticia.objects.get_or_create(
            titulo="Nova Escola Municipal Inaugurada",
            defaults={
                "conteudo": "Foi inaugurado uma nova escola no centro para atender a população.",
                "categoria": categoria_educacao,
                "data_publicacao": timezone.now().date()
            }
        )
        
        Noticia.objects.get_or_create(
            titulo="Campanha de Vacinação Começa Hoje",
            defaults={
                "conteudo": "A campanha de vacinação contra a gripe começa hoje e irá até o final do mês.",
                "categoria": categoria_saude,
                "data_publicacao": timezone.now().date()
            }
        )

        # Criando vídeos, se não existirem
        Video.objects.get_or_create(
            titulo="Como Funciona o Sistema de Saúde",
            defaults={
                "descricao": "Uma explicação completa sobre o funcionamento do SUS.",
                "url": "https://www.youtube.com/watch?v=exemplo1"
            }
        )
        
        Video.objects.get_or_create(
            titulo="Novo Serviço de Atendimento Rápido",
            defaults={
                "descricao": "Conheça o novo serviço de atendimento rápido para emergências.",
                "url": "https://www.youtube.com/watch?v=exemplo2"
            }
        )

        # Criando links rápidos, se não existirem
        LinkRapido.objects.get_or_create(
            titulo="Portal da Transparência",
            defaults={
                "url": "https://www.portaltransparencia.gov.br",
                "descricao": "Acesse informações sobre gastos públicos."
            }
        )
        
        LinkRapido.objects.get_or_create(
            titulo="Sistema Único de Saúde (SUS)",
            defaults={
                "url": "https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/sistema-unico-de-saude-sus",
                "descricao": "Informações sobre o SUS e atendimento à saúde."
            }
        )
        
        LinkRapido.objects.get_or_create(
            titulo="Serviços de Ouvidoria",
            defaults={
                "url": "https://www.gov.br/ouvidorias",
                "descricao": "Acesso para denúncias, sugestões ou reclamações sobre serviços públicos."
            }
        )

        # Criando funcionalidades, se não existirem
        funcionalidades_data = [
            {"nome": "Home Feed", "descricao": "Área principal com atualizações e novidades sobre serviços e projetos.", "rota": "/api/home-feed", "icone": "icons/home_icon.png"},
            {"nome": "Construção de Serviços", "descricao": "Acompanhe o desenvolvimento e implementação de novos serviços.", "rota": "/api/construcao-servicos", "icone": "icons/servicos_icon.png"},
            {"nome": "Status dos Serviços", "descricao": "Exibe o status dos serviços públicos em andamento.", "rota": "/api/status-servicos", "icone": "icons/status_icon.png"},
            {"nome": "Análise de Dados", "descricao": "Ferramenta de visualização e análise de dados sobre saúde pública.", "rota": "/api/analise-dados", "icone": "icons/analise_icon.png"},
            {"nome": "Observatório de Dados", "descricao": "Repositório de dados estatísticos e relatórios para insights sobre políticas.", "rota": "/api/observatorio-dados", "icone": "icons/observatorio_icon.png"},
            {"nome": "Ouvidoria", "descricao": "Canal para reclamações, denúncias e sugestões dos cidadãos.", "rota": "/api/ouvidoria", "icone": "icons/ouvidoria_icon.png"},
            {"nome": "Ecosistema de Inovação", "descricao": "Área dedicada ao incentivo à inovação, com projetos em desenvolvimento.", "rota": "/api/ecossistema-inovacao", "icone": "icons/inovacao_icon.png"},
        ]

        for funcionalidade_data in funcionalidades_data:
            Funcionalidade.objects.get_or_create(
                nome=funcionalidade_data["nome"],
                defaults={
                    "descricao": funcionalidade_data["descricao"],
                    "rota": funcionalidade_data["rota"],
                    "icone": funcionalidade_data["icone"]
                }
            )

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso, sem duplicações!"))
