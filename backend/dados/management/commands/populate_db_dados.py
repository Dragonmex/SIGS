from django.core.management.base import BaseCommand
from dados.models import Person
import csv

class Command(BaseCommand):
    help = "Popula o banco de dados com os dados fornecidos em um arquivo CSV"

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path',
            type=str,
            help='Caminho do arquivo CSV contendo os dados a serem importados'
        )
        parser.add_argument(
            '--database',
            type=str,
            default='default',
            help='Nome do banco de dados a ser utilizado (padrão: default)'
        )

    def handle(self, *args, **options):
        GENDER_MAP = {
            'Bigender': 'Other',
            'Genderfluid': 'Other',
            'Agender': 'Other',
            'Genderqueer': 'Other',
            'Polygender': 'Other',
            'Non-binary': 'Other',
        }

        file_path = options['file_path']
        database = options['database']

        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    gender = row["gender"]
                    normalized_gender = GENDER_MAP.get(gender, gender)

                    person_data = {
                        "first_name": row["first_name"],
                        "last_name": row["last_name"],
                        "gender": normalized_gender,
                    }
                    Person.objects.using(database).create(**person_data)

            self.stdout.write(self.style.SUCCESS(f"Dados importados com sucesso para o banco {database}!"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro ao importar dados: {str(e)}"))
