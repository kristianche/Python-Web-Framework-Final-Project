from django.contrib import admin
from .models import Author, Book, Publisher, Profile, ReviewBook


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'created_by']
    list_filter = ['first_name', 'last_name', 'created_by']
    list_per_page = 30
    search_fields = ('first_name', 'last_name', 'created_by')
    ordering = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'created_by']
    list_filter = ['author', 'genre']
    search_fields = ('title', 'author', 'created_by')
    list_per_page = 30
    ordering = ('title',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'office', 'created_by']
    list_filter = ['created_by', 'office']
    list_per_page = 30
    search_fields = ('name', 'created_by')
    ordering = ('name',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'country', 'sex']
    list_filter = ['user', 'city', 'country', 'sex']
    list_per_page = 30
    ordering = ('user', )
    search_fields = ('sex', 'city', 'country')


@admin.register(ReviewBook)
class ReviewBook(admin.ModelAdmin):
    list_display = ['author', 'book', 'grade']
    list_filter = ['author', 'book']
    ordering = ('author',)
    list_per_page = 30
    search_fields = ('author', 'book')