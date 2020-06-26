from django.contrib import admin

# Register your models here.


from cardRelitionship.models import CardRelitionship

class CardRelitionshipAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'PersonId', 'MonsterId', 'cardId', 'using']

admin.site.register(CardRelitionship, CardRelitionshipAdmin)
