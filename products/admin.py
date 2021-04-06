from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):  # чтобы в товаре отображались фотки
    model = ProductImage
    extra = 0  # сколько дополнительных окон под фотографии по умолчанию


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]  # какие колонки выводить в админке

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)  # регистрируем модель


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # какие колонки выводить в админке
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)  # регистрируем модель


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]  # какие колонки выводить в админке

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)  # регистрируем модель

