import sqlite3
import csv
import os
from datetime import datetime, timedelta
from home_library.config import DATABASE_NAME, LOAN_DAYS


class Database:
    def __init__(self, db_name=DATABASE_NAME):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Creates necessary tables for books and users."""
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                genre TEXT,
                checked_out_by INTEGER,
                due_date TEXT
            )
        """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        """
        )
        self.conn.commit()

    def import_books_from_csv(self, csv_file="data/books.csv"):
        """Imports books from a CSV file into the database."""
        if not os.path.exists(csv_file):
            print(f"❌ Error: CSV file '{csv_file}' not found.")
            return

        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.cursor.execute(
                    """
                    INSERT INTO books (title, author, genre) 
                    VALUES (?, ?, ?)
                """,
                    (row["title"], row["author"], row["genre"]),
                )
        self.conn.commit()
        print("✅ Books imported successfully from CSV.")

    def insert_book(self, title, author, genre):
        """Insert a new book into the database."""
        self.cursor.execute(
            "INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",
            (title, author, genre),
        )
        self.conn.commit()

    def get_all_books(self):
        """Retrieves all books from the database."""
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def get_book(self, book_id):
        """Gets a book by its ID."""
        self.cursor.execute("SELECT * FROM books WHERE id=?", (book_id,))
        return self.cursor.fetchone()

    def checkout_book(self, book_id, user_id):
        """Handles checking out a book, updating the due date."""
        book = self.get_book(book_id)
        if not book:
            return "❌ Error: Book not found."
        if book[4] is not None:
            return f"❌ Error: Book '{book[1]}' is already checked out."

        due_date = (datetime.now() + timedelta(days=LOAN_DAYS)).strftime("%Y-%m-%d")
        self.cursor.execute(
            "UPDATE books SET checked_out_by=?, due_date=? WHERE id=?",
            (user_id, due_date, book_id),
        )
        self.conn.commit()
        return f"✅ '{book[1]}' checked out to User {user_id}. Due back: {due_date}."

    def return_book(self, book_id):
        """Handles returning a book and clearing the due date."""
        book = self.get_book(book_id)
        if not book:
            return "❌ Error: Book not found."
        if book[4] is None:
            return f"⚠ '{book[1]}' is already in the library."

        self.cursor.execute(
            "UPDATE books SET checked_out_by=NULL, due_date=NULL WHERE id=?", (book_id,)
        )
        self.conn.commit()
        return f"📚 '{book[1]}' returned successfully."

    def pay_fine(self, user_id, amount):
        """Allows users to pay a fine (if a fine system is implemented)."""
        # You might need a fines table if implementing fines tracking
        return f"✅ Fine of ${amount:.2f} paid by User {user_id}."

    def close(self):
        """Closes the database connection."""
        self.conn.close()
