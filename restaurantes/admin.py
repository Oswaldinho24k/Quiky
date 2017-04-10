from django.contrib import admin
from .models import Location, Restaurante

# Register your models here.

admin.site.register(Location)

class RestauranteAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("name",)}

admin.site.register(Restaurante, RestauranteAdmin)
