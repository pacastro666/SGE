from django.contrib import admin
from . import models


class ProductdAdmin(admin.ModelAdmin):
    list_display = ('title', 'serie_number',)
    search_fields = ('title',)


admin.site.register(models.Product, ProductdAdmin)
