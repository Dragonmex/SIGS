import csv
from django.core.management.base import BaseCommand
from dados.models import Resident

class Command(BaseCommand):
    help = 'Importa os dados demográficos de um arquivo CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        file_path = 'C:/Users/Davi Jr/Desktop/dados/dados_demograficos.csv'

        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            residents = [
                Resident(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    gender=row['gender'],
                    district=row['district'],
                    age=int(row['age']),
                    age_map=row['age_map'],
                    income=float(row['income']),
                    education_level=row['education_level']
                )
                for row in reader
            ]

            Resident.objects.bulk_create(residents)

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
