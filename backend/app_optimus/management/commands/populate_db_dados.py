from app_optimus.models.dados import Person
import csv

class Command(BaseCommand):
    help = "Popula o banco de dados com os dados fornecidos em um arquivo CSV"

    def handle(self, *args, **options):
        GENDER_MAP = {
            'Bigender': 'Other',
            'Genderfluid': 'Other',
            'Agender': 'Other',
            'Genderqueer': 'Other',
            'Polygender': 'Other',
            'Non-binary': 'Other',
        }

        # Caminho do arquivo CSV
        file_path = options["file_path"]

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Normalizar o gênero
                gender = row["gender"]
                normalized_gender = GENDER_MAP.get(gender, gender)

                # Criar pessoa
                person_data = {
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "gender": normalized_gender,
                }
                Person.objects.create(**person_data)

        self.stdout.write(self.style.SUCCESS("Dados importados com sucesso!"))
