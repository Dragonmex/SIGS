from django.http import JsonResponse
from dados.models import Person
from django.db.models import Count
from django.shortcuts import render

def gender_data_api(request):
    data = Person.objects.values('gender').annotate(count=Count('gender'))
    response_data = {
        'labels': [entry['gender'] for entry in data],
        'counts': [entry['count'] for entry in data],
    }
    return JsonResponse(response_data)



def gender_chart_view(request):
    return render(request, 'dados/gender_chart.html')
