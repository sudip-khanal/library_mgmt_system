from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model representing library users

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    MembershipDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Name


# Model representing books in the library
class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)
    def __str__(self):
        return self.Title

# Model representing additional details of each book (1-1 relationship with Book)
class BookDetail(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    DetailsID = models.AutoField(primary_key=True)
    NumberOfPages = models.PositiveIntegerField()
    Publisher = models.CharField(max_length=255)
    Language = models.CharField(max_length=50)

# Model representing borrowed books and due dates (1-M relationship with User)

class BorrowedBook(models.Model):
    STATUS_CHOICES = [
        ('', 'Choose an option'),
        ('Borrowed', 'Borrowed'),
        ('Returned', 'Returned'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='')

    def __str__(self):
        return f"{self.user} - {self.book}"
    


