from django.core.management.base import BaseCommand
from app_optimus.models.funcionalidades_models import CategoriaNoticia, CategoriaServico, Noticia, Servico, ServicoEtapa
from django.utils import timezone


class Command(BaseCommand):
    help = "Popula o banco de dados 'conteudos_db' com dados de exemplo para as tabelas principais"

    def handle(self, *args, **options):
        # Limpar dados antigos
        Servico.objects.all().delete()
        Noticia.objects.all().delete()
        CategoriaServico.objects.all().delete()
        CategoriaNoticia.objects.all().delete()

        # Criando categorias de notícias
        categorias_noticias_data = [
            {"nome": "Política", "descricao": "Notícias relacionadas ao governo e administração pública", "slug": "politica"},
            {"nome": "Educação", "descricao": "Atualizações sobre o setor educacional", "slug": "educacao"},
            {"nome": "Saúde", "descricao": "Notícias do setor de saúde pública e privada", "slug": "saude"},
            {"nome": "Esporte", "descricao": "Novidades sobre esportes e competições", "slug": "esporte"},
            {"nome": "Cultura", "descricao": "Eventos culturais e artísticos", "slug": "cultura"},
        ]

        categorias_noticias = [
            CategoriaNoticia.objects.create(**categoria_data)
            for categoria_data in categorias_noticias_data
        ]

        # Criando categorias de serviços
        categorias_servicos_data = [
            {"nome": "Saúde", "descricao": "Serviços relacionados à saúde pública", "slug": "saude"},
            {"nome": "Educação", "descricao": "Serviços voltados ao ensino e formação", "slug": "educacao"},
            {"nome": "Transporte", "descricao": "Serviços de transporte público e mobilidade urbana", "slug": "transporte"},
            {"nome": "Segurança", "descricao": "Serviços relacionados à segurança pública", "slug": "seguranca"},
            {"nome": "Assistência Social", "descricao": "Programas de apoio social", "slug": "assistencia-social"},
            {"nome": "Habitação", "descricao": "Serviços voltados à moradia e urbanização", "slug": "habitacao"},
            {"nome": "Cultura", "descricao": "Serviços culturais e eventos artísticos", "slug": "cultura"},
            {"nome": "Esporte", "descricao": "Programas esportivos e recreativos", "slug": "esporte"},
            {"nome": "Meio Ambiente", "descricao": "Serviços relacionados à preservação ambiental", "slug": "meio-ambiente"},
            {"nome": "Trabalho e Emprego", "descricao": "Programas de incentivo ao trabalho e geração de empregos", "slug": "trabalho-emprego"},
            {"nome": "Turismo", "descricao": "Iniciativas para promover o turismo local", "slug": "turismo"},
            {"nome": "Fazenda", "descricao": "Serviços de arrecadação e gestão tributária", "slug": "fazenda"},
            {"nome": "Infraestrutura", "descricao": "Serviços de obras públicas e manutenção urbana", "slug": "infraestrutura"},
            {"nome": "Tecnologia", "descricao": "Inovação tecnológica e inclusão digital", "slug": "tecnologia"},
            {"nome": "Direitos Humanos", "descricao": "Apoio à inclusão e garantia de direitos", "slug": "direitos-humanos"},
            {"nome": "Ouvidoria", "descricao": "Serviços para escuta e resolução de demandas dos cidadãos", "slug": "ouvidoria"},
            {"nome": "Saneamento Básico", "descricao": "Serviços de abastecimento de água e tratamento de esgoto", "slug": "saneamento-basico"},
            {"nome": "Agricultura", "descricao": "Incentivo à produção agrícola e apoio rural", "slug": "agricultura"},
            {"nome": "Indústria e Comércio", "descricao": "Apoio ao desenvolvimento industrial e comercial", "slug": "industria-comercio"},
            {"nome": "Defesa Civil", "descricao": "Prevenção e resposta a desastres e emergências", "slug": "defesa-civil"},
        ]

        categorias_servicos = [
            CategoriaServico.objects.create(**categoria_data)
            for categoria_data in categorias_servicos_data
        ]

        # Criando 10 notícias
        noticias_data = [
    {
        "titulo": "Governo Municipal Lança Novo Programa de Saúde Preventiva",
        "resumo": "Iniciativa busca atender mais de 50 mil moradores com foco em prevenção.",
        "conteudo": "O programa de saúde preventiva lançado pela Prefeitura inclui campanhas de vacinação, check-ups gratuitos em postos de saúde e palestras sobre bem-estar. O objetivo é reduzir os casos de doenças evitáveis e melhorar a qualidade de vida da população. Segundo o prefeito, a ação também visa desafogar o sistema de saúde da cidade.",
        "autor": "Equipe de Comunicação",
        "data_publicacao": timezone.now(),
        "imagem": "https://images.unsplash.com/photo-1495364141860-b0d03eccd065?q=80&w=2676&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
        "titulo": "Escolas Municipais Recebem Investimento de R$ 5 Milhões",
        "resumo": "Recursos serão destinados para melhorias em infraestrutura e aquisição de materiais didáticos.",
        "conteudo": "A Prefeitura anunciou um investimento recorde em educação para reformar escolas, construir novas salas de aula e adquirir equipamentos tecnológicos. A ação beneficiará cerca de 30 mil alunos da rede municipal. Segundo a secretária de educação, as reformas começarão ainda este semestre.",
        "autor": "Assessoria de Imprensa",
        "data_publicacao": timezone.now(),
        "imagem": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?q=80&w=2670&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
        "titulo": "Prefeitura Organiza Festival Cultural com Entrada Gratuita",
        "resumo": "Evento contará com apresentações musicais, exposições de arte e feira gastronômica.",
        "conteudo": "O Festival Cultural, que acontecerá na praça central da cidade, reunirá artistas locais e regionais. A iniciativa tem como objetivo promover a cultura e valorizar os talentos locais. Estima-se que cerca de 10 mil pessoas compareçam ao evento durante o final de semana.",
        "autor": "Departamento de Cultura",
        "data_publicacao": timezone.now(),
        "imagem": "https://images.unsplash.com/flagged/photo-1572213426852-0e4ed8f41ff6?q=80&w=2674&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
        "titulo": "Projeto de Arborização Planta Mil Árvores em Bairros Carentes",
        "resumo": "Ação faz parte do programa de sustentabilidade da Prefeitura.",
        "conteudo": "A Prefeitura iniciou o projeto de arborização urbana com o plantio de mil árvores em bairros com baixa cobertura vegetal. A ação busca melhorar a qualidade do ar e proporcionar mais áreas verdes para a população. Moradores também receberam orientações sobre cuidados com as mudas.",
        "autor": "Secretaria de Meio Ambiente",
        "data_publicacao": timezone.now(),
        "imagem": "https://www.pensarcursos.com.br/blog/wp-content/uploads/2024/12/Concurso-Pub-3-2-750x430.png",
    },
    {
        "titulo": "Nova Linha de Ônibus Reduz Tempo de Deslocamento em 30%",
        "resumo": "Moradores de bairros afastados agora contam com transporte público mais eficiente.",
        "conteudo": "A Prefeitura anunciou a criação de uma nova linha de ônibus para atender moradores de áreas periféricas. Com trajetos mais curtos e maior frequência, a medida promete reduzir significativamente o tempo de deslocamento até o centro da cidade.",
        "autor": "Assessoria de Transporte",
        "data_publicacao": timezone.now(),
        "imagem": "https://www.cosemssp.org.br/wp-content/uploads/2019/06/CAMPANHA-INFLUENZA-01.jpg",
    },
    {
        "titulo": "Campanha de Vacinação Contra Gripe Atinge 80% do Público-Alvo",
        "resumo": "Mais de 20 mil pessoas foram vacinadas em menos de uma semana.",
        "conteudo": "A Prefeitura comemorou o sucesso da campanha de vacinação contra a gripe. Postos de saúde e unidades móveis foram mobilizados para imunizar moradores em diversas regiões. A meta de vacinar 100% do público-alvo deve ser alcançada nos próximos dias.",
        "autor": "Secretaria de Saúde",
        "data_publicacao": timezone.now(),
        "imagem": "https://i0.wp.com/diariodotransporte.com.br/wp-content/uploads/2022/07/WhatsApp-Image-2022-07-30-at-09.52.28-1-e1659186466945.jpeg?fit=799%2C599&ssl=1",
    },
    {
        "titulo": "Concurso Público Abre 200 Vagas para Diversas Áreas",
        "resumo": "Oportunidades abrangem saúde, educação e segurança pública.",
        "conteudo": "A Prefeitura abriu inscrições para um novo concurso público com salários que variam de R$ 1.500 a R$ 8.000. Os candidatos terão até o final do mês para se inscrever. O edital completo está disponível no site oficial da Prefeitura.",
        "autor": "Departamento de Recursos Humanos",
        "data_publicacao": timezone.now(),
        "imagem": "https://rioplantas.com.br/wp-content/uploads/2021/04/arborizacao-urbana.jpg",
    },
    {
        "titulo": "Mutirão de Limpeza Remove 50 Toneladas de Resíduos",
        "resumo": "Ação envolveu mais de 200 voluntários em diversos bairros da cidade.",
        "conteudo": "Com o apoio de moradores e organizações locais, a Prefeitura realizou um mutirão para recolher resíduos e promover a conscientização sobre descarte adequado de lixo. Além da coleta, os participantes receberam orientações sobre reciclagem e sustentabilidade.",
        "autor": "Secretaria de Infraestrutura",
        "data_publicacao": timezone.now(),
        "imagem": "https://www.pmvc.ba.gov.br/wp-content/uploads/sem-t%C3%ADtulo-0725-1.jpg",
    },
    {
        "titulo": "Prefeitura Reduz Taxa de Licenciamento para Pequenos Negócios",
        "resumo": "Medida busca incentivar o empreendedorismo na cidade.",
        "conteudo": "Empreendedores locais comemoraram a redução da taxa de licenciamento para pequenos negócios, anunciada pela Prefeitura. A medida é válida para empresas com faturamento anual de até R$ 120 mil e pretende estimular a economia local.",
        "autor": "Secretaria de Desenvolvimento Econômico",
        "data_publicacao": timezone.now(),
        "imagem": "https://www.lucasdorioverde.mt.gov.br/arquivos/noticias/13127/g/pref_lrv.jpg",
    },
    {
        "titulo": "Obras de Pavimentação São Concluídas em Tempo Recorde",
        "resumo": "Moradores de quatro bairros agora têm acesso a ruas asfaltadas.",
        "conteudo": "A Prefeitura entregou as obras de pavimentação em quatro bairros, melhorando a mobilidade urbana e valorizando os imóveis da região. As obras, iniciadas há três meses, foram concluídas antes do prazo previsto.",
        "autor": "Assessoria de Infraestrutura",
        "data_publicacao": timezone.now(),
        "imagem": "https://saoluis.ma.gov.br/midias/2021/grandes/up_ag_34929_9d6dc053-03b2-8d00-2334-75ffaba3a7eb.jpg",
    },
    ]


        for i, noticia_data in enumerate(noticias_data):
            noticia_data["categoria"] = categorias_noticias[i % len(categorias_noticias)]  # Garantir que cada notícia tenha categoria
            Noticia.objects.create(**noticia_data)

        # Criando 05 serviços
        servicos_data = [
    {
        "nome": "Consulta Médica",
        "descricao": "Agendamento de consultas médicas em unidades de saúde.",
        "categoria": CategoriaServico.objects.get(slug="saude"),
        "etapas": [
            {"nome": "Agendamento", "descricao": "Realize o agendamento da consulta na unidade de saúde."},
            {"nome": "Confirmação de Documentos", "descricao": "Leve os documentos necessários no dia da consulta."},
            {"nome": "Consulta com Médico", "descricao": "Compareça à unidade para a consulta agendada."},
        ],
    },
    {
        "nome": "Matrícula Escolar",
        "descricao": "Serviço de matrícula para escolas públicas municipais.",
        "categoria": CategoriaServico.objects.get(slug="educacao"),
        "etapas": [
            {"nome": "Preenchimento do Cadastro", "descricao": "Forneça os dados do aluno e responsáveis."},
            {"nome": "Envio de Documentos", "descricao": "Envie cópias dos documentos necessários para matrícula."},
            {"nome": "Confirmação da Matrícula", "descricao": "Receba a confirmação da matrícula pela secretaria."},
        ],
    },
    {
        "nome": "Bilhete Único",
        "descricao": "Emissão de cartões para transporte público com integração tarifária.",
        "categoria": CategoriaServico.objects.get(slug="transporte"),
        "etapas": [
            {"nome": "Cadastro no Sistema", "descricao": "Realize o cadastro no sistema de transporte público."},
            {"nome": "Envio de Foto e Documentos", "descricao": "Envie uma foto recente e documentos de identificação."},
            {"nome": "Recebimento do Bilhete", "descricao": "Aguarde a entrega do bilhete único no endereço informado."},
        ],
    },
    {
        "nome": "Patrulhamento de Bairros",
        "descricao": "Rondas de segurança realizadas pela guarda municipal.",
        "categoria": CategoriaServico.objects.get(slug="seguranca"),
        "etapas": [
            {"nome": "Solicitação de Patrulhamento", "descricao": "Registre uma solicitação na central de segurança."},
            {"nome": "Avaliação da Solicitação", "descricao": "A central avalia e designa a ronda para o bairro."},
            {"nome": "Realização da Ronda", "descricao": "Equipe realiza a ronda no bairro em horários definidos."},
        ],
    },
    {
        "nome": "Cadastro para Auxílio Social",
        "descricao": "Inscrição em programas de apoio a famílias em situação de vulnerabilidade.",
        "categoria": CategoriaServico.objects.get(slug="assistencia-social"),
        "etapas": [
            {"nome": "Preenchimento do Cadastro", "descricao": "Informe os dados pessoais e familiares."},
            {"nome": "Entrevista com Assistente Social", "descricao": "Agende e participe da entrevista de avaliação."},
            {"nome": "Aprovação e Recebimento do Benefício", "descricao": "Aguarde a aprovação e receba o benefício."},
        ],
    },
]

        for servico_data in servicos_data:
            # Criação do serviço
            etapas = servico_data.pop("etapas")  # Remove etapas do dicionário principal
            servico = Servico.objects.create(**servico_data)

        # Adicionando etapas para o serviço
            for ordem, etapa_data in enumerate(etapas, start=1):
                ServicoEtapa.objects.create(
                    servico=servico,
                    nome=etapa_data["nome"],
                    descricao=etapa_data["descricao"],
                    ordem=ordem,
                )

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
