from django.contrib import admin
from books.models import Book, CustomUser
# Register your models here.


class BookAdmin(admin.ModelAdmin):
     list_display = ("book_title", "book_author")
admin.site.register(CustomUser)
admin.site.register(Book, BookAdmin)