

 # Library Management System 

The Library Management System API is a Django Rest Framework (DRF) based web service designed to manage a library's inventory, users, and book borrowing/returning operations through API endpoints.

 # Features

User Management:
  - Retrieve and add, user details.

Book Management:
  - Retrieve, add, update, and delete book details.

  Borrowing/Returning:
  - Borrow books.
  - Return borrowed books and update inventory.

  Book Details:
  - Manage additional details for each book, such as genre, publication year, etc.

 Installation

1. Clone the repository:

   git clone https://github.com/sudip-khanal/library_mgmt_system.git


2. Navigate to the project directory:
   ```bash
   cd library_mgmt_system
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Configure the MySQL database:
   - Update the `DATABASES` setting in `settings.py` with your MySQL database credentials.

7. Run migrations:
   ```bash
   python manage.py migrate
   ```

   Access the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints

Users

- GET /api/users/: Retrieve a list of all users.
- GET /api/users/{id}/: Retrieve user details by user ID.
- POST /api/users/: Create a new user.

Books

- GET /api/books/:Retrieve a list of all books.
- GET /api/books/{id}/: Retrieve book details by book ID.
- POST /api/books/: Create a new book.
- PUT /api/books/{id}/: Update existing book details.
- DELETE /api/books/{id}/: Delete a book by ID.

### Borrowing/Returning

- POST /api/borrow-book/:Borrow a book.
- POST /api/return-book/:Return a borrowed book.

### Book Details

- GET /api/book-detail/: Retrieve a list of all book details.
- GET /api/book-detail/{id}/: Retrieve book detail by ID.
- PUT /api/book-detail/{id}/:Update book detail by ID.
