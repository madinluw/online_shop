from django.contrib import admin
from .models import Category, NewBalance, Images, OrderItem, Order


class ImagesInline(admin.TabularInline):
    model = Images


@admin.register(NewBalance)
class New_Balance(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ('title', 'price',)


admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)
# admin.site.register(Images)