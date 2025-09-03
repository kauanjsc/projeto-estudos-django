import csv
from django.http import HttpResponse
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
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=products.csv'
        writer = csv.writer(response)
        writer.writerow(['Titulo', 'Marca', 'Categoria', 'Preço', 'Ativo', 'Criação em', 'Atualizado em'])
        for product in queryset:
            writer.writerow([
                product.title,
                product.brand.name if product.brand else '',
                product.category.name if product.category else '',
                product.price,
                product.is_active,
                product.created_at,
                product.updated_at
            ])
        return response

    export_as_csv.short_description = "Exportar Selecionados como CSV"
