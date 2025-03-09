import unittest
import subprocess

class TestCLI(unittest.TestCase):
    def test_add_book(self):
        """Test adding a book via CLI"""
        result = subprocess.run(
            ["home-library", "add-book", "--title", "1984", "--author", "George Orwell", "--genre", "Dystopian"],
            capture_output=True, text=True
        )
        self.assertIn("📚 Added: 1984 by George Orwell", result.stdout)

    def test_list_books(self):
        """Test listing books via CLI"""
        result = subprocess.run(["home-library", "list-books"], capture_output=True, text=True)
        self.assertIn("1984 by George Orwell", result.stdout)

    def test_checkout_book(self):
        """Test checking out a book"""
        result = subprocess.run(["home-library", "checkout", "--book_id", "1", "--user_id", "2"], capture_output=True, text=True)
        self.assertIn("✅", result.stdout)

    def test_return_book(self):
        """Test returning a book"""
        result = subprocess.run(["home-library", "return-book", "--book_id", "1"], capture_output=True, text=True)
        self.assertIn("📚 Book returned successfully!", result.stdout)

if __name__ == '__main__':
    unittest.main()
