from django.contrib import admin

# Register your models here.

from monster.models import Monster

class MonsterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'maxBloodValue', 'maxMagicValue', 'maxCardNumbers']

admin.site.register(Monster, MonsterAdmin)
