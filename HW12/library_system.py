

from typing import Optional


class Book:
    def __init__(self, book_name: str, author: str, num_pages: int, isbn: str):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved_by: Optional["Reader"] = None
        self.issued_to: Optional["Reader"] = None

    def reserve(self, reader: "Reader") -> bool:
        if self.reserved_by or self.issued_to:
            return False
        self.reserved_by = reader
        return True

    def cancel_reserve(self, reader: "Reader") -> bool:
        if self.reserved_by != reader:
            return False
        self.reserved_by = None
        return True

    def get_book(self, reader: "Reader") -> bool:
        if self.issued_to or (self.reserved_by and self.reserved_by != reader):
            return False
        self.issued_to = reader
        self.reserved_by = None
        return True

    def return_book(self, reader: "Reader") -> bool:
        if self.issued_to != reader:
            return False
        self.issued_to = None
        return True


class Reader:
    def __init__(self, name: str):
        self.name = name

    def reserve_book(self, book_obj: Book) -> bool:
        return book_obj.reserve(self)

    def cancel_reserve(self, book_obj: Book) -> bool:
        return book_obj.cancel_reserve(self)

    def get_book(self, book_obj: Book) -> bool:
        return book_obj.get_book(self)

    def return_book(self, book_obj: Book) -> bool:
        return book_obj.return_book(self)


if __name__ == "__main__":
    test_book = Book(
        book_name="The Hobbit",
        author="J.R.R. Tolkien",
        num_pages=400,
        isbn="0006754023"
    )
    vasya = Reader("Vasya")
    petya = Reader("Petya")

    assert vasya.reserve_book(test_book)
    assert not petya.reserve_book(test_book)
    assert vasya.cancel_reserve(test_book)
    assert petya.reserve_book(test_book)
    assert not vasya.get_book(test_book)
    assert petya.get_book(test_book)
    assert not vasya.return_book(test_book)
    assert petya.return_book(test_book)
    assert vasya.get_book(test_book)
