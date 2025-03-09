from datetime import datetime, timedelta


def calculate_due_date():
    """Calculate the due date for a borrowed book."""
    return (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")


def format_book(book):
    """Format book output nicely."""
    return f"{book['id']}: {book['title']} by {book['author']} (Genre: {book['genre']})"
