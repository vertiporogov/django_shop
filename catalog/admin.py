from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class DogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'price', 'name', 'category', )
    list_filter = ('category', )
    search_fields = ('name', 'description',)
