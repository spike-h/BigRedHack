from django.contrib import admin

from .models import brand

class brandAdmin(admin.ModelAdmin):
    list_display = ("name", "emissions",)

admin.site.register(brand, brandAdmin)
