from django.contrib import admin
from .models import Category, Product, StockMovement

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity', 'date', 'user')
    list_filter = ('movement_type', 'date')
    search_fields = ('product__name',)
