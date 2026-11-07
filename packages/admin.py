from django.contrib import admin
from .models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("package_name", "destination", "duration", "price")
    search_fields = ("package_name", "destination")
