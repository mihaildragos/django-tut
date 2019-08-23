from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
# admin.site.register(BookInstance)


class BookAdminInline(admin.TabularInline):
    model = Book
    extra = 0


# We can register models for how the information is displayed in the admin panel by adding models and registering them with admin.site.register() syntax
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookAdminInline]

admin.site.register(Author, AuthorAdmin)

# To be able to add associated records at the same time in the detailed view
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0 # to have NO spare book instances by default

# Or we can add a decorator @register which does the same thing as admin.site.register()
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline] # To be able to add associated records at the same time in the detailed view

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('get_full_book_name', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Details', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )