# Author: Madi Cho-Richmond
# Github username: chorichm
# Date: 2023 October 12
# Description: The goal of this assignment is to write a library simulator
# using multple classes. You will have private classes of LibraryItem, Patron
# and Library classes, and the three classes that inherit from LibraryItem (Book, Album and Movie).
# To access them outside of the class, you will use get_ and set_ methods followed by the data member.
# You will be able to keep track of patrons, their check outs or on shelves, and sum fines.


class Book:
    """Represents a book in the library."""

    def __init__(self, book_id: int, title: str, author: str, genre: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out_by = None  # User ID of borrower

    def __repr__(self):
        return f"{self.title} by {self.author} ({'Checked Out' if self.checked_out_by else 'Available'})"


class User:
    """Represents a user who borrows books from the library."""

    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.books_checked_out = []

    def __repr__(self):
        return f"User: {self.name}, Borrowed Books: {len(self.books_checked_out)}"


class Library:
    """Main class to manage books and users in the home library system."""

    def __init__(self):
        # Delay the import to avoid circular import issues
        from home_library.database import Database

        self.db = Database()

    def add_book(self, title, author, genre):
        """Add a new book to the library database."""
        self.db.insert_book(title, author, genre)
        print(f"Added book: {title} by {author}")

    def list_books(self):
        """Retrieve and display all books."""
        books = self.db.get_all_books()
        return books  # Returns a list of books for CLI or other interfaces

    def check_out_book(self, book_id, user_id):
        """Check out a book for a user if available."""
        book = self.db.get_book(book_id)
        if book and not book[4]:  # Column 4 = checked_out_by
            self.db.return_book(book_id, user_id)
            print(f"Checked out '{book[1]}' to user {user_id}.")  # book[1] = title
        else:
            print("Book is either checked out or does not exist.")

    def return_book(self, book_id):
        """Return a book to the library."""
        self.db.return_book(book_id)
        print("Book returned successfully!")

    def apply_fines(self):
        """Check overdue books and apply late fees."""
        import datetime

        overdue_books = self.db.get_overdue_books()
        for book in overdue_books:
            fine = (
                datetime.datetime.now()
                - datetime.datetime.strptime(book[5], "%Y-%m-%d")
            ).days * 0.50
            self.db.add_fine(book[4], fine)  # book[4] = user_id
            print(f"Applied ${fine:.2f} fine to user {book[4]}.")
