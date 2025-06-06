from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)

# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # This prevents the display of extra blank forms

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

# Challenge
class BookInline(admin.TabularInline):
    model = Book
    extra = 0 # This prevents the display of extra blank forms
#
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    # Challenge
    inlines = [BookInline]
    # 

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)
#admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    # Challenge
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    #

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


admin.site.register(Language)
