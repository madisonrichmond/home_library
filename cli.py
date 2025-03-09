import argparse


def main():
    """Command-line interface for the Home Library system."""
    from home_library.library import (
        Library,
    )  # Import inside function to prevent circular import

    library = Library()

    parser = argparse.ArgumentParser(description="Home Library CLI")
    parser.add_argument("--list-books", action="store_true", help="List all books")
    parser.add_argument(
        "--add-book",
        nargs=3,
        metavar=("title", "author", "genre"),
        help="Add a new book",
    )
    parser.add_argument(
        "--checkout", nargs=2, metavar=("book_id", "user_id"), help="Check out a book"
    )
    parser.add_argument(
        "--return-book", metavar="book_id", help="Return a book"
    )  # Changed from --return
    parser.add_argument(
        "--import-books", action="store_true", help="Import books from CSV"
    )

    args = parser.parse_args()

    if args.list_books:
        books = library.list_books()
        print("\n📚 **Books in the Library:**")
        for book in books:
            book_id, title, author, genre, checked_out_by, due_date = book
            status = (
                f"Checked out by User {checked_out_by}"
                if checked_out_by
                else "✅ Available"
            )
            print(f"{book_id}. {title} by {author} [{genre}] - {status}")

    elif args.add_book:
        title, author, genre = args.add_book
        library.add_book(title, author, genre)
        print(f"Book '{title}' added successfully!")

    elif args.checkout:
        book_id, user_id = map(int, args.checkout)
        library.check_out_book(book_id, user_id)

    elif args.return_book:
        book_id = int(args.return_book)
        print(library.return_book(book_id))  # ✅ Always prints message

    elif args.import_books:
        result = library.db.import_books_from_csv()  # ✅ Call CSV import function
        print(result)  # ✅ Print success/failure message


if __name__ == "__main__":
    main()
