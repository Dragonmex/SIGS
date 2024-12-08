from django.urls import path
from .views import gender_data_api
from .views import gender_chart_view

urlpatterns = [
    path('api/gender-data/', gender_data_api, name='gender_data_api'),
    path('gender-chart/', gender_chart_view, name='gender_chart'),
]

