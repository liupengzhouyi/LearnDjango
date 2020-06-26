from django.contrib import admin

# Register your models here.

from card.models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'funcName', 'consume', 'returnBloodValue', 'returnMagicValue', 'damageValue', 'protect']

admin.site.register(Card, CardAdmin)

