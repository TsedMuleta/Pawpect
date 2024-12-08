from django.contrib import admin
from .models import PetFood, Category

class PetFoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'created_at')  # Show category in the list
    search_fields = ('name',)
    list_filter = ('created_at', 'category')  # Add category filter
    ordering = ('created_at',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display name and description of category
    search_fields = ('name',)  # Allow searching by category name

# Register the models with the admin
admin.site.register(PetFood, PetFoodAdmin)
admin.site.register(Category, CategoryAdmin)
