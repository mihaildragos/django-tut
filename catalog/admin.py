from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
# admin.site.register(BookInstance)

# We can register models for how the information is displayed in the admin panel by adding models and registering them with admin.site.register() syntax
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)

# Or we can add a decorator @register which does the same thing as admin.site.register()

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    pass