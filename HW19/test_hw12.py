import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from HW12.bank_deposit import Bank
from HW12.library_system import Book, Reader


class TestBank(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()
        self.client_id = "0000001"

    def test_register_client_positive(self):
        self.bank.register_client(self.client_id, "Siarhei")
        self.assertIn(self.client_id, self.bank.clients)

    def test_register_client_duplicate_error(self):
        self.bank.register_client(self.client_id, "Siarhei")
        with self.assertRaises(ValueError):
            self.bank.register_client(self.client_id, "Another")

    def test_open_deposit_positive(self):
        self.bank.register_client(self.client_id, "Siarhei")
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        self.assertIn(self.client_id, self.bank.deposits)

    def test_open_deposit_unregistered(self):
        with self.assertRaises(ValueError):
            self.bank.open_deposit_account(self.client_id, 1000, 1)

    def test_calculate_interest(self):
        self.bank.register_client(self.client_id, "Siarhei")
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        amount = self.bank.calc_interest_rate(self.client_id)
        self.assertEqual(amount, 1104.71)

    def test_close_deposit(self):
        self.bank.register_client(self.client_id, "Siarhei")
        self.bank.open_deposit_account(self.client_id, 1000, 1)
        self.bank.close_deposit(self.client_id)
        self.assertNotIn(self.client_id, self.bank.deposits)

    def test_close_nonexistent_deposit(self):
        self.bank.register_client(self.client_id, "Siarhei")
        with self.assertRaises(ValueError):
            self.bank.close_deposit(self.client_id)


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.book = Book("The Hobbit", "J.R.R. Tolkien", 400, "0006754023")
        self.reader1 = Reader("Vasya")
        self.reader2 = Reader("Petya")

    def test_reserve_book_positive(self):
        result = self.reader1.reserve_book(self.book)
        self.assertTrue(result)

    def test_reserve_already_reserved(self):
        self.reader1.reserve_book(self.book)
        result = self.reader2.reserve_book(self.book)
        self.assertFalse(result)

    def test_cancel_reserve_positive(self):
        self.reader1.reserve_book(self.book)
        result = self.reader1.cancel_reserve(self.book)
        self.assertTrue(result)

    def test_cancel_reserve_by_another(self):
        self.reader1.reserve_book(self.book)
        result = self.reader2.cancel_reserve(self.book)
        self.assertFalse(result)

    def test_get_book_positive(self):
        result = self.reader1.get_book(self.book)
        self.assertTrue(result)
        self.assertEqual(self.book.issued_to, self.reader1)

    def test_get_reserved_book(self):
        self.reader1.reserve_book(self.book)
        result = self.reader1.get_book(self.book)
        self.assertTrue(result)

    def test_get_book_already_issued(self):
        self.reader1.get_book(self.book)
        result = self.reader2.get_book(self.book)
        self.assertFalse(result)

    def test_return_book_positive(self):
        self.reader1.get_book(self.book)
        result = self.reader1.return_book(self.book)
        self.assertTrue(result)

    def test_return_book_by_another(self):
        self.reader1.get_book(self.book)
        result = self.reader2.return_book(self.book)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
