from django.contrib import admin
from .models import (
    Product,
    CompanyManufacturing,
    ShelfLife
)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_display', 'company_manufacturing', 'composition', 'shelf_life', 'quantity']
    readonly_fields = ['image_display']  # Делаем поле с изображением только для чтения

    def image_display(self, obj):
        # Возвращает HTML-код для отображения изображения в админке
        if obj.image:
            return '<img src="{}" width="100" />'.format(obj.image.url)
        else:
            return 'No image'

    # Добавляем заголовок для столбца с изображением
    image_display.short_description = 'Image'

admin.site.register(Product, ProductAdmin)

class CompanyManufacturindAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(CompanyManufacturing,CompanyManufacturindAdmin)

class ShelfLifeAdmin(admin.ModelAdmin):
    list_display = ['period']
admin.site.register(ShelfLife,ShelfLifeAdmin)