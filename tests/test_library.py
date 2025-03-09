import unittest
from home_library.home_library.library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book("Test Book", "Test Author", "Fiction")

    def test_add_book(self):
        books = self.lib.db.get_all_books()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]['title'], "Test Book")

    def test_checkout_book(self):
        self.lib.check_out_book(1, 1)
        book = self.lib.db.get_book(1)
        self.assertIsNotNone(book['checked_out_by'])

if __name__ == '__main__':
    unittest.main()

