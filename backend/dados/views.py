from django.db.models import Count, Avg, F
from django.http import JsonResponse
from .models import Resident
from django.db.models import Count, Avg, Min, Max


def income_distribution_api(request):
    """API para retornar a distribuição de renda por bairro."""
    data = Resident.objects.values("district").annotate(
        avg_income=Avg("income"),
        min_income=Min("income"),
        max_income=Max("income"),
    )
    response_data = {
        "labels": [entry["district"] for entry in data],
        "avg_incomes": [entry["avg_income"] for entry in data],
        "min_incomes": [entry["min_income"] for entry in data],
        "max_incomes": [entry["max_income"] for entry in data],
    }
    return JsonResponse(response_data)


def education_distribution_api(request):
    """API para retornar a distribuição de níveis de escolaridade por bairro."""
    valid_education_levels = [
        "Analfabeto",
        "Ensino Fundamental Incompleto",
        "Ensino Fundamental Completo",
        "Ensino Médio Incompleto",
        "Ensino Médio Completo",
        "Ensino Superior Incompleto",
        "Ensino Superior Completo",
    ]
    data = (
        Resident.objects.filter(education_level__in=valid_education_levels)
        .values("district", "education_level")
        .annotate(count=Count("id"))
    )
    response_data = {}
    for entry in data:
        district = entry["district"]
        education = entry["education_level"]
        if district not in response_data:
            response_data[district] = {}
        response_data[district][education] = entry["count"]
    return JsonResponse(response_data)


def district_distribution_api(request):
    """API para retornar a distribuição por distrito."""
    data = Resident.objects.values("district").annotate(count=Count("id"))
    response_data = {
        "labels": [entry["district"] for entry in data],
        "counts": [entry["count"] for entry in data],
    }
    return JsonResponse(response_data)


def gender_distribution_api(request):
    """API para retornar a distribuição por gênero."""
    allowed_genders = ["Male", "Female", "Non-binary", "Agender", "Genderqueer"]
    data = (
        Resident.objects.filter(gender__in=allowed_genders)
        .values("gender")
        .annotate(count=Count("gender"))
    )
    response_data = {
        "labels": [entry["gender"] for entry in data],
        "counts": [entry["count"] for entry in data],
    }
    return JsonResponse(response_data)
