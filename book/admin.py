from django.contrib import admin

# Register your models here.

from book.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']

admin.site.register(Book, BookAdmin)
