from django.contrib import admin
from .models import City, Shops, Street


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street',
                    'number_home_shop', 'opening_time',
                    'closing_time')


class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


admin.site.register(City)
admin.site.register(Shops, ShopAdmin)
admin.site.register(Street, StreetAdmin)
