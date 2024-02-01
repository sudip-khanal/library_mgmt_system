# importing necessary modules and resources
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Book, BorrowedBook, BookDetail
from .serilizers import Userserializer, Bookserializer, BorrowBookserializer, BookDetailserializer, ReturnBookserializer
from rest_framework.decorators import action
from rest_framework import serializers  # Import serializers module from the framework
from rest_framework.permissions import IsAuthenticated


class UserApiView(APIView):
    
    # API view for User model.
    
    def get(self, request, pk=None):
       
        # Retrieve user(s) data based on the presence of a primary key.
        
        if pk is not None:
            user = User.objects.get(pk=pk)
            serializer = Userserializer(user)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = Userserializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        
        # Create a new user.
        
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookApiView(APIView):    # API view for Book model.

    def get(self, request, pk=None):
      
        # Retrieve book(s) data based on the presence of a primary key.
      
        if pk is not None:
            book = Book.objects.get(pk=pk)
            serializer = Bookserializer(book)
            return Response(serializer.data)
        else:
            books = Book.objects.all()
            serializer = Bookserializer(books, many=True)
            return Response(serializer.data)

    def post(self, request):
       
        # Create a new book object or instance.
       
        serializer = Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        
        # Update a book instance based on the provided primary key.
        
        if pk is not None:
            book = Book.objects.get(pk=pk)
            serializer = Bookserializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        
        # Delete a book instance or all books if no primary key is provided.
        
        if pk is not None:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Book.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class BookDetailApiView(APIView):
    
    # API view for BookDetail model.
    
    
    def get(self, request, pk=None):
        
        # Retrieve book detail(s) data.
        
        if pk is not None:
            book_detail = BookDetail.objects.get(pk=pk)
            serializer = BookDetailserializer(book_detail)
            return Response(serializer.data)
        else:
            books_detail = BookDetail.objects.all()
            serializer = BookDetailserializer(books_detail, many=True)
            return Response(serializer.data)
        
    def post(self, request):
       
        # Create a book details object or instance.
       
        serializer = BookDetailserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
       
        # Update a book detail instance based on the provided primary key.
        
        if pk is not None:
            book_detail = BookDetail.objects.get(pk=pk)
            serializer = BookDetailserializer(book_detail, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid book ID.'}, status=status.HTTP_400_BAD_REQUEST)


class BorrowBookApiView(APIView):
   
    # API view for borrowing a book.
   
    serializer_class = BorrowBookserializer

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('UserID')
        serializer = self.serializer_class(data=request.data, context={'request': request, 'user': user_id})

        try:
            serializer.is_valid(raise_exception=True)
            borrow = serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

class ReturnBookApiView(APIView):
    serializer_class = ReturnBookserializer

    def post(self, request, *args, **kwargs):
        # the borrowed_book_id in the request or URL parameters
        borrowed_book_id = request.data.get('user')  # Update with your actual parameter

        try:
            borrowed_book_instance = BorrowedBook.objects.get(id=borrowed_book_id)
        except BorrowedBook.DoesNotExist:
            return Response({'error': 'Borrowed book not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(instance=borrowed_book_instance, data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
            serializer.update(instance=borrowed_book_instance, validated_data=request.data)
            return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class BorrowedBookListView(APIView):
    """
    API view for the list of all borrowed books.
    """

    def get(self, request):
        # Filter books with status 'Borrowed'
        borrowed_books = BorrowedBook.objects.filter(status='Borrowed')
        
        # Serialize the filtered books
        serializer = BorrowBookserializer(borrowed_books, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)