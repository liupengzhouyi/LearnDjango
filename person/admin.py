from django.contrib import admin

# Register your models here.

from person.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'maxBloodValue', 'maxMagicValue', 'maxCardNumbers']

admin.site.register(Person, PersonAdmin)

