
from django.contrib import admin
from .models import User, Book, BookDetail, BorrowedBook

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.
    """
    list_display = ['UserID', 'Name', 'Email', 'MembershipDate']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.
    """
    list_display = ['BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre']

@admin.register(BookDetail)
class BookDetailAdmin(admin.ModelAdmin):
    """
    Admin configuration for the BookDetail model.
    """
    list_display = ['book', 'DetailsID', 'NumberOfPages', 'Publisher', 'Language']

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the BorrowedBook model.
    """
    list_display = ['user', 'book', 'BorrowDate', 'ReturnDate', 'status']
