from django.contrib import admin
from .models import AdministrativeSettings

class CustomAdminSettingsList(admin.ModelAdmin):
  model = AdministrativeSettings
  list_display = [
    "name",
    "value",
  ]

admin.site.register(AdministrativeSettings, CustomAdminSettingsList)