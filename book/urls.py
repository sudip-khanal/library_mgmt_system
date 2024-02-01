from django.urls import path
from .views import UserApiView, BookApiView, BookDetailApiView, BorrowBookApiView, ReturnBookApiView,BorrowedBookListView

urlpatterns = [
    # User API endpoints
    path('users/', UserApiView.as_view(), name='users-list'),             # List all users or create a new user
    path('users/<int:pk>/', UserApiView.as_view(), name='user-detail'),   # Retrieve a specific user

    # Book API endpoints
    path('books/', BookApiView.as_view(), name='books-list'),             # List all books or create a new book
    path('books/<int:pk>/', BookApiView.as_view(), name='book-detail'),   # Retrieve, update, or delete a specific book

    # BookDetail API endpoints
    path('book-detail/', BookDetailApiView.as_view(), name='book-details-list'),              # List all book details or create a new book detail
    path('book-detail/<int:pk>/', BookDetailApiView.as_view(), name='book-detail-detail'),   # Retrieve and update a specific book detail

    # BorrowBook API endpoint
    path('borrow-book/', BorrowBookApiView.as_view(), name='borrow-book'),   # Borrow a book

    # ReturnBook API endpoint
    path('return-book/', ReturnBookApiView.as_view(), name='return-book'),   # Return a borrowed book
    # list of all borrowed book API endpoint
    path('borrowed-books-list/', BorrowedBookListView.as_view(), name='borrowed-books-list'),
]
