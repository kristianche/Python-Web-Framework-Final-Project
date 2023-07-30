from django.contrib import admin
from .models import Author, Book, Publisher, Profile, ReviewBook


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date_book']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']


@admin.register(ReviewBook)
class ReviewBook(admin.ModelAdmin):
    list_display = ['author', 'book', 'grade']