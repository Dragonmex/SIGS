from django.db import models

class Resident(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    age_map = models.CharField(max_length=50)
    income = models.PositiveIntegerField()
    education_level = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
