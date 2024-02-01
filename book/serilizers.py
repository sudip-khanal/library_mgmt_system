from rest_framework import serializers
from .models import User, Book, BookDetail, BorrowedBook

class Userserializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['UserID', 'Name', 'Email', 'MembershipDate']


class Bookserializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    class Meta:
        model = Book
        fields = ['BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre']


class BookDetailserializer(serializers.ModelSerializer):
    """
    Serializer for the BookDetail model.
    """
    class Meta:
        model = BookDetail
        fields = ['book', 'DetailsID', 'NumberOfPages', 'Publisher', 'Language']

class BorrowBookserializer(serializers.ModelSerializer):
    """
    Serializer for the BorrowedBook model when borrowing a book.
    """
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BorrowedBook
        fields = ['user', 'book', 'BorrowDate']

    def save(self):
        """
        Save method to handle book borrowing.
        """
        user_id = self.validated_data.get('user')
        book = self.validated_data['book']

        # Fetch the user based on the provided user ID
        user, _ = User.objects.get_or_create(UserID=user_id)

        # Associate BorrowedBook with the fetched user
        borrow, created = BorrowedBook.objects.get_or_create(user=user, status='Borrowed')

        # Ensure the book is not already borrowed
        if BorrowedBook.objects.filter(book=book, status='Borrowed').exists():
            raise serializers.ValidationError("This Book is already Borrowed")

        # Update the status to 'Borrowed'
        borrow.status = 'Borrowed'
        borrow.book = book
        borrow.save()
        return borrow

class ReturnBookserializer(serializers.ModelSerializer):
    """
    Serializer for the BorrowedBook model when returning a borrowed book.
    """
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BorrowedBook
        fields = ['user', 'book', 'BorrowDate', 'ReturnDate', 'status']

    def update(self, instance, validated_data):
        """
        Update method to handle returning a borrowed book.
        """
        instance.ReturnDate = validated_data.get('ReturnDate', instance.ReturnDate)
        instance.status = 'Returned'
        instance.save()
        return instance
