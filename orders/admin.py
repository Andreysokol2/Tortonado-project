from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):      #чтобы в товаре отображались фотки
    model = ProductInOrder
    extra = 0   #сколько дополнительных окон под фотографии по умолчанию


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]  # какие колонки выводить в админке
    inlines = [ProductImageInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)  # регистрируем модель


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]  # какие колонки выводить в админке

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)  # регистрируем модель

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]  # какие колонки выводить в админке

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)  # регистрируем модель

class ProductInBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]  # какие колонки выводить в админке

    class Meta:
        model = ProductInBasket


admin.site.register(ProductInBasket, ProductInBasketAdmin)  # регистрируем модель
