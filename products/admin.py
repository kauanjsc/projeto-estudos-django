from django.contrib import admin
from .models import Brand, category, Product

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at') # Define os campos exibidos na lista
    search_fields = ('name',) #BUSCAR
    list_filter = ('is_active', ) #LISTAR FILTROS SE ESTIVER ATIVO OU NAO


@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at') # Define os campos exibidos na lista
    search_fields = ('name',) #BUSCAR
    list_filter = ('is_active', ) #LISTAR FILTROS SE ESTIVER ATIVO OU NAO


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price', 'is_active', 'created_at', 'updated_at') # Define os campos exibidos na lista
    search_fields = ('title', 'brand__name', 'category__name') #BUSCAR
    list_filter = ('is_active', 'brand', 'category') #LISTAR FILTROS SE ESTIVER ATIVO OU NAO, MARCA E CATEGORIA