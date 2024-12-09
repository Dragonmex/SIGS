from django.contrib import admin
from .models import Resident

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'district', 'age', 'income', 'education_level')
    list_filter = ('gender', 'district', 'age_map', 'education_level')
    search_fields = ('first_name', 'last_name', 'district')
