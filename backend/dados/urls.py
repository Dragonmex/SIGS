from django.urls import path
from .views import income_distribution_api, education_distribution_api, district_distribution_api, gender_distribution_api

urlpatterns = [
    path('gender-distribution/', gender_distribution_api, name='gender_distribution_api'),
    path('income-distribution/', income_distribution_api, name='income_distribution_api'),
    path('education-distribution/', education_distribution_api, name='education_distribution_api'),
    path('district-distribution/', district_distribution_api, name='district_distribution_api'),
    
]