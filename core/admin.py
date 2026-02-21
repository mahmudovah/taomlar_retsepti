from django.contrib import admin
from .models import Ingredient, Meal, Comment
# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity','unit','created_at','updated_at']
    list_display_links =['name']
    readonly_fields = ['id','created_at','updated_at']
    fields = ['id', 'name', 'quantity','unit','created_at','updated_at']
    search_fields = ['name', 'unit']
    list_filter = ['quantity','created_at','updated_at']


class MealAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'status', 'created_at','updated_at']
    list_display_links = ['name']
    readonly_fields = ['id','created_at','updated_at']

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(Comment)