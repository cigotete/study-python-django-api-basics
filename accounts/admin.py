from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlparse, urlunparse

class CustomUserAdmin(UserAdmin):
  add_form = CustomUserCreationForm
  form = CustomUserChangeForm
  model = CustomUser
  list_display = [
    "email",
    "username",
    "name",
    "is_staff",
    "admin_url",
    "get_admin_url_link",
    ]
  fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
  add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)

  def admin_url(self, obj):
    return reverse("admin:accounts_customuser_change", args=[obj.id])
  
  def get_admin_url_link(self, obj):
    url = urlparse(self.admin_url(obj))
    url = url._replace(query=url.query.replace("pk=", ""))  # Modifica la query string
    new_url = urlunparse(url)  # Reconstruye la URL completa
    return format_html(
        f"<a href='{new_url}'>Editar</a>",
    )

  list_display_links = [
        "username",
        "get_admin_url_link",
    ]

admin.site.register(CustomUser, CustomUserAdmin)